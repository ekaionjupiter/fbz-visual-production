"""Build self-contained pages: inline quiet-hours.css and embed images as base64.
Source: pages/_src/*.html   Output: pages/*.html
Run: python3 pages/_src/build.py
"""
import base64, re, pathlib
SRC = pathlib.Path(__file__).resolve().parent
OUT = SRC.parent
ASSETS = OUT.parent / "assets"
css = (SRC / "quiet-hours.css").read_text()
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".svg": "image/svg+xml"}
cache = {}
def data_uri(rel):
    p = (SRC / rel).resolve()
    if p not in cache:
        cache[p] = f"data:{MIME[p.suffix.lower()]};base64," + base64.b64encode(p.read_bytes()).decode()
    return cache[p]
for f in sorted(SRC.glob("*.html")):
    html = f.read_text()
    html = html.replace('<link rel="stylesheet" href="quiet-hours.css">', f"<style>\n{css}\n</style>")
    html = re.sub(r'((?:src|href)=")(\.\./\.\./assets/[^"]+)(")', lambda m: m.group(1) + data_uri(m.group(2)) + m.group(3), html)
    html = re.sub(r"(url\(['\"]?)(\.\./\.\./assets/[^'\")]+)(['\"]?\))", lambda m: m.group(1) + data_uri(m.group(2)) + m.group(3), html)
    (OUT / f.name).write_text(html)
    print(f"built {f.name:28s} {len(html)/1024:8.0f} KB")
