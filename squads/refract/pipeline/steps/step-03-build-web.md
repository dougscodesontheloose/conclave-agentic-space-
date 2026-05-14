---
execution: inline
agent: "wade-web"
inputFile: squads/refract/output/task-brief.md
outputFile: squads/refract/output/web-validation.md
---

# Step 03: Build Web

## Context Loading

- `squads/refract/output/task-brief.md` — contrato visual e specs
- `squads/refract/output/backend-status.md` — verifica se há API local a consumir
- `squads/refract/pipeline/data/quality-criteria.md` — critérios gerais do squad

## Instructions

### Process
1. Assumir persona de Wade Web.
2. Executar a task `build-web.md`: scaffold TypeScript+Vite, PWA completa, /src estruturado, tokens CSS do contrato visual, `scene-spec.json` se 3D.
3. Se `backend-status.md` indica `status: built` com modo `api`, configurar o cliente web para consumir do endpoint local (fetch com base URL da API).
4. Rodar `npm install && npm run build`. Corrigir erros até passar.
5. Executar a task `run-and-validate-web.md`: preview server + Playwright screenshots + Lighthouse.
6. Escrever `web-validation.md` com scores Lighthouse, screenshots linkados e eventuais ressalvas.

## Output Format

`web-validation.md` conforme formato da task `run-and-validate-web.md` — Lighthouse por categoria, screenshots desktop/mobile, ressalvas.

## Output Example

```markdown
# Web Validation — orbital-viewer

**Build:** a3f2b1c
**Data:** 2026-04-19 14:32

## Lighthouse (mobile)
| Categoria | Score |
|-----------|-------|
| Performance | 94 |
| Accessibility | 100 |
| Best Practices | 100 |
| SEO | 91 |
| PWA | 100 |

## Screenshots
- Desktop 1440×900: `web/screenshots/desktop.png`
- Mobile 390×844: `web/screenshots/mobile.png`

## Ressalvas
- Nenhuma.
```

## Veto Conditions

1. `npm run build` falha.
2. Manifest/SW ausente ou inválido.
3. Screenshots não capturados.

## Quality Criteria

- [ ] Build web compila e roda.
- [ ] Screenshots desktop + mobile em `web/screenshots/`.
- [ ] Lighthouse report em `web/lighthouse.json`.
- [ ] `scene-spec.json` emitido se 3D.
