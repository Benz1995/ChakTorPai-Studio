---
name: gpt-motion-story
description: Create illustrated motion biographies, historical explainers and narrative documentaries (ชีวประวัติ, ประวัติศาสตร์, สารคดีเล่าเรื่อง) by combining GPT-generated raster assets with deliberately choreographed objects, maps, diagrams, typography, cameras and sound in BigO Content Studio. Use when the user wants GPT imagery and motion together or asks to avoid slide-like storytelling; not for a single static image, a simple existing diagram, an animestory one-picture-per-scene recap, or a code-only film without generated imagery (use opuscar).
---

# GPT imagery + directed motion storytelling

Owner-selected production approach: use well-designed GPT imagery as visual material
and motion as the means of explaining events. The deliverable is a watchable moving
story, not a sequence of finished pictures with uniform zooms and crossfades.

Worked example (English sample, Opuscar route): the
[Seub Nakhasathien treatment](../../../workspaces/video/ChannelLab/20261105-seub-motion/TREATMENT.md)
and its [claim record](../../../workspaces/video/ChannelLab/20261105-seub-motion/CLAIMS.md).

## Inherit the brief and existing contracts

Read [motion-studio](../motion-studio/SKILL.md) and the requested project's/channel's
own rules. Preserve language, voice, audience, budget, publication scope and existing
assets. Use the app API/MCP for app-owned content; never edit its database directly.
For frame-rendered work follow the shared [render contract](../motion-studio/references/render-contract.md).

Use this hybrid approach by default for illustrated biographies, history and narrative
documentaries when rich imagery is appropriate. Code-native maps, diagrams, labels
and existing vector assets do not need to be regenerated as raster pictures. Select
only the imagery and tools needed for the actual shot.

## 1. Story and evidence before assets

Identify the person/event, one narrative question, factual beats and an ending.
For biographies verify dates, roles and causal claims against primary/reliable
sources and keep them in a claim record (`CLAIMS.md`). Distinguish an actual quote
from authored narration. Do not invent archival documents, testimonials or a person's
facial likeness and present them as evidence.

Write a short treatment and shot plan (`TREATMENT.md`) with: time/voice beat, move,
visual event, focal object, asset layers, camera/framing, motion/contact logic,
transition, sound cue and claim source. An event changes the scene: water rises, a route
grows, a document opens, a boundary connects habitats, a person reaches and establishes
a grip. A changing subtitle is not the shot's principal action.

Choose moves from the [move library](references/moves.md) (คลังท่า): tag each line's
purpose, pick a four-to-six-move vocabulary plus one signature move for the film, and
write each beat's move ID in the `Move` column. The owner may name moves by ID or Thai name.
For a short mechanism/word explainer, a smaller vocabulary is appropriate when it
serves the facts. Preserve a continuing action across adjacent voice beats rather
than resetting the mechanism merely to meet a variety count.

## 2. Generate production assets with GPT

Use the GPT route for the agent doing the work. Do not silently switch to another
paid image/video provider. A skill does not grant purchasing or account-switch authority.

| Agent | Default GPT route | When it cannot do a step |
| --- | --- | --- |
| Codex | The available `imagegen` skill and its built-in image tool | Ask the owner |
| Claude Code | ChatGPT on the web (chatgpt.com, the owner's signed-in account) per [chatgpt-images](../chatgpt-images/SKILL.md): browser order, consistent conversations, download and filing | [playwright-mcp](../playwright-mcp/SKILL.md); then ask the owner |

The app's OpenAI API provider (`generate_images` with `OPENAI_API_KEY`) and local SDXL
are not the default GPT route; use them only when the owner asks. If ChatGPT is signed
out, ask the owner to sign in in the browser pane; never type their password. Move every
download into the content's workspace `assets/` folder; do not leave files in Downloads.

Design the asset list before generation, starting with the film's
[asset kit](references/moves.md#asset-kit) (style frame, location plates,
character views, props, blank document material, occluders) generated once and shared by
every move; generate extras only for the moves that need them. Separate foreground, middle/background,
people/props and graphic inserts when they need independent movement. Specify palette,
light direction, period, perspective, proportion, edge quality, subject clearance and
space for compositing. Use a selected style frame as the reference for every later
layer so palette, line and light match.

Generate without baked captions, fake handwriting or decorative logos. A beautiful
flattened poster is not an editable layer rig.
For science cutaways, keep counts and contents consistent when parts separate:
extracted seeds must not also remain baked into the emptied shells.

**Cutouts need real alpha.** Ask for a transparent PNG, then measure the downloaded
file; a chat download may be opaque (the app notes that `gpt-image-2` has no transparent
background). If it is opaque, regenerate the subject on a plain contrasting background
with clearance, then remove it with the app: MCP `upload_file` with `cutout: true`
(it calls `/api/cutout`, which needs the local image server, `npm run images` in
`content-studio`). Copy the result back into `assets/`. Accept a cutout only when the
subject's interior is opaque, nothing of the subject is cut away, and composited over a
contrasting test background it shows no halo or leftover background haze.
Check empty-region alpha values as well as the presence of an alpha channel; a faint
matte can still produce rectangular cards over a dark composition.
Inspect each atlas quadrant for small fragments of its neighbours. Retain the original
generation and use a documented non-destructive compositor crop when it removes only
spill; regenerate when cleaning it would cut off or change the actual subject.

**Record every asset** in `assets/ASSETS.md`, one row per file: file, role/layer,
route (imagegen, ChatGPT web conversation, cutout), verbatim prompt, date, pixel size,
alpha (none, native, cutout) and status (selected, rejected, superseded). Record
rejected attempts too; this is the image receipt the delivery step relies on.

For real people, use an identity reference only when an accurate likeness is needed,
the owner may use that photo (their own, licensed, public domain or otherwise permitted)
and the image service allows it. Otherwise use a clearly interpretive scene, a
non-identifiable back view or another honest visual treatment; do not call an invented
face an authenticated portrait. Retain an illustration/reconstruction disclosure
appropriate to the project and the destination platform.

## 3. Animate the story, not just the image frame

Choose the composition route from what must move:

| What the shot needs | Route |
| --- | --- |
| One picture per beat with labels, callouts, a library graphic or shader | Existing Content Studio templates through the API/MCP (`set_scene_image`, `scene.labels`, `scene.fx.graphic`); a scene holds one `imageUrl` |
| Several independently moving raster layers, occlusion, drawn maps, paper inserts | An [opuscar](../opuscar/SKILL.md) Canvas page that loads the workspace PNGs; set `window.READY` only after images and fonts load. Content Studio can still own the voice; mux with FFmpeg |
| Layered composition kept inside the app | A new Remotion template via [motion-remotion](../motion-remotion/SKILL.md) and [remotion-best-practices](../remotion-best-practices/SKILL.md) |
| A short pose-changing action, flipbook or reusable subject loop from generated drawings | [frame-sequence-animation](../frame-sequence-animation/SKILL.md): a consistent sprite sheet or ordered poses, then timed GIF/MP4 or explicit frame selection |
| Articulated limbs, grip or contact | Generated part layers on a rig ([gsap](../gsap/SKILL.md), on-demand) or a [studio-3d](../studio-3d/SKILL.md) shot |

Combine only relevant existing skills:

- `canvas-design` / `art-motion`: asset craft, palette, composition and visual hierarchy.
- `animation-principles`: support, arcs, timing/spacing, preparation, contact and settling.
- `studio-3d`, `motion-threejs` or baked physics: when geometry, materials or contact need control.
- `gsap` (on-demand) or native frame-driven transforms: layered timelines and rigs.
- `motion-remotion` or `opuscar`: deterministic composition and export.
- `earshot` / `motion-ffmpeg`: sound evidence, mix and final-file checks.

Use the [production stack](../motion-studio/references/production-stack.md) to resolve
scope and conflicting advice. Avoid installing a library for an effect existing tools cover.

Create spatial continuity: foreground occludes, camera movement reveals, a prop retains
its identity, a map or paper insert emerges from the scene. Keep screen direction and
depth consistent. Designed parallax can support a scene, but a slow zoom on each
flattened asset cannot substitute for a meaningful visual event throughout the film.

Use acceleration, grip/support and physical response suited to the medium. Do not force
every layer to wobble, spring, lag or move continuously. Purposeful rests let an outcome
register. Do not claim physical realism from particle noise, a solver toggle or a score.
Keep motion within the asset's actual structure: a flattened person can be staged in
depth but cannot convincingly walk or reach by bending the entire bitmap. Generate
compatible pose/part layers or use a rig/3D shot when articulation or contact is needed.

Set typeset names, dates, captions and map labels in the compositor, not in the image
generator. Keep them subordinate to the focal action, readable at phone size and timed
to measured narration. Use the project's Thai fonts for Thai text and break Thai lines
at word boundaries, never inside a word. Avoid recurring oversized title panels or card
layouts that replace the scene at every sentence.

## 4. Prove the difficult shot before the full film

Follow the representative-shot review in
[motion-quality.md](../motion-studio/references/motion-quality.md): render a short
moving interval with the main visual event and its transition, inspect continuous
playback when available plus dense frames around contact/occlusion, and state the
limitation if only frames were reviewed.

For this workflow also reject and revise: slideshow-like progression, crude or
mismatched assets, style drift between generated layers, morphing identity across
generations, broken alpha/halos, a whole bitmap bent to fake articulation, unsupported
floating, irrelevant effects, uniform pacing or captions hiding the event. Improve the
failed upstream decision (asset, layer split or route) before rendering a batch.

## 5. Finish and deliver

Retain `TREATMENT.md`, `CLAIMS.md`, `assets/ASSETS.md`, shot timings, voice attempts and
editable motion source. Encode a playable video and verify the actual file: duration,
streams, full decode, first/last frames, transitions, captions and measured audio.
Treat ASR, technical QC, visual review, human listening and owner approval as separate
evidence. After the review, update each used move card's status and log in the
[move library](references/moves.md), including failures.

Deliver the moving film, not only stills, a contact sheet or a plan. Link the research
and sources separately as the project requires. Generating a local sample does not
authorize channel creation or publication. Describe unresolved quality limits honestly.
