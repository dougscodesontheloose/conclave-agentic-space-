# Conclave Ecosystem Context

This document provides the context you need when creating or improving skills that will run inside the Conclave pipeline. Understanding how skills are loaded, injected, and executed prevents the most common integration failures.

## How Skills Are Used in Conclave

### 1. Declaration

Skills are declared in two places:
- **Squad level**: `squads/{code}/squad.yaml` under the `skills:` section
- **Agent level**: each `.agent.md` file has a `skills:` field in its YAML frontmatter

```yaml
# In squad.yaml
skills:
  - web_search       # native — always available
  - web_fetch        # native — always available
  - apify            # installed skill
  - my-custom-skill  # your skill goes here

# In agent .agent.md frontmatter
---
id: "squads/my-squad/agents/researcher"
name: "Rita Research"
skills:
  - apify
  - my-custom-skill
---
```

### 2. Resolution (Pre-Execution)

Before a squad runs, the Pipeline Runner resolves every non-native skill:
1. Checks `skills/{name}/SKILL.md` exists
2. Parses frontmatter for type, MCP config, env vars
3. If MCP type → verifies MCP server is configured in `.claude/settings.local.json`
4. If any env vars are missing → warns but does NOT block

**If the skill directory doesn't exist, the pipeline stops.** Skills must be installed before execution.

### 3. Injection (During Execution)

For each step in the pipeline, the Runner composes the agent's context in this exact order:

```
┌─────────────────────────────────────┐
│  Agent .agent.md                    │  ← Persona, Principles, Voice,
│  (full markdown body)               │     Anti-Patterns, Quality Criteria
├─────────────────────────────────────┤
│  --- FORMAT: {format name} ---      │  ← Platform best-practice (if step
│  {best-practice markdown body}      │     has `format:` in frontmatter)
├─────────────────────────────────────┤
│  --- SKILL INSTRUCTIONS ---         │  ← Your skill's body goes HERE
│                                     │
│  ## {skill name from frontmatter}   │
│  {SKILL.md markdown body}           │
├─────────────────────────────────────┤
│  Step file instructions             │  ← Process, Output Format,
│  (from pipeline/steps/)             │     Veto Conditions, Quality Criteria
└─────────────────────────────────────┘
```

**Key insight:** Your skill body is injected AFTER the agent's persona and best-practice, but BEFORE the step instructions. The agent is already "in character" by the time it reads your skill. Your instructions should complement the agent, not override it.

### 4. Context Budget Management

The Pipeline Runner uses a tiered system to prevent context window saturation:

| Tier | Content | Policy |
|------|---------|--------|
| **Tier 1** (always) | Step file + Agent persona + Input data | Non-negotiable |
| **Tier 2** (if space) | Squad memory + Company context + **Skill instructions** | Full content |
| **Tier 3** (summarize) | Best-practices → Key Rules only; Output examples → first only | Compressed |
| **Tier 4** (reference) | Other agents, historical run data | Never injected |

**Your skill body lives in Tier 2.** If the combined Tier 1 + Tier 2 exceeds ~15,000 words, skill instructions are moved to Tier 3 — only the `## Quick Start` or first 50 lines are injected.

**Practical limit:** Keep your SKILL.md body under 500 lines. If it approaches this limit, move detail into `references/` files that the agent reads on demand.

---

## SKILL.md Requirements for Conclave

### Frontmatter (mandatory fields)

```yaml
---
name: my-skill-name           # lowercase, hyphenated
description: >                # what + when — this is what the Skills Engine
  What the skill does.        # shows during discovery and listing
  Use when X needs Y.
type: mcp | script | hybrid | prompt
version: "1.0.0"              # semver
categories:                    # used for Skill Discovery matching
  - scraping
  - data
env:                           # environment variables the skill needs
  - MY_API_KEY
---
```

See `references/skill-format.md` for the complete schema per type (MCP, script, hybrid, prompt).

### Body — Integration-Aware Patterns

**DO:**
- Start with `## When to use` — this helps the Architect during Phase D (Skill Discovery) match your skill to squad needs
- Include clear `## Instructions` with numbered steps — the agent executing your skill is already loaded with its own operational framework; your steps should be complementary
- Keep instructions agent-agnostic — your skill may be used by a researcher, a writer, or a reviewer; don't assume which agent type
- Use `## Available operations` for MCP/script skills — list what the tools can do without prescribing when to use them (the step file handles orchestration)

**DON'T:**
- Override the agent's communication style or persona — your skill is injected into an existing identity
- Duplicate quality criteria — the step file and agent definition already have quality checks
- Include system prompts, role definitions, or persona instructions — those belong in `.agent.md`
- Use absolute paths — skills are portable across squads; use paths relative to the skill directory
- Exceed 500 lines in the body — use `references/` for detailed documentation

### Categories for Skill Discovery

The Architect uses these categories during Phase D to match skills to squad needs:

| Squad Need | Matching Categories |
|------------|-------------------|
| Web scraping / structured data | `scraping`, `data` |
| Social media content | `social-media`, `content`, `design` |
| API integrations | `integration`, `messaging`, `automation` |
| Data analysis | `analytics`, `data`, `visualization` |
| Image/design work | `design`, `image`, `visual` |

If your skill's categories don't match any squad need, it won't be suggested during creation. Choose categories thoughtfully.

---

## Common Integration Anti-Patterns

### 1. Context Bloat
**Problem:** SKILL.md body > 500 lines, pushing the total context past Tier 2 limits.
**Solution:** Move examples, detailed references, and edge case documentation into `references/` files. Keep the body lean — instructions and key patterns only.

### 2. Persona Collision
**Problem:** Skill body includes "You are a..." or "Your role is..." instructions that conflict with the agent's `.agent.md` persona.
**Solution:** Never define agent identity in a skill. Write instructions as capabilities ("This skill enables you to..."), not identity ("You are a...").

### 3. Orphaned Dependencies
**Problem:** Skill requires an MCP server or script that's installed during creation but not tracked.
**Solution:** Always declare dependencies in frontmatter: `mcp.server_name` for MCP, `script.dependencies` for packages, `env` for API keys.

### 4. Format Assumption
**Problem:** Skill assumes a specific output format that conflicts with the step file's `## Output Format`.
**Solution:** Skills should provide capabilities and transformations, not prescribe final output format. The step file is the authority on what gets produced.

### 5. Undiscoverable Skill
**Problem:** Skill has no `categories` or generic categories like `["general"]`, so it's never suggested during Skill Discovery.
**Solution:** Use specific, meaningful categories that map to squad needs (see table above).

---

## Testing Skills in Conclave Context

When evaluating your skill, the test environment should replicate the real execution context:

1. **Compose context like the Runner does:** Agent persona → Format (if applicable) → Skill body → Step instructions
2. **Respect the budget:** Verify total context < 15k words
3. **Include veto conditions:** Real pipeline steps have veto conditions that reject substandard output
4. **Test with different agent types:** A skill used by a researcher behaves differently than one used by a writer

See `references/pipeline-simulation.md` for detailed instructions on replicating the pipeline environment in evals.
