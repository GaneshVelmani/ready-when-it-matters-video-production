#!/usr/bin/env python3
"""Preflight Step 2 male-character PNG exports before animation import.

Usage:
  python scripts/check_step2_asset_pack.py path/to/png_layers
  python scripts/check_step2_asset_pack.py path/to/png_layers --csv audit.csv

The 17 rig body parts must share a 1024x1536 canvas. Auxiliary facial crops
may use their own dimensions. This validates technical PNG properties only;
it cannot prove clean silhouettes, hidden-pixel overlap, pivots or rig quality.
"""
from __future__ import annotations
import argparse
import csv
import sys
from pathlib import Path
from PIL import Image

REQUIRED = [
    "01_head_base.png", "02_hair.png", "03_neck.png", "04_torso_jacket_front.png",
    "05_left_upper_arm.png", "06_left_forearm.png", "07_left_hand.png",
    "08_right_upper_arm.png", "09_right_forearm.png", "10_right_hand.png",
    "11_pelvis.png", "12_left_thigh.png", "13_left_lower_leg.png",
    "14_right_thigh.png", "15_right_lower_leg.png", "16_left_boot.png",
    "17_right_boot.png",
]
EXPECTED_CANVAS = (1024, 1536)

def inspect(path: Path) -> dict:
    with Image.open(path) as im:
        im.load()
        alpha = im.getchannel("A") if "A" in im.getbands() else None
        extrema = alpha.getextrema() if alpha else None
        bbox = alpha.getbbox() if alpha else None
        transparent = bool(extrema and extrema[0] == 0 and extrema[1] > 0)
        rgba = im.mode == "RGBA"
        return {
            "file": path.name, "width": im.width, "height": im.height,
            "mode": im.mode, "rgba": rgba, "has_alpha": alpha is not None,
            "has_transparency": transparent, "alpha_bbox": str(bbox) if bbox else "",
            "status": "PASS" if rgba and transparent and bbox else "FAIL",
        }

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("directory", type=Path)
    ap.add_argument("--csv", type=Path)
    args = ap.parse_args()
    root = args.directory
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 2
    missing = [name for name in REQUIRED if not (root / name).is_file()]
    pngs = sorted(root.glob("*.png"))
    rows, failures = [], []
    for path in pngs:
        try:
            row = inspect(path)
            rows.append(row)
            if row["status"] != "PASS":
                failures.append(path.name)
        except Exception as exc:
            failures.append(path.name)
            rows.append({"file": path.name, "status": f"ERROR: {exc}"})
    by_name = {row["file"]: row for row in rows}
    wrong_canvas = [
        name for name in REQUIRED
        if name in by_name and (by_name[name].get("width"), by_name[name].get("height")) != EXPECTED_CANVAS
    ]
    print(f"PNG files: {len(pngs)}")
    print(f"Required body parts missing: {missing or 'none'}")
    print(f"Required body parts off {EXPECTED_CANVAS[0]}x{EXPECTED_CANVAS[1]} canvas: {wrong_canvas or 'none'}")
    print(f"RGBA/transparency failures: {failures or 'none'}")
    for row in rows:
        print(f"{row.get('status')}\t{row['file']}\t{row.get('width','?')}x{row.get('height','?')}\t{row.get('mode','?')}\t{row.get('alpha_bbox','')}")
    if args.csv:
        fields = ["file", "width", "height", "mode", "rgba", "has_alpha", "has_transparency", "alpha_bbox", "status"]
        with args.csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        print(f"CSV written: {args.csv}")
    ok = bool(pngs) and not missing and not failures and not wrong_canvas
    print("PREFLIGHT:", "PASS" if ok else "FAIL")
    print("NOTE: visual and animation acceptance tests remain mandatory.")
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
