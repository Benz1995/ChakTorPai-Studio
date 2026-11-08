---
name: thai-voiceover
description: Write, voice and check Thai narration for Content Studio clips (เสียงพากย์, บทพูด, เสียงบรรยาย, อ่านผิด, คำอ่าน, ซับไทย) — speech-paced scripts, delivery tags, ElevenLabs v3 / F5-TTS voice choice, the pronunciation dictionary, number readings, Thonburian ASR checks, child voices and burned-in Thai subtitles. Use before voice_content and whenever a Thai voice sounds read-aloud, rushed or mispronounced; Chatterbox is not a Thai route.
---

# Thai voiceover

Narration is produced per scene by Content Studio (`voice_content`). This skill covers the
script, the voice, pronunciation and the checks around it. Text review, ASR and human
listening are separate states; report each one for what it is.

## 1. Write for speech

- **Master Thai Craft (กฎเหล็กกลาง):** Scripts and narrations must strictly follow
  `.agents/skills/thai-craft/SKILL.md` (dynamic flow, zero English calques, proper Thai
  dialogue registers with ครับ/ค่ะ/ลูก, verb-serial storytelling, 3-second spoken test).
  Mandatory Human Gate: present the Thai draft to the owner for review before generating voice.
- One idea per scene. Pace is measured in spoken letters per second (spaces, punctuation
  and `[tags]` not counted): aim for 10–12; the editor flags above **12.5** (⚠ พูดเร็ว) and
  treats **14** as rushed (`src/shared/timing.ts`). Split or shorten rather than squeeze.
- Write how a person says it: short clauses, commas where the breath goes, natural particles
  (นะ, เลย, อ่ะ) where they fit the character.
- Delivery tags at the start of a line (`[สดใส]`, `[ขำ ๆ]`, `[ตื่นเต้น แบบผู้ประกาศข่าว]`) are
  performed by ElevenLabs v3 and hidden from captions. Tag only where the mood changes —
  tagging every scene makes v3 over-act.
- Before voicing, run the local Thai second reader (per `AGENTS.md`):
  `python scripts/thai-language-review.py draft.txt --kind narration --context "<channel, audience, tone>" --out out/thai-review/<attempt>`
  from `content-studio` (kinds: narration, dialogue, lyrics, captions; setup in
  `docs/thai-language-review.md`). Review each suggestion; never apply them blindly.

## 2. Choose the voice explicitly

Check `list_voices` and `GET /api/providers`; never let a default call a paid service the
owner did not choose, and respect the character budget for the round.

| Voice | Provider | Use |
| --- | --- | --- |
| `FfrJDiyJZK` เสียงของฉัน | ElevenLabs `eleven_v3` | the owner's own voice; KinJi affiliate default |
| `82YT7fke7C` เสียงของฉัน | ElevenLabs | second owner-voice binding (check which the project uses) |
| `Kao-pfFHCf` เสียงของฉัน | F5-TTS local (`local-tts`) | free local route; check the provider is healthy first |

- Keep ElevenLabs stability at **0.5** (Natural); 0 (Creative) drifts in tone between scenes.
- ElevenLabs library voices: "Mali" cannot be used through the API (not fine-tuned);
  "Hammy" (middle-aged woman) works. Designed voice "HW26 Mint (designed)"
  (`w3e1Jn4F37O7wDwETrJ9`, young Bangkok woman) is in the account.
- Child voice: generate an adult female line, then raise pitch and keep duration, e.g.
  `ffmpeg -i in.mp3 -af "asetrate=44100*1.18,aresample=44100,atempo=0.847" out.wav`
  (match the source sample rate; listen for chipmunk artefacts).
- Edge-TTS is the Opuscar runtime's voice, not the app's; Chatterbox has no verified Thai
  checkpoint ([motion-chatterbox](../motion-chatterbox/SKILL.md)).

## 3. Pronunciation

- Numbers, ranges and common brand terms are converted to Thai readings automatically
  (`5,979`, `2-12`, `Type-C`). Check the 🔊 spoken preview in the editor for every scene.
- Add unusual names (games, product models, places) with `set_pronunciations`; the user
  lexicon (`GET /api/lexicon`) is read live. "11.11" / "12.12" were read as decimals
  ("สิบเอ็ดจุดหนึ่งหนึ่ง") until added — check campaign dates every time.
- Built-in readings live in `src/shared/pronounce.ts`. The API runs as plain
  `tsx server/index.ts` without watch, so a change there needs a server restart; use
  `set_pronunciations` for an immediate fix.

## 4. Check the audio

- Run the app's alignment/QC (`align_scene_captions`) and read each scene's similarity.
- To verify **how numbers and names were read**, transcribe with the Thai fine-tuned model —
  `large-v3-turbo` prints digits, so it cannot tell "สิบเอ็ดสิบเอ็ด" from "สิบเอ็ดจุดหนึ่งหนึ่ง":

  ```bash
  cd content-studio && RECAP_ASR_MODEL=thonburian-whisper-th-large-v3 python scripts/recap-transcribe.py --input <scene.mp3> --output <out.json>
  ```

  Run `python scripts/recap-transcribe.py --probe` first. If CUDA fails (missing
  `cublas64_12`), add `RECAP_ASR_DEVICE=cpu`; it is slow but fine for short scenes.
- ASR shows what a model heard, not that the line sounds natural. Ask the owner to listen
  to at least the lowest-scoring scene before calling a batch approved.
- For feed clips run `npx tsx scripts/retention-check.ts <contentId>` (pace, opening,
  loudness, true peak) and fix the warnings that apply.

## 5. Burned-in Thai subtitles (outside the Remotion captions)

Use Tahoma with complex shaping: `ffmpeg -i in.mp4 -vf "ass=subs.ass:shaping=complex" out.mp4`
and `Fontname: Tahoma` in the ASS style. Leelawadee UI drops stacked tone marks
(เผื่อ → เผือ). Inspect a frame with stacked marks before delivering.
