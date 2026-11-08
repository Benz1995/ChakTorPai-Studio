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
CHILD_VOICE = "w3e1Jn4F37O7wDwETrJ9"
KRU_EK_VOICE = "pqHfZKP75CvOlQylNhV4" # Bill (elderly male)

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
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af",
                            f"asetrate={sr}*{pitch},aresample={sr},atempo={1 / pitch:.4f}", out_file], check=True)
            os.remove(raw)
        print(f"Generated: {os.path.basename(out_file)}")
    except Exception as e:
        print(f"Error generating {out_file}: {e}")

# Narrator lines
narrator_lines = {
    "vo-01.mp3": "ถ้าเสียงระเบิดเพิ่งสงบลง… แต่มีสิ่งอันตรายที่มองไม่เห็นลอยอยู่ทั่วฟ้า… คุณจะกล้าออกไปไหม?",
    "vo-02.mp3": "ประตูเหล็กกระแทกปิดสนิท… ผลโหวตพาเราเลี้ยวเข้ามาหลบในห้องใต้ดินร้านซ่อมวิทยุของครูเอก",
    "vo-03.mp3": "กลิ่นสนิมเหล็กกับฝุ่นตลบอบอวล… ครูเอกรีบเอาเทปผ้าอุดรอยต่อช่องลมอย่างร้อนรน",
    "vo-05.mp3": "พอพัดลมหยุดหมุน… ทั้งห้องก็เหลือเพียงเสียงหายใจหอบของเราสามคนกับหมาหนึ่งตัว",
    "vo-06b.mp3": "ต้นกล้ากอดไดโนเสาร์ไว้แนบอก… ปลอบมันเหมือนกำลังปลอบตัวเอง",
    "vo-07.mp3": "เข็มบนเครื่องวัดรังสีโบราณเริ่มกระดิก… เสียงคลิกดังถี่ขึ้นเรื่อย ๆ ยืนยันว่าฝุ่นมรณะเริ่มโปรยลงมาบนหลังคา",
    "vo-09.mp3": "ถ้าเจอเหตุการณ์วิกฤตแบบนี้จริง จำสามข้อนี้ไว้ให้ขึ้นใจ: หนึ่ง ปิดประตูหน้าต่าง ดับพัดลมและแอร์ทั้งหมด เพื่อไม่ให้ดึงอากาศปนเปื้อนเข้ามา สอง หลบในจุดที่ลึกที่สุด เช่น ห้องใต้ดินหรือใจกลางอาคารที่มีผนังหนาหลายชั้น และสาม กบดานอยู่ข้างในอย่างน้อยยี่สิบสี่ชั่วโมง อย่าเพิ่งออกไปตามหาใคร จนกว่าจะมีประกาศยืนยันความปลอดภัยจากทางการ",
    "vo-10.mp3": "หลักการนี้ใช้ได้จริงในชีวิตประจำวัน… ทั้งตอนเกิดเพลิงไหม้ ควันสารเคมี หรือวันฝุ่นพีเอ็มสองจุดห้าวิกฤต การปิดช่องลมและดับระบบดูดอากาศ จะช่วยกักมลพิษไม่ให้เข้าสู่ปอด",
    "vo-11.mp3": "ความเงียบโรยตัวอยู่ได้ไม่นาน… จู่ ๆ ประตูเหล็กด้านบนก็ถูกกระแทกอย่างแรงจนฝุ่นร่วงกราว",
    "vo-12.mp3": "ข้าวตูลุกขึ้นขู่ฟ่อ… พร้อมเสียงคนแหบแห้งตะโกนลงมา",
    "vo-13.mp3": "ต้นกล้ามองหน้าคุณด้วยความสงสาร… แต่ครูเอกส่ายหน้าเด็ดขาด เพราะการเปิดประตูตอนนี้ จะนำฝุ่นรังสีข้างนอกทะลักลงมาฆ่าทุกคน",
    "vo-14.mp3": "ถ้าเป็นคุณในวินาทีนี้… จะยอมเปิดรับคนบาดเจ็บ หรือกัดฟันปิดตายตามกฎยี่สิบสี่ชั่วโมง? โหวตมา… เอ หรือ บี",
    "vo-15.mp3": "วันที่ 0 ตอนที่ 2 ใต้ดิน เรื่องแต่ง",
}

# Character lines
character_lines = {
    # Kru Ek in shot 4
    "vo-04-kru.mp3": ("[ตึงเครียด เร่งรีบ] ไอ้หนู! รีบไปดึงปลั๊กพัดลมระบายอากาศออกเดี๋ยวนี้! อย่าให้ลมข้างนอกรั่วเข้ามาแม้แต่นิดเดียว!", KRU_EK_VOICE, 1.0),
    # Kru Ek in shot 8
    "vo-08-kru.mp3": ("[จริงจัง หนักแน่น] ไม่ว่าข้างบนจะเงียบแค่ไหน… ห้ามใครโผล่หัวออกไปเด็ดขาด ยี่สิบสี่ชั่วโมงนี้คือชี้เป็นชี้ตาย", KRU_EK_VOICE, 1.0),
    # Ton Kla in shot 6
    "vo-06-child.mp3": ("[กลัว เสียงสั่น] พี่ครับ… แม่จะตามหาเราเจอไหมอ่ะ…", CHILD_VOICE, 1.18),
    # Stranger knocking in shot 12
    "vo-12-stranger.mp3": ("[เจ็บปวด สิ้นหวัง] ช่วยด้วย! เปิดให้ผมที! ข้างนอกไม่ไหวแล้ว!", "N2lVS1w4EtoT3dr4eOWO", 1.0),
}

if __name__ == "__main__":
    print("Generating narrator lines...")
    for fn, txt in narrator_lines.items():
        tts(txt, NARRATOR_VOICE, os.path.join(VO_DIR, fn))
    print("Generating character lines...")
    for fn, (txt, v_id, p) in character_lines.items():
        tts(txt, v_id, os.path.join(VO_DIR, fn), pitch=p)
    print("Done generating ep02 voices.")
