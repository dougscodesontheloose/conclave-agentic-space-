---
execution: inline
agent: "refract/pietro-prompt"
outputFile: squads/refract/output/refined-dev-instruction.md
---

# Step 00: Refinamento de Engenharia (Ground Zero)

## Context Loading

Load these files before executing:
- `_conclave/_memory/preferences.md` — Preferências de stack e IDE.
- `pipeline/data/technique-registry.md` — Framework T01-T13.
- `pipeline/data/pietro-anti-patterns.md` — Erros de engenharia de prompt.

## Instructions

### Process
1. **Analise o briefing técnico**: Identifique qual é o objetivo de software (feature, bug, refactor).
2. **Execute MSTCTRL**: Foque em identificar ambiguidades que possam confundir os devs (ex: versão de framwork, tipo de renderização).
3. **Refine a Instrução**: Aplique `T01`, `T04` e `T12 (ReAct Pattern)` para que os agentes saibam quando usar ferramentas de pesquisa ou código.
4. **Validação Cross-Platform**: Se houver portabilidade envolvida, garanta que o prompt mencione os requisitos de paridade.

## Output Format

```markdown
# 🛠️ Pietro Prompt: Refinamento de Engenharia

## 1. Instrução Técnica Refinada
> Base para o Arquiteto e Desenvolvedores:

```prompt
[Prompt de Engenharia Otimizado]
```

## 2. Meta-Análise Arquitetural (MSTCTRL)
- **Diagnóstico**: [Como o prompt original foi estruturado]
- **Gargalos de Software**: [Ambiguidades técnicas resolvidas]
- **Padrão de Ferramentas**: [Recomendações de uso de habilidades]
```

## Output Example

# 🛠️ Pietro Prompt: Refinamento de Engenharia

## 1. Instrução Técnica Refinada
> Base para o Arquiteto e Desenvolvedores:

```prompt
Role: Senior Analytics Engineer (Data & Growth).
Task: Build a SQL model for LTV (Lifetime Value) prediction.
Context: Using dbt core with Snowflake. Raw data in 'RAW_WEB_EVENTS'.
Requirements: Use incremental models. Include unit tests for uniqueness.
```

## 2. Meta-Análise Arquitetural (MSTCTRL)
- **Diagnóstico**: O prompt original era muito genérico e não especificava a stack técnica.
- **Gargalos de Software**: Stack de dados não definida; ausência de critérios de teste.
- **Padrão de Ferramentas**: dbt para modelagem, SQL para lógica Snowflake.

## Veto Conditions

Reject and redo if ANY are true:
1. O briefing refinado ainda contém ambiguidades de tecnologia (versão de framework, tipo de renderização ou runtime não especificados).
2. O prompt não inclui requisito de paridade visual quando a demanda envolve portabilidade entre plataformas.

## Quality Criteria

- [ ] Prompt agnóstico de modelo mas específico em tecnologia.
- [ ] Checklist de paridade visual incluído se aplicável.
