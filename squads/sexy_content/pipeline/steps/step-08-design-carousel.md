---
execution: inline
agent: flynn-design
inputFile: squads/sexy_content/output/draft-conteudo.md
outputFile: squads/sexy_content/output/carousel.html
skip_if: "format != carousel"
---

# Step 08: Design do Carrossel (Flynn Design)

## Context Loading

Load these files before executing:
- `squads/sexy_content/output/draft-conteudo.md` — roteiro textual aprovado dos slides
- `pipeline/data/visual-identity.md` — pacotes visuais e diretrizes de design
- `pipeline/data/color-palettes.md` — paletas de cores disponíveis para cruzamento
- `squads/sexy_content/_memory/douglas-visual-voice.md` — identidade visual detalhada do Doug
- `squads/sexy_content/_memory/douglas-color-palettes.md` — paletas estendidas com contexto de uso

**Condição de ativação:** Este step é executado APENAS quando `formato-selecionado.md` contém `format = carousel`. Para posts e artigos, pular diretamente para step-09.

## Instructions

### Process

1. **Carregar referências visuais**: Ler todos os arquivos de Context Loading antes de qualquer decisão de design.
2. **Analisar o roteiro**: Identificar o tema central, a tensão principal e a emoção dominante do conteúdo.
3. **Selecionar pacote visual**: Cruzar o tema com a tabela de pacotes em `visual-identity.md`. Justificar a escolha em 1 linha antes de continuar.
4. **Selecionar paleta de cores**: Escolher de `color-palettes.md` — preferencialmente a paleta *não-óbvia* para o pacote. Justificar o cruzamento em 1 linha.
5. **Planejar hierarquia**: Para cada slide, definir quais elementos dominam (headline, dado, espaço negativo) antes de gerar código.
6. **Renderizar via `create-html-carousel`**: Gerar HTML com 1080×1080px por slide, tipografia com personalidade, paleta aplicada, metadados visíveis em monoespaçado.
7. **Auto-revisão**: Verificar cada slide contra os Veto Conditions antes de entregar o output.

### Decision Criteria

- Tema dados/métricas → Telemetria & Cockpit; IA/tech → Transparência Anatômica; carreira/estratégia → Arquitetura da Tensão; reflexão/humanidade → Soft Minimal Anthropic; tendências/mercado → Brutalista Tecnológico.
- Quando a paleta óbvia for "Cockpit para Telemetria": cruzar com Oceânica ou Red Energy.
- Quando o slide de capa não tiver impacto visual imediato no rascunho mental → reescrever o headline antes de renderizar.

## Output Format

```
Flynn Design — Decisões de Design:
— Pacote Visual: [nome] — [justificativa em 1 linha]
— Paleta: [nome] ([hex principal]) — [justificativa do cruzamento em 1 linha]
— Tipografia: [display font] + [mono font]

Slides gerados (N):
[NN] — [headline do slide] ([descrição do elemento visual dominante])
...

Output: squads/sexy_content/output/carousel.html ([N] slides, 1080×1080px)
```

## Output Example

```
Flynn Design — Decisões de Design:
— Pacote Visual: Transparência Anatômica — tema de IA como mecanismo interno, blueprint como metáfora visual
— Paleta: Cockpit Dark (#0A0A12 + #00D4FF) — cruzamento não-óbvio: frieza clínica do cockpit amplifica o caráter mecânico da Transparência
— Tipografia: Cabinet Grotesk Bold (display) + Space Mono (metadados)

Slides gerados (8):
01 — "A IA não pensa. Ela calcula." (blueprint de circuito como background translúcido, texto central peso máximo)
02 — "87% dos profissionais que 'usam IA' nunca modificaram um prompt." (dado em Space Mono grande, contexto em peso regular)
03 — "Prompt engineering não é skill de dev. É alfabetização do século XXI." (espaço negativo massivo, texto centrado)
04 — "Você não precisa saber Python. Precisa saber perguntar." (assimetria funcional: texto à esquerda, espaço vazio à direita)
05 — "A diferença entre o que a IA entrega e o que você precisa é o prompt." (linha de grade sutil como elemento decorativo)
06 — "Descreva seu trabalho para a IA em 3 linhas. Se ela não entendeu, o problema é sua clareza." (fundo mais escuro para criar tensão)
07 — "Quem domina o contexto, domina o output." (slide de transição — tipografia em peso extralight)
08 — CTA: "Qual prompt você já quis que alguém te ensinasse?" + @dougpmoura (metadado 08/08 em destaque)

Output: squads/sexy_content/output/carousel.html (8 slides, 1080×1080px)
```

## Veto Conditions

Reject and redo if ANY are true:
1. Qualquer slide parece template da Canva — design genérico sem decisão autoral visível.
2. A tipografia usa Inter, Roboto ou Arial — fontes sem personalidade são automaticamente rejeitadas.
3. O slide de capa não tem impacto visual imediato sem contexto dos outros slides.
4. As cores usadas não correspondem à paleta selecionada e justificada.

## Quality Criteria

- [ ] Pacote visual escolhido e justificado antes da renderização
- [ ] Paleta escolhida com cruzamento não-óbvio justificado
- [ ] Nenhum slide ultrapassa 40 palavras
- [ ] Metadados visíveis em monoespaçado em todos os slides (ex: "03 / 08")
- [ ] Tipografia com personalidade: Cabinet Grotesk / Clash Display / Space Mono / JetBrains Mono
- [ ] Slide de capa funciona como ativo independente — para o scroll sem contexto
- [ ] HTML gerado em `output/carousel.html` com dimensões 1080×1080px
