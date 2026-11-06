# Step 2 — Male character staging record

Date: 2026-11-06  
Branch: `step2/male-character-staging`  
Design approval: **APPROVED / LOCKED**  
Production asset status: **STAGED FOR REBUILD AND VALIDATION — NOT RIG-READY**

## Purpose

This branch stages the approved male-character design constraints and the existing Step 2 production plan for controlled completion. The approved character sheet is the immutable visual target. Approval of the design does not imply approval of the extracted cut-outs or rig.

## Locked design constraints

- Preserve the approved male face, hairstyle, black hair, beard, skin tone and body proportions.
- Preserve the olive-green explorer jacket and pocket details, white T-shirt, khaki cargo trousers and brown lace-up boots.
- Preserve the approved 2D cartoon linework, shading and rendering style.
- Reject any generated or reconstructed asset that changes identity, outfit, silhouette or proportions.

## Existing repository records

- `characters/male/rig_preparation/APPROVED_DESIGN_LOCK.md`
- `characters/male/STEP2_ASSET_AUDIT_2026-11-06.md`
- `characters/male/VALIDATION_REPORT.md`
- `characters/male/PRODUCTION_REBUILD_BRIEF.md`
- `characters/male/rig_preparation/layer_order.json`
- `characters/male/rig_preparation/pivot_map_estimated.json`
- `characters/male/rigby2d_import_candidate/IMPORT_MANIFEST.json`

## Staging decision

The existing first-pass extraction is a **candidate only**. The audit identified duplicate hair/head content, inconsistent torso/arm occlusion, fragmented hand alpha, incomplete expression crops, absent independent turnaround views, absent accessory cut-outs, absent hand/boot variation exports, and untested pivots/joint deformation.

Do not import the candidate into final animation production or mark Step 2 complete until those issues are resolved.

## Required completion gates

- [ ] Clean head base and separate hair/face feature layers.
- [ ] Separate jacket front/back and T-shirt; reconstruct hidden overlap pixels.
- [ ] Rebuild left/right upper arms, forearms and hands with shoulder/elbow/wrist overlap.
- [ ] Rebuild pelvis, thighs, lower legs and boots with hip/knee/ankle overlap.
- [ ] Export six consistent views: front, 3/4 front, left profile, right profile, 3/4 back and back.
- [ ] Export six replacement-ready expressions: neutral, happy, surprised, serious, confused and angry.
- [ ] Export all six accessories as independent transparent PNGs: backpack, compass, neckband, headlamp, rope coil and canteen.
- [ ] Export seven hand poses and five boot angles independently.
- [ ] Normalize canvas size, alignment, naming and alpha edges across the layer set.
- [ ] Define and verify pivots; test shoulder, elbow, wrist, hip, knee and ankle rotations with no gaps or detached fragments.
- [ ] Save and reopen a native Krita `.kra` file.
- [ ] Import into the selected 2D animation application and validate a short motion test.
- [ ] Compare final composite and contact sheet against the approved design and obtain final asset approval.

## Release rule

Only validated production PNGs and the tested native project may be promoted from this staging branch. Reference crops, audit files, estimated pivots and first-pass extraction outputs must remain clearly labeled as reference or candidate material.
