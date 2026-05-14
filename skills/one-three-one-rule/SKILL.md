---
name: 1-3-1 Decision Rule
description: Framework estruturado para tomada de decisão e apresentação de soluções: 1 Problema, 3 Opções, 1 Recomendação.
type: prompt
tags: [system, strategy, decision-making]
---

# Skill: 1-3-1 Decision Rule

**Core principle:** Sistemas resilientes assumem a falha como padrão e a recuperação como regra.


Esta skill deve ser usada sempre que o agente precisar apresentar uma proposta, resolver um impasse estratégico ou sugerir um caminho a seguir para o usuário. Ela evita paralisia por análise e garante clareza.

## O Framework 1-3-1

### 1. O Problema (Problem)
Defina o problema de forma concisa em uma ou duas frases.
*   *Errado:* "O site está meio lento e o pessoal não está clicando no botão de cadastro, talvez seja o servidor ou a cor do botão."
*   *Certo:* "A taxa de conversão da landing page caiu 15% após a última atualização, e os dados apontam para um tempo de carregamento de 6 segundos no mobile."

### 3. As Opções (Options)
Apresente exatamente três caminhos possíveis, detalhando os prós e contras de cada um.
*   **Opção A (Conservadora/Rápida):** Ajuste imediato com baixo risco.
*   **Opção B (Equilibrada/Ideal):** O caminho que ataca a causa raiz com esforço médio.
*   **Opção C (Ambiciosa/Transformadora):** Mudança profunda para ganhos de longo prazo.

### 1. A Recomendação (Recommendation)
Escolha UMA das opções acima e justifique o porquê.
*   Não peça para o usuário escolher sem antes dar sua opinião de especialista.
*   "Minha recomendação é a **Opção B**, pois ela resolve o problema de performance sem a necessidade de um redesign completo agora, otimizando o ROI imediato."

## Quando usar:
- Briefings de campanha.
- Relatórios de analytics com sugestões de melhoria.
- Decisões de arquitetura de dados ou código.
- Planejamento de novos squads.

## Regra de Ouro
Nunca entregue um problema sem as 3 opções, e nunca entregue as opções sem a sua recomendação final.


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
| **Key findings** | `[OPERACIONAL]: one-three-one-rule — [finding]` | `[OPERACIONAL]: one-three-one-rule — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: one-three-one-rule — [param] works better as [value]` | `[OPERACIONAL]: one-three-one-rule — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: one-three-one-rule — [insight]` | `[ESTRATÉGICO]: one-three-one-rule — Competitor X has no case studies page, vulnerability for battlecard` |

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

