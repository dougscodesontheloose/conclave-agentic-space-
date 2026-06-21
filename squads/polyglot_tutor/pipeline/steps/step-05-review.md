---
execution: inline
agent: demerzel-council
inputFile: squads/polyglot_tutor/output/study-plan.md
on_reject: 4
---
# Step 05: Review

## Context Loading
- squads/polyglot_tutor/output/study-plan.md
- squads/polyglot_tutor/output/research-focus.md
- squads/polyglot_tutor/output/research-results.md
- squads/polyglot_tutor/pipeline/data/quality-criteria.md
- squads/polyglot_tutor/pipeline/data/natural-acquisition-framework.md
- squads/polyglot_tutor/pipeline/data/session-boot-checklist.md

## Instructions
### Process

1. Ler o plano de estudo inteiro.
2. Avaliar viabilidade, engajamento, rigor, uso das fontes e clareza.
3. Checar se o plano respeita o ambiente e o soul local quando aplicável.
4. Para A0/A1 ou pre-A1 de leitura, checar Silent Period, 3 pilares, no-subtitles/no translated subtitles e regra de 80%.
5. Para Omega/grego moderno, checar se fala nao foi forçada e se a métrica mede leitura, chunking visual, audio+texto em grego e SRS.
6. Checar se há input, prática ativa adequada, revisão e métrica de progresso.
7. Checar se há proposta de atualização do `learning-loop.md` local quando a entrega for sessão de estudo.
8. Se a rodada veio de boot, checar se o plano respeita defaults locais e nao exige memoria extra do usuario.
9. Checar se ha decisao de progressao: repetir, avancar, reduzir dificuldade ou intensificar.
10. Identificar blocos problemáticos pelo nome.
11. Emitir veredito `APPROVE` ou `REJECT`.
12. Se rejeitar, indicar o menor ajuste necessário para aprovação.
13. Se aprovar, registrar riscos residuais, recomendação de execução e critério de próxima revisão.

## Output Format
```yaml
verdict: APPROVE|REJECT
scores:
  viability: 0
  engagement: 0
  rigor: 0
  source_use: 0
  feedback_loop: 0
  environment_fit: 0
  acquisition_fit: 0
critical_issues:
  - ""
required_fix: ""
residual_risks:
  - ""
next_review_trigger: ""
```

## Output Example
```yaml
verdict: REJECT
scores:
  viability: 6
  engagement: 8
  rigor: 7
  source_use: 4
  feedback_loop: 6
  environment_fit: 5
  acquisition_fit: 4
critical_issues:
  - "O plano cita materiais pesquisados, mas não os integra nas sessões."
required_fix: "Adicionar links específicos em cada bloco de prática."
residual_risks: []
next_review_trigger: "Revisar após a primeira gravação ou texto produzido."
```

## Veto Conditions
1. Feedback vago.
2. Contradição.
3. Veredito sem pontuação.
4. Aprovação sem avaliar uso das fontes.
5. Rejeição sem correção mínima.
6. Aprovação de plano sem mecanismo de feedback.
7. Aprovação de plano que contradiz o soul local.
8. Aprovação de plano A0/A1 ou pre-A1 que força fala antes de compreensão.
9. Aprovação de plano A0/A1 ou pre-A1 que depende de legenda traduzida no input principal.
10. Aprovação de sessão sem proposta de atualização do learning loop.
11. Aprovação de plano Omega que troca leitura de grego moderno por grego antigo ou por historias infantis genericas sem justificativa.
12. Aprovação de boot que exige o usuário lembrar parâmetros que o checklist deveria perguntar.
13. Aprovação de sessão sem decisão de progressão.

## Quality Criteria
- [ ] Rigorosa
- [ ] Veredito claro.
- [ ] Pontuação por critério.
- [ ] Feedback acionável.
- [ ] Riscos residuais aparecem quando aprovado.
- [ ] Próximo gatilho de revisão está explícito.
- [ ] Aderência ao ambiente foi avaliada.
- [ ] Aderência ao Natural Acquisition Framework foi avaliada quando aplicável.
- [ ] Para Omega/grego moderno, leitura e chunking foram avaliados como métricas principais.
- [ ] Atualização de learning loop foi avaliada quando aplicável.
- [ ] Boot de sessão foi avaliado quando aplicável.
- [ ] Decisão de progressão foi avaliada.
