---
execution: inline
agent: gibson-writer
format: copywriting
inputFile: squads/from-html-to-carousel/output/input-base.md
outputFile: squads/from-html-to-carousel/output/slide-copy.yaml
---

# Step 01: Cria Estrutura de Slides

## Context Loading

Load these files before executing:
- `squads/from-html-to-carousel/output/input-base.md` — O link ou texto fornecido pelo usuário. Caso seja um link e ainda não tenha sido lido, utilize a Web Fetch skill rapidamente se disponível ou resuma o material anexado.
- `squads/from-html-to-carousel/pipeline/data/research-brief.md` — Parâmetros base da disciplina.
- `squads/from-html-to-carousel/pipeline/data/domain-framework.md` — As metodologias de copy e redução.

## Instructions

### Process
1. Extrair os ensinamentos base do arquivo de entrada. 
2. Redigir 5 a 10 slides (1 gancho, 3 a 8 contexto, 1 de CTA).
3. Ajustar linguagem considerando as memórias da marca e evitar dumbing down. Reduzir ativamente frases muito complexas e prolixas (text-wall).

## Output Format

The output MUST follow this exact structure:
```yaml
slides:
  - id: 1
    type: "hook"
    text: "..."
  - id: 2
    type: "content"
    title: "..."
    text: "..."
  # ...
  - id: N
    type: "cta"
    text: "..."
```

## Output Example

```yaml
slides:
  - id: 1
    type: "hook"
    text: "Por que sua análise de coorte falha na previsão de retenção LTV."
  - id: 2
    type: "content"
    title: "O Viés"
    text: "Modelos baseados apenas no mês 1 assumem homogeneidade no churn. O usuário é mutável."
  - id: 3
    type: "cta"
    text: "Arrume isso com a nova query SQL disponivel no link acima."
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. Menos de 5 ou mais de 10 slides totais.
2. Qualquer descritivo de texto passa de 30 palavras em um único slide.

## Quality Criteria

- [ ] A ideia central no gancho é provocativa e gera interesse direto na classe de recrutadores, pares ou líderes técnicos em MarTech.
- [ ] A linguagem usada para explicar o problema é firme: "Estratégia", "Escala" ao invés de floreios exaustivos.
