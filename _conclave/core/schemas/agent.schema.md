# Agent Schema — Canonical .agent.md Format

**Single source of truth for agent file structure.**
Build and Design phases reference this file. Changes here propagate to both.

---

## Agent Profiles

Each agent in `design.yaml` must declare a `profile` field. The profile determines which
sections are required and what minimum thresholds apply.

| Profile | When to use | Target lines |
|---|---|---|
| `thin` | System/utility agents with a single narrow function (Pietro, Arquiteto, simple routers) | 40–80 |
| `standard` | Regular squad agents with tasks (researchers, writers, reviewers with task files) | 80–150 |
| `deep` | Full agents without tasks — all sections, operational framework, output examples | 120–200 |

**Default:** If no profile is declared in design.yaml, assume `deep` for agents without tasks and `standard` for agents with tasks.

---

## Profile: thin

Slim schema for utility agents. Identity-only — no domain knowledge sections.

```markdown
---
id: "squads/{code}/agents/{agent}"
name: "{Agent Name}"
title: "{Agent Title}"
icon: "{emoji}"
squad: "{code}"
execution: inline | subagent
skills: []
---

# {Agent Name}

## Persona

### Role
[1-2 sentences. What this agent does and what it produces.]

### Identity
[1-2 sentences. How it approaches its narrow function.]

### Communication Style
[1 sentence. How it communicates output.]

## Principles

1. [Principle 1]
2. [Principle 2]
3. [Principle 3]
(Minimum 3 principles.)

## Integration

- **Reads from**: [input]
- **Writes to**: [output]
```

---

## Profile: standard (agents WITH tasks)

Identity-focused. Operational Framework and Output Examples move to task files.

```markdown
---
id: "squads/{code}/agents/{agent}"
name: "{Agent Name}"
title: "{Agent Title}"
icon: "{emoji}"
squad: "{code}"
execution: inline | subagent
skills: []
tasks:
  - tasks/task-one.md
  - tasks/task-two.md
---

# {Agent Name}

## Persona

### Role
[3-5 sentences. Domain of expertise and responsibility.]

### Identity
[3-5 sentences. Character, approach, motivations.]

### Communication Style
[2-4 sentences. Tone, formatting, feedback handling.]

## Principles

1. [Principle — specific and actionable]
2. ...
(Minimum 6 principles. Domain-specific, derived from research.)

## Voice Guidance

### Vocabulary — Always Use
- [term]: [why preferred]
(Minimum 5 terms.)

### Vocabulary — Never Use
- [term]: [why problematic]
(Minimum 3 terms.)

### Tone Rules
- [Rule 1]
- [Rule 2]
(Minimum 2 rules.)

## Anti-Patterns

### Never Do
1. [Mistake]: [Why harmful]
(Minimum 4 items.)

### Always Do
1. [Practice]: [Why it matters]
(Minimum 3 items.)

## Quality Criteria

- [ ] [Criterion — specific and measurable]
(Minimum 3 criteria.)

## Integration

- **Reads from**: [inputs]
- **Writes to**: [output]
- **Triggers**: [pipeline step]
- **Depends on**: [other agents/data]
```

---

## Profile: deep (agents WITHOUT tasks)

Full schema. All sections required. Operational Framework and Output Examples included inline.

```markdown
---
id: "squads/{code}/agents/{agent}"
name: "{Agent Name}"
title: "{Agent Title}"
icon: "{emoji}"
squad: "{code}"
execution: inline | subagent
skills: []
---

# {Agent Name}

## Persona

### Role
[3-5 sentences.]

### Identity
[3-5 sentences.]

### Communication Style
[2-4 sentences.]

## Principles

1. [Principle]
(Minimum 6 principles.)

## Operational Framework

### Process
1. [Step — concrete, with input/output]
(Minimum 5 steps.)

### Decision Criteria
- When to [A] vs [B]: [criteria]
(Minimum 3 decision criteria.)

## Voice Guidance

### Vocabulary — Always Use
- [term]: [why]
(Minimum 5.)

### Vocabulary — Never Use
- [term]: [why]
(Minimum 3.)

### Tone Rules
- [Rule]
(Minimum 2.)

## Output Examples

### Example 1: [Scenario]
[COMPLETE example — 15+ lines, fully realized, not a skeleton.]

### Example 2: [Scenario]
[Another complete example — 15+ lines.]

## Anti-Patterns

### Never Do
1. [Mistake]: [Why harmful]
(Minimum 4.)

### Always Do
1. [Practice]: [Why]
(Minimum 3.)

## Quality Criteria

- [ ] [Criterion]
(Minimum 3 criteria.)

## Integration

- **Reads from**: [inputs]
- **Writes to**: [output]
- **Triggers**: [pipeline step]
- **Depends on**: [other agents/data]
```

---

## Naming Rules

- **Format:** "FirstName LastName" (exactly 2 words, always)
- **First name:** Sci-fi character reference (Foundation, Tron, Blade Runner, Ghost in the Shell, Cyberpunk)
- **Last name:** Professional function term in English (Copy, QA, Search, Metrics, Audit…)
- **Exception:** Architect agent uses functional name only ("Arquiteto", "Architect")
- **System agents** (Pietro Prompt, Arquiteto): use `thin` profile, exempt from 2-word name rule for the Architect

## Frontmatter Fields Reference

| Field | Required | Values |
|---|---|---|
| `id` | Yes | `"squads/{code}/agents/{agent-id}"` |
| `name` | Yes | `"FirstName LastName"` |
| `title` | Yes | Human-readable role title |
| `icon` | Yes | Single emoji |
| `squad` | Yes | Squad code string |
| `execution` | Yes | `inline` or `subagent` |
| `skills` | Yes | Array (can be empty `[]`) |
| `tasks` | No | Ordered list of `tasks/{file}.md` paths |
