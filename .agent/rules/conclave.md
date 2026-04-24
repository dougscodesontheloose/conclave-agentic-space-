---
name: conclave
---

# Conclave — Project Instructions

This project uses **Conclave**, a multi-agent orchestration framework.

## Quick Start

Type `/conclave` to open the main menu, or use any of these commands:
- `/conclave create` — Create a new squad
- `/conclave run <name>` — Run a squad
- `/conclave help` — See all commands

## Directory Structure

- `_conclave/` — Conclave core files (do not modify manually)
- `_conclave/_memory/` — Persistent memory (company context, preferences)
- `skills/` — Installed skills (integrations, scripts, prompts)
- `squads/` — User-created squads
- `squads/{name}/_investigations/` — Sherlock content investigations (profile analyses)
- `squads/{name}/output/` — Generated content and files
- `_conclave/_browser_profile/` — Persistent browser sessions (login cookies, localStorage)

## How It Works

1. The `/conclave` workflow is the entry point for all interactions
2. The **Architect** agent creates and modifies squads
3. During squad creation, the **Sherlock** investigator can analyze reference profiles (Instagram, YouTube, Twitter/X, LinkedIn) to extract real content patterns
4. The **Pipeline Runner** executes squads automatically
5. All tasks run inline and sequentially (no background subagents)
6. Checkpoints pause execution for user input/approval

## Rules

- Always use `/conclave` commands to interact with the system
- Do not manually edit files in `_conclave/core/` unless you know what you're doing
- Squad YAML files can be edited manually if needed, but prefer using `/conclave edit`
- Company context in `_conclave/_memory/company.md` is loaded for every squad run

## Antigravity Environment: Subagents

This environment (Google Antigravity) does not support spawning background or parallel subagents. When agent instructions (e.g., from the Architect) say to "use the Task tool with run_in_background: true" or similar, you MUST instead execute all tasks inline and sequentially:

1. Inform the user you will process the tasks one by one
2. Execute each task in the current conversation — do NOT skip or defer any of them
3. Complete ALL tasks before asking the next question or moving on

Never announce that you "will do something in parallel" and then skip the work. Always do the actual research inline before continuing.

## Interaction Rules

- NEVER ask more than one question per message — always wait for the user's answer before proceeding to the next question
- When presenting options, always use a numbered list (1. / 2. / 3.) — tell the user to reply with the option number
