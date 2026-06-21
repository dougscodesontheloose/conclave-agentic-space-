---
title: "Camada Didatica Autonoma — Contratos Centrais"
date: 2026-06-05
type: capability_expansion
era: "Memory & Log Optimization (v3)"
impact: medium
---

# Camada Didatica Autonoma — Contratos Centrais

## Contexto

<user_name> trouxe referencias de sistemas multiagentes aplicados a educacao autonoma,
com foco em planejamento, logging multimodal, inventario de materiais,
privacidade, baixo custo e governanca incremental de agentes.

## Decisao

Foi criada uma camada de contratos em `_conclave/core/learning/`, sem alterar o
Runner, squads existentes, dashboard ou ambientes ativos. A camada define
arquivos Markdown/JSONL que podem ser adotados gradualmente por ambientes de
aprendizado.

## Capacidade Adicionada

- Schema de ambiente de aprendizado.
- Ledger de decisoes pedagogicas e operacionais.
- Log estruturado de sessoes.
- Inventario de materiais fisicos e digitais.
- Dieta de conteudo aprovada, condicional, bloqueada ou em revisao.
- Escada de permissao para agentes de aprendizado.

## Impacto

O Conclave passa a ter uma base comum para transformar hubs como o Polyglot
Tutor em ambientes de aprendizado mais observaveis, estaveis e seguros, sem
forcar migracao imediata nem acrescentar automacao antes de validar os
contratos.

