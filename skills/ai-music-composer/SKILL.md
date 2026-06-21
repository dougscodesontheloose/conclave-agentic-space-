---
name: AI Music Composer
description: Composição e geração de trilhas musicais e efeitos sonoros usando modelos de IA (Suno, Udio, MusicLM).
version: 1.0.0
author: Conclave Architecture
license: MIT
metadata:
  conclave:
    tags: [creative, content, automation, music, audio, songwriting]
    related_skills: [manim-video-creator, creative-ideation]
---

# Skill: AI Music Composer

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


Gera trilhas sonoras, jingles, e composições completas através de prompts de texto. Suporta a estruturação de letras e estilos musicais para inputs em engines de áudio generativo.


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

Use esta skill para criar trilhas de fundo para vídeos (Manim), podcasts, apresentações ou jingles de branding.

**Auto-trigger:** Quando o usuário pedir para "gerar uma música", "compor um jingle" ou "criar efeitos sonoros".

## ⚠️ City Limits & Security Rules

1. **OUTPUT:** Arquivos `.mp3` ou `.wav` gerados devem ser salvos dentro do City Limits.
2. **API USAGE:** Monitorar custos de créditos em APIs de terceiros.

## Workflow

1. **Lyrics/Structure:** O Conclave ajuda a escrever a letra e definir o gênero (ex: "Lo-fi hip hop, upbeat").
2. **API Call:** Envio para a engine selecionada.
3. **Retrieval:** Download e verificação do arquivo de áudio.

## Quality Gate

- [ ] **Coerência:** O áudio gerado corresponde ao gênero e tom solicitados.
- [ ] **Acessibilidade:** O arquivo final está disponível no path do projeto.
