# Anti-Patterns — Full Reference
# Load when: diagnosing a prompt in IMPROVE mode that exhibits quality issues

---

## AP-01: The Verbosity Paradox
**Error:** Writing long narrative paragraphs assuming "more context is always better."
- **Symptom:** AI ignores instructions in the middle of text (lost-in-the-middle effect).
- **Fix:** Use Markdown, numbered lists, and delimiters (`###`, `---`, XML tags).
- **Bad:**
  ```
  Hi AI, how are you? I'd like you to write something about cats,
  but not too long, and please use a cute tone and talk about
  the Persian breed too...
  ```
- **Good:**
  ```
  Task: Write about cats.
  Breed: Persian.
  Tone: Cute/affectionate.
  Constraint: Max 50 words.
  ```

---

## AP-02: Isolated Negative Instructions
**Error:** Saying only "don't do X" without providing what TO do instead.
- **Symptom:** AI fixates on the prohibited term and ends up mentioning it.
- **Fix:** Combine negative constraints with positive instructions.
- **Bad:** `"Don't use technical terms."`
- **Good:** `"Use simple, accessible language. Avoid technical jargon or academic terms."`

---

## AP-03: Persona Ambiguity
**Error:** Asking the AI to be "an expert" without specifying the domain.
- **Symptom:** Generic, superficial responses.
- **Fix:** Define role, domain, experience level, and objective.
- **Bad:** `"Act as an expert."`
- **Good:** `"Act as a Senior Software Architect specializing in Java microservices."`

---

## AP-04: Missing Input Delimiters
**Error:** Pasting long text for analysis without marking where it begins and ends.
- **Symptom:** AI confuses prompt instructions with the provided content.
- **Fix:** Use XML tags or clear delimiters.
- **Bad:** `"Summarize this text: [PASTED TEXT]"`
- **Good:**
  ```
  Analyze the text delimited by <content>:
  <content>
  [TEXT HERE]
  </content>
  ```

---

## AP-05: Binary Questions on Complex Topics
**Error:** Forcing yes/no on subjects requiring nuance.
- **Symptom:** Hallucination or forced bias.
- **Fix:** Request pros/cons analysis before the conclusion.
- **Good:** `"Evaluate options A and B. List risks for each. Recommend the safest."`

---

## AP-06: Options Explosion
**Error:** Presenting too many alternatives without a default recommendation.
- **Symptom:** Model picks randomly or generates a non-committal answer.
- **Fix:** Provide one default with a narrow escape hatch for edge cases.
- **Bad:** `"You can use Python, or JavaScript, or Go, or Rust, or Java..."`
- **Good:** `"Use Python. If the task requires sub-millisecond latency, use Go instead."`

---

## AP-07: Assumed Environment
**Error:** Assuming packages, tools, or configurations are already installed.
- **Symptom:** Instructions fail silently in different environments.
- **Fix:** Include explicit setup steps (`pip install`, `npm install`).

---

## AP-08: Magic Numbers Without Justification
**Error:** Using arbitrary thresholds, limits, or values without explaining why.
- **Symptom:** Future maintainers (or the model itself) can't adapt the constraint intelligently.
- **Fix:** Always document the reasoning behind numeric constraints.
- **Bad:** `"Limit to 3 paragraphs."`
- **Good:** `"Limit to 3 paragraphs (executive summary standard for C-level readers)."`
