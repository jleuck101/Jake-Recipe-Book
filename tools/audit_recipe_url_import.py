#!/usr/bin/env python3
"""
Usage:
  python3 tools/audit_recipe_url_import.py input.csv output.csv

Input CSV columns:
  site,recipe,url
"""

from __future__ import annotations

import csv
import re
import sys

import requests


ENDPOINT = "https://jake-recipe-book-import.onrender.com/api/import-recipe-url"
OUTPUT_COLUMNS = [
    "site",
    "recipe",
    "url",
    "status",
    "http_ok",
    "title_ok",
    "image_ok",
    "ingredients_count",
    "directions_count",
    "total_time_present",
    "html_entities_found",
    "needs_manual_review",
    "notes",
]

HTML_ENTITY_RE = re.compile(r"&(?:[a-zA-Z][a-zA-Z0-9]+|#\d+|#x[0-9a-fA-F]+);")


def as_bool(value: bool) -> str:
    return "true" if value else "false"


def has_html_entities(value: str) -> bool:
    text = str(value or "")
    return bool(HTML_ENTITY_RE.search(text))


def count_items(value) -> int:
    if not isinstance(value, list):
        return 0
    return len([item for item in value if str(item or "").strip()])


def build_row(source_row: dict[str, str], response: requests.Response | None, payload: dict | None, error_note: str = "") -> dict[str, str]:
    recipe = (payload or {}).get("recipe") if isinstance(payload, dict) else None
    recipe = recipe if isinstance(recipe, dict) else {}

    title = str(recipe.get("title") or "").strip()
    image = str(recipe.get("image") or "").strip()
    total_time = str(recipe.get("total_time") or "").strip()
    ingredients = recipe.get("ingredients") if isinstance(recipe.get("ingredients"), list) else []
    directions = recipe.get("directions") if isinstance(recipe.get("directions"), list) else []

    ingredients_count = count_items(ingredients)
    directions_count = count_items(directions)

    html_entities_found = any(
        has_html_entities(value)
        for value in [title, image, total_time]
    ) or any(has_html_entities(item) for item in ingredients + directions)

    notes = []
    if error_note:
        notes.append(error_note)

    if directions_count <= 1:
        notes.append("directions_count<=1")
    if ingredients_count < 3:
        notes.append("ingredients_count<3")
    if not title:
        notes.append("missing_title")
    if not image:
        notes.append("missing_image")
    if html_entities_found:
        notes.append("html_entities_found")

    if directions_count == 1:
        only_direction = str(directions[0] or "").strip() if directions else ""
        if len(only_direction) >= 400:
            notes.append("single_long_direction_block")

    needs_manual_review = any(
        [
            directions_count <= 1,
            ingredients_count < 3,
            not title,
            not image,
            html_entities_found,
            "single_long_direction_block" in notes,
        ]
    )

    return {
        "site": str(source_row.get("site") or "").strip(),
        "recipe": str(source_row.get("recipe") or "").strip(),
        "url": str(source_row.get("url") or "").strip(),
        "status": str(response.status_code if response is not None else "request_failed"),
        "http_ok": as_bool(bool(response is not None and response.ok)),
        "title_ok": as_bool(bool(title)),
        "image_ok": as_bool(bool(image)),
        "ingredients_count": str(ingredients_count),
        "directions_count": str(directions_count),
        "total_time_present": as_bool(bool(total_time)),
        "html_entities_found": as_bool(html_entities_found),
        "needs_manual_review": as_bool(needs_manual_review),
        "notes": "; ".join(notes),
    }


def audit_one(session: requests.Session, source_row: dict[str, str]) -> dict[str, str]:
    url = str(source_row.get("url") or "").strip()
    if not url:
        return build_row(source_row, None, None, "missing_url")

    try:
        response = session.post(
            ENDPOINT,
            json={"url": url},
            timeout=90,
            headers={"Content-Type": "application/json"},
        )
    except requests.RequestException as exc:
        return build_row(source_row, None, None, f"request_error:{exc.__class__.__name__}")

    try:
        payload = response.json()
    except ValueError:
        payload = None

    if not response.ok:
        error_message = ""
        if isinstance(payload, dict):
            error_message = str(payload.get("error") or "").strip()
        return build_row(source_row, response, payload, error_message or "http_error")

    return build_row(source_row, response, payload)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python3 tools/audit_recipe_url_import.py input.csv output.csv", file=sys.stderr)
        return 1

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        missing = [name for name in ("site", "recipe", "url") if name not in (reader.fieldnames or [])]
        if missing:
            print(f"Missing required input columns: {', '.join(missing)}", file=sys.stderr)
            return 1

        rows = list(reader)

    session = requests.Session()
    output_rows = [audit_one(session, row) for row in rows]

    with open(output_path, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {len(output_rows)} rows to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
