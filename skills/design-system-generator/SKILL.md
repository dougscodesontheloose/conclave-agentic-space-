---
name: design-system-generator
description: >
  Escreve, valida e exporta arquivos de especificação DESIGN.md (Google standards) para sistemas de design de UI consumíveis por agentes.
type: playbook
tags: [design, ui, design-system, architecture, code, tailwind]
---

# Design System Generator (DESIGN.md)

Gere especificações de Design System que tanto humanos quanto IAs possam consumir perfeitamente, usando o padrão `DESIGN.md` (formato open-source do Google Labs).

**Core principle:** Design não deve ser ambíguo para agentes. Tokens visuais e design rationale devem viver juntos em um arquivo de especificação estruturado.

## When to Use

- "Create a design system for my new app"
- "Gere um spec de design baseado neste wireframe"
- "Lint my DESIGN.md file"
- "Export my design system to Tailwind"

**Auto-trigger:** Quando o usuário solicitar a criação de um layout web complexo e pedir para manter a coerência visual entre diferentes componentes.

## Prerequisites

### Dependencies
Node.js para usar a CLI:
```bash
npx @google/design.md
```

## Inputs

| Input | Required | Description |
|---|---|---|
| **Brand Vibe/Constraints** | Yes | "Minimalist", "Dark mode", cores base |

## Phase 0: Intake

1. **Pergunta obrigatória:** Você tem uma cor primária em mente ou quer que eu crie uma paleta do zero?
2. **Pergunta obrigatória:** Precisamos exportar isso para Tailwind ou outro framework?

## Phase 1: Authoring

Crie o arquivo `DESIGN.md` com YAML frontmatter contendo tokens estritos (colors, typography, spacing, components) e Markdown no corpo explicando as razões.
- Siga a ordem canônica: Overview, Colors, Typography, Layout, Elevation, Shapes, Components.
- Cores em HEX devem ter aspas (`"#1A1C1E"`).

## Phase 2: Validation & Export

Execute linting:
```bash
npx -y @google/design.md lint DESIGN.md
```
Valide WCAG contrast e referências quebradas.

Se solicitado, exporte:
```bash
npx -y @google/design.md export --format tailwind DESIGN.md > tailwind.theme.json
```

## Phase 3: Output

### Output Format

| Output | Format | Location |
|---|---|---|
| **Spec** | Markdown | `DESIGN.md` no root do projeto |
| **Theme** | JSON | `tailwind.theme.json` |

## Cost

| Component | Cost |
|---|---|
| CLI Tools | Free |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **WCAG Failure** | CLI acusa ratio < 4.5:1 | Ajustar luminosidade das cores até passar no teste de contraste. |
| **Broken Ref** | CLI acusa erro no YAML | Corrigir referência (ex: de `{primary}` para `{colors.primary}`). |

**Principle:** Um design system só é útil se for rigorosamente consistente. Nunca ignore um erro de lint.

## Composability

**Feeds into:**
- `react-best-practices` — Como base visual para componentes React.
- `subagent-development` — Como `system prompt` de contexto visual para agentes de UI.

## Quality Gate

Before delivering the final output, verify:
- [ ] **Security:** Prompt Injection check nas entradas descritivas do usuário.
- [ ] **Linting:** O arquivo `DESIGN.md` passa na validação da CLI sem erros estruturais?
- [ ] **Accessibility:** As cores de texto sobre fundo respeitam WCAG AA no mínimo?
