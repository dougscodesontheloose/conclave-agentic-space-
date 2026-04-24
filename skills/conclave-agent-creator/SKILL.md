---
name: "Best-Practice & Agent Creator"
description: >
  Guides creation and maintenance of best-practice files for the Conclave best-practices library,
  and standalone agent templates outside of squads. Handles format validation, cross-references,
  versioning, catalog consistency, research-informed content creation, skill cross-referencing,
  maturity tracking, and eval-driven quality validation.
description_pt-BR: >
  Guia a criação e manutenção de arquivos de best-practice na biblioteca de best-practices do Conclave,
  e templates de agentes standalone fora de squads. Cuida de validação de formato, referências cruzadas,
  versionamento, consistência do catálogo, criação informada por pesquisa, cross-referencing com skills,
  rastreamento de maturidade e validação de qualidade orientada por evals.
description_es: >
  Guía la creación y mantenimiento de archivos de best-practice en la biblioteca de best-practices de Conclave,
  y templates de agentes standalone fuera de squads. Maneja validación de formato, referencias cruzadas,
  versionamiento, consistencia del catálogo, creación informada por investigación, cross-referencing con skills,
  tracking de madurez y validación de calidad orientada por evals.
type: prompt
version: "3.0.0"
---

# Best-Practice Creator — Workflow

Use this workflow when creating a new best-practice file for the `_conclave/core/best-practices/` library.

## Pre-flight Checks

1. **Scan existing best-practice files**: Read `_conclave/core/best-practices/_catalog.yaml`. Extract `id`, `name`, `whenToUse`, `file` from each entry.
2. **Check for overlap**: Verify the new best-practice file doesn't duplicate an existing entry's `whenToUse` scope. If there's overlap, clarify the differentiation before proceeding.
3. **List available skills**: Read all `skills/*/SKILL.md` files. Extract `name`, `description`, `type` from each — these may inform the best-practice file's content.

## Research Phase (before writing)

Before writing any best-practice content, conduct targeted domain research. Best-practices built only from internal model knowledge are generic — real-world calibration produces dramatically better agent behavior.

1. **Framework Research**: Search for "{domain} framework" and "{domain} best practices 2025/2026"
   - Extract: the 2-3 most cited frameworks, methodologies, or processes
   - These become the foundation for **Core Principles** and **Techniques & Frameworks**

2. **Quality Benchmarks**: Search for "{domain} quality criteria" and "how to evaluate {output type}"
   - Extract: scoring rubrics, evaluation standards, acceptance thresholds
   - These become the **Quality Criteria** section with real, measurable thresholds

3. **Common Mistakes**: Search for "{domain} mistakes to avoid" and "{domain} anti-patterns"
   - Extract: specific errors practitioners make, with explanations of why they're harmful
   - These become the **Anti-Patterns** section with grounded, not speculative, entries

4. **Professional Vocabulary**: From all research, collect:
   - Terms professionals always use in this domain → **Vocabulary Always Use**
   - Terms that signal amateur or low-quality work → **Vocabulary Never Use**
   - Tone conventions specific to the domain → **Tone Rules**

5. **Real Examples**: Search for "best {content/output type} examples" and study 2-3 high-quality specimens
   - These calibrate the **Output Examples** section to realistic quality levels

Run research as a subagent if available, otherwise inline. Compile findings into a brief that feeds every section of the best-practice file. This research phase typically takes 3-5 minutes and 2-3 web searches.

**Rule:** Never write a best-practice file without at least searching for frameworks and common mistakes. The research makes the difference between generic advice and domain-calibrated expertise.

## Creation Checklist

For each new best-practice file, ensure ALL of the following:

### Frontmatter (YAML)

- [ ] `id`: lowercase kebab-case (e.g., `copywriting`)
- [ ] `name`: Display name for catalog listing (e.g., `"Copywriting & Persuasive Writing"`)
- [ ] `whenToUse`: Multi-line with positive scope AND "NOT for: ..." negative scope referencing other best-practice IDs
- [ ] `version`: `"1.0.0"` for new best-practice files

### Body (Markdown) — All sections mandatory

- [ ] **Core Principles**: 6+ numbered domain-specific decision rules, each with a bold title and detailed explanation
- [ ] **Techniques & Frameworks**: Concrete methods, models, or processes practitioners use in this discipline (e.g., diagnostic steps, framework selections, structural patterns)
- [ ] **Quality Criteria**: 4+ checkable criteria as `- [ ]` list that can be used to evaluate output
- [ ] **Output Examples**: 2+ complete examples, 15+ lines each, realistic NOT template-like
- [ ] **Anti-Patterns**: Never Do (4+) + Always Do (3+), each with explanation
- [ ] **Vocabulary Guidance**: Terms/phrases to Always Use (5+), Terms/phrases to Never Use (3+), Tone Rules (2+)

### Quality Minimums

| Section | Minimum |
|---------|---------|
| Total file lines | 200+ |
| Core Principles | 6+ numbered rules |
| Techniques & Frameworks | 3+ concrete techniques |
| Vocabulary Always Use | 5+ terms |
| Vocabulary Never Use | 3+ terms |
| Output Examples | 2 complete, 15+ lines each |
| Anti-Patterns (Never Do) | 4+ |
| Anti-Patterns (Always Do) | 3+ |
| Quality Criteria | 4+ checkable items |

## Post-Creation Steps

### 1. Update existing best-practice files' `whenToUse`

For each existing best-practice file whose scope overlaps with the new one:
- Add a "NOT for: {overlapping-scope} → See {new-best-practice-id}" line to their `whenToUse`
- Bump their version (patch increment)

### 2. Update `_catalog.yaml`

Add a new entry to `_conclave/core/best-practices/_catalog.yaml` with:
- `id`: matching the frontmatter `id`
- `name`: matching the frontmatter `name`
- `whenToUse`: single-line summary of the scope (positive only, no "NOT for")
- `file`: `{id}.md`

Place it under the appropriate section comment (Discipline or Platform best practices).

### 3. File placement

Save to `_conclave/core/best-practices/{id}.md`.

### 4. Validation

Re-read the created file and verify:
- [ ] All checklist items above are present
- [ ] YAML frontmatter parses correctly (no syntax errors)
- [ ] `whenToUse` references only existing best-practice IDs
- [ ] Output examples are realistic, not template placeholders
- [ ] File exceeds 200 lines
- [ ] Corresponding entry exists in `_catalog.yaml`

### 5. Cross-Reference with Skills

After creating/updating a best-practice, check for related skills:

1. Scan `skills/*/SKILL.md` files. For each, parse frontmatter and extract `name`, `categories`.
2. Compare the new best-practice's `id` and scope with each skill's `categories`.
3. If overlap found (e.g., best-practice `image-design` ↔ skill with `categories: [design, image]`):
   - Add a section at the end of the best-practice file:
     ```markdown
     ## Related Skills
     - **{skill-name}** ({skill-type}): {skill-description}
     ```
   - This helps the Architect know which skills pair naturally with which best-practices during Phase D (Skill Discovery) and Phase E (Agent Design).
4. If no matching skills exist, proceed without note — this is informational, not blocking.

### 6. Ecosystem Awareness Checklist

Before considering the best-practice complete, verify its integration fitness:

- [ ] **Injectability**: The file can be loaded by the Design phase (Phase A) via `_catalog.yaml` match — verify `whenToUse` is specific enough to match relevant squads but not so broad it matches everything
- [ ] **Build Compatibility**: Quality criteria format uses `- [ ]` checkboxes compatible with `build.prompt.md` validation gates (Gate 1: Agent Completeness)
- [ ] **Context Budget**: Total file size is reasonable for Tier 3 summarization — if the file exceeds 400 lines, include a `## Key Rules` or `## Quick Reference` section at the top (the Pipeline Runner preferentially injects this section when space is tight)
- [ ] **Output Example Realism**: Output examples match the format and depth expected by `build.prompt.md` (15+ lines, realistic content, not templates)
- [ ] **Vocabulary Compatibility**: Always Use / Never Use terms don't conflict with existing best-practices in overlapping domains (check cross-references)

### 7. Maturity Classification

Every best-practice file starts at the lowest maturity level and progresses through usage:

Add the following fields to the YAML frontmatter:

```yaml
maturity: draft          # draft | validated | battle-tested
lastValidated: ""        # YYYY-MM-DD, set when promoted
usedInSquads: []         # populated by pipeline runner post-completion
```

**Maturity levels:**

| Level | Meaning | Promotion Criteria |
|-------|---------|-------------------|
| `draft` | Newly created, not yet used in a squad run | Default for all new best-practices |
| `validated` | Used in at least 1 squad run where the reviewer approved the output | Pipeline Runner updates this automatically after a successful run |
| `battle-tested` | Used in 3+ squad runs with reviewer approval rate > 80% | Pipeline Runner promotes automatically when threshold met |

**How promotion works:**
- The Pipeline Runner (`runner.pipeline.md`) tracks which best-practices were consulted during a run (from `design.yaml → best_practices_consulted`)
- After a successful run (reviewer approves), the runner:
  1. Reads each consulted best-practice file
  2. Adds the squad code to `usedInSquads` (if not already present)
  3. Checks if promotion criteria are met
  4. If yes, bumps `maturity` and sets `lastValidated` to today's date
  5. Does NOT bump `version` — maturity changes are metadata, not content changes

**Catalog display:** When listing best-practices, append a maturity badge:
- `draft` → 📝
- `validated` → ✅
- `battle-tested` → 🏆

---

# Best-Practice Updater — Workflow

Use this workflow when updating best-practice files in the `_conclave/core/best-practices/` library.

## Versioning Rules (Semver)

| Change Type | Version Bump | Examples |
|-------------|-------------|----------|
| **Patch** (x.x.X) | Fix typos, adjust wording, minor refinements | Fix anti-pattern phrasing, correct a vocabulary term |
| **Minor** (x.X.0) | Add new content, extend capabilities | Add new principle, new output example, new technique |
| **Major** (X.0.0) | Rewrite or restructure significantly | Rewrite core principles, fundamentally change scope |

Always update the `version` field in the YAML frontmatter after any change.

## Update Scenarios

### When a best-practice file is removed from the library

1. Get the removed best-practice file's `id`
2. Remove its entry from `_conclave/core/best-practices/_catalog.yaml`
3. Scan ALL remaining best-practice files in `_conclave/core/best-practices/*.md`
4. For each file, check if the removed ID is referenced in `whenToUse`
   - Look for patterns: "NOT for: ... → See {removed-id}"
5. If found, remove that "NOT for" line
6. Bump the affected files' version (patch: x.x.X)

### When a new best-practice file is added to the library

The Best-Practice Creator workflow (above) handles the initial `whenToUse` cross-references during creation. This section is only needed if cross-references were missed or need adjustment after the fact.

1. Read the new best-practice file's `whenToUse` — identify its scope
2. Scan existing best-practice files for overlapping scope
3. Add "NOT for: {new-scope} → See {new-id}" where appropriate
4. Bump affected files' version (patch)
5. Ensure the new entry exists in `_catalog.yaml`

### When updating a best-practice file's content

1. Make the content changes
2. Verify ALL mandatory sections still exist:
   - [ ] Core Principles (6+ rules)
   - [ ] Techniques & Frameworks (3+ techniques)
   - [ ] Quality Criteria (4+ checkable items)
   - [ ] Output Examples (2+ complete examples)
   - [ ] Anti-Patterns (Never Do + Always Do)
   - [ ] Vocabulary Guidance (Always Use, Never Use, Tone Rules)
3. Bump version according to semver rules above
4. If the `whenToUse` scope changed, update cross-references in other best-practice files and in `_catalog.yaml`

### When updating a best-practice file's `whenToUse` scope

This is the most impactful change — it affects how the Architect selects best practices during squad creation.

1. Document the old scope and new scope
2. Update the best-practice file's `whenToUse` field
3. Scan ALL other best-practice files' `whenToUse` for references to this ID
4. Update cross-references to reflect the new scope
5. Update the `whenToUse` summary in `_catalog.yaml`
6. Bump version (minor if scope expanded, patch if scope narrowed)

## Validation Checklist

After ANY update, verify:

- [ ] Version was bumped correctly (patch/minor/major per rules above)
- [ ] All mandatory sections still present and non-empty
- [ ] `whenToUse` cross-references are consistent across ALL best-practice files
- [ ] No broken cross-references to removed best-practice IDs
- [ ] Output examples are still realistic and complete
- [ ] File still exceeds 200 lines minimum
- [ ] `_catalog.yaml` entry is in sync with frontmatter (`id`, `name`, `whenToUse`)

## Bulk Operations

### Verify catalog consistency

```
Read _conclave/core/best-practices/_catalog.yaml
For each entry in catalog:
  1. Verify _conclave/core/best-practices/{entry.file} exists
  2. Read the file's frontmatter
  3. Verify entry.id matches frontmatter id
  4. Verify entry.name matches frontmatter name
  5. Flag any mismatches

For each .md file in _conclave/core/best-practices/ (excluding _catalog.yaml):
  1. Verify a corresponding entry exists in _catalog.yaml
  2. Flag any orphaned files with no catalog entry
```

### Verify cross-reference consistency

```
For each best-practice file A in _conclave/core/best-practices/*.md:
  For each "NOT for: ... → See {id}" in A.whenToUse:
    1. Verify _conclave/core/best-practices/{id}.md exists
    2. Verify {id}'s whenToUse covers the referenced scope
    3. Flag inconsistencies
```

---

# Agent Template Creator — Workflow

Use this workflow when creating a standalone agent (outside of a squad). Standalone agents are reusable agent definitions that can be imported into any squad, or used directly as assistants.

This is **separate from squad creation** — the Architect creates squad-specific agents during the Design/Build phases. This workflow creates portable, reusable agent templates.

## When to Use

- User wants a custom agent that works across multiple squads
- User wants to define a domain expert (e.g., "SEO analyst", "brand voice guardian") once and reuse everywhere
- User wants to prototype an agent before committing to a full squad

## Agent Template Structure

Standalone agents follow the exact same `.agent.md` format used by squad agents (from `build.prompt.md`):

```markdown
---
id: "agents/{agent-id}"
name: "{Agent Name}"          # Two words, alliterative (FirstName LastName)
title: "{Agent Title}"
icon: "{emoji}"
squad: "standalone"            # marks this as portable, not squad-bound
execution: inline | subagent
skills: []
tasks: []                      # optional — list of task files
---

# {Agent Name}

## Persona
### Role
### Identity
### Communication Style

## Principles

## Operational Framework
### Process
### Decision Criteria

## Voice Guidance
### Vocabulary — Always Use
### Vocabulary — Never Use
### Tone Rules

## Output Examples

## Anti-Patterns
### Never Do
### Always Do

## Quality Criteria

## Integration
```

## Creation Process

### Step 1: Intent Capture

Ask the user:
1. What should this agent do? (open-ended description)
2. What domain is this for? (helps select relevant best-practices)
3. Will this agent work within squads, standalone, or both?

### Step 2: Research

Follow the same **Research Phase** defined in the Best-Practice Creator section above. The research targets the agent's domain and role.

Additionally:
- Read relevant best-practices from `_conclave/core/best-practices/` (use `_catalog.yaml` to find matches)
- These best-practices inform the agent's Principles, Voice Guidance, Anti-Patterns, and Quality Criteria

### Step 3: Agent Design

Design the agent following `build.prompt.md` format rules:
- All mandatory sections present
- Minimum 6 principles (domain-specific, from research)
- Minimum 5-step operational framework
- Minimum 2 complete output examples (15+ lines each, realistic)
- Minimum 4 anti-patterns (Never Do) + 3 positive practices (Always Do)
- Total: 120-200 lines

### Step 4: Naming

Apply the naming convention from `design.prompt.md` Phase E:
- **Two words**: FirstName LastName, both starting with the same letter (alliteration)
- **First name**: common human name in the user's Output Language
- **Last name**: playful reference to the agent's specialty
- **Icon**: emoji representing the role

### Step 5: Save

Save to `agents/{agent-id}.agent.md` at the project root. Standalone agents live outside the `squads/` directory.

If the agent has tasks, also create `agents/{agent-id}/tasks/{task-name}.md` for each task.

### Step 6: Validation

Verify against `build.prompt.md` Gate 1 (Agent Completeness):
- [ ] Has `## Persona` with 3 subsections
- [ ] Has `## Principles` with min 6 items
- [ ] Has `## Operational Framework` with `### Process` (min 5 steps) and `### Decision Criteria`
- [ ] Has `## Voice Guidance` with Always Use (5+) and Never Use (3+)
- [ ] Has `## Output Examples` with 1-2 complete examples (15+ lines each)
- [ ] Has `## Anti-Patterns` with Never Do (4+) and Always Do (3+)
- [ ] Has `## Quality Criteria`
- [ ] Has `## Integration`
- [ ] Total lines >= 100
- [ ] Name has exactly two words with alliteration

---

# Eval & Validation — Quality Verification

This section provides a lightweight validation loop for both best-practices and standalone agents. The goal is to test that the created artifact actually improves downstream output quality.

## When to Use

- After creating a new best-practice, to verify it improves agent output
- After creating a standalone agent, to verify it produces quality work
- After significant updates to either artifact type
- When the user explicitly asks to test/validate a best-practice or agent

## Validation Process for Best-Practices

### Step 1: Design a Test Scenario

Create a realistic scenario that an agent using this best-practice would face:
1. Define a task prompt (e.g., "Write an Instagram carousel about AI trends")
2. Define success criteria derived from the best-practice's Quality Criteria section
3. Define 2-3 veto conditions from the Anti-Patterns section

### Step 2: Run Comparative Test

Execute the task twice:
- **With best-practice**: Create a temporary agent with the best-practice injected into its context (simulating how `design.prompt.md` Phase A loads best-practices)
- **Without best-practice**: Same agent, same task, no best-practice context

If subagents are available, run both in parallel. Otherwise, run sequentially.

### Step 3: Evaluate

Compare the two outputs against the success criteria:
- Does the with-best-practice output satisfy more quality criteria?
- Does it avoid more anti-patterns?
- Does it use the correct vocabulary?
- Is the overall quality noticeably better?

Present both outputs to the user with a brief analysis. Ask: "Does the best-practice version look meaningfully better?"

### Step 4: Iterate

If the best-practice didn't improve output:
1. Identify which sections are underperforming (weak principles? generic examples? missing techniques?)
2. Revise those sections
3. Re-run the test
4. Maximum 2 iterations — after that, the best-practice is likely addressing a domain that doesn't benefit from this type of guidance

## Validation Process for Standalone Agents

### Step 1: Design a Test Task

1. Pick a task that the agent should handle well
2. Define expected quality based on the agent's Quality Criteria and Output Examples
3. Create 1-2 veto conditions from the agent's Anti-Patterns

### Step 2: Execute

Run the agent on the test task:
- If the agent has tasks, execute them in sequence (simulating Pipeline Runner's task-based execution)
- If no tasks, execute the agent's operational framework monolithically

### Step 3: Evaluate

Check the output against:
- [ ] Quality Criteria (all checkboxes should pass)
- [ ] Veto Conditions (none should be triggered)
- [ ] Output matches the style and depth of Output Examples
- [ ] Voice Guidance vocabulary is correctly applied

Present to user for qualitative review.

### Step 4: Iterate

If quality is insufficient:
1. Identify the weakest section (vague principles? missing decision criteria? generic examples?)
2. Revise and re-test
3. Maximum 2 iterations

---

## Quick Reference — When to Use Which Workflow

| User Intent | Workflow |
|-------------|----------|
| "Create a best-practice for X" | Best-Practice Creator |
| "Update/improve the copywriting best-practice" | Best-Practice Updater |
| "Create an agent that does X" (no squad context) | Agent Template Creator |
| "Test if this best-practice actually works" | Eval & Validation (Best-Practice) |
| "Test if this agent is any good" | Eval & Validation (Agent) |
| "Create a squad for X" | → Route to Architect (`/conclave create`) |
