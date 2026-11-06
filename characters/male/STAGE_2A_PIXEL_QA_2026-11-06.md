# Stage 2A — Static Extraction and Pixel QA

Date: 2026-11-06

## Result
**PASS for static extraction QA only. NOT rig-ready.**

The user-approved 1024x1536 front-view character image was split into 13 aligned full-canvas RGBA PNG extraction layers. The masks were revised to exclusive pixel ownership after the initial pass showed duplicated alpha ownership.

## Verified checks
- Canvas: 1024x1536 on every extracted PNG.
- Layer count: 13.
- Duplicate alpha ownership after correction: 0 pixels.
- Mean RGB difference over extracted pixels when recomposited: 0.0.
- Exact RGB match over extracted pixels: 100%.
- Rough foreground pixels outside extraction masks: 87.
- Original flattened reference retained as a separate hidden layer in the ORA.
- OpenRaster archive rebuilt with full-canvas layer entries.

## Deliverables generated in the ChatGPT workspace
- `male_character_step2_assets.zip`
- `male_character_layers.ora`
- `layers_composite_preview.png`
- `PIXEL_QA_REPORT.md`

SHA-256:
- ZIP: `83788786fc573b368fffd1e58f212be7ed7a2b2231f1a16c371ef43eb45857f9`
- ORA: `59a87bdc3ee6ac79789134767105497eee45e714abbffc588e8b0c7a2e0eaef6`
- Preview: `3b7c580925e4c45344eb0321be8b3b33d63cbfbcee5ecc30c735c632e42e7925`

## Important scope boundary
This commit records the Stage 2A result and its checks. **The binary ZIP/ORA/PNG files are not included in this Git commit** because the connected GitHub write interface available here supports text blobs but does not provide a direct binary file-upload action. The generated binaries remain available as conversation files for download.

## Not validated
- Hidden artwork behind body-part overlaps.
- Joint rotation, pivots, deformation, or gap-free articulation.
- Independent facial components and expression variants.
- Six-view turnaround, hand/boot variants, and accessories.
- Native Krita `.kra` save/reopen.
- Import into an animation application and rendered motion test.

## Gate decision
Stage 2A is complete for static extraction and pixel QA. Stage 2B must reconstruct concealed overlap artwork, split semantic parts, clean edges, and test articulation. Do not label the character rig-ready until those tests pass.
