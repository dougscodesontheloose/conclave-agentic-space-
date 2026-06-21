---
name: ComfyUI Image Gen
description: Automação e orquestração de workflows de geração de imagem via API do ComfyUI.
version: 1.0.0
author: Conclave Architecture
license: MIT
metadata:
  conclave:
    tags: [creative, design, automation, ai-images, stable-diffusion, comfyui]
    related_skills: [manim-video-creator, creative-ideation]
---

# Skill: ComfyUI Image Gen

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


Orquestra e automatiza a geração de imagens de alta fidelidade usando a API do ComfyUI. Esta skill permite enviar prompts, configurar checkpoints e recuperar imagens geradas de forma programática.


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

Requer ambiente de execução padrão do Conclave.

## When to Use

Use esta skill para produções de imagem em massa, workflows complexos de Image-to-Image, Inpainting ou quando precisar de controle granular sobre o grafo de geração (Stable Diffusion).

**Auto-trigger:** Quando o usuário solicitar automação de ComfyUI ou geração de imagens via pipelines complexas.

## ⚠️ City Limits & Security Rules

1. **API SECRETS:** Chaves de API ou endereços de servidor ComfyUI devem ser lidos de arquivos de configuração seguros.
2. **LOCAL OUTPUT:** As imagens baixadas devem ser salvas no diretório de assets do projeto dentro do City Limits.

## Exemplo de Orquestração

O Conclave envia um payload JSON para o endpoint `/prompt` do ComfyUI:

```python
# Pseudo-código de ativação
import websocket
import json

def queue_prompt(prompt):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    # Request para o servidor
```

## Quality Gate

- [ ] **Conectividade:** O servidor ComfyUI está acessível e respondendo.
- [ ] **Integridade:** O output gerado é movido para a pasta final e indexado no squad memory.
