"""PolyTale procedural sound bed (no external assets, no credits).

Usage: python sound.py <episode_dir> [out.wav]     # default <episode_dir>/audio/sfx-bed.wav
Reads timeline.json "length" and the optional "sound" block (seconds, episode time):
  {"drone": true, "phones": [a, b], "siren": a, "run": [a, b], "heart": [a, b], "flash": t}
Every key except length is optional; omit what the episode does not need.
"""
import json
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import tl as tl_mod  # noqa: E402
import sys
import wave

import numpy as np

SR = 48000
rng = np.random.default_rng(3)


def t_axis(sec):
    return np.arange(int(sec * SR)) / SR


def env(n, a, r):
    e = np.ones(n)
    a, r = int(a * SR), int(r * SR)
    if a:
        e[:a] = np.linspace(0, 1, a)
    if r:
        e[-r:] *= np.linspace(1, 0, r)
    return e


def lowpass(x, cutoff):
    # one-pole, applied twice
    a = np.exp(-2 * np.pi * cutoff / SR)
    for _ in range(2):
        y = np.empty_like(x)
        acc = 0.0
        for i in range(len(x)):
            acc = (1 - a) * x[i] + a * acc
            y[i] = acc
        x = y
    return x


def lowpass_fast(x, cutoff):
    # FFT brick-ish lowpass with soft knee (fast for long buffers)
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / (1 + (f / cutoff) ** 4)
    return np.fft.irfft(X, len(x))


def highpass_fast(x, cutoff):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / (1 + (cutoff / np.maximum(f, 1e-3)) ** 4)
    return np.fft.irfft(X, len(x))


def reverb(x, decay=1.6, mix=0.35):
    n = int(decay * SR)
    ir = rng.standard_normal(n) * np.exp(-np.linspace(0, 7, n))
    ir = lowpass_fast(ir, 3000)
    ir /= np.abs(ir).sum() ** 0.5 * 8
    wet = np.convolve(x, ir)[: len(x)] if len(x) < 200000 else fft_conv(x, ir)
    return (1 - mix) * x + mix * wet


def fft_conv(x, h):
    n = len(x) + len(h)
    return np.fft.irfft(np.fft.rfft(x, n) * np.fft.rfft(h, n), n)[: len(x)]


def add(bus, sig, at):
    i = int(at * SR)
    j = min(len(bus), i + len(sig))
    if j > i:
        bus[i:j] += sig[: j - i]


def phones(dur):
    """Emergency-alert two-tone (853 + 960 Hz) from many phones, slightly offset."""
    out = np.zeros(int(dur * SR))
    for k in range(9):
        t = t_axis(dur)
        det = 1 + rng.uniform(-0.004, 0.004)
        tone = np.sin(2 * np.pi * 853 * det * t) + np.sin(2 * np.pi * 960 * det * t)
        gate = (np.sin(2 * np.pi * (2.2 + rng.uniform(-0.15, 0.15)) * t + rng.uniform(0, 6)) > -0.2)
        g = lowpass_fast(gate.astype(float), 60)
        dist = 1.0 if k == 0 else rng.uniform(0.12, 0.35)
        sig = tone * g * dist
        if k:
            sig = lowpass_fast(sig, 2500)
        out += np.roll(sig, int(rng.uniform(0, 0.4) * SR))
    # buzz of the hero phone
    t = t_axis(dur)
    out += 0.25 * np.sign(np.sin(2 * np.pi * 150 * t)) * (np.sin(2 * np.pi * 1.1 * t) > 0)
    return out * env(len(out), 0.05, 0.6) * 0.12


def siren(dur):
    t = t_axis(dur)
    # slow rising-falling air-raid wail
    f = 330 + 260 * (0.5 - 0.5 * np.cos(2 * np.pi * t / 7.0))
    ph = 2 * np.pi * np.cumsum(f) / SR
    s = np.sin(ph) + 0.5 * np.sin(2 * ph) + 0.3 * np.sin(3 * ph)
    s = lowpass_fast(s, 1800)
    s = reverb(s, 2.5, 0.6)
    return s * env(len(s), 2.0, 0.3) * 0.07


def drone(dur):
    t = t_axis(dur)
    s = 0.6 * np.sin(2 * np.pi * 46 * t) + 0.3 * np.sin(2 * np.pi * 69.3 * t + 1)
    n = lowpass_fast(rng.standard_normal(len(t)), 180) * 3
    return (s + n) * env(len(t), 1.5, 0.5) * 0.06


def footsteps(start, end):
    dur = end - start
    out = np.zeros(int(dur * SR))
    step = 1 / 3.4
    k = 0
    while k * step < dur - 0.05:
        n = int(0.09 * SR)
        hit = lowpass_fast(rng.standard_normal(n), 900) * np.exp(-np.linspace(0, 9, n)) * 2.5
        thump = np.sin(2 * np.pi * 80 * t_axis(0.09)) * np.exp(-np.linspace(0, 12, n))
        add(out, (hit + thump) * (0.8 if k % 2 else 1.0), k * step + rng.uniform(-0.01, 0.01))
        k += 1
    breath = lowpass_fast(rng.standard_normal(len(out)), 1200) * (0.5 + 0.5 * np.sin(2 * np.pi * 1.7 * t_axis(dur))) ** 3
    return (out * 0.35 + breath * 0.04) * env(len(out), 0.05, 0.2)


def heartbeat(start, end):
    dur = end - start
    out = np.zeros(int(dur * SR))
    beat = 0.0
    while beat < dur - 0.3:
        for off, amp in ((0, 1.0), (0.16, 0.7)):
            n = int(0.12 * SR)
            b = np.sin(2 * np.pi * 52 * t_axis(0.12)) * np.exp(-np.linspace(0, 8, n)) * amp
            add(out, b, beat + off)
        beat += 0.62
    return out * 0.5 * env(len(out), 0.3, 0.1)


def blast(length_after):
    n = int(length_after * SR)
    t = t_axis(length_after)
    boom = np.sin(2 * np.pi * (60 * np.exp(-t * 1.2) + 28) * t) * np.exp(-t * 0.9)
    crack = rng.standard_normal(n) * np.exp(-t * 6)
    rumble = lowpass_fast(rng.standard_normal(n), 120) * 6 * np.exp(-t * 0.6)
    s = boom * 1.0 + lowpass_fast(crack, 2500) * 0.6 + rumble
    return s * 0.55


def whoosh(dur):
    t = t_axis(dur)
    n = rng.standard_normal(len(t))
    s = highpass_fast(n, 400)
    s = lowpass_fast(s, 6000) * (t / dur) ** 2.5
    return s * 0.25


def ring(dur):
    t = t_axis(dur)
    return np.sin(2 * np.pi * 3900 * t) * env(len(t), 0.4, 1.5) * 0.025


def main():
    import os
    ep = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ep, "audio", "sfx-bed.wav")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    tl = tl_mod.load(ep)
    L = tl["length"]
    sd = tl.get("sound", {})
    bus = np.zeros(int(L * SR))
    flash = sd.get("flash")
    end_pre = flash if flash is not None else L
    pre = np.zeros_like(bus)
    if sd.get("drone", True):
        add(pre, drone(end_pre), 0)
    if "phones" in sd:
        p0, p1 = sd["phones"]
        add(pre, phones(p1 - p0), p0)
    if "siren" in sd:
        add(pre, siren(end_pre - sd["siren"]), sd["siren"])
    if "run" in sd:
        r0, r1 = sd["run"]
        add(pre, footsteps(r0, r1), r0)
    if "heart" in sd:
        h0, h1 = sd["heart"]
        add(pre, heartbeat(h0, h1), h0)
    if flash is not None:
        add(pre, whoosh(0.9), flash - 0.9)
        i = int(flash * SR)
        pre[i:] = lowpass_fast(pre[i:], 250) * 0.3
    bus += pre
    if flash is not None:
        add(bus, blast(L - flash), flash)
        add(bus, ring(L - flash - 0.2), flash + 0.2)
    peak = np.max(np.abs(bus)) or 1
    bus = bus / peak * 0.8
    pcm = (np.clip(bus, -1, 1) * 32767).astype(np.int16)
    with wave.open(out, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print("wrote", out, L, "s")


if __name__ == "__main__":
    main()
