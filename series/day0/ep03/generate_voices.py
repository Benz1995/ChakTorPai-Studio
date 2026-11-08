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
    ("vo-01.mp3", NARRATOR_VOICE, "ถ้าหลังระเบิดผ่านไป 24 ชั่วโมง… มีคนคุ้นเคยที่เปื้อนฝุ่นมรณะทั้งตัวมาเคาะขอความช่วยเหลือ… คุณจะช่วยเขาอย่างไรโดยไม่ให้ทุกคนตายไปด้วย?", 1.0),
    ("vo-02.mp3", NARRATOR_VOICE, "ผลโหวตตัดสินให้เรากัดฟันปิดตาย… รอจนครบเวลายี่สิบสี่ชั่วโมงตามกฎความปลอดภัย", 1.0),
    ("vo-03.mp3", NARRATOR_VOICE, "เช้าวันที่หนึ่ง… เสียงเคาะประตูด้านบนกลับมาอีกครั้ง คราวนี้เป็นเสียงไอแหบแห้งที่คุ้นหู", 1.0),
    ("vo-04.mp3", SOMSAK_VOICE, "ครูเอกครับ… น้าสมศักดิ์เอง… เปิดให้ผมที… ข้างนอกหายใจไม่ออกแล้ว…", 1.0),
    ("vo-05.mp3", NARRATOR_VOICE, "ครูเอกสวมถุงมือยาง ค่อย ๆ ปลดสลักแง้มดู… ภาพตรงหน้าคือน้าสมศักดิ์ ร้านชำฝั่งตรงข้าม ทั้งตัวขาวโพลนไปด้วยฝุ่นเถ้า", 1.0),
    ("vo-06.mp3", NARRATOR_VOICE, "ต้นกล้ารีบคว้าขวดเจลแอลกอฮอล์กับทิชชู่เปียกจะไปเช็ดตัวให้น้า… แต่ครูเอกตะโกนห้ามลั่น!", 1.0),
    ("vo-07.mp3", KRU_EK_VOICE, "อย่านะไอ้หนู! ห้ามใช้เจลแอลกอฮอล์หรือทิชชู่เปียกเด็ดขาด! มันยิ่งละลายสารเคมีให้ซึมลึกเข้าผิวหนัง!", 1.0),
    ("vo-08.mp3", NARRATOR_VOICE, "ขั้นตอนแรก รีบถอดเสื้อผ้าชั้นนอกออกให้หมด มัดใส่ถุงดำแยกไว้… แค่นี้ก็กำจัดสารปนเปื้อนไปได้ถึง 90%", 1.0),
    ("vo-09.mp3", NARRATOR_VOICE, "จากนั้นใช้น้ำกับสบู่ล้างตัวเบา ๆ ห้ามขัดถูรุนแรงเด็ดขาด เพราะรอยถลอกจะเปิดทางให้สารกัมมันตรังสีซึมเข้ากระแสเลือด", 1.0),
    ("vo-10.mp3", NARRATOR_VOICE, "ถ้าตัวเราหรือคนรอบข้างเปื้อนฝุ่นสารพิษ จำสามข้อนี้ไว้: หนึ่ง ถอดเสื้อผ้าชั้นนอกมัดถุงดำทิ้งทันที กำจัดฝุ่นพิษได้ถึง 90% สอง ล้างตัวด้วยน้ำและสบู่อย่างเบามือ สระผม ล้างหน้า แต่ห้ามขัดถูผิวหนัง สาม ปิดแผลให้สนิทก่อนล้างตัว และห้ามใช้เจลแอลกอฮอล์ล้างสารรังสีเด็ดขาด", 1.0),
    ("vo-11.mp3", NARRATOR_VOICE, "น้าสมศักดิ์ปลอดภัย… แต่น้ำสะอาดในถังยี่สิบลิตรที่ใช้ล้างตัวและประทังชีวิต ตอนนี้เหลือไม่ถึงครึ่งถังแล้ว", 1.0),
    ("vo-12.mp3", NARRATOR_VOICE, "พร้อมข้อความแจ้งเตือนด่วนบนมือถือ: ระบบน้ำประปาปนเปื้อนรังสี… ทางการสั่งห้ามบริโภคน้ำประปาทุกกรณี!", 1.0),
    ("vo-13.mp3", NARRATOR_VOICE, "ถ้าเป็นคุณในสถานการณ์นี้… จะตัดสินใจอย่างไร?", 1.0),
]

if __name__ == "__main__":
    for name, v_id, text, p in LINES:
        out = os.path.join(VO_DIR, name)
        tts(text, v_id, out, pitch=p)
