# Pipeline Simulation for Skill Evals

When testing skills that will run inside the Conclave pipeline, it's important to replicate the real execution environment. The standard eval loop (draft → test → review → improve) works best when the test environment matches production.

## Why This Matters

In the real pipeline, your skill body is one piece of a larger context:

```
Agent persona (~100-200 lines) → Format best-practice (~200-400 lines) → SKILL body (~100-500 lines) → Step instructions (~60-120 lines)
```

A skill that works perfectly in isolation may fail when:
- The agent's persona contradicts the skill's instructions (persona collision)
- The combined context exceeds the ~15k word budget (context bloat)
- The step's veto conditions catch patterns the skill produces (format mismatch)

## Replicating the Pipeline Environment

### Step 1: Create a Realistic Agent Context

Instead of running evals with just the skill, compose a context that mirrors what the Pipeline Runner builds:

```markdown
# Agent Context (simulated)

## Agent Persona
[Read a real .agent.md from an existing squad, or create a minimal one:]

---
id: "test-agent"
name: "Test Agent"
title: "Domain Specialist"
icon: 🧪
execution: inline
skills:
  - {your-skill-name}
---

### Role
A specialist in {domain relevant to the skill}.

### Identity
Methodical, detail-oriented, follows frameworks precisely.

### Communication Style
Clear and structured. Uses numbered lists.

## Principles
1. Follow the operational framework step by step
2. Apply quality criteria to every output
3. Never skip validation steps

--- SKILL INSTRUCTIONS ---

## {Your Skill Name}
{Your SKILL.md body goes here}
```

### Step 2: Add Format Context (if applicable)

If the skill will be used alongside a format best-practice (e.g., the agent creates Instagram content while using your scraping skill), include the format:

```markdown
--- FORMAT: Instagram Feed & Carousels ---

[Read _conclave/core/best-practices/instagram-feed.md and insert the body here]
```

### Step 3: Add Step Instructions

Real pipeline steps have structure. Include step-like instructions in your eval prompt:

```markdown
## Step Instructions (simulated)

### Context Loading
- Read {input file description}

### Process
1. {What the agent should do with the skill}
2. {Next concrete step}
3. {Final step producing output}

### Output Format
{Template of expected output}

### Veto Conditions
Reject and redo if:
1. {Condition that would trigger a redo}
2. {Another condition}

### Quality Criteria
- [ ] {Criterion 1}
- [ ] {Criterion 2}
```

### Step 4: Estimate Context Size

Before running the eval, estimate the total context:

| Component | Typical Size |
|-----------|-------------|
| Agent persona | 100-200 lines (~1-2k words) |
| Format best-practice | 200-400 lines (~3-5k words) |
| SKILL body | Variable — **your skill** |
| Step instructions | 60-120 lines (~1-2k words) |
| Input data | Variable |
| Squad memory | 20-50 lines (~0.5k words) |
| Company context | 50-100 lines (~1k words) |

**Target:** Total context < 15,000 words.

If your skill body pushes the total past 15k words, the Pipeline Runner will summarize it to the first 50 lines or `## Quick Start` section. Test with the summarized version too.

### Step 5: Run With Veto Conditions Active

In the real pipeline, after an agent produces output, the Runner checks veto conditions. Include veto-style checks in your eval:

```
After the skill produces output, verify:
1. Output is not empty
2. Output follows the specified format
3. Output does not contain placeholder text
4. [Domain-specific veto conditions]

If ANY veto is triggered, revise and re-attempt (max 2 attempts).
```

## Eval Prompt Template

Here's a complete template for a pipeline-simulated eval:

```
You are {Agent Name}, a {role description}.

{Full agent .agent.md body — persona, principles, voice guidance}

--- SKILL INSTRUCTIONS ---

## {Skill Name}
{Full SKILL.md body}

--- FORMAT: {format name} (if applicable) ---

{Format best-practice body}

---

## Your Task

### Context
{Background information the step would provide}

### Input
{Data from previous pipeline step — simulate with realistic content}

### Process
1. {Concrete step 1}
2. {Concrete step 2}
3. {Concrete step 3}

### Output
Save results to: {output path}

### Veto Conditions
Reject and redo if:
1. {Condition 1}
2. {Condition 2}

### Quality Criteria
- [ ] {Criterion 1}
- [ ] {Criterion 2}
- [ ] {Criterion 3}
```

## What to Watch For

When reviewing pipeline-simulated eval results vs isolated eval results:

1. **Persona compliance**: Does the agent follow its persona AND the skill, or does one override the other?
2. **Format adherence**: If a format best-practice is injected, does the output respect both the format rules AND the skill's guidance?
3. **Context window pressure**: With the full context loaded, does the agent still follow all skill instructions, or does it skip/simplify some?
4. **Veto condition interaction**: Do the step's veto conditions catch legitimate output that the skill produces? This signals a compatibility issue.
5. **Vocabulary consistency**: The agent's voice guidance, the skill's terminology, and the format's vocabulary should harmonize, not conflict.
