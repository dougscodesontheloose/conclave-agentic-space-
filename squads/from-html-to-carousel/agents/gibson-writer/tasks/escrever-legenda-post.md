---
task: "Escrever Legenda"
order: 2
input: |
  - estrutura_slides: Copy recém extraída para formar contexto.
  - tom_voz: Identidade da marca (do arquivo memory ou pipeline).
output: |
  - legenda: Texto que acompanhará a publicação no LinkedIn ou Instagram.
---

# Escrever Legenda

Com formato otimizado para as redes sociais como LinkedIn, crie a legenda ideal que acompanha o carrossel como peça complementar e de atração.

## Process

1. Leia o Hook gerado na tarefa de design de slides.
2. Crie uma abertura (lead-in) de 2 a 3 linhas curtas que capture imediatamente o interesse (sem entregar o carrossel todo).
3. Inclua a instrução: "Arraste para o lado para ver o detalhamento" (uma linha clara de usabilidade).
4. Crie de 3 a 5 hashtags focadas em nicho (MKT Analytics, BI).

## Output Format

```markdown
**[Legenda]**

[Linha de choque ou contexto de 1 ou 2 frases]

[Por que isso importa / transição para o carrossel]

[Instrução, tipo: Arraste para o lado 👉]

[Hashtags]
```

## Output Example

> Use as quality reference, not as rigid template.

**[Legenda]**

O Last Click morreu e continuam usando ele para justificar orçamentos milionários de mídia. 

Se você trabalha gerindo campanhas no Meta ou Google Ads, sua capacidade de provar o próprio ROI depende de migrar sua confiança para o DDA do GA4. 

Entenda na prática o motivo 👇

Arraste para o lado nas imagens.

#MarketingAnalytics #PowerBI #GoogleAnalytics #MarketingEstrategico

## Quality Criteria

- [ ] Legenda contém ganchos sem spoilers excessivos do próprio post.
- [ ] O modelo textual utiliza espaços (sem blocos rígidos, frases fragmentadas de 1-2 linhas).
- [ ] Manteve o vocabulário estratégico (ROI, Mídia, DDA).

## Veto Conditions

Reject and redo if ANY are true:
1. O texto é apenas a transcrição do conteúdo do primeiro slide.
2. Não há uma chamada instruindo a pessoa a rodar o carrossel.
