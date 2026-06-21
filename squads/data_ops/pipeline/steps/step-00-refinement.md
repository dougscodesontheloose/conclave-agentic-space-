---
execution: inline
agent: "pietro-prompt"
---

# Step 00: Refinement

## Context Loading
- `_conclave/state/memory/company.md`

## Instructions
### Process

1. Analyze the user's raw request and identify the business decision it should support.
2. Extract objective, dataset, target audience, metrics, time period, and expected output.
3. Flag missing context that would change the analysis materially.
4. Convert vague requests into a structured analytical brief.
5. Separate confirmed requirements from assumptions.
6. Specify whether the work belongs to data cleaning, analysis, modeling, dashboarding, or executive narrative.
7. Define success criteria before handing off to the next step.

## Output Format
```markdown
# Refined Prompt

## Objective

## Business Decision

## Available Data

## Metrics

## Assumptions

## Missing Context

## Expected Output

## Success Criteria
```

## Output Example
```markdown
# Refined Prompt

## Objective
Evaluate whether campaign performance improved after the budget shift.

## Business Decision
Decide whether to keep the new allocation for the next cycle.

## Metrics
- CAC
- ROAS
- Conversion rate

## Missing Context
- Exact date of budget shift.
- Attribution window.

## Success Criteria
The final output must show trend, driver, confidence, and recommendation.
```

## Veto Conditions

1. Missing objective.
2. Missing business decision.
3. No metric or analytical dimension defined.
4. Assumptions mixed with confirmed facts.
5. Output type unclear.

## Quality Criteria
- [ ] Clear goal.
- [ ] Business question is explicit.
- [ ] Metrics are named.
- [ ] Missing context is visible.
- [ ] Handoff is actionable for analyst or scientist.
