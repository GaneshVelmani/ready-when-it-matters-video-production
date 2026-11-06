# Rigby2D import candidate — male character

This package is prepared from the existing audited Step 2 v2 PNG extraction. It is **not rigging-ready**.

## Import procedure

1. Open https://rigby2d.com/editor/ and create an empty project.
2. Extract the local archive `Rigby2D_Male_Character_Import_Candidate.zip`.
3. Import the 17 body-part PNGs together using **File → Import → PNG images…**. They share a 1024 × 1536 canvas.
4. Open **File → AutoRig artwork…** and manually correct every part/side mapping.
5. Exclude `reference_master_do_not_autorig.png`; it is comparison-only.
6. Generate the rig only after inspecting the mapping table.
7. Test shoulder, elbow, wrist, hip, knee and ankle rotations. Check for gaps, duplicated pixels and detached fragments.
8. Save a native `.rigby` file, close it, reopen it, then render a short 5–10 second motion test.

## Known limitations

- Head base and hair content overlap/duplicate.
- Hand layers contain disconnected alpha fragments.
- Hidden joint overlap is not reconstructed or validated.
- Jacket back and T-shirt are not split into independent layers.
- Neutral facial crops are not six expression replacements.
- Six turnaround views, six accessories, seven hand variants and five boot variants are not included as individual assets.
- No Rigby2D project, rig generation, pose test or render has yet been completed.

Use this pack as a **first import test only**, not as final approved Step 2 artwork. See `TOOLCHAIN_ASSESSMENT_2026-11-06.md` and `STEP2_ASSET_AUDIT_2026-11-06.md`.
