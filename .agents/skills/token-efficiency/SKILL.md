---
name: Token Efficiency & Context Management
description: Faz a IA gastar menos tokens, responder mais rápido e evitar limites de contexto, utilizando diffs e logs terciários.
type: core_protocol
---

# Skill: Token Efficiency & Context Management

Esta skill introduz um protocolo estrito para evitar desperdício de tokens, prevenir a exaustão da janela de contexto ("amnésia") e acelerar as respostas durante as execuções do pipeline do Conclave.

## O Protocolo de Compressão

1. **Uso Exclusivo de Diffs:** 
   Nunca reescreva ou imprima no console um arquivo inteiro (salvo se for a criação inicial do arquivo). Ao fazer edições ou sugerir código, utilize sempre o formato de Diffs ou indique as linhas que serão modificadas.
2. **Truncamento Inteligente de Logs:**
   Se uma ferramenta (como scraper ou compilador) retornar centenas de linhas de log, não as repasse para o prompt. Filtre apenas o resumo do sucesso, do erro ou as métricas essenciais.
3. **Resumo Periódico de Contexto:**
   Ao realizar uma cadeia de várias operações complexas, antes que o contexto se torne longo demais, faça um "Resumo Executivo" do que já foi alcançado e descarte os logs intermediários.

## Sistema de Logs Terciário (Mitigação de Amnésia)

A compressão excessiva pode gerar amnésia de curto prazo. Para evitar a perda permanente de nuances contextuais que já foram processadas:

- Quando você for "limpar" o contexto da sua memória operacional ou condensar logs pesados, extraia os aprendizados e chaves essenciais e os salve no **Sistema de Logs Terciário**.
- **Caminho:** Salve esses resumos sucintos na pasta `_conclave/_memory/tertiary-logs/`.
- **Formato:** Crie arquivos `.md` com timestamp e contexto (ex: `2026-04-22-scraping-insights.md`).
- Se precisar recuperar detalhes passados que foram comprimidos, consulte esse diretório.

## Heurística de Resposta

- Seja conciso.
- Responda apenas o que foi solicitado.
- Evite monólogos confirmatórios longos ("Entendi, agora vou fazer X, Y e Z..."). Aja e retorne o status.
