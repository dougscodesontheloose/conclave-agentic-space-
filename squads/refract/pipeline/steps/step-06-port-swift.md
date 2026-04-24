---
execution: inline
agent: "sulu-swift"
inputFile: squads/refract/output/platform-choice.md
outputFile: squads/refract/output/mac-status.md
---

# Step 06: Port Swift (condicional)

## Context Loading

- `squads/refract/output/platform-choice.md` — verifica se "mac" foi escolhido
- `squads/refract/output/task-brief.md` — contrato visual e entidades 3D
- `squads/refract/output/web/scene-spec.json` — fonte da verdade 3D (se existe)
- `squads/refract/output/web/screenshots/` — referência visual

## Instructions

### Process
1. Ler `platform-choice.md`. Se `platforms` não contém "mac", escrever `mac-status.md` com `status: skipped` e retornar.
2. Assumir persona de Sulu Swift.
3. Executar a task `port-swift.md`: xcodegen/xcodeproj, Asset Catalog com tokens, SwiftUI + SceneKit espelhando hierarquia do `scene-spec.json`, compilação com `xcodebuild`, captura de screenshot, `parity-map.md`.
4. Escrever `mac-status.md` com path do projeto, versão Xcode/SDK, screenshots gerados.

## Output Format

```yaml
status: "built" | "skipped"
path: "squads/refract/output/{run-id}/mac/" | null
xcode_sdk: "macOS 14.5" | null
build_result: "success" | "failed" | null
screenshots:
  - mac/screenshots/main.png
parity_map: "mac/parity-map.md" | null
known_gaps:
  - "Bloom via SCNTechnique (compromisso)"
```

## Output Example

```yaml
status: "built"
path: "squads/refract/output/2026-04-19-orbital-viewer/mac/"
xcode_sdk: "macOS 14.5"
build_result: "success"
screenshots:
  - mac/screenshots/main.png
  - mac/screenshots/hover.png
parity_map: "mac/parity-map.md"
known_gaps:
  - "Bloom do post-processing via SCNTechnique custom"
```

## Veto Conditions

1. Código Swift escrito sem "mac" em `platform-choice.md`.
2. Build falhou e status marcado como "built".
3. `parity-map.md` ausente quando status é "built".

## Quality Criteria

- [ ] `platform-choice.md` consultado primeiro.
- [ ] Build Xcode passa ou erro documentado.
- [ ] Screenshots capturados.
- [ ] Parity map escrito.
