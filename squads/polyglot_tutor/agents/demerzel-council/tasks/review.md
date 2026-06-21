---
task: "Review Plan"
order: 1
input: |
  - study_plan: O roteiro gerado
output: |
  - verdict: APPROVE ou REJECT
  - scores: Pontuações por critério
  - feedback: Razões da rejeição ou riscos residuais
---

# Review Plan

Passa um pente-fino no material, garantindo engajamento e eficácia estrutural.

## Process
1. Avalia o roteiro frente aos critérios de qualidade.
2. Checa o balanço do tom de voz.
3. Verifica se a pesquisa foi usada dentro das sessões.
4. Para A0/A1 ou pre-A1 de leitura, verifica Silent Period, 3 pilares, no-subtitles/no translated subtitles e 80%.
5. Para Omega/grego moderno, verifica leitura, chunking visual, audio+texto em grego, SRS e ausencia de fala forçada.
6. Verifica se existe proposta de atualização do learning loop local.
7. Se a rodada veio de boot, verifica se defaults locais foram usados.
8. Verifica se existe feedback, revisão, métrica e decisão de progressão.
9. Emite o veredito.

## Output Format
```yaml
verdict: APPROVE|REJECT
scores:
  viability: 0
  engagement: 0
  rigor: 0
  source_use: 0
  feedback_loop: 0
  acquisition_fit: 0
critical_issues:
  - ""
required_fix: ""
residual_risks:
  - ""
next_review_trigger: ""
```

## Output Example
> Use as quality reference, not as rigid template.

```yaml
verdict: REJECT
feedback: |
  O plano está muito teórico. Falta aplicar os vídeos do YouTube pesquisados. 
  Por favor, reescreva o Passo 2 incluindo prática passiva.
```

## Quality Criteria
- [ ] Veredito claro
- [ ] Feedback acionável
- [ ] Avaliação do tom
- [ ] Critérios avaliados separadamente
- [ ] Blocos problemáticos nomeados
- [ ] Próxima ação está clara
- [ ] Feedback loop é avaliado
- [ ] Riscos residuais aparecem quando aprovado
- [ ] Aquisição natural é avaliada quando o idioma for A0/A1 ou pre-A1 de leitura
- [ ] Para Omega/grego moderno, leitura e chunking são avaliados como eixo principal
- [ ] Learning loop local é avaliado quando for sessão de estudo
- [ ] Boot guiado é avaliado quando o input foi curto
- [ ] Decisão de progressão aparece quando for sessão

## Veto Conditions
Reject and redo if ANY are true:
1. Feedback é vago (ex: "melhore a estrutura").
2. Veredito contradiz o feedback.
3. Plano aprovado sem uso dos materiais pesquisados.
4. Plano rejeitado sem indicar o menor ajuste necessário.
5. Plano aprovado sem primeiro passo executável.
6. Plano aprovado sem gatilho de revisão.
7. Plano A0/A1 ou pre-A1 aprovado sem Silent Period, 3 pilares ou regra de 80%.
8. Sessão aprovada sem proposta de atualização do learning loop.
9. Plano Omega aprovado forçando fala ou trocando grego moderno por grego antigo sem pedido explícito.
10. Boot aprovado exigindo briefing completo do usuário.
11. Sessão aprovada sem decisão de progressão.
