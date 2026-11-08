# Suno AI fact sheet - as of 3 Nov 2026

Method: WebSearch + WebFetch only. No sign-in, no downloads, no forms. Nothing here was tested inside the live app.

Confidence tags used on every fact:
- [OFFICIAL] = fetched directly from suno.com / help.suno.com / blog.suno.com in this session (page date given if the page showed one, otherwise "undated").
- [OFFICIAL-UNDATED] = official help article that shows no date and may pre-date v6 (UI wording can be stale).
- [3RD-PARTY-MEASURED] = a third party that says it read the live UI / counters / ToS (GitHub issue #562, HookGenius, etc.).
- [3RD-PARTY] = blog / news / aggregator claim only.
- [UNCONFIRMED] = could not confirm for 2026; do not rely on it.

Caveat on fetching: WebFetch returns a model-written summary of each page, not raw HTML. Quotes below are the summary's wording of what the page said. jackrighteous.com and musicbusinessworldwide.com returned 429/403 on some fetches, so those claims come from search-result excerpts only.

---------------------------------------------------------------------------------

## 0. Headline changes since mid-2026 (read this first)

1. Suno shipped the v6 family on 9 Sep 2026 and retired every earlier model for new generations the same day. v5.5 / v5 / v4.5 no longer exist in the model picker.
   - https://suno.com/blog/introducing-v6 (9 Sep 2026) [OFFICIAL: "Suno plans to retire its previous models as v6 rolls out"]
   - https://suno.com/release-notes (entry "Sep 9") [OFFICIAL]
   - https://help.suno.com/en/articles/13924481 (v6 FAQ, undated) [OFFICIAL-UNDATED; the retirement sentence "All models prior to v6 have been retired" is quoted from this FAQ by the search result and by https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 (issue opened 10 Sep 2026)]
2. Download caps started 3 Sep 2026: Free 7 lifetime trial downloads, Pro 20/month, Premier 60/month. This changes the economics of a "main song generator".
   - https://suno.com/blog/suno-updates-tos (10 Aug 2026) [OFFICIAL]
   - https://help.suno.com/en/articles/13614785 (Upcoming Changes FAQ, undated) [OFFICIAL-UNDATED]
   - https://suno.com/pricing (fetched 3 Nov 2026) [OFFICIAL]
3. New Terms of Service effective 3 Sep 2026 (last revised 10 Aug 2026). https://suno.com/terms (fetched 3 Nov 2026) [OFFICIAL]
4. Label litigation is NOT over: Warner and BMG are licensed partners; Universal and Sony are still suing (second suit filed 18 Sep 2026 aimed at v6). See section 8.

---------------------------------------------------------------------------------

## 1. Model versions in the web app

### 1.1 What exists now
- v6 (flagship), v6-wild (experimental, less predictable), v6-mini (faster, more efficient, free for everyone). Launched 9 Sep 2026.
  - https://suno.com/blog/introducing-v6 (9 Sep 2026) [OFFICIAL]
  - https://suno.com/release-notes "Sep 9 v6 family" [OFFICIAL]
- Official descriptions: v6 = "Balanced, expressive, and built for a wide range of styles and prompts"; v6-wild = experimental, leans into genre-blending and unexpected results; v6-mini = lighter, faster, for quick ideas and high-volume generation.
  - https://help.suno.com/en/articles/13924801 ("What's new in v6?", undated) [OFFICIAL-UNDATED]
- Model picker: dropdown at the top right of the Create form. Picker captions reported as: v6 "Our best model yet", v6-wild "Best for experimental ideas", v6-mini "A free, more efficient version of premium v6 models".
  - https://help.suno.com/en/articles/13924801 [OFFICIAL-UNDATED] (dropdown location)
  - https://hookgenius.app/learn/what-happened-to-suno-v5/ (9 Sep 2026) [3RD-PARTY-MEASURED] (captions)
- No model newer than v6 found as of 3 Nov 2026. Release notes list nothing newer through 29 Oct 2026. https://suno.com/release-notes [OFFICIAL]
- Which is the "default"? Suno does not document a default model. Not confirmed. [UNCONFIRMED]. Variety default differs by model (see 4.2).

### 1.2 Plan access (live pricing page, 3 Nov 2026)
| Plan | Models |
|---|---|
| Free | v6-mini only ("Best free model (v6-mini)") |
| Pro | v6 + v6-wild (and v6-mini) |
| Premier | v6 + v6-wild (and v6-mini) |
- https://suno.com/pricing (fetched 3 Nov 2026) [OFFICIAL]
- https://suno.com/release-notes: "v6 and v6-wild are available only to paid users." [OFFICIAL]

### 1.3 What v6 adds (Suno's own words, short)
- Edit one section of an existing song with natural-language instructions; change a single lyric without regenerating the whole song; mashups of several songs in one request; sample a riff / isolate an instrument; generate from text, audio, images and video inputs; generate from mood / genre / references.
  - https://suno.com/blog/introducing-v6 (9 Sep 2026) [OFFICIAL]
- "Developed with industry partners, including Warner Music Group, BMG, and Believe." The blog does NOT say it was trained only on licensed music; treat "100% licensed" claims as unverified. [OFFICIAL for the partner list; the exclusivity claim is UNCONFIRMED]
  - https://suno.com/blog/introducing-v6 (9 Sep 2026)
  - https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 (10-12 Sep 2026) [3RD-PARTY-MEASURED: says Suno's text only mentions "industry partners"]
- Existing Custom Models auto-upgrade to v6; old songs stay in the library unchanged but extensions / remixes / covers of them now run on v6 so they may sound different.
  - https://help.suno.com/en/articles/13614785 (undated) [OFFICIAL-UNDATED]
  - https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED]
- Cover, Extend, Replace Section, Song Editor, Remaster, Inspire, Sounds, Custom Models all run on v6.
  - https://help.suno.com/en/articles/13924801 [OFFICIAL-UNDATED] (lists Custom Models, Sounds, Remix & Edit as built on v6)
- Hidden internal model IDs reported as chirp-hawk / chirp-hawk-wild / chirp-goose; there is no official public API. [3RD-PARTY-MEASURED] https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562

### 1.4 Version history (for context)
| Date | Model | Source |
|---|---|---|
| 1 May 2025 | v4.5 (richer vocals, better genre handling), Pro/Premier | https://suno.com/release-notes [OFFICIAL] |
| 23 Sep 2025 | v5 (clearer audio, more natural vocals, Remaster variation strength) | https://suno.com/release-notes [OFFICIAL] |
| 21 Oct 2025 | v4.5-all (free model for everyone) | https://suno.com/release-notes [OFFICIAL] |
| 26 Mar 2026 | v5.5 + Voices + Custom Models (min 6 tracks) + My Taste | https://suno.com/release-notes ; https://suno.com/blog "Suno v5.5: More Expressive. More You." [OFFICIAL] |
| 20 Jul 2026 | Duration slider (web, v5.5) | https://suno.com/release-notes [OFFICIAL] |
| 9 Sep 2026 | v6 / v6-wild / v6-mini; older models retired | see above |

---------------------------------------------------------------------------------

## 2. Song length and Extend

- Max length per single generation: up to 8 minutes for all three v6 models.
  - https://help.suno.com/en/articles/13924801 ("Length: All three support up to 8 minutes per generation", undated) [OFFICIAL-UNDATED]
  - https://help.suno.com/en/articles/13924929 ("How long will my song be?", states up to 8 minutes with v6 / v6-wild / v6-mini, undated) [OFFICIAL-UNDATED]
  - The help category lists the article as "Maximum song length, which is now up to 8 minutes". https://help.suno.com/en/categories/550017 [OFFICIAL]
- Typical Auto length is much shorter than the 8-minute ceiling: one author reports about 2:42-2:47 on v5.5 and 3:08-3:16 on v6 for one prompt. https://hookgenius.app/learn/suno-v6-guide/ (published 9 Sep 2026, updated 22 Oct 2026) [3RD-PARTY-MEASURED, single prompt]
- Duration control: official release note (20 Jul 2026) says "Available on Web using V5.5 model" - i.e. it was announced for v5.5. https://suno.com/release-notes [OFFICIAL]
  - On v6, the Advanced mode "More Options" reportedly still has Duration: Auto, or Custom 10 s to 6 min (default 3:00). https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 (10-12 Sep 2026) [3RD-PARTY-MEASURED]; also HookGenius (above) says "More Options offers Custom or Auto". That issue explicitly rejects the claim that the slider is v5.5-only. Official v6 confirmation of Duration: [UNCONFIRMED].
  - Mobile app has no Duration slider (web only). https://suno.com/release-notes [OFFICIAL]
- Max Mode (new v6 toggle): "put in more effort for a better result"; costs more credits; Suno recommends it for songs longer than two minutes, covers that should stay close to the original, style transfer, and keeping vocals/style consistent across a full track.
  - https://help.suno.com/en/articles/13924481 (v6 FAQ, undated) [OFFICIAL-UNDATED]
  - Reported cost 2x = 20 credits per generation: https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED]. Three users there report audio degrading after about 2:30 in Standard mode; whether Max Mode fixes it is not confirmed.
- How Extend works (two official descriptions, both undated - UI names may have moved):
  1. Classic path: song "..." > Remix/Edit > Extend; drag the white arrow to choose how much of the original to keep and where the extension starts (a timestamp); enter new lyrics / style; Create. Pick the extension you like, then "..." > Create > "Get Whole Song" stitches the new ending onto the original. https://help.suno.com/en/articles/2409601 ("How do I make my song longer?", undated) [OFFICIAL-UNDATED]
  2. Song Editor path: click the "+" icon at the far right of the track, enter a prompt to steer it, or use "Quick Extend" for a seamless continuation. https://help.suno.com/en/articles/6141505 ("How to Use: Song Editor", undated) [OFFICIAL-UNDATED]
  3. Another menu path quoted: More Actions > Edit > Extend. https://songsmith.studio/blog/how-to-make-full-length-songs-on-suno (published 15 Apr 2026, updated 23 Oct 2026) [3RD-PARTY]
- Maximum TOTAL length after repeated Extends: no documented cap found. [UNCONFIRMED] One guide says Extend is the only way past 8 minutes, to extend "once or twice" for ~15 min, and to start fresh after ~3 extensions. https://songsmith.studio/blog/how-to-make-full-length-songs-on-suno (23 Oct 2026) [3RD-PARTY]. The help pages checked do not state an Extend credit cost.
- Extending/covering an old (pre-v6) song re-runs it on v6. https://help.suno.com/en/articles/13614785 [OFFICIAL-UNDATED]

---------------------------------------------------------------------------------

## 3. Editing features, names and where they live

(Web UI. "..." = the More Actions / three-dot menu on a song in Library or Workspace.)

| Feature | Current name / location | Plan | Source |
|---|---|---|---|
| Extend | "..." > Remix/Edit (or Edit) > Extend; or "+" at the far right of a track in the Song Editor ("Quick Extend"); then "Get Whole Song" to stitch | Not stated in the help pages; assume paid for v6/v6-wild, v6-mini free | https://help.suno.com/en/articles/2409601 ; https://help.suno.com/en/articles/6141505 [OFFICIAL-UNDATED] |
| Cover | "..." > Create > Cover Song; enter a new Style of Music. Beta. Help text: "You can only use this feature for songs you created." | Pro and Premier (help text) | https://help.suno.com/en/articles/2872257 [OFFICIAL-UNDATED] |
| Persona -> Voices | The Create-menu "Voices" button replaced "Personas"; Style Personas still exist inside the Voices menu. Make a Persona: song "..." > Create > Make Persona (name, avatar, description; public by default, can be made private); list at suno.com/me/personas. Custom-mode Personas picker fills Style of Music automatically. | Pricing page: "Record, upload, and create with your own voice" on Pro and Premier; "personas and advanced editing" listed on Premier | https://help.suno.com/en/articles/11362433 (Voices FAQ) ; https://help.suno.com/en/articles/3484161 (What are Personas?) ; https://suno.com/pricing (3 Nov 2026) [OFFICIAL / OFFICIAL-UNDATED] |
| Voices (your own voice) | Create > Add Voice dialog; from a library song, live recording, or upload; clip 15 s - 4 min, best 2 min; a spoken-phrase check verifies it is you; 18+ only; not available in all countries; Audio Influence slider should stay fairly high | Pro / Premier (pricing page) | https://help.suno.com/en/articles/11362369 ; https://suno.com/pricing [OFFICIAL] |
| Replace Section | "..." > Edit > Replace Section; drag-select the region; edit lyrics; "Recreate Section"; get two versions. In Song Editor: Replace / Quick Replace, Edit Lyrics, Crop / Remove, fades. v6 adds plain-language single-section edits and single-lyric changes. | Pro and Premier | https://help.suno.com/en/articles/3271873 ; https://help.suno.com/en/articles/6141505 ; https://suno.com/blog/introducing-v6 (9 Sep 2026) [OFFICIAL / OFFICIAL-UNDATED] |
| Crop | trims start/end | Pro and Premier | https://help.suno.com/en/categories/550017 [OFFICIAL] |
| Remaster | "..." > Remaster; Variation strength: Subtle / Normal (default) / High (since v5). Subtle = only small acoustic/production changes; High can alter musical elements and vocals. | Not stated | https://help.suno.com/en/articles/8105281 (undated) [OFFICIAL-UNDATED] (read via search excerpt only) |
| Stems | "..." > Get Stems > choose split type > Extract; in Studio right-click a clip > Split Stems. Auto Split = up to 12 stems (original model), 50 credits per extraction. Split from Mix = one chosen instrument/voice + the complement, 10 credits per stem. Advanced Split = pick from nearly 100 instruments, 10 credits per stem, Premier only. | Free: no stems. Pro: Auto + Split from Mix. Premier: all three. | https://help.suno.com/en/articles/13925185 (undated) ; https://suno.com/release-notes "Jun 11 Stem Separation updates" ; https://suno.com/pricing [OFFICIAL / OFFICIAL-UNDATED] |
| Suno Studio (DAW / "Generative Audio Workstation") | Studio icon under Create in the left panel. Multitrack timeline, take lanes, comping, record/upload, drag-to-Create, versions, export (Full Song, Selected Time Range, Multitracks), MIDI export. Studio 1.2 (16 Feb 2026), Studio 2.0 (13 Aug 2026: MIDI, chat bar, effects, wavetable synth, automation), further updates 2 Sep, 17 Sep, 8 Oct, 29 Oct 2026. | Premier only ("Studio is only available with a Premier plan") | https://help.suno.com/en/articles/7940161 ; https://suno.com/release-notes ; https://suno.com/pricing [OFFICIAL] |
| Add Vocals / Add Instrumental | Pricing page lists "Add new vocals or instrumentals to existing songs" under Premier only. The older help article calls Add Vocals a beta for Pro and Premier ("..." > Add Vocals from the remix dropdown, enter lyrics, Create; Audio Strength slider in advanced options). | Conflict: pricing page (3 Nov 2026) = Premier; help article (undated) = Pro and Premier. Prefer the pricing page. | https://suno.com/pricing ; https://help.suno.com/en/articles/6882817 [OFFICIAL vs OFFICIAL-UNDATED] |
| Audio upload | "Audio Upload" button next to Create. Pricing page: Free up to 8 min; Premier up to 30 min; the Pro card does not state a limit (a comparison table in one fetch showed 30 min for Pro - not re-confirmed). The old help article (undated) says Free 60 s, Pro/Premier 8 min - outdated. Release note 3 Jun 2025: uploads up to 8 min. | see left | https://suno.com/pricing ; https://help.suno.com/en/articles/6141569 ; https://suno.com/release-notes [OFFICIAL] ; Pro limit [UNCONFIRMED] |
| Custom Models | Train on at least 6 catalogue tracks (24+ advised); up to three models (help category blurb); reported 100 credits to create; Premier-only sharing with 2x inputs (15 Oct 2026). | Pro and Premier | https://suno.com/release-notes ; https://help.suno.com/en/categories/550017 ; https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [OFFICIAL / 3RD-PARTY-MEASURED for credits] |
| Other | Sounds (one-shot samples / loops, Pro+), Mashup, Sample, Inspire, Hooks (free), Speech beta (1 Oct 2026, web + mobile), Albums, Suno MCP beta (28 Oct 2026; connect Claude / ChatGPT; all plans, songs use credits, early-access sign-up) | various | https://suno.com/release-notes [OFFICIAL] |

Notes
- Voices FAQ (undated) still says "Voices requires model v5.5"; v6 compatibility is not stated there. Third-party reports an "Upgrade Voice to v6" option and a "Style Voice (legacy)" label, and that Voices cannot be used on instrumentals. https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED]. Official v6 Voices compatibility: [UNCONFIRMED].
- Commercial status of tracks that use a Voice: no answer in the Voices FAQ; ToS forbids creating a Voice Model of another person. https://help.suno.com/en/articles/11362433 ; https://suno.com/terms [OFFICIAL]

---------------------------------------------------------------------------------

## 4. Prompt limits and Advanced options (v6)

### 4.1 Character limits
Suno has never published these; the figures below were read from the live composer counters on 7-9 Sep 2026 by third parties. Same as v5.5.
- Style of Music: 1,000 characters
- Lyrics: 5,000 characters
- Exclude Styles: 1,000 characters
- Simple-mode song description: 3,000 characters (measured on v5.5)
- Title: no enforced limit on v6 (the old 100-character figure was retracted)
- v4 for comparison: style 200, lyrics 3,000, title 80 (retired)
  - https://hookgenius.app/learn/suno-character-limits/ (dated 9 Sep 2026, footer "last updated 8 Sep 2026") [3RD-PARTY-MEASURED]
  - https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 (10-12 Sep 2026) [3RD-PARTY-MEASURED]
  - https://hookgenius.app/learn/suno-v6-guide/ (9 Sep 2026, updated 22 Oct 2026) [3RD-PARTY-MEASURED: "lyrics 5,000 characters, styles 1,000 (read from the composer counters)"]
- Simple Mode vs Advanced Mode: Simple mode expands supplied lyrics rather than singing them verbatim, so finished-lyric workflows should stay in Advanced mode. Simple mode also accepts up to 5 images, 1 video (<= 241 s), up to 5 audio references. https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED]

### 4.2 Advanced options / sliders
- Weirdness: "Safe" to "Chaos"; 50% is the "normal expected result". Custom/Advanced mode. https://help.suno.com/en/articles/6141377 ("How to Use: Creative Sliders", undated) [OFFICIAL-UNDATED]
- Style Influence: "Loose" to "Strong" - how closely the result follows your style input. Default 50 reported. https://help.suno.com/en/articles/6141377 [OFFICIAL-UNDATED]; default from https://hookgenius.app/learn/suno-v6-guide/ [3RD-PARTY-MEASURED]
- Audio Influence: appears only when you use an audio upload (or a Voice). Default 25 reported. https://help.suno.com/en/articles/6141377 [OFFICIAL-UNDATED]; default from https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED]
- Variety (NEW in v6, in "More Options"): "designed to introduce variety in your outputs by adjusting and updating your style prompts." To keep full control of your style tags set it to 0 / Off. https://help.suno.com/en/articles/13924481 (v6 FAQ) [OFFICIAL-UNDATED]
  - Five stops reported: Off ("Exact style"), Normal, High, Extra, Max. Default Normal on v6 and v6-mini, Off on v6-wild. https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED]
  - Measured: at Normal the stored style differed from the pasted style on every take in a 30-take batch; at Off it was stored as pasted on 52 of 54 takes. https://hookgenius.app/learn/suno-v6-guide/ (updated 22 Oct 2026) [3RD-PARTY-MEASURED]
  - Practical consequence for an engineered style box: set Variety to Off first.
- Max Mode toggle: see section 2.
- Exclude Styles: the only reliable negative prompt (putting "no drums" inside the style box was reported to fail). https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED]
- Also present: Vocal Gender, Duration, My Taste. https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED]
- Artist names in prompts are rewritten: Suno states "We don't reference artists directly, so we've replaced your prompt with similar styles you might like." https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED, quoting the app]; official policy: prompts naming specific artists or copyrighted songs are not allowed and are redirected to descriptive traits. https://suno.com/blog/building-the-future-of-music-responsibly (6 Aug 2026) [OFFICIAL]

---------------------------------------------------------------------------------

## 5. Meta tags / structure tags

- There is NO official, complete tag specification from Suno. Anything below is community-derived. [UNCONFIRMED as official]
- What Suno itself shipped: a redesigned lyrics editor (9 Jul 2026) with "structure labels", natural-language editing, autosave. https://suno.com/release-notes [OFFICIAL]. Reported behavior: the editor adds one bracketed production note per section, e.g. [half-time drums]. https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED]
- Commonly used section tags (square brackets, in the Lyrics box): [Intro], [Verse] / [Verse 1], [Pre-Chorus], [Chorus], [Bridge], [Instrumental] / [Instrumental Break], [Outro], [End]. [End] is described as a hard stop. Case does not matter. Per-section modifiers follow a colon, e.g. [Verse: whispered vocals, acoustic guitar only]. A mistyped/unbracketed tag can be sung as lyrics. https://www.blakecrosley.com/guides/suno (page "Updated May 13, 2026", changelog to 16 Aug 2026; says vocabulary "unchanged through V5.5"; does not mention v6) [3RD-PARTY]
- v6-specific: one tester found v6 follows per-section delivery notes placed inside lyric brackets (e.g. whispered bridge; a section language switch) - evidence = one track judged by ear, not blind. https://hookgenius.app/learn/suno-v6-guide/ (updated 22 Oct 2026) [3RD-PARTY-MEASURED, weak]
- Reported as surviving into Advanced mode on v6: structure tags, Weirdness, Style Influence, Audio Influence, Vocal Gender, Exclude Styles, Duration, My Taste. Bar-count tags such as [VERSE 1 8] are unverified on v6. https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED]
- Style-box advice: plain descriptors, no brackets, about 4-7 descriptors; put negatives in Exclude Styles, not the style box. https://www.blakecrosley.com/guides/suno [3RD-PARTY]
- Suno's own "Music Glossary for Suno" article exists but its text was not retrieved. https://help.suno.com/en/categories/550017 (title only) [OFFICIAL list entry]

---------------------------------------------------------------------------------

## 6. Language notes (Thai / non-English)

- Official Thai support or a Thai-specific guide: none found. Suno publishes no supported-language list or pronunciation guide that I could locate. [UNCONFIRMED for Thai in 2026]
- Thai pronunciation / tone accuracy: no credible test of Suno on Thai found (searched English and Thai). Treat Thai quality as untested until you A/B it yourself. [UNCONFIRMED]
- General, non-official tips that apply to any non-English lyric (all vendor/community, not tested for Thai):
  - Phonetic respelling ("spell words the way they should sound"), hyphens to split syllables, one language per section, name the language in the style prompt. https://hookgenius.app/learn/fix-suno-pronunciation/ (page dated Feb/May 2026) [3RD-PARTY, asserted without evidence]
  - There are no pronunciation-specific meta tags and no IPA support; Suno predicts pronunciation from spelling patterns. Same source [3RD-PARTY].
  - Fix a bad word after the fact with Replace Section / Edit Lyrics (Pro+), which regenerates only that region and gives two alternates. https://help.suno.com/en/articles/3271873 [OFFICIAL-UNDATED]
- Beware a false lead: the note.com article from a Bangkok creator (3 Mar 2026) is about Japanese lyrics (hiragana particle fix), not Thai. https://note.com/hip_llama3643/n/nb48f138650d7?hl=en [3RD-PARTY]
- Section-level language switching on v6 was observed (Italian verses, whispered French bridge from bracket cues in one track). https://hookgenius.app/learn/suno-v6-guide/ [3RD-PARTY-MEASURED, weak]
- Suggested validation (my suggestion, not a sourced fact): run the same 4-line Thai verse in Thai script vs. phonetic romanization vs. mixed, on v6-mini and v6, Variety Off; check tones and final consonants by ear before committing credits.

---------------------------------------------------------------------------------

## 7. Downloads, rights, credits

### 7.1 Download formats
- MP3: all plans, web and mobile. WAV: Pro and Premier, on suno.com only (mobile defaults to MP3). Video file: available. Stems: individual stem files when the song has stems (do not count as extra downloads). MIDI: only for songs created in Suno Studio, Premier only. Note the article says options "may vary depending on the song, feature, plan, or device".
  - https://help.suno.com/en/articles/13926081 ("What types of files can I download?", undated) [OFFICIAL-UNDATED]
  - https://help.suno.com/en/categories/550209-troubleshooting ("Why can't I download wav files?" - WAV is Pro/Premier, suno.com) [OFFICIAL]
- Studio exports reported as 32-bit / 48 kHz and unlimited for Premier. https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562 [3RD-PARTY-MEASURED]; WAV sample rate / bit depth of normal Create-page downloads: [UNCONFIRMED].

### 7.2 Download caps (from 3 Sep 2026)
| Plan | Cap |
|---|---|
| Free | 7 lifetime trial downloads (joined before 3 Sep 2026); later signups "may occasionally receive trial downloads"; trial downloads are personal use only |
| Pro | 20 song downloads per month |
| Premier | 60 song downloads per month; Suno Studio downloads are NOT limited |
- Counting rules: one song = one download regardless of format; a song plus its stems = one; re-downloads and failed downloads do not count; monthly count resets on the billing date; unused downloads do not roll over; limits apply to ALL songs including ones made before 3 Sep; extra downloads can be bought (price not shown in the FAQ); streaming / sharing / linking stays unlimited; after cancelling, downloads fall under free-tier limits.
  - https://suno.com/blog/suno-updates-tos (10 Aug 2026) [OFFICIAL]
  - https://help.suno.com/en/articles/13614785 (undated) [OFFICIAL-UNDATED]
  - https://help.suno.com/en/categories/550017 (articles "What counts as one download?", "How many downloads come with my subscription?", "Do download limits apply to songs I already made?") [OFFICIAL]
  - https://suno.com/pricing (3 Nov 2026): "No monthly song downloads" (Free), "20 song downloads per month" (Pro), "60 song downloads per month" (Premier) [OFFICIAL]
- Price of extra downloads: officially unpublished; one site claims about $2.99 each. https://replayedstudio.com/blog/suno-download-limits-2026/ [3RD-PARTY, UNCONFIRMED]
- Reason Suno gave: make it harder for bad actors to mass-export music (RouteNote, 12 Aug 2026) [3RD-PARTY quoting Suno]; Suno's own blog of 6 Aug 2026 says a downloads policy will restrict mass distribution to streaming services while preserving personal / professional use. https://suno.com/blog/building-the-future-of-music-responsibly [OFFICIAL]

### 7.3 Commercial-use rights (ToS effective 3 Sep 2026, last revised 10 Aug 2026)
- Free: outputs limited to "lawful, personal and non-commercial purposes"; commercial use not allowed; trial downloads "are not eligible for commercial use".
- Pro / Premier: Suno assigns its rights in Output to you; commercial use requires that you "obtained a permitted download" of that Output; rights described as perpetual and not lost on cancellation; Suno makes no warranty that copyright will vest in any Output; Output may resemble other users' Output.
- Remixes of someone else's output are jointly owned and non-commercial only. Creating a Voice Model of another person is prohibited. Suno may append a fingerprint / watermark / metadata and you must not remove it. Getting a copy by any route other than Suno's download channel (stream ripping, recording) is prohibited.
  - https://suno.com/terms (fetched 3 Nov 2026) [OFFICIAL]
  - https://suno.com/pricing: "No commercial rights" (Free), "Commercial use rights" (Pro, Premier), footnote "See the terms of service for limitations on commercial use" [OFFICIAL]
  - https://help.suno.com/en/articles/2746945 ("Do I have the copyrights to songs I made?", undated): Free = Suno owns, non-commercial; Pro/Premier = you own; songs may not be eligible for copyright if wholly AI-made ("Writing the prompt does not constitute the creation of the song"); some distributors exclude non-copyrightable songs [OFFICIAL-UNDATED]
- Songs created while on Free and subscribing later: not retroactively licensed per third-party commentary; official wording not found. [UNCONFIRMED] (older help text: commercial status tied to the plan at creation).
- Practical: Pro/Premier needed to publish commercially, but the real constraint is the monthly download count (20 on Pro, 60 on Premier).

### 7.4 Credits and prices
- Free: 50 credits per day (about 10 songs/day by Suno's older wording), 4 concurrent generations (shared queue), v6-mini only, no downloads beyond trial, no stems.
- Pro: 2,500 credits per month, up to 10 songs at once (priority queue), purchase add-on credits/downloads.
- Premier: 10,000 credits per month, same queue, Studio, Advanced Split, 30-min uploads.
- Subscription credits do not carry over; purchased top-up credits do not expire but need an active subscription.
- Prices on the pricing page: Pro "$8/month" with "Saves $24 by billing yearly" (=> $10 monthly, $8 effective yearly); Premier "$24/month" with "Saves $72 by billing yearly" (=> $30 monthly, $24 effective yearly). Billing toggle says "save 20%". https://suno.com/pricing (3 Nov 2026) [OFFICIAL]; arithmetic of monthly price is mine.
- Per-generation cost: each generation makes two songs for a total of 10 credits; v6 costs the same as previous models; adding many images/videos to a prompt raises the cost; Max Mode costs more (reported 20). https://help.suno.com/en/articles/13924481 (undated) [OFFICIAL-UNDATED]; 20-credit Max Mode figure [3RD-PARTY-MEASURED] https://github.com/bitwize-music-studio/claude-ai-music-skills/issues/562
  - => Pro 2,500 credits ~ 250 generations (500 songs); Premier 10,000 ~ 1,000 generations (2,000 songs) - arithmetic mine; matches the "500 / 2,000 songs" figure on third-party sites.
- Other credit costs: stems Auto 50, Split from Mix 10/stem, Advanced Split 10/stem (https://help.suno.com/en/articles/13925185); Custom Model creation about 100 credits (3rd-party).
- Daily top-up after the monthly allotment is used: older help text says paid users get up to 50 credits/day after monthly credits are gone. https://help.suno.com/en/articles/2410049 (undated) [OFFICIAL-UNDATED]; the pricing page does not mention it - current status [UNCONFIRMED].
- Cancel / annual plan: cancel at suno.com/account. https://help.suno.com/en/articles/13614785 [OFFICIAL-UNDATED]

---------------------------------------------------------------------------------

## 8. Notable 2025-2026 changes that affect how a channel should use Suno

Chronology
- 3 Jun 2025: Song Editor, Stem Extraction (up to 12 stems), uploads up to 8 min, Creative Sliders (Pro/Premier). https://suno.com/release-notes [OFFICIAL]
- 25 Sep 2025: Suno Studio introduced (Premier). https://suno.com/release-notes/introducing-suno-studio [OFFICIAL]
- 19 Nov 2025: $250M raise at $2.45B valuation. https://suno.com/blog [OFFICIAL listing]
- 25 Nov 2025: Warner Music Group settled its lawsuit and signed a licensed-AI partnership with Suno (opt-in controls for artist name/likeness/voice; Suno acquired Songkick; financial terms undisclosed). Reports said downloads would require a paid account and that new licensed models would replace current ones in 2026. https://suno.com/blog "A new chapter in music creation" (25 Nov 2025) [OFFICIAL listing]; coverage https://www.musicweek.com/labels/read/warner-music-group-settles-lawsuit-and-signs-ai-licensing-deal-with-suno/093129 and https://www.engadget.com/entertainment/music/warner-music-drops-lawsuit-against-ai-music-platform-suno-in-exchange-for-licensing-agreement-224619025.html [3RD-PARTY]
- 3 Jun 2026: $400M raise at $5.4B valuation. https://suno.com/blog "The Next Chapter for Suno" [OFFICIAL listing]
- Spring 2026: Believe and TuneCore publicly refused to distribute Suno-made music (about four months before the 8 Sep deal). https://suno.com/blog/believe-partnership (8 Sep 2026: "Earlier in the year, Believe and TuneCore had said they would not distribute music made with Suno's models at that time") [OFFICIAL]; "just over four months" figure from https://www.musicbusinessworldwide.com/suno-inks-global-licensing-deal-with-believe via search excerpt [3RD-PARTY]
- 31 Jul 2026: Munich Regional Court (42nd Civil Chamber) ruled for GEMA against Suno: training on GEMA repertoire and storing/reproducing works breached copyright; licence fees owed; first-instance, appeal status unknown. https://www.gema.de/en/w/suno-entscheidung-2026 (press release 31 Jul 2026) [3RD-PARTY: rights-holder body's own release]; damages / disclosure details from https://www.thestar.com.my/tech/tech-news/2026/07/31/german-court-rules-ai-music-firm-suno-broke-copyright-rules [3RD-PARTY]
- 6 Aug 2026: Suno "How We're Building the Future of Music Responsibly": uploaded audio and lyrics screened with Audible Magic and Musixmatch; artist names left out of training metadata and prompts naming artists/copyrighted songs are redirected; audio watermarking and fingerprinting "in the coming weeks"; new Community Guidelines prohibit recreating existing songs, uploading material without rights, and voice cloning / using someone's likeness without permission (penalties from warnings to permanent bans). https://suno.com/blog/building-the-future-of-music-responsibly (6 Aug 2026) [OFFICIAL]
- 10 Aug 2026: downloads policy + ToS update announced (effective 3 Sep). https://suno.com/blog/suno-updates-tos [OFFICIAL]
- 12 Aug 2026: BMG global licensing deal (recorded + publishing, settles past use, opt-in for BMG artists). https://suno.com/blog "Announcing a Landmark Global Partnership with BMG" [OFFICIAL listing]; detail https://routenote.com/blog/suno-announces-20-monthly-downloads-and-new-music-industry-models/ (12 Aug 2026) [3RD-PARTY]
- 8 Sep 2026: Believe + TuneCore partnership: tracks made with Suno's new industry-partner model become eligible for Believe/TuneCore distribution; Suno's watermarking/fingerprinting and download limits apply to that distribution. https://suno.com/blog/believe-partnership (8 Sep 2026) [OFFICIAL]. Third-party coverage says music from Suno's EARLIER models stays blocked at Believe/TuneCore and that eligibility does not guarantee acceptance by every DSP or monetization program. https://www.aimusicpreneur.com/ai-music-news/suno-believe-tunecore-licensing-partnership-opt-in/ and search excerpts [3RD-PARTY]. Other distributors (DistroKid etc.) policy for v6: [UNCONFIRMED].
- 9 Sep 2026: v6 launch, all older models retired (section 1).
- 18 Sep 2026: UMG and Sony filed a SECOND lawsuit against Suno (D. Mass., reported case 1:26-cv-14275, 60,202 recordings) calling v6 "the fruit of the same poisoned tree"; Suno's CPO says v6 was trained "entirely from scratch" without UMG/Sony recordings; no ruling. https://www.musicbusinessworldwide.com/universal-and-sony-sue-suno-for-a-second-time-claiming-platforms-v6-models-are-the-fruit-of-the-same-poisoned-tree-/ and https://thenextweb.com/news/universal-sony-second-lawsuit-suno-60202-recordings (via search excerpts; pages themselves not opened) [3RD-PARTY]. First UMG/Sony case (filed June 2024) still running; dispositive motions reportedly not until 9 Apr 2027; late Oct 2026 UMG/Sony/DistroKid told the court they are "working on a resolution" about AI-music data. https://www.musicbusinessworldwide.com/umg-sony-and-distrokid-tell-court-they-are-working-on-a-resolution-in-dispute-over-ai-music-data-for-suno-case/ (search excerpt only; page returned 403) [3RD-PARTY, lower confidence]. No UMG or Sony settlement found as of 3 Nov 2026.
- 3 Sep / 28 Oct 2026 etc.: see sections 3 and 7.

Implications for a channel (my reading, not Suno's advice)
1. Only Pro/Premier songs, downloaded through Suno's own download channel, are commercially licensed. Plan the 20 (Pro) or 60 (Premier) downloads per month as the real production quota; re-downloads, WAV+MP3 and stems of the same song cost one. Keep all work inside Studio (Premier) if you need uncapped exports.
2. Cover / upload-of-others'-songs: Suno's help says Cover works only on songs you created; Community Guidelines (6 Aug 2026) ban recreating existing songs and uploads without rights; uploads are screened (Audible Magic, Musixmatch); the ToS makes remixes of other users' tracks non-commercial. Do not build the channel around covers of existing Thai or foreign songs.
3. Do not use artist names in style prompts (rewritten/blocked) and do not make Voices of other people.
4. Do not try to strip or avoid watermarks / fingerprints; ToS prohibits it.
5. Distribution: if the channel will use Believe/TuneCore, only new-model (v6-era) tracks are eligible per Suno; verify other distributors and YouTube policy yourself. YouTube: no official wording retrieved; third-party consensus is AI music is allowed but needs honest disclosure where required and original creative input, avoiding mass-produced near-duplicates. [3RD-PARTY, UNCONFIRMED] e.g. https://dynamoi.com/learn/ai-music-distribution/is-ai-music-allowed-on-youtube
6. Copyright eligibility: Suno itself says a wholly AI-made song may not be copyrightable; own the lyrics and add human edits if registration matters. https://help.suno.com/en/articles/2746945 [OFFICIAL-UNDATED]
7. Litigation risk is live (UMG/Sony vs v6; GEMA first-instance loss). Not legal advice.

---------------------------------------------------------------------------------

## 9. Open questions I could not close for 2026

- Whether Duration slider is officially available on v6 (official note says v5.5; third parties say it is in v6 Advanced).
- Maximum total length after repeated Extend; credit cost of Extend.
- Whether the "Get Whole Song" label still exists in the v6 UI (documented only in an undated help article).
- Whether Voices and Personas work with v6 without an upgrade step; plan-by-plan Persona/Voice limits.
- Upload length for the Pro plan; Cover plan requirement in v6 (undated text says Pro/Premier).
- Thai language quality, pronunciation, and best script (Thai vs romanized) on v6.
- Price of extra downloads; whether the daily 50-credit top-up for paid users still exists.
- Whether YouTube / other distributors treat v6 tracks differently from older-model tracks.
- Note on the repo: the project skill `suno` (listing description: "Covers v3.5/v4/v4.5 ... extension to 3:30") predates v6 and v5.x retirement; I did not read the file, but its model-specific advice should be re-checked against this sheet.
