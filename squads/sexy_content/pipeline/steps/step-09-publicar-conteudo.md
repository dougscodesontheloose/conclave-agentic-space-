---
execution: inline
agent: "deckard-publisher"
inputFile: squads/sexy_content/output/conteudo-revisado.md
outputFile: squads/sexy_content/output/status-publicacao.md
---

# Step 09: Publicar Conteúdo

## Context Loading

- O texto markdown final, aprovado.
- Dependência do Blotato API Key nas credenciais locais para a publicação rodar.

## Instructions

### Process
1. Emule o processo ou execute a publicação via Tool de "Blotato" de maneira que o payload do texto capturado em Markdown transite de forma pura (sem rasgar bullets e quebras de linha essenciais pro Retro-futurismo).
2. Monitore a flag HTTP retornada.
3. Crie e anote o status na base em YAML / Log estruturado de saída para relatar o Sucesso pro User.

## Output Format

```text
Status do Deploy da Peça

Platform: ...
Status: ...
Data: ...

Nota Adicional: [Link ou msg]
```

## Output Example

```text
Status do Deploy da Peça

Platform: LinkedIn (dougpmoura)
Status: Agendado / Publicado
Data: 2026-04-06

Nota Adicional: Deploy realizado com sucesso e ID da transação ABC1234
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. Apresentar dados faltantes na checagem final (como credencial inválida e marcar que publicou).
2. Alterou o texto do Doug para fugir da validação ao invés de barrar e notificar erro na submissão.

## Quality Criteria

- [ ] Log estrutural claro e sucinto.
- [ ] Confirmação inquestionável de upload via Blotato.
