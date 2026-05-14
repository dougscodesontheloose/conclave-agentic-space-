---
type: checkpoint
outputFile: squads/refract/output/web-decision.md
---

# Step 04: Checkpoint — Aprovação Web

## Context Loading

- `squads/refract/output/web-validation.md` — scores e screenshots do build web
- `squads/refract/output/task-brief.md` — contrato original

## Instructions

Apresente ao usuário:

1. Um resumo de 3 linhas do que foi construído (nome da demanda, stack web, scores Lighthouse).
2. Os caminhos dos screenshots desktop e mobile para visualização.
3. A pergunta principal via AskUserQuestion com 3 opções:
   - **Finalizar aqui** — a web é o entregável; pular ports nativos.
   - **Iterar no web** — pedir correções ao Wade Web antes de qualquer port.
   - **Portar pra nativo** — avançar para Checkpoint B e escolher plataformas.

Salvar a resposta em `web-decision.md` com o formato:
```yaml
decision: "finalize" | "iterate" | "port"
feedback: "{texto livre, se iterate}"
```

Se `iterate`, voltar ao Step 03 com o feedback.
Se `finalize`, pular direto pro Step 09 (checkpoint final).
Se `port`, prosseguir para Step 05.

## Output Format

```yaml
decision: "finalize" | "iterate" | "port"
feedback: ""
timestamp: "YYYY-MM-DD HH:mm"
```

## Output Example

```yaml
decision: "port"
feedback: ""
timestamp: "2026-04-19 14:45"
```

## Veto Conditions

1. Decisão não é uma das três opções válidas.
2. `iterate` sem feedback textual.

## Quality Criteria

- [ ] Três opções apresentadas via AskUserQuestion.
- [ ] Decisão salva em formato yaml.
- [ ] Se iterate: feedback registrado e Step 03 re-executado.
