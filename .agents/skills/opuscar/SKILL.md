---
name: opuscar
description: "Direct and produce short films, explainers, tech keynotes, documentaries, and art animations made entirely in code (HTML5 Canvas, WebGL, Three.js) using BigO's local Opuscar engine (content-studio/local-opuscar). Zero diffusion video generation, zero stock footage, frame-accurate timing, procedural audio and sound design, and automated QC gates (readcheck, asr-check, loudnorm). Use for หนังสั้นจากโค้ด, คลิปอธิบายแบบกราฟิก or keynote-style videos without generated imagery."
---

# Opuscar — Code-Driven Film Studio for BigO

**Opuscar** is a local, programmatic animation studio integrated into BigO Content Studio (`content-studio/local-opuscar/`). It renders short films (30–60s), product explainers, and artistic sequences **entirely through code**:
- **Visuals**: Procedural Canvas 2D, Three.js PBR, and WebGL2 shaders rendered frame-by-frame via Playwright headless Chrome into FFmpeg.
- **Voiceover**: Offline English (Kokoro), Thai & Chinese neural voices (Microsoft Edge-TTS with phonetic `say` mapping), and automated Faster-Whisper ASR script verification.
- **Audio & Score**: Procedural foley synthesis (numpy/scipy filters, clicks, thumps, whooshes) synced to visual hit points (`events.json`), instrument sampling (VCSL, Freepats), and two-pass loudness mastering (-14 LUFS, TP -1.2 dB).

---

## 🚀 Quick Execution (Windows PowerShell Runner)

Run from `content-studio/local-opuscar/` using `render.ps1`:

```powershell
# 1. Environment check
.\render.ps1 doctor

# 2. Preview still frames at time t (seconds)
.\render.ps1 still <demo_dir> 1.5

# 3. Check on-screen text dwell time (Readcheck Gate)
.\render.ps1 readcheck <demo_dir>

# 4. Generate Thai Voiceovers (Edge-TTS Premwadee / Niwat)
.\render.ps1 tts <lines.json> <out_dir> th

# 5. Render full MP4 video (multi-worker parallel Chrome headless)
.\render.ps1 video <demo_dir> 24 3 <out_file>

# 6. Mux audio & video with 2-pass Loudnorm (-14 LUFS) and film grain
.\render.ps1 mux <video.mp4> <audio.wav> <out.mp4> 24 2
```

---

## 🎨 67 Production-Grade Film Styles

All styles reside in `content-studio/local-opuscar/styles/<slug>/` with full `STYLE.md` rules and executable `demo/` code:

| Category | Styles |
|---|---|
| **Edit & Documentary (8)** | `caption-news`, `newsreel`, `countdown`, `city-symphony`, `visual-investigation`, `kino-montage`, `telestrator`, `news-package` |
| **Evidence Films (8)** | `satellite-briefing`, `briefing-board`, `lidar-survey`, `white-model`, `data-physical`, `teardown`, `microscope`, `archive-lighttable` |
| **Hand-drawn & Painting (8)** | `crayon-book`, `watercolor`, `ink-wash`, `impasto`, `one-line`, `whiteboard`, `urban-sketch`, `chalkboard` |
| **East Asian Traditions (4)** | `shadow-puppet`, `ukiyoe`, `papercut-red`, `paper-lantern` |
| **Print & Printmaking (6)** | `risograph`, `halftone-dossier`, `woodcut`, `engraving`, `silkscreen-poster`, `printed-long-take` |
| **Graphic & Type (7)** | `swiss-motion`, `spy-titles`, `art-deco`, `blueprint`, `stained-glass`, `pictogram-motion`, `ascii-crt` |
| **Information & Keynote (8)**| `dataviz`, `iso-infographic`, `dark-keynote`, `living-screencast`, `hologram-hud`, `transit-map`, `isometric-picture-book`, `circuit-board` |
| **Cartoon & Anime (4)** | `rubber-hose`, `cel-anime-80s`, `scifi-toon`, `midcentury-toon` |
| **Games (4)** | `pixel-rpg`, `hd-2d`, `microgame`, `game-show` |
| **Cinema & Eras (2)** | `silent-film`, `backrooms` |
| **Materials & 3D (7)** | `brick-toy`, `paper-popup`, `tilt-shift`, `lowpoly-island`, `glass-product`, `memphis-diorama`, `desktop-flythrough` |

---

## 🎬 Directing Standards (`DIRECTOR.md`)

When creating an Opuscar film, follow these mandatory rules:
1. **Hook in the first 3 seconds**: Never start with a slow static logo.
2. **Signature Shot**: At least 1 memorable camera move or transition born from the medium itself (e.g. paper fold, ink bloom, CAD explosion).
3. **At least 4 camera framings**: Vary between Wide, Medium, Close, Insert, and dynamic tracking.
4. **Music Grid First**: BPM and cue map drive visual hit points (aim for 0 ms sync).
5. **Dynamic Pacing & 2 Real Silences**: Include at least two moments of digital zero / room tone before major dramatic turns.

---

## 🇹🇭 Thai Language Contracts & Pronunciation

1. **Edge-TTS Thai Voices**:
   - Default Female: `th-TH-PremwadeeNeural` (Friendly, Positive)
   - Default Male: `th-TH-NiwatNeural` (Friendly, Positive)
2. **Foreign & English Word Handling**:
   - Edge-TTS Thai voices fail on unpronounceable Latin characters.
   - Always map English brand names/terms in the `say` property using Thai phonetics while keeping proper English in `text`:
     ```json
     {
       "id": "line_01",
       "text": "เปิดตัว BigO Content Studio สตูดิโอคอนเทนต์เจเนอเรชันใหม่",
       "say": "เปิดตัว บิ๊กโอ คอนเทนต์ สตูดิโอ สตูดิโอคอนเทนต์เจเนอเรชันใหม่"
     }
     ```
3. **Thai Fonts & Word Segmentation**:
   - Use Google Fonts Thai OFL: Prompt, Kanit, Sarabun, Mitr.
   - For Canvas 2D text wrapping, break Thai phrases with `Intl.Segmenter` or `pythainlp.tokenize.word_tokenize`.

---

## 🛡️ BigO Quality Gates Integration

- **Readcheck Gate (`readcheck.mjs`)**:
  Ensures on-screen text and captions hold long enough for human reading:
  $$\text{Dwell Time} \ge \frac{\text{Thai/CJK}}{4.5} + \frac{\text{Latin}}{15} + 1.5\text{s}$$
- **ASR Gate (`asr_check.py`)**:
  Transcribes TTS WAVs with Faster-Whisper and validates character match $\ge 0.90$ to guarantee zero mispronunciations.
- **Audio Mastering**:
  All exports pass through two-pass FFmpeg EBU R128 `loudnorm` (-14 LUFS, TP -1.2 dB, LRA 11).
