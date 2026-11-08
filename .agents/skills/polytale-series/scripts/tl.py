"""Shared timeline loader: resolves relative timing so a re-voiced line never breaks sync.

Every script calls tl.load(ep). Rules (see references/timeline.md):
- A shot may give "len" instead of start/end; shots then follow each other in order.
- A shot with "vo": <file> places that voice line at shot start + "vo_at" (default 0.2) and
  grows the shot to at least voice length + "vo_at" + "vo_pad" (default 0.4). Its "th"/"en"
  become the subtitle for the line automatically.
- Any vo/sfx/subs/cards/countdown/stamp/alert/choice/title item with "shot": <id> has its
  times ("at", "start", "end", "t0", "t1") counted from that shot's start.
  "end": "shot_end" means the end of that shot; "dur": "to_shot_end" trims to it.
- "length" defaults to the end of the last shot.
"""
import json
import os
import subprocess

_cache = {}


def audio_len(path):
    if path not in _cache:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                             capture_output=True, text=True).stdout.strip()
        _cache[path] = float(out or 0)
    return _cache[path]


def load(ep):
    tl = json.load(open(os.path.join(ep, "timeline.json"), encoding="utf-8"))
    shots = tl["shots"]
    vo = list(tl.get("vo", []))
    subs = list(tl.get("subs", []))
    t = 0.0
    for s in shots:
        if "start" not in s:
            s["start"] = t
        need = 0.0
        if s.get("vo"):
            at = s.get("vo_at", 0.2)
            path = os.path.join(ep, s["vo"])
            d = audio_len(path) if os.path.exists(path) else 0.0
            need = at + d + s.get("vo_pad", 0.4)
            vo.append({"file": s["vo"], "at": s["start"] + at, "gain": s.get("vo_gain", 1.0)})
            if s.get("th"):
                subs.append({"start": s["start"] + at, "end": s["start"] + at + d + 0.15,
                             "th": s["th"], "en": s.get("en", "")})
        if "end" not in s:
            s["end"] = s["start"] + max(s.get("len", 0.0), need)
        t = s["end"]
    by_id = {s["id"]: s for s in shots}
    tl["length"] = tl.get("length") or shots[-1]["end"]

    def rel(item):
        sh = by_id.get(item.get("shot")) if item.get("shot") else None
        base = sh["start"] if sh else 0.0
        for k in ("at", "start", "end", "t0", "t1"):
            v = item.get(k)
            if isinstance(v, dict) and "shot" in v:  # {"shot": "s15", "at": 3.2}: any shot in the episode
                item[k] = by_id[v["shot"]]["start"] + v.get("at", 0.0)
            elif v == "shot_end" and sh:
                item[k] = sh["end"]
            elif isinstance(v, (int, float)) and sh:
                item[k] = v + base
        if item.get("dur") == "to_shot_end" and sh:
            item["dur"] = round(sh["end"] - item["at"], 3)
        ea = item.pop("end_at", None)  # {"shot": id, "at": s}: play until that moment
        if isinstance(ea, dict):
            item["dur"] = round(by_id[ea["shot"]]["start"] + ea.get("at", 0.0) - item.get("at", 0.0), 3)
        item.pop("shot", None)
        return item

    tl["vo"] = [rel(v) for v in vo]
    tl["subs"] = sorted((rel(s) for s in subs), key=lambda x: x["start"])
    for key in ("sfx", "cards", "countdown", "lessons"):
        tl[key] = [rel(x) for x in tl.get(key, [])]
    for ls in tl.get("lessons", []):
        for it in ls.get("items", []):
            if isinstance(it.get("at"), dict):
                it["at"] = by_id[it["at"]["shot"]]["start"] + it["at"].get("at", 0.0) - ls["start"]
    for key in ("stamp", "alert", "choice", "title", "music", "follow"):
        if tl.get(key):
            rel(tl[key])
    return tl


if __name__ == "__main__":
    import sys
    r = load(sys.argv[1])
    for s in r["shots"]:
        print(f"{s['id']:6s} {s['start']:6.2f} - {s['end']:6.2f}  {s['type']}")
    print("length", round(r["length"], 2))
