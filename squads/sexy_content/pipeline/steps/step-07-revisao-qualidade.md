---
execution: inline
agent: "demerzel-audit"
inputFile: squads/sexy_content/output/draft-conteudo.md
outputFile: squads/sexy_content/output/conteudo-revisado.md
on_reject: 6
---

# Step 07: Revisão de Qualidade

## Context Loading

- O draft gerado pela Laura no passo anterior.
- As guidelines de Visual Identity e Cultura Pop do arquivo principal e data.

## Instructions

### Process
1. Re-leia a copy assumindo o viés de Editora de Revista Sênior.
2. Anote pontos de falha no hook, fluidez de frases e clichês vazios ("sinergia", "o que acha?").
3. Promova os "consertos" na copy e libere a versão Refatorada como resposta oficial da tarefa ("Relatório de Peer-Review" e "Texto Final Revisado").

## Output Format

```markdown
# Relatório de Peer-Review

## Críticas
- ...

## Texto Final Revisado
...
```

## Output Example

```markdown
# Relatório de Peer-Review

## Críticas
- Cortei o uso de "hoje aprendi", pois aniquilou sua credibilidade. Adicionei algo alusivo ao jogo da velha para exemplificar o caso.

## Texto Final Revisado
[Copy integral aqui]
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. O relatório de Peer-Review afirmar que está tudo impecável se claramente há termos genéricos apontados nos filtros de voz.
2. A revisora apagar a analogia criativa porque julgá-la boba, desconsiderando a ordem principal da Laura.

## Quality Criteria

- [ ] Tom de voz garantido (Dica de Amigo / Colega Experiente).
- [ ] O Markdown entregue é puro, para o Blotato e Doug.
