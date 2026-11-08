# Generator for ep02 timeline.json
import json
import os
import sys

NL = chr(92) + 'N'
C = "../characters/"
Q = '"'

tl = {
    "id": "day0-ep02", "series": "วันที่ 0", "episode": "ตอนที่ 2 · ใต้ดิน",
    "content_studio": {"project": "6Q9g7R_TFm", "content": "day0-ep02", "voice": "FfrJDiyJZK"},
    "look": {"sat": 0.92, "contrast": 1.06, "tint": [30, 45, 60], "tint_a": 0.05, "grain": 0.05},
    "shots": [
        {"id": "s01", "len": 4.0, "type": "push", "image": "images/eyes-ecu.png", "anchor": [0.5, 0.22], "zoom": [1.04, 1.18], "pulse": [255, 30, 30], "pulse_hz": 1.1, "pulse_alpha": 30,
         "vo": "audio/vo-01.mp3", "th": "ถ้าเสียงระเบิดเพิ่งสงบลง…" + NL + "แต่มีสิ่งอันตรายลอยอยู่ทั่วฟ้า…" + NL + "คุณจะกล้าออกไปไหม?", "en": "If the blast just went quiet," + NL + "but an invisible threat hangs in the sky…" + NL + "would you step outside?"},
        {"id": "s02", "len": 4.5, "type": "push", "image": "images/doorway.png", "anchor": [0.5, 0.5], "zoom": [1.12, 1.02], "transition": "whip", "end_shake": 6,
         "vo": "audio/vo-02.mp3", "th": "ประตูเหล็กกระแทกปิดสนิท…" + NL + "ผลโหวตพาเราเลี้ยวเข้ามาหลบ" + NL + "ในห้องใต้ดินร้านซ่อมวิทยุของครูเอก", "en": "The heavy iron door slammed shut." + NL + "The vote brought us into Kru Ek's shelter."},
        {"id": "s03", "len": 4.5, "type": "push", "image": "images/basement-radio.png", "zoom": [1.04, 1.12], "pan": 20,
         "vo": "audio/vo-03.mp3", "th": "กลิ่นสนิมเหล็กกับฝุ่นตลบอบอวล…" + NL + "ครูเอกรีบเอาเทปผ้า" + NL + "อุดรอยต่อช่องลมอย่างร้อนรน", "en": "Rust and dust filled the air." + NL + "Kru Ek hastily taped every seam in the vent."},
        {"id": "s04", "len": 4.5, "type": "layers", "bg": "images/basement-radio.png", "chars": [C + "kru-ek.png"], "scale": [0.9], "pos": [[0.5, 0.72]],
         "vo": "audio/vo-04-kru.mp3", "th": Q + "ไอ้หนู! รีบไปดึงปลั๊ก" + NL + "พัดลมระบายอากาศออกเดี๋ยวนี้!" + NL + "อย่าให้ลมข้างนอกรั่วเข้ามาเด็ดขาด!" + Q, "en": Q + "Kid! Pull the plug on that fan right now!" + NL + "Don't let outside air leak in!" + Q},
        {"id": "s05", "len": 4.0, "type": "push", "image": "images/hands.png", "zoom": [1.08, 1.02], "end_shake": 4,
         "vo": "audio/vo-05.mp3", "th": "พอพัดลมหยุดหมุน…" + NL + "ทั้งห้องก็เหลือเพียงเสียงหายใจหอบ" + NL + "ของเราสามคนกับหมาหนึ่งตัว", "en": "As the blades stopped," + NL + "nothing remained but ragged breathing."},
        {"id": "s06", "len": 4.5, "type": "push", "image": "images/brother-dino.png", "anchor": [0.5, 0.45], "zoom": [1.03, 1.12],
         "vo": "audio/vo-06-child.mp3", "th": Q + "พี่ครับ… แม่จะตามหาเราเจอไหมอ่ะ…" + Q, "en": Q + "Bro… will Mom be able to find us?" + Q},
        {"id": "s07", "len": 5.0, "type": "push", "image": "images/basement-radio.png", "anchor": [0.65, 0.45], "zoom": [1.15, 1.25], "pulse": [255, 50, 50], "pulse_hz": 2.5, "pulse_alpha": 25,
         "vo": "audio/vo-07.mp3", "th": "เข็มบนเครื่องวัดรังสีโบราณเริ่มกระดิก…" + NL + "เสียงคลิกดังถี่ขึ้นเรื่อย ๆ" + NL + "ยืนยันว่าฝุ่นมรณะเริ่มโปรยลงมาบนหลังคา", "en": "The dial needle flickered." + NL + "Faster clicks confirmed the lethal fallout had begun."},
        {"id": "s08", "len": 5.5, "type": "layers", "bg": "images/basement-radio.png", "chars": [C + "kru-ek.png"], "scale": [0.9], "pos": [[0.5, 0.72]],
         "vo": "audio/vo-08-kru.mp3", "th": Q + "ไม่ว่าข้างบนจะเงียบแค่ไหน…" + NL + "ห้ามใครโผล่หัวออกไปเด็ดขาด" + NL + "ยี่สิบสี่ชั่วโมงนี้คือชี้เป็นชี้ตาย" + Q, "en": Q + "No matter how quiet it gets," + NL + "don't step outside. 24 hours decide life or death." + Q},
        # s09: Lesson Card "ถ้าเจอจริง" - clean typography, no bottom subtitle overlap
        {"id": "s09", "len": 24.9, "type": "push", "image": "images/basement-radio.png", "zoom": [1.02, 1.08], "dim": 0.35},
        {"id": "s10", "len": 7.5, "type": "push", "image": "images/window-street.png", "zoom": [1.08, 1.02], "dim": 0.25,
         "vo": "audio/vo-10.mp3", "th": "หลักการนี้ใช้ได้จริงในชีวิตประจำวัน…" + NL + "ทั้งตอนเพลิงไหม้ ควันสารเคมี" + NL + "หรือวันฝุ่น PM2.5 วิกฤต", "en": "This applies to real life too:" + NL + "fires, chemical spills, or severe PM2.5 haze."},
        {"id": "s11", "len": 4.5, "type": "push", "image": "images/doorway.png", "zoom": [1.05, 1.15], "end_shake": 8, "pulse": [255, 30, 30], "pulse_hz": 2.0, "pulse_alpha": 35,
         "vo": "audio/vo-11.mp3", "th": "ความเงียบโรยตัวอยู่ได้ไม่นาน…" + NL + "จู่ ๆ ประตูเหล็กด้านบน" + NL + "ก็ถูกกระแทกอย่างแรงจนฝุ่นร่วงกราว", "en": "Suddenly, violent pounding" + NL + "shook the iron hatch above."},
        # s12a: Narrator speaks while Khao Tu barks/growls
        {"id": "s12a", "len": 4.8, "type": "layers", "bg": "images/basement-radio.png", "chars": [C + "dog.png"], "scale": [0.65], "pos": [[0.5, 0.78]],
         "vo": "audio/vo-12.mp3", "th": "ข้าวตูลุกขึ้นขู่ฟ่อ…" + NL + "พร้อมเสียงคนแหบแห้งตะโกนลงมา:", "en": "Khao Tu growled as a voice cried:"},
        # s12b: Cut to doorway with stranger shouting - completely sequential, ZERO voice overlap!
        {"id": "s12b", "len": 4.6, "type": "push", "image": "images/doorway.png", "anchor": [0.5, 0.4], "zoom": [1.08, 1.18], "end_shake": 6, "transition": "whip",
         "vo": "audio/vo-12-stranger.mp3", "th": Q + "ช่วยด้วย! เปิดให้ผมที!" + NL + "ข้างนอกไม่ไหวแล้ว!" + Q, "en": Q + "Help! Please open up!" + NL + "I can't survive out here!" + Q},
        # s13: Reaction shot - Ton Kla and Kru Ek
        {"id": "s13", "len": 6.0, "type": "reveal", "bg": "images/basement-radio.png",
         "chars": [C + "boy.png", C + "brother.png", C + "kru-ek.png"],
         "blink": {"0": C + "boy-blink.png", "1": C + "brother-blink.png"},
         "vo": "audio/vo-13.mp3", "th": "ต้นกล้ามองหน้าคุณด้วยความสงสาร…" + NL + "แต่ครูเอกส่ายหน้าเด็ดขาด" + NL + "เพราะการเปิดประตูตอนนี้ จะนำฝุ่นรังสีข้างนอก" + NL + "ทะลักลงมาฆ่าทุกคน", "en": "Ton Kla looked with pity, but Kru Ek shook his head." + NL + "Opening now lets fallout kill everyone inside."},
        # s14: Choice Card - extended to 14.0s so viewers have 5+ seconds to read options and comment
        {"id": "s14", "len": 14.0, "type": "push", "image": "images/doorway.png", "zoom": [1.12, 1.02], "dim": 0.4},
        # s15: Summary Card & Follow - extended to 8.5s so viewers have ample time to read summary and tap follow
        {"id": "s15", "len": 8.5, "type": "push", "image": "images/basement-radio.png", "zoom": [1.04, 1.04], "dim": 0.25},
    ],
    "vo": [
        {"file": "audio/vo-09.mp3", "shot": "s09", "at": 0.2},
        {"file": "audio/vo-14.mp3", "shot": "s14", "at": 0.2},
        {"file": "audio/vo-15.mp3", "shot": "s15", "at": 0.2},
    ],
    "cut_sfx": {"prompt": "air whoosh sound effect, quick swoosh of wind passing by, no drums", "gen_dur": 1.2, "file": "../ep01/audio/sfx/cut-whoosh.mp3", "gain": 0.08, "lead": 0.2},
    "vo_gain": 1.45,
    "duck": {"ratio": 4.5, "threshold": 0.08},
    "music": {"prompt": "dark tense underground thriller", "file": "audio/music/full_score.mp3", "at": 0.0, "gain": 0.20, "fade_in": 0.3},
    "sfx": [
        {"id": "doorslam", "shot": "s02", "at": 0.2, "dur": 3.0, "prompt": "heavy steel cellar door slamming shut loudly, massive metallic clang, echoing reverb", "gen_dur": 3.5, "gain": 0.22},
        {"id": "tape", "shot": "s03", "at": 0.5, "dur": 3.5, "prompt": "duct tape peeling off roll loudly and sticking firmly to metal surface", "gen_dur": 3.5, "gain": 0.12},
        {"id": "fanstop", "shot": "s05", "at": 0.1, "dur": 3.5, "prompt": "electric exhaust fan slowing down and grinding to a complete halt, hum fading", "gen_dur": 4.0, "gain": 0.14},
        {"id": "geiger", "shot": "s07", "at": 0.0, "dur": "to_shot_end", "prompt": "geiger counter rapidly clicking, repeating erratic static clicks, radiation detector sound", "gen_dur": 6.0, "gain": 0.14},
        {"id": "pounding", "shot": "s11", "at": 0.3, "dur": 4.0, "prompt": "violent heavy pounding and banging on an iron trapdoor from outside, frantic fists slamming metal", "gen_dur": 4.5, "gain": 0.25},
        {"id": "pounding2", "shot": "s12b", "at": 0.1, "dur": 4.0, "file": "../ep01/audio/sfx/cut-whoosh.mp3", "gain": 0.08},
        {"id": "sting", "shot": "s15", "at": 0.0, "dur": 8.0, "prompt": "deep cinematic end sting, low boom with long dark reverb tail", "gen_dur": 5, "file": "../ep01/audio/sfx/end-sting.mp3", "gain": 0.40},
        {"id": "tap", "shot": "s15", "at": 2.1, "dur": 0.6, "prompt": "soft user interface button tap", "gen_dur": 0.6, "file": "../ep01/audio/sfx/cut-whoosh.mp3", "gain": 0.20},
    ],
    "stamp": {"shot": "s02", "start": 0.3, "end": "shot_end", "text": "วันที่ 0 · 08:15"},
    "lessons": [
        {"shot": "s09", "start": 0.0, "end": "shot_end", "title": "ถ้าเจอจริง", "y": 280, "items": [
            {"text": "1. ปิดประตู หน้าต่าง ดับพัดลมและแอร์ทั้งหมด" + NL + "ไม่ให้ดึงอากาศภายนอกเข้ามา", "src": "Ready.gov · CDC", "at": {"shot": "s09", "at": 1.0}, "h": 220},
            {"text": "2. หลบในจุดที่ลึกที่สุด เช่น ห้องใต้ดิน" + NL + "หรือใจกลางอาคารที่มีผนังหนาหลายชั้น", "src": "Ready.gov · CDC", "at": {"shot": "s09", "at": 4.5}, "h": 220},
            {"text": "3. กบดานอย่างน้อย 24 ชม. อย่าเพิ่งออกไปตามหาใคร" + NL + "ติดตามประกาศ ปส. สายด่วน 1296", "src": "Ready.gov · CDC · สำนักงานปรมาณูเพื่อสันติ (ปส.)", "at": {"shot": "s09", "at": 8.0}, "h": 220}],
            "source": "แนวทางของสหรัฐฯ กรณีระเบิดนิวเคลียร์ · ในไทยให้ทำตามประกาศของทางการเสมอ"},
        {"shot": "s15", "start": 0.0, "end": "shot_end", "title": "สรุปบทเรียน · ตอนที่ 2", "y": 250, "items": [
            {"text": "1. ซีลห้องทันที: ปิดช่องลม ดับพัดลมและแอร์", "src": "Ready.gov · CDC", "at": 0.0, "h": 200},
            {"text": "2. หลบจุดลึกที่สุด: ห้องใต้ดินหรือแกนกลางอาคาร", "src": "Ready.gov · CDC", "at": 0.0, "h": 200},
            {"text": "3. อยู่ข้างในอย่างน้อย 24 ชม. ห้ามเปิดประตูเด็ดขาด", "src": "Ready.gov · CDC · ปส.", "at": 0.0, "h": 200}],
            "source": "ในไทย: ปส. สายด่วน 1296 · ปภ. 1784 · แนวทางทั่วไป ทำตามประกาศของทางการเสมอ"}
    ],
    "follow": {"shot": "s15", "start": 1.2, "end": "shot_end", "tap": 0.9, "y": 1430},
    "choice": {"shot": "s14", "start": 0.3, "end": "shot_end", "question": "ถ้าเป็นคุณ… จะตัดสินใจอย่างไร?", "a": "แง้มประตูรับคนบาดเจ็บ", "b": "ปิดตาย 24 ชม. ห้ามเปิดเด็ดขาด", "cta": "คอมเมนต์ A หรือ B · ตอนหน้าดำเนินตามเสียงส่วนใหญ่"},
}

out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), 'timeline.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(tl, f, ensure_ascii=False, indent=1)
print('ep02 timeline built successfully')
