# Step 2 Male Character — Independent Asset Audit

Audit date: 2026-11-06

## Decision

**HOLD — NOT APPROVED FOR RIGGING OR FINAL STEP 2 SIGN-OFF.**

The current package is a useful extraction prototype, not a complete animation asset set. The OpenRaster project is structurally readable and contains 22 aligned layers at 1024 × 1536, but the layer content and coverage do not satisfy the requested design sheet.

## Verified contents

- One transparent master image (1024 × 1536 RGBA).
- 17 body-part cutout PNGs (full-canvas 1024 × 1536 RGBA).
- Four facial crop PNGs (eyes, eyebrows, nose, mouth/beard region).
- One neutral-face reference crop.
- One OpenRaster .ora with 22 layers (one full-character reference + 17 body parts + four facial crops).
- Reference panels for turnaround, expressions, segmentation, hand poses, boot views, and accessories.

The .ora is an OpenRaster interchange file, not a native Krita .kra file. Open it in Krita and use Save As after review and correction.

## Defects found

1. **Head duplication risk:** the head-base PNG already contains the face and hair silhouette, while the hair layer separately repeats the hair.
2. **Torso/arm overlap is not reconstructed:** the torso contains sleeve/shoulder areas while upper-arm pieces are also separate. No shoulder pivot test exists.
3. **Hand cutouts are fragmented:** the hand layers contain multiple disconnected alpha islands; the preview shows detached skin/finger fragments.
4. **Facial crops are not animation-ready:** these are crops from one neutral expression, not six independently authored expression sets with clean replacement patches.
5. **No independent turnaround artwork:** 3/4 front, profiles, 3/4 back, and back exist only in a reference panel.
6. **No accessory cutouts:** backpack, compass, neckband, headlamp, rope coil, and canteen are reference illustrations only.
7. **No hand/boot variation exports:** the hand poses and boot angles are not separate production PNGs.
8. **No pivot/deformation validation:** no pivot coordinates, overlap measurements, joint pose tests, or target-animation-app rig test are present.

## Automated checks

- The 17 body-part PNGs and four facial component PNGs use RGBA and share a 1024 × 1536 canvas.
- All have non-empty alpha masks.
- Alpha bounding boxes and connected-component counts are recorded in `layer_alpha_audit.json`.
- Several pieces contain small disconnected alpha components. Some may be legitimate details, but visual inspection confirms unwanted fragments on hand layers.
- ORA stack XML parses and declares 22 full-canvas layers.
- Only the full-character reference layer is initially visible; extracted layers are hidden by default.

## Required rebuild

### Base rig
- Rebuild head base without duplicated hair.
- Separate jacket front/back and T-shirt, then reconstruct hidden pixels under overlaps.
- Cleanly isolate arms, hands, pelvis, thighs, lower legs, and boots.
- Rebuild joint overlap at shoulder, elbow, wrist, hip, knee, and ankle.
- Define pivot coordinates and overlap margins.
- Separate facial elements with replacement patches and alternate eye/mouth shapes.

### Design-sheet deliverables
- Six individual turnaround views: front, 3/4 front, left profile, right profile, 3/4 back, back.
- Six individual expressions: neutral, happy, surprised, serious, confused, angry.
- Six individual accessories: backpack, compass, neckband, headlamp, rope coil, canteen.
- Seven individual hand poses and five boot angles.

### Acceptance tests
- Transparent-background and edge-fringe inspection at 100% zoom.
- Layer on/off test and composite reconstruction against approved master.
- Shoulder, elbow, wrist, hip, knee, and ankle rotations with no gaps or detached fragments.
- Expression swaps without facial misalignment.
- Native Krita .kra save/reopen test.
- Import and test in the selected animation application.
- Final contact-sheet approval.

**Do not mark Step 2 complete until all required assets are individually exported and rig tests pass.**
