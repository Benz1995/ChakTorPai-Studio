# Generator for ep03_badend timeline.json
import json
import os
import sys

NL = chr(92) + 'N'
C = "../characters/"
Q = '"'

tl = {
    "id": "day0-ep03-badend", "series": "วันที่ 0", "episode": "ตอนที่ 3 · ทางเลือกที่ผิด (Bad End)",
    "content_studio": {"project": "6Q9g7R_TFm", "content": "day0-ep03-badend", "voice": "FfrJDiyJZK"},
    "look": {"sat": 0.88, "contrast": 1.08, "tint": [40, 30, 50], "tint_a": 0.06, "grain": 0.06},
    "shots": [
        {"id": "s01", "len": 9.04, "type": "push", "image": "images/eyes-ecu.png", "anchor": [0.5, 0.22], "zoom": [1.04, 1.18], "pulse": [255, 30, 30], "pulse_hz": 1.1, "pulse_alpha": 30,
         "vo": "audio/vo-01.mp3", "th": "ถ้าในตอนที่สอง คุณเลือกโหวต บี…" + NL + "กัดฟันปิดตายประตูเหล็กยี่สิบสี่ชั่วโมง" + NL + "และไม่ยอมเปิดรับเสียงเคาะของน้าสมศักดิ์…", "en": "If in Episode 2 you chose Option B… keeping it deadlocked for 24 hours, ignoring Somsak's knocking…"},
        {"id": "s02", "len": 5.52, "type": "push", "image": "images/bunker-hatch-locked.png", "zoom": [1.04, 1.12], "pan": 15,
         "vo": "audio/vo-02.mp3", "th": "เรายืนนิ่งเงียบอยู่ในความมืด…" + NL + "เสียงน้าสมศักดิ์ทุบประตูเหล็ก" + NL + "ดังสะท้อนก้องลงมา:", "en": "We stood frozen in the dark as frantic pounding echoed above:"},
        {"id": "s03", "len": 5.28, "type": "push", "image": "images/bunker-hatch-locked.png", "anchor": [0.5, 0.4], "zoom": [1.08, 1.20], "end_shake": 8, "transition": "whip",
         "vo": "audio/vo-03.mp3", "th": Q + "เปิดเถอะครูเอก… ผมแสบตาไปหมดแล้ว…" + NL + "หายใจไม่ออก… ได้โปรดเถอะครับ…" + Q, "en": Q + "Open up Kru Ek… my eyes are burning… I can't breathe… please!…" + Q},
        {"id": "s04", "len": 6.64, "type": "push", "image": "images/brother-dog-crying.png", "anchor": [0.5, 0.6], "zoom": [1.02, 1.10], "end_shake": 4, "pan": -10,
         "vo": "audio/vo-04.mp3", "th": "ต้นกล้ากอดตุ๊กตาไดโนเสาร์ร้องไห้…" + NL + "ข้าวตูนอนครางหงิง ๆ" + NL + "อยู่หน้าประตูเหล็กที่สั่นสะเทือน", "en": "Ton Kla wept hugging his dinosaur, while Khao Tu whined by the vibrating hatch."},
        {"id": "s05", "len": 7.92, "type": "push", "image": "images/bunker-hatch-locked.png", "zoom": [1.10, 1.02], "dim": 0.25,
         "vo": "audio/vo-05.mp3", "th": "เวลาผ่านไปอย่างทรมาน…" + NL + "เสียงเคาะด้านบนค่อย ๆ แผ่วลง… แผ่วลง…" + NL + "จนกระทั่งทุกอย่างเงียบสนิท", "en": "Hours dragged in agony… the desperate pounding grew weaker, until silence fell."},
        {"id": "s06", "len": 7.04, "type": "push", "image": "images/kru-ek-open-hatch.png", "anchor": [0.5, 0.4], "zoom": [1.02, 1.10], "transition": "whip",
         "vo": "audio/vo-06.mp3", "th": "เช้าวันที่หนึ่ง… ครบกำหนดยี่สิบสี่ชั่วโมง" + NL + "ครูเอกค่อย ๆ ปลดสลัก" + NL + "แง้มประตูเหล็กขึ้นไปดู…", "en": "Day 1 morning… 24 hours up, Kru Ek slowly unlatched the hatch to look outside…"},
        {"id": "s07", "len": 8.80, "type": "push", "image": "images/neighbour-collapsed-ash.png", "anchor": [0.5, 0.5], "zoom": [1.03, 1.12], "end_shake": 2,
         "vo": "audio/vo-07.mp3", "th": "ภาพตรงหน้าคือน้าสมศักดิ์… นอนหมดสติอยู่บนพื้นเถ้าถ่าน" + NL + "ร่างกายชักเกร็งจากการสูดฝุ่นรังสีเข้มข้น" + NL + "ตลอดทั้งคืน", "en": "Outside lay Uncle Somsak… unconscious in the toxic ash, convulsing from severe radiation poisoning."},
        {"id": "s08", "len": 7.28, "type": "push", "image": "images/kru-ek-open-hatch.png", "anchor": [0.5, 0.35], "zoom": [1.10, 1.22], "dim": 0.15,
         "vo": "audio/vo-08.mp3", "th": Q + "ไอ้หนู… ถ้าเรารู้วิธีล้างสารปนเปื้อนแต่แรก…" + NL + "น้าเขาก็ไม่ต้องมาจบชีวิตแบบนี้…" + Q, "en": Q + "Kid… if we knew how to decontaminate him from the start… he wouldn't have ended like this…" + Q},
        # s09: Lesson Card "บทเรียนจากความผิดพลาด" - clean typography, NO bottom subtitle overlap
        {"id": "s09", "len": 24.0, "type": "push", "image": "images/bunker-hatch-locked.png", "zoom": [1.02, 1.08], "dim": 0.40},
        # s10: Choice Card - extended hold 14.0s
        {"id": "s10", "len": 14.0, "type": "push", "image": "images/bunker-hatch-locked.png", "zoom": [1.05, 1.10], "dim": 0.45},
        # s11: Outro Follow Card - extended hold 8.0s
        {"id": "s11", "len": 8.0, "type": "push", "image": "images/basement-radio.png", "zoom": [1.04, 1.04], "dim": 0.25},
    ],
    "vo": [
        {"file": "audio/vo-09.mp3", "shot": "s09", "at": 0.2},
        {"file": "audio/vo-10.mp3", "shot": "s10", "at": 0.2},
    ],
    "cut_sfx": {"prompt": "air whoosh sound effect, quick swoosh of wind passing by, no drums", "gen_dur": 1.2, "file": "../ep01/audio/sfx/cut-whoosh.mp3", "gain": 0.08, "lead": 0.2},
    "vo_gain": 1.45,
    "duck": {"ratio": 4.5, "threshold": 0.08},
    "music": {"prompt": "dark tense underground thriller", "file": "audio/music/full_score.mp3", "at": 0.0, "gain": 0.20, "fade_in": 0.3},
    "sfx": [
        {"id": "pounding", "shot": "s02", "at": 0.5, "dur": 4.0, "prompt": "violent heavy pounding and banging on an iron trapdoor from outside, frantic fists slamming metal", "gen_dur": 4.5, "file": "../ep01/audio/sfx/cut-whoosh.mp3", "gain": 0.22},
        {"id": "pounding2", "shot": "s03", "at": 0.2, "dur": 4.0, "file": "../ep01/audio/sfx/cut-whoosh.mp3", "gain": 0.22},
        {"id": "creak", "shot": "s06", "at": 0.2, "dur": 3.0, "file": "../ep01/audio/sfx/cut-whoosh.mp3", "gain": 0.16},
        {"id": "sting", "shot": "s11", "at": 0.0, "dur": 8.0, "file": "../ep01/audio/sfx/end-sting.mp3", "gain": 0.40},
        {"id": "tap", "shot": "s11", "at": 2.1, "dur": 0.6, "file": "../ep01/audio/sfx/cut-whoosh.mp3", "gain": 0.20},
    ],
    "stamp": {"shot": "s01", "start": 0.3, "end": "shot_end", "text": "วันที่ 1 · ทางเลือกที่ผิด"},
    "lessons": [
        {"shot": "s09", "start": 0.0, "end": "shot_end", "title": "บทเรียนจากความผิดพลาด (ถ้าเจอจริง)", "y": 280, "items": [
            {"text": "1. กฎ 24 ชม. มีไว้ปกป้องเรา แต่ถ้ามีผู้รอดชีวิตมาเคาะ" + NL + "สามารถรับเข้าได้ หากรู้วิธี Decontamination ทันที", "src": "Ready.gov · CDC", "at": {"shot": "s09", "at": 1.0}, "h": 220},
            {"text": "2. ถอดเสื้อผ้าชั้นนอกและล้างตัวน้ำสบู่เบา ๆ" + NL + "กำจัดฝุ่นพิษได้ถึง 90% โดยไม่ทำให้คนในห้องติดไปด้วย", "src": "Ready.gov · CDC · ปส.", "at": {"shot": "s09", "at": 7.5}, "h": 220},
            {"text": "3. การปล่อยคนเจ็บไว้ภายนอกโดยไม่ช่วยเหลือ" + NL + "นำไปสู่อาการรับรังสีเฉียบพลัน (ARS) ถึงแก่ชีวิต", "src": "Ready.gov · CDC", "at": {"shot": "s09", "at": 14.5}, "h": 220}],
            "source": "แนวทางของ CDC / Ready.gov กรณีฝุ่นกัมมันตรังสี · สำนักงานปรมาณูเพื่อสันติ (ปส.) 1296"},
        {"shot": "s11", "start": 0.0, "end": "shot_end", "title": "สรุปบทเรียน · ตอนที่ 3B", "y": 250, "items": [
            {"text": "1. ถอดเสื้อผ้าชั้นนอกใส่ถุงดำ ลดฝุ่นพิษได้ทันที 90%", "src": "Ready.gov · CDC", "at": 0.0, "h": 200},
            {"text": "2. ล้างตัวด้วยน้ำสบู่เบา ๆ ห้ามขัดถูรุนแรงเด็ดขาด", "src": "Ready.gov · CDC", "at": 0.0, "h": 200},
            {"text": "3. รู้วิธีชำระล้าง ช่วยชีวิตคนอื่นได้โดยเราไม่ตาย", "src": "Ready.gov · CDC · ปส.", "at": 0.0, "h": 200}],
            "source": "ในไทย: ปส. สายด่วน 1296 · ปภ. 1784 · แนวทางทั่วไป ทำตามประกาศของทางการเสมอ"}
    ],
    "follow": {"shot": "s11", "start": 1.2, "end": "shot_end", "tap": 0.9, "y": 1430},
    "choice": {"shot": "s10", "start": 0.3, "end": "shot_end", "question": "ต้องการมีชีวิตรอดใช่ไหม?", "a": "A. ย้อนกลับไปดูตอนที่ 3 (สายรอด)", "b": "B. ติดตามตอนต่อไป", "cta": "คลิกติดตามและย้อนกลับไปแก้มือที่ตอนที่ 3!"},
}

out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), 'timeline.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(tl, f, ensure_ascii=False, indent=1)
print('ep03_badend timeline built successfully')
