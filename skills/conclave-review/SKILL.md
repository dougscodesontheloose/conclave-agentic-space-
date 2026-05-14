---
name: conclave-review
description: >
  Two-stage blocking review skill for Conclave agents. Stage 1 evaluates spec
  compliance (did the agent do what was asked?). Stage 2 evaluates quality
  (is the output premium or AI slop?). Returns a structured machine-readable
  verdict — APPROVE, CONDITIONAL APPROVE, or REJECT — that the pipeline runner
  enforces as a hard gate before advancing. Pair with type:review pipeline steps.
description_pt-BR: >
  Skill de revisão bloqueante em dois estágios para agentes do Conclave.
  Estágio 1 avalia conformidade com a especificação. Estágio 2 avalia qualidade.
  Retorna um veredicto legível por máquina que o runner executa como gate duro.
type: prompt
version: "1.0.0"
categories: [review, quality, blocking, two-stage]
contract:
  inputs:
    - name: artifact
      required: true
      description: "The content file, output, or step result being reviewed"
    - name: original_brief
      required: true
      description: "The step instructions or squad goal that defined what should be produced"
    - name: quality_criteria
      required: false
      description: "Explicit criteria list from skill contract or review step file"
  quality_criteria:
    - "Review output includes a scoring table with one row per criterion"
    - "Every score below 7/10 includes a 'Required change:' with specific fix instructions"
    - "Final line of output is exactly one of: VERDICT: APPROVE, VERDICT: REJECT, or VERDICT: CONDITIONAL APPROVE"
    - "Stage 1 (spec compliance) is evaluated separately from Stage 2 (quality)"
    - "At least one 'Strength:' item is present even in a REJECT review"
  on_failure: halt
---

# Conclave Review — Two-Stage Blocking Review

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


> "Stage 1 asks: did you build what was asked? Stage 2 asks: is it worth keeping?"

## Governing Best Practice

This skill operates on the full methodology defined in:
`_conclave/core/best-practices/review.md`

Read and internalize that file before proceeding. It defines the scoring system
(1-10), decision thresholds (approve ≥ 7/10, reject if any criterion < 4/10),
required output format, vocabulary rules, and the Council of Agents framework.

This skill file defines **what to review** and **in which stages**. The best practice
defines **how to review**.

---

## The Two Stages

### Stage 1 — Spec Compliance

**Question:** Did the agent produce what the brief asked for?

Load the original brief (step instructions, squad goal, or checkpoint response that
defined this task). Compare it against the artifact.

**Evaluate:**
- Does the artifact address the stated objective?
- Are all required elements from the brief present?
- Is the format, length, and structure what was requested?
- Did the agent stay within scope (no unexplained additions or omissions)?

**Scoring for Stage 1** uses the same 1-10 scale. A score below 4/10 on any
spec-compliance criterion is a hard rejection trigger — regardless of Stage 2.

A spec failure means the agent misunderstood or ignored the task. Quality cannot
compensate for building the wrong thing.

---

### Stage 2 — Quality

**Question:** Is this output worth delivering?

Load the quality criteria from:
1. The `skill_contract` listed in the review step frontmatter (if present)
2. Any `## Criteria` section in the review step file
3. The squad's `memories.md` — `## Proibições Explícitas` section (prohibitions always apply)
4. The Adversarial Layer from `review.md` (AI Slop / Aesthetic Drift / Strategic Intent)

**Evaluate each criterion individually.** Do not average away a critical failure.

---

## Structured Review Output Format

Your output MUST follow this exact structure:

```
══════════════════════════════════════
 CONCLAVE REVIEW — {stage: SPEC | QUALITY | BOTH}
══════════════════════════════════════

Artifact: {filename or description}
Reviewer: {your agent name}
Cycle: {N} of {max_review_cycles}
Date: {YYYY-MM-DD}

──────────────────────────────────────
 STAGE 1 — SPEC COMPLIANCE
──────────────────────────────────────
| Criterion                  | Score  | Summary                        |
|----------------------------|--------|--------------------------------|
| {spec criterion 1}         | N/10   | {one-line justification}       |
| {spec criterion 2}         | N/10   | {one-line justification}       |

Stage 1 Score: {average}/10
Stage 1 Result: PASS / FAIL

──────────────────────────────────────
 STAGE 2 — QUALITY
──────────────────────────────────────
| Criterion                  | Score  | Summary                        |
|----------------------------|--------|--------------------------------|
| {quality criterion 1}      | N/10   | {one-line justification}       |
| {quality criterion 2}      | N/10   | {one-line justification}       |

Stage 2 Score: {average}/10
Stage 2 Result: PASS / FAIL

──────────────────────────────────────
 DETAILED FEEDBACK
──────────────────────────────────────

Strength: {what genuinely works — specific, not vague}

{For every score below 7/10:}
Required change: {exact location} — {what is wrong} — {how to fix it, specific enough to act on}

{For suggestions that are not blocking:}
Suggestion (non-blocking): {improvement that would elevate quality but is not required}

──────────────────────────────────────
 PATH TO APPROVAL (if REJECT)
──────────────────────────────────────
1. {Required change 1 — restate concisely}
2. {Required change 2}
...
Expected outcome: if these changes are made, the artifact is expected to reach approval threshold.

══════════════════════════════════════
 OVERALL: {combined average}/10
══════════════════════════════════════
VERDICT: {APPROVE | REJECT | CONDITIONAL APPROVE}
```

**The `VERDICT:` line is machine-parsed by the pipeline runner. Rules:**
- It must be the last line of your output
- It must be exactly one of the three values above — no extra words, no punctuation after
- `CONDITIONAL APPROVE` = spec passes + overall ≥ 7/10 + at least one non-critical criterion between 4-6/10
- `APPROVE` = spec passes + overall ≥ 7/10 + no criterion below 4/10
- `REJECT` = spec fails OR overall < 7/10 OR any criterion below 4/10

---

## Running Only One Stage

If the review step frontmatter sets `stage: spec` — run Stage 1 only. Omit Stage 2 table.
If the review step frontmatter sets `stage: quality` — run Stage 2 only. Omit Stage 1 table.
Default (`stage: both`) — run both.

The `VERDICT:` line is still required regardless of which stage(s) ran.

---

## The Council of Agents (mandatory for Stage 2)

Before writing the Stage 2 scoring table, briefly surface two internal voices:

**The Skeptic:** What is the strongest case for rejecting this? What risks or
weaknesses does an adversarial reader find?

**The Visionary:** What is genuinely strong here? What would be lost if this were rejected?

Present these as a two-line block before the Stage 2 table:
```
Skeptic: {one sentence — strongest objection}
Visionary: {one sentence — strongest defense}
```

The Judge (you) then scores based on criteria, informed by both perspectives.

---

## Prohibited Behaviors

- **Never approve without reading the full artifact.** Partial reads produce partial verdicts.
- **Never score without justification.** Every row in the scoring table has a "Summary" column — fill it.
- **Never reject without a Path to Approval.** If you REJECT, you must explain exactly what would make it approvable.
- **Never let cycle pressure inflate scores.** Cycle 3 of 3 is not a reason to approve a weak artifact. It is a reason to escalate.
- **Never issue a verdict on a missing artifact.** If `inputFile` does not exist or is empty, return `VERDICT: REJECT` with the single required change: "Produce the artifact."


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
