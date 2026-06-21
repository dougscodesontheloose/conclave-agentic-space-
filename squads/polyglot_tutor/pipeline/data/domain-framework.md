# Domain Framework

O Polyglot Tutor opera como motor de aprendizagem, não apenas como curador de links. Toda saída precisa conectar objetivo, nível, insumo, prática, feedback e revisão.

## Camadas do Método

1. Diagnosticar o aluno
   - Idioma-alvo e idioma de saída.
   - Nível CEFR estimado ou sinais observáveis quando o nível for incerto.
   - Objetivo real: compreensão, fala, escrita, leitura, pronúncia, vocabulário, certificação ou uso profissional.
   - Tempo disponível, energia cognitiva e tolerância a rotina.

2. Definir o modo de entrega
   - Plano de estudo: roadmap de dias/semanas.
   - Treino prático: sessão de exercícios, fala, escrita ou shadowing.
   - Curadoria: lista de materiais e sequência de consumo.
   - Diagnóstico: avaliação de nível, lacunas e prioridades.
   - Correção: feedback em texto, áudio transcrito ou produção do aluno.
   - Aquisição natural: dieta linguística de 45 minutos, Silent Period e repetição até 80% de compreensão.

3. Selecionar input i+1
   - O material deve ser compreensível com leve desafio.
   - Conteúdo nativo entra quando sustenta pronúncia, ritmo e uso real.
   - Conteúdo didático entra quando reduz atrito e explica padrões.
   - O plano deve evitar tanto gramática seca quanto imersão sem direção.

4. Aplicar aquisição natural quando o idioma for A0/A1 ou pre-A1 de leitura
   - Usar `natural-acquisition-framework.md`.
   - Priorizar compreensão antes da fala.
   - Dividir a prática em 3 pilares: simplificada, dia a dia e técnica personalizada.
   - Repetir material até 80% de compreensão.
   - Evitar legendas traduzidas no consumo principal.
   - Registrar progresso por compreensão, não por performance oral precoce.
   - Para grego moderno/Omega, texto original em grego pode acompanhar o audio como trilha de leitura, não como legenda traduzida.

5. Construir o ciclo de aprendizado
   - Exposição: ouvir, ler ou assistir com objetivo claro.
   - Noticing: identificar padrões, chunks, pronúncia, conectores e estruturas.
   - Recuperação ativa: responder sem olhar, resumir, traduzir reversamente, reler em chunks ou completar lacunas.
   - Produção: falar, escrever ou executar leitura ativa usando o material, conforme o objetivo e o nível.
   - Feedback: comparar com modelo, corrigir erro recorrente e registrar uma regra de uso.
   - Revisão espaçada: D+1, D+3 e D+7 para planos semanais.

6. Medir progresso
   - Métricas simples: minutos de input, frases produzidas, acertos, gravações, textos revisados ou termos retidos.
   - Métricas de qualidade: naturalidade, precisão, fluidez, compreensão e autonomia.
   - O estudante deve saber o que fazer na próxima sessão sem reinterpretar o plano.

## Heurísticas por Habilidade

- Listening: input curto, repetição seletiva, transcrição parcial e shadowing.
- Speaking: respostas guiadas, gravação curta, repetição de chunks e autocorreção.
- Reading: skimming, scanning, chunking visual, vocabulário em contexto e recontagem.
- Writing: modelos curtos, reescrita, conectores e feedback por erro recorrente.
- Pronunciation: pares mínimos, ritmo, entonação e comparação com fala nativa.
- Grammar: padrão em contexto antes do nome formal da regra.

## Integração com Hubs de Idioma

Antes de atuar sobre um hub, carregue `language-environments.md` e o `soul.md` local do ambiente. O core define o método comum; o soul local define as especificidades que não podem ser misturadas entre idiomas.

Quando o plano alimentar um hub React, a saída deve preservar blocos reutilizáveis:

- roadmap_items: etapas, status, objetivo e métrica.
- glossary_items: termo, tradução, contexto, exemplo e nota de uso.
- session_loop: duração, input, prática, produção e revisão.
- progress_log: data, foco, evidência e próximo ajuste.

## Separação de Responsabilidades

- `polyglot_tutor`: diagnóstico, método, curadoria, plano, revisão e contratos de output.
- `soul.md` local: identidade do ambiente, nível real, foco, restrições, agentes e especificidades do idioma.
- `learning-loop.md` local: estado adaptativo, métrica, próxima sessão e regra de avanço daquele idioma.
- Hub React: visualização, timer, glossário, roadmap e logs.
- Logs locais: histórico de sessões, manutenção e evolução.
