---
type: checkpoint
outputFile: squads/refract/output/final-approval.md
---

# Step 09: Checkpoint — Aprovação Final

## Context Loading

- `squads/refract/output/web-validation.md`
- `squads/refract/output/mac-status.md` (se existe)
- `squads/refract/output/windows-status.md` (se existe)
- `squads/refract/output/parity-report.md` (se existe)
- `squads/refract/output/task-brief.md`

## Instructions

### Process
1. Compor um resumo final de 1 tela ao usuário:
   - Demanda (1 linha do task-brief).
   - Plataformas entregues (com caminhos de pasta).
   - Scores chave (Lighthouse web, veredito Phasma se houve diff).
   - Known gaps de paridade (lista).
2. Apresentar AskUserQuestion com 3 opções:
   - **Aceitar entrega** — encerrar o run, atualizar `_memory/runs.md`.
   - **Pedir correção** — informar dono (Wade/Sulu/Dex) e feedback; pipeline volta ao step relevante.
   - **Rodar Phasma de novo** — útil se o usuário corrigiu algo manualmente e quer re-auditar.
3. Salvar decisão em `final-approval.md`.
4. Se aceito, registrar run no `squads/refract/_memory/runs.md` como nova linha da tabela.

## Output Format

```yaml
decision: "accept" | "fix" | "rerun-parity"
target_agent: "wade-web" | "sulu-swift" | "dex-dotnet" | null
feedback: "..."
timestamp: "YYYY-MM-DD HH:mm"
```

## Output Example

```yaml
decision: "accept"
target_agent: null
feedback: ""
timestamp: "2026-04-19 15:12"
```

## Veto Conditions

1. `fix` sem `target_agent` definido.
2. `fix` sem feedback textual.

## Quality Criteria

- [ ] Resumo de entrega apresentado com caminhos e scores.
- [ ] Decisão salva em yaml.
- [ ] Se accept: `_memory/runs.md` atualizado.
