---
execution: subagent
agent: "hari-searcher"
inputFile: squads/sexy_content/output/research-focus.md
outputFile: squads/sexy_content/output/noticias-rankeadas.md
model_tier: powerful
---

# Step 02: Pesquisa Tendências

## Context Loading

- `squads/sexy_content/output/research-focus.md` — O foco definido pelo usuário

## Instructions

### Process
1. Execute a pesquisa na web buscando fatos nas janelas de tempo requisitadas.
2. Analise a intersecção desse assunto com a base de Martech, Growth, BI e Criação de Dashboards, conforme seus princípios de filtro "ruído vs realidade".
3. Compile as top escolhas, formatando suas descobertas no YAML exigido pelo arquivo da sua Task.

## Output Format

```yaml
noticias:
  - id: 1
    titulo: "..."
    fonte: "..."
    url: "..."
    data: "..."
    resumo_analitico: "O impacto prático deste item é..."
```

## Output Example

```yaml
noticias:
  - id: 1
    titulo: "Notion adquire startup de automação"
    fonte: "TechCrunch"
    url: "https://..."
    data: "Ontem"
    resumo_analitico: "Afeta como equipes de performance orquestram tasks diretamente do board para a plataforma de mídias."
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. O robô falhou em pesquisar a internet trazendo datas alucinadas.
2. Nenhuma notícia foi realmente ranqueada ou validada; o YAML está vazio.

## Quality Criteria

- [ ] Variedade nas fontes lincadas.
- [ ] Conexão visível à temática central de marketing analytics e business intelligence.
