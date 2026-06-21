---
privacy: internal
domain: conclave-learning
status: draft
version: 0.1.0
last_validated: 2026-06-05
---

# Learning Environment Schema

Contrato minimo para ambientes de aprendizado recorrente no Conclave.

## Objetivo

Um ambiente de aprendizado e um subprojeto local que preserva metodo, estado,
fontes, sessoes e progresso de uma area especifica. Ele pode ser operado por um
squad, mas nao depende de um squad para existir.

## Estrutura recomendada

```text
ambientes/{grupo-ou-projeto}/{environment}/
  _conclave/
    _memory/
      soul.md
      learning-loop.md
      decision.md
      session-log.jsonl
      materials-inventory.md
      content-diet.md
      progress-ledger.md
  output/
  sources/
```

## Arquivos obrigatorios no MVP

### soul.md

Define identidade, objetivo, restricoes e especificidade pedagogica do
ambiente.

Campos de frontmatter recomendados:

```yaml
---
privacy: internal
domain: learning
environment: environment-code
status: active
last_validated: YYYY-MM-DD
---
```

Secoes recomendadas:

- Identidade do Ambiente
- Fonte de Verdade Atual
- Diagnostico Operacional
- Metodo Principal
- Formatos Preferidos
- Metricas
- Vetoes
- Proxima Direcao

### learning-loop.md

Define estado adaptativo, boot de sessao, loop recorrente, metricas e regra de
avanco.

Secoes recomendadas:

- Estado Atual
- Boot de Sessao
- Loop de Sessao
- Metricas
- Regras de Adaptacao
- Proxima Sessao — Template

## Arquivos opcionais

- `decision.md`: decisoes estabilizadas.
- `session-log.jsonl`: historico estruturado de sessoes.
- `materials-inventory.md`: materiais fisicos e digitais disponiveis.
- `content-diet.md`: fontes aprovadas, condicionais, bloqueadas e em revisao.
- `progress-ledger.md`: marcos de progresso e lacunas persistentes.

## Regras de integracao

- O ambiente deve ser lido antes de qualquer sessao recorrente.
- `soul.md` define identidade e limites; `learning-loop.md` define o estado
  adaptativo.
- `decision.md`, quando existir, deve ser consultado antes de propor mudancas
  estruturais.
- Logs de sessao devem registrar evidencias, nao narrativas longas.
- Materiais externos seguem a politica de conteudo externo do SafeGuard.
- Acoes externas, publicacao, compra, envio ou automacao fisica exigem
  aprovacao humana.

