#!/usr/bin/env python3
"""Lena Park asset build: every finished composite from plates + emblem + type, via the fbz-visual-production skill.
Run from lena-park/assets:  python3 build_assets.py
Writes finals to ./final/ and dumps every spec to ../../skills/fbz-visual-production/examples/."""
import json, os, sys, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
SK = os.path.abspath(os.path.join(HERE, '..', '..', 'skills', 'fbz-visual-production'))
spec = importlib.util.spec_from_file_location('composite', os.path.join(SK, 'scripts', 'composite.py')); comp = importlib.util.module_from_spec(spec); spec.loader.exec_module(comp)
F_SERIF = os.path.join(SK, 'fonts', 'Fraunces.ttf'); F_SERIF_I = os.path.join(SK, 'fonts', 'Fraunces-Italic.ttf'); F_SANS = os.path.join(SK, 'fonts', 'DMSans.ttf')
EMB = 'emblem/emblem-depth.png'
NAVY, LAMP, DEEP, MOON, LINEN = '#1E2638', '#D9965F', '#A9622F', '#F7F2EA', '#EDE4D6'
OUT = os.path.join(HERE, 'final'); os.makedirs(OUT, exist_ok=True); EX = os.path.join(SK, 'examples'); os.makedirs(EX, exist_ok=True)

def grade_dark(top=0.25, bottom=0.78): return {"type":"linear","from":[0,0],"to":[0,1],"color":NAVY,"opacity":[top,bottom]}
def glow(cx, cy, r=0.55, op=0.38): return {"type":"radial","center":[cx,cy],"radius":r,"color":LAMP,"opacity":[op,0.0],"blend":"screen"}
def band(text, y, size=30, skew=-10, full=True, color=DEEP, op=0.94, font=F_SANS, weight=600, tracking=9, tcolor='#FFFFFF'):
    return {"text":text,"font":font,"weight":weight,"size":size,"color":tcolor,"anchor":[0.5,y],"align":"center","tracking":tracking,
            "band":{"color":color,"opacity":op,"pad":[16,56],"skew":skew,"full_width":full}}
def grain(): return {"amount":0.035,"seed":3}
def vig(s=0.32): return {"strength":s,"softness":0.62}
TAG = "RHYTHM  ·  ROOM  ·  RESPONSE  ·  RELAY  ·  RECOVERY"

SPECS = {}
# ---------- EMAIL HEADERS 1800x600 ----------
SPECS['email-header-01'] = {"size":[1800,600],"out":"final/email-header-01.jpg",
  "plate":{"src":"plates/header-morning-nursery.png","fit":"cover","focus":[0.5,0.45]},
  "grade":[{"type":"linear","from":[0,0],"to":[0,1],"color":NAVY,"opacity":[0.18,0.70]}, glow(0.5,0.42,0.5,0.30)],
  "light":[{"type":"rays","origin":[0.08,-0.3],"color":"#FFF1DC","opacity":0.16,"blur":70,"count":6,"seed":4}],
  "emblem":{"src":EMB,"anchor":[0.5,0.42],"height":0.50,"depth":{"shadow":0.5,"glow":LAMP,"glow_opacity":0.45,"rim":True}},
  "text":[band(TAG,0.86,26,-10)], "grain":grain(), "vignette":vig(0.3)}
SPECS['email-header-02'] = {"size":[1800,600],"out":"final/email-header-02.jpg",
  "plate":{"src":"plates/header-mother-window.png","fit":"cover","focus":[0.35,0.5]},
  "grade":[{"type":"linear","from":[0,0],"to":[1,0],"color":NAVY,"opacity":[0.05,0.82]}, glow(0.14,0.5,0.45,0.30)],
  "light":[{"type":"slash","angle":-16,"x":0.405,"width":0.006,"color":LAMP,"opacity":0.95,"blur":2},{"type":"slash","angle":-16,"x":0.405,"width":0.05,"color":LAMP,"opacity":0.35,"blur":26}],
  "emblem":{"src":EMB,"anchor":[0.165,0.50],"height":0.44,"depth":{"shadow":0.5,"glow":LAMP,"glow_opacity":0.4,"rim":True}},
  "text":[{"text":"First 90 Nights","font":F_SERIF,"weight":350,"size":112,"color":MOON,"anchor":[0.69,0.44],"align":"center","tracking":-1},
          {"text":"A CALM, SHARED PLAN FOR YOUR EVENINGS AND NIGHTS","font":F_SANS,"weight":600,"size":22,"color":LAMP,"anchor":[0.69,0.60],"align":"center","tracking":6}],
  "grain":grain(), "vignette":vig(0.3)}
SPECS['email-header-03'] = {"size":[1800,600],"out":"final/email-header-03.jpg",
  "plate":{"src":"ad-bg-e-window-blue-hour.png","fit":"cover","focus":[0.5,0.35],"scale":1.0},
  "grade":[grade_dark(0.1,0.75), glow(0.5,0.45,0.5,0.34)],
  "light":[{"type":"bokeh","count":22,"color":LAMP,"opacity":0.3,"seed":11}],
  "emblem":{"src":EMB,"anchor":[0.5,0.42],"height":0.50,"depth":{"shadow":0.5,"glow":LAMP,"glow_opacity":0.5,"rim":True}},
  "text":[band(TAG,0.86,26,0,False,DEEP,0.94)], "grain":grain(), "vignette":vig(0.34)}
SPECS['email-header-04'] = {"size":[1800,600],"out":"final/email-header-04.jpg",
  "plate":{"src":"hero.png","fit":"cover","focus":[0.75,0.45]},
  "grade":[{"type":"linear","from":[0,0],"to":[0,1],"color":NAVY,"opacity":[0.25,0.72]}],
  "light":[{"type":"slash","angle":-12,"x":0.5,"width":0.19,"color":DEEP,"opacity":0.88,"blur":0,"blend":"normal"},{"type":"slash","angle":-12,"x":0.5,"width":0.19,"color":LAMP,"opacity":0.25,"blur":40}],
  "emblem":{"src":EMB,"anchor":[0.5,0.47],"height":0.58,"depth":{"shadow":0.6,"glow":LAMP,"glow_opacity":0.35,"rim":True}},
  "text":[{"text":"QUIET HOURS","font":F_SANS,"weight":600,"size":22,"color":MOON,"anchor":[0.5,0.90],"align":"center","tracking":10}],
  "grain":grain(), "vignette":vig(0.36)}

# ---------- ADS ----------
ADS = [  # name, plate4:5, plate9:16, hook lines, cta
 ('ad-01-index-card','ad-bg-d-flatlay-routine.png','plates/story-d-flatlay.png',"I had a PhD in\ninfant routines.\nIt didn't help at 3 a.m.",'Free: The Evening Rhythm Guide',True),
 ('ad-02-fewer-decisions','ad-bg-a-nursery-nightlight.png','plates/story-a-nursery.png',"More rules won't\nhelp at 3 a.m.\nFewer decisions will.",'Free printable evening guide',False),
 ('ad-03-give-them-a-job','ad-bg-c-dad-dawn-coffee.png','plates/story-c-dad.png',"He wanted to help.\nNobody gave him\na job.",'The Night Relay, free guide',False),
 ('ad-04-stop-googling','ad-bg-e-window-blue-hour.png','plates/story-e-window.png',"“I stopped googling\nin the dark. That alone\nwas worth it.”",'Marcus, dad of a 7-week-old',False),
 ('ad-05-tonight-smaller','ad-bg-b-hand-sleep-sack.png','plates/story-b-sleepsack.png',"Not the whole month.\nJust tonight.",'Free: The Evening Rhythm Guide',True),
]
for name, p45, p916, hook, cta, light in ADS:
    for fmt,(W,H),plate in (('feed',(1080,1350),p45),('story',(1080,1920),p916)):
        dark = not light
        tcol = MOON if dark else NAVY
        g = [ {"type":"linear","from":[0,1],"to":[0,0],"color":NAVY if dark else LINEN,"opacity":[0.0,0.82 if dark else 0.55]} ]
        if dark: g.append(glow(0.5,0.12,0.6,0.22))
        hook_y = 0.17 if fmt=='feed' else 0.20
        txt = [{"text":hook,"font":F_SERIF,"weight":350,"size":78 if fmt=='feed' else 84,"color":tcol,"anchor":[0.5,hook_y],"align":"center","tracking":-1,"line_height":1.08,"shadow":dark},
               {"text":cta.upper(),"font":F_SANS,"weight":600,"size":22,"color":'#FFFFFF',"anchor":[0.5,0.925 if fmt=='feed' else 0.90],"align":"center","tracking":4,
                "band":{"color":DEEP,"opacity":0.96,"pad":[14,34],"skew":0,"full_width":False}}]
        SPECS[f'{name}-{fmt}'] = {"size":[W,H],"out":f"final/{name}-{fmt}.jpg","plate":{"src":plate,"fit":"cover","focus":[0.5,0.55]},
          "grade":g, "light":[{"type":"bokeh","count":10,"color":LAMP,"opacity":0.22,"seed":5}] if dark else [],
          "emblem":{"src":EMB,"anchor":[0.11,0.925 if fmt=='feed' else 0.90],"height":0.055 if fmt=='feed' else 0.04,"depth":{"shadow":0.4,"glow":LAMP,"glow_opacity":0.3,"rim":False}},
          "text":txt, "grain":grain(), "vignette":vig(0.28)}

# ---------- HERO re-grade (no text, no emblem) ----------
SPECS['hero'] = {"size":[2688,1520],"out":"final/hero.jpg","plate":{"src":"hero.png","fit":"cover","focus":[0.5,0.5]},
  "grade":[{"type":"linear","from":[0,0],"to":[1,0],"color":NAVY,"opacity":[0.45,0.0]},{"type":"linear","from":[0,0.4],"to":[0,1],"color":NAVY,"opacity":[0.0,0.35]}, glow(0.86,0.42,0.35,0.30)],
  "light":[{"type":"rays","origin":[1.05,-0.2],"color":"#FFE9CC","opacity":0.14,"blur":80,"count":5,"seed":9}],
  "grain":{"amount":0.03,"seed":2}, "vignette":vig(0.30)}
# ---------- LEAD MAGNET COVER (title set in code on the blank booklet) ----------
SPECS['lead-magnet-cover'] = {"size":[1792,2240],"out":"final/lead-magnet-cover.jpg","plate":{"src":"plates/cover-blank-booklet.png","fit":"cover","focus":[0.5,0.5]},
  "grade":[{"type":"linear","from":[0,0],"to":[0,1],"color":NAVY,"opacity":[0.0,0.22]}, {"type":"radial","center":[0.78,0.12],"radius":0.7,"color":"#FFF4E2","opacity":[0.22,0.0],"blend":"screen"}],
  "light":[],
  "text":[{"text":"QUIET HOURS","font":F_SANS,"weight":600,"size":24,"color":'#6B6457',"anchor":[0.37,0.375],"align":"center","tracking":9,"rotate":8,"shadow":False},
          {"text":"The Evening\nRhythm Guide","font":F_SERIF,"weight":350,"size":96,"color":NAVY,"anchor":[0.385,0.465],"align":"center","tracking":-1,"line_height":1.02,"rotate":8,"shadow":False},
          {"text":"A calm, printable plan for your\nbaby's evenings and nights","font":F_SERIF_I,"weight":350,"size":31,"color":'#4A5368',"anchor":[0.395,0.575],"align":"center","line_height":1.25,"rotate":8,"shadow":False},
          {"text":"DR. LENA PARK","font":F_SANS,"weight":600,"size":22,"color":MOON,"anchor":[0.40,0.80],"align":"center","tracking":10,"rotate":8,"shadow":False}],
  "emblem":{"src":EMB,"anchor":[0.37,0.315],"height":0.05,"depth":{"shadow":0.25,"glow":LAMP,"glow_opacity":0.0,"rim":False}},
  "grain":{"amount":0.025,"seed":5}, "vignette":vig(0.22)}

if __name__ == '__main__':
    only = sys.argv[1:]
    for k,v in SPECS.items():
        if only and k not in only: continue
        json.dump(v, open(os.path.join(EX, k+'.json'),'w'), indent=1)
        img = comp.build(v, HERE); out = os.path.join(HERE, v['out']); img.save(out, quality=94); print('built', k, img.size)
