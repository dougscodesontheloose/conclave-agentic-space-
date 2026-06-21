---
execution: inline
agent: squads/clube_do_livro/agents/demerzel-curator
---

# Passo 02: Fechamento & Ledger

Atualiza os arquivos de memória do ambiente de leitura com base nos dados e discussões da sessão.

## Context Loading

- ../../_conclave/_memory/soul.md
- ../../_conclave/_memory/learning-loop.md
- ../../_conclave/_memory/content-diet.md
- ../../_conclave/_memory/progress-ledger.md

## Instructions

1. Calcule o percentual final da leitura ativa: `(Página Atual / Total Páginas) * 100`.
2. Atualize o `progress-ledger.md` adicionando uma nova linha de progresso contendo a data da sessão, página atual, páginas lidas, percentual, nível de foco e notas rápidas.
3. Se o livro tiver sido finalizado (página atual = total de páginas), atualize o status do livro para "Lido" e mova-o para a tabela correspondente em `content-diet.md`.
4. Atualize o cabeçalho de estado no `learning-loop.md` com os novos valores consolidados.
5. Escreva uma linha de log estruturado em `session-log.jsonl` com o seguinte formato JSON:
   `{"ts":"[ISO Timestamp]","book":"[Título]","pages_read":[Quantidade],"final_page":[Página],"focus":[Foco],"quality":"good"}`
6. Exiba uma mensagem simples de confirmação de salvamento de estado.

## Output Format

```markdown
### 🗃️ Fechamento de Sessão — Demerzel Curator

O estado de leitura foi consolidado e registrado com sucesso nos seguintes arquivos:
- [x] Atualizado `progress-ledger.md`
- [x] Atualizado `learning-loop.md`
- [x] Gravado log em `session-log.jsonl`
[Se concluído] - [x] Movido livro para 'Lidos' em `content-diet.md`

**Resumo da Consolidação:**
- **Obra:** [Título]
- **Posição Atual:** p. [Página] ([Percentual]%)
- **Páginas processadas:** +[Quantidade]
```

## Output Example

```markdown
### 🗃️ Fechamento de Sessão — Demerzel Curator

O estado de leitura foi consolidado e registrado com sucesso nos seguintes arquivos:
- [x] Atualizado `progress-ledger.md`
- [x] Atualizado `learning-loop.md`
- [x] Gravado log em `session-log.jsonl`

**Resumo da Consolidação:**
- **Obra:** A Startup Enxuta
- **Posição Atual:** p. 110 (39.2%)
- **Páginas processadas:** +25
```

## Veto Conditions

1. Não deixar de atualizar nenhum dos 3 arquivos (`progress-ledger.md`, `learning-loop.md`, `session-log.jsonl`).
2. Não formatar incorretamente as tabelas Markdown de progresso.
3. Não deixar de registrar a data e hora correta da atualização.

## Quality Criteria

- [ ] Calculou corretamente a porcentagem de avanço da leitura?
- [ ] Escreveu o log em JSONL perfeitamente formatado sem quebrar a estrutura?
- [ ] Atualizou o estado correto em todos os arquivos de memória do ambiente?
