---
name: conclave-debugging
description: >
  Systematic debugging protocol for Conclave agents. Enforces root-cause
  investigation before any fix attempt. Four mandatory phases: Observe,
  Hypothesize, Test, Fix. Invoked when an agent encounters an unexpected
  failure, broken output, or recurring error pattern.
description_pt-BR: >
  Protocolo sistemático de debugging para agentes do Conclave. Exige investigação
  de causa-raiz antes de qualquer tentativa de correção. Quatro fases obrigatórias:
  Observar, Hipotetizar, Testar, Corrigir. Invocado quando um agente encontra
  falha inesperada, output quebrado, ou padrão de erro recorrente.
type: prompt
version: "1.0.0"
categories: [debugging, quality, systematic, process]
contract:
  inputs:
    - name: error_description
      required: true
      description: "The symptom, error message, or unexpected behavior being investigated"
    - name: failing_artifact
      required: false
      description: "The file, output, or step that produced the wrong result"
  quality_criteria:
    - "Root cause is stated explicitly before any fix is proposed"
    - "At least one diagnostic command or observation was executed before hypothesizing"
    - "The hypothesis was tested against evidence — not assumed to be correct"
    - "Fix is minimal — addresses only the confirmed root cause, not adjacent issues"
    - "The proposed fix includes a verification step to confirm the problem is resolved"
  on_failure: halt
---

# Conclave Debugging Protocol

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


> "A fix without a root cause is a guess wearing a solution's clothes."

## The Non-Negotiable Rule

**NO FIX MAY BE PROPOSED BEFORE A ROOT CAUSE IS STATED.**

If you are about to suggest a correction and you cannot complete the sentence
"The root cause is ___", you are not ready to fix. Return to Phase 2.

This rule exists because patching symptoms without understanding causes creates
three new bugs for every one it hides.

---

## The Four Phases

Execute these phases in strict order. Never skip. Never merge two into one.

### Phase 1 — Observe

Gather raw diagnostic evidence before forming any opinion about the cause.

**Required actions:**

1. Read the exact error message or failure output in full — never paraphrase it yet
2. Identify the boundary: what was the last known-good state vs. the first failure point?
3. Collect the relevant context:
   - The input that triggered the failure
   - The step or agent that produced the broken output
   - Any recent changes to the squad, skill, or pipeline (check `runs.md` and `audit.jsonl`)
4. Reproduce the failure if possible — confirm you are seeing the same symptom
5. Record findings as a numbered list: "What I observed: ..."

**Output of Phase 1:** A factual, evidence-only description. No "probably", no "I think".

**Anti-patterns (these terminate Phase 1 prematurely):**
- "It looks like X is causing..." → that is Phase 2, not Phase 1
- Skipping reproduction to save time
- Reading only partial error output

---

### Phase 2 — Hypothesize

Form one specific, falsifiable hypothesis based only on the Phase 1 evidence.

**Required actions:**

1. State the hypothesis in one sentence: *"I believe the root cause is [X] because [evidence from Phase 1]."*
2. Identify what would be true if this hypothesis is correct
3. Identify what would be true if this hypothesis is wrong
4. Rank competing hypotheses if more than one is plausible (highest-evidence first)

**Output of Phase 2:** One ranked hypothesis list. Most likely cause at the top.

**Anti-patterns:**
- "There could be many causes..." → pick one, test it, move on
- Forming hypothesis before completing Phase 1 evidence collection
- Hypothesis that cannot be tested: "something in the context is off"

---

### Phase 3 — Test

Test the top hypothesis against new evidence. One variable at a time.

**Required actions:**

1. Design the smallest test that would confirm or refute the hypothesis
2. Execute it (bash command, file read, re-run the step, etc.)
3. Compare result to what Phase 2 predicted
4. Conclude:
   - **Confirmed** → proceed to Phase 4 with this root cause
   - **Refuted** → return to Phase 2 with the next hypothesis. Increment counter.

**Escalation rule:** If 3 consecutive hypotheses are refuted, STOP patching.
Surface to the user:
```
🔍 Debugging escalation — 3 hypotheses refuted.
Observed symptom: {symptom}
Hypotheses tested: {list}
None confirmed. This may be an architectural issue, not a surface bug.
Recommend: review {step/skill/pipeline design} before retrying.
```

**Output of Phase 3:** Confirmed root cause — one sentence, specific, testable.

**Anti-patterns:**
- Changing two things at once and calling it a test
- Declaring hypothesis confirmed without running a test
- Treating "test passed" as "fixed" before Phase 4

---

### Phase 4 — Fix

Apply the minimal fix that addresses the confirmed root cause. Nothing more.

**Required actions:**

1. State the fix in one sentence before implementing it
2. Implement only what the root cause demands — do not refactor adjacent code,
   do not add "while I'm here" improvements
3. Verify the fix resolves the original symptom (re-run the failing step or check)
4. Write a one-line note in the relevant `## Técnico` section of the squad's
   `memories.md` if the fix reveals a non-obvious pattern:
   *"[date] — {root cause}: {fix applied}"*

**Output of Phase 4:** Fixed artifact + verification result + optional memory note.

**Anti-patterns:**
- Implementing a "better" fix than the minimal one while you're there
- Skipping verification after applying the fix
- Applying the same fix pattern from a different bug without testing

---

## Quick Reference

```
Phase 1 — OBSERVE:    What exactly happened? Collect raw evidence.
Phase 2 — HYPOTHESIZE: Why? One sentence, one cause, falsifiable.
Phase 3 — TEST:       Is the hypothesis true? One variable at a time.
Phase 4 — FIX:        Minimal correction for the confirmed cause. Verify.
```

**Escalation triggers (present to user immediately):**
- 3 refuted hypotheses → architectural review
- Fix applied but symptom persists → return to Phase 1 (new evidence exists)
- Root cause involves a Conclave core file (`runner.pipeline.md`, `security.policy.md`, charter) → do not fix unilaterally; surface to user

---

## Integration with Conclave

When this skill is active in a squad agent:

- The agent's output for any debug task MUST include a labeled section:
  `## Debug Trace — {phase reached}` before any fix is proposed
- If the agent reaches Phase 4 and the fix touches a shared resource
  (`memories.md`, `squad.yaml`, pipeline files), it must present the fix
  as a proposal and wait for user confirmation before writing
- Eval criteria for this skill are measured against the **Debug Trace** section —
  POSEIDON will flag runs where the trace is missing or jumps directly to Phase 4


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

Requer ambiente de execução padrão do Conclave.
