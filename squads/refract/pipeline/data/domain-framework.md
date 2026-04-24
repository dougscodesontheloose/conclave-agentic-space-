# Domain Framework — Refract

## Filosofia Operacional

**Web é o trilho padrão. Portabilidade é gated, consultiva e quantificada.**

Todo trabalho começa em stack web (PWA). Ports nativos para macOS (SwiftUI+SceneKit) e Windows (WinUI 3+Win2D/SharpDX) são opcionais e só iniciam após checkpoint explícito do usuário. A recompensa do port é fidelidade visual nativa + performance + distribuição offline. O custo é tempo e tokens. Cada decisão de port passa por recomendação consultiva do Arquiteto antes da pergunta ao usuário.

## Pipeline Canônica

1. **Decompose** — Arquiteto transforma demanda em task-brief com contrato visual quantificado, flag `python_needed` e entidades 3D mapeadas.
2. **Backend (opcional)** — Pris Python roda só se `python_needed: true`. FastAPI, pipeline ou conversor.
3. **Web** — Wade Web implementa PWA completa em TypeScript, roda, valida com Lighthouse.
4. **Checkpoint A (Web Approval)** — The user chooses: finalizar, iterar ou portar.
5. **Checkpoint B (Platform Choice)** — Se portar, Arquiteto recomenda, The user chooses plataformas.
6. **Port Mac (condicional)** — Sulu Swift.
7. **Port Windows (condicional)** — Dex Dotnet.
8. **Visual Parity** — Phasma Parity audita (só se ≥2 plataformas).
9. **Checkpoint Final** — The user accepts or requests correction.

## Decisões Arquiteturais Centrais

### Web Stack
- TypeScript estrito sempre; JS só quando a demanda exige.
- Vite como bundler default (esbuild aceitável).
- Three.js para 3D (modular: scene/entities/lights/materials/render).
- PWA completo: manifest, SW offline-first, ícones.
- Lighthouse ≥ 90 em mobile.

### Mac Stack
- SwiftUI declarativo para UI.
- SceneKit para 3D (RealityKit se AR/física avançada).
- Metal só se shader custom inescapável.
- Asset Catalog com tokens do contrato visual.
- `xcodegen` preferencial para reprodutibilidade.

### Windows Stack
- .NET 8+ com Nullable habilitado.
- WinUI 3 + Windows App SDK 1.5+ para UI (Avalonia como fallback cross-platform se compilando do Mac).
- Win2D para 2D GPU-accelerated.
- SharpDX/DirectX11 para 3D.
- MSIX packaging para distribuição.
- MVVM via CommunityToolkit.Mvvm.

## Regra de Contrato Visual

O task-brief do Arquiteto **sempre** quantifica:
- Cores em hex (`#RRGGBB`).
- Tipografia (nome + fallback).
- Breakpoints em px.
- Timing de animação em ms.
- Easing por nome (ex: `ease-out-cubic`, `spring(0.5,100)`).

Valores aproximados ("cor azul claro", "animação suave") são veto no task-brief.

## Regra de Paridade

A versão web é a fonte da verdade visual. Ports nativos existem para reproduzir a experiência web com fidelidade máxima, não para "melhorar" ou reinterpretar. Phasma Parity usa métricas objetivas (pixel-diff, SSIM, ΔE) com thresholds:

- **Passa**: pixel-diff <2%, SSIM >0.95, ΔE_max_crítico <3.
- **Ressalvas**: 2-5% / 0.90-0.95 / 3-6.
- **Reprova**: >5% / <0.90 / >6.
