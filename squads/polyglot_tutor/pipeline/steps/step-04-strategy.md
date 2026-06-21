---
execution: inline
agent: athena-strategy
inputFile: squads/polyglot_tutor/output/research-results.md
outputFile: squads/polyglot_tutor/output/study-plan.md
---
# Step 04: Strategy

## Context Loading
- squads/polyglot_tutor/output/research-focus.md
- squads/polyglot_tutor/output/research-results.md
- squads/polyglot_tutor/pipeline/data/learner-model.md
- squads/polyglot_tutor/pipeline/data/language-environments.md
- squads/polyglot_tutor/pipeline/data/language-specificity-framework.md
- squads/polyglot_tutor/pipeline/data/natural-acquisition-framework.md
- squads/polyglot_tutor/pipeline/data/session-routing.md
- squads/polyglot_tutor/pipeline/data/session-boot-checklist.md
- squads/polyglot_tutor/pipeline/data/domain-framework.md
- squads/polyglot_tutor/pipeline/data/quality-criteria.md

## Instructions
### Process

1. Ler os materiais aprovados na pesquisa.
2. Identificar objetivo, nível, tempo disponível e formatos preferidos.
3. Se a rodada veio de boot, aplicar os defaults do ambiente e as respostas do checklist.
4. Aplicar as especificidades do idioma: som, escrita, gramática nuclear, transferência e pragmática.
5. Para A0/A1 ou pre-A1 de leitura, montar dieta linguística de 45 minutos com os 3 pilares.
6. Para A0/A1 ou pre-A1 de leitura, honrar Silent Period e medir compreensão antes de fala.
7. Para Omega/grego moderno, tratar fala como opcional/adiada e medir progresso por leitura, chunking visual, audio+texto e SRS.
8. Integrar links e materiais diretamente em blocos do plano.
9. Distribuir carga cognitiva em sessões viáveis.
10. Incluir revisão/repetição até 80% de compreensão.
11. Incluir ajuste de dificuldade: o que fazer se estiver fácil, difícil ou chato.
12. Definir métrica simples de acompanhamento.
13. Fechar com decisão de progressão: repetir, avançar, reduzir dificuldade ou intensificar.
14. Incluir proposta de atualização do `learning-loop.md` local.
15. Se a saída puder alimentar um hub de idioma, incluir blocos exportáveis no fim.

## Output Format
```markdown
# Roteiro de Estudo

## Objetivo

## Perfil do Aprendiz

## Materiais Usados

## Ciclo de Aprendizado

## Boot Aplicado

## Dieta Linguística

## Plano por Sessão

## Revisão Espaçada

## Regra de 80%

## Ajuste de Dificuldade

## Métrica de Progresso

## Decisão de Progressão

## Atualização Proposta do Learning Loop

## Blocos Exportáveis
```

## Output Example
```markdown
# Roteiro de Inglês C2

## Sessão 1 — Input Compreensível
- Material: vídeo principal da pesquisa.
- Duração: 20 min.
- Tarefa: extrair 10 frases e repetir em voz alta.

## Revisão Espaçada
- D+1: reouvir sem legenda.
- D+3: gravar resumo de 2 minutos.
- D+7: usar 5 frases em texto próprio.

## Ajuste de Dificuldade
- Fácil demais: regravar sem legenda e aumentar produção livre para 3 minutos.
- Difícil demais: reduzir para 5 frases e usar transcrição parcial.
```

## Veto Conditions
1. Fugiu do tema.
2. Não usou a pesquisa.
3. Plano impossível de cumprir no tempo informado.
4. Sem prática ativa.
5. Sem métrica de progresso.
6. Sem ajuste de dificuldade em planos de mais de um dia.
7. Rodada de boot ignorou os defaults locais.
8. Sessão não define repetir, avançar, reduzir ou intensificar.

## Quality Criteria
- [ ] Boa estrutura
- [ ] Usa materiais pesquisados.
- [ ] Carga horária é realista.
- [ ] Inclui input, prática ativa adequada ao nível e revisão.
- [ ] Cada sessão tem objetivo observável.
- [ ] Se houve boot, os defaults locais aparecem ou foram ajustados.
- [ ] Há decisão de progressão explícita.
- [ ] O plano pode ser executado sem nova interpretação.
- [ ] Blocos exportáveis aparecem quando há destino de hub/app.
