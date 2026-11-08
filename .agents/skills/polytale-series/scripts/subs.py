"""PolyTale overlay: bilingual subtitles, optional phone alert card, episode title card (ASS).

Usage: python subs.py <episode_dir> [out.ass]       # default <episode_dir>/render/overlay.ass
Reads timeline.json: "subs" (required), "alert" and "title" (optional). Thai uses \\N for a
line break. Rendered later by final.py with libass, Kanit fonts and complex shaping.
"""
import json
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import tl as tl_mod  # noqa: E402
import os
import sys


def ts(s):
    return f"{int(s // 3600)}:{int(s % 3600 // 60):02d}:{s % 60:05.2f}"


HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TH,Kanit,64,&H0000E1FF,&H000000FF,&H00101010,&H96000000,-1,0,0,0,100,100,0,0,1,6,3,2,150,150,480,222
Style: EN,Kanit,38,&H00FFFFFF,&H000000FF,&H00000000,&HB4000000,0,0,0,0,100,100,0,0,3,10,0,2,150,150,410,1
Style: ALT,Kanit,54,&H00FFFFFF,&H000000FF,&H00000000,&HD0101018,-1,0,0,0,100,100,0,0,3,26,0,8,80,80,150,222
Style: CLOCK,Kanit,58,&H003C3CFF,&H000000FF,&H00000000,&HB4000000,-1,0,0,0,100,100,2,0,3,12,0,9,0,70,250,1
Style: STAMP,Kanit,40,&H00FFFFFF,&H000000FF,&H00000000,&HB4000000,-1,0,0,0,100,100,0,0,3,12,0,7,70,0,250,222
Style: DIM,Kanit,20,&H00000000,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: Q,Kanit,60,&H00FFFFFF,&H000000FF,&H00101010,&H96000000,-1,0,0,0,100,100,0,0,1,6,3,5,120,120,0,222
Style: CH,Kanit,50,&H00FFFFFF,&H000000FF,&H001E1ED6,&HB4000000,-1,0,0,0,100,100,0,0,3,24,0,5,0,0,0,222
Style: LHEAD,Kanit,62,&H00101010,&H000000FF,&H0000D7FF,&H0000D7FF,-1,0,0,0,100,100,0,0,3,18,0,7,110,110,0,222
Style: LITEM,Kanit,46,&H00FFFFFF,&H000000FF,&H00101010,&H96000000,-1,0,0,0,100,100,0,0,1,4,2,7,110,150,0,222
Style: LSRC,Kanit,28,&H00B4B4B4,&H000000FF,&H00101010,&H00000000,0,0,0,0,100,100,0,0,1,2,0,7,110,150,0,222
Style: FOLLOW,Kanit,54,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,5,0,0,0,222
Style: BADGE,Kanit,70,&H00FFFFFF,&H000000FF,&H001E1ED6,&H001E1ED6,-1,0,0,0,100,100,0,0,3,18,0,5,60,60,0,222
Style: TITLE,Kanit,150,&H00FFFFFF,&H000000FF,&H00101010,&H96000000,-1,0,0,0,100,100,0,0,1,8,4,5,60,60,0,222
Style: SMALL,Kanit,34,&H00C8C8C8,&H000000FF,&H00101010,&H00000000,0,0,0,0,100,100,0,0,1,3,0,5,60,60,0,222

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


DIM = r"{\an7\pos(0,0)\1c&H000000&\1a&H70&\fad(300,200)\p1}m 0 0 l 1080 0 1080 1920 0 1920{\p0}"
FADE = r"{\fad(300,300)}"


def at7(y, fad):
    return r"{\an7\pos(110,%d)\fad(%s)}" % (y, fad)


def pop(x, y, fad="200,200"):
    return (r"{\pos(%d,%d)\fad(%s)\t(0,200,\fscx110\fscy110)\t(200,400,\fscx100\fscy100)}" % (x, y, fad))


_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))
_FONT_CANDIDATES = [
    _os.path.join(_ROOT, "assets", "fonts"),
    _os.path.join(_ROOT, "content-studio", "assets", "fonts"),
    _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", "assets", "fonts"),
]
FONTS = next((d for d in _FONT_CANDIDATES if _os.path.exists(d)), _FONT_CANDIDATES[0])
NL = chr(92) + "N"
FAD = r"{\fad(120,120)}"
SRC_TAG = r"{\fs28\b0\c&HC8C8C8&\bord2\shad0}"
# Subtitle geometry (PlayRes 1080x1920). Measured with the same font libass uses.
TH_SIZE, EN_SIZE = 64, 38
TH_MAX_W, EN_MAX_W = 760, 760          # text width inside x 150..930 (right-side buttons start at 940)
EN_MARGIN_V = 410                     # bottom of the English block at y 1510 (caption zone starts at 1540)
EN_LINE_H = 50                        # one English line incl. leading
EN_BLOCK_PAD = 20                     # box padding (BorderStyle 3, outline 10, top + bottom)
GAP = 14                              # clear space between the English box and the Thai outline/shadow


class _Measured:
    """PIL font scaled the way libass sizes fonts (ASS size = ascent + descent, not the em)."""

    def __init__(self, size):
        from PIL import ImageFont
        self.f = ImageFont.truetype(_os.path.join(FONTS, "Kanit-Bold.ttf"), size)
        a, d = self.f.getmetrics()
        self.k = size / float(a + d)

    def getlength(self, text):
        return self.f.getlength(text) * self.k


def _font(size):
    return _Measured(size)


TH_FONT, EN_FONT = None, None


def wrap(text, font, max_w):
    # Split text into lines no wider than max_w
    global TH_FONT, EN_FONT
    out = []
    for para in text.split(NL):
        words = para.split(" ")
        line = ""
        for w in words:
            if not w:
                continue
            if font.getlength(w) > max_w:
                if line:
                    out.append(line)
                    line = ""
                chunk = ""
                for ch in w:
                    if font.getlength(chunk + ch) > max_w:
                        if chunk:
                            out.append(chunk)
                        chunk = ch
                    else:
                        chunk += ch
                if chunk:
                    line = chunk
                continue
            cand = (line + " " + w).strip() if line else w
            if line and font.getlength(cand) > max_w:
                out.append(line)
                line = w
            else:
                line = cand
        if line:
            out.append(line)
    return [l for l in out if l]


def pill(w, h):
    """ASS drawing of a rounded pill w x h, origin top-left."""
    r = h / 2.0
    k = 0.5523 * r
    return (f"m {r:.0f} 0 l {w - r:.0f} 0 "
            f"b {w - r + k:.0f} 0 {w:.0f} {r - k:.0f} {w:.0f} {r:.0f} "
            f"b {w:.0f} {r + k:.0f} {w - r + k:.0f} {h:.0f} {w - r:.0f} {h:.0f} "
            f"l {r:.0f} {h:.0f} "
            f"b {r - k:.0f} {h:.0f} 0 {r + k:.0f} 0 {r:.0f} "
            f"b 0 {r - k:.0f} {r - k:.0f} 0 {r:.0f} 0")


def circle(d):
    return pill(d, d)


def follow_events(fo, ts):
    """Animated follow button (no channel name): pops in, gets tapped, turns to 'followed'."""
    a, b = fo["start"], fo["end"]
    y = fo.get("y", 1240)
    tap = a + fo.get("tap", 1.3)
    w, h = fo.get("w", 440), fo.get("h", 112)
    BS = "BACKSLASH"
    pop = "{BSt(0,180,BSfscx115BSfscy115)BSt(180,330,BSfscx100BSfscy100)}"
    ev = []
    ev.append(f"Dialogue: 5,{ts(a)},{ts(tap)},DIM,,0,0,0,,{{BSan5BSpos(540,{y})BS1c&H2B2BE6&BSbord0BSshad5BS4c&H000000&BSfad(150,0)BSp1}}" + pop.replace("{", "{") + f"{pill(w, h)}")
    ev.append(f"Dialogue: 6,{ts(a)},{ts(tap)},FOLLOW,,0,0,0,,{{BSan5BSpos(540,{y})BSfad(150,0)}}" + pop + fo.get("label", "+ ติดตาม"))
    ev.append(f"Dialogue: 7,{ts(tap - 0.05)},{ts(tap + 0.45)},DIM,,0,0,0,,{{BSan5BSpos(540,{y})BS1c&HFFFFFF&BS1a&H40&BSbord0BSshad0BSt(BSfscx260BSfscy260BS1a&HFF&)BSp1}}{circle(70)}")
    ev.append(f"Dialogue: 5,{ts(tap)},{ts(b)},DIM,,0,0,0,,{{BSan5BSpos(540,{y})BS1c&H4A4A4A&BSbord0BSshad5BSfad(0,200)BSp1}}{pill(w, h)}")
    ev.append(f"Dialogue: 6,{ts(tap)},{ts(b)},FOLLOW,,0,0,0,,{{BSan5BSpos(540,{y})BSfad(0,200)}}" + fo.get("done", "ติดตามแล้ว"))
    return [e.replace("BS", "\\") for e in ev]


def main():
    global TH_FONT, EN_FONT
    TH_FONT, EN_FONT = _font(TH_SIZE), _font(EN_SIZE)
    ep = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ep, "render", "overlay.ass")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    tl = tl_mod.load(ep)
    ev = []
    for s in tl["subs"]:
        a, b = s["start"], s["end"]
        th_lines = wrap(s["th"], TH_FONT, TH_MAX_W)
        en_lines = wrap(s.get("en", ""), EN_FONT, EN_MAX_W) if s.get("en") else []
        # English block sits at the bottom; the Thai block is raised by the English block's height
        th_margin = EN_MARGIN_V + (len(en_lines) * EN_LINE_H + EN_BLOCK_PAD + GAP if en_lines else 0)
        ev.append(f"Dialogue: 2,{ts(a)},{ts(b)},TH,,0,0,{th_margin},,{FAD}{NL.join(th_lines)}")
        if en_lines:
            ev.append(f"Dialogue: 1,{ts(a)},{ts(b)},EN,,0,0,{EN_MARGIN_V},,{FAD}{NL.join(en_lines)}")
    al = tl.get("alert")
    if al:
        text = (r"{\an8\fad(150,200)\move(540,-200,540,250,0,280)}{\c&H4848FF&}⚠  " + al["title"]
                + r"\N{\c&HFFFFFF&\fs40\b0}" + al["body"])
        ev.append(f"Dialogue: 3,{ts(al['start'])},{ts(al['end'])},ALT,,0,0,0,,{text}")
    ti = tl.get("title")
    if ti:
        t0, t1 = ti["start"], ti["end"]
        ev.append(f"Dialogue: 3,{ts(t0)},{ts(t1)},DIM,,0,0,0,,{DIM}")
        ev.append(f"Dialogue: 4,{ts(t0)},{ts(t1)},BADGE,,0,0,0,,{{\\pos(540,800)\\fad(200,0)\\t(0,180,\\fscx112\\fscy112)\\t(180,320,\\fscx100\\fscy100)}}{ti['badge']}")
        ev.append(f"Dialogue: 4,{ts(t0 + 0.25)},{ts(t1)},TITLE,,0,0,0,,{{\\pos(540,960)\\fad(250,0)}}{ti['title']}")
        if ti.get("note", "(เรื่องแต่ง)"):
            ev.append(f"Dialogue: 4,{ts(t0 + 0.5)},{ts(t1)},SMALL,,0,0,0,,{{\\pos(540,1090)\\fad(250,0)}}{ti.get('note', '(เรื่องแต่ง)')}")
    for c in tl.get("countdown", []):
        last = None
        n = max(1, int((c["t1"] - c["t0"]) * 30))
        for i in range(n + 1):
            tt = c["t0"] + (c["t1"] - c["t0"]) * i / n
            v = int(round(c["v0"] + (c["v1"] - c["v0"]) * i / n))
            if last is not None and v == last[1]:
                continue
            if last is not None:
                ev.append(f"Dialogue: 3,{ts(last[0])},{ts(tt)},CLOCK,,0,0,0,,⏱ {last[1] // 60:02d}:{last[1] % 60:02d}")
            last = (tt, v)
        hold = c.get("hold", 0.0)
        ev.append(f"Dialogue: 3,{ts(last[0])},{ts(c['t1'] + hold)},CLOCK,,0,0,0,,⏱ {last[1] // 60:02d}:{last[1] % 60:02d}")
    for cd in tl.get("cards", []):
        ev.append(f"Dialogue: 4,{ts(cd['start'])},{ts(cd['end'])},Q,,0,0,0,,{pop(540, cd.get('y', 760), '200,200')}{cd['text']}")
    for ls in tl.get("lessons", []):
        a, b = ls["start"], ls["end"]
        ev.append(f"Dialogue: 3,{ts(a)},{ts(b)},DIM,,0,0,0,,{DIM}")
        ev.append(f"Dialogue: 4,{ts(a)},{ts(b)},LHEAD,,0,0,0,,{at7(ls.get('y', 400), '200,200')}{ls.get('title', 'ถ้าเจอจริง')}")
        y = ls.get("y", 400) + 140
        for it in ls["items"]:
            t0 = a + it.get("at", 0.0)
            txt = it["text"]
            if it.get("src"):  # per-item credit, small grey line under the step
                txt += NL + SRC_TAG + "ที่มา: " + it["src"]
            ev.append(f"Dialogue: 4,{ts(t0)},{ts(b)},LITEM,,0,0,0,,{at7(y, '250,200')}{txt}")
            y += it.get("h", 150)
        if ls.get("source"):
            ev.append(f"Dialogue: 4,{ts(a + 0.5)},{ts(b)},LSRC,,0,0,0,,{at7(y + 10, '250,200')}{ls['source']}")
    if tl.get("follow"):
        ev += follow_events(tl["follow"], ts)
    st = tl.get("stamp")
    if st:
        ev.append(f"Dialogue: 3,{ts(st['start'])},{ts(st['end'])},STAMP,,0,0,0,,{FADE}{st['text']}")
    ch = tl.get("choice")
    if ch:
        a, b = ch["start"], ch["end"]
        ev.append(f"Dialogue: 3,{ts(a)},{ts(b)},DIM,,0,0,0,,{DIM}")
        ev.append(f"Dialogue: 4,{ts(a)},{ts(b)},Q,,0,0,0,,{pop(540, 640, '300,200')}{ch['question']}")
        ev.append(f"Dialogue: 4,{ts(a + 0.6)},{ts(b)},CH,,0,0,0,,{pop(540, 860)}A  {ch['a']}")
        ev.append(f"Dialogue: 4,{ts(a + 1.2)},{ts(b)},CH,,0,0,0,,{pop(540, 1020)}B  {ch['b']}")
        if ch.get("cta"):
            ev.append(f"Dialogue: 4,{ts(a + 1.8)},{ts(b)},SMALL,,0,0,0,,{pop(540, 1150)}{ch['cta']}")
    with open(out, "w", encoding="utf-8-sig") as fh:
        fh.write(HEAD + "\n".join(ev) + "\n")
    print("wrote", out, len(ev), "events")


if __name__ == "__main__":
    main()
