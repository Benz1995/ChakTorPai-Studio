# Generator for ep02_badend timeline.json
import json
import os
import sys

NL = chr(92) + 'N'
C = "../characters/"
Q = '"'

tl = {
    "id": "day0-ep02-badend", "series": "วันที่ 0", "episode": "ตอนที่ 2B · สถานีใต้ดิน (ทางเลือกที่ผิด)",
    "content_studio": {"project": "6Q9g7R_TFm", "content": "day0-ep02-badend", "voice": "FfrJDiyJZK"},
    "look": {"sat": 0.88, "contrast": 1.10, "tint": [40, 20, 20], "tint_a": 0.08, "grain": 0.06},
    "shots": [
        {"id": "s01", "len": 4.0, "type": "push", "image": "images/fork.png", "anchor": [0.5, 0.3], "zoom": [1.02, 1.15], "pulse": [255, 30, 30], "pulse_hz": 1.2, "pulse_alpha": 35,
         "vo": "audio/vo-01.mp3", "th": "ถ้าคุณเลือกทิ้งที่หลบภัยที่ใกล้ที่สุด…" + NL + "แล้ววิ่งตามฝูงชนไป…" + NL + "คิดว่าจะรอดจริงหรือ?", "en": "If you leave the nearest shelter" + NL + "to run with the crowd… will you survive?"},
        {"id": "s02", "len": 4.5, "type": "push", "image": "images/fork.png", "zoom": [1.12, 1.02], "transition": "whip",
         "vo": "audio/vo-02.mp3", "th": "คุณตัดสินใจไม่เชื่อชายแก่…" + NL + "แล้วพาต้นกล้ากับข้าวตู" + NL + "วิ่งตามฝูงชน" + NL + "มุ่งหน้าไปสถานีรถไฟใต้ดิน", "en": "You ignored the old man and ran" + NL + "with the crowd toward the subway station."},
        {"id": "s03", "len": 4.5, "type": "push", "image": "images/jam-topdown.png", "zoom": [1.15, 1.05], "end_shake": 5,
         "vo": "audio/vo-03.mp3", "th": "ถนนแน่นขนัดจนแทบไม่มีที่ก้าว…" + NL + "เสียงแตรรถดังระงม" + NL + "ปนเสียงกรีดร้องอย่างบ้าคลั่ง", "en": "The streets were completely blocked." + NL + "Horns blared amidst screams of sheer panic."},
        {"id": "s04", "len": 4.5, "type": "push", "image": "images/fork.png", "anchor": [0.6, 0.4], "zoom": [1.05, 1.18], "end_shake": 6,
         "vo": "audio/vo-04.mp3", "th": "หน้าปากทางลงสถานี…" + NL + "คลื่นมนุษย์นับร้อย" + NL + "กำลังแย่งกันเบียดทะลัก" + NL + "ลงบันไดแคบ ๆ", "en": "At the station entrance," + NL + "a massive crowd surged down the stairs."},
        {"id": "s05", "len": 4.2, "type": "push", "image": "images/brother-scared.png", "anchor": [0.5, 0.4], "zoom": [1.02, 1.12], "end_shake": 4,
         "vo": "audio/vo-05-child.mp3", "th": Q + "พี่ครับ! ผมหายใจไม่ออก!" + NL + "ไดโนเสาร์ผมหล่น!" + Q, "en": Q + "Bro! I can't breathe!" + NL + "I dropped my dinosaur!" + Q},
        {"id": "s06", "len": 5.0, "type": "push", "image": "images/doorway.png", "zoom": [1.08, 1.02], "dim": 0.4,
         "vo": "audio/vo-06.mp3", "th": "ทันใดนั้น ไฟฟ้าดับวูบ!" + NL + "ประตูชัตเตอร์เลื่อนปิดลงมา…" + NL + "คนข้างหน้าล้ม" + NL + "คนข้างหลังยังดันไม่หยุด", "en": "Suddenly power cut!" + NL + "The shutter lowered… crowd crushed."},
        {"id": "s07", "len": 4.5, "type": "push", "image": "images/hands.png", "zoom": [1.04, 1.14], "end_shake": 5,
         "vo": "audio/vo-07.mp3", "th": "คุณกอดน้องแน่น…" + NL + "แต่ไม่สามารถขยับได้เลย" + NL + "ท่ามกลางการเหยียบกัน" + NL + "จนเริ่มขาดอากาศหายใจ", "en": "You held your brother tight," + NL + "completely trapped in the crush."},
        {"id": "s08", "len": 5.0, "type": "push", "image": "images/jam-topdown.png", "zoom": [1.02, 1.12], "pulse": [255, 255, 255], "pulse_hz": 3.0, "pulse_alpha": 80,
         "vo": "audio/vo-08.mp3", "th": "เหลือศูนย์วินาที…" + NL + "แล้วแสงสว่างวาบก็กลืนกินท้องฟ้า" + NL + "ในขณะที่คุณยังติดอยู่กลางแจ้ง", "en": "Zero seconds left." + NL + "A blinding flash engulfed the sky."},
        {"id": "s09", "len": 5.5, "type": "push", "image": "images/aftermath.png", "zoom": [1.0, 1.10], "ash": True, "end_shake": 7,
         "vo": "audio/vo-09.mp3", "th": "เสียงระเบิดดังกึกก้อง" + NL + "คลื่นกระแทกพัดเศษกระจก" + NL + "และฝุ่นผงมรณะ" + NL + "ซัดเข้าใส่ฝูงชนอย่างรุนแรง", "en": "The shockwave hurled glass and fallout" + NL + "directly into the trapped crowd."},
        {"id": "s10", "len": 6.5, "type": "push", "image": "images/aftermath.png", "zoom": [1.05, 1.05], "dim": 0.45, "ash": True,
         "vo": "audio/vo-10.mp3", "th": "จุดจบ: เสียชีวิตจากคลื่นกระแทก" + NL + "และการเหยียบกัน…" + NL + "คุณและต้นกล้า ไม่สามารถรอดชีวิตได้", "en": "BAD END: Crushed and caught in blast." + NL + "You and Ton Kla did not survive."},
        # s11: Lesson Card - no subtitles to avoid collision with lesson text and sources
        {"id": "s11", "len": 27.5, "type": "push", "image": "images/aftermath.png", "zoom": [1.02, 1.08], "dim": 0.35},
        # s12: Choice Card - extended to 14.0s so viewers have 5+ seconds to read options and comment
        {"id": "s12", "len": 14.0, "type": "push", "image": "images/fork.png", "zoom": [1.08, 1.02], "dim": 0.3},
        # s13: Outro / Follow Shot - extended to 7.5s so viewers have ample time to tap follow and exit
        {"id": "s13", "len": 7.5, "type": "push", "image": "images/aftermath.png", "zoom": [1.04, 1.04], "dim": 0.25},
    ],
    "vo": [
        {"file": "audio/vo-11.mp3", "shot": "s11", "at": 0.2},
        {"file": "audio/vo-12.mp3", "shot": "s12", "at": 0.2},
    ],
    "cut_sfx": {"prompt": "air whoosh sound effect", "file": "../ep01/audio/sfx/cut-whoosh.mp3", "gain": 0.08, "lead": 0.2},
    "vo_gain": 1.45,
    "duck": {"ratio": 4.5, "threshold": 0.08},
    "music": {"prompt": "panic and tragedy", "file": "audio/music/full_score.mp3", "at": 0.0, "gain": 0.20, "fade_in": 0.3},
    "sfx": [
        {"id": "traffic", "shot": "s03", "at": 0.0, "dur": 8.0, "file": "../ep01/audio/sfx/traffic.mp3", "gain": 0.08},
        {"id": "crowd", "shot": "s04", "at": 0.0, "dur": 12.0, "file": "../ep01/audio/sfx/crowd.mp3", "gain": 0.08},
        {"id": "blackout", "shot": "s06", "at": 0.2, "dur": 3.0, "prompt": "electrical power grid sudden loud pop and hum shutdown, sparks, silence", "gen_dur": 3.5, "gain": 0.18},
        {"id": "shutter", "shot": "s06", "at": 1.2, "dur": 3.5, "file": "../ep01/audio/sfx/shutter.mp3", "gain": 0.18},
        {"id": "boom", "shot": "s09", "at": 0.0, "dur": 8.0, "file": "../ep01/audio/sfx/boom.mp3", "gain": 0.28},
        {"id": "ring", "shot": "s09", "at": 0.2, "dur": 5.0, "file": "../ep01/audio/sfx/ring.mp3", "gain": 0.08},
        {"id": "sting", "shot": "s13", "at": 0.0, "dur": 7.0, "file": "../ep01/audio/sfx/end-sting.mp3", "gain": 0.40},
        {"id": "tap", "shot": "s13", "at": 1.6, "dur": 0.6, "prompt": "soft user interface button tap", "gen_dur": 0.6, "file": "../ep01/audio/sfx/cut-whoosh.mp3", "gain": 0.20},
    ],
    "stamp": {"shot": "s02", "start": 0.3, "end": "shot_end", "text": "วันที่ 0 · 08:08"},
    "countdown": [{"t0": {"shot": "s02", "at": 0.0}, "t1": {"shot": "s08", "at": 2.5}, "v0": 150, "v1": 0, "hold": 1.0}],
    "lessons": [
        {"shot": "s11", "start": 0.0, "end": "shot_end", "title": "บทเรียนจากความผิดพลาด", "y": 260, "items": [
            {"text": "1. วิ่งในที่โล่งตามฝูงชน เสี่ยงเหยียบกันตาย (Crowd Crush)" + NL + "และไม่พ้นคลื่นกระแทกเมื่อขีปนาวุธมาถึง", "src": "Ready.gov · CDC", "at": {"shot": "s11", "at": 1.0}, "h": 220},
            {"text": "2. กฎสากล: 'อาคารทุกแห่ง ปลอดภัยกว่าที่โล่งแจ้งเสมอ'" + NL + "(Any building is safer than outside)", "src": "Ready.gov · CDC", "at": {"shot": "s11", "at": 6.0}, "h": 220},
            {"text": "3. ได้รับเตือน → มุ่งหน้าเข้าอาคารที่ใกล้ที่สุดทันที" + NL + "อย่าพยายามเดินทางไกล", "src": "Ready.gov · CDC · ปส.", "at": {"shot": "s11", "at": 11.5}, "h": 220}],
            "source": "แนวทางของสหรัฐฯ กรณีระเบิดนิวเคลียร์ · ในไทยให้ทำตามประกาศของทางการเสมอ"},
    ],
    "choice": {"shot": "s12", "start": 0.3, "end": "shot_end", "question": "ต้องการมีชีวิตรอดใช่ไหม?", "a": "ย้อนกลับไปดูตอนที่ 2A (สายรอด)", "b": "ติดตามตอนต่อไป", "cta": "คอมเมนต์ A หรือ B · ย้อนกลับไปแก้มือที่ร้านซ่อมวิทยุ!"},
    "follow": {"shot": "s13", "start": 0.5, "end": "shot_end", "tap": 1.1, "y": 1350},
    "title": {"shot": "s13", "start": 0.0, "end": "shot_end", "badge": "วันที่ 0", "title": "ตอนต่อไป", "note": "กดติดตามเพื่อดูตอนที่ 2A และตอนใหม่ · (เรื่องแต่ง)"},
}

out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), 'timeline.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(tl, f, ensure_ascii=False, indent=1)
print('ep02_badend timeline built successfully')
