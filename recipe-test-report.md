# Recipe URL Import Audit Report

Source files:
- `recipe-test-input.csv`
- `recipe-test-results.csv`

## Summary

- Total rows audited: `10`
- Passed cleanly: `8`
- Needs manual review: `2`
- Fetch/import failures: `2`

Interpretation:
- The live import flow is working for most tested recipe pages.
- The current failures are concentrated in upstream fetch compatibility, not broad parsing regressions.
- No rows were flagged for HTML entities, long single direction blocks, or missing title/image on successful imports.

## Rows Needing Attention

These are all rows where `status` is not OK or `needs_manual_review` is `true`.

| Site | Recipe | URL | Status | Needs Manual Review | Notes |
|---|---|---|---:|---|---|
| Allrecipes | Classic Lasagna | https://www.allrecipes.com/recipe/156037/classic-lasagna/ | `502` | `true` | Failed to fetch recipe URL.; directions_count<=1; ingredients_count<3; missing_title; missing_image |
| Serious Eats | Homemade Fresh Pasta | https://www.seriouseats.com/fresh-egg-pasta | `502` | `true` | Failed to fetch recipe URL.; directions_count<=1; ingredients_count<3; missing_title; missing_image |

## Issue Groups

### Fetch failure / 502
- `2` rows
- Sites:
  - Allrecipes
  - Serious Eats

### Missing title
- `2` rows
- Both are a consequence of fetch failure, not successful parsing.

### Missing image
- `2` rows
- Both are a consequence of fetch failure, not successful parsing.

### Low ingredient count
- `2` rows
- Both are a consequence of fetch failure (`0` ingredients returned).

### Low directions count
- `2` rows
- Both are a consequence of fetch failure (`0` directions returned).

### HTML entities found
- `0` rows

### Long single direction block
- `0` rows

## Successful Rows

These rows passed cleanly in the audit:

- Sally's Baking Addiction | Best Chocolate Chip Cookies
- Budget Bytes | Chicken Noodle Soup
- Minimalist Baker | 30-Minute Coconut Curry
- The Woks of Life | Chicken Fried Rice
- King Arthur Baking | Rustic Sourdough Bread
- BBC Good Food | Homemade pasta
- Minimalist Baker | Thai Yellow Coconut Curry with Mango
- The Woks of Life | Fried Rice Formula

## Top 5 Live Manual Tests

Priority order for testing in the live app:

1. `https://www.allrecipes.com/recipe/156037/classic-lasagna/`
   Reason: hard `502` fetch failure on a major recipe site; highest-value compatibility check.

2. `https://www.seriouseats.com/fresh-egg-pasta`
   Reason: second hard `502` fetch failure on another major recipe site; confirms whether fetch-header improvements worked.

3. `https://www.bbcgoodfood.com/recipes/fresh-pasta`
   Reason: passed, but with the smallest successful structure (`3` ingredients, `3` directions), so it is the most likely “successful but fragile” formatting case.

4. `https://www.kingarthurbaking.com/recipes/rustic-sourdough-bread-recipe`
   Reason: passed with a relatively small ingredient count and a baking-oriented format that can expose sectioning/time quirks.

5. `https://sallysbakingaddiction.com/chewy-chocolate-chip-cookies/`
   Reason: strong successful import from a popular recipe site; good regression check for preview, draft, image, and time mapping.

## Recommendation

Immediate next manual checks:
- Re-test the two current `502` URLs in the live app first.
- Then verify one borderline successful page and one clearly successful page:
  - BBC Good Food `fresh-pasta`
  - Sally's Baking Addiction `chewy-chocolate-chip-cookies`

If the two failing URLs still fail after the latest backend fetch-header change, the next backend work should focus on site compatibility for stricter publishers rather than frontend import UX.
