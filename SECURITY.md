# Security notes

No app can honestly be "unhackable", but this one is built to keep the attack surface small.

## What protects the app
- **No server, no dependencies, no third-party scripts.** Nothing to breach or supply-chain attack.
- **Strict Content-Security-Policy** (in `index.html`): only the app's own hashed script/style may run; the only network destination allowed is Google Apps Script. Injected scripts are blocked by the browser.
- **All output is HTML-escaped; all incoming data is validated** (import, backup, diary file, Google Sheet reply): types, lengths, status whitelist, safe IDs.
- **Sync can only add/update, never wipe** local data; requests send no cookies and no referrer.
- **CSV export neutralises spreadsheet formulas** (`=`, `+`, `-`, `@`).
- No secrets are stored in this repository.

## After editing index.html
Run `python3 tools/update-csp.py` to refresh the policy hashes (otherwise the browser blocks the app).

## What you must do yourself (cannot be fixed in code)
1. **Turn on 2-factor authentication** for your GitHub and Google accounts. This is the biggest real-world protection.
2. **Google Sheet / Apps Script:** the `/exec` URL is effectively a password. Never share or post it. Deploy it as "Execute as: Me" and rotate it (new deployment) if it ever leaks. Ideally also have the script reject requests lacking a secret you add.
3. **Data is stored unencrypted in the browser and in the diary/backup files.** Use a device with a screen lock/disk encryption, do not use this on shared computers, and keep backup files private.
4. If this repo is public, the code is public (fine) - but never commit exported data (`.gitignore` helps).
5. GitHub: enable branch protection, secret scanning and Dependabot alerts in repo Settings.
