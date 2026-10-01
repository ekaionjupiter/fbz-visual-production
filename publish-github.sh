#!/usr/bin/env bash
# One-time: publish this workspace (skill + doctrine + POC) to GitHub.
# Needs: ~/.local/bin/gh (installed) and a login. Run:  gh auth login   (browser flow), then:  ./publish-github.sh
set -e
export PATH="$HOME/.local/bin:$PATH"
cd "$(dirname "$0")"
gh auth status >/dev/null 2>&1 || { echo "Run: gh auth login"; exit 1; }
gh repo view fbz-visual-production >/dev/null 2>&1 || gh repo create fbz-visual-production --private --source=. --remote=origin --description "Freedom Builderz visual production skill + 14-video doctrine" 
git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$(gh api user -q .login)/fbz-visual-production.git"
git branch -M main
git push -u origin main
echo "pushed: $(gh repo view --json url -q .url)"
