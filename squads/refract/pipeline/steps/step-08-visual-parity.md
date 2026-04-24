---
execution: inline
agent: "phasma-parity"
inputFile: squads/refract/output/platform-choice.md
outputFile: squads/refract/output/parity-report.md
---

# Step 08: Visual Parity (condicional)

## Context Loading

- `squads/refract/output/mac-status.md`
- `squads/refract/output/windows-status.md`
- `squads/refract/output/web/screenshots/`
- `squads/refract/output/mac/screenshots/` (se Mac construído)
- `squads/refract/output/windows/screenshots/` (se Windows construído)
- `squads/refract/output/task-brief.md` — regiões críticas

## Instructions

### Process
1. Contar plataformas construídas (web sempre + {mac, windows} conforme status).
2. Se total < 2, escrever `parity-report.md` com `status: skipped`, motivo "single-platform build" e retornar.
3. Assumir persona de Phasma Parity.
4. Executar task `visual-diff-report.md`: normalizar screenshots, calcular pixel-diff + SSIM + ΔE, gerar side-by-side e heatmaps, atribuir veredito + dono da correção.
5. Salvar relatório em `parity-report.md`.

## Output Format

`parity-report.md` conforme formato da task `visual-diff-report.md` — métricas por plataforma em tabela, side-by-side, heatmaps, detalhes por região crítica, recomendações de correção.

## Output Example

```markdown
# Parity Report — orbital-viewer

**Veredito geral:** Passa com ressalvas
**Plataformas analisadas:** web, mac

## Métricas
| Plataforma | Pixel-diff % | SSIM | ΔE max | Veredito | Dono |
|------------|-------------|------|--------|----------|------|
| mac | 2.4% | 0.94 | 3.1 | Ressalva | Sulu Swift |

## Recomendações de correção
- **Sulu Swift**: aplicar SCNTechnique com blur gaussiano no nodo "sun".
```

## Veto Conditions

1. Relatório emitido sem números (só adjetivos).
2. Veredito "Reprova" sem dono da correção.
3. Screenshots comparados sem normalização de viewport.

## Quality Criteria

- [ ] ≥2 plataformas analisadas (ou `.skipped` documentado).
- [ ] Métricas numéricas presentes.
- [ ] Heatmap e side-by-side gerados.
- [ ] Veredito categórico emitido.
