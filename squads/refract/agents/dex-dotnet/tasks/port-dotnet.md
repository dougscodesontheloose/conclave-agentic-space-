---
task: "Port Dotnet"
order: 1
input: |
  - task_brief: output/{run-id}/task-brief.md
  - web_build: output/{run-id}/web/
  - scene_spec: output/{run-id}/web/scene-spec.json (se 3D)
  - platform_choice: output/{run-id}/platform-choice.md
output: |
  - dotnet_solution: windows/ com solution compilável
  - parity_map: windows/parity-map.md
  - screenshots: windows/screenshots/*.png
---

# Port Dotnet

Traduz a build web em app Windows nativo usando WinUI 3 + Win2D (2D) e SharpDX (3D). Aborta imediatamente se `platform-choice.md` não inclui "windows".

## Process

1. Ler `platform-choice.md`. Se não contém "windows"/"win" (case-insensitive), escrever `windows/.skipped` e sair.
2. Scaffold da solution: `dotnet new sln -n Project` em `windows/`, projeto WinUI 3 via template `Microsoft.WinUI` (requer Windows App SDK 1.5+) ou template equivalente para macOS via `cross-platform` fallback. Se compilação WinUI não é viável no the user's Mac, usar **Avalonia UI** como fallback declarado e avisar.
3. Configurar `.csproj` com `<Nullable>enable</Nullable>`, `<TargetFramework>net8.0-windows10.0.22621.0</TargetFramework>` (ou `net8.0` para Avalonia).
4. `ResourceDictionary` em `Resources.xaml` com cores do contrato visual como `SolidColorBrush` nomeados.
5. UI em XAML declarativo com `MainWindow.xaml` + page(s); code-behind mínimo, lógica em ViewModels usando `CommunityToolkit.Mvvm`.
6. Se 3D: ler `scene-spec.json` e construir cena SharpDX — entidades viram objetos 3D com vertex/index buffers, materiais PBR via pixel shader simples. Alternativa: Win2D para 2D puro.
7. Compilar: `dotnet build -c Release`. Se no Mac, limitar a validação de compilação (cross-compile parcial); empacotar para execução em VM Windows quando disponível.
8. Capturar screenshot (XAML Designer ou execução com captura). Salvar em `windows/screenshots/`.
9. Escrever `windows/parity-map.md`.
10. Incluir `build.ps1` e `run.ps1` no root de `windows/`.

## Output Format

```markdown
# Parity Map — Web → WinUI 3 + SharpDX/Win2D

**Web source:** {commit-sha}
**.NET build:** {build-number}
**SDK:** Windows App SDK 1.5 + .NET 8 (ou fallback: Avalonia)

## Tokens Visuais (Resources.xaml)

| Token Web | CSS | XAML Resource |
|-----------|-----|---------------|
| --primary | #05060A | SurfacePrimaryBrush |
| --accent | #FFB454 | AccentBrush |

## Entidades 3D (SharpDX)

| ID | Three.js | SharpDX | Notas |
|----|----------|---------|-------|
| sun | SphereGeometry + emissive | sphere mesh + emissive PS | Pixel shader custom |
| earth | SphereGeometry + PBR | sphere mesh + PBR PS | Cook-Torrance |

## Known Gaps
- Bloom: `Microsoft.Graphics.Canvas.Effects.GaussianBlurEffect` como compromisso.
```

## Output Example

```csharp
// windows/App/Views/MainWindow.xaml.cs
using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;

public sealed partial class MainWindow : Window
{
    public MainWindow()
    {
        this.InitializeComponent();
        this.Title = "Orbital Viewer";
    }
}
```

```xml
<!-- windows/App/Resources.xaml -->
<ResourceDictionary
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
    <SolidColorBrush x:Key="SurfacePrimaryBrush" Color="#05060A"/>
    <SolidColorBrush x:Key="AccentBrush" Color="#FFB454"/>
</ResourceDictionary>
```

## Quality Criteria

- [ ] `platform-choice.md` consultado antes de escrever código.
- [ ] `.csproj` com Nullable habilitado.
- [ ] `Resources.xaml` com cores do contrato visual.
- [ ] `dotnet build -c Release` passa (ou diagnóstico documentado se rodando em Mac).
- [ ] Screenshots capturados (ou placeholder com plano de captura em VM).
- [ ] `parity-map.md` completo.
- [ ] `build.ps1` e `run.ps1` no root.

## Veto Conditions

1. Código .NET escrito sem "windows" em `platform-choice.md`.
2. Code-behind com lógica de negócio (violação MVVM).
3. Cores hardcoded no XAML sem ResourceDictionary.
