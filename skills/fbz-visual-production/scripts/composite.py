#!/usr/bin/env python3
"""
composite.py: layered compositor for FBZ brand assets (Pillow + numpy).

Builds a finished asset from a JSON spec using the FBZ layer order:
  plate -> grade -> light -> emblem (with depth) -> type band -> grain -> vignette

Usage:
  python3 composite.py spec.json
  python3 composite.py spec.json --out /path/final.png

Spec (all keys optional except size + plate):
{
  "size": [1800, 600],
  "out": "renders/email-header-01.png",
  "plate": {"src": "assets/plate.jpg", "fit": "cover", "focus": [0.6, 0.5], "scale": 1.0},
  "grade": [
    {"type": "linear", "from": [0,0], "to": [0,1], "color": "#1E2638", "opacity": [0.15, 0.75]},
    {"type": "radial", "center": [0.7, 0.4], "radius": 0.7, "color": "#D9965F", "opacity": [0.35, 0.0], "blend": "screen"}
  ],
  "light": [
    {"type": "slash", "angle": -18, "x": 0.62, "width": 0.05, "color": "#D9965F", "opacity": 0.55, "blur": 18},
    {"type": "rays", "origin": [0.15, -0.2], "color": "#FFF2DD", "opacity": 0.18, "blur": 60},
    {"type": "bokeh", "count": 18, "color": "#D9965F", "opacity": 0.35, "seed": 7}
  ],
  "emblem": {"src": "assets/logo-emblem.png", "anchor": [0.5, 0.42], "height": 0.46,
             "depth": {"shadow": 0.55, "glow": "#D9965F", "glow_opacity": 0.45, "rim": true}},
  "text": [
    {"text": "BOXING · FITNESS · MINDSET", "font": "fonts/DMSans-SemiBold.ttf", "size": 34, "color": "#FFFFFF",
     "anchor": [0.5, 0.86], "align": "center", "tracking": 8,
     "band": {"color": "#A9622F", "opacity": 0.92, "pad": [18, 48], "skew": -12, "full_width": true}}
  ],
  "grain": {"amount": 0.04, "seed": 3},
  "vignette": {"strength": 0.35, "softness": 0.65}
}

Colors are hex strings. Positions are fractions of the canvas (0..1). Blend modes: normal, multiply, screen, overlay, soft.
"""
import json, math, os, random, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops, ImageOps
import numpy as np

# ---------- helpers ----------
def hexrgb(h, a=255):
    h = h.lstrip('#'); return (int(h[0:2],16), int(h[2:4],16), int(h[4:6],16), a)

def fit_cover(img, size, focus=(0.5,0.5), scale=1.0):
    W,H = size; iw,ih = img.size
    s = max(W/iw, H/ih)*scale
    nw,nh = int(iw*s)+1, int(ih*s)+1
    img = img.resize((nw,nh), Image.LANCZOS)
    ox = int((nw-W)*focus[0]); oy = int((nh-H)*focus[1])
    ox = min(max(ox,0), nw-W); oy = min(max(oy,0), nh-H)
    return img.crop((ox,oy,ox+W,oy+H))

def blend(base, layer, mode='normal'):
    """base, layer: RGBA same size. Returns RGBA."""
    if mode == 'normal':
        return Image.alpha_composite(base, layer)
    b = np.asarray(base.convert('RGB')).astype(np.float32)/255
    l = np.asarray(layer.convert('RGB')).astype(np.float32)/255
    a = (np.asarray(layer.split()[3]).astype(np.float32)/255)[...,None]
    if mode == 'multiply': r = b*l
    elif mode == 'screen': r = 1-(1-b)*(1-l)
    elif mode == 'overlay': r = np.where(b<0.5, 2*b*l, 1-2*(1-b)*(1-l))
    elif mode == 'soft': r = (1-2*l)*b*b + 2*l*b
    else: r = l
    out = b*(1-a) + r*a
    res = Image.fromarray((np.clip(out,0,1)*255).astype(np.uint8), 'RGB').convert('RGBA')
    res.putalpha(base.split()[3]); return res

def linear_gradient(size, p0, p1, color, op):
    W,H = size
    xs, ys = np.meshgrid(np.linspace(0,1,W), np.linspace(0,1,H))
    dx,dy = p1[0]-p0[0], p1[1]-p0[1]; L = dx*dx+dy*dy or 1
    t = np.clip(((xs-p0[0])*dx + (ys-p0[1])*dy)/L, 0, 1)
    alpha = (op[0] + (op[1]-op[0])*t)*255
    layer = Image.new('RGBA', size, hexrgb(color)); layer.putalpha(Image.fromarray(alpha.astype(np.uint8)))
    return layer

def radial_gradient(size, center, radius, color, op):
    W,H = size
    xs, ys = np.meshgrid(np.linspace(0,1,W), np.linspace(0,1,H))
    d = np.sqrt(((xs-center[0])*(W/H if W>H else 1))**2 + ((ys-center[1])*(H/W if H>W else 1))**2)/radius
    t = np.clip(d,0,1); t = t*t*(3-2*t)
    alpha = (op[0] + (op[1]-op[0])*t)*255
    layer = Image.new('RGBA', size, hexrgb(color)); layer.putalpha(Image.fromarray(alpha.astype(np.uint8)))
    return layer

def light_slash(size, angle, x, width, color, opacity, blur):
    W,H = size; layer = Image.new('RGBA', size, (0,0,0,0)); d = ImageDraw.Draw(layer)
    w = width*W; cx = x*W; t = math.tan(math.radians(angle))*H
    poly = [(cx - w/2 + t/2, 0), (cx + w/2 + t/2, 0), (cx + w/2 - t/2, H), (cx - w/2 - t/2, H)]
    d.polygon(poly, fill=hexrgb(color, int(opacity*255)))
    return layer.filter(ImageFilter.GaussianBlur(blur))

def light_rays(size, origin, color, opacity, blur, count=7, seed=1):
    W,H = size; layer = Image.new('RGBA', size, (0,0,0,0)); d = ImageDraw.Draw(layer); rnd = random.Random(seed)
    ox,oy = origin[0]*W, origin[1]*H
    for i in range(count):
        a = math.radians(rnd.uniform(20,70)); L = max(W,H)*2; w = rnd.uniform(0.02,0.07)*W
        ex,ey = ox+math.cos(a)*L, oy+math.sin(a)*L
        nx,ny = -math.sin(a)*w, math.cos(a)*w
        d.polygon([(ox,oy),(ex+nx,ey+ny),(ex-nx,ey-ny)], fill=hexrgb(color, int(opacity*255*rnd.uniform(0.5,1))))
    return layer.filter(ImageFilter.GaussianBlur(blur))

def bokeh(size, count, color, opacity, seed=1):
    W,H = size; layer = Image.new('RGBA', size, (0,0,0,0)); rnd = random.Random(seed)
    for i in range(count):
        r = rnd.uniform(0.006,0.03)*W; x,y = rnd.uniform(0,W), rnd.uniform(0,H)
        dot = Image.new('RGBA', (int(r*2)+2,)*2, (0,0,0,0)); ImageDraw.Draw(dot).ellipse((1,1,r*2,r*2), fill=hexrgb(color, int(opacity*255*rnd.uniform(0.3,1))))
        dot = dot.filter(ImageFilter.GaussianBlur(r*rnd.uniform(0.2,0.6)))
        layer.alpha_composite(dot, (int(x-r), int(y-r)))
    return layer

def place_emblem(canvas, spec):
    W,H = canvas.size
    em = Image.open(spec['src']).convert('RGBA')
    h = int(spec.get('height',0.4)*H); s = h/em.size[1]; em = em.resize((int(em.size[0]*s), h), Image.LANCZOS)
    ax,ay = spec.get('anchor',[0.5,0.5]); x = int(ax*W - em.size[0]/2); y = int(ay*H - em.size[1]/2)
    depth = spec.get('depth', {})
    if depth.get('glow'):
        glow = Image.new('RGBA', canvas.size, (0,0,0,0)); g = Image.new('RGBA', em.size, hexrgb(depth['glow'])); g.putalpha(em.split()[3])
        glow.alpha_composite(g, (x,y)); glow = glow.filter(ImageFilter.GaussianBlur(h*0.12))
        a = glow.split()[3].point(lambda v: int(v*depth.get('glow_opacity',0.4))); glow.putalpha(a); canvas = Image.alpha_composite(canvas, glow)
    if depth.get('shadow'):
        sh = Image.new('RGBA', canvas.size, (0,0,0,0)); s2 = Image.new('RGBA', em.size, (0,0,0,255)); s2.putalpha(em.split()[3])
        sh.alpha_composite(s2, (x+int(h*0.02), y+int(h*0.06))); sh = sh.filter(ImageFilter.GaussianBlur(h*0.06))
        a = sh.split()[3].point(lambda v: int(v*depth['shadow'])); sh.putalpha(a); canvas = Image.alpha_composite(canvas, sh)
    canvas.alpha_composite(em, (x,y))
    if depth.get('rim'):
        # subtle top-left rim light: offset alpha edge
        rim = Image.new('RGBA', em.size, (255,245,225,255)); rim.putalpha(em.split()[3])
        edge = ImageChops.subtract(em.split()[3], ImageChops.offset(em.split()[3], int(h*0.012), int(h*0.012)))
        rim.putalpha(edge.point(lambda v: int(v*0.55))); canvas.alpha_composite(rim.filter(ImageFilter.GaussianBlur(1)), (x,y))
    return canvas

def draw_text(canvas, spec):
    W,H = canvas.size
    try:
        font = ImageFont.truetype(spec['font'], spec['size'])
        if spec.get('weight') or spec.get('opsz'):
            try:
                axes = font.get_variation_axes(); vals=[]
                for a in axes:
                    n=(a['name'].decode() if isinstance(a['name'],bytes) else a['name']).lower()
                    if n=='weight' and spec.get('weight'): vals.append(spec['weight'])
                    elif 'optical' in n: vals.append(spec.get('opsz', min(max(spec['size'],a['minimum']),a['maximum'])))
                    else: vals.append(a['default'])
                font.set_variation_by_axes(vals)
            except Exception: pass
    except Exception: font = ImageFont.load_default()
    text = spec['text']; tracking = spec.get('tracking',0)
    # measure with tracking
    widths = [font.getlength(ch) for ch in text]; tw = sum(widths) + tracking*(len(text)-1); th = spec['size']*1.2
    ax,ay = spec.get('anchor',[0.5,0.5]); align = spec.get('align','center')
    x0 = ax*W - (tw/2 if align=='center' else (tw if align=='right' else 0)); y0 = ay*H - th/2
    band = spec.get('band')
    if band:
        pt,pr = band.get('pad',[16,40]); bl = Image.new('RGBA', canvas.size, (0,0,0,0)); d = ImageDraw.Draw(bl)
        bx0 = 0 if band.get('full_width') else x0-pr; bx1 = W if band.get('full_width') else x0+tw+pr
        by0, by1 = y0-pt, y0+th+pt; sk = math.tan(math.radians(band.get('skew',0)))*(by1-by0)
        d.polygon([(bx0+sk/2,by0),(bx1+sk/2,by0),(bx1-sk/2,by1),(bx0-sk/2,by1)], fill=hexrgb(band['color'], int(band.get('opacity',1)*255)))
        canvas = Image.alpha_composite(canvas, bl)
    layer = Image.new('RGBA', canvas.size, (0,0,0,0)); d = ImageDraw.Draw(layer)
    if spec.get('shadow', True):
        sl = Image.new('RGBA', canvas.size, (0,0,0,0)); sd = ImageDraw.Draw(sl); cx = x0
        for ch,w in zip(text,widths): sd.text((cx+2, y0+3), ch, font=font, fill=(0,0,0,150)); cx += w+tracking
        canvas = Image.alpha_composite(canvas, sl.filter(ImageFilter.GaussianBlur(3)))
    cx = x0
    for ch,w in zip(text,widths): d.text((cx, y0), ch, font=font, fill=hexrgb(spec.get('color','#FFFFFF'))); cx += w+tracking
    return Image.alpha_composite(canvas, layer)

def add_grain(canvas, amount, seed=1):
    rnd = np.random.default_rng(seed); W,H = canvas.size
    noise = rnd.normal(0, amount*255, (H,W,1)).astype(np.float32)
    arr = np.asarray(canvas.convert('RGB')).astype(np.float32) + noise
    out = Image.fromarray(np.clip(arr,0,255).astype(np.uint8),'RGB').convert('RGBA'); out.putalpha(canvas.split()[3]); return out

def add_vignette(canvas, strength, softness):
    W,H = canvas.size; xs,ys = np.meshgrid(np.linspace(-1,1,W), np.linspace(-1,1,H))
    d = np.sqrt(xs*xs+ys*ys)/math.sqrt(2); m = np.clip((d-(1-softness))/softness, 0, 1); m = m*m*(3-2*m)
    layer = Image.new('RGBA', canvas.size, (8,10,16,255)); layer.putalpha(Image.fromarray((m*strength*255).astype(np.uint8)))
    return Image.alpha_composite(canvas, layer)

# ---------- main ----------
def build(spec, base_dir='.'):
    W,H = spec['size']; size = (W,H)
    p = spec['plate']; src = os.path.join(base_dir, p['src'])
    canvas = fit_cover(Image.open(src).convert('RGBA'), size, tuple(p.get('focus',[0.5,0.5])), p.get('scale',1.0))
    for g in spec.get('grade', []):
        layer = linear_gradient(size, g['from'], g['to'], g['color'], g['opacity']) if g['type']=='linear' else radial_gradient(size, g['center'], g.get('radius',0.7), g['color'], g['opacity'])
        canvas = blend(canvas, layer, g.get('blend','normal'))
    for l in spec.get('light', []):
        if l['type']=='slash': layer = light_slash(size, l.get('angle',-18), l.get('x',0.6), l.get('width',0.05), l['color'], l.get('opacity',0.5), l.get('blur',16))
        elif l['type']=='rays': layer = light_rays(size, l.get('origin',[0.1,-0.2]), l['color'], l.get('opacity',0.2), l.get('blur',50), l.get('count',7), l.get('seed',1))
        else: layer = bokeh(size, l.get('count',16), l['color'], l.get('opacity',0.3), l.get('seed',1))
        canvas = blend(canvas, layer, l.get('blend','screen'))
    if spec.get('emblem'):
        e = dict(spec['emblem']); e['src'] = os.path.join(base_dir, e['src']); canvas = place_emblem(canvas, e)
    for t in spec.get('text', []):
        t = dict(t); t['font'] = os.path.join(base_dir, t['font']) if not os.path.isabs(t['font']) else t['font']; canvas = draw_text(canvas, t)
    if spec.get('grain'): canvas = add_grain(canvas, spec['grain'].get('amount',0.04), spec['grain'].get('seed',1))
    if spec.get('vignette'): canvas = add_vignette(canvas, spec['vignette'].get('strength',0.35), spec['vignette'].get('softness',0.65))
    return canvas.convert('RGB')

if __name__ == '__main__':
    spec_path = sys.argv[1]; spec = json.load(open(spec_path))
    out = spec.get('out');
    if '--out' in sys.argv: out = sys.argv[sys.argv.index('--out')+1]
    base = os.path.dirname(os.path.abspath(spec_path))
    img = build(spec, base); out = os.path.join(base, out) if not os.path.isabs(out) else out
    os.makedirs(os.path.dirname(out), exist_ok=True); img.save(out, quality=95); print('wrote', out, img.size)
