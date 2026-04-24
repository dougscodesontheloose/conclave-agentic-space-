---
execution: inline
agent: "dex-dotnet"
inputFile: squads/refract/output/platform-choice.md
outputFile: squads/refract/output/windows-status.md
---

# Step 07: Port Dotnet (condicional)

## Context Loading

- `squads/refract/output/platform-choice.md` — verifica se "windows" foi escolhido
- `squads/refract/output/task-brief.md` — contrato visual
- `squads/refract/output/web/scene-spec.json` — hierarquia 3D se aplicável
- `squads/refract/output/web/screenshots/` — referência visual

## Instructions

### Process
1. Ler `platform-choice.md`. Se `platforms` não contém "windows", escrever `windows-status.md` com `status: skipped` e retornar.
2. Assumir persona de Dex Dotnet.
3. Executar a task `port-dotnet.md`: solution .NET 8 + WinUI 3 (ou Avalonia como fallback documentado se rodando em Mac), ResourceDictionary com tokens, code-behind mínimo, SharpDX/Win2D para gráficos, `build.ps1` e `run.ps1`, `parity-map.md`.
4. Compilar com `dotnet build -c Release`. Documentar qualquer limitação de cross-compile do Mac.
5. Escrever `windows-status.md`.

## Output Format

```yaml
status: "built" | "skipped"
path: "squads/refract/output/{run-id}/windows/" | null
sdk: "Windows App SDK 1.5 + .NET 8" | "Avalonia 11 + .NET 8 (fallback)"
build_result: "success" | "failed" | "cross-compile-only"
screenshots:
  - windows/screenshots/main.png
parity_map: "windows/parity-map.md"
known_gaps:
  - "..."
```

## Output Example

```yaml
status: "built"
path: "squads/refract/output/2026-04-19-orbital-viewer/windows/"
sdk: "Avalonia 11 + .NET 8 (fallback — WinUI 3 não compila em Mac)"
build_result: "success"
screenshots:
  - windows/screenshots/main.png
parity_map: "windows/parity-map.md"
known_gaps:
  - "Executável final só testável em VM Windows"
  - "Bloom via GaussianBlurEffect"
```

## Veto Conditions

1. Código .NET escrito sem "windows" em `platform-choice.md`.
2. Build marcado "success" quando passou só cross-compile parcial.

## Quality Criteria

- [ ] `platform-choice.md` consultado.
- [ ] Build passa (ou limitação de ambiente documentada).
- [ ] Screenshots (ou plano de captura em VM).
- [ ] Parity map escrito.
