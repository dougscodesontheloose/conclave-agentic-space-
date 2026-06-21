---
title: "COP — Conclave Observer Protocol"
date: 2026-05-14
type: architectural_shift
era: "Memory & Log Optimization (v3)"
impact: critical
---

# 🌾 COP — Conclave Observer Protocol

## Contexto

O ecossistema Conclave possuía uma arquitetura de autoaprendizado sofisticada (cadeia D3→D8 no `runner.pipeline.md`) com 4 feedback loops projetados, 6 subroutines GAIA, e streams JSONL para sinais de qualidade, gossip cross-squad e inferência de user-model.

**Problema**: todo o learning loop dependia exclusivamente de `conclave run` — uma invocação formal de pipeline que o usuário raramente executava. O uso real do sistema era conversacional e direto, resultando em **100% da arquitetura de aprendizado codificada e 0% alimentada com dados de produção**.

## Decisão Arquitetural

Introduzir o **Conclave Observer Protocol (COP)** — um mecanismo passivo de coleta de sinais que se embute no fluxo natural de trabalho (AGENTS.md → sessão → heartbeat), dropando breadcrumbs silenciosamente durante qualquer interação e harvesting automaticamente no fim da sessão.

**Princípio**: não forçar o usuário a mudar seu fluxo de trabalho. Instrumentar o fluxo que já existe.

## Componentes Implementados

1. **`breadcrumb.py`** — Script Python (drop / harvest / status) que gerencia o ciclo de vida dos breadcrumbs
2. **AGENTS.md instrumentado** — Step 9 (COP init) + regra de breadcrumb tracking em Critical Rules
3. **heartbeat.py com harvest** — `harvest_breadcrumbs()` roda antes do scan de leaks no `--end`
4. **`/conclave harvest`** — Comando manual para harvest a qualquer momento (rota no SKILL.md)
5. **`bridge_session_logs.py`** — Script one-shot que bootstrappou 8 sessões históricas no `session-log.jsonl`
6. **Fix de `promote_signals.py`** — Schema mismatch corrigido (`"value"` adicionado como primeiro campo de lookup)

## Impacto nos GAIA Subroutines

- 🌊 POSEIDON: passa a ter marés para ler (session-log populado)
- 🦉 MINERVA: passa a ter run history para scoring
- 🏹 ARTEMIS: gossip bus pode começar a emitir se squads gerarem quality:good
- 🌱 ELEUTHIA: user-model começa a acumular dados para drift detection
- 🔨 HEPHAESTUS: skill-candidates podem aparecer se D5 disparar

## Metáfora

> A biblioteca de Alexandria já estava construída. O COP são os bibliotecários que trazem os livros — a política de documentação constante que mantém a memória viva e em evolução, sem pausa para inventário.
