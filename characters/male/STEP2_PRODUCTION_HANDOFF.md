# Step 2 — Male character production handoff

Status: DESIGN APPROVED; ASSET PACKAGE AUDIT HOLD

The approved male character design is the visual source of truth. The current extraction package is a useful prototype but is not rig-ready.

## Verified local review package
A 40-file audited review package has been assembled for review. It contains:
- OpenRaster (.ora) working document with 22 aligned layers
- Transparent master and first-pass body-part cutouts
- Facial component crops and reference sheets
- Layer alpha audit JSON/CSV
- Asset manifest and independent validation report

## Audit findings — blockers
1. Head base includes hair while a separate hair layer duplicates it.
2. Jacket torso overlaps arm cutouts; hidden shoulder pixels are not reconstructed.
3. Hand masks contain disconnected alpha fragments.
4. Facial parts are neutral crops only; alternate expression sets and replacement patches are missing.
5. Turnaround angles are reference-panel images, not independent production assets.
6. Six accessories are reference-only, not separate transparent PNGs.
7. Seven hand poses and five boot angles are not exported as separate production assets.
8. No joint pivot/deformation tests or animation-app import test are recorded.
9. The .ora is not a native .kra file; it must be opened and saved in Krita after corrections.

## Acceptance gates
- Reconstruct hidden pixels and clean masks at all joints.
- Export six independent turnaround views, six expressions, six accessories, seven hand poses and five boot angles.
- Preserve full-canvas alignment and transparent backgrounds.
- Validate layer on/off reconstruction, pivots, joint rotations, expression swaps and 100% edge quality.
- Save/reopen a native .kra and test import into the selected animation application.
- Obtain final user approval before marking Step 2 complete.

## Important
Design approval is not approval of extracted layers. Do not mark Step 2 complete or start final animation rigging until all blockers pass.
