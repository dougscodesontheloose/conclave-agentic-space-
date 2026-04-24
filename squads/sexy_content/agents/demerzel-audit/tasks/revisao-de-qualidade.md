---
task: "Revisão de Qualidade"
order: 1
input: |
  - Draft gerado pela Trinity Copy.
output: |
  - Feedbacks explícitos onde quebra os the user's brand principles.
  - A cópia aprovada ou correções aplicadas se autorizado.
---

# Revisão de Qualidade

Critica a copy sem piedade usando a mentalidade do Retro-Futurismo Funcional: menos enfeite verbal, mais entrega mecânica, hook com aderência real e voz autoral.

## Process

1. Leia a linha de hook em isolamento. Se estiver fofa ou clichê, aponte.
2. Analise os blocos de texto (ritmo). Encontre qualquer frase enorme e quebre.
3. Se for carrossel, valide a contagem verbal por slide.
4. Identifique o uso indevido de qualquer tom professoral ("ensinar lição de forma hierárquica").
5. Reescreva o que for necessário para aprovação final.

## Output Format

```markdown
# Relatório de Peer-Review

## Crítica
- O hook "..." está fraco porque ... -> Sugestão: "..."
- O ritmo visual no parágrafo 2 precisa de linha de respiro.

## Texto Final Revisado
...
```

## Output Example

> Use as quality reference, not as rigid template.

```markdown
# Relatório de Peer-Review

## Crítica
O termo "mindset no growth" usado no Slide 3 enfraquece o profissionalismo. Trocado por "mudança estrutural". No geral, a analogia está ótima.

## Texto Final Revisado
...
```

## Quality Criteria

- [ ] Todas as violações do anti-pattern de linkedin-writing foram banidas.
- [ ] O tom geral está muito mais pragmático e direto.
- [ ] Emoticon/Emoji foram reduzidos ou limitados apenas a um destaque numérico ou de viés estritamente instrumental (como no Retro-futurismo).

## Veto Conditions

Reject and redo if ANY are true:
1. O revisor aprovar um texto que tenha a frase "E aí, o que você acha?".
2. A revisão focar apenas em ortografia ignorando os traços culturais da escrita (analogias).
