# Stage 2B — Male character rig preparation report

**Status: PROTOTYPE BUILT / RIG ACCEPTANCE FAILED — NOT PRODUCTION READY**

## Work completed
- Consolidated 17 first-pass body-part PNGs from the approved-master extraction.
- Added a documented bone hierarchy and estimated pivot map in `rig_prototype/rig.json`.
- Added a deterministic local renderer for neutral, arm-raise and alternating walk-cycle diagnostics.
- Rendered pose previews and a 16-frame walk-cycle diagnostic GIF.
- Kept the flattened master as comparison-only, not a deforming bone.

## Validation findings

| Check | Result | Notes |
|---|---|---|
| Canvas registration | PASS | 17 body sprites are 1024 × 1536 and share the master origin. |
| RGBA alpha | PASS | Source layers use RGBA. |
| Neutral composite | PASS WITH CAVEAT | Recognizable and broadly consistent with the approved front view. |
| Independent head/hair | FAIL | Head base still contains hair; separate hair sprite duplicates the upper hair region. |
| Face feature layers | BLOCKED | Head base already contains face details; isolated masks are incomplete/fragmented. |
| Joint overlap | FAIL | First-pass parts lack verified hidden overlap; gaps appear during rotations. |
| Pivot accuracy | PROVISIONAL | Estimated from one static front view; not calibrated in a native rig. |
| Walk cycle | FAIL | Diagnostic reveals gaps and rigid cutout behavior; not approved animation. |
| Native editor project | NOT TESTED | No native Rigby2D project was opened or validated. |

## Critical limitations
The approved source is a single flattened front-facing image. Pixels hidden behind the original pose do not exist in that source. Slicing or masking cannot recover them exactly. They must be reconstructed/redrawn and checked against the approved design.

The earlier `rigby2d_import_candidate` directory was not used as source of truth because its `face_mouth_beard_region.png` is alpha-empty and some PNGs are truncated. The valid V2 extraction is used for this prototype.

## Required before Stage 2B can pass
1. Reconstruct hidden shoulder, elbow, wrist, hip, knee and ankle overlap artwork.
2. Rebuild head as clean separate face base, hair, ears and neck; remove duplicate hair.
3. Split jacket and T-shirt where independent movement is needed.
4. Rebuild facial feature masks; do not overlay the incomplete current extracts.
5. Calibrate pivots/hierarchy in the target editor.
6. Re-render arm raise, leg swing, walk and turn tests; inspect at 100% for gaps, clipping and silhouette changes.
7. Save/reopen a native project and record the application/version.

**Do not mark the character rigging-ready or use the diagnostic GIF as final episode footage.**
