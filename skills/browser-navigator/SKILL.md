---
name: Browser Navigator
description: Transforma qualquer pesquisador em um navegador autônomo resiliente (Inspirado em browser-use).
type: prompt
tags: [system, automation, scraping]
---

# Skill: Browser Navigator

**Core principle:** Sistemas resilientes assumem a falha como padrão e a recuperação como regra.


Esta skill injeta a capacidade de **Navegação Autônoma** no agente. Ela deve ser usada sempre que a tarefa exigir interação dinâmica (cliques, preenchimento de formulários, navegação em SPAs) em vez de simples extração de texto estático.

## O Loop de Decisão

Você deve seguir rigorosamente este loop para cada sub-tarefa:

1.  **Observação Visual:** Use `browser_take_screenshot` para ver o estado real. Não confie apenas no que você *acha* que aconteceu no comando anterior.
2.  **Análise de Obstáculos:** Procure por modais de cookies, popups de newsletter ou botões de login que podem estar obstruindo sua tarefa.
3.  **Ação Mínima:** Execute uma ação que remova o obstáculo ou aproxime você do objetivo.
4.  **Verificação:** Após agir, tire um novo screenshot. Se o screenshot não mostrar a mudança esperada, tente uma abordagem diferente (seletores diferentes ou espera adicional).

## Ações Compostas (Cheat Sheet)

Sempre que possível, combine ferramentas para estas manobras:

- **Auth Scout:** Verifique se há botões de "Sign In" ou "Log In". Se encontrados e você não tiver credenciais, peça ao usuário.
- **Dynamic Scroller:** Se o conteúdo carregar dinamicamente, execute `browser_press(key="PageDown")` várias vezes seguidas de pequenos sleeps até que novos elementos apareçam no screenshot.
- **Popup Smasher:** Priorize clicar no `[X]` ou botões de `Close/Accept` antes de interagir com o conteúdo principal.

## Restrições

- **Max Steps:** Você tem um limite de **5 iterações** por tarefa. Se falhar após 5 passos, pare e peça ajuda enviando o último screenshot.
- **Verificação Pós-Clique:** Nunca assuma que um clique funcionou sem ver o resultado em um screenshot.


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Nenhuma. Pure reasoning skill.

## When to Use

Use `Browser Navigator` when you need to:
- Collect data from external sources for downstream analysis
- Feed data into research, qualification, or monitoring pipelines
- Build datasets for competitive intelligence or lead generation

**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.


## Inputs

| Input | Required | Description |
|---|---|---|
| **Keywords/Query** | Varies | Search terms or filters |
| **API credentials** | Yes | API key (set via environment variable) |
| **Output format** | No | `json` (default) or `csv` |


## Output Format

| Output | Format | Location |
|---|---|---|
| **Raw data** | JSON or CSV | Current working directory or specified path |
| **Summary** | Markdown table | Displayed to user in terminal |
| **Error log** | Inline notes | Included in output when sources fail |


## Cost

Free. Uses public APIs that do not require paid credentials.

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **API rate limit / 429** | HTTP 429 or `rate_limit` in response | Wait 60s, retry with exponential backoff (max 3 retries) |
| **API key missing/invalid** | HTTP 401/403 or env var not set | Log `❌ Missing API key: [VAR_NAME]`. Stop and inform user with setup instructions |
| **Target page structure changed** | Zero results from a previously working source | Log `⚠️ 0 results from [source]`. Continue with other sources, flag in output |
| **Network timeout** | No response within configured timeout | Retry once. If still failing, skip source and note in output |
| **Empty dataset returned** | Valid API response but 0 results | Distinguish "no data exists" vs "query too narrow". Suggest query adjustments |

**Principle:** Never fail silently. Every error must produce a visible log line and a note in the final output.


## Composability


**Feeds into:**
- `competitor-intel`
- `customer-discovery`
- `industry-scanner`
- `lead-qualification`

**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: browser-navigator — [finding]` | `[OPERACIONAL]: browser-navigator — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: browser-navigator — [param] works better as [value]` | `[OPERACIONAL]: browser-navigator — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: browser-navigator — [insight]` | `[ESTRATÉGICO]: browser-navigator — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Data completeness:** At least 1 source returned results. If all sources failed, the output must explain why
- [ ] **No silent failures:** Every source that was attempted has a status (success/partial/failed) in the output
- [ ] **Deduplication applied:** No duplicate entries in the final dataset
- [ ] **Output format valid:** CSV/JSON is well-formed and parseable
- [ ] **User checkpoint:** Present summary to user before proceeding to downstream skills

**If any check fails:** Stop, report the failure, and ask the user how to proceed.

