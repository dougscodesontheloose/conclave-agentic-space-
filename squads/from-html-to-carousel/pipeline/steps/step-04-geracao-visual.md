---
execution: subagent
agent: ash-visuals
format: image-design
inputFile: squads/from-html-to-carousel/output/slide-copy.yaml
outputFile: squads/from-html-to-carousel/output/design-log.md
model_tier: powerful
---

# Step 04: Geração de Carrossel Visual Gráfico

## Context Loading

Load these files before executing:
- `squads/from-html-to-carousel/output/slide-copy.yaml` — Estrutura de dados aprovada do texto.
- `_conclave/_memory/company.md` — Para resgatar elementos de nome de autor, ou brand se referenciada ("Poética Racional").
- `squads/from-html-to-carousel/pipeline/data/research-brief.md` — Exigências de alto contraste e regras tipográficas visuais extraídas no design inicial.

## Instructions

### Process
1. Chame as skills adequadas para montagem visual se houver (como create-html-carousel).
2. Injete os dados oriundos de slide-copy em um template HTML limpo e de alto contraste visual (conforme seu Operational Framework).
3. Salve e execute a conversão/log em seu workflow de skill, listando todos os paths gerados dentro de `output/`.

## Output Format

The output MUST follow this exact structure:
```yaml
design_assets:
  tool_invoked: true
  platform: "[linkedin/instagram]"
  files_produced: "squads/from-html-to-carousel/output/[nomes_gerados]"
  status_html: "[HTML ou Log do que foi montado e submetido]"
```

## Output Example

```yaml
design_assets:
  tool_invoked: true
  platform: "linkedin"
  files_produced: "squads/from-html-to-carousel/output/carrossel_exportado.pdf"
  status_html: "HTML template aplicado com sucesso usando Roboto, fundo dark e CTA em destaque azul neon. Skill disparou export."
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. O HTML ou código referenciado perdeu os textos informados e mandou slides vazios.
2. A resolução ou estilo está visivelmente sem css legível e cairá nos Anti-patterns.

## Quality Criteria

- [ ] A hierarquia entre Hook e corpo do slide está evidente usando Font-size e Font-weight de forma lógica.
- [ ] As regras gerais indicadas no arquivo de best-practices de design (caso aplicável) como respiro visual foram aplicadas (Padding).
- [ ] O slide de capa possui um contraste visual agressivo e engajante (Hook Visual).
- [ ] Centralização e alinhamento impecáveis em 100% dos slides de miolo.
- [ ] Uso correto de famílias tipográficas sans-serif para legibilidade máxima em mobile.
- [ ] Teste de leitura: O conteúdo pode ser absorvido em uma passada rápida de 3 segundos por slide.
