---
task: "Port Swift"
order: 1
input: |
  - task_brief: output/{run-id}/task-brief.md
  - web_build: output/{run-id}/web/ (fonte da verdade)
  - scene_spec: output/{run-id}/web/scene-spec.json (se 3D)
  - web_screenshots: output/{run-id}/web/screenshots/
  - platform_choice: output/{run-id}/platform-choice.md (verifica se Mac foi escolhido)
output: |
  - xcode_project: mac/ com projeto Xcode compilável
  - parity_map: mac/parity-map.md (mapeamento Three.js → SceneKit)
  - screenshots: mac/screenshots/*.png
---

# Port Swift

Traduz a build web em app Swift nativo com paridade visual. Aborta imediatamente se `platform-choice.md` não inclui "mac".

## Process

1. Ler `platform-choice.md`. Se não contém "mac" (case-insensitive), escrever `mac/.skipped` e sair.
2. Criar estrutura Xcode via xcodegen (preferencial) ou xcodeproj manual: `mac/Project.yml`, `mac/Sources/`, `mac/Assets.xcassets/`.
3. Mapear tokens do contrato visual para `Assets.xcassets/Colors/` — cada cor do contrato vira um `Color Set` nomeado (ex: `AccentColor`, `SurfacePrimary`).
4. Construir UI em SwiftUI honrando breakpoints. Em macOS, usar `NavigationSplitView` ou `WindowGroup` adequadamente.
5. Se há 3D: ler `scene-spec.json` e construir `SCNScene` correspondente. Cada entidade vira um `SCNNode` nomeado identicamente (ex: `sun`, `earth`). Materiais Three.js viram `SCNMaterial` com PBR (lightingModel `.physicallyBased`, metalness/roughness espelhados).
6. Animações: timing em ms viram `TimeInterval` em segundos; easing nomeado vira `CAMediaTimingFunction` equivalente.
7. Compilar: `xcodebuild -project mac/Project.xcodeproj -scheme Project -destination 'platform=macOS' build` — corrigir até passar.
8. Capturar screenshot via SwiftUI Preview snapshot (ou `xcrun simctl io ... screenshot` para iOS, ou CGWindowList capture para macOS). Salvar em `mac/screenshots/`.
9. Escrever `mac/parity-map.md` com tabela de mapeamento.

## Output Format

```markdown
# Parity Map — Web → SwiftUI + SceneKit

**Web source:** {commit-sha}
**Xcode build:** {build-number}

## Tokens Visuais

| Token Web | CSS | SwiftUI Color |
|-----------|-----|---------------|
| --primary | #05060A | Color("SurfacePrimary") |
| --accent | #FFB454 | Color("Accent") |

## Entidades 3D

| ID | Three.js | SceneKit | Notas |
|----|----------|----------|-------|
| sun | SphereGeometry r=1.2 + MeshBasicMaterial emissive #FFB454 | SCNSphere radius:1.2 + SCNMaterial emission:FFB454 | Paridade direta |
| earth | SphereGeometry r=0.4 + MeshStandardMaterial #4F9DDE | SCNSphere radius:0.4 + SCNMaterial PBR albedo:4F9DDE | Paridade direta |

## Animações

| Ação | Web | SceneKit |
|------|-----|----------|
| Zoom | 650ms ease-out-cubic | duration: 0.65, timingFunction: easeOut |

## Known Gaps
- Post-processing bloom não suportado 1:1; compromisso: usar `SCNTechnique` custom com blur gaussiano.
```

## Output Example

```swift
// mac/Sources/Scene/OrbitalScene.swift
import SceneKit

@MainActor
func buildOrbitalScene() -> SCNScene {
    let scene = SCNScene()

    let sun = SCNNode(geometry: SCNSphere(radius: 1.2))
    sun.name = "sun"
    let sunMat = SCNMaterial()
    sunMat.emission.contents = NSColor(hex: "#FFB454")
    sun.geometry?.materials = [sunMat]
    scene.rootNode.addChildNode(sun)

    let earth = SCNNode(geometry: SCNSphere(radius: 0.4))
    earth.name = "earth"
    let earthMat = SCNMaterial()
    earthMat.lightingModel = .physicallyBased
    earthMat.diffuse.contents = NSColor(hex: "#4F9DDE")
    earthMat.roughness.contents = 0.7
    earthMat.metalness.contents = 0.1
    earth.geometry?.materials = [earthMat]
    earth.position = SCNVector3(5.2, 0, 0)
    scene.rootNode.addChildNode(earth)

    return scene
}
```

## Quality Criteria

- [ ] `platform-choice.md` foi consultado antes de escrever código.
- [ ] Projeto Xcode compila em macOS.
- [ ] Entidades 3D nomeadas identicamente ao web.
- [ ] Asset Catalog com cores do contrato visual.
- [ ] Screenshots capturados.
- [ ] `parity-map.md` completo.

## Veto Conditions

1. Código Swift escrito sem "mac" em `platform-choice.md`.
2. Hex de cor hardcoded no código (deveria vir de Asset Catalog).
3. Entidades 3D com nomes divergentes do web.
