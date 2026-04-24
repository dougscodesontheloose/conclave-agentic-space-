---
execution: inline
agent: gibson-writer
format: linkedin-publication
inputFiles:
  - squads/from-html-to-carousel/output/slide-copy.yaml
  - squads/from-html-to-carousel/output/legenda.md
outputFile: squads/from-html-to-carousel/output/legenda-publicacao.md
---

# Step 07: Legenda de Publicação Final

Este step é executado **após a aprovação do design final** no checkpoint visual (Step 06).
Ele produz a versão de legenda otimizada para publicação imediata no LinkedIn — rápida, com ritmo, e com CTA empolgante.

## Context Loading

Carregue antes de executar:
- `squads/from-html-to-carousel/output/slide-copy.yaml` — A estrutura final dos slides aprovados.
- `squads/from-html-to-carousel/output/legenda.md` — A legenda analítica gerada no Step 02 (use como referência de conteúdo, não de tom).

## Instructions

### Objetivo
Reescrever a legenda do Step 02 na versão de publicação: curta, divertida, com ritmo de feed e CTA de alta energia. Não é um resumo do carrossel — é um **convite irresistível** para arrastar.

### Princípios obrigatórios (LinkedIn Publication Voice)
1. **Linha 1 = gancho de parada de rolagem.** Frase curta. Sem rodeios. Deve funcionar sozinha, isolada do resto.
2. **Corpo = 2–3 frases curtas, no máximo.** Cada uma em seu próprio parágrafo. Ritmo de leitura rápida.
3. **CTA = ação única, clara, com energia.** Nada de múltiplos pedidos (curtir + compartilhar + comentar).
4. **Pergunta de engajamento = opcional, mas bem-vinda.** Uma pergunta simples que convida comentário real.
5. **Hashtags = 3 a 4, no máximo.** Só as de máxima relevância temática.

### Tom
- Direto, com leveza. Não é um relatório — é uma conversa.
- Pode usar ":/" ou emojis funcionais com moderação — quando reforçam o ponto, não para decorar.
- Imperativo no CTA: "Arraste", "Leia", "Descubra" — verbos que movem.

## Veto Conditions
1. A legenda tem mais de 6 linhas visíveis antes do "ver mais" do LinkedIn.
2. O primeiro parágrafo começa com "Neste carrossel...", "Hoje vamos falar sobre..." ou similares — proibido.
3. Existe mais de 1 CTA explícito.
4. Tom é de relatório, não de conversa.

## Output Format

```markdown
**[Legenda — Publicação]**

[Linha de gancho — uma frase, punch total]

[Frase 2 — contexto rápido ou tensão]

[Frase 3 — o que o carrossel resolve ou revela]

[CTA — imperativo, uma ação apenas]

[Pergunta de engajamento — opcional]

[#Hashtag1 #Hashtag2 #Hashtag3]
```

## Output Example

```markdown
**[Legenda — Publicação]**

Quando a IA concorda com você, ela não está certa.

Ela desistiu. :/

Esse padrão contamina toda a operação — de um agente simples a pipelines rodando no background.

Arraste o carrossel → entenda como quebrar o ciclo antes que o erro escale.

💬 Você já percebeu isso acontecendo? Conta aqui embaixo.

#PromptEngineering #InteligenciaArtificial #AIAgents #Analytics
```

## Quality Criteria

- [ ] A legenda pode ser lida em menos de 10 segundos.
- [ ] O gancho funciona sozinho, sem o resto do texto.
- [ ] Existe exatamente 1 CTA claro.
- [ ] O tom é de conversa — não de white paper.
