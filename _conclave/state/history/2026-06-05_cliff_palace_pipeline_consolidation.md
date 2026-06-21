# 📜 Consolidação de Pipeline Único e Refatoração Estrutural (Cliff Palace)

**Data:** 2026-06-05  
**Autor:** Antigravity (com aprovação do <user_name>)  
**Tópico:** Eliminação de redundâncias e bugs nos pipelines de dados financeiros.  

## 📍 Contexto e Motivação

O Cliff Palace operava com **3 pipelines concorrentes e conflitantes** para processamento de transações bancárias e de cartão de crédito:
1. **Pipeline A (ingest.rb / ingest.py):** Sobrescrita de históricos e uso de categorizações em hardcoded.
2. **Pipeline B (core/extract_pdf.py, core/normalize.py):** Bug falsy-zero e dedup inconsistente.
3. **Pipeline C (Knowledge Base):** Scripts em Python sob `squads/cliff_palace/knowledge_base-money/_scripts/` (o mais robusto e completo).

Isso causava atrito, redundâncias e dados desalinhados. <user_name> determinou a consolidação sob o **Pipeline C (Canônico)** e a eliminação dos pipelines legados.

## 🛠️ Decisões Arquiteturais e Implementação

1. **Pipeline Único Consolidado:**
   - Todos os scripts de `ambientes/cliff-palace/` (Pipelines A e B) foram depreciados e movidos para `ambientes/cliff-palace/_legacy/`.
   - Adicionada documentação de deprecação clara em `_DEPRECATED.md` nos diretórios do ambiente.
2. **Sanamento de Bugs no Pipeline C:**
   - Heurística de ano em `parse_fatura.py` ajustada (limiar de 60 para 31 dias) para categorizar corretamente transações de dezembro em faturas de janeiro do ano seguinte.
   - Corrigido bug de deduplicação por ID em `gerar_historicos.py` e `validate_pipeline.py`. Identificadores repetidos do Nubank (ex. crédito e débito no mesmo dia pelo mesmo estorno) não são mais descartados por engano. Agora a deduplicação usa a chave composta `(id, data, valor)`.
   - Corrigido typo `"tranferência"` no script de recomputação de derivados.
3. **Padrão de Sinal (Sign Convention):**
   - Entradas (recebimentos reais): Sempre **POSITIVO**.
   - Saídas (gastos, Pix enviados, tarifas): Sempre **NEGATIVO**.
   - Movimentações internas: Mantêm o sinal original.
   - O dashboard legado (`dados.json`) atua como camada de visualização aplicando `abs()` nas saídas para manter a retrocompatibilidade visual.
4. **Validação E2E Automatizada:**
   - Criado `validate_pipeline.py` para cruzar dados do YAML classificado com CSVs raw, conferir checksums centesimais mês a mês e garantir zero perdas de dados.
   - Roteado com sucesso o pipeline do zero: 101 meses auditados e 100% batendo.

## 📈 Impactos nos Agentes

- Todos os agentes (`albert-daily`, `marie-biweekly`, `galileu-monthly`, `tio-patinhas`, `<user_name>-ui` e `karen-translator`) foram atualizados para consumir explicitamente das fontes canônicas (`historico-extratos.yaml`, `historico-faturas.yaml`, `fluxo-mensal.yaml`, etc.) declaradas no `master-index.yaml`.
- Atualizado o `squads/cliff_palace/_memory/memories.md` para fixar as novas regras e proibir intervenções manuais.
