# Anti-Patterns — Refract

## Arquitetura

### Never Do
- **Começar ports nativos sem checkpoint explícito.** Viola a regra gated — consome tokens sem aprovação.
- **Ativar Pris Python "por precaução".** Se `python_needed: false`, `backend/` fica vazio. Especulação é desperdício.
- **Reinterpretar a demanda durante o port.** A versão web é a fonte da verdade; não use o port pra "melhorar" o design.

### Always Do
- **Decompor antes de codar.** O task-brief é contrato — nenhum dev começa sem ele.
- **Quantificar tudo no contrato visual.** Hex, ms, px, easing nomeado. Zero adjetivos.

## Web

### Never Do
- **Tudo inline em um arquivo.** `index.html` com CSS+JS+Three.js num bloco só destrói a portabilidade.
- **Service Worker sem fallback offline.** PWA incompleta viola o DNA do squad.
- **Timing de animação em "segundos aproximados".** `duration: '0.5s'` quando o contrato diz `500ms` é aceitável; `duration: 'fast'` é veto.
- **Dependência pesada sem justificativa.** Uma biblioteca CSS de 200KB para 3 utilitários é descartável.

### Always Do
- **Estrutura `/src` padrão** (core/scene/ui/pwa/styles). Facilita mapeamento para Swift/.NET.
- **Emitir `scene-spec.json`** quando há 3D — ele é o contrato que Sulu e Dex consomem.

## Python

### Never Do
- **Endpoint sem schema Pydantic.** Cliente perde tipagem; contrato fica implícito.
- **Dependência não-pinada.** `fastapi` sem versão fecha reprodutibilidade.
- **Rodar sem virtualenv.** Contamina o the user's global environment.

### Always Do
- **Type hints 100%.** `pyright --strict` é baseline.
- **Documentar com curls.** README mostra como bater nos endpoints.

## Swift

### Never Do
- **Code app "from scratch" ignorando `scene-spec.json`.** Destrói paridade.
- **Hex hardcoded no Swift.** Use Asset Catalog.
- **Sem Xcode Preview ou screenshot.** Entregável obrigatório.
- **Nomes de SCNNode divergentes do web.** Phasma precisa comparar entidades por nome.

### Always Do
- **Asset Catalog com tokens.** `Color("Accent")` espelha `--accent` do CSS.
- **Parity-map em tabela.** Three.js → SceneKit, documentado.
- **Known Gaps declarados.** Se bloom via SCNTechnique é compromisso, está no parity-map.

## Dotnet

### Never Do
- **UWP.** Deprecated; use WinUI 3 sobre Windows App SDK.
- **Cores hardcoded no XAML.** ResourceDictionary é obrigatório.
- **Code-behind inflado.** Lógica fora da View (MVVM).
- **Sem MSIX/packaging config.** Sem Visual Studio, the user cannot run it.

### Always Do
- **Nullable enabled.** Qualidade moderna de C#.
- **build.ps1 e run.ps1 no root.** Reprodutibilidade CLI.
- **Design tokens em Resources.xaml.** Espelham CSS vars.

## Paridade

### Never Do
- **Comparar em viewports diferentes.** Fake diff.
- **JPG como composição.** Artefatos de compressão viram falso positivo. PNG sempre.
- **Veredito Reprova sem dono da correção.** Phasma sempre aponta o agente responsável.
- **"Parece igual" como justificativa.** Sem número, não é QA.

### Always Do
- **Normalizar antes de diffar.** Viewport + DPR + background.
- **Heatmap PNG entregue.** Humanos precisam inspecionar.
- **Citar versões.** Commit SHA web, build number Xcode, build number dotnet.
