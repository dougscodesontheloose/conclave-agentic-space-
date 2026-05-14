---
name: p5js Creative Coding
description: Geração de esboços e visualizações generativas usando p5.js e processamento criativo.
version: 1.0.0
author: Conclave Architecture
license: MIT
metadata:
  conclave:
    tags: [creative, development, visualization, p5js, generative-art, canvas]
    related_skills: [manim-video-creator, creative-ideation]
---

# Skill: p5js Creative Coding

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


Cria visualizações interativas, artes generativas e animações baseadas em canvas usando a biblioteca p5.js. O Conclave gera o código e fornece um ambiente de visualização (HTML/JS).


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Contexto** — Qual a situação atual?
2. **Objetivo** — O que define o sucesso desta execução?
3. **Restrições** — O que não devemos fazer?

### Environment Variables

```env
# Nenhuma variável obrigatória estrita
```

### Dependencies

Nenhuma. Pure reasoning skill.

## When to Use

Use esta skill para prototipar visualizações de dados criativas, gerar patterns visuais para branding, ou criar animações procedurais leves que rodam no browser.

**Auto-trigger:** Quando o usuário pedir para "codar uma arte generativa", "usar p5js" ou "criar uma visualização interativa em canvas".

## ⚠️ City Limits & Security Rules

1. **SANDBOX:** O código JS gerado deve ser executado no contexto do browser do usuário (via arquivo HTML temporário) e não deve ter acesso a APIs do sistema fora do browser.
2. **ASSETS:** Imagens ou dados usados no sketch p5js devem estar dentro do City Limits.

## Workflow de Geração

1. **Geração do Sketch:** O Conclave escreve o arquivo `sketch.js`.
2. **Wrapper HTML:** O Conclave gera um `index.html` básico injetando o CDN do p5.js e o `sketch.js`.
3. **Visualização:** O usuário abre o arquivo no browser para ver o resultado.

```javascript
// Exemplo de Sketch gerado
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  ellipse(mouseX, mouseY, 50, 50);
}
```

## Quality Gate

- [ ] **Execução:** O arquivo HTML gerado abre sem erros de console.
- [ ] **Aesthetica:** A visualização atende aos critérios de design premium do Conclave.
