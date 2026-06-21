---
privacy: internal
domain: conclave-learning
status: draft
version: 0.1.0
last_validated: 2026-06-05
---

# Conclave Learning Layer

Esta pasta define a Camada Didatica Autonoma do Conclave. Ela nao substitui
squads, ambientes, `memories.md`, COP, SafeGuard ou o Pipeline Runner. Ela
adiciona contratos de baixo atrito para transformar qualquer area de estudo em
um ambiente recorrente, mensuravel e revisavel.

## Principio

Um ambiente de aprendizado deve preservar quatro coisas:

1. identidade pedagogica;
2. estado adaptativo;
3. decisoes estabilizadas;
4. evidencias de progresso.

O Conclave ja possui memoria Markdown, checkpoints e observabilidade. Esta
camada apenas padroniza como esses recursos aparecem em contextos de estudo.

## Contratos

- `learning-environment.schema.md`: estrutura minima de um ambiente de estudo.
- `decision-ledger.schema.md`: decisoes pedagogicas e operacionais que nao
  devem ser reabertas sem motivo.
- `session-log.schema.md`: registro estruturado de sessoes.
- `materials-inventory.schema.md`: catalogo de materiais fisicos e digitais.
- `content-diet.schema.md`: fontes aprovadas, bloqueadas e sob revisao.
- `permission-ladder.md`: niveis graduais de autonomia para agentes.

## Nao objetivos

- Nao criar um banco de dados novo antes de validar os arquivos Markdown.
- Nao mover ambientes existentes.
- Nao alterar o comportamento de squads existentes.
- Nao automatizar acoes externas sem aprovacao humana.
- Nao registrar dados sensiveis em logs exportaveis.

## Ordem de adocao recomendada

1. Aplicar o contrato em um ambiente ja existente.
2. Registrar decisoes locais em `decision.md`.
3. Padronizar `session-log.jsonl`.
4. Adicionar inventario de materiais apenas quando houver ganho operacional.
5. Integrar a um squad depois que o formato estiver estavel.

