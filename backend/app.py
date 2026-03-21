from __future__ import annotations

from html import unescape
import json
import logging
import re
from typing import Any
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request


app = Flask(__name__)
logger = logging.getLogger(__name__)
http = requests.Session()
http.headers.update(
    {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "no-cache",
        "DNT": "1",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
    }
)

_WHITESPACE_RE = re.compile(r"\s+")
_ISO_DURATION_RE = re.compile(
    r"^P"
    r"(?:(?P<days>\d+)D)?"
    r"(?:T"
    r"(?:(?P<hours>\d+)H)?"
    r"(?:(?P<minutes>\d+)M)?"
    r"(?:(?P<seconds>\d+)S)?"
    r")?$",
    re.IGNORECASE,
)


def _corsify(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return response


@app.after_request
def add_cors_headers(response):
    return _corsify(response)


@app.route("/api/import-recipe-url", methods=["OPTIONS"])
def import_recipe_url_options():
    return _corsify(app.make_default_options_response())


def _validate_url(url: str) -> str:
    candidate = str(url or "").strip()
    parsed = urlparse(candidate)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("Enter a valid http(s) recipe URL.")
    return candidate


def _flatten_json_ld(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        out: list[dict[str, Any]] = []
        if isinstance(payload.get("@graph"), list):
            for item in payload["@graph"]:
                out.extend(_flatten_json_ld(item))
            return out
        return [payload]

    if isinstance(payload, list):
        out: list[dict[str, Any]] = []
        for item in payload:
            out.extend(_flatten_json_ld(item))
        return out

    return []


def _is_recipe_type(value: Any) -> bool:
    if isinstance(value, str):
        return value.lower() == "recipe"
    if isinstance(value, list):
        return any(_is_recipe_type(item) for item in value)
    return False


def _clean_text(value: str) -> str:
    decoded = unescape(str(value or "")).replace("\xa0", " ")
    return _WHITESPACE_RE.sub(" ", decoded).strip()


def _format_duration(value: str) -> str:
    raw = _clean_text(value)
    if not raw:
        return ""

    match = _ISO_DURATION_RE.match(raw)
    if not match:
        return raw

    days = int(match.group("days") or 0)
    hours = int(match.group("hours") or 0)
    minutes = int(match.group("minutes") or 0)
    seconds = int(match.group("seconds") or 0)

    total_minutes = days * 24 * 60 + hours * 60 + minutes
    if seconds >= 30:
        total_minutes += 1

    if total_minutes <= 0:
        return raw

    whole_hours, remaining_minutes = divmod(total_minutes, 60)
    parts: list[str] = []

    if whole_hours:
        parts.append(f"{whole_hours} hr" + ("" if whole_hours == 1 else "s"))
    if remaining_minutes:
        parts.append(f"{remaining_minutes} min" + ("" if remaining_minutes == 1 else "s"))

    return " ".join(parts) if parts else "0 mins"


def _text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return _clean_text(value)
    if isinstance(value, (int, float)):
        return _clean_text(str(value))
    if isinstance(value, dict):
        return _text(value.get("text") or value.get("name") or value.get("@value"))
    return ""


def _image_url(value: Any) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        for item in value:
            found = _image_url(item)
            if found:
                return found
        return ""
    if isinstance(value, dict):
        return _text(value.get("url") or value.get("contentUrl"))
    return ""


def _string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        out: list[str] = []
        for item in value:
            item_text = _text(item)
            if item_text:
                out.append(item_text)
        return out

    item_text = _text(value)
    return [item_text] if item_text else []


def _instruction_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        text = value.strip()
        return [text] if text else []
    if isinstance(value, list):
        out: list[str] = []
        for item in value:
            out.extend(_instruction_list(item))
        return out
    if isinstance(value, dict):
        if isinstance(value.get("itemListElement"), list):
            return _instruction_list(value["itemListElement"])
        text = _text(value.get("text") or value.get("name"))
        return [text] if text else []
    return []


def _looks_like_block_page(response: requests.Response) -> bool:
    text = (response.text or "")[:4000].lower()
    markers = (
        "captcha",
        "verify you are human",
        "access denied",
        "attention required",
        "request blocked",
        "cf-chl",
        "/cdn-cgi/challenge",
        "bot detection",
    )
    return any(marker in text for marker in markers)


def _response_snippet(response: requests.Response, limit: int = 220) -> str:
    text = (response.text or "")[:4000]
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace("\x00", "")
    if len(text) > limit:
        return text[:limit] + "..."
    return text


def _log_fetch_failure(stage: str, target_url: str, exc: requests.RequestException) -> None:
    response = getattr(exc, "response", None)
    if response is not None:
        logger.warning(
            "Recipe import %s failed for %s: status=%s final_url=%s content_type=%r server=%r block_page=%s snippet=%r",
            stage,
            target_url,
            response.status_code,
            response.url,
            response.headers.get("content-type"),
            response.headers.get("server"),
            _looks_like_block_page(response),
            _response_snippet(response),
        )
        return

    if isinstance(exc, requests.Timeout):
        logger.warning("Recipe import %s timed out for %s", stage, target_url)
        return

    logger.warning("Recipe import %s failed for %s: %s", stage, target_url, exc)


def import_recipe_from_url(url: str) -> dict[str, Any] | None:
    target_url = _validate_url(url)
    parsed = urlparse(target_url)
    origin = f"{parsed.scheme}://{parsed.netloc}"

    try:
        response = http.get(
            target_url,
            timeout=25,
            headers={
                "Referer": origin,
            },
        )
        response.raise_for_status()
    except requests.RequestException as first_exc:
        _log_fetch_failure("direct fetch", target_url, first_exc)
        logger.info("Recipe import attempting warm-up retry for %s", origin)

        try:
            http.get(
                origin,
                timeout=15,
                headers={
                    "Referer": origin,
                },
            )
        except requests.RequestException as warmup_exc:
            _log_fetch_failure("warm-up request", origin, warmup_exc)

        try:
            response = http.get(
                target_url,
                timeout=25,
                headers={
                    "Referer": origin,
                },
            )
            response.raise_for_status()
            logger.info("Recipe import retry succeeded for %s", target_url)
        except requests.RequestException as retry_exc:
            _log_fetch_failure("retry fetch", target_url, retry_exc)
            raise retry_exc

    soup = BeautifulSoup(response.text, "html.parser")
    scripts = soup.find_all("script", attrs={"type": "application/ld+json"})

    for script in scripts:
        raw = script.string or script.get_text() or ""
        raw = raw.strip()
        if not raw:
            continue

        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            continue

        for node in _flatten_json_ld(payload):
            if not _is_recipe_type(node.get("@type")):
                continue

            recipe = {
                "title": _text(node.get("name")),
                "source_url": target_url,
                "servings": _text(node.get("recipeYield")),
                "prep_time": _format_duration(_text(node.get("prepTime"))),
                "cook_time": _format_duration(_text(node.get("cookTime"))),
                "total_time": _format_duration(_text(node.get("totalTime"))),
                "image": _image_url(node.get("image")),
                "ingredients": _string_list(node.get("recipeIngredient")),
                "directions": _instruction_list(node.get("recipeInstructions")),
            }

            if recipe["title"] or recipe["ingredients"] or recipe["directions"]:
                return recipe

    return None


@app.post("/api/import-recipe-url")
def import_recipe_url():
    payload = request.get_json(silent=True) or {}
    url = str(payload.get("url") or "").strip()

    if not url:
        return jsonify({"error": "Missing url"}), 400

    try:
        recipe = import_recipe_from_url(url)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    except requests.RequestException as exc:
        logger.warning("Recipe import fetch failed for %s: %s", url, exc)
        return jsonify({"error": "Failed to fetch recipe URL."}), 502
    except Exception:
        return jsonify({"error": "Recipe import failed."}), 500

    if not recipe:
        return jsonify({"error": "No recipe JSON-LD data found at that URL."}), 404

    return jsonify({"recipe": recipe})


if __name__ == "__main__":
    # Local run:
    #   cd backend
    #   python3 -m flask --app app run --port 8787
    app.run(host="127.0.0.1", port=8787, debug=True)
