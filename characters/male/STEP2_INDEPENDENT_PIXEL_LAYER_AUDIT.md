# Independent Step 2 pixel/layer audit — 2026-11-06

## Verdict

**FAIL for rigging acceptance. PASS only as a first-pass extraction prototype.**

I independently reopened the delivered ZIP, inspected the layer preview, parsed the OpenRaster document and recomputed alpha-mask metrics from the PNG files. The visible defects in the preview are confirmed by the pixel-level measurements below.

## File integrity and structure

- ZIP archive opens successfully; 40 files are present.
- OpenRaster document is readable and declares 22 full-canvas layers at 1024 × 1536.
- 23 PNG files are present in `png_layers`.
- 22 of the PNGs are full-canvas 1024 × 1536 RGBA; `face_neutral_reference.png` is a 220 × 285 RGBA crop and is not canvas-aligned.
- The full-canvas body-part PNGs are dimensionally aligned, but this does not prove that their artwork is correctly separated or animation-safe.
- Alpha masks are non-empty. That alone is not an acceptance criterion.

## Recomputed pixel findings

| Layer | Connected alpha components | Components under 100 px |
|---|---:|---:|
| 01_head_base | 12 | 11 |
| 02_hair | 3 | 2 |
| 03_neck | 4 | 3 |
| 04_torso_jacket_front | 14 | 13 |
| 05_left_upper_arm | 2 | 1 |
| 06_left_forearm | 15 | 14 |
| 07_left_hand | 10 | 8 |
| 08_right_upper_arm | 2 | 1 |
| 09_right_forearm | 10 | 9 |
| 10_right_hand | 9 | 7 |
| 11_pelvis | 5 | 4 |
| 12_left_thigh | 5 | 4 |
| 13_left_lower_leg | 2 | 1 |
| 14_right_thigh | 8 | 7 |
| 15_right_lower_leg | 3 | 2 |
| 16_left_boot | 8 | 7 |
| 17_right_boot | 14 | 13 |

Small components may sometimes be intentional details, so component count is not used alone to reject a layer. Here, however, the preview visibly shows detached hand fragments and the quantitative results corroborate the concern.

## Critical overlap check

Alpha intersection between head base and hair is **11,358 pixels** (IoU 0.3241). The head base preview visibly contains the hair silhouette already. Enabling both therefore duplicates the hair; these are not independent clean rig layers.

Torso-to-upper-arm alpha intersections are 7,426 px (left) and 6,537 px (right). Overlap exists, but the source artwork does not demonstrate reconstructed hidden sleeve/shoulder pixels or validated pivot coverage. Intersection alone cannot establish safe articulation.

Other adjoining pairs have overlaps, but there is no recorded pivot map, deformation test or layer-toggle composite test proving gap-free articulation.

## Visual defects confirmed

1. Hair is duplicated between head base and hair layer.
2. Left and right hand PNGs contain detached fragments; right forearm/hand preview includes a separate stray sliver.
3. Forearm, hand, head and body masks include many tiny isolated alpha components requiring manual cleanup or classification.
4. Facial PNGs are single neutral crops, not alternate expression sets with replacement patches.
5. Turnarounds, accessories, hand poses and boot angles remain reference-sheet crops, not independent production exports.
6. The current package does not include a Krita-native `.kra` file or a saved/reopened Krita verification.
7. No joint pivot coordinates, overlap margins, pose/deformation screenshots or target animation import test exist.

## Stage decision

- **Stage 2A — source extraction and package integrity:** complete as a prototype.
- **Stage 2B — layer repair and production asset completion:** next stage; currently blocked/in progress.
- **Stage 2C — rigging validation and Step 2 sign-off:** not started; do not proceed yet.

## Required next actions

1. Rebuild the head/hair separation and clean detached alpha fragments.
2. Reconstruct hidden pixels behind shoulders, elbows, wrists, hips, knees and ankles.
3. Produce a proper torso stack (jacket front/back, shirt) and independent limbs with overlap margins.
4. Create separate expression variants with face patches, six independent turnaround views, six accessory PNGs, seven hand poses and five boot views.
5. Add pivot metadata and run joint rotation/pose tests.
6. Open the ORA in Krita, repair it, save as native `.kra`, close/reopen and verify.
7. Run composite reconstruction and animation-app import tests; submit contact sheets for final approval.

**Do not merge this as a Step 2 completion claim.** Design approval remains valid; extracted asset approval does not.
