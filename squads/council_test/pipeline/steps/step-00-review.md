---
title: Revisão de Excelência
agent: quorra_oracle
---

# step-01-review.md

## Context Loading

Load recent posts from `output/` and any review brief supplied by the user.
If multiple drafts exist, evaluate the most recent artifact first and reference older versions only for comparison.

## Instructions

Execute a revisão usando o protocolo de 3 personas.

### Process

1. Ler o conteúdo integralmente sem comentar.
2. Fazer a primeira avaliação como `Skeptic`, procurando risco, fragilidade lógica, promessa vaga e ausência de prova.
3. Fazer a segunda avaliação como `Visionary`, procurando potencial estratégico, expansão criativa e oportunidades de posicionamento.
4. Fazer a terceira avaliação como `Judge`, comparando risco e oportunidade.
5. Atribuir nota de 0 a 10 para clareza, impacto, risco e potencial.
6. Emitir veredito `APPROVE`, `REVISE` ou `REJECT`.
7. Encerrar com o menor conjunto de mudanças necessárias para elevar o conteúdo.

## Output Format

```markdown
# Relatório do Conselho

## PARECER DO CÉTICO
- Risco principal:
- Evidência:
- Correção necessária:

## PARECER DO VISIONÁRIO
- Oportunidade:
- Ampliação possível:
- Ganho esperado:

## VEREDITO DO JUIZ
- Status:
- Nota:
- Confiança:
- Decisão:

## Matriz de Veredito
| Critério | Nota | Motivo | Ação |
|---|---:|---|---|
```

## Veto Conditions

1. Missing any persona viewpoint.
2. Veredito sem status objetivo.
3. Crítica sem ação corretiva.
4. Nota final incompatível com os riscos apontados.
5. Parecer visionário com elogio genérico e sem melhoria concreta.

## Quality Criteria

- [ ] Três personas aparecem claramente.
- [ ] Cada crítica cita risco específico.
- [ ] Cada oportunidade inclui ação concreta.
- [ ] Veredito tem nota e confiança.
- [ ] Há matriz de decisão.
- [ ] O relatório preserva a intenção central quando ela é defensável.

## Output Example

```markdown
## PARECER DO CÉTICO
- Risco principal: a promessa inicial é ampla demais.
- Evidência: o texto fala em "transformar resultados" sem métrica.
- Correção necessária: inserir um indicador ou exemplo verificável.

## PARECER DO VISIONÁRIO
- Oportunidade: o ângulo pode virar uma tese de autoridade.
- Ampliação possível: conectar o insight a uma experiência real.
- Ganho esperado: mais credibilidade e menos abstração.

## VEREDITO DO JUIZ
- Status: REVISE
- Nota: 7/10
- Confiança: média
- Decisão: revisar abertura e prova antes de publicar.
```
