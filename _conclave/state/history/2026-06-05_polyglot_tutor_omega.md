---
title: "Polyglot Tutor — Ambiente Omega para Grego Moderno"
date: 2026-06-05
type: capability_expansion
era: "Memory & Log Optimization (v3)"
impact: medium
---

# Polyglot Tutor — Ambiente Omega para Grego Moderno

## Contexto

O módulo de idiomas do Conclave já operava com um squad central, `polyglot_tutor`, e ambientes separados para inglês, espanhol, italiano e japonês. <user_name> solicitou a inclusão de um novo objeto de estudo: grego moderno, com inspiração no grego antigo, foco inicial em leitura e sem objetivo imediato de fala.

## Decisão

Foi criado o ambiente `Omega` como hub local de grego moderno, mantendo a arquitetura híbrida:

1. **Core central:** `polyglot_tutor` continua responsável por método, roteamento, pesquisa, plano e revisão.
2. **Memória local:** `Omega` recebe `soul.md` e `learning-loop.md` próprios.
3. **Separação de alvo:** grego moderno é o idioma-alvo; grego antigo entra apenas como inspiração cultural, etimológica e comparativa.
4. **Adaptação metodológica:** o framework de aquisição natural passa a reconhecer `pre-A1 de leitura` como caso específico, com fala opcional/adiada e progresso medido por leitura, chunking visual, áudio+texto e SRS.

## Capacidade Adicionada

- Roteamento do input `Omega`, `grego`, `Greek` ou `grego moderno` para o novo ambiente.
- Diagnóstico inicial: A0+/pre-A1 de leitura, com alfabeto/fonologia básica parcialmente superados.
- Loop separado para leitura de grego moderno, usando microcontos mitológicos, citações, causos e vocabulário de alta frequência.
- Critérios de revisão que vetam fala forçada, troca automática para grego antigo e uso de histórias infantis genéricas como eixo principal.

## Impacto

O `polyglot_tutor` passa a suportar um quinto ambiente linguístico com progressão própria. O sistema agora diferencia contato inicial geral de contato inicial voltado à leitura, preservando o interesse cultural do aprendiz sem perder rigor pedagógico.
