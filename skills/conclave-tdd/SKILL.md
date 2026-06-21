---
name: conclave-tdd
description: >
  Output-Contract-First development protocol for Conclave agents. The agent
  declares the exact structure, format, and key elements of its output BEFORE
  generating any content — then produces the content — then self-validates
  against the declared contract. Prevents output drift, lazy generation, and
  "fill-in-later" placeholders. Invoke on any agent step where output quality
  is non-negotiable.
description_pt-BR: >
  Protocolo de Desenvolvimento Contrato-Primeiro para agentes do Conclave.
  O agente declara a estrutura exata, formato e elementos-chave do seu output
  ANTES de gerar qualquer conteúdo — produz o conteúdo — depois valida contra
  o contrato declarado. Previne output drift, geração preguiçosa e placeholders.
type: prompt
version: "1.0.0"
categories: [quality, process, tdd, output-contract]
contract:
  inputs:
    - name: step_instructions
      required: true
      description: "The step file or task instructions the agent will execute"
    - name: quality_criteria
      required: false
      description: "Optional external quality criteria from skill contract or squad brief"
  quality_criteria:
    - "Output includes a '## Output Contract' section written BEFORE the main content"
    - "Output Contract declares: structure (sections/elements), format, length target, and at least 2 specific quality constraints"
    - "Main content matches the declared structure — no undeclared sections, no missing declared sections"
    - "Output includes a '## Self-Validation' section at the end listing each contract item as pass/fail"
    - "No placeholder text in the final output: no TODO, TBD, [insert X], 'add content here'"
  on_failure: retry_previous
---

# Output-Contract-First Protocol (Conclave TDD)

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


> "Declare what you'll build. Build what you declared. Prove you built it."

## Why This Exists

Agents drift. Without a declared target, generation follows the path of least resistance:
generic structures, safe formats, filler sentences. The output might be technically
complete but fail to deliver what was actually needed.

Output-Contract-First fixes this by making the agent commit to a specific output shape
before generating — the same way a test defines what "correct" means before the code is
written.

## The Three Phases

### Phase R — Red: Declare the Contract

Before generating ANY substantive content, write a `## Output Contract` block.

```markdown
## Output Contract

**Format:** {the exact output format — e.g., "LinkedIn post, prose, 200-280 words"}
**Structure:**
- {element 1: e.g., "Opening hook — 1-2 lines, creates tension or poses a question"}
- {element 2: e.g., "Body — 3-4 paragraphs, each advancing one argument"}
- {element 3: e.g., "Closing CTA — 1 line, ends with a question or provocation"}

**Quality constraints:**
- {constraint 1: measurable — e.g., "No bullet lists"}
- {constraint 2: measurable — e.g., "Contains at least one specific data point or example"}
- {constraint 3 (optional): measurable}

**What I will NOT do:**
- {anti-pattern 1 — e.g., "No generic opener ('In today's world...')"}
- {anti-pattern 2 — e.g., "No closing with 'hope this helps'"}
```

**Rules for the Contract block:**
- Write it cold — before reading the input material for generation purposes
- Every structural element must be specific enough to fail: "good intro" is not a contract item; "opening hook under 2 lines that names a concrete problem" is
- The Contract is your commitment to the user, not a description of what you plan to attempt

---

### Phase G — Green: Generate Against the Contract

Produce the content. Keep the Output Contract block visible at the top of your output.

**During generation, actively reference the Contract:**
- Before writing each section, re-read the corresponding Contract item
- If you find the Contract was wrong (the format doesn't serve the content), STOP and revise the Contract — never silently deviate from it
- If you are tempted to add something not in the Contract, question whether the Contract was underspecified, then update the Contract first

**Prohibited during generation:**
- Placeholders of any kind: `TODO`, `TBD`, `[add example here]`, `[data pending]`, `content goes here`
- Deferring: "I'll refine this in the next pass" — this IS the pass
- Truncating: if the declared length is 200-280 words, produce 200-280 words, not 150 with a note to expand

---

### Phase V — Validate: Self-Check Against the Contract

After generating the main content, append a `## Self-Validation` block:

```markdown
## Self-Validation

| Contract Item | Result | Note |
|---|---|---|
| Format: {declared format} | ✅ pass / ❌ fail | {one sentence if fail} |
| Structure: {element 1} | ✅ pass / ❌ fail | |
| Structure: {element 2} | ✅ pass / ❌ fail | |
| Constraint: {constraint 1} | ✅ pass / ❌ fail | |
| Constraint: {constraint 2} | ✅ pass / ❌ fail | |
| Anti-pattern: {not X} | ✅ pass / ❌ fail | |
| No placeholders | ✅ pass / ❌ fail | |
```

**If any item is `❌ fail`:**

1. Fix it immediately — do not deliver a failing output
2. Re-run the Self-Validation block after the fix
3. If fixing one item breaks another, update the Contract to reflect the actual correct constraints (the Contract learns from the generation)
4. Maximum 2 self-correction cycles. After 2, surface to the user:

```text
⚠️ TDD self-correction limit reached.
Failing items after 2 cycles:
- {item}: {why it keeps failing}

This may indicate a conflict in the contract or an instruction ambiguity.
Review the step instructions and quality criteria before retrying.
```

---

## Output Structure (Required)

Every output from an agent using this skill MUST follow this sequence:

```
## Output Contract          ← Phase R (written first, before content)
[contract block]

## {Main Content Title}     ← Phase G (the actual deliverable)
[generated content]

## Self-Validation          ← Phase V (always last)
[validation table]
```

The `## Output Contract` and `## Self-Validation` blocks are **informational infrastructure** — they are stripped from the final deliverable before user presentation or downstream use. The pipeline runner extracts them for eval signal purposes.

---


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Contexto** — Qual a situação atual?
2. **Objetivo** — O que define o sucesso desta execução?
3. **Restrições** — O que não devemos fazer?

### Environment Variables

```env
# Nenhuma variável obrigatória estrita
```

### Dependencies

Nenhuma. Pure reasoning skill.

## When to Use This Skill

**High value:** Steps that produce the core deliverable (post, script, report, analysis), steps with complex format requirements, steps that have failed validation before.

**Optional:** Research and extraction steps (the output format is often dictated by the data, not a contract), checkpoint steps (user input, not agent output).

**Not needed:** Validate steps, plan-gate steps, and steps that simply copy or transform a file.

---


**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.

## Integration with the Eval Harness

When a `type: validate` step follows an agent step using this skill, the `## Self-Validation` block from the agent's output provides a richer signal source for the eval harness. The validator should:

1. Check whether the `## Output Contract` section is present — if absent, all criteria fail
2. Use the contract's declared items as an augmented criteria list (in addition to any `skill_contract:` criteria)
3. Emit an eval signal with the combined criteria results
