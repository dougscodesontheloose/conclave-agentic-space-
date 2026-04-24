---
task: "Build Web"
order: 1
input: |
  - task_brief: output/{run-id}/task-brief.md
  - backend_contracts: output/{run-id}/backend/contracts/*.json (se python_needed)
output: |
  - web_app: web/ com código-fonte, build servível, manifest, SW
  - scene_spec: web/scene-spec.json (se há 3D)
---

# Build Web

Implementa a PWA completa em TypeScript honrando o contrato visual do task-brief. Se há 3D, estrutura a cena Three.js modularmente e exporta `scene-spec.json` consumível por Sulu Swift e Dex Dotnet.

## Process

1. Leia o task-brief completo. Extraia stack, contrato visual, entidades 3D e tarefas atribuídas a Wade Web.
2. Gere scaffold em `web/`: `package.json` (Vite + TypeScript + Three.js se aplicável), `tsconfig.json` estrito, `index.html` com manifest linkado, `public/manifest.json`, `public/sw.js` (service worker offline-first com cache-first para shell + stale-while-revalidate para dados).
3. Estruture `/src`: `/src/core` (state, loop), `/src/scene` (se 3D: setup.ts, entities.ts, lights.ts, materials.ts, render.ts), `/src/ui` (components), `/src/pwa` (sw registration), `/src/main.ts`.
4. Aplique tokens do contrato visual em `/src/styles/tokens.css` (cores, tipografia, breakpoints como CSS custom properties).
5. Se há 3D: ao final, emita `scene-spec.json` com a hierarquia serializável: camera (position, fov, near, far), lights (array de {type, color, intensity, position}), entities (array de {id, geometry-type, params, material-type, material-params, position, rotation, scale}).
6. Rode `npm install` e `npm run build`. Se falhar, corrija. Se passar, siga.

## Output Format

Estrutura de `web/`:
```
web/
├── package.json
├── tsconfig.json
├── vite.config.ts
├── index.html
├── public/
│   ├── manifest.json
│   └── sw.js
├── src/
│   ├── main.ts
│   ├── core/
│   ├── scene/     (se 3D)
│   ├── ui/
│   ├── pwa/
│   └── styles/tokens.css
├── scene-spec.json  (se 3D)
└── README.md
```

## Output Example

```json
// web/scene-spec.json
{
  "camera": {
    "type": "perspective",
    "position": [0, 5, 12],
    "fov": 50,
    "near": 0.1,
    "far": 1000
  },
  "lights": [
    {"id": "ambient", "type": "ambient", "color": "#FFFFFF", "intensity": 0.3},
    {"id": "sun", "type": "point", "color": "#FFE4A0", "intensity": 1.8, "position": [0, 0, 0]}
  ],
  "entities": [
    {
      "id": "sun",
      "geometry": {"type": "sphere", "radius": 1.2, "widthSegments": 64, "heightSegments": 64},
      "material": {"type": "basic", "emissive": "#FFB454"},
      "position": [0, 0, 0]
    },
    {
      "id": "earth",
      "geometry": {"type": "sphere", "radius": 0.4, "widthSegments": 48, "heightSegments": 48},
      "material": {"type": "standard", "color": "#4F9DDE", "roughness": 0.7, "metalness": 0.1},
      "position": [5.2, 0, 0]
    }
  ]
}
```

## Quality Criteria

- [ ] TypeScript estrito (`strict: true` em tsconfig).
- [ ] Manifest e service worker presentes e registrados.
- [ ] Tokens do contrato visual em CSS custom properties.
- [ ] Se 3D: `scene-spec.json` emitido com hierarquia completa.
- [ ] `npm run build` passa sem erro.

## Veto Conditions

1. Bundle não gera (build falha).
2. Manifest inválido ou SW não registrado.
3. Se há 3D e `scene-spec.json` não foi gerado.
