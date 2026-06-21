---
name: exodus-protocol
description: Skill to handle system backups and sanitization for open source export. Uses the exodus_engine.py script to execute fullride (private) or opensource (public/sanitized) operations safely.
---

# Exodus Protocol Skill

This skill automates the heavy-lifting of backing up Conclave.

## Script Path
`_conclave/skills/exodus-protocol/scripts/exodus_engine.py`

## Usage Modes

### Mode 1: Fullride (Private Backup)
Runs a complete backup of the repository, pushing to the private GitHub remote `main` branch. It strictly enforces the GH001 rule (no files > 100MB) before staging.
**Command**:
```bash
python3 _conclave/skills/exodus-protocol/scripts/exodus_engine.py --mode fullride
```

### Mode 2: Open Source (Sanitized Export)
Clones and sanitizes the core repository structure into a clean `_export_opensource/` directory. It aggressively strips API keys, user identifiers (<user_name>, <user_name>), erases memory files, and removes private squads and environment directories (`ambientes/`, `references/`).
**Command**:
```bash
python3 _conclave/skills/exodus-protocol/scripts/exodus_engine.py --mode opensource
```

## Security Protocol
- NEVER run `fullride` if the user specifies open source or public export.
- Always use the script; never run raw `git add . && git commit` for backups manually again, as the script provides bounds checking and memory sanitation.
