# Scoring Rubric — Full Reference
# Load when: MODE 3 (SCORE) is active and detailed justification is needed

---

## [C] Clarity (Clareza)
**Key question:** Is the objective obvious and unambiguous?

| Score | Anchor |
|-------|--------|
| 10/10 | Direct instruction, no vague terms, single clear objective |
| 7/10 | Clear main intent, minor ambiguity in secondary constraints |
| 5/10 | Understandable but requires model to "guess" parts of the intent |
| 3/10 | Multiple possible interpretations; model will likely choose wrong one |
| 0/10 | Contradictory or excessively confusing prompt |

---

## [S] Specificity (Especificidade)
**Key question:** Does the prompt constrain the model enough to avoid unwanted variation?

| Score | Anchor |
|-------|--------|
| 10/10 | Defines persona, context, technical details, depth level |
| 7/10 | Defines task and context but missing expertise level or constraints |
| 5/10 | Defines the task but ignores context or required expertise |
| 3/10 | Very generic with minimal constraints |
| 0/10 | Generic prompt (e.g., "write about X") |

---

## [F] Format (Formato)
**Key question:** Is the output format defined in an auditable way?

| Score | Anchor |
|-------|--------|
| 10/10 | Specifies exact structure (JSON with keys X/Y, table with columns A/B/C) |
| 7/10 | Specifies format type but missing internal structure details |
| 5/10 | Suggests a format ("as a list") without structural specifics |
| 3/10 | Vague format hint ("make it organized") |
| 0/10 | No format mentioned; fully model-dependent |

---

## [R] Robustness (Robustez)
**Key question:** Does the prompt handle error cases and unexpected inputs?

| Score | Anchor |
|-------|--------|
| 10/10 | Includes fallback protocol + instructions for insufficient data |
| 7/10 | Handles common edge cases but missing explicit fallback |
| 5/10 | Mentions what to avoid but no failure-mode behavior defined |
| 3/10 | Minimal error handling, assumes mostly good input |
| 0/10 | Assumes input will always be perfect |

---

## [P] Portability (Portabilidade)
**Key question:** Does the prompt work consistently across different models?

| Score | Anchor |
|-------|--------|
| 10/10 | Standard Markdown, no proprietary syntax, tested on 3+ models |
| 7/10 | Mostly portable, uses one platform-specific feature that's easily adapted |
| 5/10 | Depends heavily on one model's characteristic but is adaptable |
| 3/10 | Uses proprietary features that require significant rewriting |
| 0/10 | Only works on one specific platform due to restricted system commands |

---

## Score Calculation

**Total = arithmetic mean of C + S + F + R + P**

| Total Range | Classification | Recommended Action |
|-------------|---------------|-------------------|
| 9.0–10 | **Elite** | Production-ready. Suitable for automation. |
| 7.0–8.9 | **Strong** | Good for manual use. Minor format/robustness tweaks. |
| 5.0–6.9 | **Average** | Requires significant structural revision. |
| < 5.0 | **Weak** | High hallucination/inconsistency risk. Rebuild. |
