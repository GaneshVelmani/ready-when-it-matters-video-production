#!/usr/bin/env python3
"""Validate the basic dimensions and alpha channels of exported character PNGs."""
from pathlib import Path
from PIL import Image
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
files = sorted(root.glob("*.png"))
if not files:
    raise SystemExit(f"No PNG files found in {root}")
failed = False
for path in files:
    try:
        with Image.open(path) as im:
            alpha_ok = im.mode == "RGBA" and im.getchannel("A").getextrema() != (255, 255)
            size_ok = im.size == (1024, 1536)
            status = "PASS" if alpha_ok and size_ok else "CHECK"
            print(f"{status}\t{path.name}\t{im.size}\t{im.mode}\talpha={alpha_ok}")
            failed |= not (alpha_ok and size_ok)
    except Exception as exc:
        failed = True
        print(f"FAIL\t{path.name}\t{exc}")
raise SystemExit(1 if failed else 0)
