# Technique Registry — Full Reference
# Load when: applying techniques during BUILD or IMPROVE modes

---

## [T01] Role Prompting (Persona Assignment)
**What:** Define a specific identity, expertise level, and behavioral frame for the AI.
**When:** Always. Foundation for tone and knowledge calibration.
**Example:**
```
You are a Senior Cloud Security Architect with 20 years of experience
in banking system audits and NIST/ISO compliance frameworks.
```
**Why it works:** Constrains the probability space — the model generates from a narrower, more relevant distribution.

---

## [T02] Chain-of-Thought (Step-by-Step Reasoning)
**What:** Instruct the model to show its reasoning process before delivering the final answer.
**When:** Complex logic, calculations, multi-variable decisions, debugging.
**Example:**
```
Think step by step:
1. First identify the bottlenecks.
2. Then calculate the impact of each.
3. Finally suggest the optimal solution.
```
**Why it works:** Prevents premature token commitment. Intermediate reasoning tokens improve downstream accuracy.

---

## [T03] Few-Shot Examples (Pattern Demonstration)
**What:** Provide 2–3 input/output pairs showing the exact pattern desired.
**When:** Output format is highly specific or hard to describe in prose.
**Example:**
```
Input: "The sun rises in the east" → Output: "Astronomical phenomenon"
Input: "The stock market fell 2%" → Output: "Financial event"
Input: "[USER TEXT]" → Output: ?
```
**Why it works:** In-context learning — the model pattern-matches from examples more reliably than from abstract instructions.

---

## [T04] Output Schema (Structured Format Definition)
**What:** Define the exact structure of the response (JSON, Markdown table, YAML, CSV).
**When:** System integrations, automated pipelines, or when readability/auditability is critical.
**Example:**
```
Respond strictly in JSON:
{"id": number, "status": "active"|"inactive", "summary": string}
```
**Why it works:** Removes format ambiguity entirely. Model allocates zero tokens deciding structure.

---

## [T05] Negative Constraints (Explicit Prohibitions)
**What:** Instructions about what the AI must NOT do.
**When:** Preventing hallucination, banned terminology, unwanted styles or behaviors.
**Example:**
```
Use simple, accessible language. Avoid technical jargon, acronyms,
or academic terminology. Do not exceed 50 words.
```
**Gotcha:** Never use negatives alone — always pair with a positive alternative. "Don't use jargon" → model fixates on jargon. "Use simple language; avoid jargon" → model focuses on simplicity.

---

## [T06] Context Injection (Domain Knowledge Embedding)
**What:** Insert external data, documents, or domain-specific information into the prompt.
**When:** The AI needs facts not in its training data (private data, recent events, custom schemas).
**Example:**
```
Use the Q3 sales data below to project Q4 growth:
<data>
[EMBEDDED DATA HERE]
</data>
```
**Gotcha:** Always delimit injected content with XML tags or fences. Without delimiters, the model confuses data with instructions.

---

## [T07] Task Decomposition (Multi-Step Breakdown)
**What:** Break a complex task into ordered, manageable subtasks.
**When:** Long-form content, software development plans, strategic documents.
**Example:**
```
1. Create the outline with 5 sections.
2. Write the introduction (max 100 words).
3. Develop 3 main arguments with evidence.
4. Write the conclusion with a clear CTA.
```
**Why it works:** Prevents the model from attempting everything in one pass, which degrades quality on complex tasks.

---

## [T08] Self-Evaluation Loop (Internal QA)
**What:** Instruct the model to review its own draft before delivering the final version.
**When:** Critical outputs, legal/financial content, production-ready deliverables.
**Example:**
```
After generating the report, review it critically:
- Check for logical inconsistencies.
- Verify all claims have supporting evidence.
- Correct any errors found.
Then deliver the final version.
```
**Why it works:** Second-pass attention catches errors the first-pass generation missed.

---

## [T09] Tone Calibration (Register Definition)
**What:** Specify the linguistic register (formal, casual, technical, empathetic, authoritative).
**When:** Marketing copy, customer support, mentoring, brand-voice compliance.
**Example:**
```
Use a professional but encouraging tone, like a career mentor
speaking to a junior developer. Avoid condescension.
```
**Gotcha:** "Be friendly" is too vague. Anchor tone to a recognizable archetype or relationship.

---

## [T10] Fallback Instruction (Graceful Degradation)
**What:** Define what the AI should do when input is ambiguous, insufficient, or outside scope.
**When:** Autonomous agents, repeated-use prompts, production systems.
**Example:**
```
If you cannot determine the user's intent from their message,
respond ONLY with:
"I need more context. Please specify: [list missing info]"
Do not attempt to guess.
```
**Why it works:** Prevents hallucination on ambiguous inputs. Critical for trust in production systems.

---

## [T11] Meta-Prompting (Prompt-about-Prompts)
**What:** Prompts that instruct the AI to generate, refine, or evaluate other prompts.
**When:** Building prompt engineering tools, automation pipelines, self-improving systems.
**Example:**
```
Generate a system prompt for an AI legal assistant specialized
in contract review. The prompt must include: persona, scope
constraints, output format, and fallback behavior.
```
**Why it works:** Leverages the model's understanding of its own instruction-following to produce better instructions.

---

## [T12] ReAct Pattern (Reasoning + Acting)
**What:** Combines explicit reasoning steps with tool-use actions in an interleaved loop.
**When:** Agentic systems with access to tools (search, code execution, APIs).
**Example:**
```
Thought: I need to find the current exchange rate.
Action: search("USD to BRL exchange rate today")
Observation: [result from tool]
Thought: Now I can calculate the conversion.
Action: calculate(1000 * exchange_rate)
Final Answer: [consolidated result]
```
**Why it works:** Externalizes reasoning, making the agent's decision process auditable and debuggable.
