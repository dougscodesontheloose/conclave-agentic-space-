---
execution: inline
agent: squads/clube_do_livro/agents/demerzel-curator
---

# Passo 00: Boot de Leitura

Este passo inicializa a sessão de leitura, carrega o contexto literário e solicita informações sobre as páginas lidas e/ou anotações brutas.

## Context Loading

- ../../_conclave/_memory/soul.md
- ../../_conclave/_memory/learning-loop.md
- ../../_conclave/_memory/content-diet.md
- ../../_conclave/_memory/progress-ledger.md

## Instructions

1. Leia o `content-diet.md` para identificar o livro que está no estado "Lendo Agora".
2. Se não houver livro ativo, solicite ao <user_name> que indique qual obra da "Fila de Espera" ou nova ele deseja iniciar.
3. Leia o `progress-ledger.md` para encontrar a última página registrada desse livro.
4. Apresente ao usuário o status do livro ativo e pergunte qual a página atual atingida.
5. Peça para o usuário inserir as notas brutas ou observações do dia para a discussão crítica.

## Output Format

```markdown
### 📚 Conclave Clube do Livro — Boot de Sessão

- **Livro Ativo:** [Título do Livro] (por [Autor])
- **Última Página Registrada:** p. [Página] (de [Total])
- **Progresso:** [Percentual]%

Responda indicando a **nova página atual** e, se desejar, digite ou cole suas **anotações de leitura** (marginalia) para iniciarmos a discussão crítica.
```

## Output Example

```markdown
### 📚 Conclave Clube do Livro — Boot de Sessão

- **Livro Ativo:** A Startup Enxuta (por Eric Ries)
- **Última Página Registrada:** p. 85 (de 280)
- **Progresso:** 30.3%

Responda indicando a **nova página atual** e, se desejar, digite ou cole suas **anotações de leitura** (marginalia) para iniciarmos a discussão crítica.
```

## Veto Conditions

1. Não prosseguir se não houver um livro ativo ou selecionado pelo usuário.
2. Não aceitar uma página atual menor do que a última registrada no ledger.
3. Não registrar dados confidenciais do usuário.

## Quality Criteria

- [ ] Identificou o livro ativo corretamente a partir do `content-diet.md`?
- [ ] Recuperou a última página correta do `progress-ledger.md`?
- [ ] Formatou o output final com as informações recuperadas?

<!-- Padding para validação de infraestrutura ---------------------------------------------------------------------------------------------------- -->
 -->
 -->
 -->
 -->
 -->
