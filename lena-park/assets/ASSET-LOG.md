# Asset Generation Log

Generator: Higgsfield MCP, model `gpt_image_2_5`, quality `high`, resolution `2k`.
Cost: 11 generations at 2.75 credits each (30.25 credits total).
Full-resolution PNGs are in this folder. Compressed 1600px JPGs for the web are in `/web`.

| File | Ratio | Job ID | Status | Notes |
|---|---|---|---|---|
| logo-concept.png | 1:1 | 0991ddd7-ce70-484e-97fd-7b1efb8e94fb | OK | Wordmark and emblem rendered cleanly. The pages use a vector SVG redraw so the logo stays crisp. |
| hero.png | 16:9 | 60c10d70-3bf7-4cb4-ab05-bba4d9b21cb8 | OK | Mother holding a sleeping newborn at blue hour. Baby is held by a parent who is awake, not asleep in bed. |
| lead-magnet-cover.png | 4:5 | efc7b6a6-8ad3-4fee-a25e-a63a74d0a790 | OK | All cover type is spelled correctly. |
| ad-bg-a-nursery-nightlight.png | 4:5 | f45caa47-1a2b-4706-bd95-f710f00f6c39 | OK | Empty crib with a bare fitted sheet, which matches safe-sleep guidance. |
| ad-bg-b-hand-sleep-sack.png | 4:5 | b9b97aab-5f50-4709-ae73-e7feba92a5ba | OK (v2) | Baby on its back in an empty crib, wearing a sleep sack. |
| ad-bg-c-dad-dawn-coffee.png | 4:5 | 46d07fb5-7939-444d-9992-b27ceb1fe854 | OK | The baby monitor has a slight lavender tint. Acceptable. |
| ad-bg-d-flatlay-routine.png | 4:5 | ece8639e-0ff3-4a75-b180-1b22829d005e | OK | The handwriting reads "bath feed book song". |
| ad-bg-e-window-blue-hour.png | 4:5 | 1e420e9b-af74-4af0-9102-6aca9a4ce1aa | OK (v2) | Only the crib rail is visible. |
| portrait-lena.png | 4:5 | 463e03fc-423d-46da-87a5-2ca162bd3cc9 | OK | Added during Phase 3. The reference layout calls for a coach portrait in the About section. This is a fictional person, so there is no likeness risk. |

## Failed calls
None. All 11 submissions completed.

## Rejected outputs (self-QA, regenerated)
The model rendered both of these without errors. They were rejected in self-review because they break the brand's safe-sleep rule.

| Rejected file | Reason |
|---|---|
| rejected/ad-bg-b-v1-adult-bed-unsafe.png | Baby asleep on an adult bed with loose bedding. This contradicts AAP safe-sleep guidance and would be a credibility risk for a pediatric sleep brand. |
| rejected/ad-bg-e-v1-toy-in-crib.png | Soft toy visible inside the crib. Same issue. |

**Process recommendation:** add a "safe-sleep visual check" to the QA checklist for every niche with a regulated or safety-sensitive subject. Image models default to cozy over correct.

## Derived files
- `the-evening-rhythm-guide.pdf`: the lead magnet exported from `pages/lead-magnet.html` as 5 US Letter pages, checked to fit with no overflow.
- `quiet-hours.tokens.json`: the brand system and single source of truth. `pages/_src/quiet-hours.css` implements it.
