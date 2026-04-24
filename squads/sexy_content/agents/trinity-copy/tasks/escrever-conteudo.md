---
task: "Escrever Conteúdo"
order: 2
input: |
  - Ângulo selecionado pelo usuário.
  - Diretriz Visual (Visual Identity) se for carrossel.
output: |
  - Corpo final do texto formatado com quebras e respiros, ou o conteúdo fatiado por slide.
---

# Escrever Conteúdo

Transfere a estratégia do ângulo para as palavras finais (o manifesto). 

## Process

1. Pergunte ao usuário (ou deduza via input se já decidido) se ele quer Post de Texto Simples ou Roteiro de Carrossel.
2. Pull the user's brand voice (Tom de Voz: Dica de colega experiente, Retro-futurismo Funcional aplicado à precisão vocabular, analogia inteligente).
3. Produza o artefato respeitando as amarras de cadência do LinkedIn.

## Output Format

```markdown
(Se for Post Normal)
# Draft

[O hook de primeira linha]

[Desenvolvimento focado, com variação de tam de parágrafo]
[Analogia sutil se houver]

[Fechamento e Fonte]


(Se for Carrossel)
# Roteiro de Carrossel

## Slide 01 - Capa
**Signal:** [Hook Curto]
**Context:** [Abertura se houver]

## Slide 02
**Signal:** [Dado Específico / Número Grande]
**Context:** [Tradução do dado]
**Detail:** [Fonte]

...
```

## Output Example

> Use as quality reference, not as rigid template.

```markdown
# Draft

Você não precisa de mais ferramentas. Você precisa de menos métricas.

Sempre que a conta fecha no vermelho no fim do Q3, a primeira reação da diretoria é comprar um software novo de atribuição.
É o equivalente corporativo a comprar um tênis caro pra ver se assim você cria vontade de ir correr.

A inteligência de marketing real trabalha com o dado que já existe — limpando, não empilhando.

As respostas estão nas colunas que você ignora no seu Power BI.
```

## Quality Criteria

- [ ] Se Carrossel, os slides são minimalistas (<40 palavras por slide).
- [ ] Espaço em branco mantido no markdown (parágrafos curtos).
- [ ] Sem palavras-gatilho de bloqueio (revolucionário, sinergia, dicas de ouro).

## Veto Conditions

Reject and redo if ANY are true:
1. O post começa com cumprimento ou encerra com CTA de like.
2. O carrossel descreve slides densos, cheios de parágrafos intermináveis que violam a regra dos "3 Segundos".
