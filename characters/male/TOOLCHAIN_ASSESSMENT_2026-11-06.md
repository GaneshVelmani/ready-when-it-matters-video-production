# Step 2 — External Toolchain Assessment (2026-11-06)

## Decision

Use a multi-tool workflow rather than expecting the Krita source repository to perform character rigging:

1. **Krita** — artwork authoring and layer cleanup. The linked KDE/Krita GitHub repository is source code, not a remotely executable drawing workspace. The GitHub README identifies GitHub as a mirror of the KDE Invent repository.
2. **Rigby2D** — preferred rigging and short-film animation candidate. Its public beta documentation describes import of same-canvas PNG layers, AutoRig bone/joint generation, IK, pose/face controls, audio tracks, and MP4/WebM/PNG-sequence rendering. Browser editor: https://rigby2d.com/editor/
3. **OpenToonz** — mature 2D animation fallback for scene assembly and final rendering if Rigby2D proves unstable or its import/rigging workflow fails.
4. **Synfig Studio** — optional vector/bitmap tweening alternative; not the primary choice for this cut-out rig.

## Repositories inspected

- https://github.com/KDE/krita — Krita drawing application source mirror. Not a rigging or video-production service.
- https://github.com/jaisurya-dev-art/rigby2d — public-beta 2D skeletal animation editor, dual MIT/Apache-2.0 license for its own code. Its documentation supports PSD, SVG, or same-size PNG-layer import and AutoRig. Treat as a promising candidate, not as production-validated software until the project is imported, saved, reopened, and rendered.
- https://github.com/opentoonz/opentoonz — established open-source 2D animation application. Official README points to the official website and source repository.
- https://github.com/synfig/synfig — official Synfig Studio source repository, GPL-3.0.

## Why Rigby2D is the preferred first attempt

The documented PNG import route accepts multiple PNG files with identical dimensions, preserving their original canvas positions. This avoids requiring a PSD export from Krita for the first rigging test. Its AutoRig documentation recognizes common layer names such as torso, pelvis, head, neck, upperarm, forearm, hand, thigh, shin/lower-leg and boot/foot. It also documents a manual correction table before rig generation.

Film workspace documentation describes 1080p/4K and vertical output, audio tracks, lip-sync, PNG sequences, WebM with alpha and MP4 rendering. These are claims from the project's own documentation and still require a real test with our character.

## Import candidate and naming convention

The existing Step 2 v2 package contains 17 full-canvas body-part PNGs plus four neutral facial crop layers. The body parts can be staged for an initial Rigby2D import using names such as:

- head_base.png
- hair.png
- neck.png
- torso_jacket_front.png
- upperarm_l.png / upperarm_r.png
- forearm_l.png / forearm_r.png
- hand_l.png / hand_r.png
- pelvis.png
- thigh_l.png / thigh_r.png
- lower_leg_l.png / lower_leg_r.png
- boot_l.png / boot_r.png

This is only an import candidate. The existing audit identified hand alpha fragments, duplicated head/hair content, missing hidden joint reconstruction, no jacket-back/T-shirt split, and no six-expression system. Do not auto-rig or publish these as final until those defects are corrected.

## Critical limitation

No Rigby2D desktop/browser editor session is connected to this ChatGPT workspace. GitHub source inspection alone cannot execute the application, create a native .rigby project, or verify a live bone pose. The current environment also has no Krita, OpenToonz or Synfig executable installed. Therefore this assessment does not claim that a rig was generated or tested.

## Acceptance sequence

1. Rebuild/clean the PNG layers with genuine alpha and joint overlap.
2. Import the same-canvas PNGs into Rigby2D.
3. Correct AutoRig's detected part/side assignments.
4. Generate the rig; inspect shoulder, elbow, wrist, hip, knee and ankle.
5. Save the native .rigby file; close and reopen it.
6. Create a short motion test and render a 5–10 second MP4.
7. If Rigby2D import, saving or rendering fails, use OpenToonz for scene assembly while preserving the PNG layers.
8. Only after these checks and human review should Step 2 be marked complete.

## Official project documentation consulted

- Rigby2D AutoRig: https://rigby2d.com/docs/autorig.html
- Rigby2D importing art: https://rigby2d.com/docs/importing-art.html
- Rigby2D Film workspace: https://rigby2d.com/docs/film.html
- Rigby2D MCP: https://rigby2d.com/docs/mcp.html
- OpenToonz README: https://github.com/opentoonz/opentoonz
- Krita README: https://github.com/KDE/krita
- Synfig README: https://github.com/synfig/synfig
