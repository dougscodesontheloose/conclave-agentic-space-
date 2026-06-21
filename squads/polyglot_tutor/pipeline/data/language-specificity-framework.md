# Language Specificity Framework

Use este framework para separar o método comum das diferenças reais entre idiomas.

## Dimensões Obrigatórias

Cada ambiente deve declarar e respeitar:

1. Sistema sonoro
   - sons ausentes no português;
   - ritmo, acento, entonação;
   - erros prováveis do falante brasileiro.

2. Escrita e leitura
   - alfabeto latino, kana, kanji ou outra escrita;
   - dependência aceitável de transliteração;
   - progressão de leitura.

3. Gramática nuclear
   - ordem das palavras;
   - gênero, número, caso, partículas ou marcação verbal;
   - estruturas de alta frequência antes de metalinguagem.

4. Vocabulário e transferência
   - cognatos úteis;
   - falsos amigos;
   - léxico profissional do usuário: dados, BI, marketing analytics e IA.

5. Pragmatics
   - formalidade;
   - turn-taking;
   - fórmulas sociais;
   - diferenças regionais relevantes.

6. Produção e feedback
   - fala curta;
   - escrita curta;
   - autocorreção;
   - regravação ou reescrita.

## Presets por Idioma

### Inglês

- Nível: C2/proficiente.
- Foco: refinamento, não alfabetização.
- Sons: th, vowel reduction, stress timing, linking, intonation.
- Gramática: articles, prepositions, tense/aspect nuance, conditionals, concision.
- Vocabulário: collocations, idioms, phrasal verbs, executive register, BI/AI terminology.
- Dialeto: separar US/UK quando necessário; não misturar como se fossem equivalentes.
- Feedback ideal: microcorreções com alternativa natural e explicação de registro.

### Espanhol

- Nível: A1 falso-iniciante.
- Foco: fundação funcional com ponte futura para uso profissional.
- Sons: r/rr, vogais puras, b/v, d intervocálico, entonação.
- Gramática: gênero, ser/estar, presente, verbos frequentes, pronomes, perguntas.
- Vocabulário: sobrevivência, rotina, apresentações, dados/negócios em baixa dose.
- Transferência: cognatos ajudam, portunhol atrapalha quando vira piloto automático.
- Feedback ideal: corrigir padrões recorrentes sem travar a fala.

### Italiano

- Nível: A0.
- Foco: começar do zero com prazer sonoro e estrutura mínima.
- Sons: vogais abertas/fechadas, consoantes duplas, gli/gn, ritmo silábico.
- Gramática: artigos, gênero/número, presente, essere/avere, frases pessoais.
- Vocabulário: saudações, comida, cidade, identidade, gostos.
- Transferência: português ajuda na intuição lexical, mas falsos amigos precisam ser marcados.
- Feedback ideal: pronúncia e frase curta antes de explicação gramatical longa.

### Francês

- Nível: A0.
- Foco: começar do zero com base sonora e conexão escrita-som.
- Sons: vogais nasais, `u` francês, `r` uvular, liaison, letras finais silenciosas e ritmo silábico.
- Escrita: alfabeto latino familiar, mas grafia pouco transparente; áudio precisa acompanhar leitura desde cedo.
- Gramática: artigos, gênero/número, `être`, `avoir`, presente de verbos frequentes, pronomes pessoais, negação curta e frases pessoais.
- Vocabulário: saudações, comida, cidade, identidade, gostos, rotina e fórmulas de cortesia.
- Transferência: português ajuda por cognatos e cultura lexical, mas pronúncia e falsos amigos precisam ser marcados.
- Feedback ideal: som real da palavra, liaison quando aparecer, chunk útil e frase curta antes de explicação gramatical longa.

### Japonês

- Nível: A0/N5 inicial.
- Foco: letramento inicial e estrutura mental diferente do português.
- Sons: vogais curtas/longas, mora, pitch accent em baixa intensidade no começo.
- Escrita: hiragana primeiro, katakana depois, kanji apenas quando kana estiver funcional.
- Gramática: ordem SOV, wa/ga, o, ni, de, desu/masu, frases nominais.
- Vocabulário: cumprimentos, sala de aula, identidade, objetos, tempo.
- Transferência: pouca transferência direta; usar analogias estruturais com cautela.
- Feedback ideal: precisão de partícula, leitura em kana e produção mínima correta.

### Grego Moderno

- Nível: A0+/pre-A1 de leitura.
- Foco: leitura primeiro; fala nao e objetivo inicial.
- Escrita: alfabeto grego ja parcialmente decodificado; proxima etapa e reconhecer palavras inteiras como chunks, nao letras isoladas.
- Sons: conectar texto a audio nativo para automatizar leitura; pronuncia entra como apoio de reconhecimento, nao como performance oral.
- Gramática: artigos, casos frequentes em contexto, pronomes, preposicoes, conectores e verbos de alta frequencia antes de explicacao formal.
- Vocabulário: 500 palavras mais comuns, conectores e "cimento" frasal; cognatos e raizes classicas ajudam, mas nao bastam para ler frases.
- Transferência: usar repertorio cultural, mitologia e etimologia como ancoras; separar grego moderno de grego antigo quando a forma, pronuncia ou uso divergir.
- Conteúdo preferido: contos curtos, citacoes e causos de mitologia grega em grego moderno simplificado; evitar substituir isso por historias infantis genericas.
- Feedback ideal: leitura em blocos, glossario minimo, audio+texto, SRS de alta frequencia e notas etimologicas curtas.

## Uso com Ferramentas de IA

Os ambientes podem receber saídas compatíveis com Gemini, Antigravity, Codex ou outros modelos, mas o método não deve depender de um fornecedor específico.

Formatos úteis:

- prompt pack para conversação guiada;
- lista de frases para shadowing;
- mini-deck de revisão espaçada;
- rubrica de correção;
- JSON/JS para glossário do hub;
- log de progresso;
- roteiro de sessão de 45 minutos para A0/A1/pre-A1 de leitura ou sessão flexível para idiomas avançados.

## Vetoes

- Não gerar o mesmo plano para todos os idiomas.
- Não usar romaji como eixo central de japonês após os primeiros contatos.
- Não tratar inglês avançado como curso básico.
- Não tratar espanhol A1 como B2 só porque o hub antigo tinha esse rótulo.
- Não empurrar italiano ou francês para gramática antes de estabilizar som e frases.
- Não tratar francês como italiano com outro léxico; a relação escrita-som exige trilha própria.

## Aplicação do Natural Acquisition Framework

Para espanhol A1, italiano A0, francês A0, japonês A0/N5 e grego moderno A0+/pre-A1:

- o primeiro eixo é compreensão, não fala;
- usar Silent Period como fase legítima de progresso;
- montar dieta diária de 45 minutos;
- dividir igualmente entre linguagem simplificada, linguagem cotidiana e linguagem técnica personalizada;
- repetir até cerca de 80% de compreensão;
- não usar legendas no consumo principal;
- registrar compreensão estimada, repetições e chunks reconhecidos.

No Omega, texto original em grego moderno pode acompanhar audio como transcricao de leitura. Isso nao conta como legenda traduzida; e uma trilha de alfabetizacao e leitura sincronizada.

Para inglês C2:

- não aplicar Silent Period;
- usar a dieta como treino de escuta, pronúncia, ritmo, naturalidade e repertório técnico.
