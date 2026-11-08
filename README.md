# ฉากต่อไป (ChakTorPai Studio)

โปรเจกต์ผลิตคอนเทนต์แอนิเมชัน **3D Low-Poly แนวตั้ง (9:16)** สำหรับ YouTube Shorts, Facebook Reels และ Instagram Reels

---

## 🚀 เริ่มต้นใช้งานด่วน (Quick Start)

### 1. สิ่งที่ต้องมีในเครื่อง (Prerequisites)
1. **Python 3.10+**
2. **FFmpeg & ffprobe** (ต้องติดตั้งและเพิ่มลงใน System PATH เรียบร้อย)
   * ตรวจสอบด้วยคำสั่ง: `ffmpeg -version` และ `ffprobe -version`

### 2. ติดตั้ง Dependencies
เปิด Terminal ในโฟลเดอร์นี้ แล้วรัน:
```bash
pip install -r requirements.txt
```

### 3. ตั้งค่า API Key
ไฟล์ `.env` ได้รับการจัดเตรียมไว้แล้ว หากต้องการเปลี่ยนคีย์ ElevenLabs ให้แก้ไขในไฟล์ `.env`:
```env
ELEVENLABS_API_KEY="your-api-key"
```

---

## 🎬 วิธีการเรนเดอร์วิดีโอ (Render Video)

คุณสามารถเรนเดอร์ตอนที่ต้องการได้ด้วยคำสั่งเดียว:

```bash
python scripts/render_episode.py series/day0/ep01
```

หรือบน Windows Command Prompt:
```cmd
render_episode.bat series\day0\ep01
```

สคริปต์จะดำเนินการอัตโนมัติ 6 ขั้นตอน:
1. คำนวณความยาวและไทม์มิ่งตามเสียงพูดจริง (`tl.py`)
2. สร้างเสียง SFX และดนตรีประกอบ (`audio_gen.py`)
3. สร้างซับไตเติล 2 ภาษาด้วยฟอนต์ Kanit (`subs.py`)
4. คอมโพสิตวิดีโอภาพเคลื่อนไหว 1080×1920 30fps (`shots.py`)
5. มิกซ์รวมภาพ เสียงพูด เสียงเอฟเฟกต์ และความดังมาตรฐานโซเชียล (-14 LUFS) (`final.py`)
6. สร้าง Strip ตรวจสอบความปลอดภัย Safe-Zone (`qc.py`)

**ไฟล์วิดีโอผลลัพธ์จะอยู่ที่:**
`series/day0/ep01/render/day0-ep01.mp4`

---

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

```
ChakTorPai Studio/
├── .agents/skills/          # สคริปต์คอมโพสิต, ไพป์ไลน์ และศาสตร์งานเขียนบท
├── assets/fonts/            # ฟอนต์ Kanit และ Prompt สำหรับซับไตเติล
├── series/day0/             # ซีรีส์ "วันที่ 0"
│   ├── characters/          # เลเยอร์ตัวละครโปร่งใส (ครูเอก, ต้นกล้า, ข้าวตู)
│   ├── ep01/                # ตอนที่ 1 · ไซเรน
│   ├── ep02/                # ตอนที่ 2 · ใต้ดิน (สายรอด)
│   ├── ep02_badend/         # ตอนที่ 2B · สถานีใต้ดิน (Bad End)
│   ├── ep03/                # ตอนที่ 3 · เคาะ (สายรอด)
│   ├── ep03_badend/         # ตอนที่ 3B · ปิดตาย (Bad End)
│   ├── SERIES.md            # บันทึกตอนและตัวละครของซีรีส์
│   └── SURVIVAL.md          # ข้อมูลทักษะเอาชีวิตรอดจริง
├── scripts/
│   └── render_episode.py    # สคริปต์รันเรนเดอร์คลิปจบในคำสั่งเดียว
├── render_episode.bat       # ไฟล์รันสำหรับ Windows
├── AGENTS.md                # คู่มือและกฎเหล็กสำหรับ AI Assistant
├── CHANNEL.md               # ข้อมูลช่องทางโซเชียลและแฮชแท็ก
└── requirements.txt         # ไลบรารี Python
```

---

## 🎨 การสร้างภาพและตัวละคร (Image Generation)

ทุกภาพในซีรีส์นี้ถูกสร้างผ่าน **ChatGPT Web** ในเธรดประจำซีรีส์:
🔗 **URL เธรดสร้างภาพ:** [ChatGPT Series Thread](https://chatgpt.com/c/6aee0d87-9e90-83ec-858f-6c64f613fc89)

### กฎการสร้างภาพ:
* **สไตล์:** `Dark low-poly chibi 3D, faceted polygonal origami, cinematic moody lighting, teal shadows, warm highlights, 9:16 vertical`
* **ตัวละครเดิม:** ใส่คำสั่งอ้างอิงเสมอ:
  `"Same exact 3D low-poly chibi faceted origami style and the exact same character design as established in this thread"`
* **ห้ามมีตัวอักษร:** ภาพต้องไม่มีตัวหนังสือ โลโก้ หรือข้อความภาษาอังกฤษฝังลงในภาพ

---

## 📢 บัญชีทางการของช่อง (Official Channels)
* **YouTube:** [@ChakTorPaiStudio](https://www.youtube.com/@ChakTorPaiStudio)
* **Facebook:** [ฉากต่อไป](https://www.facebook.com/profile.php?id=61596425637822)
* **Instagram:** [@chaktorpai](https://www.instagram.com/chaktorpai/)
