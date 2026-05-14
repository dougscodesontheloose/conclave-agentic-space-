---
name: Dialectical Memory
description: Padrao de raciocinio para higiene e estruturacao de memoria a longo prazo.
type: prompt
tags: [system, memory, quality-assurance]
---

# Skill: Dialectical Memory

**Core principle:** Sistemas resilientes assumem a falha como padrão e a recuperação como regra.


Esta skill injeta um "filtro de consciência" no agente antes de ele escrever no arquivo `memories.md` de qualquer squad. O objetivo é evitar que o sistema se torne um cemitério de dados inúteis, mantendo apenas o "ouro" estratégico.

## O Processo Dialético

Sempre que você for salvar um aprendizado ou fato novo, aplique estas 3 perguntas:

1.  **Isso é Reutilizável?** Este fato será útil para um novo squad no futuro ou para o Doug tomar uma decisão daqui a um mês? (Se for apenas um log técnico de execução, não salve).
2.  **Qual o Impacto?** Isso altera a estratégia (Estratégico), o fluxo de trabalho (Operacional) ou os gostos/valores do usuário (Pessoal)?
3.  **Posso Sintetizar?** Existe uma forma de dizer isso em uma frase curta que capture a essência sem precisar de 3 parágrafos?

## Categorização de Memória

Ao escrever no `memories.md`, use estes prefixos para facilitar a recuperação pelo Arquiteto:

*   **[ESTRATÉGICO]:** Insights sobre posicionamento, mercado ou carreira.
*   **[OPERACIONAL]:** Descobertas sobre ferramentas, bugs fixados ou fluxos otimizados.
*   **[PESSOAL]:** Preferências do Doug, tom de voz, rotinas de saúde ou valores.

## Exemplo de Transformação
*   **Antes:** "Tentei rodar o comando X mas deu erro Y porque a permissão do diretório Z estava errada. Aí dei o comando chmod e funcionou."
*   **Depois (Dialética):** `[OPERACIONAL]: Em sistemas macOS, o diretório Z exige permissão explicita via chmod antes de instalações via Homebrew.`

## Regras de Ouro
- Mantenha a memória limpa. Menos é mais.
- Priorize o aprendizado (o *insight*) sobre a ação (o *log*).
- Se a informação contradiz uma memória anterior, registre a contradição e decida qual é a nova verdade.

## Quality Gate

Before delivering the final output, verify:

- [ ] **Output completeness:** All required fields/sections are populated
- [ ] **No silent failures:** Every step that was attempted has a status in the output
- [ ] **Format valid:** Output matches the documented schema
- [ ] **User checkpoint:** Present results summary to user before finalizing

**If any check fails:** Report the specific gap and ask user how to proceed.


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

### Environment Variables

```env
# Nenhuma variável obrigatória estrita
```

### Dependencies

Nenhuma. Pure reasoning skill.

## When to Use

Use `Dialectical Memory` when you need to:
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
| External API calls | Varies by provider (check API documentation) |
| LLM reasoning | Free (included in agent session) |

