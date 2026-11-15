# Project summary

**Last updated:** 2026-11-15, branch `ccr-4831413b-t37f3q`, commit `34321b7`

## What this project is
"Daily Task Register": a personal task diary for procurement work (who assigned a task, what was asked, PR/PO/WO references, status, and what was done). It is a single HTML file that runs in the browser with no server. Data is saved in browser storage, optionally mirrored to a linked file or a Google Sheet through an Apps Script URL.

## Structure
- `index.html`: the whole app (HTML, CSS and JavaScript in one file)
- `SECURITY.md`: security notes and the owner's manual steps
- `tools/update-csp.py`: recalculates the Content-Security-Policy hashes. Run it after any change to the inline script or style.
- `.gitignore`: keeps backups, exports and secrets out of git
- `.claude/agents/project-memory.md`: this memory agent
- `.claude/memory/`: memory files (this summary)

## Current state
- Working: add, edit, archive and restore entries; status cycling; search and filters; import from JSON; CSV and text export; JSON backup; undo; linked diary file; optional Google Sheet sync.
- Security hardening is committed on this branch: strict Content-Security-Policy, input validation on every data source, CSV formula guard, and merge-only sync.
- Not yet verified: a real browser check of the Google Sheet sync and the diary file link on Chrome or Edge.

## Recent changes
- `34321b7` Harden app: strict CSP, input validation, CSV formula guard, safer sync (this branch, pushed to origin, not merged)
- `9052034` Update index.html
- `ffe2a35` Update and rename task-tracker final.html to index.html
- `79464cf` Add files via upload

## Open decisions
- Merge branch `ccr-4831413b-t37f3q` into `main`?
- The repo is public and `index.html` contains real-looking sample data (names, PR numbers, "TTIPL"). Make the repo private, replace the sample data with fake examples, or both?
- Undo and the file-permission error after linking a diary file are still open bugs (see the brief, not yet fixed).

## Known risks
- Sample business data is in `index.html` in a public repo.
- Stored data is unencrypted in the browser and in backup files.
- The Google Sheet URL works as a password. Anyone who has it can read and write the sheet.
- A diary file link can stop the page loading if the browser rejects the permission prompt (`index.html`, `linkFile` / `restoreHandle`).

## Where to look for detail
- Security steps for the owner: `SECURITY.md`
- Hash update procedure: `tools/update-csp.py`
- Full change history: `git log`
- Sister project (TTIPL site tracker, not in this repo): change brief kept in the user's scratchpad, not in this repo
