# Language Environments Registry

Este arquivo é a ponte entre o core `polyglot_tutor` e os hubs locais de aprendizado. Ele define onde cada idioma mora, qual é o nível atual declarado e qual `soul.md` deve ser carregado antes de qualquer plano, correção ou atualização de app.

## Regra Central

O core nunca deve tratar os idiomas como variações cosméticas do mesmo curso. Cada ambiente tem:

- nível atual;
- objetivo;
- profissionais/agentes locais;
- especificidades linguísticas;
- formato de UI;
- memória de aprendizado;
- contrato de integração com ferramentas de IA.

## Ambientes Identificados

| Idioma | Ambiente | Caminho | Nível atual | Uso principal | Soul | Loop |
|---|---|---|---|---|---|---|
| Inglês | I'd like some tea | `ambientes/projetos/Id like some tea` | C2/proficiente | refinamento avançado, US/UK, vocabulário técnico, fluência e pronúncia | `_conclave/_memory/soul.md` | `_conclave/_memory/learning-loop.md` |
| Espanhol | Hablando Demais | `ambientes/projetos/Hablando demais!` | A1 falso-iniciante | fundações, conversação inicial, ponte para espanhol profissional | `_conclave/_memory/soul.md` | `_conclave/_memory/learning-loop.md` |
| Italiano | Ci Vediamo Dopo / Ativi Di Amodopo | `ambientes/projetos/ci vediamo dopo` | A0 | alfabetização linguística inicial, fonética, frases essenciais | `_conclave/_memory/soul.md` | `_conclave/_memory/learning-loop.md` |
| Francês | Cé la vie | `ambientes/projetos/Cé la vie` | A0 | fundação sonora, escrita-som, frases essenciais, cortesia e rotina | `_conclave/_memory/soul.md` | `_conclave/_memory/learning-loop.md` |
| Japonês | Gozaimasu | `ambientes/projetos/gozaimasu` | A0/N5 inicial | kana, partículas, cumprimentos, estrutura SOV | `_conclave/_memory/soul.md` | `_conclave/_memory/learning-loop.md` |
| Grego moderno | Omega | `ambientes/projetos/Omega` | A0+/pre-A1 leitura | leitura em grego moderno, chunking visual, audio+texto e repertorio mitologico | `_conclave/_memory/soul.md` | `_conclave/_memory/learning-loop.md` |

## Ambientes Não Classificados Como Idioma

- `ambientes/projetos/corporeitura`: app conceitual/literário-corporal; não deve receber rotinas de idiomas por padrão.
- `ambientes/projetos/Arcade House`: aparece em registros históricos, mas não é um hub ativo de idioma neste mapeamento.

## Contrato de Carregamento

Antes de atuar em um idioma específico:

1. Identificar idioma ou ambiente pelo pedido do usuário.
2. Ler este registro.
3. Ler o `soul.md` do ambiente correspondente.
4. Ler o `learning-loop.md` do ambiente correspondente.
5. Ler logs locais quando a tarefa depender de progresso real.
6. Aplicar o `language-specificity-framework.md`.
7. Gerar output no idioma de saída preferido do usuário, preservando exemplos no idioma-alvo.

## Contrato de Escrita

Quando um plano gerar aprendizado reutilizável:

- Atualizar o `soul.md` apenas se a mudança for estrutural ou confirmada pelo usuário.
- Atualizar o `learning-loop.md` após sessões de estudo ou mudanças de progressão.
- Atualizar logs locais para eventos de sessão, progresso ou manutenção.
- Atualizar componentes React somente quando o usuário pedir alteração de interface ou exportação para hub.
- Nunca misturar vocabulário, roteiro ou status de um idioma dentro do ambiente de outro.

## Perfis Operacionais

### English / I'd like some tea

- Tipo: refinement hub.
- Agentes: Scholar, Lexicist.
- Deve evitar: exercícios básicos de A1/A2, vocabulário genérico e correções condescendentes.
- Deve priorizar: collocations, register, idioms, discourse markers, precision grammar, accent work, executive communication.

### Spanish / Hablando Demais

- Tipo: foundation-to-professional hub.
- Agentes: Mestre, Analista.
- Estado corrigido: apesar de arquivos antigos citarem B1/B2, o nível atual declarado é A1 falso-iniciante.
- Deve priorizar: pronúncia, verbos essenciais, ser/estar, presente, gêneros, frases de sobrevivência e vocabulário de dados em dose baixa.
- Método padrão: aquisição natural com 45 minutos diários, Silent Period, 3 pilares e repetição até 80% de compreensão.

### Italian / Ci Vediamo Dopo

- Tipo: zero-to-A1 hub.
- Agente: Professore.
- Deve priorizar: sons abertos, vogais, artigos, gênero/número, presente de verbos frequentes e frases pessoais.
- Deve usar: ponte com português com cuidado para evitar falsos amigos.
- Método padrão: aquisição natural com 45 minutos diários, Silent Period, 3 pilares e repetição até 80% de compreensão.

### French / Cé la vie

- Tipo: zero-to-A1 hub.
- Agente: Professeur.
- Estado inicial: A0.
- Deve priorizar: escrita-som, vogais nasais, `u` francês, `r` uvular, liaison, letras finais silenciosas, artigos e frases pessoais.
- Deve usar: ponte com português com cuidado; cognatos ajudam na leitura, mas podem esconder pronúncia errada e falsos amigos.
- Deve evitar: ensinar francês como variação de italiano, iniciar por tabelas extensas de conjugação ou ignorar a distância entre grafia e som.
- Método padrão: aquisição natural com 45 minutos diários, Silent Period, 3 pilares e repetição até 80% de compreensão.

### Japanese / Gozaimasu

- Tipo: A0/N5 foundation hub.
- Agente: Sensei.
- Deve priorizar: hiragana, katakana, partículas, ordem SOV, cumprimentos e fórmulas de polidez.
- Deve evitar: kanji cedo demais, romaji como muleta permanente, excesso de gramática abstrata.
- Método padrão: aquisição natural com 45 minutos diários, Silent Period, 3 pilares e repetição até 80% de compreensão; escrita kana corre em trilha separada.

### Modern Greek / Omega

- Tipo: reading-first foundation hub.
- Agente: tutor de leitura helenica, com foco em grego moderno e inspiracao cultural no grego antigo.
- Estado inicial: A0+/pre-A1 para leitura; o alfabeto e a fonologia basica ja foram parcialmente superados.
- Deve priorizar: sair da decodificacao letra-a-letra para chunking de palavras, audio+texto em grego, vocabulario de alta frequencia, conectores e leitura fluente.
- Deve usar: contos curtos, citacoes e causos de mitologia grega em grego moderno simplificado, em vez de historias infantis como eixo principal.
- Deve separar: grego moderno como idioma-alvo; grego antigo como inspiracao cultural, etimologica e comparativa, nunca como objetivo principal automatico.
- Metodo padrão: aquisição natural adaptada para leitura, com Silent Period oral, 3 pilares, repeticao ate 80% de compreensao e trilha SRS para palavras de alta frequencia.
