# FBZ_Claude_Code

Freedom Builderz production workspace. Kai Stone (kai@ekaistone.com) runs it; Mike and Miles are the partners who judge output.

## Always
- Replies to Kai: 2 sentences maximum. A build ends with `DONE`, then at most 2 sentences needing attention, then any message he asked for. Put detail in files, not chat.
- Any image, header, ad, logo, hero, cover, brand or motion work: load `skills/fbz-visual-production/SKILL.md` first and follow it. The "creative doctrine" (also called the visual doctrine) is `doctrine/Visual_Production_Doctrine.md`; when Kai says "creative doctrine" he means that file.
- Any page or UI work: also use `.claude/skills/impeccable` and `.claude/skills/design-taste-frontend`; run `npx impeccable detect <html>` before shipping.
- Quality bar: the Leonel Salas Figma (`UVmXkMR8Qc57lPf6kJ3WE7`, node `7:233`). Match production value, never its brand.
- Copy rules: no em or en dashes, no invented statistics, no medical claims, no urgency timers.
- Client deliverable naming: `[First] [Last] - Pre-Launch Kit` (Drive folder in "Mid Ticket Storage", id `1p8YwyYd5HBulX0ug1MCABpN_FVtH-mZu`; Figma file of the same name).

## Layout
- `lena-park/` POC client build (intake, binder, assets, pages, renders)
- `skills/fbz-visual-production/` the visual production skill (scripts, fonts, references)
- `doctrine/` the merged 14-video doctrine + per-video transcripts
- `.claude/skills/` third-party skills (impeccable, taste-skill)
