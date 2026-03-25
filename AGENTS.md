# Jake Recipe Book Codex Guide

## Purpose
- This repo powers Jake's Recipe Book, a static GitHub Pages recipe site backed by Firebase.
- Keep changes practical, minimal, and safe for a live site.

## Repo Layout
- `index.html`: current main app shell and most live UI/state logic.
- `src/firebase.js`: Firebase app/auth/storage/db setup.
- `src/auth.js`: auth state helpers and owner check fallback.
- `src/recipe-schema.js`: canonical recipe normalization.
- `src/recipes-api.js`: per-recipe Firestore CRUD and recipe subscriptions.
- `backend/app.py`: Flask recipe-import backend used for URL import preview.
- `backend/requirements.txt`: backend Python dependencies.
- `render.yaml`: Render Blueprint for the URL import backend.
- `sw.js`: current service worker. Do not refactor unless explicitly asked.
- `_import/`: source/import material, not core runtime.
- `tools/`: maintenance scripts, not app runtime.

## Current Architecture Notes
- Normal recipe CRUD now uses per-recipe Firebase operations.
- `syncAll()` still exists in `index.html` for manual push/import/restore paths and is dangerous legacy behavior.
- Signed-out public read is enabled; edits remain owner-only.
- Owner check currently falls back to email until owner UID is wired.
- Recipe viewer interaction rules:
  - `Escape` only closes local viewer subpanels such as edit/tag/export UI.
  - overlay clicks only close local viewer subpanels.
  - only the explicit `← Back to Recipes` button exits the recipe page.
- Compatibility globals in use:
  - `window.FB`
  - `window.AUTH`
  - `window._authInit`
  - `window._getCurrentUser`

## Recipe URL Import Status
- Recipe URL import is live and working.
- The frontend flow is:
  - `Import -> Import URL`
  - preview from backend
  - `Use This Preview`
  - editable in-memory draft
  - save through the normal editor flow
- The backend endpoint is:
  - `https://jake-recipe-book-import.onrender.com/api/import-recipe-url`
- Import behavior currently supports:
  - JSON-LD recipe extraction from the backend
  - preview-first import
  - read-only preview matching draft formatting closely
  - `total_time` mapping into `timeMinutes` when parseable
  - stricter max-time filtering that excludes recipes without valid `timeMinutes` when the filter is active
  - warning before discarding an unsaved URL-import draft
- Known unsupported / partially supported publishers:
  - Some stricter publishers are currently blocked upstream for automated import, especially Allrecipes and Serious Eats
  - Treat those as unsupported for automated import unless backend compatibility improves
  - Fallback for blocked sites: paste recipe text instead
  - Blocked publishers now fail with a clearer user-facing message instead of a generic fetch error
- Current backend fetch strategy:
  - direct fetch first
  - if direct fetch fails, one origin warm-up request
  - then one retry
  - concise upstream failure logging is in place for timeout / HTTP error / redirect target / likely block page
- Render free-tier note:
  - the import backend may take up to about a minute to wake up on the first request

## Working Rules
- Prefer extending the extracted `src/` modules instead of growing Firebase logic inline.
- Keep Firebase imports separated by product:
  - Firestore APIs from `firebase-firestore`
  - Storage APIs from `firebase-storage`
  - Auth APIs from `firebase-auth`
- Avoid new globals unless needed for compatibility with the existing non-module script.
- Preserve the current UI/layout unless the task explicitly changes it.
- Keep routing unchanged unless the task explicitly asks for it.
- Keep shared viewer/export/menu helpers top-level and shared; do not duplicate them in narrower scopes.
- Do not reintroduce older viewer close-flow experiments unless the task explicitly asks for a behavior change.

## Local Run Notes
- Frontend:
  - open `index.html` locally with a simple static server if needed
  - the service worker may cache aggressively; hard refresh or unregister SW if behavior looks stale
- Backend:
  - `cd backend`
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
  - `pip install -r requirements.txt`
  - `python3 -m flask --app app run --port 8787`
- Local frontend endpoint override:
  - `window.RECIPE_IMPORT_URL_ENDPOINT = "http://127.0.0.1:8787/api/import-recipe-url"`
- Owner/admin controls:
  - owner-only controls may require opening the app with `?admin=1`

## Safety / Do-Not Rules
- Do not reintroduce normal-path destructive full-collection sync.
- Do not refactor the service worker unless explicitly requested.
- Do not refactor import/restore flows unless explicitly requested.
- Do not change Firebase rules from this repo unless rules/config are added to the repo and the task asks for it.
- Treat `syncAll()` paths as admin/recovery-only.

## Render Deployment Notes
- Render Blueprint config lives in `render.yaml`.
- The service uses:
  - `rootDir: backend`
  - `plan: free`
  - start command: `gunicorn app:app`
- If backend changes are deployed, remember the live frontend uses the production endpoint via:
  - `<meta name="recipe-import-endpoint" ...>` in `index.html`

## Audit Tooling
- `tools/audit_recipe_url_import.py`
  - local audit script for batch-testing the live import endpoint from a CSV of URLs
- `recipe-test-input.csv`
  - current seed list of recipe URLs for audit testing
- `recipe-test-results.csv`
  - latest raw audit output
- `recipe-test-report.md`
  - human-readable audit summary and manual follow-up priorities

## Highest-Value Next Steps
- Improve backend compatibility for stricter blocked publishers only if needed by checking live logs first.
- Re-run the audit after backend fetch changes and compare:
  - Allrecipes
  - Serious Eats
  - BBC Good Food
- Keep frontend work small and focused on formatting/UX only; the main remaining risk is upstream publisher blocking, not general app flow.

## Testing Checklist After Code Changes
- Verify the site still loads from `index.html`.
- Verify Firebase imports are valid and separated by product.
- Verify normal recipe create, edit, cooked count, image update, and delete do not route through `syncAll()`.
- Verify import/restore/manual push behavior was not changed unintentionally.
- Verify no unnecessary globals were added.
- For recipe URL import changes:
  - verify preview loads from the backend
  - verify `Use This Preview` opens an editable draft
  - verify save goes through the normal editor path
  - verify blocked publishers fail with a clear user-facing message

## Git / Checkpoints
- Prefer small, reviewable commits.
- Preserve checkpoint references in docs when given by the user.
- Latest verified checkpoint:
  - commit: `9236a0e`
  - tag: `checkpoint-crud-modules-working`

## Next Milestone
- Improve owner/auth hardening and publisher compatibility while keeping the current UI/layout mostly unchanged.

## Planning
- Longer multi-step work should update `PLANS.md` so future sessions can resume safely.
