---
task: "Build Study Plan"
order: 1
input: |
  - research_data: Insumos brutos pesquisados
output: |
  - markdown_plan: O roteiro de estudos formatado
  - export_blocks: Blocos reutilizáveis para hubs, quando aplicável
  - loop_update: Proposta de atualização do learning-loop.md local
---

# Build Study Plan

Cria o relatório Markdown com métodos, ferramentas e rotina de estudo adaptada.

## Process
1. Lê o material aprovado na pesquisa.
2. Reconfere modo, objetivo, nível e tempo disponível.
3. Se a rodada veio de boot, aplica defaults locais e respostas do checklist.
4. Estrutura os dias/módulos do plano.
5. Para A0/A1 ou pre-A1 de leitura, aplica aquisição natural: Silent Period, 3 pilares, no-subtitles/no translated subtitles e 80%.
6. Inclui exposição, noticing, prática ativa, produção ou leitura ativa, feedback e revisão quando a produção for adequada ao nível.
7. Para Omega/grego moderno, prioriza leitura, chunking visual, audio+texto em grego, SRS e mitologia; fala fica opcional.
8. Define ajuste de dificuldade, métrica de progresso e decisão repetir/avançar/ajustar.
9. Propõe atualização do learning loop local.
10. Escreve o roteiro com tom didático e fluido.

## Output Format
```markdown
# Roteiro de Estudos: [Tópico]

## Perfil do Aprendiz

## Estratégia Geral
...

## Dieta Linguística

## Silent Period

## O Plano

### Sessão 1
- Input:
- Noticing:
- Prática ativa:
- Produção:
- Feedback:
- Métrica:

## Revisão Espaçada

## Regra de 80%

## Ajuste de Dificuldade

## Blocos Exportáveis

## Atualização Proposta do Learning Loop
```

## Output Example
> Use as quality reference, not as rigid template.

# Roteiro: Italiano para Viagem (Sobrevivência)

## Estratégia
Vamos focar no Input Compreensível usando o canal X. A ideia é treinar o ouvido primeiro.

## Passo a Passo
1. Assista ao vídeo Y prestando atenção nos gestos.
2. Anote as 5 expressões mais repetidas...

## Quality Criteria
- [ ] Uso correto de Markdown
- [ ] Didática mesclada (Rigor + Creator)
- [ ] Passo a passo executável
- [ ] Cada sessão tem resultado observável
- [ ] Há revisão e feedback
- [ ] Há ajuste de dificuldade
- [ ] Export blocks aparecem quando o destino for um hub
- [ ] Quando a rodada veio de boot, usa defaults locais
- [ ] Para A0/A1 ou pre-A1 de leitura, há dieta de 45 minutos em 3 pilares
- [ ] Para A0/A1 ou pre-A1 de leitura, fala não é forçada antes da compreensão
- [ ] Para Omega/grego moderno, a prática mede leitura/chunking e usa mitologia quando adequado
- [ ] Há proposta de atualização do learning loop local
- [ ] Há decisão de progressão: repetir, avançar, reduzir ou intensificar

## Veto Conditions
Reject and redo if ANY are true:
1. Faltam links para materiais práticos.
2. O plano é apenas um bloco de texto contínuo sem quebras.
3. O plano não tem prática ativa.
4. O plano não tem métrica de progresso.
5. O plano não cabe no tempo informado.
6. Para A0/A1 ou pre-A1 de leitura, o plano depende de legendas traduzidas no input principal.
7. Para A0/A1 ou pre-A1 de leitura, o plano avança antes de 80% de compreensão.
8. Sessão de estudo sem atualização proposta de learning loop.
9. Para Omega/grego moderno, o plano força fala ou ignora leitura em chunks.
10. Rodada de boot exige briefing completo em vez de usar checklist curto.
11. Sessão sem decisão de progressão.
