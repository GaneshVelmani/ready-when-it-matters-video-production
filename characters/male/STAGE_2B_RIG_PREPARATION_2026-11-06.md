# Stage 2B — Rig Preparation and Import Preflight

Date: 2026-11-06
Branch: stage-2b-rig-preparation

## Purpose
Move the Stage 2A pixel-isolated extraction into a controlled skeletal-rig import workflow. This stage does not declare the character rig-ready.

## Source package
The source package is the approved front-facing male master and the 13 same-canvas cutouts from Stage 2A. A mechanically renamed Rigby2D import candidate has been prepared separately as Stage2B_Rigby2D_Import_Preflight.zip in the ChatGPT workspace. The ZIP is not committed here because the connected GitHub writer does not expose direct binary upload.

## Prepared
- Dedicated stage-2b-rig-preparation branch.
- 13-layer Rigby2D import naming map.
- Preflight manifest describing combined layers and blockers.
- Repeatable PNG preflight script for canvas and alpha validation.
- Manual rig-test protocol covering shoulder, elbow, wrist, hip, knee and ankle.

## Important source limitation
The current extraction has 13 layers, not the complete design-sheet decomposition. Layers remain combined: head/face/hair; jacket/T-shirt torso; forearm/hand on each side. Concealed pixels behind joints have not been reconstructed. AutoRig must be treated as an import smoke test only.

## Selected tool
Rigby2D is the first import candidate because its public project documentation describes same-canvas PNG-layer import and AutoRig. Repository: https://github.com/jaisurya-dev-art/rigby2d. Editor: https://rigby2d.com/editor/.

This workspace has no live Rigby2D editor session. Repository inspection and import-preflight packaging do not prove that a native project was created, reopened, or rendered.

## Required Stage 2B execution
1. Import the 13 PNGs together, preserving common canvas coordinates.
2. Manually map left/right body parts; do not import the flattened reference as a rig layer.
3. Run first AutoRig only as a smoke test.
4. Rebuild independent semantic parts: head base, hair, facial features, neck, jacket front/back, T-shirt, upper arms, forearms, hands, pelvis, thighs, lower legs and boots.
5. Paint concealed pixels behind shoulder, elbow, wrist, hip, knee and ankle overlaps.
6. Add pivots and overlap margins; test at -20, -10, 0, +10 and +20 degrees.
7. Inspect at 100% zoom for gaps, clipping, duplicated edges, detached alpha islands and texture sliding.
8. Save the native project, close it, reopen it, and render a 5–10 second motion test.
9. Only after all tests pass, proceed to Stage 2C design variants and final approval.

## Exit criteria
- [ ] All semantic parts are independent transparent PNGs.
- [ ] Hidden joint artwork exists behind all articulated overlaps.
- [ ] Alpha edges are clean and no stray fragments remain.
- [ ] Joint tests pass at all prescribed angles.
- [ ] Neutral pose recomposes to the approved master.
- [ ] Native project save/reopen succeeds.
- [ ] Test render plays correctly.
- [ ] User reviews the final result.

**Current Stage 2B status: PREPARATION COMPLETE; ART RECONSTRUCTION AND LIVE RIG TESTS PENDING.**