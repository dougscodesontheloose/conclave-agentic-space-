---
execution: inline
agent: quorra-qa
inputFile: squads/from-html-to-carousel/output/slide-copy.yaml
outputFile: squads/from-html-to-carousel/output/revisao-log.yaml
on_reject: 1
---

# Step 05: Revisão e Quality Assurance

## Context Loading

Load these files before executing:
- `squads/from-html-to-carousel/output/slide-copy.yaml`
- `squads/from-html-to-carousel/output/legenda.md`
- `squads/from-html-to-carousel/pipeline/data/quality-criteria.md`

## Instructions

### Process
1. Compare rigidamente o slide-copy produzido contra as restrições da régua métrica do auditor. Cada bloco passou das 30 palavras limitantes? Teve alguma infantilização indesejada? O post reflete os anti-padrões?
2. Avalie a congruência visual das informações logadas no log de design, se aplicável, mas as regras e a estrutura textuais são soberanas.
3. Gere o Status final. Se recusar, mande imediatamente regras corretivas indicando de quem foi a falha e qual linha exata contém demasiadas palavras ou uso de vocabulário incorreto ("Diquinha", etc.). Cuidado com excesso de preciosismo — se for meramente subjetivo e aceitável estrategicamente, priorize a agilidade e aprove.

## Output Format

The output MUST follow this exact structure:
```yaml
verdict:
  status: "[APROVADO | REJEITADO]"
  critical_issues:
    - "[Falha encontrada se tiver]"
  improvements_mandatory:
    - agent_target: "[Quem vai refazer - ex: gibson-writer]"
      task: "[Ação específica requerida]"
```

## Output Example

```yaml
verdict:
  status: "REJEITADO"
  critical_issues:
    - "A legislação não permite textões longos. O Slide 4 tem 40 palavras."
    - "Dumbing down do conceito ao redor do Slide 5. Uso de 'olha que magiquinha' é terminologia banida."
  improvements_mandatory:
    - agent_target: "gibson-writer"
      task: "Revisar tamanho do copy slide 4 e refazer a analogia slide 5 focando no mercado de MarTech formal."
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. O log for confuso ao dar REJEITADO sem evidências claras em métricas (tamanho do texto, palavras limitadas achadas, desvio de tom claro).

## Quality Criteria

- [ ] A análise engloba slides (copy + tamanhos) e legenda em uníssono.
- [ ] O Status gerado é perfeitamente "APROVADO" ou "REJEITADO", sem ambiguidades como "PARCIAL".
- [ ] O tom audível condizente com a the user's persona ("Dica de amigo", "Didático").
- [ ] O "Gancho" principal é magnético e direto.
- [ ] CTAs não são sobrepostos; apenas uma ação por publicação.
