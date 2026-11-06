# Step 2 / Episode 1 — production execution plan

Updated: 2026-11-06  
Target publication: Sunday, 2026-11-08  
Priority: ship a coherent Episode 1, do not block publication on optional character-sheet extras.

## Current verified state

- Male character has an audited 17-part first-pass PNG extraction and a 22-layer OpenRaster source.
- The source is **not** a finished rig. The audit found duplicated head/hair content, fragmented hand masks, missing hidden joint overlap, and no pivot/deformation tests.
- The Rigby2D import ZIP is a convenience package; it is not a native Rigby2D project.
- Krita, OpenToonz and a local animation editor are not installed in the current execution environment.
- GitHub documentation and text assets can be committed. Binary PNG upload requires a verified binary Git-data path.

## Independent work that can proceed

1. Run `scripts/check_step2_asset_pack.py` against the full PNG layer directory.
2. Preserve the approved master and design-sheet references as immutable references.
3. Keep the current extraction labelled `candidate`; never label it approved/rigging-ready.
4. Prepare an import list and validation checklist for Rigby2D.
5. Prepare Episode 1 shot timing, narration, captions, sound cues and scene continuity independently of the final rig.
6. Prefer a reduced, tested front-view rig for Episode 1 over attempting all optional turnarounds and accessories before publication.

## Required editor-side acceptance

- Import the 17 body parts at identical canvas coordinates.
- Fix head/hair duplication before enabling both layers.
- Repair left/right hand alpha islands.
- Reconstruct concealed shoulder, elbow, wrist, hip, knee and ankle overlaps.
- Assign and inspect pivots; rotate every joint in both directions.
- Confirm no transparent gaps, clipping, detached fragments or texture sliding.
- Save, close and reopen the native project.
- Render a short movement test and inspect it frame by frame.

## Full Step 2 backlog (not to be silently waived)

- Six separate turnarounds: front, 3/4 front, left profile, right profile, 3/4 back, back.
- Six separate facial expressions: neutral, happy, surprised, serious, confused, angry.
- Six accessory PNGs: backpack, compass, neckband, headlamp, rope coil, canteen.
- Seven hand-pose PNGs: relaxed, open, fist, point, grab, hold, thumbs up.
- Five boot-angle PNGs: front, side, 3/4 front, 3/4 back, back.
- Jacket front/back and T-shirt independent layers.
- Clean head base, hair, facial replacement patches and alternate eyes/mouths.
- Final composite match against approved reference, then user review.

## Deadline risk

If the editor import, joint repair and render test cannot be completed by Sunday morning, use a controlled cut-out/limited-motion animation for Episode 1 rather than presenting the current candidate as a production-ready skeletal rig. A video can ship with constrained movement; a visibly broken rig should not.
