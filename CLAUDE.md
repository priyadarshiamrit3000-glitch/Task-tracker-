# Instructions for every agent working in this repo

## Start of every session
1. Read `.claude/memory/PROJECT_SUMMARY.md` before doing anything else.
2. If the summary's "Last updated" commit is not the current `git rev-parse --short HEAD`, read the `git log` since then and treat the summary as a starting point, not the truth.
3. Only open other files when the task needs them.

## Keeping the summary current
- After a significant change, update `.claude/memory/PROJECT_SUMMARY.md` (or ask the `project-memory` agent to do it).
- Keep it short. Facts only. No secrets or personal data.

## Rules
- Commit and push only when the user asks, and only to the designated branch, never to `main`.
- Do not create pull requests unless asked.
