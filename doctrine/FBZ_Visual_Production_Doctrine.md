# FBZ Visual Production Doctrine

Merged from 14 YouTube videos (full descriptions + cleaned transcripts in `videos/`). Built 2026-09-30 for Freedom Builderz so image, logo, header, ad, motion and page work ships at the Leonel Salas production bar without re-prompting. The operational version of this doctrine is the Claude Code skill at `skills/fbz-visual-production/SKILL.md`.

Videos: 01 Chase AI · 02 Viktor Oddy · 03 AI Master · 04 Jack Roberts · 05 Jack Roberts · 06 Metics Media · 07 Liam Ottley · 08 Joseph Martin · 09 Jack Roberts · 10 Higgsfield (Adil) · 11 Kristian Jennings · 12 Nate Herk · 13 Nate Herk · 14 Open Residency (Remy Gaskell).

---

## PART 1: THE RULES (ranked by how many of the 14 videos agree)

### Tier 1: said in 8 or more videos

1. **Reference first, never a text prompt alone.** Every asset starts from 2 to 3 reference images (layout, mood, object). "Hand it a reference instead of a pile of adjectives"; "one image carries a palette better than a paragraph full of words like premium and clean" (03). "Show, not tell" (04). References come from Pinterest (02, 01; note 11 says Pinterest is now full of AI slop for UGC, use real TikTok/IG/FB creators instead), Dribbble, Mobbin (07), Godly/Land-book/Awwwards (04), the client's own photos (06, 07, 14), and screenshots of real brand sites (09). Prompt pattern: "match the feel, not the content." [01, 02, 03, 04, 06, 07, 09, 11, 12, 14]

2. **Never one-shot. Generate wide, pick, narrow, tweak.** 5 directions on one screen, pick one, 3 variations of it, pick, then tweak fonts/colors/components (01). "Give me 10 concepts, I like that one, give me five more like that" (07). "Generate a hundred, there'll be maybe five to ten really good ones" (14). 2 to 4 variants per image (04). Storyboard before spending video credits (10). [01, 04, 06, 07, 09, 10, 12, 14]

3. **Fonts are the number-one AI tell.** "Fonts are Dr. Slop, the biggest giveaway" (05). "Never Inter" (01). "Claude will get the fonts very wrong" (02): identify the font yourself (Google Fonts, Fontshare, Fonts In Use, Typewolf), name it in the brief, import it from Google Fonts, and for a long-term brand buy it. "Always ask for the design sheet in HTML, fonts arrive way better that way" (10). [01, 02, 04, 05, 09, 10, 12, 14]

4. **The model makes the plate; code makes the type and the logo.** Image models melt and misspell text and warp logos (03, 10). Generate backgrounds and subjects only ("remove all text, buttons, icons, circles, no logo" 02), then set type, emblem, bands and CTAs in code or in the design tool. Motion test: "if the model can't hold a word still on a flat sheet, it won't hold a lower third" (03). [02, 03, 05, 10, 11, 12, 14 + FBZ Leonel analysis]

5. **Split every reference composite into plate + cutout + layout.** Viktor Oddy's split: "create me an image exactly like this in 4K/8K, remove all text, buttons, icons, circles, no logo" (background only) and "text position the same way, remove the background, plain black background" (layout only). Cutouts on pure black get background-removed and used as absolute-positioned section dividers (02). The same split is how Leonel's headers are built (photo plate, slash, emblem, band). [02, 04, 06, 10, 12]

6. **Install the design skills and name them in the prompt.** Impeccable (23 commands, 46 slop patterns catalogued, CLI scan; 01), Taste Skill v2 (01, 09), ui-ux-pro-max, frontend-design, awesome-design-skills, gsap-skills (04), ScrollCraft and HyperFrames (12), Higgsfield's own motion prompt skill (10), the "10K Website Skill" (06). "Use all the best skills and design principles" (04). Avoid narrow prescriptive skills and 10,000-page design.md files (01). [01, 04, 05, 06, 09, 10, 12, 14]

7. **Codify every correction into a skill, then iterate the skill.** "If you ever find yourself repeating something, throw it in the skill" (12). "When I'm building a chart, use this exact style for all future charts" (05). "Create a skill for this process we've just done"; skills are V5 to V10 before they are good; memory.md records every correction as a rule (14). "I really liked this and didn't like this. Update the skill" (12). [05, 09, 12, 13, 14]

8. **Higgsfield MCP is the image/video engine inside Claude.** Connect via Claude > Settings > Connectors > Add custom connector > paste the URL from Higgsfield's "MCP and CLI" page > OAuth (01, 03, 06, 07, 10, 14). "The Composio for image models" (14). Let Claude "explore the MCP and figure out which models work best" (07). [01, 03, 06, 07, 08, 10, 14]

### Tier 2: said in 4 to 7 videos

9. **Resolution: 2K for hero and section art, 4K for plates you will crop or upscale. 1K is too low; 4K is wasteful for web.** (02, 04, 06, 09)

10. **Real beats generated.** Real client photos, real logos, real products, real data. "You have to have media of your own" (07). Generated product shots squish the product; supply the real product image (14). Real iPhone still for UGC avatars; "AI always takes the aggregate" so pure prompts produce generic faces (11). Firecrawl the brand site for logos, fonts and colors before generating anything (05, 14). [05, 06, 07, 11, 14]

11. **Motion rules: "animate this, no zoom in or zoom out" (02), name the one thing that must not move ("the product keeps its exact shape" 03), describe the outcome like a director, not the technique (03), explicit camera ("static locked off shot" / "handheld UGC iPhone shot" 11), one continuous take, no cuts (03, 11, 13), start frame = end frame for a seamless loop (04).** [02, 03, 04, 08, 10, 11, 13]

12. **Remove the AI tells in UI: no card fills different from the background (stroke only or none), no unnecessary dividers, no purple gradients, no 3D SaaS blobs, no eyebrow-chip-over-giant-headline, no side-tab accent borders.** (01, 02, Impeccable's 61 rules) Buttons are "extremely important" (02). [01, 02, 04, 09]

13. **Critique loop against the reference before shipping.** "Compare it with mine. Be ruthless" against Linear/Apple screenshots (09). Design-loop skill with 3 critic sub-agents (brief, design quality, visual impact) until it hits the mark (09). Chrome DevTools MCP as a visual QA loop (14). Agent screenshots its own render and iterates (12). Final quality pass + mobile check mandatory (06). [04, 06, 09, 12, 14]

14. **Layer external assets Claude cannot synthesize: icon packs (one style per piece), Lottie JSON, real illustrations, legibility layers (liquid-glass card or dark overlay behind every overlaid element).** (05, 12) [05, 10, 12]

15. **Intent + guardrails in every brief: what, why, audience, action, plus "always / never" lines.** Chase AI: "never purple gradients, never Inter, no 3D SaaS blobs." Remy: "Assumptions are the enemy. If the answer isn't there, ask me." [01, 09, 13, 14]

### Tier 3: single-source but adopted by FBZ

16. **UGC realism (11):** one-shot the avatar prompt (iterative edits create feathered overlays that surface when animated); start from a real creator still with both hands visible, no blown highlights, background with depth; change identity enough that it could not be the same person; Nano Banana Pro original (not 2) for baked-in imperfections; never GPT Image for faces ("too perfect"); CAPITALISE a word to stress it in dialogue.
17. **Motion graphics (03, 10):** test the model on melting text, drift, and composition loss before trusting it; storyboard 9 frames first; fix at the image stage; HTML design sheet before video; "one wrong number and the whole video goes in the trash."
18. **Web (02, 04, 06, 07):** hero first, then transition, then body; scroll-scrubbed hero video from a start frame is what makes sites "feel expensive"; concepts must be physically continuous top to bottom; headline shrinks 30% and body 10 to 15% when generated art makes legibility suffer; mobile is a separate pass.
19. **Pipelines (13, 14):** proof-then-final (3 proofs at 1024, confirm, render finals at 2048); sub-workflows hold no AI step, only binary handling; manager agents call tools, they do not write; start read-only and escalate permissions; money-spending tools last.

---

## PART 2: THE FBZ LAYER RECIPE (how Leonel-grade assets are actually built)

Every composite, in this order, in code (Pillow via `scripts/composite.py`) or in Figma:

1. **Plate**: photoreal background from Higgsfield (GPT Image 2.5 "high" 2K for stills; Nano Banana Pro for products and people). No text, no logo, no UI in the prompt. 35mm grain, real skin, lived-in rooms. Compliance checks live here (for FBZ health niches: safe-sleep, no medical claims).
2. **Grade**: brand color gradient, 40 to 75% opacity, navy-to-transparent for calm brands, red/black for performance brands; one radial warm light where the lamp or the emblem sits.
3. **Light**: a diagonal highlight slash, soft rays from a corner, or bokeh. One treatment per asset.
4. **Emblem with depth**: the vector logo rendered with a material (brushed metal, ceramic, enamel), soft shadow, rim light, 30 to 45% glow in the brand accent. Depth render comes from Higgsfield image-to-image on the clean SVG; the clean SVG is also kept.
5. **Type band**: tagline or headline set in the named brand fonts, on a skewed band or a solid strip, with a soft drop shadow for legibility.
6. **Grain 3 to 5% + vignette 25 to 40%.**

Then: `scripts/slop_check.sh` (Impeccable detect on HTML + render checks), side-by-side with the Leonel reference tiles, score 1 to 5, anything under 4 gets one more pass.

---

## PART 3: THE STACK (what is installed, what is free, what costs money)

| Tool | Role | Cost | Status |
|---|---|---|---|
| Higgsfield MCP | image + video + motion engine (GPT Image 2.5, Nano Banana Pro, Seedance 2.5, Kling 3.0, Veo 3.1, Cinema Studio) | paid credits, already connected | installed |
| Impeccable (pbakaus/impeccable) | 23 design commands + 61-rule deterministic slop detector CLI | free | installed in `.claude/skills/impeccable` |
| Taste Skill (Leonxlnx/taste-skill) | design-taste-frontend v2, high-end-visual-design, image-to-code, redesign-existing-projects | free | installed in `.claude/skills/` |
| fbz-visual-production (this doctrine) | FBZ composite pipeline + rules | free | `skills/fbz-visual-production` |
| Pillow + numpy | compositing in code | free | installed |
| Fraunces, DM Sans (Google Fonts) | FBZ calm-brand type | free | `skills/fbz-visual-production/fonts` |
| Figma MCP | editable deliverables, library, Code-to-Canvas | on Kai's team plan | connected |
| Firecrawl MCP | scrape brand identity (logos, fonts, colors) from client sites | free tier, paid above | not installed |
| Mobbin | finished big-brand site references + MCP | ~$20/mo | not bought |
| 21st.dev | component search + copy-prompt | ~$9/mo | not bought |
| Flaticon icon packs | one-style icon sets | ~$8/mo | not bought |
| HyperFrames + ScrollCraft | HTML motion graphics / video editing skills | free | not installed (video work only) |
| Kie.ai / OpenRouter / fal.ai | alternate image/video APIs (Omni, Veo via API) | pay as you go | not needed while Higgsfield is connected |
| n8n media-agent army template | Telegram-driven generation pipeline | free template | not installed |

---

## PART 4: PROMPT PATTERNS (verbatim, reusable)

See `skills/fbz-visual-production/references/prompt-patterns.md` for the full set. The core ones:

- Plate: "Create an image exactly like this in 4K. Remove all text, buttons, icons, circles. No logo." (02)
- Layout: "Keep the text position the same way, remove the background, plain black background." (02)
- Remix: "Replace all content to be around [niche]. Remove the navbar. Add the [element] from the second and third images across the hero. Background the same as the first image." (02)
- Color pass: "Apply this color reference: dark gradient, dark mode. Do not add the yellow circle." (02)
- Motion: "Animate this. No zoom in or zoom out." (02) / "[Object] cannot change shape or shift position." (03)
- Outpaint: "Turn these portrait stills into widened 16x9 footage." (07)
- Concepts: "Give me 10 different concepts. I like that one, give me five more like that in different variations." (07)
- Critique: "Compare it with mine. I want you to be ruthless. Output a concise HTML breakdown." (09)
- Brand extraction: "Go to this website, understand the typography and design, and give me an extraction blueprint so I can build something that levels this up." (04)
- Skill capture: "Create a skill for this process we just did." / "Update the skill: I liked X, I did not like Y." (12, 14)

---

## PART 5: SOURCES

Per-video files (verbatim description with links, key takeaways, full cleaned transcript):

01 `videos/01-7FU98O0JLHs.md` Chase AI, Turn Claude Into A Design GENIUS In 3 Simple Steps
02 `videos/02-5ZAsjUoMx1Y.md` Viktor Oddy, Build $50,000 Websites Using Claude Fable 5
03 `videos/03-FgTLSKXOCBE.md` AI Master, Claude + Higgsfield: Motion Graphics with AI
04 `videos/04-AFRL9dtUHeI.md` Jack Roberts, Claude Fable 5 Builds $10,000 Websites in 21 mins
05 `videos/05-RDytbVDzMF4.md` Jack Roberts, Claude Design FINALLY Solved Motion Graphics
06 `videos/06-snErQUyqwCU.md` Metics Media, How to Build $10K Websites in Minutes
07 `videos/07-1P5xtV-Kf0o.md` Liam Ottley, Claude Fable 5.1 + Higgsfield = Insane $10K Websites
08 `videos/08-AlJWfhAIrOI.md` Joseph Martin, I Mixed Higgsfield with Claude Opus 5.5
09 `videos/09-NAumQObJEwM.md` Jack Roberts, Turn Claude into a Design Genius... Just Watch
10 `videos/10-2OwMjg5As2g.md` Higgsfield, Claude Fable 5.1 + Higgsfield AI = Insane Motion Graphics
11 `videos/11-kvf2lRSGixg.md` Kristian Jennings, How I Make AI UGC Ads Look 100% Real
12 `videos/12-7jHXoPGnA4c.md` Nate Herk, Opus 5.5 Just Changed Video Editing Forever
13 `videos/13-jBanaNBY-sM.md` Nate Herk, I Built the Ultimate Army of Media Agents in n8n
14 `videos/14-5p-sq8v3OXw.md` Open Residency, AI Agents: The Most Valuable Skill You Can Learn in 2026
