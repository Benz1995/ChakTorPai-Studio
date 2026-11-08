# Practical content recipes

Treat these as selectable approaches, not mandatory multi-library stacks.

For chart-led evidence, architecture request journeys, exploded objects, annotated
replay and geographic storytelling, use [visual-formats.md](visual-formats.md) for
event planning, existing starting points and the boundary between authoring and
missing integrations.

| Brief | Start with | Add when needed | Result and key check |
| --- | --- | --- | --- |
| Thai knowledge short, 30-60 seconds | Existing Remotion Explainer/Callout + F5 voice + FFmpeg | Anime.js for complex seekable choreography | Readable Thai, narration-led highlights, inspect boundaries and audio sync |
| Affiliate product short | KinJi Shopee clips: [shopee-affiliate](../../shopee-affiliate/SKILL.md) (animestory chibi, hook → gag → product, regenerated product image, no prices); other shops: existing Affiliate template + real product photo | Three.js for a supplied 3D product, glTF Transform for asset size | Product identity and factual claims survive motion; compare to source |
| Physics explainer | Remotion + Matter.js | Rapier for 3D collision behavior | Precomputed fixed-step trajectory; random seek agrees with sequential playback |
| 3D product hero | Three.js + Remotion + FFmpeg | glTF Transform, OGL only for a specific shader need | Known lighting/camera, local optimized assets, actual headless test |
| Music visual or generative background | p5.js or PixiJS, chosen by rendering needs | tsParticles for a supported particle system, offline Tone.js for original effects | Seeded generation, safe text contrast, no live export clock |
| HTML promo already supplied | HyperFrames as a separate render path | FFmpeg for packaging | Verify renderer's current project/seek contract; import resulting asset intentionally |
| Tutorial/demo | OBS selected window capture + Remotion packaging | faster-whisper to propose transcription | Explicit capture source, legible UI, corrected Thai transcript, no unintended windows |
| External editorial pass | Exported MP4/assets + a verified working OpenCut release | FFmpeg for delivery | Preserve source package; verify current OpenCut capability before promising API automation |
| Story recap for Reels/Shorts | Recap Studio via MCP (`start_recap` → `analyze_shots` → `create_recap_contents`) with narration written from the full transcript, ranges picked on real shot cuts from its contact sheets, its `custom:` themeId | Sound library cues, a 16:9 version reusing the same voice | Hook in the first 1–2 s, no looping footage, credit the source; `scripts/retention-check.ts` before and after render |

## Example requests

Codex explicit invocation:

```text
$motion-studio ทำคลิปความรู้ภาษาไทย 45 วินาที แนว Callout เรื่องแรงกดอากาศ
ใช้เสียงและแบรนด์ของโปรเจกต์เดิม ส่ง MP4 แนวตั้งพร้อมภาพตรวจแต่ละฉาก

$motion-matterjs ทำแอนิเมชันลูกบอลตกกระทบพื้นสำหรับฉากที่ 2
ให้เปิดตรงเฟรมไหนก็ได้ผลเหมือนกัน และเชื่อมกับ Remotion เดิม

$motion-threejs ทำช็อตหมุนสินค้าจากไฟล์ GLB ที่ให้มา
ตรวจตัวอย่างกับไฟล์เรนเดอร์จริง ใช้ motion-gltf-transform เมื่อไฟล์หนัก

$motion-ffmpeg ตรวจ MP4 ที่เรนเดอร์แล้วและทำไฟล์ส่งมอบตามสเปกที่ระบุ
```

Claude Code uses `/motion-studio`, `/motion-matterjs`, `/motion-threejs`, or
`/motion-ffmpeg` with the same request. Natural-language invocation is also enabled
by the descriptions; the skills are not pinned to any particular model/version.

## Minimal production note

Alongside a requested final asset, record enough to resume the work: content and
render IDs, source assets and actual providers, selected libraries/versions, seed
or baked simulation parameters where relevant, output path/specification, checks
performed, and any material unfinished requirement. Reuse the current project's
existing notes if present instead of creating a parallel tracking system.
