---
task: "Gerar Ângulos"
order: 1
input: |
  - Notícia selecionada pelo checkpoint.
output: |
  - 5 abordagens de ângulo para a notícia, com base no framework arquétipos (Insight / Story / Contrário / Framework).
---

# Gerar Ângulos

Pega a notícia crua fornecida pelo pesquisador e abre 5 possibilidades diferentes de ataque literário. O mesmo fato pode ser olhado pela ótica de "Oportunidade", "Ameaça", "Mentira da Indústria", etc.

## Process

1. Leia o resumo e a fonte da notícia.
2. Identifique qual arquétipo de post se adequaria melhor.
3. Crie opções reais de hooks.
4. Para cada opção, indique se ela suportaria uma analogia Pop (Games/Filmes) e qual seria.

## Output Format

```yaml
angulos:
  - id: 1
    arquetipo: "..."
    resumo_da_ideia: "..."
    hook_proposto: "..."
    analogia_sugerida: "..."
  - id: 2
    ...
```

## Output Example

> Use as quality reference, not as rigid template.

```yaml
angulos:
  - id: 1
    arquetipo: "Opinião Contrária"
    resumo_da_ideia: "Todo mundo foca no prompt, mas o gargalo na IA corporativa é a limpeza do data lake."
    hook_proposto: "O hype do ChatGPT escondeu o defeito mais feio do seu BI."
    analogia_sugerida: "É como ter o motor de uma Ferrari e abastecer com gasolina adulterada."
```

## Quality Criteria

- [ ] Pelo menos 1 ângulo deve ser Contrário ou Insight Direto.
- [ ] Os hooks propostos obedecem ao padrão do linkedin-writing-v2 (sem "hoje quero compartilhar", tamanho controlado).

## Veto Conditions

Reject and redo if ANY are true:
1. Mais de 2 ângulos são basicamente idênticos em abordagem.
2. Hook usa clichês corporativos explícitos ("A importância da inovação no cenário atual...").
