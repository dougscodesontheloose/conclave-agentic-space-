# Parity Rubric — Phasma Parity

Rubrica operacional para auditoria de paridade visual entre plataformas. Fonte única de verdade para Phasma.

## Normalização obrigatória antes do diff

1. **Viewport lógico único**: default 1440×900 para desktop; 390×844 para mobile.
2. **DPR unificado**: reamostrar para DPR=2 via Lanczos se diverge.
3. **Background**: compor sobre fundo opaco identico (o token Background do contrato visual).
4. **Formato**: PNG lossless. Nunca JPG.
5. **Fonte renderizada**: garantir que a mesma face da fonte foi carregada (Inter Regular 400, não Inter Medium 500 em uma plataforma).

## Métricas

### Pixel-diff
- **Definição**: percentual de pixels cuja distância Euclidiana em RGB excede 8 (escala 0-255).
- **Biblioteca sugerida**: `pixelmatch` (Node) ou `scikit-image` (Python).
- **Escopo**: calculado sobre a viewport completa.

### SSIM (Structural Similarity Index)
- **Definição**: 0..1, onde 1 é identidade.
- **Biblioteca sugerida**: `ssim.js` ou `scikit-image`.
- **Escopo**: global.

### ΔE (Delta E — CIE76 ou CIEDE2000)
- **Definição**: distância perceptual no espaço Lab.
- **Preferência**: CIEDE2000 (mais preciso perceptualmente).
- **Escopo**: amostrar 20-50 pontos dentro de cada região crítica; reportar média e máximo.

## Thresholds por veredito

| Veredito | Pixel-diff | SSIM | ΔE max região crítica |
|----------|-----------|------|-----------------------|
| **Passa** | <2% | >0.95 | <3 |
| **Ressalvas** | 2-5% | 0.90-0.95 | 3-6 |
| **Reprova** | >5% | <0.90 | >6 |

Se uma das 3 métricas cai em tier pior, o veredito é o pior entre elas. (Ex: Pixel-diff 1.5% + SSIM 0.88 → Reprova.)

## Atribuição de dono da correção

Quando Ressalvas ou Reprova:

| Sintoma | Dono provável |
|---------|---------------|
| Cor primária fora em todas plataformas nativas | **Wade Web** — bug no token CSS ou renderização web |
| Cor primária certa no web, errada só no Mac | **Sulu Swift** — Asset Catalog divergente |
| Cor primária certa no web, errada só no Win | **Dex Dotnet** — ResourceDictionary divergente |
| Bloom ausente no Mac, presente no web | **Sulu Swift** — precisa SCNTechnique ou RealityKit |
| Bloom ausente no Win, presente no web | **Dex Dotnet** — precisa Win2D GaussianBlur ou shader custom |
| Animação com timing errado em uma plataforma | Dono daquela plataforma |
| Posição de elemento divergente | Dono daquela plataforma |
| Hierarquia 3D com entidade faltando | Dono daquela plataforma |

## Formato do relatório

O relatório `parity-report.md` sempre abre com a tabela de veredito por plataforma, depois side-by-side, heatmaps, e detalhes por região crítica. A última seção é sempre **Recomendações de correção** com linguagem imperativa ("Dex Dotnet: ajustar X para Y").

## Checklist de entrega

- [ ] Screenshots normalizados armazenados em `parity/normalized/`.
- [ ] `parity/side-by-side.png` gerado (web | mac | windows na ordem construída).
- [ ] `parity/heatmap-{plataforma}.png` por par comparado.
- [ ] `parity/diff-report.md` escrito com veredito, métricas, recomendações.
- [ ] Versões citadas: commit SHA web, build number Xcode, build number dotnet.
