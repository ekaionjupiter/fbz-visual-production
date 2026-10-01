#!/usr/bin/env bash
# slop_check.sh: mandatory pre-ship scan.
# 1) Impeccable deterministic detector on every HTML page in the target (61 anti-pattern rules, no API key).
# 2) Pixel checks on every PNG/JPG render: size, flat-image tell (low layer variance), text-in-plate OCR not available so we flag by metadata only.
# Usage: slop_check.sh <dir-or-file> [--json]
set -u
T="${1:-.}"; JSON="${2:-}"
echo "== Impeccable detect: $T =="
if ls "$T"/*.html >/dev/null 2>&1 || [[ "$T" == *.html ]]; then
  npx -y impeccable detect "$T" ${JSON:+--json}; RC=$?
  echo "impeccable exit code: $RC (0 clean, 2 findings, 1 scan failure)"
else
  echo "no HTML in target, skipping Impeccable"
fi
echo "== Render checks =="
python3 - "$T" <<'EOF'
import sys, os, glob
from PIL import Image
import numpy as np
t=sys.argv[1]; files=[t] if os.path.isfile(t) else sorted(glob.glob(os.path.join(t,'**','*.png'),recursive=True)+glob.glob(os.path.join(t,'**','*.jpg'),recursive=True))
bad=0
for f in files:
    try: im=Image.open(f).convert('RGB')
    except Exception as e: print('SKIP',f,e); continue
    a=np.asarray(im.resize((256,int(256*im.size[1]/im.size[0]) or 1))).astype(float)
    lum=a.mean(axis=2); contrast=lum.std(); sat=(a.max(axis=2)-a.min(axis=2)).mean()
    flags=[]
    if im.size[0]<1000: flags.append('low-res (<1000px wide)')
    if contrast<28: flags.append('flat tonal range (no depth/grade)')
    if sat>95: flags.append('oversaturated')
    print(('FLAG ' if flags else 'ok   ')+os.path.relpath(f,t if os.path.isdir(t) else os.path.dirname(t))+(' :: '+', '.join(flags) if flags else ''))
    bad+=bool(flags)
print(f"{len(files)} renders checked, {bad} flagged")
EOF
