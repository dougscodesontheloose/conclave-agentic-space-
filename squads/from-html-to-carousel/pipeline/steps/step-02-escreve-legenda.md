---
execution: inline
agent: gibson-writer
format: linkedin-post
inputFile: squads/from-html-to-carousel/output/slide-copy.yaml
outputFile: squads/from-html-to-carousel/output/legenda.md
---

# Step 02: Escreve Legenda do Post

## Context Loading

Load these files before executing:
- `squads/from-html-to-carousel/output/slide-copy.yaml` — Os slides criados na etapa anterior.
- `squads/from-html-to-carousel/pipeline/data/anti-patterns.md` — Erros comuns e o que evitar.

## Instructions

### Process
1. Analise o gancho recém-criado em `slide-copy.yaml`.
2. Escreva uma versão expandida breve (2-4 parágrafos pequenos) baseada no mesmo tom técnico de marketing analytics presente na identidade da persona.
3. Adicione necessariamente um CTA de arraste (para consumo do carrossel em PDF) e 3-4 hashtags.

## Output Format

The output MUST follow this exact structure:
```markdown
**[Legenda]**

[Parágrafo 1 - Lead in]

[Parágrafo 2 - Contexto Rápido / Tensão]

[Parágrafo 3 - Solução prometida no PDF e Call-to-scroll]

[Hashtags]
```

## Output Example

**[Legenda]**

As empresas focam num tracking milimétrico nos UTMs, mas perdem toda a visão holística do porquê o lead escapou na última etapa.

A atribuição Data-driven foca não em last click imperfeito, mas numa jornada em rede e multifocal.

Entenda como remodelar isso e parar de perder dinheiro nos criativos. 
👉 Arraste para o lado neste carrossel para ler o breakdown.

#MarketingAnalytics #PowerBI #Attribution

## Veto Conditions

Reject and redo if ANY of these are true:
1. O texto formou um paredão longo, ao modo bloqueado (text-wall) impossibilitando escaneabilidade em uma timeline de LinkedIn.
2. Não há uma chamada técnica ao PDF.

## Quality Criteria

- [ ] O primeiro parágrafo atua com uma reflexão, não com um resumo seco "neste PDF temos...".
- [ ] Linguagem é corporativa, direta e atrativa.
