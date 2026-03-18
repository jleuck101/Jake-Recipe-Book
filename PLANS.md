# Jake Recipe Book Plan

## Current Milestone
- Finish auth/admin hardening while keeping the current UI/layout mostly unchanged.

## Done
- Extracted Firebase setup into `src/firebase.js`.
- Extracted auth helpers into `src/auth.js`.
- Extracted recipe normalization into `src/recipe-schema.js`.
- Extracted per-recipe Firestore operations into `src/recipes-api.js`.
- Switched normal recipe CRUD to per-recipe Firebase operations.
- Enabled signed-out public read with owner-edit-only controls.
- Added hidden admin sign-in via `?admin=1`.
- Cleaned up old login-gate remnants.
- Added verified hash-based per-recipe URLs/history.
- Made recipe tiles real links for right-click and open-in-new-tab behavior.

## Next Tasks
- Wire owner UID and stop relying on email fallback.
- Admin-gate legacy import/restore and manual push paths.
- Keep `syncAll()` out of normal edit flows.

## Constraints
- Do not refactor the service worker yet.
- Do not refactor import/restore yet except for admin gating.
- Keep changes scoped and minimal.
- Avoid new globals unless needed for compatibility.
- Keep Firebase imports separated correctly by product.

## Known Risks
- `syncAll()` still exists for manual push/import/restore paths and is destructive.
- Owner check still falls back to email until UID is wired.
- `index.html` remains the main app shell, so behavior changes require careful review.

## Current Checkpoint
- commit: `9236a0e`
- tag: `checkpoint-crud-modules-working`
