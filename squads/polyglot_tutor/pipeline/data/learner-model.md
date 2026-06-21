# Learner Model

Use este modelo como memória operacional durante cada execução. Ele não substitui a preferência global do usuário; ele traduz o pedido da rodada em decisões pedagógicas.

## Snapshot do Aprendiz

```yaml
learner:
  target_language: ""
  output_language: "Português (Brasil)"
  cefr_level: ""
  evidence_for_level:
    - ""
  current_goal: ""
  time_budget: ""
  preferred_formats:
    - ""
  constraints:
    - ""
  motivation_context: ""
```

## Diagnóstico Rápido

- Se o nível for desconhecido, não invente CEFR. Use "nível estimado: indefinido" e peça uma evidência mínima no checkpoint.
- Se o usuário der pistas ("consigo ler, mas travo falando"), traduza isso em habilidade prioritária.
- Se o objetivo for amplo ("ficar fluente"), reduza para uma habilidade treinável na rodada.
- Se o tempo disponível for alto demais, reduza para uma rotina sustentável e explique o trade-off.
- Se o usuário quiser só pesquisa, não force roteiro completo; entregue curadoria com sequência de consumo.

## Modos de Entrega

| Modo | Quando usar | Saída principal |
|---|---|---|
| Diagnóstico | Nível, lacunas ou objetivo incertos | mapa de nível, lacunas e próxima hipótese |
| Curadoria | Usuário precisa de fontes | materiais principais, complementares e sequência |
| Plano | Usuário quer rotina | roteiro por sessão com revisão espaçada |
| Treino | Usuário quer praticar agora | exercícios, respostas esperadas e feedback |
| Correção | Usuário traz produção própria | erros recorrentes, reescrita e microtreino |
| Aquisição natural | Idioma A0/A1, pre-A1 de leitura ou contato inicial | dieta de 45 minutos, Silent Period e regra de 80% |

## Ajuste de Dificuldade

- Muito fácil: aumentar naturalidade, velocidade, produção livre ou vocabulário específico.
- Muito difícil: reduzir duração, aumentar apoio visual, limitar vocabulário novo ou trocar para input didático; legenda/transcrição só como tarefa separada, não como muleta do input principal.
- Muito chato: trocar tema, encurtar blocos e aumentar produção com contexto pessoal/profissional.
- Muito teórico: começar com exemplo real e nomear a regra apenas depois.

## Perfil Ativo Conhecido

Use `language-environments.md` como fonte de verdade para ambiente, nível e foco por idioma. O estado conhecido nesta data:

- Ingles: C2/proficiente; foco em vocabulário, fluência, pronúncia, gramática fina, dialeto US/UK e retórica profissional.
- Espanhol: A1 falso-iniciante; não é zero absoluto, mas precisa consolidar fundações antes de perseguir B1/B2.
- Italiano: A0; começar do zero com ponte português -> italiano e fonética desde o primeiro dia.
- Francês: A0; começar do zero com foco especial em escrita-som, vogais nasais, `u`, `r`, liaison e cortesia básica.
- Japonês: A0/N5 inicial; kana primeiro, partículas básicas e eliminação gradual de romaji.
- Grego moderno: A0+/pre-A1 de leitura; alfabeto e fonologia basica ja foram parcialmente dominados, mas a leitura ainda esta em modo de decifracao e precisa migrar para chunking.

Não aplique automaticamente o roadmap de um idioma em outro. A transferência entre línguas deve ser explícita: cognatos ajudam em espanhol/italiano/francês, mas podem atrapalhar por falsos amigos e pronúncia enganosa; japonês exige um trilho separado de escrita e partículas; grego moderno permite ancoras culturais e etimologicas, mas elas nao substituem vocabulario funcional de alta frequencia.

## Método Padrão para Baixa Proficiência

Para espanhol A1, italiano A0, francês A0, japonês A0/N5 e grego moderno A0+/pre-A1, aplicar por padrão o Natural Acquisition Framework:

- 45 minutos por dia;
- 7 dias por semana;
- 15 minutos por pilar: linguagem simplificada, linguagem cotidiana, linguagem técnica personalizada;
- sem legendas no consumo principal;
- repetir até 80% de compreensão;
- honrar o Silent Period;
- só introduzir fala como microprodução depois de compreensão estável.

No Omega, adaptar a producao: fala nao e objetivo inicial; medir progresso por leitura, reconhecimento de chunks, sincronizacao audio+texto em grego e compreensao sem soletrar mentalmente.
