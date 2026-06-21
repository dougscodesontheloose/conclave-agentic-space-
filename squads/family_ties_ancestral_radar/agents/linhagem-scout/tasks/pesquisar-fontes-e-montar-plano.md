---
task: "pesquisar-fontes-e-montar-plano"
order: 2
---

# Task: Pesquisar Fontes e Montar Plano

## Process

1. Ler a matriz de busca e atacar as lacunas na ordem definida.
2. Para lacunas `local`, consultar somente material interno e registrar o próximo documento necessário.
3. Para lacunas `web`, montar consultas progressivas por nome, variante, localidade, evento, ano e parentes associados.
4. Priorizar fontes oficiais, arquivos públicos, registros civis, acervos paroquiais e catálogos reconhecidos.
5. Para cada fonte consultada, registrar query, link, cobertura, valor documental, limitação e próximo passo.
6. Classificar cada achado com `A`, `B`, `C`, `D`, `X`, `qualified_negative` ou `access_block`.
7. Separar achado útil de ruído. Índice, catálogo e orientação não podem ser tratados como certidão integral.
8. Consolidar o resultado em plano de expansão com fatos confirmados, hipóteses fortes e pendências abertas.

## Output Format

```markdown
# Achados e Plano de Expansão

## Achados por Lacuna

### L-01
- Status:
- Grau/resultado:
- Queries usadas:
- Fontes consultadas:
- Fatos extraídos:
- Limitações:
- Próximo passo:
- Ledger update:

## Quadro Geral
- Melhor frente aberta:
- Gargalo principal:
- Depende de pedido de certidão:
- Depende de busca presencial:

## Plano de Expansão

### Fatos Confirmados
- ...

### Hipóteses Fortes
- ...

### Fila de Documentos
1. ...

### Próximas Buscas
1. ...
```

## Output Example

```markdown
### L-02
- Status: encontrou fonte útil, sem prova final
- Queries usadas:
  - "Pedro Teixeira de Paula" Pernambuco casamento
  - "Pedro Jacinto" Pernambuco família
- Fontes consultadas:
  - FamilySearch Catalog - https://www.familysearch.org/search/catalog
- Fatos extraídos:
  - Há coleções regionais que podem conter registro civil ou paroquial pertinente.
- Limitações:
  - A fonte indica caminho de busca, não confirma identidade.
- Próximo passo:
  - Refinar município por documento intermediário antes de pedir certidão.
```

## Quality Criteria

- [ ] Cada lacuna tem status objetivo.
- [ ] Cada busca web tem query e link registrados.
- [ ] Cada fonte tem valor documental e limitação.
- [ ] Próximos passos são executáveis por uma pessoa.
- [ ] Fato, hipótese e pendência aparecem separados.
- [ ] Implicações de cidadania são apenas preliminares.
- [ ] Cada achado tem grau/resultado e acao compativel com o ledger.

## Veto Conditions

1. Refazer se uma fonte aparecer sem link ou sem valor documental.
2. Refazer se uma query web não estiver registrada.
3. Refazer se índice ou catálogo for tratado como documento final.
4. Refazer se a saída pular gerações sem prova intermediária.
5. Refazer se houver conclusão de elegibilidade jurídica.
6. Refazer se bloqueio de acesso for tratado como negativo ou como permissao para busca ampla.
