---
execution: inline
agent: deckard-publisher
inputFile: squads/sexy_content/output/draft-conteudo.md
outputFile: squads/sexy_content/output/publicacao.md
---

# Step 11: Publicar Conteúdo (Deckard Publisher)

## Context Loading

Load these files before executing:
- `squads/sexy_content/output/draft-conteudo.md` — conteúdo final aprovado
- `squads/sexy_content/output/carousel.html` — HTML do carrossel (se formato = carousel)
- `squads/sexy_content/output/formato-selecionado.md` — formato do conteúdo
- `squads/sexy_content/output/revisao.md` — veredicto da revisão (confirmar APROVADO antes de publicar)

## Instructions

### Process

1. Verificar que `revisao.md` contém veredicto APROVADO — nunca publicar com COM RESSALVAS ou REPROVADO.
2. Ler o formato selecionado e executar a seção correspondente.
3. Perguntar ao <user_name>: publicar imediatamente ou agendar?
4. Executar a publicação ou entrega conforme o formato.
5. Salvar log de publicação em `publicacao.md`.

**Para Posts de Texto:**

1. Formatar o texto final: remover markdown (`**`, `##`), ajustar quebras de linha para o ritmo do LinkedIn.
2. Confirmar horário de publicação com <user_name> (imediato ou agendar com data/hora).
3. Publicar via skill `blotato`.

**Para Carrosséis:**

1. Verificar que `output/carousel.html` existe e foi gerado pelo step-08.
2. Informar ao <user_name>: "O carrossel está em `output/carousel.html`. Abra no navegador para visualizar. Para publicar no LinkedIn, faça upload manual das imagens PNG."
3. Se a skill de screenshot estiver disponível, gerar PNGs automaticamente dos slides.
4. Registrar entrega no log.

**Para Artigos:**

1. Formatar com título, subtítulos e parágrafos no padrão do LinkedIn Articles.
2. Publicar via `blotato` ou fornecer texto formatado para publicação manual.

## Output Format

```markdown
# Log de Publicação

**Data/Hora:** [timestamp]
**Formato:** [Post / Carrossel / Artigo]
**Status:** [Publicado / Agendado para YYYY-MM-DD HH:MM / Pronto para upload manual]
**Link:** [URL do post se publicado, ou "N/A"]
**Arquivo:** [caminho do output gerado]

---

✅ Conteúdo processado com sucesso!
```

## Output Example

```markdown
# Log de Publicação

**Data/Hora:** 2026-04-20 14:32:00
**Formato:** Post
**Status:** Publicado
**Link:** https://linkedin.com/posts/dougpmoura_activity-123456789
**Arquivo:** squads/sexy_content/output/draft-conteudo.md

---

✅ Conteúdo processado com sucesso!

Formato: Post LinkedIn
Status: Publicado imediatamente via Blotato
Link: https://linkedin.com/posts/dougpmoura_activity-123456789
```

## Veto Conditions

Reject and redo if ANY are true:
1. O veredicto em `revisao.md` não é APROVADO — nunca publicar conteúdo não aprovado pela revisão.
2. Para carrossel: `output/carousel.html` não existe — não publicar sem o arquivo de design gerado.

## Quality Criteria

- [ ] Veredicto APROVADO confirmado antes de qualquer ação de publicação
- [ ] Formato do texto ajustado para LinkedIn (sem markdown residual em posts)
- [ ] Horário de publicação confirmado com <user_name> (imediato ou agendado)
- [ ] Log salvo em `publicacao.md` com timestamp, status e link
