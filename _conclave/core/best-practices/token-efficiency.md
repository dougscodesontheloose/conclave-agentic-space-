# Token Efficiency & Context Management

## Objective
To ensure AI agents operate with maximum token efficiency, preventing context window exhaustion (amnesia), reducing costs, and accelerating response times during complex executions.

## Core Rules

1.  **Strict Diff Usage:** Never rewrite entire files unless it's a new file creation. Always use Diffs or line-specific instructions for modifications.
2.  **Log Truncation:** Do not pass hundreds of lines of logs (e.g., from scrapers or compilers) to the next step. Extract only the success metric, error root cause, or essential insight.
3.  **Context Condensation:** During long multi-step pipelines, periodically summarize the context. Discard intermediate scratchpads.
4.  **Tertiary Log System:** Before discarding heavy context, extract the essential learnings and save them to a `.md` file in `_conclave/_memory/tertiary-logs/` with a timestamp. This prevents permanent amnesia of critical details.
5.  **Conciseness:** Avoid long confirmatory monologues. Acknowledge tasks briefly and return status/results immediately.
