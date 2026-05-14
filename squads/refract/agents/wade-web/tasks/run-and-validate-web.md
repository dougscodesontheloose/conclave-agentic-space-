---
task: "Run and Validate Web"
order: 2
input: |
  - web_app: web/ com build funcional
output: |
  - screenshots: web/screenshots/desktop.png e web/screenshots/mobile.png
  - validation_log: web/validation.md com resultado do Lighthouse e runtime
---

# Run and Validate Web

Inicia o preview server, abre no Playwright, captura screenshots em desktop e mobile, roda Lighthouse e salva o log. Só finaliza quando Lighthouse performance ≥ 90 em mobile.

## Process

1. Rode `npm run build && npm run preview` em background — capture a porta.
2. Use Playwright MCP para navegar ao preview em viewport 1440×900 (desktop) e 390×844 (mobile), aguarde `networkidle` + 500ms, capture screenshot PNG para `web/screenshots/desktop.png` e `web/screenshots/mobile.png`.
3. Rode `npx lighthouse http://localhost:{porta} --preset=mobile --output=json --output-path=web/lighthouse.json --chrome-flags="--headless"`.
4. Leia o JSON do Lighthouse; extraia scores (performance, accessibility, best-practices, seo, pwa).
5. Se performance < 90 ou PWA < 90, documente gaps em `web/validation.md` e tente 1 rodada de correção trivial (ex: preload crítico, lazy image). Se ainda falhar, entregue com veredito "passou com ressalvas".
6. Escreva `web/validation.md` com scores, screenshots linkados e eventuais ressalvas.

## Output Format

```markdown
# Validation — Wade Web

**Build:** {commit-sha-curto}
**Data:** YYYY-MM-DD HH:mm

## Lighthouse (mobile)

| Categoria | Score |
|-----------|-------|
| Performance | 94 |
| Accessibility | 96 |
| Best Practices | 100 |
| SEO | 91 |
| PWA | 100 |

## Screenshots
- Desktop 1440×900: `web/screenshots/desktop.png`
- Mobile 390×844: `web/screenshots/mobile.png`

## Ressalvas
- Nenhuma | ou lista de gaps
```

## Output Example

```markdown
# Validation — Wade Web

**Build:** a3f2b1c
**Data:** 2026-04-19 14:32

## Lighthouse (mobile)

| Categoria | Score |
|-----------|-------|
| Performance | 92 |
| Accessibility | 100 |
| Best Practices | 100 |
| SEO | 91 |
| PWA | 100 |

## Screenshots
- Desktop 1440×900: `web/screenshots/desktop.png`
- Mobile 390×844: `web/screenshots/mobile.png`

## Ressalvas
- LCP em 2.6s (threshold 2.5s) — hero image precisa de `fetchpriority="high"` se persistir.
```

## Quality Criteria

- [ ] Preview server rodou e respondeu.
- [ ] Screenshots desktop e mobile capturados.
- [ ] Lighthouse report gerado.
- [ ] Performance score documentado.
- [ ] `validation.md` escrito.

## Veto Conditions

1. Preview server não sobe.
2. Screenshots não capturados.
3. Lighthouse performance < 70 (abaixo disso é falha estrutural, não ressalva).
