# Male Character — Step 2 Production Assets

**Status: PARTIAL REVIEW PACKAGE — NOT RIGGING-READY.**

The current review package contains the approved front-facing master, a layered OpenRaster working file, 17 first-pass full-canvas cutouts, approximate facial crop layers, a preview, and the supplied design-reference panels.

## Recommended workflow
- Edit in Krita; retain the native `.kra` as the authoritative editable source.
- Use `.ora` for interchange and aligned transparent PNGs for animation runtime.
- Keep the production assets in this repository. Do not fork Krita's source repository; Krita is the editor, not the character-rigging asset pipeline.
- Use the downloadable review package for the binary working assets. This repository commit records the manifest and acceptance status; it does not pretend the binaries are already committed.

## Important limitations
The approved source is a single flattened front view. It cannot provide hidden joint artwork, genuine side/back views, independent expressions, alternate hand/boot poses, or accessory cutouts. The current masks and facial crops are preliminary and need manual cleanup and reconstruction.

## Acceptance criteria
1. Every body part and variant is a separate transparent PNG.
2. Rig layers share a canvas and include pivot/overlap guidance.
3. Joint rotation tests show no gaps.
4. Face, costume, proportions and palette match the approved master.
5. Turnaround, expressions, hands, boots and accessories are separate authored assets.
6. The layered project opens and is saved natively in Krita; the rig is tested in the selected animation application.

See [VALIDATION_REPORT.md](./VALIDATION_REPORT.md) and [manifest.json](./manifest.json).
