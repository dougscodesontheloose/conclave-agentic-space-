---
task: "Review Plan"
order: 1
input: |
  - study_plan: O roteiro gerado
output: |
  - verdict: APPROVE ou REJECT
  - feedback: Razões da rejeição ou elogios
---

# Review Plan

Passa um pente-fino no material, garantindo engajamento e eficácia estrutural.

## Process
1. Avalia o roteiro frente aos critérios de qualidade.
2. Checa o balanço do tom de voz.
3. Emite o veredito.

## Output Format
```yaml
verdict: APPROVE
feedback: |
  Pontos fortes: ...
  Melhorias: ...
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

## Veto Conditions
Reject and redo if ANY are true:
1. Feedback é vago (ex: "melhore a estrutura").
2. Veredito contradiz o feedback.
