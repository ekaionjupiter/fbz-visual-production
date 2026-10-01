# Lena Park POC: $2,000 Pre-Launch Build (AI-only)

Fictional client: Dr. Lena Park, Quiet Hours (pediatric sleep). First product: **First 90 Nights**.
Status: Phases 0 to 4 are complete. **Pushed to Figma on 2026-09-30:** https://www.figma.com/design/ra0Qa4ZIzzJrbbU1UPyg7u

## Figma file structure
| Page | Contents |
|---|---|
| Cover | Title card and file index |
| Foundations | Brand board. Variables: Primitives (22 colors), Theme (19 semantic colors in Light and Dark modes), Space & Radius (23). 21 text styles and 2 effect styles. |
| Components | 13 components: Logo, Button (3 variants), Eyebrow, Input Field, Chip, List Item, Quote Card, Pillar Card, Value Box, FAQ Item, Step Card, Credential, Footer. All are bound to the variables. |
| Desktop (1440) | Waitlist Sales Page, Thank-You Page, Offer Cart, Doors-Open email (600px), Lead Magnet print sheets (5 sheets, US Letter) |
| Mobile (390) | Waitlist Sales Page, Thank-You Page, Offer Cart |
| Assets | The 9 Higgsfield images, used as image fills |

Every page is built from editable text and component instances. There are no flattened screenshots. Page 1 ("Pre-Launch Kit") is now a single canvas with every deliverable in a grid; Foundations, Components and Assets are the back pages.

## Image upgrade (fbz-visual-production skill)
All hero, cover, email-header and ad images were rebuilt as layered composites (Higgsfield plate + grade + light + brass emblem with depth + type in Fraunces/DM Sans + grain + vignette). Finals: `assets/final/`. Build script: `assets/build_assets.py`. Log and scores: `assets/ASSET-LOG.md`.

## Delivery
Drive: "Mid Ticket Storage / Lena Park - Pre-Launch Kit" (https://drive.google.com/drive/folders/1Kx67WVSSlSXiAikEPmHoAHaT4b0s-W9c), subfolders 00 to 08. Binder docs are Google Docs; renders, HTML, PDF and images are native files.

## Where everything lives

| Folder | Contents |
|---|---|
| `intake/` | The synthetic Playbook answers, the OTO questionnaire and a 21-minute extraction-call transcript. This is the only input the rest of the build used. |
| `binder/` | `01-master-offer-doc.md` (about 9.1k words), `02-master-copy-suite.md` (about 10.1k words, 7 tabs), `03-program-curriculum.md` (about 7.1k words, 23 lessons, 7 printables) |
| `assets/` | `quiet-hours.tokens.json` (the brand system), 9 Higgsfield images (PNG, plus web JPGs in `web/`), `the-evening-rhythm-guide.pdf`, `ASSET-LOG.md`, and `rejected/` |
| `pages/` | 6 self-contained HTML files with CSS and images inlined. Sources are in `pages/_src/`. Rebuild with `python3 pages/_src/build.py`. |
| `pages/_src/REFERENCE-LAYOUT.md` | Section order, spacing and component patterns taken from the Leonel Salas Figma reference |
| `renders/` | Final PNGs: mobile (390px) and desktop (1440px) for every page, plus dark-mode renders of the sales and thank-you pages |

## QA performed
- Every page was rendered, reviewed visually, fixed and rendered again, in 4 passes. Every final render has zero horizontal overflow.
- WCAG contrast was checked for every color pair. Primary button: 4.69:1. Dark-mode accent text was fixed (it was about 3:1, now 6.87:1).
- The guide PDF was checked under print media. All 5 Letter pages fit with no overflow.
- Compliance sweep: zero em or en dashes, no banned phrases, no invented statistics. Only the 6 approved testimonials are used, verbatim.
- Two images were rejected and regenerated because they violated AAP safe-sleep guidance (see `assets/ASSET-LOG.md`).

## Open items for the client
These are consolidated from the binder's sign-off lists:
- 1:1 credit amount: $97 or $147.
- Whether testimonial permission covers paid ads.
- Publishing her children's names.
- AAP wording and source for the Room Checklist.
- Delivery platform.
- [DOMAIN] and [LINK] placeholders.
