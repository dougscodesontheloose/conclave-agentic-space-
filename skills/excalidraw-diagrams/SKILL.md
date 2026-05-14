---
name: excalidraw-diagrams
description: >
  Crie diagramas hand-drawn (arquitetura, fluxogramas, sequence diagrams) em formato Excalidraw JSON.
  Gera arquivos .excalidraw que podem ser abertos em excalidraw.com. Sem API keys, sem dependências.
type: tool_orchestration
tags: [creative, design, visualization]
---

# Excalidraw Diagrams

Crie diagramas no estilo hand-drawn escrevendo JSON Excalidraw. Arraste os arquivos para excalidraw.com para visualizar.

**Core principle:** Diagramas clarificam o que texto não consegue. JSON puro, sem dependências de rendering.

## When to Use

- "Crie um diagrama de arquitetura"
- "Faça um flowchart deste processo"
- "Diagrama de sequência para [sistema]"
- Qualquer visualização de sistemas, processos, ou conceitos

**Auto-trigger:** Quando o usuário pede diagrama e Excalidraw é o formato mais adequado.

## Prerequisites

### Dependencies

Nenhuma. Apenas `write_file` para salvar o JSON. Opcional: `pip install cryptography` para upload.

## Inputs

| Input | Required | Description |
|---|---|---|
| **Conceito/sistema** | Yes | O que diagramar |
| **Tipo** | No | architecture/flowchart/sequence/concept-map |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Audiência** — Para quem estamos escrevendo/criando?
2. **Tom de Voz** — Qual a diretriz de marca a ser usada?
3. **Canal** — Onde isso será publicado?

## Phase 1: Construir Elementos

### Envelope do Arquivo

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "conclave",
  "elements": [ ... ],
  "appState": { "viewBackgroundColor": "#ffffff" }
}
```

### Elementos Básicos

**Rectangle com label:**
```json
{ "type": "rectangle", "id": "r1", "x": 100, "y": 100, "width": 200, "height": 80,
  "roundness": { "type": 3 }, "backgroundColor": "#a5d8ff", "fillStyle": "solid",
  "boundElements": [{ "id": "t_r1", "type": "text" }] },
{ "type": "text", "id": "t_r1", "x": 105, "y": 110, "width": 190, "height": 25,
  "text": "Label", "fontSize": 20, "fontFamily": 1, "textAlign": "center",
  "verticalAlign": "middle", "containerId": "r1", "originalText": "Label" }
```

**Arrow com binding:**
```json
{ "type": "arrow", "id": "a1", "x": 300, "y": 150, "width": 200, "height": 0,
  "points": [[0,0],[200,0]], "endArrowhead": "arrow",
  "startBinding": { "elementId": "r1", "fixedPoint": [1, 0.5] },
  "endBinding": { "elementId": "r2", "fixedPoint": [0, 0.5] } }
```

### Paleta de Cores

| Uso | Cor | Hex |
|---|---|---|
| Primary/Input | Light Blue | `#a5d8ff` |
| Success/Output | Light Green | `#b2f2bb` |
| Warning/External | Light Orange | `#ffd8a8` |
| Processing | Light Purple | `#d0bfff` |
| Error | Light Red | `#ffc9c9` |
| Notes | Light Yellow | `#fff3bf` |
| Storage | Light Teal | `#c3fae8` |

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Diagrama** | `.excalidraw` JSON | Arquivo no projeto |
| **Link** | URL excalidraw.com | Se upload solicitado |

## Cost

| Component | Cost |
|---|---|
| Geração | Free |
| Upload | Free (excalidraw.com) |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Labels invisíveis** | Usou `label` property | Usar container binding |
| **Texto sem contraste** | Cor clara em fundo branco | Min text color: `#757575` |

## Composability

**Receives data from:**
- `development-planning` — arquitetura para diagramar
- `create-workflow-diagram` — complementa com diagramas Excalidraw

**Feeds into:**
- Documentação do projeto
- Apresentações

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Patterns** | `[OPERACIONAL]: excalidraw-diagrams — [insight]` | `Nunca usar label property, sempre container binding` |

## Quality Gate

- [ ] **Todas as shapes têm labels via container binding**
- [ ] **Arrows conectados via startBinding/endBinding**
- [ ] **Paleta consistente**
- [ ] **Font size mínimo 16**

**If any check fails:** Corrigir o JSON e re-gerar.
