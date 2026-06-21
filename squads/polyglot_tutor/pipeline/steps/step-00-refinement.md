---
execution: inline
agent: athena-strategy
---
# Step 00: Refinement
Refina o input do usuário para garantir que está claro.

## Context Loading
- squads/polyglot_tutor/pipeline/data/learner-model.md
- squads/polyglot_tutor/pipeline/data/language-environments.md
- squads/polyglot_tutor/pipeline/data/language-specificity-framework.md
- squads/polyglot_tutor/pipeline/data/natural-acquisition-framework.md
- squads/polyglot_tutor/pipeline/data/session-routing.md
- squads/polyglot_tutor/pipeline/data/session-boot-checklist.md
- squads/polyglot_tutor/pipeline/data/domain-framework.md

## Instructions
### Process

1. Confirmar idioma-alvo e idioma de saída.
2. Identificar o ambiente correspondente, se existir no registro.
3. Carregar mentalmente o `soul.md` local quando o pedido mencionar um idioma/ambiente específico.
4. Carregar mentalmente o `learning-loop.md` local quando o pedido for uma sessão de estudo.
5. Identificar nível aproximado usando CEFR quando possível; para japonês, mapear também para JLPT/N5 quando útil; para grego, separar decodificação de alfabeto de leitura fluente.
6. Classificar o modo da rodada: diagnóstico, curadoria, plano, treino, correção ou sessão.
7. Para A0/A1 ou pre-A1 de leitura, considerar `aquisição natural` como modo padrão, salvo se o usuário pedir correção ou treino específico.
8. Se o input contiver apenas ambiente/idioma conhecido, tratar como `boot de sessão` e aplicar `session-boot-checklist.md`.
9. Definir objetivo treinável quando informado; se não informado, usar `padrão do loop` como hipótese.
10. Registrar tempo disponível por dia ou por semana; se não informado, usar default local e pedir confirmação no boot.
11. Identificar preferência de formato quando houver; se não houver, usar default local.
12. Traduzir objetivo amplo em um foco pesquisável e executável.
13. Explicitar lacunas que precisam de checkpoint antes da pesquisa; para boot, limitar lacunas ao checklist curto.
14. Respeitar os níveis declarados no registro: inglês C2, espanhol A1 falso-iniciante, italiano A0, francês A0, japonês A0/N5 e grego moderno A0+/pre-A1 de leitura.

## Output Format
```markdown
# Research Focus

- Idioma-alvo:
- Idioma de saída:
- Ambiente:
- Loop local:
- Nível:
- Evidência do nível:
- Modo de entrega:
- Método aplicado:
- Objetivo:
- Tempo disponível:
- Formatos preferidos:
- Restrições:
- Boot necessário:
- Checklist de boot:
- Foco de pesquisa:
- Lacunas para checkpoint:
```

## Output Example
```markdown
# Research Focus

- Idioma-alvo: Inglês
- Idioma de saída: Português (Brasil)
- Ambiente: I'd like some tea
- Loop local: ambientes/projetos/Id like some tea/_conclave/_memory/learning-loop.md
- Nível: C2/proficiente
- Evidência do nível: usuário relata proficiência avançada e quer refinar naturalidade
- Modo de entrega: plano
- Método aplicado: aquisição natural, se o idioma estiver em A0/A1 ou pre-A1 de leitura
- Objetivo: refinar listening, pronúncia e registro profissional
- Tempo disponível: 30 min/dia
- Formatos preferidos: YouTube e podcast curto
- Restrições: evitar aulas longas de gramática isolada
- Boot necessário: não
- Checklist de boot: já respondido pelo input
- Foco de pesquisa: materiais de input compreensível sobre carreira e tecnologia
- Lacunas para checkpoint: confirmar se aceita conteúdo com sotaque britânico
```

## Veto Conditions
1. Faltam informações básicas e não há ambiente conhecido suficiente para boot.
2. Input vazio.
3. Idioma-alvo indefinido.
4. Foco amplo demais para pesquisa útil.
5. Nível ignorado quando o usuário forneceu pistas.
6. Modo de entrega indefinido.
7. Ambiente conhecido ignorado quando o pedido menciona um hub existente.
8. Input curto com ambiente conhecido foi rejeitado em vez de virar boot guiado.

## Quality Criteria
- [ ] Claro
- [ ] Idioma, nível e objetivo aparecem.
- [ ] Ambiente/soul local aparece quando aplicável.
- [ ] O modo de entrega aparece.
- [ ] O foco pode ser usado diretamente pelo pesquisador.
- [ ] Restrições e preferências estão explícitas.
- [ ] Quando faltam parâmetros, há boot checklist em vez de rejeição.
- [ ] Lacunas reais foram separadas para o checkpoint.
- [ ] Não há promessa de fluência rápida.
