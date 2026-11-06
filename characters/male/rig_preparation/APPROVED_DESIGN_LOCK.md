# Approved male character design lock — 2026-11-06

## Approval state
The user has approved the male character design and existing design sheet. Treat the approved full-body front reference and the supplied asset sheet as immutable identity/outfit targets.

## Locked visual attributes
- Same male facial identity, face shape, eyes, brows, nose, mouth, jawline, black hairstyle and beard.
- Olive-green explorer jacket with the original pocket layout and details.
- White inner T-shirt.
- Khaki cargo trousers with the original pocket layout.
- Brown lace-up boots.
- Preserve the approved 2D cartoon rendering, body proportions, skin tone and line treatment.

## Production rule
Approval of the design is not approval of every extracted layer or of a completed rig. Do not use generated variants that change the face, hair, outfit, accessories or proportions. A generated concept sheet that does not match the approved reference must be rejected, not committed as production art.

## Existing candidate defects remain open
- Head base contains hair while a separate hair layer also exists.
- Torso/jacket and arm layers overlap inconsistently.
- Hand masks contain detached or missing alpha fragments.
- Hidden pixels behind joints are not reconstructed.
- Current extracted layers are from one flattened front view; they do not constitute six finished turnaround views.
- Expression crops are not complete replacement-ready facial rigs.
- Pivot positions are estimates and have not passed editor-side rotation tests.

## Remaining production outputs
1. Rebuild clean head base, hair, neck, face feature replacement patches and six expression sets.
2. Reconstruct torso as separate jacket front/back and T-shirt layers.
3. Rebuild arms/hands with concealed overlap at shoulder, elbow and wrist; include the approved hand pose set.
4. Rebuild pelvis, thighs, lower legs and boots with concealed overlap at hip, knee and ankle; include the approved boot-angle set.
5. Create six consistent turnarounds: front, 3/4 front, left profile, right profile, 3/4 back and back.
6. Create the six approved accessory assets as separate transparent PNGs.
7. Composite-match against the approved reference; verify alpha edges, common canvas, pivots, joint rotation, save/reopen and short render.

## Acceptance gate
Mark a layer or group complete only after visual inspection against the approved design, transparent PNG validation, and a successful composite/rig test. Until then label it candidate or reference-only.
