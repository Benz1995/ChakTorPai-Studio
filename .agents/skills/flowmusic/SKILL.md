---
name: flowmusic
description: "Co-produce songs with the FlowMusic Producer chat (flowmusic.app) — multi-turn dialogue, recommendation chips, Extend to 3:20–3:40, stems, inpainting and take verification. Secondary song generator for Elyndraze since 3 Nov 2026 (Suno is primary); use when the owner asks for FlowMusic (ทำเพลงใน FlowMusic) or Suno cannot deliver. FlowMusic SFX uses flowmusic-sfx."
---

# FlowMusic AI Interactive Co-Production & Advanced Playbook
## Universal Multi-Agent Standard (Model-Agnostic & Cross-Platform)

Operate `https://www.flowmusic.app` (Producer Mode) as a true musical collaborator and co-producer, not a static one-shot prompt dumper. 

> [!IMPORTANT]
> **Universal Multi-Agent Standard (มาตรฐานรองรับ AI ทุกค่าย):**
> สกิลนี้ออกแบบให้เป็น **Model-Agnostic** และ **Harness-Agnostic** ไม่ผูกขาดกับระบบหรือค่ายใดค่ายหนึ่ง AI Agent ทุกค่าย (เช่น **Claude Code**, **OpenAI ChatGPT / Codex**, **Cursor**, **Windsurf**, **Google Antigravity**, **GitHub Copilot CLI**, หรือ Local Agent) สามารถสวมบทบาทเป็น **AI Music Director (Producer Agent)** และปฏิบัติตามมาตรฐานนี้ได้อย่างแม่นยำและเท่าเทียมกันทุกประการ

FlowMusic AI features an intelligent **conversational Producer engine** that analyzes lyrics, suggests musical directions, generates multiple takes, provides **dynamic recommendation chips** (e.g. `[สลับจังหวะดรัมกรูฟให้แน่นขึ้น]`, `[เปลี่ยนซาวด์สยามป็อปยุค 80s]`, `[แยกสเต็มไปมิกซ์ต่อใน DAW]`), and allows multi-turn iterative sculpting of every musical element.

---

## 🎹 1. System Architecture & Capabilities

```
┌────────────────────────────────────────────────────────────────────────┐
│                      FlowMusic AI Producer Session                     │
│                                                                        │
│  [Prompt / Lyrics] ───► [AI Producer Dialogue] ───► [2 Generated Takes]│
│                               │                           │            │
│                               ▼                           ▼            │
│                    [Dynamic Action Chips]         [Track Context Menu] │
│                    - สลับจังหวะดรัมกรูฟแน่นขึ้น     - Extend (ต่อเพลง)   │
│                    - เปลี่ยนซาวด์สยามป็อป 80s      - Separate Stems    │
│                    - แยกสเต็มไปมิกซ์ต่อใน DAW       - Create Variation  │
│                                                   - Inpaint / Replace  │
└────────────────────────────────────────────────────────────────────────┘
```

### UI Components & Controls
1. **Producer Chat Stream:** Conversational feed where the AI Producer explains arrangement choices, dynamic curves, instrument textures, and artwork style.
2. **Take Cards (Take 1 & Take 2):** Each with Audio Playback, Cover Art (35mm film / cinematic style), Title, Style Tags, Thumbs Up/Down, and `...` More Options.
3. **Dynamic Suggestion Chips (Action Pills):** One-click buttons presented under the AI Producer's reply proposing immediate creative iterations.
4. **Input Bar ("Ask Producer..."):**
   - Text input for creative direction, feedback, or lyric adjustments.
   - `+` Button: Attach files, lyric sheets, or session context.
   - Sliders Icon: Adjust generation parameters (Style fidelity, Creativity, Vocal presence).
   - Audio Waveform Icon: Upload audio reference or melody guide.
5. **Context Menu (`...`) on Each Take:**
   - **Extend:** Continue the track from a specific timestamp (essential for reaching 3:20–3:40).
   - **Separate Stems:** Extract isolated Vocals, Drums, Bass, and Other/Instruments.
   - **Create Variation / Remix:** Spin off variations preserving core melody.
   - **Inpaint / Replace:** Re-record a specific section without rerolling the entire track.
   - **Download:** Grab high-fidelity `.m4a` / `.wav` and Artwork `.jpg`.

---

## 🤝 2. Core Protocol: AI-to-AI Autonomous Co-Production (คุยโต้ตอบเพื่อหาเพลงที่ดีที่สุด)

**หัวใจสำคัญ:** ระบบต้องไม่ข้ามขั้นตอนไปทำวิดีโอทันที แต่ AI Agent (ไม่ว่าจะรันด้วยค่ายใด) ต้องเปิดการสนทนาโต้ตอบ (Multi-Turn Dialogue) กับ FlowMusic Producer อย่างจริงจังเหมือนโปรดิวเซอร์สองคนนั่งคุยกันในห้องอัด เพื่อถกเรื่องดนตรี เปรียบเทียบข้อดีข้อเสียของแต่ละเทค และช่วยกันจูนเสียงจนได้เวอร์ชั่นระดับ Masterpiece

### The 4-Turn Co-Production Dialogue Loop

```
Turn 1: Briefing & Inception
   AI Music Director ส่ง Brief + Lyric Sheet พร้อมถามแนวทางดนตรี 3 สไตล์
   FlowMusic Producer ตอบกลับ + วิเคราะห์ไดนามิก + ให้ 2 เทคแรก

Turn 2: Sound Critique & Option Debating (วิจารณ์และแลกเปลี่ยนความเห็น)
   AI Music Director ตรวจวัดเสียงจริง (ASR, LUFS, กรูฟกลอง) แล้วส่งข้อความวิจารณ์:
   - ชื่นชมจุดเด่น (เช่น การออกเสียงร้องท่อน Verse ของ Take 2)
   - ชี้จุดที่ต้องปรับ (เช่น กรูฟกลองท่อน Chorus ยังไม่พุ่ง หรือเพลงสั้นไป)
   - ขอคำแนะนำเชิงเทคนิค (เช่น "ถ้าใส่ท่อน Solo กีตาร์ 15 วิ ควรปรับบีตยังไง?")
   FlowMusic Producer ตอบคำแนะนำ + เสนอ Action Chips หรือปรับ Arrangement

Turn 3: Tuning & Move Execution (ทดลองเล่นท่าและผสานจุดเด่น)
   ทดลองใช้ท่าพลิกแพลง (เช่น สลับกรูฟกลองแน่นขึ้น, ข้ามยุค 80s, หรือสั่ง Extend)
   ฟังผลลัพธ์ของเทคใหม่ นำมา A/B Test เทียบกับเทคเดิม

Turn 4: Master Locking & Quality Gate
   เมื่อทั้งสองฝ่ายเห็นพ้องว่าได้เพลงที่ดีที่สุด (ร้องชัด 100%, กรูฟแน่น, ยาว 3:20–3:40, ความดัง −14.0 LUFS)
   จึงล็อกเทคนี้เป็น Master Take แล้วถึงส่งไม้ต่อไปทำ Music Video
```

---

## ⚡ 3. วิชาพลิกแพลงท่า (The 8 Advanced Production Moves)

### ท่าที่ 1: Era & Soundscape Morphing (ข้ามยุคเปลี่ยนซาวด์)
* **What it does:** Re-imagines the approved melody and lyrics in a completely different musical era without losing the song's emotional core.
* **How to trigger:**
  - Click chip: `[ เปลี่ยนซาวด์สยามป็อปยุค 80s ]`
  - Or prompt the Producer:
    ```text
    ลอง Re-arrange เพลงนี้ในสไตล์ "80s Siam Pop" ยุคทอง:
    - กลอง Linndrum พร้อม Reverb Snare แน่นๆ
    - ซินธ์ Yamaha DX7 และ Roland Juno คอร์ดหวานปนเหงา
    - กีตาร์โปร่งใส่เอฟเฟกต์ Chorus กว้างๆ
    - ร้องประสาน Double-tracking นุ่มนวล ชวนย้อนวันวาน
    ```
* **Other Era Presets to Morph:**
  - `90s Thai Alt-Rock`: Crunch electric guitars, raw drum kit, emotional rasp (สไตล์ Silly Fools / Blackhead).
  - `City Pop Bangkok`: Funky slap bass, Rhodes electric piano, jazzy brass accents, breezy groove.
  - `Modern Bedroom Pop (2026)`: Tape saturation, detuned lo-fi keys, sub-bass 808, whispery intimate vocals.

---

### ท่าที่ 2: Groove & Rhythm Sculpting (ดัดจังหวะและกรูฟให้กระชับ)
* **What it does:** Fixes lagging energy or rhythm clashes between vocal syllables and drum patterns.
* **How to trigger:**
  - Click chip: `[ สลับจังหวะดรัมกรูฟให้แน่นขึ้น ]`
  - Or instruct specific groove surgery:
    ```text
    ขอปรับกรูฟกลองใหม่:
    - ใน Verse: เปลี่ยนสแนร์เป็น Rim click เบาๆ ให้เสียงร้องเด่นชัด ไม่รก
    - ใน Pre-Chorus: ใส่ Tom fill ส่งอารมณ์ และให้เบสเดินโน้ตเชื่อม 8th notes
    - ใน Chorus: สลับเป็น Four-on-the-floor kick แน่นๆ พร้อม Open hi-hat ยกจังหวะให้โยกตามได้
    ```

---

### ท่าที่ 3: Seamless Extension & Outro Stitching (วิชาต่อเพลง 3:20–3:40)
* **What it does:** AI generations often stop naturally at 2:30–3:00. This move seamlessly extends the track into a radio-ready full single (3:20–3:40) with an epic climax and clean stop.
* **How to trigger:**
  1. Identify the timestamp where Chorus 2 ends (e.g. `02:18`).
  2. Click `...` on the chosen take -> Select **Extend from this point**.
  3. Prompt the extension:
     ```text
     ต่อเพลงจาก 02:18 ด้วยโครงสร้างดังนี้:
     [Guitar Solo: 16 บาร์ อารมณ์กรีดร้อง เมโลดี้ล้อกับท่อนฮุก]
     [Bridge: ดรอปเครื่องดนตรี เหลือเพียงฟลอร์ทอม, เบส และเสียงร้องกระซิบ]
     [Last Chorus: ระเบิดเครื่องดนตรีเต็มสูบ เพิ่ม Ad-libs เสียงสูง]
     [Outro: กีตาร์คลีนตีคอร์ดช้าลง จบด้วย Drum Kick Stop ชัดเจน ไม่ Fade out]
     ```

---

### ท่าที่ 4: Micro Inpainting & Syllable Correction (วิชาซ่อมเฉพาะท่อน)
* **What it does:** Fixes a single mispronounced Thai tone or awkward phrase without throwing away a master-level vocal performance.
* **How to trigger:**
  1. Open take context menu `...` -> Select **Inpaint / Replace Section**.
  2. Highlight the time range (e.g. `01:12 - 01:18`).
  3. Enter phonetic spelling or vocal direction:
     ```text
     ท่อนนี้ร้องวรรณยุกต์คำว่า "{คำร้อง}" ให้ชัดถ้อยชัดคำ หางเสียงลงต่ำตามสำเนียงพูดธรรมชาติ
     ```

---

### ท่าที่ 5: Stem Separation & Hybrid Studio Mixing (วิชาแยกสเต็มทำ Pro Mix)
* **What it does:** Bypasses all AI audio compression artifacts by separating individual multitrack stems for studio mastering.
* **How to trigger:**
  - Click chip: `[ แยกสเต็มไปมิกซ์ต่อใน DAW ]` or `...` -> **Separate Stems**.
  - FlowMusic generates 4 distinct stems:
     1. `vocal.wav` (Lead & backing vocals)
     2. `drums.wav` (Kick, snare, hi-hat, cymbals)
     3. `bass.wav` (Bass guitar / synth bass)
     4. `other.wav` (Guitars, keys, pads, orchestral layers)
* **Hybrid Post-Processing (Any DAW or Local FFmpeg):**
  - In BigO or local terminal, use FFmpeg or Earshot to:
    - Apply sidechain compression on `other.wav` against `vocal.wav` (vocal clarity).
    - EQ `vocal.wav` with high-shelf sparkle at 10 kHz and de-ess harsh sibilance.
    - Master the final mix to exactly **−14.0 LUFS ± 0.5** with True Peak ≤ −1.0 dBFS.

---

### ท่าที่ 6: Audio Reference Prompting (วิชาใช้เพลงอ้างอิงผ่าน Waveform)
* **What it does:** Locks the AI to a specific melody motif, chord progression, or acoustic groove.
* **How to trigger:**
  - Click the **Waveform icon** or `+` in the prompt bar.
  - Upload a 10–30s audio clip (e.g., an acoustic guitar strumming pattern or a vocal hum).
  - Instruct: *"Use the harmonic progression and tempo of this audio clip as the bed for the provided Thai lyrics."*

---

### ท่าที่ 7: Parameter Sliders Hacking (วิชาจูนหลังม่าน)
* **What it does:** Controls the AI's internal probabilistic sampling via the Sliders icon:
  - **Style Strength (ความเข้มข้นของแนวเพลง):** 
    - 60–70%: สำหรับเพลงอินดี้ไทยที่ต้องการความเป็นธรรมชาติ ปราศจากเสียงสังเคราะห์สังเกตได้
    - 85–95%: สำหรับเพลงไซไฟ, อิเล็กทรอนิกส์ หรือ 80s Synthwave ที่ต้องการซาวด์จัดจ้าน
  - **Vocal Presence (ความโดดเด่นของเสียงร้อง):**
    - High: ดันเสียงร้องไทยให้ลอยเด่นอยู่หน้ามิกซ์ เหมาะกับเพลงอกหักเน้นเนื้อหา
  - **Creativity / Temperature:**
    - Low (0.6): ยึดเมโลดี้ตามวรรณยุกต์ไทยอย่างเคร่งครัด
    - High (0.85): ปล่อยให้ AI อิมโพรไวส์ลูกเอื้อนและไลน์ส่งดนตรีใหม่ๆ

---

### ท่าที่ 8: Dual-Take Hybrid Fusion (วิชาผสานสองเทค)
* **What it does:** Combines the best elements of Take 1 and Take 2.
* **How to execute:**
  - Compare Take 1 vs Take 2:
    - *Example:* Take 1 has superior emotive vocal phrasing in Verse, but Take 2 has a much punchier rock chorus.
  - Prompt Producer:
    ```text
    เทค 1 ร้องท่อน Verse ได้กินใจมาก แต่เทค 2 มีพลังกลองและกีตาร์ท่อน Chorus ที่ยอดเยี่ยม
    ขอสร้างเวอร์ชั่นใหม่ที่ดึง Dynamic Arrangement หนักแน่นแบบเทค 2 แต่ให้สไตล์การร้องท่อน Verse อารมณ์เดียวกับเทค 1
    ```

---

## 📋 4. Universal Multi-Agent Execution Protocol (Any AI Platform)

เมื่อ AI Agent (ไม่ว่าจะค่ายใด) ได้รับคำสั่งให้ร่วมงานกับ FlowMusic ให้ปฏิบัติตามขั้นตอนมาตรฐานดังนี้:

```
[1. Brief & Inception] ──► [2. Inspect Generation & Takes]
                                    │
                                    ▼
                     [3. Extract & Report Suggestion Chips]
                                    │
                                    ▼
                     [4. Multi-Turn Co-Production Dialogue]
                                    │
                                    ▼
                     [5. Execute Tuning (80s / Groove / Stems / Extend)]
                                    │
                                    ▼
                     [6. Verify LUFS & Log Session Receipt]
```

### Protocol Checklist สำหรับ AI Agent ทุกค่าย:
1. **Never spam WebSocket / Remote Debugging connections:** 
   - อย่ารันสคริปต์เชื่อมต่อ browser ซ้ำๆ เป็นลูปที่ทำให้ Chrome เด้งถามสิทธิ์ Remote Debugging บนหน้าจอของผู้ใช้
   - ใช้ Session ที่เปิดค้างไว้ หรือใช้ Cua Browser APIs / Standard Web automation ตามแนวทางความปลอดภัย
2. **Standard CLI & Shell Operations (Cross-Platform):**
   - รันการตรวจสอบเสียงจริงผ่าน Terminal มาตรฐาน:
     - Whisper ASR: `python -X utf8 workspaces/music/Elyndraze/tools/musicvideo/asr_song.py <audio> <out.json>`
     - Loudness Normalization: `ffmpeg -i <in> -af loudnorm=I=-14.0:TP=-1.5:LRA=11 <out.wav>`
     - Duration & Streams: `ffprobe -v quiet -print_format json -show_format <file>`
3. **Multi-Agent State Sharing & Hand-off Standard:**
   - บันทึกการสนทนาโต้ตอบและประวัติการตัดสินใจไว้ใน:
     `workspaces/music/<channel>/songs/<song-id>/team/flow-co-production-dialogue.md`
   - บันทึกสถานะเชิงโครงสร้าง (URLs, Take IDs, Chips, Parameters) ใน:
     `workspaces/music/<channel>/songs/<song-id>/team/flow-session.json`
   - สิ่งนี้ช่วยให้ **AI Agent ต่างค่ายสามารถทำงานต่อกันได้ทันที** (เช่น Claude Code เริ่มแต่งเนื้อ -> Codex ช่วยคุยจูนกรูฟใน FlowMusic -> Antigravity ตรวจวัดและเรนเดอร์ MV) โดยไม่มีข้อมูลสูญหาย

---

## 🎯 5. Quick Reference: Thai Vocal Anti-Cliché Rules
เมื่อสั่งการหรือคุยกับ FlowMusic สำหรับช่องเพลงไทย (Elyndraze / RetroChill Town):
- **No robotic autotune:** ย้ำเรื่อง organic studio capture, breath nuances, และเสียงพูดกึ่งกระซิบที่เป็นธรรมชาติ
- **Natural Thai Rhymes:** รักษาฉันทลักษณ์และสัมผัสใน (internal rhymes) ห้าม AI ตัดหรือบิดคำเพื่อหลบจังหวะ
- **Definite Ending:** ปฏิเสธ computer fade-out ที่ค่อยๆ ดับ; ยืนยันให้จบด้วย Drum stop ชัดเจน หรือปล่อยให้เสียงสายกีตาร์ค่อยๆ กังวานดับลงอย่างสงบ
