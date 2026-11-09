# Step 2B — Full Character Package Execution

Status: **IN PROGRESS — NOT APPROVED / NOT RIGGING-READY**

Scope authorized by user: complete the full male-character Step 2B package before approval.

## Identity authority
Use only the approved male front master and approved male character sheet already supplied in this project. Preserve face identity, black swept-up hair, beard, warm skin tone, olive explorer jacket, white T-shirt, khaki cargo trousers, brown lace-up boots, proportions, line weight and shading. Do not redesign.

## Required deliverables and acceptance tracking

| ID | Deliverable | Required files / variants | Acceptance evidence | Status |
|---|---|---|---|---|
| B1 | Production body rig | Head base, back/front hair as appropriate, neck, jacket front/back, T-shirt, L/R upper arms, forearms and hands, pelvis, L/R thighs, lower legs and boots | RGBA, common 1024x1536 registration, reconstructed hidden overlaps, edge QA | PENDING |
| B2 | Facial expressions | Neutral, happy, surprised, serious, confused, angry; aligned eye/brow/mouth/beard replacement layers | No ghosting, face alignment and identity match | PENDING |
| B3 | Turnaround | Front, 3/4 front, left profile, right profile, 3/4 back, back | Six separately authored full-body views; consistent costume and proportions | PENDING |
| B4 | Accessories | Backpack, compass, neckband, headlamp, rope coil, canteen | Six separate transparent PNGs, independently placeable | PENDING |
| B5 | Hand poses | Relaxed, open, fist, point, grab, hold, thumbs-up | Seven separate transparent PNGs, wrist joins intact | PENDING |
| B6 | Boot angles | Front, side, 3/4 front, 3/4 back, back | Five separate transparent PNGs | PENDING |
| B7 | Layered source | Native Krita .kra plus ORA interchange and layer manifest | Save/reopen check and named groups | PENDING |
| B8 | Rig/animation QA | Shoulder, elbow, wrist, hip, knee, ankle; expression swaps; motion test | Rotation checks, no gaps/tearing/detached pixels; native rig project and rendered test | PENDING |
| B9 | Review package | Contact sheets, individual PNGs, QA report, GIF/MP4 previews | User review and approval | PENDING |

## Important production rules
- The approved master is flattened. Pixels hidden behind limbs and clothing must be reconstructed; they cannot be recovered by cropping.
- Do not promote the existing first-pass cutouts or Rigby2D import candidate to final assets. The previous audit identified duplicated head/hair pixels, fragmented hand alpha, missing joint overlap and incomplete clothing separation.
- Do not label any item PASS until the actual exported file has been inspected.
- A generated turnaround/contact sheet is a visual reference only; it is not a substitute for individual transparent PNG assets.
- A static preview is not proof of a working rig. The native project must be saved, reopened and rendered.

## Recommended production order
1. Lock source references and audit the existing package.
2. Rebuild body parts and hidden joint overlaps.
3. Produce facial expression replacement set.
4. Produce six turnarounds.
5. Produce accessories, hand poses and boot angles.
6. Assemble native layered source and aligned transparent exports.
7. Run automated PNG checks and visual edge/registration checks.
8. Test rotations and expression swaps in the selected animation application.
9. Publish review contact sheets and individual files; request user approval.

## Tooling limitation
GitHub is the version-control destination, not an image editor. Krita/OpenToonz/Rigby2D must be run in an actual editing environment to author and validate native projects. Repository documentation or source-code inspection alone does not establish a completed rig. Binary artwork must be committed through a verified binary Git-data upload path; do not represent text-only commits as artwork uploads.

## Final gate
Step 2B remains open until B1–B9 have real deliverables and the user approves the review package.