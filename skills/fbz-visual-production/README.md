# fbz-visual-production

Claude Code skill that turns the FBZ Visual Production Doctrine (14 videos, merged) into a repeatable pipeline: references, Higgsfield plates, emblem depth, compositing in code, Impeccable scan, side-by-side QA.

Install into any Claude Code workspace:

```bash
npx skills add ekaistone/fbz-visual-production -a claude-code -y
```

or copy `skills/fbz-visual-production/` into `.claude/skills/`. Requires python3 with Pillow + numpy (`pip install pillow numpy`), node for `npx impeccable`, and the Higgsfield MCP connected.
