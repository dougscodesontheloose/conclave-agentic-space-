---
task: "Revisão e Veredito de Carrossel Visual e Textual"
order: 1
input: |
  - assets_produzidos: Os arquivos textuais (legenda, e os copies ou outputs do subagent designado).
output: |
  - veredito_final: Um documento estruturado de APROVADO ou REJEITADO com lista de ações.
---

# Revisão e Veredito de Carrossel Visual e Textual

O estágio final que define se os slides produzidos atendem ao nível excepcional dos padrões MarTech de consumo digital, sem dumbing down nem fricção, antes de entregar aos checkpoiints manuais do humano.

## Process

1. Importar a estrutura final contendo a "copy" do slide principal e a legenda sugerida (`output/slide-copy.md` e `output/legenda.md`) ou caminhos/representações dos renders.
2. Avaliar cada Slide do documento contra a régua métrica do squad (Tamanho < 25-30 palavras nos corpos de corpo).
3. Avaliar se o Gancho (Hook) foi atrativo e a CTA foi única.
4. Produzir a conclusão de APROVAÇÃO, liberando o processo, ou indicar um comando `REJEITADO` que obrigue os agentes passados a consertar os blocos falhos sob suas notas.

## Output Format

```yaml
verdict:
  status: "APROVADO | REJEITADO"
  critical_issues:
    - "..."
    - "..."
  improvements_mandatory:
    - agent_target: "nome-do-agente-causador"
      task: "oque_refazer"
```

## Output Example

> Use as quality reference, not as rigid template.

```yaml
verdict:
  status: "REJEITADO"
  critical_issues:
    - "Slide 5 atingiu 42 palavras. Uma muralha de texto inescaneável em aparelhos mobile."
    - "Legenda não possui hashtags ou CTA para olhar as imagens."
  improvements_mandatory:
    - agent_target: "gibson-writer"
      task: "Quebrar o slide 5 em dois slides e otimizar texto da legenda adicionando call-to-scroll."
```

## Quality Criteria

- [ ] Foi entregue um log analítico. 
- [ ] Todos os desvios aos princípios estabelecidos na memória e anti-patterns foram pegos.
- [ ] O status reflete exatamente se cumpre o funil final de consumo do LinkedIn.

## Veto Conditions

Reject and redo if ANY are true:
1. O texto gerado como feedback for vago ou focado puramente em elogios desnecessários enquanto a contagem de métricas de legibilidade falha.
2. Feedback faltar uma diretriz de correção clara ("actionable advice").
