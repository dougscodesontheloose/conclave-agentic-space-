---
id: "step-00-mapear-alvos"
execution: inline
agent: selene-mapper
outputFile: squads/family_ties_research/output/search-brief.md
model_tier: powerful
---

# Step 00: Mapear Alvos de Busca

## Context Loading

Load these files before executing:
- `ambientes/Family Ties/01_arvore/arvore-preliminar.md`
- `ambientes/Family Ties/01_arvore/dados-declarados.md`
- `ambientes/Family Ties/02_documentos/controle-documentos.md`
- `ambientes/Family Ties/03_fontes/fontes-e-acessos.md`
- `ambientes/Family Ties/04_hipoteses_cidadania/triagem.md`
- `ambientes/Family Ties/05_saidas/evidence-ledger.csv`
- `ambientes/Family Ties/privado/pessoas/P-003-claudio-alfredo-moura-da-silva.md`

## Instructions

### Process

1. Ler o contexto do ambiente e identificar as linhas familiares já documentadas.
2. Excluir do briefing qualquer dependência de dados de pessoas vivas para busca aberta.
3. Consultar o ledger para nao repetir `access_block`, `qualified_negative` ou `X` sem novo discriminador.
4. Priorizar alvos ligados a:
   - nascimento de `Joao Moura da Silva` em Alagoas;
   - nascimento de `Maria das Gracas` em Pernambuco;
   - resolucao nominal de `Pedro Jacinto/Pedro Teixeira de Paula`;
   - pais de `Herotildes Teixeira de Paula`;
   - colecoes e orgaos oficiais que destravam esses pontos.
5. Gerar uma fila priorizada de alvos com:
   - pessoa;
   - evento;
   - localidade;
   - janela temporal;
   - variantes nominais;
   - motivo da prioridade;
   - fontes prioritarias;
   - queries-base.
   - ledger relacionado, quando existir.
6. Encerrar com uma secao `Limites de seguranca`, explicitando o que nao deve ir para a web.

## Output Format

```markdown
# Search Brief

## Escopo aprovado para busca externa

## Fila priorizada de alvos

## Variantes nominais por alvo

## Fontes prioritarias por alvo

## Limites de seguranca
```

## Veto Conditions

1. Incluir pessoas vivas no briefing externo.
2. Criar alvo sem evento, localidade ou janela temporal minima.
3. Omitir conflitos de grafia conhecidos.
4. Reabrir busca bloqueada/negativada/descartada sem novo discriminador.

## Quality Criteria

- [ ] Briefing sanitizado.
- [ ] Fila com prioridade clara.
- [ ] Variantes nominais registradas.
- [ ] Limites de seguranca explicitos.
- [ ] Ledger consultado antes de sugerir nova web aberta.

## Output Example

```markdown
# Search Brief

## Escopo aprovado para busca externa
- Linha: Moura
- Objetivo: localizar caminho documental para nascimento de Joao Moura da Silva.
- Restricao: nao usar dados de pessoas vivas em queries.

## Fila priorizada de alvos

### Alvo 01
- Pessoa: Joao Moura da Silva
- Evento: nascimento
- Localidade: Alagoas
- Janela temporal: 1890-1910
- Motivo da prioridade: pode destravar filiacao da geracao anterior.
- Query-base: "Joao Moura da Silva" Alagoas nascimento

## Limites de seguranca
- Fichas privadas foram usadas apenas para orientar a linha interna.
- Nenhum dado moderno deve ser enviado para busca aberta.
```
