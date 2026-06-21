---
name: ASCII Art Generator
description: Geração de arte e vídeos ASCII a partir de imagens, textos ou streams de vídeo.
version: 1.0.0
author: Conclave Architecture
license: MIT
metadata:
  conclave:
    tags: [creative, design, visualization, ascii, terminal-art]
    related_skills: [manim-video-creator, creative-ideation]
---

# Skill: ASCII Art Generator

**Core principle:** A precisão da resposta é diretamente proporcional à clareza da intenção.


Transforma inputs visuais (imagens, vídeos) ou strings de texto em representações ASCII estilizadas para uso em terminais, documentação markdown ou comunicações retrô.


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

Use esta skill quando precisar de visualizações leves para o terminal, branding retrô, ou quando quiser "desenhar" algo em um ambiente que suporta apenas texto (ex: logs, readmes).

**Auto-trigger:** Quando o usuário pedir para gerar arte ASCII, converter imagem para texto ou criar banners de terminal.

## ⚠️ City Limits & Security Rules

1. **FILE ACCESS:** Garanta que o acesso a imagens/vídeos de entrada respeite o City Limits (`/Users/douglasdepaulamoura/Documents/Bancada/`).
2. **CLEANUP:** Arquivos temporários de frames de vídeo convertidos devem ser limpos após a execução.

## Orquestração

### Modo 1: Texto para ASCII (Banner)
```bash
# Exemplo usando utilitário interno ou figlet se disponível
# (O Conclave prefere usar scripts python stdlib para portabilidade)
python3 -c "import pyfiglet; print(pyfiglet.figlet_format('CONCLAVE'))"
```

### Modo 2: Imagem para ASCII
```bash
# Executa script de conversão (ex: usando PIL/OpenCV)
# (Assumindo script internal: scripts/image_to_ascii.py)
python3 skills/ascii-art-generator/scripts/convert.py --input image.png --width 80
```

## Inputs e Parâmetros

| Parâmetro | Descrição |
|---|---|
| `--input` | Caminho do arquivo de imagem/vídeo |
| `--width` | Largura em caracteres da saída |
| `--charset` | Conjunto de caracteres (ex: 'simple', 'complex', 'blocks') |

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Performance** | `[OPERACIONAL]: ascii-art-generator — [insight]` | `[OPERACIONAL]: ascii-art-generator — Imagens com alto contraste produzem melhores resultados ASCII.` |

## Quality Gate

- [ ] **Visibilidade:** O resultado no terminal é legível com a largura de caractere padrão.
- [ ] **Limpeza:** Nenhum frame temporário deixado em `/tmp/`.
