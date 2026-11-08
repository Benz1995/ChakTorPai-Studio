---
name: polytale-series
description: Produce episodes for the PolyTale (โพลีเทล) channel — serialized Thai fiction told as 3D low-poly chibi vertical reels (9:16, 60–105 s, real survival lessons from verified official sources, Thai voice + yellow Thai subtitle + small English subtitle, countdown/day devices, viewer-choice cliffhanger) — with the exact pipeline proven on series "วันที่ 0": ChatGPT web images and transparent acting layers, a relative-timed timeline.json, the bundled compositor (grade, grain, rack focus, whip, depth, blinking, character swaps), ElevenLabs real sound effects/score/character lines, Content Studio narration with ASR checks, safe-zone QC. Use for any PolyTale or วันที่ 0 work (ตอนใหม่, ทำตอนต่อ, ซีรีส์ 3D, เรื่องแต่ง, เล่าเรื่องแนวตั้ง) and to start a new PolyTale series. No Google Flow, no paid video generation.
---

# PolyTale series episodes

PolyTale (โพลีเทล) is the owner's channel for serialized fiction: one story per series,
10–12 numbered episodes, each a vertical reel with a hook and a cliffhanger, in a dark
**low-poly chibi 3D** look. Everything moving is made from **still images and layers**
composited in code — the owner ruled out Google Flow for this channel (7 Nov 2026).
This skill is complete on its own: follow the steps in order and an episode comes out
the same way every time, whichever AI runs it.

Taking over a running series? Read `workspaces/video/PolyTale/HANDOFF.md` first.

Read first: the channel bible `workspaces/video/PolyTale/CHANNEL.md` and the series bible
`workspaces/video/PolyTale/series/<series>/SERIES.md` (characters, layers, episode list,
ChatGPT conversation URL, Content Studio ids). The reference episode is
`workspaces/video/PolyTale/series/day0/ep01/` (`SHOTS.md`, `timeline.json`, images, audio,
`render/day0-ep01.mp4`) — copy its structure and its timeline style.

## 0. Rules that never change

- All user-facing text is Thai. On-screen: Thai line bold yellow (Kanit), English line small
  white on black under it, `(เรื่องแต่ง)` on the title card. No real countries, leaders or
  brands in the story; Thai places and streets are fine.
- No Google Flow / Veo / paid video. Images: ChatGPT web (owner's account) through the
  browser. Motion: `scripts/shots.py`. Narration: ElevenLabs `FfrJDiyJZK` (owner's voice)
  through Content Studio. Sound effects, score and extra character voices: ElevenLabs API via
  `scripts/audio_gen.py` (same key, small credit cost — report what was generated).
- One ChatGPT conversation per series (URL in SERIES.md); reuse `series/<series>/characters/`.
- Files: save without asking, always inside the BigO folder, never left in Downloads.
- Nothing is posted automatically. Deliver the MP4 plus the posting line.
- Report honestly what was checked (frames, ASR, earshot matches, loudness) and say
  "not listened to by a person" until the owner has listened.
- **Visual Stacking & Layer Conflict Rules (กฎห้ามข้อความทับซ้อนเด็ดขาด — บทเรียนสำคัญจากงานสร้างจริง)**:
  1. **Lesson Cards (`lessons`)**: การ์ดบทเรียนเต็มจอ ("ถ้าเจอจริง", "บทเรียนจากความผิดพลาด", "สรุปบทเรียน") มีหัวข้อ รายการ 3 ข้อ ที่มา และเครดิตด้านล่างอยู่แล้ว **ห้ามใส่ซับไตเติล (`th`/`en`) ทับลงบนการ์ดเด็ดขาด** (ให้ใส่เสียงบรรยายผ่าน `tl["vo"]` หรือช็อตที่มี `th: null`) เพื่อไม่ให้ซับด้านล่างล้นขึ้นมาทับข้อความบทเรียนและเครดิต
  2. **Choice Cards (`choice`)**: การ์ดเลือกทางเลือก (A/B) กินพื้นที่กลางจอ y=640..1150 **ห้ามใส่ซับไตเติล (`th: null`) ในช็อตนี้** เพราะการ์ดแสดงคำถามและตัวเลือกชัดเจนอยู่แล้ว
  3. **Follow Button (`follow`)**: ปุ่มติดตาม (y=1240..1430) **ห้ามวางซ้อนในช็อตเดียวกับ `choice` หรือซับไตเติลเด็ดขาด** เพราะปุ่มจะทับข้อความซับไตเติล ให้แยกเป็นช็อต Outro ปิดท้ายต่างหาก หรือวางคู่กับการ์ดสรุป/Title ที่ไม่มีซับไตเติล
  4. **Outro & Choice Hold Times (เวลาค้างตอนจบเพื่อให้คนดูอ่าน/ตอบโพลทัน — บทเรียนจากคนดูจริง)**:
     - **Choice Card (`choice`)**: ต้องค้างภาพตัวเลือก A/B ไว้อย่างน้อย 5–6 วินาทีก่อนตัดช็อต (รวมความยาวช็อต 13–15 วินาที) เพื่อให้ผู้ชมมีเวลาอ่านตัวเลือกและคิดคอมเมนต์
     - **Outro & Follow Card (`follow`)**: ช็อตปิดท้ายที่มีปุ่มติดตามและสรุปบทเรียน ต้องค้างไว้อย่างน้อย 7–8.5 วินาที (ให้มีเวลาอ่านและกดออกทัน ไม่ตัดจบห้วน)
  5. **Thai Subtitle Metrics & Wrapping**: ภาษาไทยไม่มีช่องว่างระหว่างคำ การตัดบรรทัดใน `subs.py` ต้องวัดความกว้างฟอนต์จริงเทียบกับ `max_w = 760 px` (Safe zone ซ้าย-ขวา >= 150 px) และคนแต่งบทต้องใส่ `+ NL +` ที่รอยต่อวรรคธรรมชาติ (<= 18-20 ตัวอักษร) **ห้ามตัดกลางคำหรือให้มีเศษสระ/พยัญชนะตกค้าง (เช่น \Nจ)**
  6. **Audio Continuity**: ดนตรีประกอบต้องเป็นแทร็กต่อเนื่องตลอดคลิป (`full_score.mp3`) ใช้ sidechain ducking ที่นุ่มนวล (`ratio 1.6, threshold 0.18`) เพื่อรักษา Music Presence >= 80% ให้ผ่านเกณฑ์ Launch-grade ของ Earshot
  7. **Voiceover-First Sound Mix (เสียงพากย์ต้องเป็นพระเอกเสมอ — กฎเหล็กจากผู้ฟังจริง)**:
     - **เสียงพากย์ (Voiceover Gain)**: บังคับตั้ง `vo_gain: 1.45` ใน timeline.json เสมอ เพื่อยกเสียงพูดของตัวละครและคนบรรยายให้ลอยเด่น คมชัด อยู่หน้าสุดของมิกซ์
     - **การ Ducking ดนตรีเมื่อมีเสียงพูด**: ตั้ง `duck: {ratio: 4.5, threshold: 0.08}` เพื่อกดเสียงดนตรีและเสียงแวดล้อมลงทันที -10dB ถึง -14dB ขณะมีเสียงพูด
     - **ดนตรีพื้นหลัง (Background Music Bed)**: ตั้งระดับเบาคลออารมณ์ที่ `gain: 0.18–0.22` (ห้ามเกิน 0.25)
     - **เสียงรบกวน/เสียงแหลม (รถ, คนกรีดร้อง, ฝูงชน)**: ตั้งเบามาก `gain: 0.08–0.10` เป็นเพียงแบ็กกราวนด์ไกล ๆ
     - **เสียง Foley, รอยต่อช็อต และเสียงกระแทก**: `cut_sfx <= 0.08`, Foley ในห้อง `0.10–0.15`, เสียงกระแทก/ตูม `0.25–0.30`, End Sting `0.40` เพื่อไม่ให้มีเสียงใดดังแซงหน้าเสียงพากย์เด็ดขาด
  8. **Visual-Script Semantic Coherence (กฎความสัมพันธ์ระหว่างภาพและบทพากย์ 1:1 — ห้ามภาพไม่ตรงกับเสียงเด็ดขาด)**:
     - **Time & Location Continuity (ความต่อเนื่องของเวลาและสถานที่)**: เมื่อเนื้อเรื่องดำเนินผ่านเหตุการณ์สำคัญไปแล้ว (เช่น หลบเข้าห้องใต้ดินในวันที่ 1) **ห้ามนำภาพฉากเก่าที่ไม่เข้ากับสถานการณ์มาใช้ซ้ำเด็ดขาด** เช่น ห้ามนำภาพประตูบ้านไม้วันฟ้าสว่าง (`doorway.png`) หรือภาพหน้าต่างมองเห็นคนวิ่งบนถนนตอนเช้า (`window-street.png`) มาใช้ในวันที่ 1 ในห้องใต้ดิน
     - **Semantic Specificity (วัตถุและเหตุการณ์ต้องตรงกับบทพูด)**:
       * บทพูดถึง "ข้อความแจ้งเตือนบนมือถือ / วิทยุเตือนภัย" -> ภาพต้องเป็นหน้าจอมือถือ/วิทยุที่มีการแจ้งเตือนจริง (`alert-water-phone.png`) ห้ามใส่ภาพคนวิ่งนอกหน้าต่าง
       * บทพูดถึง "เสียงเคาะ/คนตะโกนอยู่นอกประตูเหล็กใต้ดิน" -> ภาพต้องเป็นประตูเหล็กห้องใต้ดินที่มีสลักหนาแน่น (`bunker-hatch-locked.png`) หรือภาพมุมมองผ่านช่องแง้ม ไม่ใช่ภาพเปิดประตูบ้านไม้ยืนดูวิว
       * บทพูดถึง "ถอดเสื้อผ้า / ล้างตัว / ถังน้ำลด" -> ภาพต้องเป็นกิริยานั้นตรงตัว (`bag-clothes.png`, `wash-soap.png`, `water-tank-radio.png`)
     - **Character Identity & Style Consistency (ห้ามตัวละครเพี้ยนเด็ดขาด — ต้องเจนในเธรด ChatGPT ประจำซีรีส์เท่านั้น)**:
       * ภาพทุกภาพที่มีตัวละคร (ครูเอก, ต้นกล้า, ข้าวตู, น้าสมศักดิ์) **ต้องเจนผ่านห้องแชต ChatGPT เดิมของซีรีส์เท่านั้น** (`https://chatgpt.com/c/6aee0d87-9e90-83ec-858f-6c64f613fc89`)
       * **ห้ามใช้ AI โมเดลภายนอกอื่น (เช่น Flash Image)** มาเจนตัวละครเด็ดขาด เพราะสไตล์ 3D โพลีกอน โครงหน้า ทรงผม แว่นตา และเสื้อผ้าจะเพี้ยนจากต้นฉบับทันที
       * เมื่อต้องการภาพช็อตใหม่ ให้ส่งพรอมต์เข้าไปในเธรดเดิมโดยอ้างอิง *"Same exact 3D low-poly chibi faceted origami style and the exact same character design as established in this thread"* เพื่อให้ AI ยึดโมเดลตัวละครเดิม 100%
  9. **Branching Routes for Every Episode (ระบบผลิตวิดีโอทางเลือกคู่ขนาน A/B ทุกตอน)**:
     - เนื่องจากทุกตอนจบด้วยการ์ดโหวต A/B ตอนถัดไปจะต้องมี 2 เวอร์ชันเสมอ:
       * **เส้นทางหลัก (Route A / Good / Survival Path)**: เนื้อเรื่องที่รอดชีวิตและแก้ปัญหาถูกต้อง
       * **เส้นทางทางเลือก / บทเรียนราคาแพง (Route B / Bad End / Alternative Path)**: ตอนที่พาผู้ชมไปสัมผัสผลลัพธ์ของการตัดสินใจที่ผิดพลาด เพื่อสอนบทเรียนความปลอดภัยจากความผิดพลาด (Failure Lesson Card)
     - โครงสร้างโฟลเดอร์: `epNN/` (Route A) และ `epNN_badend/` หรือ `epNN_alt/` (Route B) โดยทั้งสองเส้นทางต้องได้รับการผลิตด้วยมาตรฐานภาพ เสียง และบทเรียนจริงระดับเดียวกัน


## 1. Write the episode (SHOTS.md)

Episode folder `series/<series>/epNN/` with `SHOTS.md`, `timeline.json`, `images/`,
`audio/`, `render/`, `review/`.

Story craft (what makes it professional rather than a slideshow):
1. **Hook in the first 2 s**: an extreme close-up and a direct question to the viewer
   ("ถ้าคุณมีเวลาแค่สิบห้านาที… คุณจะเอาอะไรติดตัวไป"). Never open on a title.
2. **Calm before the turn**: 1 shot of ordinary life, so the turn hurts.
3. **One idea per shot, 2–6 s**, a voice line per shot; vary the size — extreme close-up,
   medium, wide, top-down, over-the-shoulder, from behind — never three similar framings in a row.
4. **Series devices** on screen: the day stamp, the countdown or counter, the recurring object
   (วันที่ 0: the brother's plush dinosaur). Reuse them every episode.
5. **A character voice** at the emotional peak (a short line in their own voice, `lines`).
6. **Smash to silence** before the big event: heartbeat → the music and world cut on the frame
   of the flash → boom → ringing → aftermath piano.
7. **End on a viewer choice** (A/B card, comments decide the next episode) or a question, then the
   title card. Recap previous episode in 2–3 s at the start from episode 2 on.
Narration & Dialogue: MUST strictly follow `.agents/skills/thai-craft/SKILL.md` (Zero
English calques, anti-calque vault, 7 Thai storytelling moves, natural dialogue with proper
Thai registers and particles like ครับ/ค่ะ/ลูก/ไอ้หนู, verb-serial experiential flow instead of
telegraphic noun lists). Second person "คุณ" or close third person, short clauses, `…` for
spoken pauses, 10–12 Thai letters per second. Pass the 3-second spoken test. Present the Thai
draft to the owner for review before generating voice. Run the Thai second reader
(`content-studio/docs/thai-language-review.md`: `lms load …`, `lms server start`,
`scripts/thai-language-review.py`, then unload) and apply only suggestions that improve the line;
keep the series voice.

## 1b. Teach something real (owner, 7 Nov 2026)

Every episode teaches practical, true survival or life skills inside the drama — the story
makes the viewer care, the lesson makes the clip worth saving and sharing.

- **Research first, then analyse** (owner, 7 Nov 2026: "ต้องหาข้อมูลที่มีอยู่จริงแล้ววิเคราะห์ให้ดี").
  For each topic a web subagent reads the official pages **at source** (no snippets), Thai
  authorities first (e.g. ปส./OAP for radiation, ปภ. for disasters, กรมควบคุมโรค for health) plus
  international ones (WHO, IAEA, CDC, Ready.gov), and writes `series/<series>/research/<topic>-<date>.md`:
  what each source says with exact numbers and URLs, where they agree, where they differ and why
  (e.g. US detonation guidance vs Thai fallout-from-abroad guidance), what Thai viewers should be
  told and which Thai channel/hotline to follow, and popular claims no official page supports.
- **Facts only from the series fact bank** (`series/<series>/SURVIVAL.md`), built from that
  analysis. Never teach something marked "do not teach" or seen only in search snippets.
- **Credit per step, not per card**: each lesson item carries `src` with the sources that say
  exactly that step; the footer states the scope (e.g. "แนวทางของสหรัฐฯ กรณีระเบิดนิวเคลียร์ ·
  ในไทยให้ทำตามประกาศของทางการเสมอ"). Narration follows the sources' wording — no extra slogans.
- **Pattern**: the characters make a natural mistake or face a choice → after the turning point
  a `lessons` card **"ถ้าเจอจริง"** (2–3 numbered steps, ≤ 2 lines each) with the narrator
  reading it, the steps appearing as they are spoken (time items to the pauses:
  `ffmpeg … silencedetect`) → a small source line "ที่มา: … — แนวทางทั่วไป ทำตามประกาศของทางการเสมอ".
- Tie each lesson to everyday life ("ใช้ในชีวิตจริง": floods, fire, smoke, unrest) in the
  caption or the next episode's recap, as mapped in SURVIVAL.md.
- Let a mentor character teach in-story when possible (วันที่ 0: ครูเอก). Keep the tone calm
  and practical — no fear-mongering, no real-world blame, fiction stays labelled.
- Order at the end: event → lesson (one **new picture per step**, e.g. the shelter, the
  lie-down pose, the basement radio; ~12–15 s narration) → viewer choice over the picture of the
  choice → title card → **summary card** ("สรุปบทเรียน · ตอนที่ N": a second `lessons` entry with all
  items at 0, scope line with Thai hotlines, on a calm picture) with the animated follow button
  (no channel name) and the end sting on that last shot. Export the summary frame as
  `render/<id>-summary.png` for a separate post.
  Never hold one picture for more than ~8 s; earshot counts long static stretches against you.

## 2. Make the images (ChatGPT web)

Follow `.agents/skills/chatgpt-images/SKILL.md` (browser, download, filing); hand the browser
work to a Sonnet subagent when running as Opus. Use the style line and templates in
[references/prompts.md](references/prompts.md). Per episode you usually need:

| Need | Where |
| --- | --- |
| Full-frame images for `push` shots (close-ups, inserts, wides) | `epNN/images/` |
| Plates (place without characters) for `run`/`reveal` | `epNN/images/` or reuse an earlier episode's |
| Acting layers, transparent, same framing as the base layer: blink (eyes closed), look/turn, react, run A/B | `characters/` |
| Foreground depth layer (debris, bars, leaves at the bottom corners) | `characters/` |
| New character: full-body transparent layer + a full-frame introduction shot | `characters/` + `images/` |

Check every image: identity matches the character notes, no text/letters, faces outside the
platform zones (§6), transparency real (Pillow alpha), acting layers within ~25 px of the base
layer's alpha box. Record each in `series/<series>/assets/ASSETS.md`.

## 3. Shot types (scripts/shots.py)

| Type | Use for | Key options |
| --- | --- | --- |
| `push` | close-ups, inserts, wides, montages (same image, different `anchor`) | zoom/pull, pan, rack focus `dof`, `dim`, colour `pulse`, phone `buzz`, `end_shake`, `fg` depth |
| `run` | running/walking toward camera | plate + 2–4 pose layers, bob, speed lines, `fg` |
| `reveal` | characters in a place, the big event | `blink`, `swaps` (turn to look), `tremble`, `flash_at` + rising prop, ash, `fg` |
| `layers` | quiet parallax moments | as reveal without the flash |

Any shot: `transition: "whip"`. Series `look` adds one grade and film grain to every frame so
ChatGPT's varying looks read as one film. All fields: [references/timeline.md](references/timeline.md).

## 4. Voice

1. Content Studio main project for the series (ids in SERIES.md). `create_content` with one
   scene per narration line (`text` = Thai, `bullets[0]` = English). Delivery tags only where
   the mood changes (`[กระซิบ ตึงเครียด]`, `[รีบ หายใจแรง]`, `[อ่อนโยน]`, `[เล่าช้า ๆ]`).
2. `voice_content`, then
   `python .agents/skills/polytale-series/scripts/voice.py <ep> <contentId> <sceneId…>` →
   `audio/vo-01.mp3 …` with durations and the Thonburian ASR transcript.
3. Compare every transcript with the script. Re-voice (`update_content` text, then
   `voice_content` with `force` and `sceneIds`) when the model **adds words** (it once added
   "นะครับ?"), leaves a **hum/noise tail**, or a whispered line becomes unclear (use
   `[ตึงเครียด]` instead of `[กระซิบ]` for very short lines). Names the ASR does not know
   (ข้าวตู) are clearer with context ("หมาข้าวตู"). Re-run voice.py after.
4. Character lines (child, old man): `lines` in timeline.json, made by `audio_gen.py`.
Because shots size themselves to their `vo`, re-voicing never breaks sync.

## 5. Sound and score (scripts/audio_gen.py)

- Write each effect as a plain physical description (`sfx[].prompt`), one sound per entry,
  placed relative to its shot. Typical set: room tone/morning, alarms, siren, crowd, Foley
  (packing, door), footsteps, traffic, heartbeat, boom, ringing, wind.
- `music`: a tension score under the whole pre-event part, cut exactly on the event
  (`end_at`); `music_extra` + an `sfx` entry with `file` for the aftermath cue.
- Run `python scripts/audio_gen.py <ep>` (cached; delete a file or `--force` to redo).
- Verify each key sound with earshot (`.agents/skills/earshot/SKILL.md`):
  `earshot.ps1 match audio/sfx/<id>.mp3 "<plain description>"`. Need **strong** (z ≥ 3);
  regenerate with a more literal prompt and `"influence": 0.75` when it says no match/weak
  (the first phone-alert prompt sounded like a car horn; "smartphone emergency alert tone,
  repeating high pitched electronic beeps" matched strongly). Keep rejects in `audio/sfx/rejected/`.
- The mix (final.py) ducks music and effects under the voice automatically and normalises to
  −14 LUFS / −1.5 dBTP.

## 6. Render and QC

```bash
S=B:/ChatGPT/BigO/.agents/skills/polytale-series/scripts
python $S/tl.py .          # resolved shot times
python $S/audio_gen.py .   # sfx, score, character lines (cached)
python $S/subs.py .
python $S/shots.py .       # ~9 s per second of video on CPU (80 s ep = ~12 min; run in background). ONLY=s07a python $S/shots.py . review/s07a.mp4 for one shot
python $S/final.py .
python $S/qc.py .
```

Look at every QC file:
- `review/strip.png` — red = platform UI zones (top 220 px, bottom 380 px, right 140 px from
  y 900–1540). No face, subtitle, card or key action inside red. Characters not cut at edges,
  effects away from faces, no baked text, grade consistent shot to shot.
- `review/subs-sheet.png` — overlay only, one tile per subtitle: Thai never touches the
  English box (subs.py measures every line with the real font, wraps English itself and raises
  the Thai block by the English block's height), no line runs past x 930.
- `review/sub-*.png` — Thai tone marks stacked correctly, subtitles clear of faces.
- Lesson cards: every step has its own `ที่มา:` line and matches the fact bank.
- Countdown, stamp, alert, choice and title readable; title and choice cards dim the frame.
- `final.py` numbers: −14 ±1 LUFS, true peak ≤ −1.5 dBFS; duration = resolved length.
- Run `earshot critique render/<id>.mp4` (full, not `--fast`) and fix every critical/major row:
  dead air at the end (end sting over the end card), cuts with no sound (`cut_sfx`), static
  stretches (more shots), loudness. Also `ffmpeg -vf "fps=1/3,scale=180:-1,tile=9x4"` for a
  frame every 3 s to judge pacing.
State what was not verified (human listening; motion judged from frames).

## 7. Deliver

Send the MP4 with: shot summary, what was checked, known weak spots, ElevenLabs items generated,
and the posting line — caption `<ซีรีส์> ตอนที่ N · <ชื่อตอน>` + 3–5 sentence recap ending on the
cliffhanger/choice + `(เรื่องแต่ง)` + hashtags from CHANNEL.md. Update SERIES.md (status, new
characters and layers, the choice asked and — later — the result).

## Starting a new series

Copy `series/day0/SERIES.md` as the template (logline, devices, 10–12 episode table, characters).
In a **new** ChatGPT conversation make style options, then character sheets and transparent
layers (base, blink, look, run A/B), get the owner's choice, record the URL, create the Content
Studio main project (workspace `workspaces/video/PolyTale`), then follow §1–7.
