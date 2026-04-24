# Conclave — Project Instructions

This project uses **Conclave**, a multi-agent orchestration framework.

## Quick Start

Type `/conclave` to open the main menu, or use any of these commands:

- `/conclave init` — Scaffold Conclave in any other folder (enables the skill outside this repo)
- `/conclave create` — Create a new squad
- `/conclave run <name>` — Run a squad
- `/conclave where` — Show resolved global/local paths (debug)
- `/conclave help` — See all commands

## Directory Structure

### This repository (the "hub")

- `_conclave/` — Conclave core files (do not modify manually)
- `_conclave/_memory/` — Persistent memory (company context, preferences)
- `squads/` — User-created squads
- `squads/{name}/_investigations/` — Sherlock content investigations (profile analyses)
- `squads/{name}/output/` — Generated content and files
- `_conclave/_browser_profile/` — Persistent browser sessions (login cookies, localStorage)

### Hybrid mode (global runtime + per-project context)

Conclave is installed as a **global skill** and can be invoked from any directory under `~/Documents/`. It resolves paths as follows:

- **Global skill entry**: `~/.claude/skills/conclave/SKILL.md`
- **Global runtime hub**: `~/.conclave/` — symlinks into this repository:
  - `~/.conclave/core` → `_conclave/core/`
  - `~/.conclave/skills_catalog` → `skills/`
  - `~/.conclave/_memory` → `_conclave/_memory/` (holds `global-preferences.md`)
  - `~/.conclave/home` → this repository root
- **Per-project context**: `$CWD/_conclave/` — created by `/conclave init` in any folder. Contains that project's `_memory/` (company, preferences), alongside `$CWD/squads/` and `$CWD/skills/`.

Run `/conclave where` in any folder to see the resolved paths for that `cwd`.

**Preference cascade (highest wins):** step-level > squad `memories.md` > project `preferences.md` > `global-preferences.md` > agent defaults.

## How It Works

1. The `/conclave` skill is the entry point for all interactions
2. The **Architect** agent creates and modifies squads
3. During squad creation, the **Sherlock** investigator can analyze reference profiles (Instagram, YouTube, Twitter/X, LinkedIn) to extract real content patterns
4. The **Pipeline Runner** executes squads automatically
5. Agents communicate via persona switching (inline) or subagents (background)
6. Checkpoints pause execution for user input/approval

## IDE Compatibility Rule (Permanent — Never Skip)

Every major structural change to this project MUST be evaluated against these IDE compatibility files and updated when applicable:

| File | When to Update |
|---|---|
| `.editorconfig` | New file types added to the project |
| `.vscode/settings.json` | New folders to hide/exclude, new language-specific settings |
| `.vscode/extensions.json` | New language runtimes or file types that benefit from an extension |
| `.vscode/tasks.json` | New Conclave commands added to `AGENTS.md` command routing |
| `.cursorrules` | Core architecture changes (new directories, new agents, new design systems, new conventions) |
| `README.md` | Any change that affects how a new user or AI agent would set up or understand the project |

**Criteria for "applicable and relevant":**

- A new top-level directory was created → update `.vscode/settings.json` (exclude from search/explorer if it's noise) and `.cursorrules` (add to architecture knowledge)
- A new `/conclave` command was added → update `.vscode/tasks.json`
- A new design system, visual identity, or agent convention was added → update `.cursorrules`
- A new scripting language or file type appears → update `.editorconfig` and `.vscode/extensions.json`

This rule ensures the project remains frictionless and IDE-agnostic as it grows in complexity.

---

## Rules

- Always use `/conclave` commands to interact with the system
- Do not manually edit files in `_conclave/core/` unless you know what you're doing
- Squad YAML files can be edited manually if needed, but prefer using `/conclave edit`
- Company context in `_conclave/_memory/company.md` is loaded for every squad run
- **Overwrite protection:** any flow that rewrites user-owned files (`company.md`, `preferences.md`, squad files, `README.md`) MUST create a `.bak-{YYYYMMDD-HHmmss}` backup first. See the Overwrite Protection Policy in [_conclave/core/skill/SKILL.md](_conclave/core/skill/SKILL.md).

## Browser Sessions

Conclave uses a persistent Playwright browser profile to keep you logged into social media platforms.

- Sessions are stored in `_conclave/_browser_profile/` (gitignored, private to you)
- First time accessing a platform, you'll log in manually once
- Subsequent runs will reuse your saved session
- **Important:** The native Claude Code Playwright plugin must be disabled. Conclave uses its own `@playwright/mcp` server configured in `.mcp.json`.
