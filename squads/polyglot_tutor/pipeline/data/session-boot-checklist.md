# Session Boot Checklist

Este arquivo define como iniciar uma sessão de idioma com o mínimo de memória exigida do usuário. A chave principal é o nome do ambiente; o Conclave deve cuidar das perguntas operacionais.

## Princípio de Ergonomia

O usuário não deve precisar memorizar tempo, modo, foco, método, nível ou restrições de cada idioma. Ele só precisa acionar:

```text
/conclave run polyglot_tutor
Omega
```

ou:

```text
Vamos estudar no Omega.
```

A partir disso, o `polyglot_tutor` deve carregar o ambiente, consultar `soul.md` e `learning-loop.md`, e apresentar um boot guiado curto.

## Contrato de Boot

Quando o usuário informar apenas o ambiente ou idioma, isso é input suficiente para iniciar o boot. Não rejeite por falta de tempo, foco ou modo. Em vez disso:

1. Identifique o ambiente.
2. Carregue `language-environments.md`.
3. Carregue `soul.md` local.
4. Carregue `learning-loop.md` local.
5. Aplique os defaults do ambiente.
6. Faça o checklist curto.
7. Se o usuário responder "padrão", execute a sessão usando os defaults.

## Checklist Curto

Apresente no máximo cinco perguntas, sempre com defaults.

```markdown
## Boot da Sessão — {Ambiente}

Vou carregar o loop atual de {idioma}. Para começar, responda só o que quiser mudar:

- Tempo hoje: padrão {default_time} ou outro?
- Intensidade: leve, padrão ou intenso?
- Tipo de sessão: padrão do loop, revisão da última sessão ou foco específico?
- Material: eu escolho, você traz material ou tema específico?
- Saída desejada: sessão guiada agora, roteiro de estudo ou curadoria de materiais?

Se quiser seguir sem ajustar nada, responda: `padrão`.
```

## Defaults Globais

- Se tempo não for informado: usar o default local do `learning-loop.md`.
- Se intensidade não for informada: `padrão`.
- Se tipo de sessão não for informado: `padrão do loop`.
- Se material não for informado: `eu escolho`, respeitando o tema e o método do ambiente.
- Se saída não for informada: `sessão guiada agora`.

## Defaults por Ambiente

| Ambiente | Tempo padrão | Tipo padrão | Material padrão | Saída padrão |
|---|---:|---|---|---|
| `Id like some tea` | 30 min | refinamento avançado | input real C2/profissional | sessão guiada |
| `Hablando demais!` | 45 min | aquisição natural A1 | 3 pilares sem legenda | sessão guiada |
| `ci vediamo dopo` | 45 min | aquisição natural A0 | 3 pilares simples | sessão guiada |
| `Cé la vie` | 45 min | aquisição natural A0 | 3 pilares simples + escrita-som | sessão guiada |
| `gozaimasu` | 45 min | aquisição natural N5 + kana | input visual + trilha kana | sessão guiada |
| `Omega` | 20 ou 45 min | leitura A0+/pre-A1 | microtexto mitológico + audio+texto | sessão guiada |

## Resposta "Padrão"

Se o usuário responder apenas `padrão`, iniciar a sessão sem novo checkpoint longo.

Exemplo para Omega:

```markdown
Boot aceito: padrão.
- Ambiente: Omega
- Tempo: 20 min se rotina curta, 45 min se sessão completa
- Tipo: leitura A0+/pre-A1
- Material: microconto mitológico em grego moderno
- Método: chunking visual + audio+texto + SRS
```

## Progressão

Toda sessão iniciada por boot deve terminar com uma atualização proposta do loop local:

- repetir ou avançar;
- compreensão estimada;
- chunks reconhecidos;
- material usado;
- próximo ajuste;
- evidência de progresso.

O objetivo é evitar a sensação de sempre recomeçar do mesmo ponto. Cada sessão deve consultar o estado anterior e produzir um próximo passo.

## Vetoes

- Não exigir que o usuário memorize o checklist.
- Não rejeitar input que contenha apenas ambiente conhecido.
- Não fazer mais de cinco perguntas no boot.
- Não substituir defaults locais por um template genérico.
- Não iniciar sessão sem consultar `learning-loop.md`.
- Não deixar a sessão sem decisão de progresso: repetir, avançar, reduzir ou intensificar.
