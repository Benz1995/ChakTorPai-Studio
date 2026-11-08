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

narrator_lines = {
    "vo-01.mp3": "ถ้าคุณเลือกทิ้งที่หลบภัยที่ใกล้ที่สุด… แล้ววิ่งตามฝูงชนไป… คิดว่าจะรอดจริงหรือ?",
    "vo-02.mp3": "คุณตัดสินใจไม่เชื่อชายแก่… แล้วพาต้นกล้ากับข้าวตูวิ่งตามฝูงชนมุ่งหน้าไปสถานีรถไฟใต้ดิน",
    "vo-03.mp3": "ถนนแน่นขนัดจนแทบไม่มีที่ก้าว… เสียงแตรรถดังระงม ปนเสียงกรีดร้องอย่างบ้าคลั่ง",
    "vo-04.mp3": "หน้าปากทางลงสถานี… คลื่นมนุษย์นับร้อยกำลังแย่งกันเบียดเสียดทะลักลงบันไดแคบ ๆ",
    "vo-06.mp3": "ทันใดนั้น ไฟฟ้าดับวูบ! ประตูชัตเตอร์อัตโนมัติเลื่อนปิดลงมาขวางทาง… คนข้างหน้าล้ม คนข้างหลังยังดันไม่หยุด",
    "vo-07.mp3": "คุณกอดน้องแน่น… แต่ไม่สามารถขยับไปไหนได้เลย ท่ามกลางการเหยียบกันจนขาดอากาศหายใจ",
    "vo-08.mp3": "เหลือศูนย์วินาที… แล้วแสงสว่างวาบก็กลืนกินท้องฟ้าในขณะที่คุณยังติดอยู่กลางแจ้ง",
    "vo-09.mp3": "เสียงระเบิดดังกึกก้อง คลื่นกระแทกพัดเศษกระจกแหลมคมและฝุ่นผงมรณะ ซัดเข้าใส่ฝูงชนอย่างรุนแรง",
    "vo-10.mp3": "จุดจบ: เสียชีวิตจากคลื่นกระแทกและการเหยียบกัน… คุณและต้นกล้า ไม่สามารถเอาชีวิตรอดจากความผิดพลาดครั้งนี้ได้",
    "vo-11.mp3": "เหตุการณ์นี้คือบทเรียนราคาแพง: หนึ่ง การวิ่งตามฝูงชนในที่โล่งเกินสิบนาที นำไปสู่การเหยียบกันตาย และทำให้ติดแหง็กกลางแจ้งเมื่อภัยมาถึง สอง คู่มือความปลอดภัยสากล เรดดี้ดอทกอฟ และ ซีดีซี ระบุชัดเจนว่า อาคารทุกแห่ง ปลอดภัยกว่าที่โล่งแจ้งเสมอ และสาม เมื่อมีสัญญาณเตือน จงมุ่งหน้าเข้าอาคารคอนกรีตที่ใกล้ที่สุดทันที อย่าพยายามวิ่งหนีไปที่ไกล ๆ",
    "vo-12.mp3": "ถ้าอยากมีชีวิตรอด… ย้อนกลับไปเลือก เอ หลบในห้องใต้ดินร้านซ่อมวิทยุของครูเอก! กดติดตามเพื่อดูตอนที่สองเอ",
}

character_lines = {
    "vo-05-child.mp3": ("[ร้องไห้ หวาดกลัว] พี่ครับ! ผมหายใจไม่ออก! ไดโนเสาร์ผมหล่น!", CHILD_VOICE, 1.18),
}

if __name__ == "__main__":
    print("Generating ep02_badend narrator lines...")
    for fn, txt in narrator_lines.items():
        tts(txt, NARRATOR_VOICE, os.path.join(VO_DIR, fn))
    print("Generating ep02_badend character lines...")
    for fn, (txt, v_id, p) in character_lines.items():
        tts(txt, v_id, os.path.join(VO_DIR, fn), pitch=p)
    print("Done generating ep02_badend voices.")
