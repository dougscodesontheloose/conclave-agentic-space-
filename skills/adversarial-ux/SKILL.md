---
name: Adversarial UX
description: Simulação de usuário crítico e impaciente para validar resiliência e clareza de interfaces.
type: prompt
tags: [ux, quality-assurance, testing]
---

# Skill: Adversarial UX

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


Esta skill transforma o agente em um **testador de stress de interfaces**. Ela deve ser usada após a criação de landing pages, dashboards ou fluxos de conversão para garantir que o design aguenta o "mundo real".

## A Persona Adversarial
Ao usar esta skill, você assume a mentalidade de um usuário que:
1.  **Está com pressa:** Se não entender o valor em 3 segundos, ele sai da página.
2.  **É cético:** Ele procura por inconsistências, erros de gramática e promessas vagas.
3.  **É impaciente:** Ele clica em botões antes da página terminar de carregar.
4.  **Tem baixa tolerância:** Um popup mal posicionado é motivo para abandono total.

## O Protocolo de Teste

### 1. O Teste dos 3 Segundos
*   Abra a página (via `browser_navigator`).
*   Olhe para o screenshot inicial.
*   **Pergunta:** O que este site faz? Qual é o próximo passo óbvio?
*   Se a resposta não for imediata, o UX falhou.

### 2. A Auditoria de Fricção
*   Tente completar o objetivo principal (ex: se cadastrar, comprar, baixar asset).
*   Conte o número de cliques e campos de formulário.
*   **Ataque:** Procure por campos desnecessários ou CTAs confusos (ex: "Saiba Mais" vs "Quero meu relatório").

### 3. Teste de Stress Móvel
*   Force uma visualização mobile (se disponível nas ferramentas).
*   Verifique se os botões são clicáveis com o "dedo" (espaçamento) e se o texto não quebra o layout.

### 4. Relatório de Vulnerabilidade & Pragmatismo
Para cada falha encontrada, classifique-a usando o **Filtro de Pragmatismo Hermes**:

*   🔴 **RED (Crítica):** Falha funcional ou risco real de negócio (ex: botão de compra inativo, erro de PII exposta, bug técnico). **Ação:** Deve ser corrigido antes do lançamento.
*   🟡 **YELLOW (Séria):** Fricção de UX que gera queda de conversão ou confusão extrema (ex: formulário longo demais, CTA escondida, falta de prova social onde é vital). **Ação:** Recomendar correção prioritária.
*   ⚪ **WHITE (Melhoria):** "Frescura estética" ou micro-interações que aumentariam a confiança, mas não impedem o uso. **Ação:** Adicionar ao backlog de melhorias futuras.
*   🟢 **GREEN (Fortaleza):** Pontos fortes da interface que devem ser protegidos em futuras iterações.

## Regras de Ouro
- Não seja "legal" com o design. Seja o crítico mais rigoroso.
- Use o Pragmatismo para separar o que é "estilo" do que é "dinheiro perdido".
- Se você ficar "preso" em um modal por mais de 2 segundos, reporte como falha 🔴 RED.


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Contexto** — Qual a situação atual?
2. **Objetivo** — O que define o sucesso desta execução?
3. **Restrições** — O que não devemos fazer?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Nenhuma. Pure reasoning skill.

## When to Use

Use `Adversarial UX` when the task requires its specific capabilities as described above.

**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.


## Inputs

| Input | Required | Description |
|---|---|---|
| **Primary input** | Yes | As described in the skill instructions |
| **Configuration** | No | Optional parameters for customization |


## Output Format

Output is delivered in the format most appropriate to the task, typically Markdown or CSV.


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
| **Key findings** | `[OPERACIONAL]: adversarial-ux — [finding]` | `[OPERACIONAL]: adversarial-ux — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: adversarial-ux — [param] works better as [value]` | `[OPERACIONAL]: adversarial-ux — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: adversarial-ux — [insight]` | `[ESTRATÉGICO]: adversarial-ux — Competitor X has no case studies page, vulnerability for battlecard` |

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

