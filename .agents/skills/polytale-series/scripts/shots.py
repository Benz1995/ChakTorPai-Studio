"""PolyTale shot compositor: timeline.json -> silent 1080x1920 30 fps MP4.

Usage (from the repo root or anywhere):
    python shots.py <episode_dir> [out.mp4]          # default out: <episode_dir>/render/shots.mp4
    ONLY=<shot id> python shots.py <episode_dir> <out.mp4>   # render one shot for review

All asset paths in timeline.json are relative to <episode_dir>.
Shot types (see references/timeline.md for every field):
    push   one full-frame image: slow push-in, optional pan, colour pulse, phone buzz, end shake
    run    plate + 1-4 transparent pose layers cycling (run/walk), bob, speed lines, handheld shake
    reveal background + transparent character layers; optional flash event with
           blast cloud rising on the skyline, regrade, shake and falling ash
    layers background + character layers + optional cloud; calm parallax, breathing, ash
"""
import json
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import tl as tl_mod  # noqa: E402
import math
import os
import random
import subprocess
import sys

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps

W, H, FPS = 1080, 1920, 30
rng = random.Random(11)


# ---------------------------------------------------------------- helpers

def load(path, fit="cover"):
    im = Image.open(path).convert("RGBA")
    if fit == "stretch":
        return im.resize((W, H), Image.LANCZOS)
    return ImageOps.fit(im, (W, H), Image.LANCZOS, centering=(0.5, 0.5))


def place(canvas, img, scale, anchor, dx=0.0, dy=0.0, sy=1.0):
    nw, nh = max(1, round(img.width * scale)), max(1, round(img.height * scale * sy))
    im = img.resize((nw, nh), Image.BILINEAR) if (nw, nh) != img.size else img
    ax, ay = anchor
    ox = round(ax - ax * scale + dx)
    oy = round(ay - ay * scale * sy + dy)
    canvas.alpha_composite(im, dest=(max(ox, 0), max(oy, 0)),
                           source=(max(-ox, 0), max(-oy, 0)))


def ease(x):
    x = min(max(x, 0.0), 1.0)
    return 0.5 - 0.5 * math.cos(math.pi * x)


def shake(t, amp, freq=18.0, seed=0):
    return (amp * (math.sin(t * freq + seed) * 0.6 + math.sin(t * freq * 1.7 + seed * 3) * 0.4),
            amp * (math.cos(t * freq * 1.3 + seed) * 0.6 + math.sin(t * freq * 2.1 + seed) * 0.4))


def alpha_bbox(img):
    return img.getchannel("A").point(lambda a: 255 if a > 128 else 0).getbbox()


def grade(img, sat=1.0, bright=1.0, tint=None, tint_a=0.0):
    rgb = img.convert("RGB")
    if sat != 1:
        rgb = ImageEnhance.Color(rgb).enhance(sat)
    if bright != 1:
        rgb = ImageEnhance.Brightness(rgb).enhance(bright)
    if tint and tint_a > 0:
        rgb = Image.blend(rgb, Image.new("RGB", rgb.size, tuple(tint)), tint_a)
    out = rgb.convert("RGBA")
    out.putalpha(img.getchannel("A"))
    return out


def solid(color, a):
    return Image.new("RGBA", (W, H), (*color, int(max(0, min(255, a)))))


def vignette(strength=0.7):
    v = Image.new("L", (W, H), 0)
    ImageDraw.Draw(v).ellipse((-300, -240, W + 300, H + 240), fill=255)
    v = v.filter(ImageFilter.GaussianBlur(200))
    d = Image.new("RGBA", (W, H), (4, 6, 10, 255))
    d.putalpha(v.point(lambda x: int((255 - x) * strength)))
    return d


def shadows(boxes):
    sh = Image.new("RGBA", (W, H))
    d = ImageDraw.Draw(sh)
    for (x0, y0, x1, y1) in boxes:
        cx, w = (x0 + x1) / 2, (x1 - x0) * 0.55
        d.ellipse((cx - w / 2, y1 - 14, cx + w / 2, y1 + 14), fill=(0, 0, 0, 150))
    return sh.filter(ImageFilter.GaussianBlur(10))


class Ash:
    def __init__(self, n=170):
        self.p = [dict(x=rng.uniform(0, W), y=rng.uniform(0, H), v=rng.uniform(40, 120),
                       dr=rng.uniform(-25, 25), ph=rng.uniform(0, 6.28),
                       r=rng.uniform(1.5, 3.5) if i < n - 30 else rng.uniform(5, 9),
                       front=i >= n - 30) for i in range(n)]

    def draw(self, frame, t, front, alpha=1.0):
        layer = Image.new("RGBA", (W, H))
        d = ImageDraw.Draw(layer)
        for a in self.p:
            if a["front"] != front:
                continue
            sp = 2.2 if front else 1.0
            y = (a["y"] + a["v"] * sp * t) % (H + 60) - 30
            x = a["x"] + a["dr"] * sp * t + 14 * math.sin(a["ph"] + t * 1.2)
            c = (215, 205, 200, int((120 if front else 150) * alpha))
            d.ellipse((x - a["r"], y - a["r"], x + a["r"], y + a["r"]), fill=c)
        if front:
            layer = layer.filter(ImageFilter.GaussianBlur(3))
        frame.alpha_composite(layer)


ASH = Ash()
VIG = vignette()


def speed_lines(t, strength):
    layer = Image.new("RGBA", (W, H))
    d = ImageDraw.Draw(layer)
    r2 = random.Random(int(t * FPS))
    cx, cy = W / 2, H * 0.55
    for _ in range(36):
        ang = r2.uniform(0, 2 * math.pi)
        r0 = r2.uniform(620, 900)
        r1 = r0 + r2.uniform(200, 500)
        d.line((cx + r0 * math.cos(ang), cy + r0 * math.sin(ang),
                cx + r1 * math.cos(ang), cy + r1 * math.sin(ang)),
               fill=(255, 255, 255, int(70 * strength)), width=r2.randint(2, 5))
    return layer


# ---------------------------------------------------------------- shot types

class Push:
    def __init__(self, s, ep):
        self.img = load(os.path.join(ep, s["image"]), s.get("fit", "cover"))
        self.s = s
        self.fg = Foreground(s, ep)

    def frame(self, t, dur):
        s = self.s
        f = Image.new("RGBA", (W, H), (0, 0, 0, 255))
        p = ease(t / dur)
        z0, z1 = s.get("zoom", [1.04, 1.12])
        dx = dy = 0.0
        if s.get("buzz"):
            amp = 3.0 * (1 if math.sin(2 * math.pi * 1.1 * t) > 0 else 0)
            dx, dy = shake(t, amp, 70)
        es = s.get("end_shake", 0)
        if es and t > dur - 1.2:
            ex, ey = shake(t, es * (t - (dur - 1.2)) / 1.2, 25, 2)
            dx, dy = dx + ex, dy + ey
        anchor = (W * s.get("anchor", [0.5, 0.5])[0], H * s.get("anchor", [0.5, 0.5])[1])
        img = self.img
        dof = s.get("dof")
        if dof:
            r = dof[0] + (dof[1] - dof[0]) * ease(t / max(dur * s.get("dof_time", 0.6), 0.01))
            if r > 0.3:
                img = img.filter(ImageFilter.GaussianBlur(r))
        place(f, img, z0 + (z1 - z0) * p, anchor, dx + s.get("pan", 0) * p, dy)
        if s.get("dim"):
            f.alpha_composite(solid((0, 0, 0), 255 * s["dim"]))
        if s.get("pulse"):
            hz = s.get("pulse_hz", 2.0)
            f.alpha_composite(solid(s["pulse"], s.get("pulse_alpha", 35) * max(0.0, math.sin(2 * math.pi * hz * t))))
        if s.get("ash"):
            ASH.draw(f, t, False)
            ASH.draw(f, t, True)
        self.fg.draw(f, t, dur, dx, dy)
        return f


class Foreground:
    """Optional near layer (debris, bars, leaves) that moves more than everything else."""

    def __init__(self, s, ep):
        self.img = load(os.path.join(ep, s["fg"]), "cover") if s.get("fg") else None
        self.drift = s.get("fg_drift", 60)
        self.blur = s.get("fg_blur", 4)
        if self.img is not None and self.blur:
            self.img = self.img.filter(ImageFilter.GaussianBlur(self.blur))

    def draw(self, f, t, dur, dx=0.0, dy=0.0):
        if self.img is None:
            return
        p = ease(t / dur)
        place(f, self.img, 1.08 + 0.10 * p, (W / 2, H), dx * 1.8 - self.drift * p, dy * 1.8)


class Run:
    def __init__(self, s, ep):
        self.plate = load(os.path.join(ep, s["plate"]), s.get("fit", "cover"))
        self.poses = [load(os.path.join(ep, p), s.get("fit", "cover")) for p in s["poses"]]
        self.box = alpha_bbox(self.poses[0])
        self.s = s
        a = ((self.box[0] + self.box[2]) / 2, self.box[3])
        sh = Image.new("RGBA", (W, H))
        ImageDraw.Draw(sh).ellipse((a[0] - 260, a[1] - 18, a[0] + 260, a[1] + 22), fill=(0, 0, 0, 130))
        self.shadow = sh.filter(ImageFilter.GaussianBlur(14))
        self.anchor = a
        self.fg = Foreground(s, ep)

    def frame(self, t, dur):
        s = self.s
        f = Image.new("RGBA", (W, H), (0, 0, 0, 255))
        p = t / dur
        dx, dy = shake(t, s.get("shake", 7), 20, 5)
        place(f, self.plate, 1.10 - 0.04 * p, (W / 2, H * 0.45), dx * 0.6, dy * 0.6)
        step = 1 / s.get("steps_per_sec", 3.4)
        n = len(self.poses)
        cycle = (t / step) % n
        pose = self.poses[int(cycle)]
        phase = cycle % 1
        bob = -abs(math.sin(math.pi * phase)) * s.get("bob", 22)
        sc0, sc1 = s.get("scale", [0.84, 0.94])
        sc = sc0 + (sc1 - sc0) * ease(p)
        place(f, self.shadow, sc, self.anchor, dx, dy)
        place(f, pose, sc, self.anchor, dx, dy + bob, sy=1.0 + 0.012 * math.sin(2 * math.pi * phase))
        if s.get("speed_lines", 0.8):
            f.alpha_composite(speed_lines(t, s.get("speed_lines", 0.8)))
        self.fg.draw(f, t, dur, dx, dy)
        return f


class Reveal:
    """Background + characters; optional flash event (blast cloud, regrade, shake, ash)."""

    def __init__(self, s, ep):
        self.s = s
        bg = load(os.path.join(ep, s["bg"]), s.get("bg_fit", "cover"))
        self.chars = [load(os.path.join(ep, c), s.get("char_fit", "stretch")) for c in s["chars"]]
        self.boxes = [alpha_bbox(c) for c in self.chars]
        self.shadow = shadows(self.boxes)
        self.flash_at = s.get("flash_at")
        self.cloud = None
        if s.get("cloud"):
            raw = Image.open(os.path.join(ep, s["cloud"])).convert("RGBA")
            raw = raw.crop(alpha_bbox(raw) or raw.getbbox())
            cw = s.get("cloud_width", 600)
            raw = raw.resize((cw, round(raw.height * cw / raw.width)), Image.LANCZOS)
            bx, by = s.get("cloud_base", [700, 560])
            self.cloud = Image.new("RGBA", (W, H))
            self.cloud.alpha_composite(raw, (bx - cw // 2, by - raw.height))
            self.cloud_anchor = (bx, by)
        pre = s.get("pre_grade", {"sat": 0.9, "bright": 0.95})
        post = s.get("post_grade", {"sat": 0.7, "bright": 0.55, "tint": [150, 45, 15], "tint_a": 0.38})
        self.bg_pre = grade(bg, **pre)
        self.bg_post = grade(bg, **post) if self.flash_at is not None else self.bg_pre
        cpre = s.get("char_pre_grade", {"bright": 1.25, "tint": [255, 230, 200], "tint_a": 0.08})
        self.chars_pre = [grade(c, **cpre) for c in self.chars]
        self.tremble = s.get("tremble", [])
        fit = s.get("char_fit", "stretch")
        self.blink = {int(k): load(os.path.join(ep, v), fit) for k, v in s.get("blink", {}).items()}
        self.swaps = []
        for sw in s.get("swaps", []):
            imgs = [load(os.path.join(ep, c), fit) for c in sw["chars"]]
            self.swaps.append((sw["at"], imgs, [alpha_bbox(c) for c in imgs]))
        self.fg = Foreground(s, ep)

    def frame(self, t, dur):
        s = self.s
        f = Image.new("RGBA", (W, H), (0, 0, 0, 255))
        after = t - self.flash_at if self.flash_at is not None else -1e9
        p = ease(t / dur)
        amp = 26 * math.exp(-after * 1.6) if after > 0 else 0.0
        dx, dy = shake(t, amp, 30, 7)
        s_bg = 1.0 + s.get("bg_push", 0.04) * p
        anc = (W / 2, H * 0.55)
        if after < 0:
            place(f, self.bg_pre, s_bg, anc, dx, dy)
            if self.cloud is not None and self.flash_at is None:
                place(f, self.cloud, s_bg, self.cloud_anchor, dx, dy)
        else:
            mix = min(1.0, after / 0.6)
            bgi = Image.blend(self.bg_pre, self.bg_post, mix) if mix < 1 else self.bg_post
            place(f, bgi, s_bg, anc, dx, dy)
            if self.cloud is not None:
                g = ease(min(1.0, after / 3.2))
                pulse = 0.5 + 0.5 * math.sin(2 * math.pi * after / 1.5)
                c = grade(self.cloud, bright=1.0 + 0.25 * pulse)
                sc = s_bg * (0.35 + 0.65 * g)
                rise = (1 - g) * 25
                glow = c.filter(ImageFilter.GaussianBlur(45))
                place(f, glow, sc * 1.08, self.cloud_anchor, dx, dy + rise)
                place(f, c, sc, self.cloud_anchor, dx, dy + rise)
            ASH.draw(f, after, front=False, alpha=min(1.0, after / 1.0))
        s_ch = 1.0 + s.get("char_push", 0.08) * p
        chars = list(self.chars_pre if after < 0 else self.chars)
        boxes = list(self.boxes)
        swapped = False
        for at, imgs, bxs in self.swaps:
            if t >= at:
                chars, boxes, swapped = list(imgs), list(bxs), True
        if not swapped:
            for i, b in self.blink.items():
                # blink ~every 3.7 s for 4 frames, offset per character
                if ((t + i * 1.3) % 3.7) < 4 / FPS:
                    chars[i] = b
        layer = Image.new("RGBA", (W, H))
        layer.alpha_composite(self.shadow)
        breathe = math.sin(2 * math.pi * t / (2.4 if after < 0 else 1.1))
        for i, (c, bb) in enumerate(zip(chars, boxes)):
            a = ((bb[0] + bb[2]) / 2, bb[3])
            jitter = (1.8 if after < 0 else 3.0) * math.sin(t * 37) if i in self.tremble else 0.0
            place(layer, c, 1.0, a, jitter, 0, sy=1.0 + 0.007 * breathe)
        place(f, layer, s_ch, (W / 2, H * 0.80), dx * 1.3, dy * 1.3)
        self.fg.draw(f, t, dur, dx, dy)
        if after >= 0:
            f.alpha_composite(solid((255, 110, 40), 30))
            ASH.draw(f, after, front=True, alpha=min(1.0, after / 1.0))
            if after < 1.6:
                fa = 1.0 if after < 0.12 else math.exp(-(after - 0.12) * 2.6)
                f.alpha_composite(solid((255, 250, 235), 255 * min(fa, 1)))
        elif self.flash_at is not None:
            pre = max(0.0, (t - (self.flash_at - 0.8)) / 0.8)
            if pre > 0:
                f.alpha_composite(solid((255, 240, 220), 120 * pre ** 2))
        return f


TYPES = {"push": Push, "run": Run, "reveal": Reveal, "layers": Reveal}


class Look:
    """Series grade applied to every frame: saturation, contrast, tint, film grain."""

    def __init__(self, look):
        self.l = look or {}
        g = self.l.get("grain", 0)
        self.grain = []
        if g:
            r2 = random.Random(5)
            for _ in range(8):
                n = Image.effect_noise((W // 2, H // 2), 64).resize((W, H), Image.BILINEAR)
                self.grain.append(n.point(lambda v: int(128 + (v - 128) * g * 4)))

    def apply(self, rgb, k):
        l = self.l
        if l.get("sat", 1) != 1:
            rgb = ImageEnhance.Color(rgb).enhance(l["sat"])
        if l.get("contrast", 1) != 1:
            rgb = ImageEnhance.Contrast(rgb).enhance(l["contrast"])
        if l.get("tint"):
            rgb = Image.blend(rgb, Image.new("RGB", rgb.size, tuple(l["tint"])), l.get("tint_a", 0.06))
        if self.grain:
            n = self.grain[k % len(self.grain)].convert("RGB")
            rgb = Image.blend(rgb, ImageChops.overlay(rgb, n), 0.5)
        return rgb


def whip(rgb, t, dur_in=0.2, direction=1):
    """Whip-pan entrance: strong horizontal smear and slide that settles in dur_in seconds."""
    if t >= dur_in:
        return rgb
    k = 1 - t / dur_in
    shift = int(direction * 260 * k * k)
    out = ImageChops.offset(rgb, shift, 0)
    blur = out.filter(ImageFilter.BoxBlur(int(2 + 40 * k)))
    return Image.blend(out, blur, min(1.0, 0.4 + k))


def main():
    ep = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ep, "render", "shots.mp4")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    tl = tl_mod.load(ep)
    only = os.environ.get("ONLY")
    shots = [s for s in tl["shots"] if not only or s["id"] == only]
    built = {s["id"]: TYPES[s["type"]](s, ep) for s in shots}
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
         "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "17",
         "-preset", "medium", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    first = tl["shots"][0]["id"]
    look = Look(tl.get("look"))
    for k in range(int(tl["length"] * FPS)):
        T = k / FPS
        shot = next((s for s in tl["shots"] if s["start"] <= T < s["end"]), tl["shots"][-1])
        if only and shot["id"] != only:
            continue
        t, dur = T - shot["start"], shot["end"] - shot["start"]
        fr = built[shot["id"]].frame(t, dur)
        fr.alpha_composite(VIG)
        rgb = look.apply(fr.convert("RGB"), k)
        if shot.get("transition") == "whip":
            rgb = whip(rgb, t, 0.2, shot.get("whip_dir", 1))
        edge = min(t, dur - t) * FPS
        if shot.get("transition") == "whip" and t < 0.2:
            edge = 99
        if edge < 2 and shot.get("dip", True):
            rgb = Image.blend(Image.new("RGB", (W, H)), rgb, 0.55 + 0.2 * edge)
        if shot["id"] == first and t < 0.4:
            rgb = Image.blend(Image.new("RGB", (W, H)), rgb, t / 0.4)
        ff.stdin.write(rgb.tobytes())
    ff.stdin.close()
    ff.wait()
    print("wrote", out)


if __name__ == "__main__":
    main()
