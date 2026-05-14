---
name: Token Efficiency & Context Management
description: Faz a IA gastar menos tokens, responder mais rápido e evitar limites de contexto, utilizando diffs e logs terciários.
type: core_protocol
tags: [system, optimization, core]
---

# Skill: Token Efficiency & Context Management

**Core principle:** Sistemas resilientes assumem a falha como padrão e a recuperação como regra.


Esta skill introduz um protocolo estrito para evitar desperdício de tokens, prevenir a exaustão da janela de contexto ("amnésia") e acelerar as respostas durante as execuções do pipeline do Conclave.

## O Protocolo de Compressão

1. **Uso Exclusivo de Diffs:** 
   Nunca reescreva ou imprima no console um arquivo inteiro (salvo se for a criação inicial do arquivo). Ao fazer edições ou sugerir código, utilize sempre o formato de Diffs ou indique as linhas que serão modificadas.
2. **Truncamento Inteligente de Logs:**
   Se uma ferramenta (como scraper ou compilador) retornar centenas de linhas de log, não as repasse para o prompt. Filtre apenas o resumo do sucesso, do erro ou as métricas essenciais.
3. **Resumo Periódico de Contexto:**
   Ao realizar uma cadeia de várias operações complexas, antes que o contexto se torne longo demais, faça um "Resumo Executivo" do que já foi alcançado e descarte os logs intermediários.

## Sistema de Logs Terciário (Mitigação de Amnésia)

A compressão excessiva pode gerar amnésia de curto prazo. Para evitar a perda permanente de nuances contextuais que já foram processadas:

- Quando você for "limpar" o contexto da sua memória operacional ou condensar logs pesados, extraia os aprendizados e chaves essenciais e os salve no **Sistema de Logs Terciário**.
- **Caminho:** Salve esses resumos sucintos na pasta `_conclave/state/memory/tertiary-logs/`.
- **Formato:** Crie arquivos `.md` com timestamp e contexto (ex: `2026-04-22-scraping-insights.md`).
- Se precisar recuperar detalhes passados que foram comprimidos, consulte esse diretório.

## Heurística de Resposta

- Seja conciso.
- Responda apenas o que foi solicitado.
- Evite monólogos confirmatórios longos ("Entendi, agora vou fazer X, Y e Z..."). Aja e retorne o status.


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

Use `Token Efficiency & Context Management` when you need to:
- Maintain system health and operational quality
- Apply development best practices
- Support the infrastructure that other skills depend on

**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.


## Inputs

| Input | Required | Description |
|---|---|---|
| **Target scope** | Varies | Files, directories, or codebase to operate on |
| **Configuration** | No | Settings or preferences for the operation |


## Output Format

| Output | Format | Location |
|---|---|---|
| **Status report** | Markdown or terminal | Displayed to user |
| **Changes applied** | Log | Inline in response |


## Cost

| Component | Cost |
|---|---|
| Apify actor runs | ~$0.01–0.05 per run (varies by actor) |
| Apify free tier | $5/month included |
| LLM reasoning | Free (included in agent session) |

## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: token-efficiency — [finding]` | `[OPERACIONAL]: token-efficiency — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: token-efficiency — [param] works better as [value]` | `[OPERACIONAL]: token-efficiency — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: token-efficiency — [insight]` | `[ESTRATÉGICO]: token-efficiency — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Output completeness:** All required fields/sections are populated
- [ ] **No silent failures:** Every step that was attempted has a status in the output
- [ ] **Format valid:** Output matches the documented schema
- [ ] **User checkpoint:** Present results summary to user before finalizing

**If any check fails:** Report the specific gap and ask user how to proceed.

