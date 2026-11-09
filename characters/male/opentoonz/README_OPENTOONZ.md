# OpenToonz Stage 2B — Male Character Import

This folder documents the OpenToonz import candidate prepared from the approved male character cutouts.

## Import
- Canvas: 1024 × 1536 RGBA; 24 fps suggested starting point.
- Import each PNG in the companion package as a separate level/column.
- Preserve the full-canvas registration. Do not trim, resize, or reposition individual PNGs.
- Use `OPENTOONZ_IMPORT_MANIFEST.json` for draw order and joint pivots.
- Parent each arm as upper arm → forearm → hand; each leg as thigh → lower leg → boot.

## Current status
- Corrected arm segmentation is used: complete shoulder-to-elbow upper arms, elbow-to-wrist forearms, and hands cut at the wrist.
- Corrected joint pivots and ~22 px overlap are recorded in the import manifest.
- The companion ZIP contains 22 full-canvas RGBA import layers plus reference material.
- PNG structural preflight passed for all 22 import layers.
- **Native OpenToonz validation is pending**: OpenToonz is not installed in the build environment, so no `.tnz` scene was created or reopened here. The motion previews from earlier packages are not represented as OpenToonz renders.

Do not sign off Step 2B until the imported scene is opened in OpenToonz, joint rotations are reviewed, and the native scene is saved and reopened.