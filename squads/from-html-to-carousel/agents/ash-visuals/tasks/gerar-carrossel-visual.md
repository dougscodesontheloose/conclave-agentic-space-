---
task: "Gerar Carrossel Visual em Código e Assets"
order: 1
input: |
  - slide_copy: Estrutura final dos textos (yaml ou text/markdown) gerada no Passo 1/2.
  - identity: Parâmetros visuais ou css da marca (ex: Poética Racional) se houver em memory.
output: |
  - artifacts: HTMLs ou indicação de uso da ferramenta que monta os slides em PNG/PDF. Códio validado.
---

# Gerar Carrossel Visual em Código e Assets

Montar de maneira codificada e utilizar os plugins/skills disponíveis no seu sistema de agente (create-html-slides ou similar) para transformar o fluxo estático de palavras do `slide-copy.md` em uma experiência de design paginada visual que será compilada em PDF para o LinkedIn ou carrossel de Imagens no Instagram.

## Process

1. **Semantic Style Scouter:** Analisar o tom da copy recebida e cruzar com o "Dicionário de Estilos" (Seção 6 da Identidade Visual). Escolher o pacote visual (ex: Claudinho Vibes vs Minimalismo Industrial) que melhor ressoa com o conteúdo.
2. Analisar os slides recebidos, a quantidade e a categoria (Hooks vs Desenvolvimento vs CTA).
3. Definir o CSS de folha geral com base no pacote escolhido no passo 1. Use fontes profissionais e cores que respeitem a "vibe" selecionada.
3. Gerar a estrutura de cada "slide" de forma modular, mapeando cada campo `text` ou `title`.
4. Utilizar a habilidade associada de compilação gráfica ou a geração de HTML base e entregar.

## Output Format

```yaml
design_assets:
  tool_invoked: true
  platform: "linkedin/instagram"
  files_produced: "output/nome_final.pdf"
  status_html: |
    <!DOCTYPE html><html><body>... (código ou paths do resultado)
```

## Output Example

> Use as quality reference, not as rigid template.

```yaml
design_assets:
  tool_invoked: true
  platform: "linkedin"
  files_produced: "output/carrossel_ga4_final.pdf"
  status_html: "Foram gerados 7 slides HTML com a skill do Conclave. Estilos CSS baseados em Roboto, fundo #1A1A1A, acento #FF4B2B de gancho."
```

## Quality Criteria

- [ ] A ferramenta visual foi chamada via subagent com as skills liberadas, transformando `slide_copy.md`.
- [ ] O fluxo resultou em peças visualizáveis de hierarquia topograficamente aceitável para mídias atuais (alto contraste).
- [ ] Cada slide do código carrega sem erros com espaçamento/padding considerável e responsivo.

## Veto Conditions

Reject and redo if ANY are true:
1. O HTML/Design gerado quebra porque não há `font-size` adequado causando mistura textual.
2. Faltaram slides essenciais definidos pelo redator.
