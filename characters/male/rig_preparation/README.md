# Male Character — Rig Preparation Supplement

Status: **PREPARATION ONLY / NOT RIGGING-READY**

This supplement adds a provisional pivot map and layer-order checklist to the existing Step 2 extraction candidate.

- `pivot_map_estimated.json`: estimated front-view joint coordinates and smoke-test angles.
- `layer_order.json`: suggested stack order plus known conflicts.
- The accompanying review package contains the original audited PNG candidate layers, design references and OpenRaster source.

## Important
The pivots are visual estimates, not verified rig coordinates. The current cutouts still have known defects: duplicated head/hair content, torso/arm overlap, fragmented hands and missing hidden pixels. Do not present this as a finished rig or use the estimated pivots as final without editor-side joint rotation tests.

## Minimum acceptance
1. Correct head/hair split and remove duplicate silhouette.
2. Reconstruct concealed shoulder, elbow, wrist, hip, knee and ankle pixels.
3. Repair hand masks and inspect at 100% zoom.
4. Import all parts at identical canvas coordinates.
5. Set pivots, rotate each joint at -20°, -10°, 0°, +10°, +20°.
6. Confirm no gaps, clipping, detached fragments or texture sliding.
7. Save/reopen the native project and render a short movement test.
