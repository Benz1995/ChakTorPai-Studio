import urllib.request
import json
import os
import subprocess

def get_key():
    curr = os.path.abspath(os.path.dirname(__file__))
    while curr and os.path.dirname(curr) != curr:
        p = os.path.join(curr, "content-studio", ".env")
        p2 = os.path.join(curr, ".env")
        for check_p in (p2, p):
            if os.path.exists(check_p):
                for line in open(check_p, encoding="utf-8"):
                    if line.startswith("ELEVENLABS_API_KEY="):
                        v = line.split("=", 1)[1].strip().strip('"')
                        if v:
                            return v
        if False and os.path.exists(p):
            for line in open(p, encoding="utf-8"):
                if line.startswith("ELEVENLABS_API_KEY="):
                    v = line.split("=", 1)[1].strip().strip('"')
                    if v:
                        return v
        curr = os.path.dirname(curr)
    raise RuntimeError("ELEVENLABS_API_KEY not found")

KEY = get_key()

NARRATOR_VOICE = "XELzaccf66eUgLtL3BV1"
KRU_EK_VOICE = "pqHfZKP75CvOlQylNhV4"
SOMSAK_VOICE = "N2lVS1w4EtoT3dr4eOWO"

VO_DIR = os.path.join(os.path.dirname(__file__), "audio")
os.makedirs(VO_DIR, exist_ok=True)

def tts(text, voice_id, out_file, pitch=1.0, stability=0.5):
    if os.path.exists(out_file):
        print(f"Skipping {os.path.basename(out_file)}, already exists")
        return
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    body = {
        "text": text,
        "model_id": "eleven_v3",
        "voice_settings": {
            "stability": stability,
            "similarity_boost": 0.75
        }
    }
    raw = out_file if pitch == 1.0 else out_file.replace(".mp3", ".raw.mp3")
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"), method="POST",
                                 headers={"xi-api-key": KEY, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
        with open(raw, "wb") as f:
            f.write(data)
        if pitch != 1.0:
            sr = 44100
            subprocess.run([
                "ffmpeg", "-y", "-i", raw,
                "-af", f"asetrate={sr}*{pitch},aresample={sr}",
                out_file
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if os.path.exists(raw):
                os.remove(raw)
        print(f"Generated: {os.path.basename(out_file)}")
    except Exception as e:
        print(f"Error {out_file}: {e}")

LINES = [
    ("vo-01.mp3", NARRATOR_VOICE, "ถ้าในตอนที่สอง คุณเลือกโหวต บี… กัดฟันปิดตายประตูเหล็กยี่สิบสี่ชั่วโมง และไม่ยอมเปิดรับเสียงเคาะของน้าสมศักดิ์…", 1.0),
    ("vo-02.mp3", NARRATOR_VOICE, "เรายืนนิ่งเงียบอยู่ในความมืด… เสียงน้าสมศักดิ์ทุบประตูเหล็กดังสะท้อนก้องลงมา:", 1.0),
    ("vo-03.mp3", SOMSAK_VOICE, "เปิดเถอะครูเอก… ผมแสบตาไปหมดแล้ว… หายใจไม่ออก… ได้โปรดเถอะครับ…", 1.0),
    ("vo-04.mp3", NARRATOR_VOICE, "ต้นกล้ากอดตุ๊กตาไดโนเสาร์ร้องไห้… ข้าวตูนอนครางหงิง ๆ อยู่หน้าประตูเหล็กที่สั่นสะเทือน", 1.0),
    ("vo-05.mp3", NARRATOR_VOICE, "เวลาผ่านไปอย่างทรมาน… เสียงเคาะด้านบนค่อย ๆ แผ่วลง… แผ่วลง… จนกระทั่งทุกอย่างเงียบสนิท", 1.0),
    ("vo-06.mp3", NARRATOR_VOICE, "เช้าวันที่หนึ่ง… ครบกำหนดยี่สิบสี่ชั่วโมง ครูเอกค่อย ๆ ปลดสลักแง้มประตูเหล็กขึ้นไปดู…", 1.0),
    ("vo-07.mp3", NARRATOR_VOICE, "ภาพตรงหน้าคือน้าสมศักดิ์… นอนหมดสติอยู่บนพื้นเถ้าถ่าน ร่างกายชักเกร็งจากการสูดฝุ่นรังสีเข้มข้นตลอดทั้งคืน", 1.0),
    ("vo-08.mp3", KRU_EK_VOICE, "ไอ้หนู… ถ้าเรารู้วิธีล้างสารปนเปื้อนแต่แรก… น้าเขาก็ไม่ต้องมาจบชีวิตแบบนี้…", 1.0),
    ("vo-09.mp3", NARRATOR_VOICE, "เหตุการณ์นี้คือบทเรียนราคาแพง: หนึ่ง กฎ 24 ชม. มีไว้ปกป้องเรา แต่ถ้ามีคนเคาะ สามารถรับเข้าได้หากรู้วิธีชำระล้างทันที สอง ถอดเสื้อผ้าชั้นนอกและล้างตัวด้วยน้ำสบู่เบา ๆ กำจัดฝุ่นพิษได้ถึง 90% สาม การปล่อยผู้รอดชีวิตไว้ข้างนอกโดยไม่ช่วยเหลือ นำไปสู่อาการรับรังสีเฉียบพลันถึงแก่ชีวิต", 1.0),
    ("vo-10.mp3", NARRATOR_VOICE, "ถ้าอยากมีชีวิตรอด… ย้อนกลับไปดูตอนที่ 3 สายรอด หรือติดตามตอนต่อไป", 1.0),
]

if __name__ == "__main__":
    for name, v_id, text, p in LINES:
        out = os.path.join(VO_DIR, name)
        tts(text, v_id, out, pitch=p)
