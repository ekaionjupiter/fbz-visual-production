# Reference Library (template)

Every asset starts from 3 references. Never from a text prompt alone. Fill one block per asset type per client and keep it in `<client>/assets/refs/`. A reference tells the model "match the FEEL, not the content".

| Slot | What it carries | Where it comes from |
|---|---|---|
| LAYOUT | where the headline, emblem, band and CTA sit; whitespace; crop | Leonel Salas email headers, the FBZ Figma library, a Pinterest/Dribbble tile, a Mobbin screenshot |
| MOOD | palette, light, grade, grain, era, lens | one photo or film still; "one image carries a palette better than a paragraph" |
| OBJECT | the exact product, mascot, emblem, prop that must not change shape | the client's real photo, the vector logo, the 3D render |

## Per-asset-type defaults (FBZ)

### Email header (1800x600)
- LAYOUT: Leonel Salas header set (4 tiles): emblem centered on a vertical red slash; emblem left + headline right; ring-ropes plate with centered emblem; band of tagline under emblem.
- MOOD: dusk/lamplight for calm brands; smoke + rim light for performance brands.
- OBJECT: the client emblem rendered with depth (see `emblem-depth` recipe).

### Hero (16:9, 2K to 4K)
- LAYOUT: subject on the right third, copy on the left; or full-bleed with a dark grade on the copy side.
- MOOD: one real photo from the client, or one film still.
- OBJECT: the product or the person. Never generate the person if a real photo exists.

### Ad creative (1080x1350 feed, 1080x1920 story)
- LAYOUT: top third quiet for the hook, emblem small bottom-left, CTA chip bottom-right.
- MOOD: match the feed the ad runs in (UGC-real, not glossy).
- OBJECT: the real product shot (supply it; the model squishes products it invents).

### Lead-magnet cover (4:5)
- LAYOUT: printed-object still life (booklet on a surface) or a flat cover with a title band.
- MOOD: paper texture, soft window light.
- OBJECT: the emblem + the exact title (set in code, never generated).

### Logo emblem
- LAYOUT: vector SVG is the source of truth.
- MOOD: a material reference (brushed metal, ceramic, enamel, foil) from a real photo.
- OBJECT: the SVG itself, fed as image reference for image-to-image depth rendering.

## Aesthetic families (name one per brief, from Chase AI's taste library)
print-tech-paper · dither-mono · vast-quiet · classical-remix · data-as-texture · lamplight-editorial (FBZ calm brands) · ring-and-smoke (FBZ performance brands)

## How to log a reference
```
refs/
  header-layout-01.jpg   # source: Leonel Salas Figma, node 7:233, tile 2
  mood-dusk-nursery.jpg  # source: Higgsfield plate 2026-09-30, job f45caa47
  object-emblem.svg      # source: assets/quiet-hours-emblem.svg
```
Write the source next to every file. A reference without a source gets deleted.
