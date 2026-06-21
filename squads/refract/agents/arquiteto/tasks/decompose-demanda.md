---
task: "Decompor Demanda"
order: 1
input: |
  - demanda_raw: texto livre do usuário descrevendo o que quer construir
  - company_context: _memory/company.md (preferências, contexto)
output: |
  - task_brief_md: arquivo task-brief.md com decomposição completa
  - python_needed: flag booleana no topo do brief
---

# Decompor Demanda

Transforma uma demanda bruta em um task-brief acionável para os devs, declarando stack alvo, contratos visuais quantificados, dependências e se Pris Python deve ser ativada.

## Process

1. Leia a demanda bruta. Se ambígua em algum ponto crítico (ex: "um app de gráficos" — qual tipo de gráfico?), marque pendência mas siga com a melhor interpretação. Não faça perguntas inline — o usuário já aprovou o squad e quer execução.
2. Classifique a natureza técnica: (a) UI app sem 3D, (b) app com Three.js, (c) data/dashboard, (d) ferramenta utilitária. Essa classificação direciona decisões abaixo.
3. Decida `python_needed`:
   - `true` se: demanda pede backend, ML, processamento de dados servidor-side, pipeline de assets (glTF gen, imagem batch).
   - `false` se: UI-only, dados estáticos ou vindos de API pública.
4. Extraia contrato visual: palette (hex), tipografia (nome + fallback), breakpoints (px), timing de animação (ms + easing). Se não explícito na demanda, adote defaults do `_memory/memories.md` ou proponha explicitamente no brief (nunca deixe implícito).
5. Se 3D: liste recursos Three.js esperados (geometrias, materiais, luzes, post-processing) e marque equivalentes nativos que devem ser mapeados.
6. Marque regiões críticas (2-5 áreas de UI que Phasma Parity deve vigiar com rigor extra).
7. Salve `task-brief.md` em `output/{run-id}/task-brief.md`.

## Output Format

```markdown
# Task Brief: {slug-da-demanda}

**Data:** YYYY-MM-DD
**Python needed:** true | false
**Natureza:** ui-sem-3d | ui-com-threejs | data-dashboard | utilitario

## Resumo em 1 linha
{síntese acionável}

## Stack Alvo

### Web (sempre)
- TypeScript + {bundler}
- Three.js: {sim/não}
- PWA: offline-first, manifest, SW

### Backend (se python_needed)
- FastAPI + Pydantic
- Endpoints planejados: ...

## Contrato Visual

| Token | Valor |
|-------|-------|
| Primary | #RRGGBB |
| Accent | #RRGGBB |
| Tipografia | {Font}, fallback: system |
| Breakpoint mobile | 390px |
| Breakpoint desktop | 1440px |
| Easing principal | ease-in-out-cubic |
| Timing de hover | 150ms |

## Entidades 3D (se aplicável)

| Entidade | Three.js | Mapeamento SceneKit | Mapeamento SharpDX |
|----------|----------|---------------------|---------------------|
| Planeta | SphereGeometry + MeshStandardMaterial | SCNSphere + SCNMaterial PBR | D3D11 Sphere + PBR shader |

## Regiões Críticas (Phasma vigia)
1. {região 1}
2. {região 2}

## Tarefas por agente

- **Wade Web:** ...
- **Pris Python (se ativada):** ...
- **Sulu Swift:** ... (adiado até Checkpoint B)
- **Dex Dotnet:** ... (adiado até Checkpoint B)
```

## Output Example

```markdown
# Task Brief: orbital-viewer

**Data:** 2026-04-19
**Python needed:** false
**Natureza:** ui-com-threejs

## Resumo em 1 linha
PWA que renderiza um sistema solar interativo em Three.js com zoom e info cards por planeta.

## Stack Alvo

### Web
- TypeScript + Vite
- Three.js r160+
- PWA: SW offline-first, manifest, ícone 512x512

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
| Sun | SphereGeometry + MeshBasicMaterial emissive | SCNSphere + emission | sphere + emissive pixel shader |
| Planet | SphereGeometry + MeshStandardMaterial | SCNSphere + SCNMaterial PBR | sphere + PBR |
| Ambient Light | AmbientLight 0.3 | SCNLight type: ambient | cbuffer ambient term |

## Regiões Críticas
1. Cena 3D central (viewport)
2. Info card de planeta (hover)

## Tarefas por agente

- **Wade Web:** montar cena modular em `/src/scene`; info cards em `/src/ui`; exportar `scene-spec.json`.
- **Sulu Swift:** adiado, aguarda Checkpoint B.
- **Dex Dotnet:** adiado, aguarda Checkpoint B.
```

## Quality Criteria

- [ ] Flag `python_needed` declarada no topo.
- [ ] Contrato visual com valores absolutos (hex, ms, px).
- [ ] Se há 3D, tabela de mapeamento Three.js ↔ nativo preenchida.
- [ ] Regiões críticas listadas (2-5 itens).
- [ ] Tarefas por agente explícitas.

## Veto Conditions

1. Contrato visual sem valores numéricos (só adjetivos como "moderno", "clean").
2. Flag `python_needed` ausente ou ambígua.
3. Demanda com 3D sem tabela de mapeamento.
