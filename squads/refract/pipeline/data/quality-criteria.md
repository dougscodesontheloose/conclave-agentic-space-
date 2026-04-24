# Quality Criteria — Refract

Critérios de aceitação por camada. Aplicados pelos próprios agentes durante a execução e revisados por Phasma Parity (quando aplicável).

## Web (Wade Web)

### Build
- [ ] TypeScript estrito (`"strict": true` no tsconfig).
- [ ] `npm install` e `npm run build` sem erros nem warnings críticos.
- [ ] Bundle final < 500KB gzipped para apps simples; justificar tamanhos maiores.
- [ ] Zero dependências não-justificadas.

### PWA
- [ ] `manifest.json` válido (validator: `web-app-manifest-validator`).
- [ ] Service Worker registrado e funcional offline (cache-first para shell).
- [ ] Ícones 192×192 e 512×512 disponíveis.
- [ ] Installability check passa no DevTools.

### Qualidade Visual
- [ ] Lighthouse Performance ≥ 90 em mobile.
- [ ] Lighthouse Accessibility ≥ 95.
- [ ] Lighthouse Best Practices = 100.
- [ ] Screenshots em viewports 1440×900 e 390×844 salvos.

### 3D (quando aplicável)
- [ ] `scene-spec.json` emitido com hierarquia completa.
- [ ] FPS ≥ 60 em desktop, ≥ 30 em mobile médio.
- [ ] Render loop desacoplado da lógica de UI.

## Backend (Pris Python)

- [ ] Type hints em 100% do código (`pyright --strict` passa).
- [ ] Virtualenv isolado em `.venv/`.
- [ ] `requirements.txt` pinado.
- [ ] Modo API: endpoint `/health` responde 200; OpenAPI auto em `/docs`.
- [ ] Schemas Pydantic exportados como JSON Schema em `contracts/`.
- [ ] README com comandos curl de exemplo.

## Mac (Sulu Swift)

- [ ] `xcodebuild ... build` passa.
- [ ] `Project.yml` (xcodegen) ou `.xcodeproj` limpo.
- [ ] Asset Catalog com tokens do contrato visual nomeados.
- [ ] Se 3D: hierarquia `SCNScene` espelha `scene-spec.json` com nomes idênticos.
- [ ] Screenshots de SwiftUI Preview ou SCNView em `mac/screenshots/`.
- [ ] `parity-map.md` com tabelas Three.js → SceneKit preenchidas.
- [ ] Known gaps documentados.

## Windows (Dex Dotnet)

- [ ] `dotnet build -c Release` passa.
- [ ] `Nullable` habilitado no `.csproj`.
- [ ] `Resources.xaml` com tokens do contrato visual.
- [ ] MVVM via CommunityToolkit (sem lógica em code-behind).
- [ ] `build.ps1` e `run.ps1` no root.
- [ ] Screenshots capturados (ou plano documentado se rodando do Mac).
- [ ] `parity-map.md` com tabelas Three.js → SharpDX/Win2D.
- [ ] Known gaps documentados.

## Paridade (Phasma Parity)

### Por plataforma comparada com web
- [ ] Pixel-diff calculado (threshold de pixel 8 em qualquer canal).
- [ ] SSIM global calculado.
- [ ] ΔE médio e máximo nas regiões críticas.
- [ ] Heatmap PNG por par.
- [ ] Composição side-by-side em PNG.
- [ ] Veredito categórico (Passa / Ressalvas / Reprova).
- [ ] Se não-Passa: dono da correção identificado.

### Thresholds
| Métrica | Passa | Ressalvas | Reprova |
|---------|-------|-----------|---------|
| Pixel-diff | <2% | 2-5% | >5% |
| SSIM | >0.95 | 0.90-0.95 | <0.90 |
| ΔE max região crítica | <3 | 3-6 | >6 |

## Artefatos por Run

Toda run bem-sucedida entrega:
- `task-brief.md`
- `web/` (sempre)
- `backend/` (se python_needed)
- `mac/` + `mac/screenshots/` + `mac/parity-map.md` (se Mac construído)
- `windows/` + `windows/screenshots/` + `windows/parity-map.md` (se Windows construído)
- `parity/diff-report.md` + `parity/side-by-side.png` + heatmaps (se ≥2 plataformas)
- `final-approval.md`
