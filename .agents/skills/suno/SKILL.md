---
name: suno
description: "Make songs on Suno (suno.com, v6 family since Sep 2026) — Custom create with Style, Lyrics and Exclude styles, Variety off, Max Mode, Extend, Replace Section, Voices, stems, downloads, and the plan, download-cap and commercial-rights limits. Primary song generator for Elyndraze since 3 Nov 2026; use for any Suno song, extension, fix or download (ทำเพลง, เจนเพลง, ต่อเพลง, แก้ท่อน, โหลดเพลง) and for driving suno.com in a browser. Lyrics come from thai-hit-songwriter."
---

# Suno — song production (v6, November 2026)

Platform facts were checked on 3 Nov 2026 with sources and confidence tags in
[references/platform-facts-2026-11.md](references/platform-facts-2026-11.md). Suno changes its UI
often: read the live page before a session; when it disagrees with this file, trust the page,
record what you saw, and update the facts file. Suno publishes no tag or prompt-limit specification;
anything marked "reported" comes from third parties.

For Elyndraze, the lyric comes from `workspaces/music/Elyndraze/skills/thai-hit-songwriter/` and the
generation is run by its [producer role](../../../workspaces/music/Elyndraze/skills/thai-hit-songwriter/roles/producer.md).

## 1. Before spending credits or downloads
- **The owner signs in.** Agents never sign in, buy credits or a plan, accept new terms, or publish or
  share on Suno unless the owner asks for that step.
- **Read the plan in the UI** and say which one is active:

  | Plan | Models | Credits | Downloads | Rights |
  |---|---|---|---|---|
  | Free | v6-mini only | 50 / day | 7 for the account's lifetime, MP3 | **personal use only** |
  | Pro | v6, v6-wild, v6-mini | 2,500 / month | 20 / month, MP3 + WAV (web) | commercial, for songs downloaded through Suno |
  | Premier | as Pro + Suno Studio | 10,000 / month | 60 / month | as Pro |

  A monetised or growing YouTube channel needs Pro or Premier: Free output is personal use only. Tell the
  owner when the account is on Free before producing a release.
- **Downloads are the real quota** (since 3 Sep 2026; they also apply to older songs). A song counts once
  whatever the format, stems included; re-downloading it is free. Download only the chosen master.
- **On Free** (Elyndraze's plan as of 3 Nov 2026): only v6-mini; no Replace Section, Crop, WAV or stems;
  Extend and Max Mode on v6-mini are unconfirmed, so check the UI. The 7 trial downloads are for the
  account's lifetime (accounts that joined before 3 Sep 2026), and trial downloads are not eligible for
  commercial use. Before each download, tell the owner how many trial downloads remain and that the song
  will be non-commercial. Upgrading later is reported not to license songs made on Free (unconfirmed).
  Record `"plan": "Free", "commercial_use": false` in `suno_take`.
- Each generation makes 2 songs for 10 credits; Max Mode costs more (about 20, reported).
- Never name artists or songs in Style or Lyrics (Suno redirects them and its guidelines ban recreating
  existing songs), never upload someone else's recording for Cover, never clone a voice without permission.

## 2. Models
| Model | Use |
|---|---|
| **v6** | Releases. Balanced and expressive; paid plans. |
| v6-wild | Experiments only; less predictable genre blends. Variety defaults to Off. |
| v6-mini | Free plan, drafts, and cheap A/B tests (Thai phrasing, style wording). Songs 040–042 were made on it. |

All earlier models were retired on 9 Sep 2026. Extending, remixing or covering an older song now runs on
v6 and can change its sound. **Max Mode** puts more effort into a generation; Suno recommends it for songs
longer than two minutes and for consistent vocals across a track, so use it for full releases on v6 (users
report Standard mode degrading after about 2:30).

## 3. The create form (Custom)
- **Lyrics** (5,000 characters, reported): paste `lyrics_for_generator.txt` from `build_release.py`.
- **Style of Music** (1,000 characters, reported): plain descriptors — genre, mood, exactly one lead vocal,
  instruments, groove and BPM, dynamics by section, room/tape character, a definite ending. No brackets, no
  negatives, no artist names. Elyndraze style prompts of 450–900 characters fit.
- **Exclude styles** (1,000 characters, reported): `negative_prompt`, a short comma list. It is the only
  reliable place for negatives; "no X" inside Style is reported to fail.
- **Seen in the live UI (3 Nov 2026, Pro):** Advanced mode; model picker v6 / v6-wild / v6-mini; Max Mode is an
  Off/On toggle; Variety is a 0–4 slider where 0 reads "Off"; Duration is Auto/Custom with a 10–360 s slider in
  5 s steps (210 s = 3:30); there is no Instrumental toggle when Lyrics has text. A Cloudflare "Verify you are
  human" box can appear on Create: agents never tick it — stop, ask the owner to tick it in that browser window,
  then read the new takes from the workspace list instead of pressing Create again (it would charge twice).
- **More Options**: set **Variety to Off** first (otherwise Suno rewrites the style prompt; default Normal on
  v6 and v6-mini). Leave Weirdness / Style Influence / Audio Influence at defaults (reported 50 / 50 / 25)
  unless a test shows drift; raise Style Influence if the genre wanders. Set Vocal Gender to the one lead.
  If a Duration control is shown (reported Auto or Custom 10 s–6 min), ask for about 3:30; otherwise Auto
  and fix length in §5.
- **Title**: the Thai or English song title from `song.json`.

## 4. Lyrics box conventions (community practice, verify by ear)
- One English section tag per line in square brackets: `[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`,
  `[Verse 2]`, `[Bridge]`, `[Guitar Solo]` or `[Instrumental]`, `[Final Chorus]`, `[Outro]`, `[End]` (hard stop).
- A short delivery cue may follow inside the tag, e.g. `[Bridge: stripped back, floor toms, soft vocal]`.
  Keep cues short and musical; a long sentence can be sung. Songs 040–042 worked with plain tags.
- Backing echoes in parentheses inside a line are sung; Elyndraze avoids backing vocals, so use them rarely.
- Line break = a breath and a phrase; keep วรรค short (Elyndraze: 3–6 syllables) and one language per line.

## 5. Thai on Suno
Suno makes no official statement about Thai. Tested evidence is the channel's own takes.
- Keep `song.json` in correct Thai spelling; subtitles come from it. If a word is misread, respell it only in
  the pasted lyrics (e.g. `สวรรค์` → `สะ-หวัน`) and note the respelling in `song.json` `notes`.
- Prefer live syllables (คำเป็น) on held and landing notes; dead syllables are fine on short notes and are
  never banned (see the rhyme lab in thai-hit-songwriter).
- Before a new trick (respelling, hyphenation, romanisation), A/B four lines on v6-mini with Variety Off.
- See [references/thai-phonetic-tuning.md](references/thai-phonetic-tuning.md) for respelling candidates.

## 6. Choose and fix the take
1. Measure each take (`ffprobe` on the download, or the page duration before downloading): Elyndraze needs
   3:20–3:40, voice in by 5–8 s, Chorus 1 before 30–40 s.
2. Check the words: Whisper ASR (`tools/musicvideo/asr_song.py`) shows every line in order, then listen to
   each lyriccheck LISTEN line. ASR cannot judge pronunciation or melody.
3. Fix rather than reroll when the song is mostly right:
   - **Too short — Extend**: track `...` → Remix/Edit → Extend, start after the last complete chorus with
     a musical continuation (guitar solo → outro, or breakdown → final chorus), then `...` → Create →
     **Get Whole Song** to stitch; the Song Editor's `+` (Quick Extend) also works. Re-measure the whole song.
   - **Too long**: Crop (Pro/Premier) only at a section boundary, or regenerate with Duration. Never cut
     mid-phrase. Lengths outside the range need the owner's decision (`length_waiver`).
   - **One bad word or line — Replace Section** (Pro/Premier): `...` → Edit → Replace Section, select the
     region, edit lyrics, Recreate Section; pick the better of the two versions.
   - **Dull mix**: Remaster (Subtle / Normal / High), then compare loudness and ASR again.
4. Stems only when a mix fix needs them: Auto Split up to 12 stems, Split from Mix 2 stems (Pro/Premier).

## 7. Voice continuity
Voices replaced Personas in the Create menu; Style Personas live inside Voices (make one from a song:
`...` → Create → Make Persona; it can be private). The Voices FAQ still says it requires v5.5 and v6 support
is unstated — check the UI before relying on it. Elyndraze uses one lead per song and may switch singers
between songs; create or reuse a channel voice only when the owner asks.

## 8. Download, master, record
1. Download the chosen take once — WAV when the plan allows, otherwise MP3 — into
   `songs/<id>/audio/raw.wav` or `raw.mp3` (inside the BigO project, never left in Downloads).
2. Master with `python tools/musicvideo/master_audio.py songs/<id> songs/<id>/audio/<take>` (Elyndraze):
   two-pass loudnorm to −14 LUFS / −1.5 dBTP, 48 kHz 24-bit `audio/master.wav` plus `team/master-receipt.json`.
3. Record in `song.json`:
   `"suno_take": {"id": "...", "duration_sec": 215.96, "model": "v6", "max_mode": true, "plan": "Pro", "commercial_use": true, "master_lufs": -14.0, "true_peak_dbfs": -1.5}`
   (`commercial_use` is true only for a Pro/Premier song downloaded through Suno's own download button.)
4. Record every attempt in `team/suno-session.json`:
   ```json
   {
     "song_id": "043-example",
     "plan": "Pro",
     "model": "v6", "max_mode": true, "variety": "off",
     "style_prompt": "...", "exclude_styles": "...",
     "attempts": [
       {"take_id": "…", "duration_sec": 212.4, "action": "create", "verdict": "kept: all lines, chorus at 0:27"},
       {"take_id": "…", "duration_sec": 168.0, "action": "create", "verdict": "rejected: skipped Verse 2"}
     ],
     "downloads_used": 1
   }
   ```
   Never record a take as heard or approved when nobody listened to it.

## 9. Driving suno.com
Use the agent's browser with the owner's signed-in session; when it cannot do a step (file chooser,
lock-ups), use [playwright-mcp](../playwright-mcp/SKILL.md). Upload files only from a staging copy under
`B:\ChatGPT\BigO\.playwright-mcp\<job>\`. Sequence: open `https://suno.com/create` → read the page
(snapshot) → Custom → model picker → Lyrics, Style, Exclude, More Options, Title → Create → wait for both
takes → read each take's `/song/<id>` link and duration → choose → download once.

## 10. Rights and distribution
- Pro/Premier output is commercial only for songs obtained through a permitted Suno download; Suno gives
  no copyright warranty. Removing watermarks or stream-ripping is banned: never save audio from the
  player stream or a CDN link instead of the Download button.
- Free output is personal and non-commercial only (Suno's help says Suno owns it). Do not enable
  monetisation on videos that use Free songs.
- Keep YouTube's altered/synthetic content disclosure set to Yes for every Suno release.
- Label partnerships (Warner, BMG) and distributor deals (Believe/TuneCore, new partner model only) exist,
  while Universal and Sony litigation continues; do not build releases on covers of existing songs.

## Style starting points (no artist names)
- Warm bedroom pop: `Thai indie bedroom pop, warm emotional female lead vocal, fingerpicked acoustic guitar, warm Rhodes, rounded bass, brushed live drums, intimate room, 84 bpm, dynamic build into chorus, definite drum stop ending`
- Soft pop-rock: `Thai indie pop-rock, heartfelt single male vocal, clean electric guitar arpeggios, live drums with rim clicks, driven chorus guitars, melodic guitar solo after chorus 2, 88 bpm, clean ending`
- Night city pop: `Thai city pop, nostalgic night drive, chorus electric guitar, slap bass, vintage drum machine and live hi-hats, warm analog tape, single female vocal, 94 bpm, clean ending`
- Acoustic R&B: `Thai acoustic R&B ballad, nylon guitar, soft Rhodes, gentle rimshot groove, close-mic male vocal, 78 bpm, warm and intimate, definite ending`

Reference: [metatag cheatsheet](references/metatags-cheatsheet.md) (community conventions).
