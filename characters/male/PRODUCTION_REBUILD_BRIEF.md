# Male Character Step 2 — Production Rebuild Brief

Status: IN PROGRESS / HOLD — NOT RIGGING-READY
Reference of truth: approved male character image and approved male character asset sheet supplied in the project.

## Identity and costume lock

Preserve the same male character identity in every output:
- Black swept-up hairstyle and hairline.
- Same face shape, eyes, eyebrows, nose, mouth, jaw, beard and moustache.
- Same warm skin tone and 2D cartoon rendering style.
- Olive-green explorer jacket with the same collar, seams, pockets, buttons and sleeve details.
- White inner T-shirt.
- Khaki cargo trousers with the same pockets and seams.
- Brown lace-up hiking boots with dark soles.
- Preserve body proportions and line weight.

Do not redesign, beautify, simplify, recolor, change age, or reinterpret the character. Do not add logos, text, weapons, props, or costume elements unless they are one of the six approved accessories.

## Source-artwork constraint

Use the approved front master and design sheet as visual references. The existing front master is flattened. Hidden pixels behind body parts cannot simply be extracted. Any hidden shoulder, elbow, wrist, hip, knee, ankle, torso, or hair pixels must be redrawn to match the visible design.

## Deliverable specification

All PNG production parts must:
- Be RGBA PNG with genuine transparency, not a white or checkerboard background.
- Use one common 1024 × 1536 canvas and exact registration for rig body layers.
- Preserve original line weight, outlines, shading, texture, and proportions.
- Include enough hidden overlap to prevent gaps during rotations.
- Have no detached pixels, stray fragments, halos, or white matte fringe.
- Be named consistently and described in the manifest.

### A. Body rig layers

1. Head base / face skin (no hair, eyes, brows, nose, mouth, or beard overlays).
2. Back hair and front hair only if the design supports a clean split.
3. Neck.
4. Jacket torso front.
5. Jacket torso back.
6. T-shirt.
7. Left and right upper arms, with shoulder overlap.
8. Left and right forearms, with elbow and wrist overlap.
9. Left and right hands, wrist overlap included.
10. Pelvis / trouser waist.
11. Left and right thighs, hip and knee overlap included.
12. Left and right lower legs, knee and ankle overlap included.
13. Left and right boots.

### B. Facial system

Export six aligned expression states: neutral, happy, surprised, serious, confused, angry. Each state must include coordinated eyes, eyebrows, mouth, and beard/moustache where expression requires it. Use replacement patches so the original neutral face does not show underneath. Keep facial features registered to the same head canvas.

### C. Turnaround

Export six separate full-body transparent views, each on the same canvas and scale:
- Front.
- 3/4 front.
- Left profile.
- Right profile.
- 3/4 back.
- Back.

These must be newly authored views, not crops from the reference sheet. Costume pockets, jacket silhouette, trouser cargo pockets, boot construction, and hair silhouette must remain consistent.

### D. Accessories

Create six separate transparent PNGs, each as its own asset and not attached to the body:
- Backpack.
- Compass.
- Neckband.
- Headlamp.
- Rope coil.
- Canteen.

### E. Hand and boot variants

Create seven separate hand assets: relaxed, open, fist, point, grab, hold, thumbs-up.
Create five separate boot assets: front, side, 3/4 front, 3/4 back, back.

## Generation prompt template

Using the supplied approved male character reference as the sole identity and design authority, create [SPECIFIC ASSET] as a standalone 2D cartoon cut-out animation asset. Preserve the exact approved face identity, hairstyle, beard, skin tone, costume design, line art, shading, proportions and rendering style. Show only [SPECIFIC ASSET], fully visible, cleanly isolated, centered and correctly oriented. Include realistic hidden overlap only where required for the named joint. Output a true transparent RGBA background, no white background, no checkerboard, no cast shadow, no text, no labels, no border, no extra objects. Maintain the same character scale and registration as the 1024 × 1536 master. Do not redesign or invent details. If the requested hidden geometry is not visible in the reference, reconstruct it conservatively to match adjacent visible artwork.

## Krita project requirements

- Deliver a native .kra project with named groups: REFERENCE, BODY_RIG, FACE_EXPRESSIONS, TURNAROUND, ACCESSORIES, HAND_VARIANTS, BOOT_VARIANTS, QA.
- Keep each independently animated part on its own layer.
- Keep production layers aligned to the common canvas.
- Include a visible composite and a hidden reference layer.
- Save a flattened preview and a layer manifest.
- Reopen the saved .kra and confirm the layer tree is intact.

## QA acceptance gates

1. Transparency: inspect all edges at 100% zoom.
2. Registration: toggle parts over the reference; no scale/position drift.
3. Reconstruction: inspect hidden overlap under each adjacent part.
4. Joint test: shoulder, elbow, wrist, hip, knee, ankle at neutral and rotated poses.
5. Face test: swap all six expressions; no ghosting or misalignment.
6. Turnaround test: compare costume and identity across all six views.
7. Export test: reopen each PNG and verify RGBA, dimensions, alpha bounds, and naming.
8. Krita test: save/reopen .kra.
9. Animation test: import into the chosen animation application and test a short motion cycle.
10. Human review: user approves contact sheets before Step 2 is marked complete.

## Current baseline

The existing male_character_rebuild_v2.ora and first-pass PNGs are a prototype only. Refer to STEP2_ASSET_AUDIT_2026-11-06.md. They must not be promoted to final rig assets without passing the gates above.
