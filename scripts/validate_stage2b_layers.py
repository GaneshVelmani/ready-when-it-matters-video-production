#!/usr/bin/env python3
"""Preflight aligned Stage 2B PNG layers; does not validate artwork quality or rigging."""
from pathlib import Path
from PIL import Image
import argparse, json, sys

EXPECTED = (1024, 1536)
EXCLUDED = {"00_reference_flat.png", "layers_composite_preview.png"}
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('directory', type=Path)
    ap.add_argument('--report', type=Path)
    args = ap.parse_args()
    files = sorted(p for p in args.directory.glob('*.png') if p.name not in EXCLUDED)
    rows, failed = [], []
    if not files:
        print('FAIL: no candidate PNG layers found')
        return 2
    for p in files:
        try:
            with Image.open(p) as im:
                im.load()
                alpha = im.getchannel('A') if im.mode == 'RGBA' else None
                bbox = alpha.getbbox() if alpha else None
                extrema = alpha.getextrema() if alpha else None
                ok = im.size == EXPECTED and im.mode == 'RGBA' and bool(bbox) and extrema[0] == 0 and extrema[1] > 0
                row = {'file': p.name, 'size': list(im.size), 'mode': im.mode, 'alpha_bbox': list(bbox) if bbox else None, 'transparent_and_opaque': bool(extrema and extrema[0] == 0 and extrema[1] > 0), 'status': 'PASS' if ok else 'FAIL'}
        except Exception as e:
            row = {'file': p.name, 'status': 'ERROR', 'error': str(e)}
            ok = False
        rows.append(row)
        if not ok:
            failed.append(p.name)
    result = {'canvas': list(EXPECTED), 'layer_count': len(files), 'failed': failed, 'layers': rows, 'scope_note': 'Technical PNG preflight only; no hidden-pixel, silhouette, pivot, deformation or editor validation.'}
    print(json.dumps(result, indent=2))
    if args.report:
        args.report.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    return 1 if failed else 0
if __name__ == '__main__':
    sys.exit(main())