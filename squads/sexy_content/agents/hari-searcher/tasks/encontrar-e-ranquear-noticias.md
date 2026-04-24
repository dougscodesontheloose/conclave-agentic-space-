---
task: "Encontrar e Ranquear Notícias"
order: 1
input: |
  - Tema recebido pelo usuário.
  - Recorte de tempo.
output: |
  - Lista de 3 a 5 fontes primárias.
  - Resumos sintéticos do impacto no mundo data/business.
---

# Encontrar e Ranquear Notícias

Encontrar, absorver e condensar as notícias de maior impacto publicadas sobre o tema solicitado. Elimina ruído técnico vazio e enfatiza o poder de aplicabilidade nos negócios (Growth / BI).

## Process

1. Execute buscas focadas, lendo os links resultantes via fetch.
2. Descarte opiniões puras, foque em fatos (lançamentos de ferramentas, relatórios oficiais, fusões).
3. Avalie se o fato afeta a arquitetura de dados (Marketing Performance e Analytics).
4. Organize as opções no formato YAML solicitado.

## Output Format

```yaml
noticias:
  - id: 1
    titulo: "..."
    fonte: "..."
    url: "..."
    data: "..."
    resumo_analitico: "O impacto prático deste item é..."
  - id: 2
    ...
```

## Output Example

> Use as quality reference, not as rigid template.

```yaml
noticias:
  - id: 1
    titulo: "HubSpot Adiciona IA Preditiva para Score de Churn de Contas"
    fonte: "HubSpot Product Updates"
    url: "https://hubspot.com/..."
    data: "Ontem"
    resumo_analitico: "Com essa feature, Martech sai do reativo para o proativo. Impacta as equipes de CS e Data Engineers."
```

## Quality Criteria

- [ ] URLs presentes e reais.
- [ ] No mínimo 3 notícias encontradas.
- [ ] Os resumos contêm fatos úteis para se criar um bom argumento.

## Veto Conditions

Reject and redo if ANY are true:
1. Nenhuma notícia nova encontrada (a busca não resultou em links válidos).
2. A listagem trouxe conteúdo de tabloide sensacionalista sem dados práticos.
