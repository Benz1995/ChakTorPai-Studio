"""Render the one-page PolyTale handoff summary (1920x1080) -> ../handoff-summary.png.

Shapes and pictures are drawn with Pillow; all Thai text is drawn by libass (ffmpeg ass filter)
so tone marks stack correctly. Usage: python -X utf8 make_summary_image.py
"""
import os
import shutil
import subprocess

from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
PT = os.path.join(ROOT, "workspaces", "video", "PolyTale")
DAY0 = os.path.join(PT, "series", "day0")
FONTS = os.path.join(ROOT, "content-studio", "assets", "fonts")
W, H = 1920, 1080
BG, PANEL, LINE = (16, 18, 23), (28, 31, 39), (52, 57, 70)
YEL, RED = (255, 215, 0), (214, 30, 30)


def cutout(path, box):
    im = Image.open(path).convert("RGBA")
    a = im.getchannel("A").point(lambda v: 255 if v > 128 else 0).getbbox()
    im = im.crop(a)
    im.thumbnail(box, Image.LANCZOS)
    return im


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # header band
    d.rectangle((0, 0, W, 104), fill=(10, 11, 14))
    d.rectangle((0, 100, W, 104), fill=YEL)
    # panels
    panels = {"chars": (36, 136, 560, 760), "steps": (584, 136, 1300, 1044), "status": (1324, 136, 1884, 760),
              "files": (36, 784, 560, 1044), "rules": (1324, 784, 1884, 1044)}
    for x0, y0, x1, y1 in panels.values():
        d.rounded_rectangle((x0, y0, x1, y1), 18, fill=PANEL, outline=LINE, width=2)
    # characters 2x2
    chars = [("boy.png", 60, 210), ("brother.png", 300, 210), ("dog.png", 60, 470), ("kru-ek.png", 300, 470)]
    for f, x, y in chars:
        c = cutout(os.path.join(DAY0, "characters", f), (220, 220))
        img.paste(c, (x + (220 - c.width) // 2, y + (220 - c.height)), c)
    # steps: 8 boxes with arrows
    sx, sy, bh, gap = 620, 200, 86, 22
    for i in range(8):
        y = sy + i * (bh + gap)
        d.rounded_rectangle((sx, y, 1264, y + bh), 14, fill=(36, 40, 50), outline=LINE, width=2)
        d.ellipse((sx + 14, y + 18, sx + 64, y + 68), fill=YEL)
        if i < 7:
            ax = 940
            d.polygon([(ax - 10, y + bh + 4), (ax + 10, y + bh + 4), (ax, y + bh + gap - 4)], fill=YEL)
    # ep01 thumbnail (summary card frame)
    th = Image.open(os.path.join(DAY0, "ep01", "render", "day0-ep01-summary.png")).convert("RGB")
    th = th.resize((198, 352), Image.LANCZOS)
    img.paste(th, (1348, 366))
    d.rectangle((1348, 366, 1546, 718), outline=YEL, width=3)
    fr = Image.open(os.path.join(DAY0, "ep01", "images", "lie-down.png")).convert("RGB").resize((150, 266))
    img.paste(fr.filter(ImageFilter.GaussianBlur(0)), (1566, 452))
    d.rectangle((1566, 452, 1716, 718), outline=LINE, width=2)
    base = os.path.join(HERE, "_summary_base.png")
    img.save(base)

    ev = []

    def t(x, y, text, style="B", an=7):
        ev.append(f"Dialogue: 0,0:00:00.00,0:00:05.00,{style},,0,0,0,,{{\\an{an}\\pos({x},{y})}}{text}")

    t(40, 22, "PolyTale · โพลีเทล  —  ซีรีส์ “วันที่ 0”   สรุปสำหรับส่งต่องาน", "H")
    t(1880, 34, "7 พ.ย. 2569", "S", 9)
    t(60, 150, "ตัวละคร", "P")
    for name, x, y in [("พี่ (คุณ)", 170, 438), ("ต้นกล้า", 410, 438), ("ข้าวตู", 170, 698), ("ครูเอก", 410, 698)]:
        t(x, y, name, "N", 8)
    t(608, 150, "ขั้นตอนทำ 1 ตอน  (สกิล polytale-series)", "P")
    steps = [("1", "เขียนบท + แผนกล้อง", "ฮุก 2 วิ · ช่วงสงบ · จุดพลิก · ภาพละ 2–6 วิ"),
             ("2", "ค้นข้อมูลจริง + วิเคราะห์", "แหล่งทางการ ไทยก่อน · ใส่ SURVIVAL.md · เครดิตทุกข้อ"),
             ("3", "ภาพจาก ChatGPT เว็บ", "ห้องแชตเดียวทั้งซีรีส์ · ภาพเต็ม + เลเยอร์ท่าทาง"),
             ("4", "เสียงพากย์ไทย", "Content Studio · ElevenLabs · ตรวจด้วย ASR"),
             ("5", "เสียงประกอบ + ดนตรี", "audio_gen.py · ตรวจด้วย earshot match"),
             ("6", "timeline.json", "ชอตยืดตามเสียง · บทเรียน · ตัวเลือก A/B · ปุ่มติดตาม"),
             ("7", "เรนเดอร์", "subs → shots → final  (−14 LUFS)"),
             ("8", "ตรวจ + ส่ง", "safe zone · ซับไม่ทับ · earshot critique · ข้อความโพสต์")]
    for i, (n, a, b) in enumerate(steps):
        y = sy + i * (bh + gap)
        t(sx + 39, y + 43, n, "NUM", 5)
        t(sx + 84, y + 10, a, "BB")
        t(sx + 84, y + 50, b, "S")
    t(1348, 150, "สถานะ", "P")
    t(1348, 196, "✓ ep00 เปิดเรื่อง 18 วิ", "B")
    t(1348, 236, "✓ ep01 ไซเรน 97.8 วิ · earshot 23/23", "B")
    t(1348, 276, "◻ เจ้าของฟัง + โพสต์ + ผลโหวต A/B", "B")
    t(1348, 316, "◻ ep02 ใต้ดิน → ep12 ตามแผนบทเรียน", "B")
    t(1348, 722, "การ์ดสรุปท้ายคลิป · ภาพใหม่ต่อบทเรียน", "S")
    t(60, 798, "ไฟล์สำคัญ", "P")
    for i, line in enumerate(["workspaces/video/PolyTale/HANDOFF.md  ← อ่านก่อน",
                              ".agents/skills/polytale-series/SKILL.md",
                              "series/day0/SERIES.md · SURVIVAL.md",
                              "series/day0/ep01/  (ตอนตัวอย่าง)",
                              "Content Studio project 6Q9g7R_TFm"]):
        t(60, 846 + i * 38, line, "M")
    t(1348, 798, "กฎของเจ้าของ", "P")
    for i, line in enumerate(["ไม่ใช้ Google Flow · ใช้ภาพนิ่ง + เลเยอร์",
                              "สอนแต่ข้อมูลจริง มีที่มาทุกข้อ",
                              "ซับไทย/อังกฤษห้ามทับกัน",
                              "ปุ่มติดตามไม่ใส่ชื่อช่อง · ไม่โพสต์เอง",
                              "ข้อความทั้งหมดเป็นภาษาไทย"]):
        t(1348, 846 + i * 38, "• " + line, "M")

    head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: H,Kanit,50,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,7,0,0,0,222
Style: P,Kanit,36,&H0000D7FF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,7,0,0,0,222
Style: B,Kanit,30,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,7,0,0,0,222
Style: BB,Kanit,32,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,7,0,0,0,222
Style: S,Kanit,24,&H00C8C8C8,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,222
Style: M,Kanit,25,&H00DCDCDC,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,222
Style: N,Kanit,30,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,8,0,0,0,222
Style: NUM,Kanit,34,&H00101010,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,5,0,0,0,222

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ass = os.path.join(HERE, "_summary.ass")
    with open(ass, "w", encoding="utf-8-sig") as fh:
        fh.write(head + "\n".join(ev) + "\n")
    fdir = os.path.join(HERE, "_fonts")
    os.makedirs(fdir, exist_ok=True)
    for f in os.listdir(FONTS):
        if f.startswith("Kanit") and f.endswith(".ttf"):
            shutil.copy(os.path.join(FONTS, f), fdir)
    out = os.path.join(PT, "handoff-summary.png")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", "_summary_base.png", "-vf",
                    "ass=_summary.ass:fontsdir=_fonts:shaping=complex", "-frames:v", "1", out], cwd=HERE, check=True)
    for f in ("_summary_base.png", "_summary.ass"):
        os.remove(os.path.join(HERE, f))
    shutil.rmtree(fdir)
    print("wrote", out)


if __name__ == "__main__":
    main()
