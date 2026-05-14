---
execution: inline
agent: "sexy_content/pietro-prompt"
outputFile: squads/sexy_content/output/refined-instruction.md
---

# Step 00: Refinamento de Instrução (Ground Zero)

## Context Loading

Load these files before executing:
- `_conclave/state/memory/company.md` — Perfil do Doug e estratégias principais.
- `pipeline/data/technique-registry.md` — Framework de técnicas T01-T13.
- `pipeline/data/pietro-anti-patterns.md` — Guia de erros a evitar.

## Instructions

### Process
1. **Analise o input inicial**: Leia o briefing ou a ideia fornecida pelo Doug.
2. **Aplique MSTCTRL**: Realize o diagnóstico arquitetural do prompt original identificando gargalos e camadas de abstração.
3. **Refine a Instrução**: Reescreva a instrução utilizando as técnicas do `technique-registry.md`, focando em `T01 (Persona)`, `T04 (Output Schema)` e `T13 (MSTCTRL)`.
4. **Valide contra Anti-Patterns**: Certifique-se de que o prompt refinado não cai nos erros de verborragia ou ambiguidade.
5. **Gere o Output**: Apresente o prompt refinado e o diagnóstico para aprovação silenciosa (ou manifesta se necessário).

## Output Format

O output deve seguir rigorosamente esta estrutura:

```markdown
# 🎯 Pietro Prompt: Refinamento Ground Zero

## 1. Prompt Refinado
> Copie e use este bloco para a próxima etapa:

```prompt
[Prompt Mestre Otimizado Aqui]
```

## 2. Meta-Análise MSTCTRL
- **Self-Analysis**: [Persona + Fluxo de Raciocínio]
- **Gargalos Identificados**: [Mínimo 3 pontos de ambiguidade resolvidos]
- **Estratégia aplicada**: [Técnicas utilizadas do Registry]

---
*Pronto para prosseguir para a Triagem de Conteúdo.*
```

## Output Example

# 🎯 Pietro Prompt: Refinamento Ground Zero

## 1. Prompt Refinado
> Copie e use este bloco para a próxima etapa:

```prompt
Role: Senior Thought Leader in AI & Marketing.
Task: Search for the latest 3 trends in Multi-Agent Orchestration.
Constraints: Focus on business impact, not just code. Negative: No generic marketing buzzwords.
Format: Structured table with 3 columns: Trend, Impact, Opportunity.
```

## 2. Meta-Análise MSTCTRL
- **Self-Analysis**: A instrução original era um comando atômico sem persona. Injetamos uma camada de autoridade sênior.
- **Gargalos Identificados**: Falta de escopo temporal, falta de restrição de tom e saída ambígua.
- **Estratégia aplicada**: T01, T04 e T09.

## Veto Conditions

Reject and redo if ANY of these are true:
1. O prompt refinado ainda contém ambiguidades sobre o objetivo final.
2. A meta-análise MSTCTRL não identifica pelo menos 3 melhorias concretas.

## Quality Criteria

- [ ] Uso correto de delimitadores.
- [ ] Inclusão de Fallback protocol se o input for vago.
- [ ] Alinhamento com a voz visual do Doug em `_memory/company.md`.
