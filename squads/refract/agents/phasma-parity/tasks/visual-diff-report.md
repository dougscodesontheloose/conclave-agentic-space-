---
task: "Visual Diff Report"
order: 1
input: |
  - web_screenshots: output/{run-id}/web/screenshots/
  - mac_screenshots: output/{run-id}/mac/screenshots/ (se Mac construído)
  - windows_screenshots: output/{run-id}/windows/screenshots/ (se Windows construído)
  - task_brief: output/{run-id}/task-brief.md (regiões críticas)
output: |
  - diff_report: parity/diff-report.md
  - side_by_side: parity/side-by-side.png
  - heatmaps: parity/heatmap-{plataforma}.png
---

# Visual Diff Report

Compara screenshots das plataformas construídas e produz relatório quantificado com veredito categórico.

## Process

1. Checar quantas plataformas existem. Se < 2, escrever `parity/.skipped` com motivo e sair.
2. Normalizar todos os screenshots: mesmo viewport lógico (1440×900 default), mesmo DPR, PNG lossless. Se há divergência de DPR, reamostrar com Lanczos.
3. Montar composição lado-a-lado em `parity/side-by-side.png` (web | mac | windows na ordem construída).
4. Para cada par (web vs nativo), calcular:
   - **Pixel-diff %**: percentual de pixels que diferem mais que threshold 8 em qualquer canal RGB.
   - **SSIM global**: Structural Similarity Index (0..1).
   - **ΔE médio** nas regiões críticas declaradas no `task-brief.md`: usar Lab color space para diferença perceptual.
5. Gerar heatmap de diff (PNG vermelho=diff alto, verde=idêntico) para cada par em `parity/heatmap-mac.png`, `parity/heatmap-windows.png`.
6. Atribuir veredito por par:
   - **Passa**: pixel-diff <2% E SSIM >0.95 E ΔE_max_regiao_critica <3.
   - **Ressalvas**: 2-5% OU SSIM 0.90-0.95 OU ΔE 3-6.
   - **Reprova**: >5% OU SSIM <0.90 OU ΔE >6.
7. Se Reprova, identificar dono: Wade Web (se bug na versão web), Sulu Swift (gap no Mac), Dex Dotnet (gap no Windows).
8. Escrever `parity/diff-report.md` com estrutura fixa abaixo.

## Output Format

```markdown
# Parity Report — {demanda-slug}

**Veredito geral:** {Passa | Passa com ressalvas | Reprova}
**Data:** YYYY-MM-DD
**Plataformas analisadas:** web, mac, windows

## Métricas por plataforma

| Plataforma | Pixel-diff % | SSIM | ΔE max (região crítica) | Veredito | Dono da correção |
|------------|-------------|------|-------------------------|----------|------------------|
| mac        | 1.8%        | 0.97 | 2.1                     | Passa    | —                |
| windows    | 4.3%        | 0.91 | 5.8                     | Ressalva | Dex Dotnet       |

## Composição lado-a-lado
`parity/side-by-side.png`

## Heatmaps
- `parity/heatmap-mac.png`
- `parity/heatmap-windows.png`

## Detalhes por região crítica

### Cena 3D central
- Web vs Mac: ΔE médio 1.9, máx 2.1 — Passa
- Web vs Windows: ΔE médio 4.2, máx 5.8 — Ressalva (emissão do sol mais apagada no SharpDX)

## Recomendações de correção
- **Dex Dotnet**: Aumentar intensidade emissive do shader do sol de 1.8 para 2.4 para compensar tone-mapping mais agressivo do DirectX.
```

## Output Example

```markdown
# Parity Report — orbital-viewer

**Veredito geral:** Passa com ressalvas
**Data:** 2026-04-19
**Plataformas analisadas:** web, mac

## Métricas por plataforma

| Plataforma | Pixel-diff % | SSIM | ΔE max (região crítica) | Veredito | Dono da correção |
|------------|-------------|------|-------------------------|----------|------------------|
| mac        | 2.4%        | 0.94 | 3.1                     | Ressalva | Sulu Swift       |

## Composição lado-a-lado
`parity/side-by-side.png`

## Heatmaps
- `parity/heatmap-mac.png`

## Detalhes por região crítica

### Cena 3D central (viewport)
- Web vs Mac: ΔE médio 2.8, máx 3.1 — diferença concentrada no halo emissive do sol.

### Info card (hover state)
- Web vs Mac: ΔE médio 1.2, máx 1.6 — Passa.

## Recomendações de correção
- **Sulu Swift**: Aplicar `SCNTechnique` com blur gaussiano radius=6 em cima do nodo "sun" para reproduzir o bloom do post-processing web.
```

## Quality Criteria

- [ ] ≥2 plataformas comparadas (ou `.skipped` documentado).
- [ ] Pixel-diff, SSIM, ΔE calculados e registrados.
- [ ] Heatmap PNG para cada par.
- [ ] Composição side-by-side gerada.
- [ ] Veredito categórico explícito.
- [ ] Dono da correção identificado quando não é Passa.

## Veto Conditions

1. Screenshots comparados em viewports diferentes sem normalização.
2. Veredito "Reprova" sem dono da correção identificado.
3. Relatório sem números (só adjetivos).
