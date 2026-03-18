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
- `sw.js`: current service worker. Do not refactor unless explicitly asked.
- `_import/`: source/import material, not core runtime.
- `tools/`: maintenance scripts, not app runtime.

## Current Architecture Notes
- Normal recipe CRUD now uses per-recipe Firebase operations.
- `syncAll()` still exists in `index.html` for manual push/import/restore paths and is dangerous legacy behavior.
- Signed-out public-read is not implemented yet.
- Owner check currently falls back to email until owner UID is wired.
- Compatibility globals in use:
  - `window.FB`
  - `window.AUTH`
  - `window._authInit`
  - `window._getCurrentUser`

## Working Rules
- Prefer extending the extracted `src/` modules instead of growing Firebase logic inline.
- Keep Firebase imports separated by product:
  - Firestore APIs from `firebase-firestore`
  - Storage APIs from `firebase-storage`
  - Auth APIs from `firebase-auth`
- Avoid new globals unless needed for compatibility with the existing non-module script.
- Preserve the current UI/layout unless the task explicitly changes it.
- Keep routing unchanged unless the task explicitly asks for it.

## Safety / Do-Not Rules
- Do not reintroduce normal-path destructive full-collection sync.
- Do not refactor the service worker unless explicitly requested.
- Do not refactor import/restore flows unless explicitly requested.
- Do not change Firebase rules from this repo unless rules/config are added to the repo and the task asks for it.
- Treat `syncAll()` paths as admin/recovery-only.

## Testing Checklist After Code Changes
- Verify the site still loads from `index.html`.
- Verify Firebase imports are valid and separated by product.
- Verify normal recipe create, edit, cooked count, image update, and delete do not route through `syncAll()`.
- Verify import/restore/manual push behavior was not changed unintentionally.
- Verify no unnecessary globals were added.

## Git / Checkpoints
- Prefer small, reviewable commits.
- Preserve checkpoint references in docs when given by the user.
- Latest verified checkpoint:
  - commit: `9236a0e`
  - tag: `checkpoint-crud-modules-working`

## Next Milestone
- Make the site public-read and owner-edit-only while keeping the current UI/layout mostly unchanged.

## Planning
- Longer multi-step work should update `PLANS.md` so future sessions can resume safely.
