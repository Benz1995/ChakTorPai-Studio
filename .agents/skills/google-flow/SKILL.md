---
name: google-flow
description: Generate and import Google Flow (flow.google.com — Veo 3.1, Omni Flash, Nano Banana) video shots for BigO — saved Characters such as อิงเอย, Ingredients vs Frames-to-video, credit costs, uploading reference files through Playwright, trimming the fake phone bezel, stripping the English speech Veo adds, and bringing clips into Content Studio. Use for any Flow/Veo clip, UGC presenter shot or B-roll (ทำคลิป Flow, วิดีโอ AI, Veo); MovieSkit films keep their own native-audio rules.
---

# Google Flow shots

Flow lives at `flow.google.com` on the owner's PRO account. The Playwright MCP browser is
already signed in to Flow. Spending credits needs the owner's instruction for the batch
(number of shots and budget); a skill does not grant purchasing or account switching.

**MovieSkit is different.** For BEFORE FILED, PHITHONG, READ01 and other films in
`B:/ChatGPT/MovieSkit`, read that workspace's `AGENTS.md`, its current handoff and the
MovieSkit skill file `C:/Users/usEr/.codex/skills/movieskit-short-drama/SKILL.md`. Those
films **keep Flow's native dialogue and sound**; never strip or redub them. The audio steps
below are only for BigO clips narrated by Content Studio.

## Costs (PRO, Oct 2026 — re-read the page before spending)

| Model | Credits per 8 s clip |
| --- | --- |
| Veo 3.1 Quality | 100 |
| Veo 3.1 Fast | 20 |
| Omni 1.1 Flash (720p) | 12 |
| Veo 3.1 Lite | 10 |
| Nano Banana image | 0 shown |

Failed generations are refunded. Character voice previews show no price but credits dropped
~6 during tests; treat a preview as ~1 credit. Log model, credits and result for every attempt.

> **Owner Ironclad Rule (8 Nov 2026):** Local image generation is strictly forbidden across BigO. **Nano Banana image** (0 credits on Flow) is one of the two authorized routes for all keyframes, start frames, and character assets (alongside ChatGPT).

## Characters (identity)

- Build a Character by **uploading a face reference**, never from a text description — the
  owner rejected text-made and low-resolution-crop versions ("ยังไม่เหมือนอิงเอยเลย").
- อิงเอย: Character "อิงเอย" in project
  https://flow.google.com/project/be9eb03e-9a81-409a-9fd3-f63d0ef2f87f, built from
  `images/ingoei/ingoei-face-official.png`. "อิงเอย v1" is rejected — do not use it.
  Canonical look and outfit rules: `B:\ChatGPT\PagePilotStarterKit\assets\selected\ingoei_v2\REFERENCE_RULES.md`
  (adult, covered outfits, petite 163 cm with a soft curvy figure in every prompt).
- **Best identity hold:** a Nano Banana 9:16 start frame with the Character, then
  **Frames-to-video** (Omni 1.1 Flash 720p 8 s = 12 credits). Ingredients mode
  (องค์ประกอบ → "+" → the Character) works but drifts more.
- Voices: binding a base voice (e.g. Sulafat, Despina) costs 0 credits. A custom voice with
  any text in the direction field plus a Thai sample fails with INVALID_ARGUMENT
  ("สร้างตัวอย่างไม่สำเร็จ") — leave direction empty and put the tone in the shot prompt.

## Uploading files to Flow

- The built-in browser pane shows no file chooser, and Claude in Chrome is often not
  connected. Use the Playwright MCP browser ([playwright-mcp](../playwright-mcp/SKILL.md)):
  `browser_file_upload` accepts only files under `B:\ChatGPT\BigO`, so copy the files to
  `B:\ChatGPT\BigO\.playwright-mcp\<job>\` (git-ignored) and delete the copies afterwards.
- "Browser is already in use": another session holds Playwright's shared profile. Ask the
  owner to close that window, or close it only when they ask. The built-in pane can still
  generate and download once the owner signs in there.
- Last resort in the built-in pane: hook `HTMLInputElement.prototype.click`, click
  "อัปโหลด", then set the captured input's `files` from a File built from base64 in chunks
  and dispatch `change` (fetching localhost from the page is blocked).

## Prompting and known defects

- One legible action per shot; state start and end positions, camera move and what must
  not happen. "Nobody speaks" is not obeyed — plan to strip speech.
- Selfie/UGC prompts often show a fake phone bezel or notch for the first ~2 s: trim it.
- Faces drift slightly in video (smaller eyes, lighter hair); jewellery changes (the clover
  necklace becomes a heart). Products change shape — compare against the real product and
  flag mismatches to the owner before use.

## Into Content Studio

1. Download each clip and move it into the project folder
   (`images/<project>/clips/<shot>/`), never leaving it in Downloads.
2. For clips that Content Studio will narrate, remove Veo's speech and keep the bed:

   ```bash
   python -X utf8 .agents/skills/google-flow/scripts/strip_speech.py <clip.mp4> <bed.wav> --video <clip-nospeech.mp4>
   ```

   It runs htdemucs through the Python API (the demucs CLI save path fails here) on the GPU
   when available; an 8 s clip takes ~11 s. Listen or ASR-check that no words remain.
3. Trim the bezel frames with FFmpeg ([ffmpeg-skill](../ffmpeg-skill/SKILL.md)).
4. `upload_file`, then use `clip-highlights` (9:16, `transitionId: "none"`) or set the clip as
   a scene's media; `preview_frames`, voice, render and verify as usual.
5. Keep a `create.json` / notes per clip: prompt, mode (Frames / Ingredients), model,
   credits, Flow clip URL, local file, trim and audio treatment.

For affiliate presenter clips, apply [shopee-affiliate](../shopee-affiliate/SKILL.md) rules
(no prices, no fake testimonial, real product shape).
