# Output Examples — Refract

## Exemplo Completo 1: Orbital Viewer (com 3D, sem backend)

### Task Brief (Arquiteto)
```markdown
# Task Brief: orbital-viewer
**Python needed:** false
**Natureza:** ui-com-threejs

## Resumo em 1 linha
PWA que renderiza sistema solar interativo em Three.js com zoom e info cards por planeta.

## Stack Alvo
- Web: TypeScript + Vite + Three.js r160+

## Contrato Visual
| Token | Valor |
|-------|-------|
| Background | #05060A |
| Accent | #FFB454 |
| Tipografia | Inter, system fallback |
| Timing zoom | 650ms ease-out-cubic |

## Entidades 3D
| Entidade | Three.js | SceneKit | SharpDX |
|----------|----------|----------|---------|
| sun | Sphere + emissive | SCNSphere + emission | sphere + emissive PS |
| earth | Sphere + PBR | SCNSphere + PBR | sphere + PBR PS |

## Regiões Críticas
1. Cena 3D central (viewport)
2. Info card hover
```

### Web Entregue (Wade Web)
- `web/` com Vite + TS + Three.js + PWA completo
- Lighthouse mobile: Perf 94, A11y 100, PWA 100
- Screenshots 1440×900 e 390×844
- `scene-spec.json` com 2 entidades, 2 lights, camera perspective

### Port Mac (Sulu Swift, após Checkpoint B = "mac")
- `mac/Project.xcodeproj` compila em macOS 14.5
- `SCNScene` com `sun` e `earth` nomeados identicamente
- Asset Catalog com `Accent` (#FFB454) e `SurfacePrimary` (#05060A)
- `parity-map.md` com tabela completa

### Parity Report (Phasma, comparando web vs mac)
- Pixel-diff: 2.4%
- SSIM: 0.94
- ΔE max (cena 3D): 3.1
- Veredito: **Passa com ressalvas** — halo emissive do sol um pouco mais apagado
- Dono da correção: Sulu Swift (aplicar SCNTechnique blur gaussiano)

---

## Exemplo Completo 2: Dashboard de Métricas (sem 3D, com Python backend)

### Task Brief (Arquiteto)
```markdown
# Task Brief: metrics-dashboard
**Python needed:** true
**Natureza:** data-dashboard

## Resumo em 1 linha
Dashboard PWA com KPIs de marketing analytics servidos por FastAPI, consumindo CSV local.

## Stack Alvo
- Web: TypeScript + Vite + Lit components + Chart.js
- Backend: FastAPI + Pydantic, rota /api/kpis

## Contrato Visual
| Token | Valor |
|-------|-------|
| Background | #FAFAFA |
| Primary | #1F6FEB |
| Tipografia | Inter, fallback system-ui |
| Breakpoints | 390/768/1440 |

## Regiões Críticas
1. Cards de KPI (topo)
2. Chart principal
3. Filtro lateral
```

### Backend Entregue (Pris Python, python_needed=true)
- FastAPI 0.115 + Pydantic 2.9
- Endpoint `/api/kpis` com schema `Kpi`
- `backend/contracts/kpi.schema.json` exportado
- README com curl para teste local

### Web Entregue (Wade Web)
- Cliente Lit consumindo `/api/kpis`
- Chart.js com cores do contrato
- PWA com cache das métricas offline
- Lighthouse: Perf 92, A11y 98, PWA 100

### Decisão em Checkpoint A
- The user chose **Finalizar aqui** — uso é pessoal no browser, sem necessidade de port nativo.

### Resultado final
- `web/` e `backend/` entregues.
- `mac/` e `windows/` não criados.
- Run registrado em `_memory/runs.md` com plataformas = ["web"].

---

## Exemplo Completo 3: Visualizador 3D com Port Completo

### Task Brief (Arquiteto)
```markdown
# Task Brief: molecule-viewer
**Python needed:** true
**Natureza:** ui-com-threejs

## Resumo em 1 linha
Visualizador 3D de moléculas químicas com rotação, zoom e seleção de átomo. Dados via backend Python.

## Stack Alvo
- Web: TypeScript + Vite + Three.js r160
- Backend: FastAPI servindo dados PDB parseados

## Contrato Visual
| Token | Valor |
|-------|-------|
| Background | #0D1117 |
| Accent | #58A6FF |
| Timing rotação | 400ms ease-out-quart |

## Entidades 3D
| Entidade | Three.js | SceneKit | SharpDX |
|----------|----------|----------|---------|
| atom | Sphere + MeshStandardMaterial | SCNSphere + SCNMaterial PBR | sphere + PBR PS |
| bond | CylinderGeometry | SCNCylinder | cylinder mesh |

## Regiões Críticas
1. Cena 3D (toda viewport)
2. Painel de info do átomo selecionado
```

### Decisões do usuário em Checkpoints
- Checkpoint A: **Portar pra nativo**
- Checkpoint B: **Ambas** (mac + windows)

### Parity Report (Phasma, web vs mac vs win)
| Plataforma | Pixel-diff % | SSIM | ΔE max | Veredito | Dono |
|------------|-------------|------|--------|----------|------|
| mac | 1.8% | 0.97 | 2.1 | Passa | — |
| windows | 4.3% | 0.91 | 5.8 | Ressalva | Dex Dotnet |

**Veredito geral:** Passa com ressalvas
**Recomendação:** Dex Dotnet ajustar intensidade emissive dos átomos para compensar tone-mapping do DirectX.
