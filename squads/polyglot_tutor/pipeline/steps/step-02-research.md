---
execution: subagent
agent: deckard-search
inputFile: squads/polyglot_tutor/output/research-focus.md
outputFile: squads/polyglot_tutor/output/research-results.md
model_tier: fast
---
# Step 02: Research
## Context Loading
- squads/polyglot_tutor/output/research-focus.md
## Instructions
### Process
1. Lê o foco.
2. Faz buscas.
3. Retorna links e resumos.
## Output Format
```
Pesquisa Concluída:
Links: ...
```
## Output Example
Pesquisa Concluída. Links: 1. video YT, 2. Artigo.
## Veto Conditions
1. Falha na busca.
2. Sem links.
## Quality Criteria
- [ ] Relevância
