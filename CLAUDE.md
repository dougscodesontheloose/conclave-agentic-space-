# Conclave — Project Instructions

This project uses **Conclave**, a multi-agent orchestration framework.

## Quick Start

Type `/conclave` to open the main menu, or use any of these commands:

- `/conclave init` — Scaffold Conclave in any other folder (enables the skill outside this repo)
- `/conclave create` — Create a new squad
- `/conclave run <name>` — Run a squad
- `/conclave where` — Show resolved global/local paths (debug)
- `/conclave help` — See all commands

**GAIA Subroutines** (Horizon Zero Dawn easter egg — system observers that close learning loops between runs):

- `/conclave tide` — 🌊 **POSEIDON** Tide Observer: aggregates JSONL streams, surfaces patterns, proposes follow-up actions ([poseidon.agent.md](_conclave/core/poseidon.agent.md))
- `/conclave curate` — ☀️ **APOLLO** Memory Curator: detects duplications, staleness, conflicts in `_memory/` ([apollo.agent.md](_conclave/core/apollo.agent.md))
- `/conclave forge` — 🔨 **HEPHAESTUS** Manufacturing Watch: surfaces pending skill/template/agent manufacturing candidates ([hephaestus.agent.md](_conclave/core/hephaestus.agent.md))
- (passive) — 🦉 **MINERVA** Intent Listener: contextual routing on natural-language input ([minerva.agent.md](_conclave/core/minerva.agent.md))
- (passive) — 🌱 **ELEUTHIA** Profile Refresh Cradle: 60-day `company.md` drift check ([eleuthia.agent.md](_conclave/core/eleuthia.agent.md))
- (passive) — 🏹 **ARTEMIS** Squad Gossip Bus: cross-squad signal propagation via `gossip.jsonl` ([artemis.agent.md](_conclave/core/artemis.agent.md))

All subroutines observe and propose; the user closes every mutation loop. SafeGuard Hard Veto remains the floor.

**Foundational documents** (motor-agnostic, inherited by every agent regardless of which engine runs them):

- [`_conclave/core/charter.md`](_conclave/core/charter.md) — **Conclave Charter**: code of conduct (honesty, refusal, autonomy, hard constraints).
- [`_conclave/core/security.policy.md`](_conclave/core/security.policy.md) — **SafeGuard**: data privacy and prompt injection defense.
- [`_conclave/core/soul.md`](_conclave/core/soul.md) — **Soul**: mission, pillars, aesthetic direction.

Charter governs *conduct*; SafeGuard governs *data*. Both are co-extensive — neither overrides the other.

## Directory Structure

### This repository (the "hub")

**Núcleo do sistema (não mover — symlinks globais dependem destes paths):**

- `_conclave/core/` — Runtime imutável (agentes GAIA, runner, schemas, prompts). Inclui `SKILLS_INDEX.md` (catálogo descobrível), `CONCLAVE_CHEATSHEET.md`.
- `_conclave/config/` — Config imutável do sistema
- `_conclave/state/memory/` — Memória persistente (company, preferences, archive/)
- `_conclave/state/investigations/` — Sherlock investigations persistidas
- `_conclave/state/history/` — Histórico de sessões (persistente)
- `_conclave/state/knowledge/` — Knowledge base (persistente)
- `_conclave/state/browser_profile/` — Sessões Playwright persistentes (gitignored)
- `_conclave/runtime/` — Workspaces efêmeros (gitignored quando aplicável): `logs/` (audit trail), `scratch/`, `lab/`. Apagáveis a qualquer momento.
- `_conclave/tools/` — Ferramentas: `tests/` (smoke tests), `scripts/` (heartbeat, validate, poseidon engine, disk guardian).
- `skills/` — Catálogo unificado de skills (178 skills, absorveu `.agents/skills/` em 2026-05-07). Índice em [`_conclave/core/SKILLS_INDEX.md`](_conclave/core/SKILLS_INDEX.md). 6 conflitos de nome marcados com sufixo `-alt` para resolução manual.
- `squads/` — User-created squads. Cada um com `_investigations/` e `output/`.

**Pastas guarda-chuva (organização visual — reorganizadas em 2026-05-01):**

- `ambientes/` — Sub-projetos paralelos. Cada um pode ter seu próprio `_conclave/` aninhado. Catálogo em [`ambientes/AMBIENTES_INDEX.md`](ambientes/AMBIENTES_INDEX.md).
- `knowledge/` — Bases de conhecimento e prompts: `memory-lane/`, `prompt-arch/`, `prompt-engineer/`.
- `references/` — Assets visuais e de marca: `brand-style/` (ex `ref_brand-style/`), `visual-style/` (ex `ref_style/`).
- `apps/` — Aplicações empacotadas: `dashboard/` (Vite app `conclave-dashboard`).

**Legacy / quarentena:**

- `legacy/linkedin-auth/` — scripts OAuth do LinkedIn (`linkedin-auth.py`, `linkedin-auth2.py`, `test-auth.py`, `.linkedin_token`). Movidos da raiz em 2026-05-07. `squads/sexy_content/scripts/linkedin_publisher.py` lê o token via `LINKEDIN_TOKEN_PATH` (default: `legacy/linkedin-auth/.linkedin_token`).

### Hybrid mode (global runtime + per-project context)

Conclave is installed as a **global skill** and can be invoked from any directory under `~/Documents/`. It resolves paths as follows:

- **Global skill entry**: `~/.claude/skills/conclave/SKILL.md`
- **Global runtime hub**: `~/.conclave/` — symlinks into this repository:
  - `~/.conclave/core` → `_conclave/core/`
  - `~/.conclave/skills_catalog` → `skills/`
  - `~/.conclave/_memory` → `_conclave/state/memory/` (holds `global-preferences.md`)
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
- Company context in `_conclave/state/memory/company.md` is loaded for every squad run
- **Overwrite protection:** any flow that rewrites user-owned files (`company.md`, `preferences.md`, squad files, `README.md`) MUST create a `.bak-{YYYYMMDD-HHmmss}` backup first. See the Overwrite Protection Policy in [_conclave/core/skill/SKILL.md](_conclave/core/skill/SKILL.md).

## Browser Sessions

Conclave uses a persistent Playwright browser profile to keep you logged into social media platforms.

- Sessions are stored in `_conclave/state/browser_profile/` (gitignored, private to you)
- First time accessing a platform, you'll log in manually once
- Subsequent runs will reuse your saved session
- **Important:** The native Claude Code Playwright plugin must be disabled. Conclave uses its own `@playwright/mcp` server configured in `.mcp.json`.
