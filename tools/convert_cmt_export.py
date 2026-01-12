from __future__ import annotations
import json
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(r"D:\recipe-site")
IN_HTML = ROOT / "_import" / "recipes.html"
OUT_JSON = ROOT / "recipes.json"

def clean_text(el) -> str:
    if not el:
        return ""
    return " ".join(el.get_text(" ", strip=True).split())

def list_text(els) -> list[str]:
    out = []
    for e in els:
        t = clean_text(e)
        if t:
            out.append(t)
    return out

def main():
    html = IN_HTML.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")

    recipe_divs = soup.find_all("div", class_=lambda c: c and "recipe" in c.split())
    recipes = []

    for div in recipe_divs:
        name_el = div.find(id="name")
        title = clean_text(name_el)

        # Image (usually: <img class="recipeImage" src="images/....jpg">)
        img = div.find("img", class_=lambda c: c and "recipeImage" in c)
        image_url = img.get("src", "").strip() if img else ""

        # Original link (in CMT export this can be plain text, not always <a>)
        link_el = div.find(id="original_link")
        source = clean_text(link_el)

        # Categories (can appear multiple)
        cat_els = div.find_all(class_=lambda c: c and "recipeCategory" in c)
        categories = list_text(cat_els)

        # Servings (text like "yields 8 servings")
        servings_el = div.find(id="servings")
        servings = clean_text(servings_el)

        # Made-this / starred / rating (if present)
        made_el = div.find(id="made_this")
        starred_el = div.find(id="starred")
        rating_el = div.find(id="rating")
        made_this = clean_text(made_el)
        starred = clean_text(starred_el)
        rating = clean_text(rating_el)

        # Ingredients
        ing_container = div.find(id="recipeIngredients")
        ing_lines = []
        if ing_container:
            # includes items like .recipeIngredient plus optional subheaders
            subheads = ing_container.find_all(class_=lambda c: c and "recipeIngredient_subheader" in c)
            items = ing_container.find_all(class_=lambda c: c and "recipeIngredient" in c)

            # If export uses subheaders, we include them as "## ..."
            # We’ll preserve order by walking children:
            for child in ing_container.descendants:
                if getattr(child, "get", None):
                    cls = child.get("class") or []
                    if "recipeIngredient_subheader" in cls:
                        t = clean_text(child)
                        if t:
                            ing_lines.append(f"## {t}")
                    if "recipeIngredient" in cls:
                        t = clean_text(child)
                        if t:
                            ing_lines.append(t)

            # Fallback if nothing captured
            if not ing_lines:
                ing_lines = list_text(items)

        # Instructions
        inst_container = div.find(id="recipeInstructions")
        inst_lines = []
        if inst_container:
            # usually .instruction items
            inst_items = inst_container.find_all(class_=lambda c: c and "instruction" in c)
            inst_lines = list_text(inst_items)

        # Notes
        notes_container = div.find(id="recipeNotes")
        notes = clean_text(notes_container)

        # Skip blank blocks
        if not title and not ing_lines and not inst_lines:
            continue

        recipes.append({
            "id": f"cmt-{len(recipes)+1:04d}",
            "title": title or "(untitled)",
            "cuisine": "",                  # you’ll fill in later
            "appliances": [],               # you’ll fill in later
            "timeMinutes": None,            # you’ll fill in later
            "dishesCount": None,            # you’ll fill in later
            "tags": [],
            "cookedCount": 0,
            "lastCookedAt": None,
            "imageUrl": image_url,          # keep as-is, usually "images/xyz.jpg"
            "sourceUrl": source,
            "servings": servings,
            "categories": categories,
            "madeThis": made_this,
            "starred": starred,
            "rating": rating,
            "ingredients": "\n".join(ing_lines).strip(),
            "directions": "\n".join([f"{i+1}. {t}" for i, t in enumerate(inst_lines)]).strip(),
            "notes": notes
        })

    OUT_JSON.write_text(json.dumps(recipes, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(recipes)} recipes to {OUT_JSON}")

if __name__ == "__main__":
    main()
