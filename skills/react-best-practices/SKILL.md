---
name: React Best Practices
description: Linter semântico e refatorador focado em React. Enforça separação de UI/Lógica (Custom Hooks), hooks rules e otimização. Requer autorização explícita do usuário baseada em relatório de impacto.
type: linting_refactoring
tags: [development, quality-assurance, code]
---

# Skill: React Best Practices

**Core principle:** Sistemas resilientes assumem a falha como padrão e a recuperação como regra.


Esta skill atua como um Arquiteto Frontend Sênior focado em React. O objetivo é analisar componentes existentes ou recém-criados e garantir que eles atendam ao padrão de excelência de mercado, focando em manutenibilidade, legibilidade e performance.

## Diretrizes de Excelência

1. **Separação de Preocupações (SoC):** Lógica complexa de estado e efeitos colaterais deve ser extraída para Custom Hooks, deixando o componente apenas responsável por renderização.
2. **Memoização Consciente:** Avaliar a necessidade real de `useMemo` e `useCallback` para evitar re-renderizações desnecessárias sem poluir o código com otimizações prematuras.
3. **Estruturação Padrão:** Garantir que importações, declarações de tipos (TypeScript, se aplicável) e a organização de pastas sigam as convenções modernas do ecossistema React.

## OBRIGATÓRIO: Relatório Comparativo (Gatekeeper)

**Atenção:** Você NÂO tem permissão para alterar os arquivos ou aplicar as refatorações de imediato. Esta skill é opinativa e pode entrar em atrito com arquiteturas locais.

Antes de qualquer refatoração, você DEVE gerar um **Relatório Comparativo de Refatoração** e exibi-lo ao usuário.

O relatório deve conter:
- **Estado Atual vs Proposto:** O que está sendo mudado em alto nível.
- **Prós:** Ganhos em performance, legibilidade ou escalabilidade.
- **Contras:** Aumento de complexidade, overhead inicial.
- **O Que Pode Quebrar (Riscos):** Dependências, props de componentes pai, efeitos colaterais.
- **Trecho de Código (Diff):** Uma pequena demonstração do "Antes" e "Depois".

Após gerar o relatório, **PARE** a execução e aguarde. A **Palavra Final é do Usuário**. Somente com um explícito "Aprovado" ou "Pode rodar", você aplicará as mudanças propostas no código.


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

Use `React Best Practices` when you need to:
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
| **Key findings** | `[OPERACIONAL]: react-best-practices — [finding]` | `[OPERACIONAL]: react-best-practices — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: react-best-practices — [param] works better as [value]` | `[OPERACIONAL]: react-best-practices — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: react-best-practices — [insight]` | `[ESTRATÉGICO]: react-best-practices — Competitor X has no case studies page, vulnerability for battlecard` |

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

