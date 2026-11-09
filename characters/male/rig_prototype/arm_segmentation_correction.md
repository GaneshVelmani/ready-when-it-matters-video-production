# Stage 2B arm segmentation correction

## Defect found
The previous screen-left and screen-right upper-arm PNGs contained sleeve-only artwork. The forearm PNGs extended into the hand, while the separate hand layers contained only partial hand pixels. This caused part of the arm to remain attached to the static torso and made the wrist cut visibly incorrect.

## Correction
A replacement set was generated from the approved 1024 × 1536 character reference:
- upper arm: shoulder to elbow, including the complete jacket sleeve and upper-arm artwork
- forearm: elbow to wrist, separate from the hand
- hand: wrist to fingertips
- all six layers retain identical full-canvas registration
- joint overlap is intentionally included at elbow and wrist to prevent gaps during rotation

## Pivot map
See `arm_layer_manifest.json` for pivot coordinates. Coordinate convention is screen-left/screen-right as viewed in the front-facing reference.

## Review package
The six corrected transparent PNGs and contact sheets are delivered in the companion file `Stage2B_Corrected_Arm_Layers.zip`. They are not embedded in this documentation-only commit. Import those PNGs to replace the earlier arm layers.

## Remaining validation
The segmentation and overlap were checked in a static composite. The target animation application still needs a live rotation test at shoulder, elbow, and wrist. Do not mark the complete rig production-ready until that test passes.
