---
execution: inline
agent: trinity-copy
inputFile: squads/sexy_content/output/angulo-aprovado.md
outputFile: squads/sexy_content/output/draft-conteudo.md
---

# Step 07: Produzir Conteúdo (Trinity Copy)

## Context Loading

Load these files before executing:
- `squads/sexy_content/output/angulo-aprovado.md` — ângulo selecionado pelo Doug no checkpoint anterior
- `squads/sexy_content/output/formato-selecionado.md` — formato escolhido (post / carousel / article)
- `pipeline/data/tone-of-voice.md` — voz, ritmo e estilo do Doug
- `squads/sexy_content/_memory/douglas-brand-voice.md` — perfil de marca detalhado
- `pipeline/data/anti-patterns.md` — padrões de escrita a evitar

## Instructions

### Process

1. Ler o ângulo aprovado e o formato selecionado.
2. Executar a seção correspondente ao formato abaixo.
3. Antes de escrever: identificar a ponte entre a Tecnologia Fria e a Emoção Humana Real no conteúdo.
4. Aplicar os verbos de ação cognitiva do perfil do Doug: decifrar, mapear, arquitetar, transmutar.
5. Inserir uma (e apenas uma) metáfora inusitada ligada a videogames, cultura pop clássica ou literatura.
6. Verificar Veto Conditions antes de entregar.

**Se formato = post:**

Produzir post LinkedIn com:
- Hook na primeira linha — sem emoji genérico no início, sem pergunta retórica óbvia
- Desenvolvimento: 3–5 parágrafos curtos, alternando dado + narrativa
- CTA: final que gera reflexão ou comentário, nunca "curta e compartilhe"
- Limite: 3000 caracteres

**Se formato = article:**

Produzir artigo com:
- Título forte (provocativo, não clickbait)
- Lead de 2 parágrafos posicionando o argumento central
- 3–5 seções com subtítulo
- Conclusão com implicação prática
- Limite: 800–1500 palavras

**Se formato = carousel:**

Produzir o roteiro textual dos slides (design feito por Flynn Design no step seguinte):
- Estrutura obrigatória descrita no Output Format abaixo
- Máximo 40 palavras por slide
- O slide de capa é o ativo mais importante — headline que para o scroll em máximo 8 palavras

## Output Format

**Para post:**
```markdown
# Draft — Post LinkedIn

[Hook — primeira linha sem emoji]

[Parágrafo 1 — dado ou anedota]

[Parágrafo 2 — desenvolvimento]

[Parágrafo 3 — implicação]

[CTA reflexivo — sem chamada vazia]
```

**Para carousel:**
```markdown
# Draft — Roteiro de Carrossel

## Slide 01 — Capa
**Headline:** [máx 8 palavras — para o scroll]
**Subheadline:** [contexto — máx 12 palavras]

## Slide 02 — Problema / Provocação
**Text:** [máx 40 palavras]

## Slide 03 — Dado / Evidência
**Stat:** [número ou fato]
**Context:** [1 linha]

## Slides 04–0N — Desenvolvimento
**Text:** [máx 40 palavras por slide]

## Slide Final — CTA
**Text:** [ação ou reflexão — máx 20 palavras]
**Handle:** @dougpmoura
```

**Para article:**
```markdown
# [Título provocativo]

[Lead — 2 parágrafos]

## [Subtítulo 1]
[Conteúdo]

## [Subtítulo 2–5]
...

## Conclusão
[Implicação prática]
```

## Output Example

```markdown
# Draft — Post LinkedIn

78% de aumento de produtividade. Cursor mediu. O debate acabou.

Mas o que esse número esconde é mais importante do que ele mesmo.

A maioria dos devs que testou os agentes do Cursor ficou empolgada com a velocidade.
Poucos perceberam que a velocidade revelou um problema diferente: eles não sabem
descrever o que querem com precisão suficiente para que um agente execute.

É como descobrir que você é rápido na corrida, mas não sabe para onde correr.

A habilidade que vai separar devs em 2027 não é Python. É clareza de contexto.
Saber articular o problema com precisão cirúrgica. Saber quando o output está errado
antes de ver o output.

Isso tem nome no design: brief. No jornalismo: pauta. Em engenharia de prompt:
contexto.

O que você está fazendo para desenvolver essa habilidade?
```

## Veto Conditions

Reject and redo if ANY are true:
1. O hook começa com "Você sabia", "Todo mundo sabe", "É importante salientar" ou similar genérico.
2. Qualquer slide de carrossel passa de 40 palavras.
3. O tom ficou corporativo-genérico — ausência da voz do Doug (técnico + narrativo + metáfora inusitada).

## Quality Criteria

- [ ] Hook para o scroll sem contexto prévio
- [ ] Voz do Doug presente: técnico, narrativo, com uma metáfora inusitada
- [ ] Dado ou evidência integrado organicamente (não jogado como trivia)
- [ ] CTA gera reflexão ou comentário, nunca engajamento vazio
- [ ] Formato correto (post: ≤3000 chars / carousel: ≤40 palavras/slide / article: 800–1500 palavras)
