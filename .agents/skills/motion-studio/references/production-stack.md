# Compose existing skills into a production workflow

Use for a quality rebuild, professional motion, or a request to reuse others' skills.
The owner asked for craft, physical plausibility and appropriate techniques. Listing
skills, adding more dependencies or copying a style name does not meet that request.

## A working chain

For work starting from GIFs or generated pose sheets, apply the
[frame-sequence production reference](../../frame-sequence-animation/references/professional-production.md).
Check native subject pixels, drawing exposures and the edited repetition budget
before compositing. Preserve RGBA frames as the master; preview/export must follow
the same reviewed path rather than an unrelated imported-template treatment.

| Stage | Existing skill | Concrete output / review |
|---|---|---|
| Visual concept and shot direction | `art-motion`; relevant treatment/camera principles from `cinematic-product-commercial` when available in the host skill catalogue | Brief, visual thesis, opening/hero/outcome, shot purpose and camera/light plan |
| Static image craft | `canvas-design`, or designed assets appropriate to the chosen medium | Style frames at target aspect; assess shapes, materials, type, composition and visual hierarchy without relying on motion |
| Action and physical logic | `animation-principles` and its `production-practice.md` | Named driver/support, pose/contact plan, timing/spacing and difficult contact interval |
| Controlled 3D objects/materials | `studio-3d`; `motion-threejs` or `motion-rapier` where appropriate | Real geometry/materials, deliberate light/lens, keyframes/constraints or a baked solver cache |
| Designed 2D character layers | `gsap` for complex timelines when installed, otherwise existing frame-driven transforms | Designed assets, real pivot/rig spaces, preserved grip/limb lengths, seekable timeline |
| Composition, captions and graphics | `motion-remotion` + local `remotion-best-practices` | Frame-driven shared preview/export, original Thai/English text and correct audio timing |
| Sound | `earshot` + existing audio tools | Event timing, measured levels, supported sound judgments; distinguish ASR from human listening |
| Edit, encoding and delivery | `motion-ffmpeg` | Motivated cuts, coherent color/audio, full-file decode and stream checks, actual review limitations |

`canvas-design` governs its static art stage; its PNG/PDF output scope does not replace
the video workflow. `cinematic-product-commercial` is not a reason to add branded
product campaign gates to an unrelated culture explainer: reuse the relevant camera,
lighting, staging and rough-cut review discipline. A cinematic quality bar is not a
credit-purchase authorization.

## Resolve conflicts before implementation

Physical constraints and the shared deterministic render contract take precedence
over a stylistic shortcut. Reject blanket rules such as “every limb must lag,”
“every shot must keep moving,” or fixed screen-angle anatomy. Do not copy a rigid
delay into a held prop, or treat UI spring durations as cinematic action timing.

Verify runtime availability. The local doctor on 5 Nov 2026 resolved Remotion
4.0.538, Three.js, Matter.js and Rapier compat; GSAP and several optional engines
were not resolvable. This is an observation, not a permanent guarantee or a test of
every integration. Blender/Cycles is installed separately. Do not upgrade Remotion
because an upstream skill currently advertises another version.

## Consult upstream without overwriting local contracts

Primary upstream skills inspected on 5 Nov 2026:

- [Remotion's skills](https://github.com/remotion-dev/skills/blob/main/skills/remotion-best-practices/SKILL.md):
  routing to focused authoring/composition guidance. Keep BigO's API ownership,
  installed version and deterministic export contract authoritative.
- [Anthropic canvas-design](https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md):
  design philosophy and deliberate static composition. Use original work; do not
  copy an artist or assume static design guidance supplies character animation.

No remote skill installation or dependency change was needed for this composition.
If a missing capability becomes necessary, identify the smallest addition and its
actual compatibility/cost before using it. For each reused source, distinguish a
text-read reference from a film/animation actually inspected.

## A sample has to demonstrate the chain

Keep one shot record: brief → selected skills and reason → designed asset → difficult
action → moving proof → contact/visual review → edit → technical receipt. Retain
failed takes and their failure reason. A technical study may demonstrate collision,
support or shading; it must not be renamed a finished channel film or evidence that
the whole desired production quality has been achieved.
