# Step 2B — OpenToonz rig assembly handoff

This package advances the user-accepted corrected PNG candidate into a rig-assembly handoff. It is **not** a native OpenToonz scene and is not yet editor-validated.

## Import
1. Create a 1024 × 1536 scene at the intended production frame rate.
2. Import every PNG as a separate level/column without resizing or changing registration.
3. Use `rig_hierarchy_pivots.json` and `pivot_map.csv` for initial peg/control hierarchy and pivot positions (pixels from top-left).
4. Arrange columns back-to-front using the draw-order list in the JSON manifest.
5. Keep hand/thumb joined to each forearm-hand layer. Do not introduce a wrist split in this pass.
6. Save the native scene, close it, reopen it, and verify that all level paths resolve.

## Required editor tests
- Neutral composite match against `corrected_neutral_composite.png`.
- Shoulder rotations: both sides, ±25° and ±45°.
- Elbow rotations: both sides, 0°, 30°, 60°, 90°.
- Hip and knee rotations: both sides, forward/back swing with no exposed transparent gaps.
- Boot/ankle alignment through full step contact and passing poses.
- Check every frame at 100% zoom for clipping, seams, detached fragments, texture sliding and silhouette pops.
- Render a 24-frame arm raise and 16-frame walk loop; close/reopen and re-render to confirm reproducibility.

## Known constraints
- Wrist is intentionally not an independent control: hand and thumb stay attached to the forearm-hand sprite.
- Head/face/hair and torso/jacket/shirt remain unified because the approved source is a flattened front view.
- Pivot coordinates are starting estimates; editor-side visual calibration is mandatory.
- OpenToonz is not installed in the current execution environment, so no native .tnz file or editor-side pass is claimed.
