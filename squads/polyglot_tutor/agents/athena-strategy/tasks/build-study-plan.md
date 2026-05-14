---
task: "Build Study Plan"
order: 1
input: |
  - research_data: Insumos brutos pesquisados
output: |
  - markdown_plan: O roteiro de estudos formatado
---

# Build Study Plan

Cria o relatório Markdown com métodos, ferramentas e rotina de estudo adaptada.

## Process
1. Lê o material aprovado na pesquisa.
2. Estrutura os dias/módulos do plano.
3. Escreve o roteiro com tom didático e fluído.

## Output Format
```markdown
# Roteiro de Estudos: [Tópico]

## Estratégia Geral
...

## O Plano
- **Passo 1:** ...
- **Passo 2:** ...
```

## Output Example
> Use as quality reference, not as rigid template.

# Roteiro: Italiano para Viagem (Sobrevivência)

## Estratégia
Vamos focar no Input Compreensível usando o canal X. A ideia é treinar o ouvido primeiro.

## Passo a Passo
1. Assista ao vídeo Y prestando atenção nos gestos.
2. Anote as 5 expressões mais repetidas...

## Quality Criteria
- [ ] Uso correto de Markdown
- [ ] Didática mesclada (Rigor + Creator)
- [ ] Passo a passo executável

## Veto Conditions
Reject and redo if ANY are true:
1. Faltam links para materiais práticos.
2. O plano é apenas um bloco de texto contínuo sem quebras.
