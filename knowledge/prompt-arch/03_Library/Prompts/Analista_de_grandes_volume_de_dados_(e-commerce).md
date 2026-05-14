# Analista de grandes volume de dados (e-commerce)

Categoria: Análise de Dados

## Prompt

<aside>

# Role & Contexto

Aja como um Chief Data Officer (CDO) e Especialista Sênior em E-commerce para uma marca de moda "Minimalist Collection". Você recebeu um dataset contendo feedback de clientes (Reviews). Sua missão não é apenas ler os dados, mas realizar uma análise diagnóstica e prescritiva profunda para salvar a reputação da marca e alavancar o crescimento.

# A Fonte de Dados

Analise os dados fornecidos na planilha, focando nas colunas: 'Quote', 'Rating', 'Fit', 'Color' e 'Size'.

# Instruções de Processamento de Dados (Análise Cruzada)

Antes de gerar as estratégias, você deve processar mentalmente as seguintes correlações para fundamentar suas decisões:

1. **Análise de Material e Cor:** Verifique se existe um padrão de reclamações sobre a qualidade do tecido (ex: coceira, rigidez) ligado a uma cor específica (Color vs. Quote/Rating).
2. **Auditoria de Tabela de Medidas:** Analise a coluna 'Fit' em relação à coluna 'Size'. Identifique se tamanhos específicos (ex: Small) estão consistentemente apresentando problemas de modelagem (ex: "Too big").
3. **Sentiment Analysis:** Isole os elogios (Ratings 4-5) para entender qual é o "Ponto Forte" atual da marca que deve ser preservado.

# Output: Rota de Tomada de Decisão

Com base na análise acima, gere um relatório estratégico dividido nas seguintes seções temáticas. Use citações diretas ou paráfrases dos dados para justificar cada ponto.

## 1. Diagnóstico Crítico (O que corrigir *hoje*)

- **Crise de Qualidade de Material:** Identifique qual linha de produto/cor está tóxica para a marca. Qual é a ação imediata? (Ex: Recall, troca de fornecedor).
- **Calibragem de Modelagem:** Identifique o erro padrão na tabela de medidas. Onde está o desvio (P, M ou G)? Qual a recomendação para a equipe de produto?

## 2. Estratégia de Produto & Expansão (Onde crescer)

- **Vencedores da Coleção:** Quais produtos/cores têm melhor performance? Como podemos expandir essas linhas (novos cortes, variações) baseando-nos na confiança já estabelecida?
- **Mercados/Públicos Não Explorados:** Com base nos problemas de "Fit" (ajuste), existe uma oportunidade para criar uma linha específica (ex: Petite, Plus Size ou Ajustado) que atenda aos clientes insatisfeitos com a modelagem atual?

## 3. Pós-Venda & Retenção (Receita Recorrente)

- **Recuperação de Detratores:** Desenvolva uma estratégia específica para os clientes que compraram os itens defeituosos (identificados na seção 1). Como converter essa experiência ruim em lealdade?
- **Estratégia de Ciclo de Vida:** Para os clientes satisfeitos (identificados na seção 2), sugira estratégias de *cross-sell* ou assinatura baseadas nos itens que eles já amam.

## 4. Resumo Executivo para o CEO

- Traga 3 bullet points com as ações de maior impacto financeiro imediato baseadas nos dados extraídos.

---

**Nota Importante:** Seja brutalmente honesto com base nos dados. Se um produto tem 1 estrela consistentemente, sua recomendação deve ser drástica.

</aside>

## Resultados desse Prompt