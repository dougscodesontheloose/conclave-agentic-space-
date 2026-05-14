---
task: "Extrair Copy para Slides"
order: 1
input: |
  - texto_bruto: O conteúdo base que o usuário deseja transformar.
  - tom_voz: A preferência de tom da marca.
output: |
  - slides: Lista de slides com Título (opcional) e Parágrafo curto, formatada para design.
---

# Extrair Copy para Slides

Transformar o conteúdo denso recebido em uma estrutura linear e rápida de leitura, dividida perfeitamente em 5 a 10 slides estratégicos.

## Process

1. Identificar o núcleo do texto: Qual é a novidade, a tese provocativa ou o tutorial?
2. Resumir essa tese em um Gancho forte de até 8 a 15 palavras que ficará no Slide 1.
3. Quebrar as seções principais em 3 a 7 slides de desenvolvimento. Aplique formatação com quebras (bullet points, tópicos) de no máximo 20-25 palavras por slide.
4. Concluir com 1 slide de fechamento / resolução (Takeaway) e 1 de CTA claro (ex: Leia o guia completo no meu blog).

## Output Format

```yaml
slides:
  - id: 1
    type: "hook"
    text: "..."
  - id: 2
    type: "content"
    title: "..."
    text: "..."
  # ... continuar até CTAs
```

## Output Example

> Use as quality reference, not as rigid template.

```yaml
slides:
  - id: 1
    type: "hook"
    text: "O GA4 não quebrou sua mídia. Ele revelou que sua estratégia de jornada estava cega."
  - id: 2
    type: "content"
    title: "O Mito do Last Click"
    text: "Até 2023, o Google Analytics recompensava o último passo. Agora ele expõe que até o fechamento um lead passou por 7 touchpoints invisíveis."
  - id: 3
    type: "content"
    title: "O Padrão Oculto"
    text: "Métricas diárias mentem hoje. A modelagem DDA quer janelas de aprendizado de pelo menos 14 dias para atribuir crédito correto às campanhas de topo."
  - id: 4
    type: "cta"
    text: "Quer saber como adaptar seu dashboard no Looker? Mude as configurações descritas no link do post."
```

## Quality Criteria

- [ ] A contagem total de slides da lista é rigorosamente entre 5 e 10.
- [ ] Foram removidas frases de preenchimento (ex.: "Neste artigo vamos falar sobre...").
- [ ] Há limite extremo nas palavras por slide para garantir legibilidade máxima.

## Veto Conditions

Reject and redo if ANY are true:
1. Algum slide possui mais de 35 palavras.
2. A entrega foi apenas um resumo e não segue a delimitação isolada de slides numéricos.
