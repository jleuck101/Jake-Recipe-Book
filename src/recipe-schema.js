function normalizeList(value) {
  return String(value || "")
    .split(",")
    .map((part) => part.trim())
    .filter(Boolean);
}

function canonicalTag(value) {
  const compact = String(value || "").trim().replace(/\s+/g, " ");
  if (!compact) return "";

  const lower = compact.toLowerCase();
  const acronyms = new Set(["bbq", "usa", "uk", "ai", "ip"]);

  const cap = (segment) => {
    if (!segment) return segment;
    if (acronyms.has(segment)) return segment.toUpperCase();
    return segment.charAt(0).toUpperCase() + segment.slice(1);
  };

  return lower
    .split(" ")
    .map((word) => (word.includes("-") ? word.split("-").map(cap).join("-") : cap(word)))
    .join(" ");
}

function toArray(value) {
  if (Array.isArray(value)) return value.map((item) => String(item || "").trim()).filter(Boolean);
  if (typeof value === "string") return normalizeList(value);
  if (value == null) return [];
  return [String(value).trim()].filter(Boolean);
}

function canonicalList(value) {
  const seen = new Set();
  const out = [];

  for (const item of toArray(value).map(canonicalTag).filter(Boolean)) {
    const key = item.toLowerCase();
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(item);
  }

  return out;
}

export function normalizeRecipe(recipe) {
  const input = recipe || {};

  return {
    id: String(input.id || ""),
    title: String(input.title || "").trim() || "(untitled)",
    cuisine: canonicalList(input.cuisine),
    dishType: canonicalList(input.dishType ?? input.course),
    base: canonicalList(input.base),
    mainIngredient: canonicalList(input.mainIngredient),
    equipment: canonicalList(input.equipment ?? input.appliances),
    timeMinutes: input.timeMinutes == null || input.timeMinutes === "" ? null : Number(input.timeMinutes),
    dishesCount: input.dishesCount == null || input.dishesCount === "" ? null : Number(input.dishesCount),
    tags: canonicalList(input.tags),
    cookedCount: Math.max(0, Number(input.cookedCount || 0)),
    lastCookedAt: input.lastCookedAt ?? null,
    createdAt: input.createdAt ?? Date.now(),
    updatedAt: input.updatedAt ?? Date.now(),
    imageUrl: String(input.imageUrl || "").trim(),
    imagePath: String(input.imagePath || "").trim(),
    sourceUrl: String(input.sourceUrl || "").trim(),
    servings: String(input.servings || "").trim(),
    ingredients: String(input.ingredients || "").trim(),
    directions: String(input.directions || "").trim(),
    notes: String(input.notes || "").trim()
  };
}

export function normalizeRecipes(recipes) {
  return (recipes || []).map(normalizeRecipe);
}
