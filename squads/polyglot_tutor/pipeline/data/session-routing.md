# Session Routing Protocol

Este protocolo explica como iniciar sessões de estudo por idioma dentro do Conclave.

## Arquitetura Atual

O sistema usa uma arquitetura híbrida:

- `polyglot_tutor`: squad central de método, roteamento, pesquisa, plano, revisão e contratos.
- Ambientes de idioma: hubs locais com `soul.md`, `learning-loop.md`, agentes, logs e UI própria.

Isso evita duplicar a pedagogia em varios squads diferentes, mas preserva loops de aprendizado separados por idioma.

## Quando Usar o Squad Central

Use `polyglot_tutor` sempre que quiser:

- iniciar sessão de estudo;
- montar dieta linguística;
- pesquisar material;
- criar plano de estudo;
- corrigir produção;
- atualizar orientação de um ambiente;
- transformar uma sessão em blocos para hub React.

## Como Chamar no Conclave

### Chamada mínima

Você pode chamar apenas com o ambiente. O Conclave deve iniciar o boot guiado, não exigir que o usuário lembre todos os parâmetros.

```text
/conclave run polyglot_tutor
Omega
```

```text
Vamos estudar no gozaimasu.
```

Depois disso, usar `session-boot-checklist.md`.

### Comando explícito

```text
/conclave run polyglot_tutor
```

Depois informe o ambiente e a sessão desejada:

```text
Ambiente: ci vediamo dopo
Idioma: italiano
Modo: aquisição natural
Objetivo: sessão de hoje A0
Tempo: 45 minutos
```

### Linguagem natural

Também pode chamar assim:

```text
Vamos estudar italiano no ci vediamo dopo. Quero a sessão de hoje, A0, aquisição natural, 45 minutos.
```

```text
Vamos estudar espanhol no Hablando Demais. Monta minha dieta linguística de hoje para A1 falso-iniciante.
```

```text
Vamos estudar japonês no gozaimasu. Quero input inicial N5 com kana separado e sem legenda no consumo principal.
```

```text
Vamos refinar inglês no I'd like some tea. Quero trabalhar pronúncia, fluência e vocabulário executivo em nível C2.
```

```text
Vamos estudar grego moderno no Omega. Quero uma sessão de leitura A0+/pre-A1 com mitologia grega, audio+texto e sem objetivo de fala por enquanto.
```

```text
Vamos estudar francês no Cé la vie. Quero a sessão de hoje, A0, aquisição natural, 45 minutos.
```

## Roteamento por Ambiente

| Input do usuário | Ambiente | Arquivos carregados |
|---|---|---|
| inglês, English, tea, I'd like some tea | `Id like some tea` | `soul.md`, `learning-loop.md`, logs locais |
| espanhol, Spanish, Hablando | `Hablando demais!` | `soul.md`, `learning-loop.md`, logs locais |
| italiano, Italian, ci vediamo dopo | `ci vediamo dopo` | `soul.md`, `learning-loop.md`, logs locais |
| francês, frances, French, Cé la vie, Ce la vie, C'est la vie | `Cé la vie` | `soul.md`, `learning-loop.md`, logs locais |
| japonês, Japanese, gozaimasu | `gozaimasu` | `soul.md`, `learning-loop.md`, logs locais |
| grego, Greek, grego moderno, Omega | `Omega` | `soul.md`, `learning-loop.md`, logs locais |

## Contrato de Sessão

Toda sessão deve:

1. Identificar ambiente e idioma.
2. Ler `language-environments.md`.
3. Ler `session-boot-checklist.md`.
4. Ler o `soul.md` local.
5. Ler o `learning-loop.md` local.
6. Se faltarem tempo, modo ou foco, iniciar boot guiado curto em vez de rejeitar o input.
7. Aplicar o framework adequado.
8. Produzir a sessão no output do squad.
9. Registrar proposta de atualização do loop.

## Boot por Ambiente

Quando a entrada for curta, como `Omega` ou `vamos estudar italiano`, use esta lógica:

```text
ambiente identificado -> carregar loop local -> perguntar checklist curto -> aceitar "padrão" -> executar sessão -> propor atualização do loop
```

O usuário deve memorizar apenas:

- o comando `/conclave run polyglot_tutor`;
- o nome do ambiente;
- ou uma frase natural com o idioma.

## Atualização do Loop

Depois de uma sessão, atualizar ou propor atualização em:

```text
ambientes/projetos/{ambiente}/_conclave/_memory/learning-loop.md
```

Atualizações típicas:

- material usado;
- compreensão estimada;
- número de repetições;
- chunks reconhecidos;
- dificuldade percebida;
- próximo ajuste;
- próximo material ou repetição.

## Regra de Separação

Nunca carregar progresso de um idioma como se fosse progresso de outro.

- Inglês C2 não reduz a carga inicial de japonês.
- Espanhol A1 não implica italiano A1.
- Italiano A0 não compartilha vocabulário automaticamente com espanhol.
- Francês A0 não deve ser tratado como italiano A0 com pronúncia diferente; escrita-som, nasais e liaison exigem trilha própria.
- Japonês tem trilha própria de escrita e não segue lógica de língua latina.
- Grego moderno herda alfabeto/fonologia inicial já parcialmente decodificados, mas isso não equivale a leitura fluente.
- Grego antigo pode inspirar temas e etimologia no Omega, mas não substitui o alvo principal: leitura de grego moderno.
