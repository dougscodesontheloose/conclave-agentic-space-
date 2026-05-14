---
execution: subagent
agent: hari-searcher
outputFile: squads/sexy_content/output/material-bruto.md
model_tier: powerful
---

# Step 02: Pesquisa ou Referência (Hari Searcher)

## Context Loading

Load these files before executing:
- `squads/sexy_content/output/research-focus.md` — modo selecionado pelo Doug (reference ou search) e foco/URL/tema
- `pipeline/data/research-brief.md` — critérios de qualidade de fontes e padrões de extração
- `pipeline/data/domain-framework.md` — framework operacional de pesquisa para conteúdo LinkedIn

## Instructions

### Process

O modo de execução é determinado pelo checkpoint anterior (`step-01-triage.md`). Ler `research-focus.md` para saber qual modo aplicar.

**Modo: Referência (mode = reference)**

1. Verificar se `research-focus.md` contém uma URL ou texto colado diretamente.
2. Se URL: acessar via `web_fetch` e extrair conteúdo principal (título, corpo, dados, citações, data).
3. Se texto colado: processar diretamente — identificar fonte, data estimada, credibilidade.
4. Extrair: pontos-chave (mínimo 5), dados e estatísticas, citações diretas, contexto e implicações.
5. Estruturar e salvar em `material-bruto.md` seguindo o Output Format abaixo.

**Modo: Pesquisa (mode = search)**

1. Ler tema e período de `research-focus.md`.
2. Executar mínimo 5 queries distintas via `web_search` — variar ângulos (dado, exemplo, controvérsia, tendência, case).
3. Selecionar as 3 fontes mais ricas e processar via `web_fetch`.
4. Consolidar em `material-bruto.md` com ranking de relevância (1 = mais relevante).
5. Para cada fonte: registrar URL, data, credibilidade (Alta/Média/Baixa + justificativa).

## Output Format

```markdown
# Material Bruto

**Fonte:** [URL ou "Input direto do Doug"]
**Data:** [data da publicação ou "N/A"]
**Credibilidade:** [Alta / Média / Baixa — justificativa em 1 linha]
**Modo:** [reference | search]

## Pontos Chave
1. [ponto com contexto suficiente para uso direto]
2. ...
(mínimo 5 pontos)

## Dados e Estatísticas
- [número/percentual + fonte + ano]
- ...

## Citações Relevantes
> "[citação direta com atribuição]"

## Contexto e Implicações
[2-4 parágrafos sobre o que esse material significa para profissionais de tecnologia/dados/negócios]

## Ranking de Relevância (modo search apenas)
1. [URL mais relevante] — [por quê]
2. ...
```

## Output Example

```markdown
# Material Bruto

**Fonte:** https://techcrunch.com/2026/04/15/cursor-ai-agents
**Data:** 15 de Abril de 2026
**Credibilidade:** Alta — TechCrunch, jornalismo especializado com verificação editorial
**Modo:** reference

## Pontos Chave
1. Cursor lançou agentes que escrevem e executam código de forma autônoma sem supervisão linha a linha.
2. O modelo interno foi treinado em 500k repositórios públicos, com foco em padrões de engenharia de software.
3. Empresas como Stripe e Linear já usam agentes similares para tarefas de manutenção de código legado.
4. O CEO afirmou que "o desenvolvedor do futuro é um diretor técnico de agentes, não um digitador de código".
5. Tempo médio de conclusão de PRs simples caiu de 4h para 23min em beta-testers.

## Dados e Estatísticas
- 78% dos beta-testers relataram aumento de produtividade acima de 3x em tarefas repetitivas (Cursor, 2026)
- Tempo médio de resolução de bugs simples: 23 min vs 4h anterior (Cursor internal data)

## Citações Relevantes
> "We're not replacing engineers. We're turning every engineer into a team of ten." — CEO Cursor

## Contexto e Implicações
O lançamento marca uma inflexão no debate sobre IA no desenvolvimento de software...
```

## Veto Conditions

Reject and redo if ANY are true:
1. O material-bruto.md tem menos de 5 pontos-chave — pesquisa insuficiente para suportar conteúdo de qualidade.
2. Não há nenhum dado numérico ou estatística — conteúdo sem evidência não tem autoridade no LinkedIn do Doug.

## Quality Criteria

- [ ] Mínimo 5 pontos-chave com contexto suficiente para uso direto no conteúdo
- [ ] Ao menos 1 dado numérico/estatística com fonte identificada
- [ ] Credibilidade da fonte avaliada e justificada
- [ ] Citação direta quando disponível
- [ ] Modo (reference/search) registrado no output
