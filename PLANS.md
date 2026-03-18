# Jake Recipe Book Plan

## Current Milestone
- Make the site public-read and owner-edit-only while keeping the current UI/layout mostly unchanged.

## Done
- Extracted Firebase setup into `src/firebase.js`.
- Extracted auth helpers into `src/auth.js`.
- Extracted recipe normalization into `src/recipe-schema.js`.
- Extracted per-recipe Firestore operations into `src/recipes-api.js`.
- Switched normal recipe CRUD to per-recipe Firebase operations.

## Next Tasks
- Make signed-out users able to read recipes without changing the current layout significantly.
- Restrict edit/create/delete/import/restore controls to the owner account only.
- Wire owner UID and stop relying on email fallback.
- Admin-gate legacy import/restore and manual push paths.
- Keep `syncAll()` out of normal edit flows.

## Constraints
- Do not add routing yet.
- Do not refactor the service worker yet.
- Do not refactor import/restore yet except for admin gating.
- Keep changes scoped and minimal.
- Avoid new globals unless needed for compatibility.
- Keep Firebase imports separated correctly by product.

## Known Risks
- `syncAll()` still exists for manual push/import/restore paths and is destructive.
- Signed-out public-read is not implemented yet.
- Owner check still falls back to email until UID is wired.
- `index.html` remains the main app shell, so behavior changes require careful review.

## Current Checkpoint
- commit: `9236a0e`
- tag: `checkpoint-crud-modules-working`
