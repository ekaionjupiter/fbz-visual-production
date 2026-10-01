#!/usr/bin/env python3
"""
split_reference.py: turn ONE reference composite (a screenshot, a competitor header, a Pinterest tile)
into the three separated inputs the doctrine requires before anything is built:

  1. background PLATE   (4K, no text, no logo, no buttons, no UI)   -> for the image model to remix
  2. transparent CUTOUT (subject only, alpha)                        -> for compositing in code
  3. UI LAYOUT reference (text/button positions on plain black)      -> for type placement in code

This script does not call Higgsfield directly (the MCP is driven by Claude). It emits the three exact
prompts + a job manifest that Claude feeds to the Higgsfield MCP (`generate_image` with the reference
as `image_references`), then post-processes the results: alpha-matting the cutout and writing the
layout JSON.

Usage:
  python3 split_reference.py reference.jpg --out ./ref-split/            # writes prompts.json
  python3 split_reference.py reference.jpg --out ./ref-split/ --cutout generated_cutout.png
      (post-process: converts a near-white or near-black background into real alpha)
"""
import json, os, sys
from PIL import Image
import numpy as np

PROMPTS = {
  "plate": ("Create an image exactly like this reference, same scene, same lighting, same color grade and mood, "
            "rendered at 4K. Remove ALL text, headlines, buttons, icons, logos, badges, circles and UI elements. "
            "Keep only the photographic background and environment. Extend the scene naturally where elements were removed. "
            "Photoreal, 35mm film grain, no watermark."),
  "cutout": ("Isolate ONLY the main subject/object from this reference on a pure solid #000000 black background, "
             "nothing else: no text, no logo, no UI, no shadow on the floor. Keep the subject's exact shape, lighting "
             "and colors. Centered, full view, 4K."),
  "layout": ("Recreate ONLY the layout of this reference on a plain solid black background: keep every text block, "
             "headline, button and badge in the exact same position and size, as flat white rectangles or white text, "
             "remove the photo/background entirely. No colors, no imagery. This is a wireframe of the composition.")
}

def manifest(ref, out):
    os.makedirs(out, exist_ok=True)
    im = Image.open(ref); w,h = im.size
    ar = "16:9" if w/h > 1.6 else ("4:5" if w/h < 0.9 else ("3:2" if w/h > 1.3 else "1:1"))
    m = {"reference": os.path.abspath(ref), "size": [w,h], "aspect_ratio": ar,
         "jobs": [{"name": k, "model": "gpt_image_2_5", "quality": "high", "resolution": "2k" if k!="plate" else "4k",
                   "aspect_ratio": ar, "medias": [{"role": "image_references", "value": "<media_id of reference>"}],
                   "prompt": v, "save_as": os.path.join(out, f"{k}.png")} for k,v in PROMPTS.items()]}
    json.dump(m, open(os.path.join(out,'prompts.json'),'w'), indent=2)
    print("wrote", os.path.join(out,'prompts.json')); print("Feed each job to the Higgsfield MCP generate_image_batch, then re-run with --cutout <file> to matte it.")

def matte(path, out):
    """Convert a subject-on-black (or on-white) render into a real RGBA cutout."""
    im = Image.open(path).convert('RGB'); a = np.asarray(im).astype(np.float32)
    lum = a.mean(axis=2); corner = np.median(np.concatenate([lum[:8,:8].ravel(), lum[-8:,-8:].ravel()]))
    dark_bg = corner < 128
    alpha = np.clip((lum - 12)/40, 0, 1) if dark_bg else np.clip((243 - lum)/40, 0, 1)
    # despill: unpremultiply toward subject color
    rgba = np.dstack([a, alpha[...,None]*255]).astype(np.uint8)
    res = Image.fromarray(rgba, 'RGBA'); dst = os.path.join(out, 'cutout-alpha.png'); res.save(dst); print('wrote', dst)

if __name__ == '__main__':
    ref = sys.argv[1]; out = sys.argv[sys.argv.index('--out')+1] if '--out' in sys.argv else './ref-split'
    if '--cutout' in sys.argv: matte(sys.argv[sys.argv.index('--cutout')+1], out)
    else: manifest(ref, out)
