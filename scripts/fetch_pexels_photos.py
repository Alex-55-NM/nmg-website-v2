#!/usr/bin/env python3
"""Download the Pexels photos listed in build/photo_ids.txt into site/assets/img/photos/.

Each photo is saved as pexels-<id>-800.jpg and pexels-<id>-1600.jpg and listed with
its source page in CREDITS.json. Photos no longer listed are removed. Standard library
only; run by .github/workflows/fetch-photos.yml (GitHub runners can reach images.pexels.com).
"""
import json, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site" / "assets" / "img" / "photos"
WIDTHS = (800, 1600)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

ids = [l.strip() for l in (ROOT / "build" / "photo_ids.txt").read_text().splitlines() if l.strip() and not l.startswith("#")]
OUT.mkdir(parents=True, exist_ok=True)
failed, credits = [], {}
for pid in ids:
    for w in WIDTHS:
        dest = OUT / f"pexels-{pid}-{w}.jpg"
        if dest.exists() and dest.stat().st_size > 5000:
            continue
        url = f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w={w}"
        for attempt in range(4):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "image/jpeg,image/*"})
                with urllib.request.urlopen(req, timeout=60) as r:
                    data = r.read()
                if len(data) < 5000 or data[:2] != b"\xff\xd8":
                    raise ValueError(f"unexpected response ({len(data)} bytes)")
                dest.write_bytes(data)
                break
            except Exception as e:
                if attempt == 3:
                    failed.append(f"{pid}@{w}: {e}")
                time.sleep(2 * (attempt + 1))
    credits[pid] = {"source": f"https://www.pexels.com/photo/{pid}/", "license": "Pexels License (https://www.pexels.com/license/)",
                    "files": [f"pexels-{pid}-{w}.jpg" for w in WIDTHS]}
for f in OUT.glob("pexels-*.jpg"):
    if f.name.split("-")[1] not in ids:
        f.unlink()
(OUT / "CREDITS.json").write_text(json.dumps(credits, indent=1) + "\n")
print(f"{len(ids)} photos listed; failed: {len(failed)}")
for f in failed: print("  FAILED", f)
sys.exit(1 if failed else 0)
