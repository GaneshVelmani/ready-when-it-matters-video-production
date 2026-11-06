# Step 2 PNG preflight — 2026-11-06

## Result

**Technical preflight: PASS (limited). Visual/rig acceptance: FAIL / HOLD.**

The local audit ran against the audited PNG layer directory.

- 23 PNG files found.
- All 17 required body-part filenames are present.
- Every required body-part PNG is RGBA, contains transparency and a non-empty alpha mask.
- All 17 required body parts use the expected 1024 × 1536 canvas.
- Four facial auxiliary crops and the neutral face reference are present; the neutral face crop is intentionally 220 × 285 and is not a body-rig canvas.
- The source OpenRaster file is present at `editable_krita_source/male_character_rebuild_v2.ora`.

## Visual inspection findings

The layer contact sheet confirms the existing audit findings:

- Head base already includes hair and facial identity; separate hair overlaps and is not a clean independent layer.
- The neck crop includes a beard/chin fragment at its upper edge.
- The torso has sleeve/shoulder areas that overlap the separated upper arms.
- Left and right hand masks have visibly detached or missing finger fragments.
- The extracted layers are cutouts from one flattened front view; concealed pixels and joint overlap are not reconstructed.
- Facial crops are neutral-only and not replacement-ready expressions.

## What this preflight does and does not establish

The automated check proves file presence, expected canvas for rig body parts, RGBA mode and non-empty transparency. It does **not** prove a correct composite, clean alpha edges, joint overlap, pivots, deformations, alternate views, accessories, or animation-editor compatibility.

## Decision

Keep the files labelled **candidate**. Do not call Step 2 complete or mark the package rigging-ready. The next required action is image repair/reconstruction in a layer-capable editor, followed by Rigby2D import and joint-rotation tests.
