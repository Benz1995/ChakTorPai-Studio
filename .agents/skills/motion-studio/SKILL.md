---
name: motion-studio
description: "Plan, create, revise, and package content videos in BigO Content Studio through AI chat, Cowork, Codex Work and local production tools (ทำคลิป, ทำวิดีโอ, วางแผนคลิป, เลือกเครื่องมือ). Use for a complete content workflow, Director Studio handoff or tool selection; use a specialist directly for a single named tool."
---

# Motion Studio

Turn a content brief into a reviewable video using this project's existing editor,
media providers, and Remotion pipeline. These are locally authored workflow skills
adapted to the user's repository list, not upstream code installations or a claim
that all twenty tools are already integrated. They are model-independent.

## Start with the project

Read [project-integration.md](references/project-integration.md) for paths, data
ownership, API/MCP entrypoints, and the production sequence. For animation, physics,
3D, generated audio, or a new renderer, also read
[render-contract.md](references/render-contract.md). For any clip meant for a feed
(Reels, Shorts, TikTok, Facebook), or a question about reach and "the algorithm",
read [platform-distribution.md](references/platform-distribution.md).

Inspect the requested existing project/content and its assets before creating or
regenerating work. Reuse session decisions about brand, language, voice, destination,
budget, and authorization. Resolve ordinary creative choices yourself; ask only
when missing information changes the result materially.

For reusable Director Studio recipes, the owner's primary workflow is AI chat /
Cowork / Codex Work with actual reference files, followed by local assembly and
QC. Read [chat-local-production.md](references/chat-local-production.md) for the
saved recipe → brief/handoff → real outputs → collect workflow. Use the chat's
available image tools directly when suitable; this route does not require an API
key. Preserve an explicit channel/provider choice. Preparing a handoff creates
files for the chat to open; it does not launch a chat or generate media itself.

For real places, events, products or factual explainers, research relevant primary
sources on the web and use real reference material before substituting invented
data or geography. A missing local importer is an implementation gap, not proof
that the source cannot be used. Reuse browser-captured map imagery, footage or
open datasets when suitable; retain source/date/attribution and disclose actual
coverage or accuracy limits. Use synthetic stand-ins when the brief calls for
them, or when a concrete access gap remains, and identify that gap explicitly.

For Google Flow / Veo shots inside BigO (UGC presenters such as อิงเอย, B-roll), use
[google-flow](../google-flow/SKILL.md). For KinJi Shopee affiliate clips, use
[shopee-affiliate](../shopee-affiliate/SKILL.md). For linked MovieSkit series or
standalone films, read the MovieSkit skill file
`C:/Users/usEr/.codex/skills/movieskit-short-drama/SKILL.md` (a Codex skill: open it as a
file) and the film's current handoff. Preserve Google Flow's native dialogue and sound rather than invoking a
new narration/stem-separation pipeline by default. Physical-action review covers
the complete used motion interval and dense contact transitions; sampled stills,
ASR and clean decode do not establish that hands, props or feet avoid penetration.
The MovieSkit skill's native-audio/physical-action reference owns these film rules.

Choose the smallest useful tool combination. Existing React/Remotion layouts and
FFmpeg cover many clips. Add an optional dependency only when the requested result
benefits from it; check its installed version and current upstream instructions.
Do not install the whole catalogue as a prerequisite.

For subject animation, cinematic samples, or feedback that a video feels like a
slideshow, read [motion-quality.md](references/motion-quality.md) before producing
another version. Review one representative moving shot before batching. A pan,
zoom, changing card, moving caption, or successful decode is not evidence of
convincing subject action or engaging direction.

For combining existing design, animation and finishing skills into a professional
production, use [production-stack.md](references/production-stack.md). Select a
coherent chain for the shot; do not install or invoke the entire catalogue.

For a format-led explainer (a chart revealing evidence, packets traversing an
architecture diagram, annotated replay, exploded object or geographic journey),
read [visual-formats.md](references/visual-formats.md). Select a visual mechanism
that explains the claim, bind its events to reviewed narration timings, and reuse
the current template/effect before proposing a new renderer. The recipes distinguish
existing primitives from authoring work and unimplemented data integrations.

**Illustrated narrative rule:** for biographies, historical explainers and documentary
stories that need rich illustration, prefer the owner's GPT-imagery + directed-motion
approach in [gpt-motion-story](../gpt-motion-story/SKILL.md). Generate separable assets,
then animate meaningful events and integrate maps/diagrams/type; do not deliver a
slideshow of flattened pictures. Keep simple code-native graphics code-native.

**Visual route selection:** for a new video or substantial visual redesign, compare
the routes relevant to the shot: existing designed graphics/effects, GPT imagery
with directed layers, [frame sequences](../frame-sequence-animation/SKILL.md), rigs/3D
or the project's approved footage/provider workflow. Briefly record the choice by
look, subject action, control, generation effort and reusable assets. A multi-frame
pose sequence is a useful alternative for short actions and loops, not a mandatory
replacement for every shot. Prove one moving shot before batching; exporting at a
higher FPS does not add new poses. Preserve an already selected creative direction.

For professional work built from GIFs or pose sheets, use the
[frame-sequence production workflow](../frame-sequence-animation/references/professional-production.md)
before batching: preserve RGBA masters, budget native subject pixels at the largest
shot scale, direct exposures and contact, then review the edit and actual export path.

## Route to independently callable specialists

| Need | Skill |
| --- | --- |
| React compositions, scene templates, final video | [motion-remotion](../motion-remotion/SKILL.md) |
| A separate HTML-to-video workflow | [motion-hyperframes](../motion-hyperframes/SKILL.md) |
| Seekable timeline choreography | [motion-animejs](../motion-animejs/SKILL.md) |
| Spring motion in interactive UI | [motion-react-spring](../motion-react-spring/SKILL.md) |
| Dense GPU 2D scenes | [motion-pixijs](../motion-pixijs/SKILL.md) |
| Generative drawing | [motion-p5js](../motion-p5js/SKILL.md) |
| Vector paths and SVG construction | [motion-paperjs](../motion-paperjs/SKILL.md) |
| 2D rigid-body motion | [motion-matterjs](../motion-matterjs/SKILL.md) |
| 3D cameras, objects, lighting | [motion-threejs](../motion-threejs/SKILL.md) |
| Blender renders, studio3d template, Poly Haven, Mixamo, splats, image-to-3D | [studio-3d](../studio-3d/SKILL.md) (project skill outside the twenty) |
| 2D/3D rigid-body collisions | [motion-rapier](../motion-rapier/SKILL.md) |
| Lightweight WebGL and custom shaders | [motion-ogl](../motion-ogl/SKILL.md) |
| Particle systems | [motion-tsparticles](../motion-tsparticles/SKILL.md) |
| Optimize glTF/GLB assets | [motion-gltf-transform](../motion-gltf-transform/SKILL.md) |
| Shader-based scene transitions | [motion-gl-transitions](../motion-gl-transitions/SKILL.md) |
| Record a selected screen/window | [motion-obs](../motion-obs/SKILL.md) |
| Optional Chatterbox narration | [motion-chatterbox](../motion-chatterbox/SKILL.md) |
| Synthesized music and effects | [motion-tonejs](../motion-tonejs/SKILL.md) |
| Transcribe audio and propose caption timing | [motion-faster-whisper](../motion-faster-whisper/SKILL.md) |
| Optional external timeline editing | [motion-opencut](../motion-opencut/SKILL.md) |
| Inspect, encode, mix, and deliver files | [motion-ffmpeg](../motion-ffmpeg/SKILL.md) |

Companion project skills outside the twenty:

| Need | Skill |
| --- | --- |
| Code-only short films, explainers and keynotes with the local Opuscar runtime | [opuscar](../opuscar/SKILL.md) |
| Art style cards and explainer storytelling grammars | [art-motion](../art-motion/SKILL.md) |
| GPT-generated illustration layers combined with directed narrative motion | [gpt-motion-story](../gpt-motion-story/SKILL.md) |
| Ordered image poses, sprite sheets, flipbook/stop motion and reusable GIF/MP4 assets | [frame-sequence-animation](../frame-sequence-animation/SKILL.md) |
| Timing, choreography and joint limits before animating characters | [animation-principles](../animation-principles/SKILL.md) |
| Multi-layer cutout rigs and nested timelines (GSAP, on-demand) | [gsap](../gsap/SKILL.md) |
| Remotion code rules: determinism, clamping, asset loading | [remotion-best-practices](../remotion-best-practices/SKILL.md) |
| One brief → 3 hooks × 3 ratios × 2 CTAs ad matrix | [campaign-matrix](../campaign-matrix/SKILL.md) |
| Posters, cover art and title cards as PNG/PDF | [canvas-design](../canvas-design/SKILL.md) |
| UI motion in the Content Studio editor (not exported video) | [animate](../animate/SKILL.md) |
| Measure, compare and design sound | [earshot](../earshot/SKILL.md) |
| Local FFmpeg edits, captions and reframing | [ffmpeg-skill](../ffmpeg-skill/SKILL.md) |
| FlowMusic sound effects into the sound library | [flowmusic-sfx](../flowmusic-sfx/SKILL.md) |
| Songs: Suno (primary for Elyndraze) or FlowMusic (secondary) | [suno](../suno/SKILL.md), [flowmusic](../flowmusic/SKILL.md) |
| Elyndraze lyrics (Thai song form, rhyme, Suno pack) | [thai-hit-songwriter](../thai-hit-songwriter/SKILL.md) |
| Browser automation when the built-in browser cannot do the step | [playwright-mcp](../playwright-mcp/SKILL.md) |
| GPT images made in ChatGPT on the web: browser, consistency, download, attach | [chatgpt-images](../chatgpt-images/SKILL.md) |
| Google Flow / Veo shots: Characters, credits, uploads, speech strip, import | [google-flow](../google-flow/SKILL.md) |
| Thai narration: pacing, voices, pronunciation, Thonburian ASR, Thai subtitles | [thai-voiceover](../thai-voiceover/SKILL.md) |
| KinJi Shopee affiliate clips and the owner's posting table | [shopee-affiliate](../shopee-affiliate/SKILL.md) |
| Multi-agent creative QA: reality, physics, story logic, emotion, lyrics, visual continuity | [creative-reality-auditor](../creative-reality-auditor/SKILL.md) |

Ready-made, frame-driven effects already in the app — the `audiodash` music-visualiser dashboard template, 149 shader backgrounds/overlays (manga/anime, skies and galaxies, nature, cyber/data, show overlays),
14 pattern wipes and 34 Thai-ready graphics (lower third, chapter title, stats, charts,
quote, price tag, checklist, timeline, comparison, callout, end card, and 14 music cards
that react to the real song: now playing, visualizers, vinyl, cassette, chords, piano, mixer; styles and accent
colors, 9:16 and 16:9) via `scene.fx` and `settings.overlayId` — are listed in the
[effects library](../../../content-studio/docs/effects-library.md); prefer them before adding a dependency.

Read only the selected specialists. Each contains upstream links, an integration
approach, and observable checks. See [recipes.md](references/recipes.md) for concrete
content combinations. Tool and source inventory is in
[catalog.json](../../../docs/motion-studio/catalog.json).

## Deliver the requested content

1. Establish audience, hook, message, approximate duration, aspect ratio, language,
   visual direction, and available assets from the request and current project.
2. Draft a scene plan: narration, visual action, on-screen text, and sound cues.
   Keep product claims and prices grounded in supplied facts. For feed clips, open on
   the strongest image and promise within 1–2 seconds, keep an open loop with a new
   beat every few seconds, fit length to content, and end with a genuine question or
   a reason to send/save — never an engagement-bait prompt.
3. Reuse or extend an appropriate template. Keep asset generation and expensive
   simulation outside frame rendering. Preserve the Thai text/timing pipeline.
4. Produce only the assets needed, persist the content, and read back its latest
   state before voice generation or rendering. For a chat handoff, collect the real
   returned files through Director Studio before binding them to a motion or shot;
   keep source masters and creation notes alongside the outputs.
5. Inspect representative frames and a short motion test; check speech, Thai line
   breaks, scene boundaries, and any simulation or shader seek behavior. For feed
   clips run `npx tsx scripts/retention-check.ts <contentId>` in `content-studio`
   and fix the warnings that apply (long opening, looping footage, bait, ending).
6. Render and verify the requested delivery file; rerun the retention check for its
   loudness and true peak. Report paths, dimensions, duration, actual providers,
   checks performed, and remaining review limitations. Do not predict reach.

## Narration that sounds spoken

Thai AI narration sounds read-aloud when lines are dense or over-directed. The full
voice workflow (voice choice, pronunciation, ASR checks, Thai subtitles) is in
[thai-voiceover](../thai-voiceover/SKILL.md). When writing scene text for any voice:

- Keep one idea per scene, roughly 10–12 spoken letters per second; the editor
  flags voiced scenes above 12.5 (⚠ พูดเร็ว). Split or shorten instead of
  squeezing more facts into a fixed scene length.
- Write it the way a person says it: short clauses, commas and spaces where the
  breath goes, natural particles (นะ, เลย, อ่ะ) where they fit the character.
- Use a delivery tag (`[สดใส]`, `[เหนื่อย]`) only where the mood changes, not on
  every line; ElevenLabs v3 over-acts when every scene is tagged.
- Numbers, ranges and common brand terms become Thai readings automatically
  (`5,979`, `2-12`, `Type-C`); check the 🔊 spoken preview and add unusual names
  (game titles, product models) to the pronunciation dictionary before voicing.
- ElevenLabs v3 voices should stay on stability 0.5 (Natural); 0 (Creative)
  drifts in tone between scenes.

Use an identifiable output directory for supporting assets and production notes,
such as `content-studio/out/content/<content-id>/`. The app owns its media and
render locations; do not relocate its referenced files. A local export, editorial
approval, and platform publication are separate states. Publishing or messaging
is performed only when requested and supported by destination evidence.
