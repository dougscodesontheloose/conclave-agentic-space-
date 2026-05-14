---
type: checkpoint
outputFile: squads/refract/output/platform-choice.md
---

# Step 05: Checkpoint — Escolha de Plataformas

## Context Loading

- `squads/refract/output/task-brief.md` — entidades 3D, complexidade estimada
- `squads/refract/output/web-validation.md` — estado da build web
- `squads/refract/output/web-decision.md` — confirmação de que o usuário escolheu portar

## Instructions

### Process
1. Se `web-decision.md` não tem `decision: "port"`, escrever `platform-choice.md` com `platforms: []` e retornar (skip dos Steps 6/7/8).
2. Assumir persona do Arquiteto. Gerar **recomendação consultiva** em `port-recommendation.md` antes de perguntar, conforme o tom consultivo:

```markdown
## Recomendação do Arquiteto

| Plataforma | Complexidade | Risco principal | Recomendação |
|------------|-------------|-----------------|--------------|
| macOS (Swift) | M | Paridade de PBR materials OK via SceneKit; bloom via SCNTechnique | **Recomendado** — ganho offline no seu Mac + preview Xcode ágil |
| Windows (.NET) | L | Custom shader PBR em SharpDX é trabalhoso; WinUI 3 estável mas empacotamento MSIX tem fricção | **Adiar** — só compensa se você for distribuir. Sem Windows à mão, QA visual fica travado. |

**Veredito consultivo:** Portar para Mac apenas nesta rodada.
```

3. Apresentar a recomendação ao usuário e perguntar via AskUserQuestion:
   - Só Mac (recomendado, se for o caso)
   - Só Windows
   - Ambas (Mac + Windows)
   - Nenhuma — voltar atrás

4. Salvar resposta em `platform-choice.md`:

```yaml
platforms: ["mac"] | ["windows"] | ["mac", "windows"] | []
user_overrode_recommendation: true | false
```

5. Se `platforms: []`, pular Steps 6/7/8 e ir direto para Step 09.

## Output Format

```yaml
platforms: [...]
user_overrode_recommendation: bool
timestamp: "YYYY-MM-DD HH:mm"
```

## Output Example

```yaml
platforms: ["mac"]
user_overrode_recommendation: false
timestamp: "2026-04-19 14:47"
```

## Veto Conditions

1. Checkpoint apresentado sem recomendação consultiva prévia.
2. `platforms` contém valor fora de {mac, windows}.

## Quality Criteria

- [ ] Recomendação consultiva gerada antes da pergunta.
- [ ] Resposta salva em `platform-choice.md`.
- [ ] Se lista vazia, pipeline pula para Step 09.
