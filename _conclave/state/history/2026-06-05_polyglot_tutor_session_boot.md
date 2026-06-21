---
title: "Polyglot Tutor — Boot Guiado por Ambiente"
date: 2026-06-05
type: capability_expansion
era: "Memory & Log Optimization (v3)"
impact: medium
---

# Polyglot Tutor — Boot Guiado por Ambiente

## Contexto

<user_name> identificou um atrito de uso no módulo de idiomas: para iniciar uma sessão produtiva, ele não queria precisar memorizar tempo, modo, foco, material e restrições de cada idioma. A memória desejada deveria ser mínima: lembrar o nome do ambiente ou o idioma, e deixar o Conclave conduzir o restante.

## Decisão

Foi criado um protocolo de boot guiado no `polyglot_tutor`. Quando o usuário informa apenas um ambiente conhecido, como `Omega`, `gozaimasu`, `ci vediamo dopo`, `Hablando Demais` ou `Id like some tea`, o sistema deve:

1. carregar o registro de ambientes;
2. carregar `soul.md` e `learning-loop.md` locais;
3. aplicar os defaults daquele idioma;
4. apresentar um checklist curto de até cinco perguntas;
5. aceitar `padrão` como resposta suficiente;
6. encerrar a sessão com decisão de progressão.

## Capacidade Adicionada

- Novo arquivo `session-boot-checklist.md` no core do `polyglot_tutor`.
- Defaults de boot adicionados aos loops locais de inglês, espanhol, italiano, japonês e grego.
- Pipeline ajustado para não rejeitar input curto com ambiente conhecido.
- Matriz de intenção atualizada para reconhecer nomes de idiomas e ambientes como gatilhos do `polyglot_tutor`.
- Reindexador atualizado para preservar esses gatilhos quando a matriz for regenerada.
- Router ajustado para preservar input curto de ambiente como boot de sessão.
- Revisão passa a vetar sessões sem decisão de progressão: repetir, avançar, reduzir dificuldade ou intensificar.

## Impacto

O módulo de idiomas passa a operar como um sistema mais fluido de estudo recorrente. O usuário aciona apenas o ambiente; o Conclave conduz o boot, aplica o loop local e mantém a progressão de cada idioma separada.
