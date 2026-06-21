---
execution: inline
agent: "trinity-copy"
inputFile: squads/sexy_content/output/noticias-rankeadas.md
outputFile: squads/sexy_content/output/angulos-gerados.md
---

# Step 04: Gerar Ângulos

## Context Loading

- O input do checkpoint e a notícia (com url) isolada.
- `pipeline/data/visual-identity.md` e os arquivos base para o banco de Analogias Pop.

## Instructions

### Process
1. Baseando-se apenas na notícia escolhida, pense em 5 maneiras de contá-la.
2. Cada ângulo precisa adotar um "Arquétipo" da matriz de voz (Insight Direto / Story / Contrário / Framework).
3. Entregue exatamente o YAML para o dashboard ou o feed da conversa.

## Output Format

```yaml
angulos:
  - id: 1
    arquetipo: "..."
    resumo_da_ideia: "..."
    hook_proposto: "..."
    analogia_sugerida: "..."
```

## Output Example

```yaml
angulos:
  - id: 1
    arquetipo: "Opinião Contrária"
    resumo_da_ideia: "Big Data atrapalha pequenas e médias."
    hook_proposto: "Você não precisa de um cientista de dados. Precisa de uma planilha limpa."
    analogia_sugerida: "Jogar Flight Simulator antes de soltar pipa."
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. Mais de 2 arquétipos idênticos foram sugeridos (tudo é historinha).
2. O hook_proposto soa "animador de auditório do linkedin".

## Quality Criteria

- [ ] Todas as sugestões de hook contêm tensão narrativa.
- [ ] Analogias trazem o universo de séries/jogos/retro-futurismo.
