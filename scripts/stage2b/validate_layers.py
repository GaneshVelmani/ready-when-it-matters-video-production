#!/usr/bin/env python3
"""Validate Stage 2B PNG layer dimensions, alpha channels and alpha bounds."""
from pathlib import Path
from PIL import Image
import json, sys
ROOT=Path(__file__).resolve().parents[2]
LAYERS=ROOT/"characters/male/rig_prototype/layers"
OUT=ROOT/"characters/male/rig_prototype/tests"
OUT.mkdir(parents=True, exist_ok=True)
rows=[]; failures=[]
for p in sorted(LAYERS.glob("*.png")):
    try:
        im=Image.open(p)
        if im.format != "PNG": raise ValueError("not PNG")
        if im.mode != "RGBA": failures.append(f"{p.name}: expected RGBA, got {im.mode}")
        if im.size != (1024,1536): failures.append(f"{p.name}: wrong canvas {im.size}")
        a=im.getchannel("A")
        rows.append({"file":p.name,"size":list(im.size),"mode":im.mode,
                     "alpha_bbox":list(a.getbbox()) if a.getbbox() else None,
                     "alpha_extrema":list(a.getextrema())})
    except Exception as e: failures.append(f"{p.name}: {e}")
report={"layer_count":len(rows),"canvas":[1024,1536],"layers":rows,
        "technical_failures":failures,
        "rig_acceptance":"FAIL — geometry and overlap tests remain unresolved"}
(OUT/"layer_validation.json").write_text(json.dumps(report,indent=2))
print(json.dumps({"layer_count":len(rows),"technical_failures":failures,
                  "rig_acceptance":report["rig_acceptance"]},indent=2))
sys.exit(1 if failures else 0)
