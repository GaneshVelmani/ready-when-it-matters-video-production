#!/usr/bin/env python3
"""Preflight Step 2 male-character PNG exports before animation import.

Usage:
  python scripts/check_step2_asset_pack.py path/to/png_layers
  python scripts/check_step2_asset_pack.py path/to/png_layers --csv audit.csv

This validates file structure, canvas consistency, RGBA mode and alpha presence.
It does NOT prove clean silhouettes, hidden-pixel overlap, correct pivots, or rig quality.
"""
from __future__ import annotations
import argparse
import csv
import sys
from pathlib import Path
from PIL import Image

REQUIRED = [
    "01_head_base.png", "02_hair.png", "03_neck.png",
    "04_torso_jacket_front.png",
    "05_left_upper_arm.png", "06_left_forearm.png", "07_left_hand.png",
    "08_right_upper_arm.png", "09_right_forearm.png", "10_right_hand.png",
    "11_pelvis.png", "12_left_thigh.png", "13_left_lower_leg.png",
    "14_right_thigh.png", "15_right_lower_leg.png",
    "16_left_boot.png", "17_right_boot.png",
]

def inspect(path: Path) -> dict:
    with Image.open(path) as im:
        im.load()
        rgba = im.mode == "RGBA"
        alpha = im.getchannel("A") if "A" in im.getbands() else None
        bbox = alpha.getbbox() if alpha else None
        alpha_extrema = alpha.getextrema() if alpha else None
        transparent = bool(alpha_extrema and alpha_extrema[0] == 0 and alpha_extrema[1] > 0)
        return {
            "file": path.name,
            "width": im.width,
            "height": im.height,
            "mode": im.mode,
            "rgba": rgba,
            "has_alpha": alpha is not None,
            "has_transparency": transparent,
            "alpha_bbox": str(bbox) if bbox else "",
            "status": "PASS" if rgba and transparent and bbox else "FAIL",
        }

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("directory", type=Path)
    ap.add_argument("--csv", type=Path, help="Optional CSV audit output")
    args = ap.parse_args()
    root = args.directory
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 2
    missing = [name for name in REQUIRED if not (root / name).is_file()]
    pngs = sorted(root.glob("*.png"))
    if not pngs:
        print("ERROR: no PNG files found", file=sys.stderr)
        return 2
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
    canvas_sizes = {(r.get("width"), r.get("height")) for r in rows if r.get("width")}
    print(f"PNG files: {len(pngs)}")
    print(f"Canvas sizes: {sorted(canvas_sizes)}")
    print(f"Missing required body parts: {missing or 'none'}")
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
    consistent = len(canvas_sizes) == 1
    ok = not missing and not failures and consistent
    print("PREFLIGHT:", "PASS" if ok else "FAIL")
    print("NOTE: visual and animation acceptance tests remain mandatory.")
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
