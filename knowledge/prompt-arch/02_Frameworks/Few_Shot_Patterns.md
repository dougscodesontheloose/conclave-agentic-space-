> Modelos Prompts Few Shots
> 
> 
> ### Modelo 1: Instrução + 2 a 3 exemplos + novo caso
> 
> ```
> Você é um(a) assistente que faz X. 
> 
> Exemplos:
> Entrada: "…"
> Saída: "…"
> 
> Entrada: "…"
> Saída: "…"
> 
> Agora faça no texto que vou te enviar.
> ```
> 
> ---
> 
> ### Modelo 2: Classificação (rótulos)
> 
> ```
> Classifique a entrada em apenas um rótulo: `A`, `B`, `C`. Responda só com o rótulo.
> 
> Exemplos:
> Entrada: "…"
> Rótulo: A
> 
> Entrada: "…"
> Rótulo: C
> 
> Agora faça no texto que vou te enviar.
> ```
> 
> ---
> 
> ### Modelo 3: Reescrita / normalização
> 
> ```
> Reescreva o texto para ficar mais claro, mantendo o sentido. Não invente informações.
> 
> Exemplos:
> Original: "…"
> Reescrito: "…"
> 
> Agora faça no texto que vou te enviar.
> ```
> 
> ---
> 
> ### Modelo 4: Resumo com estrutura fixa
> 
> ```
> Resuma seguindo exatamente este formato:
> - Resumo (1 frase)
> - Pontos-chave (3 bullets)
> - Próximos passos (2 bullets)
> 
> Agora faça no texto que vou te enviar.
> ```
> 
> ---
> 
> ### Modelo 5: Perguntas de esclarecimento (quando faltar contexto)
> 
> ```
> Se a solicitação estiver ambígua, faça até 3 perguntas objetivas antes de responder.
> 
> Exemplos:
> Pedido: "Me ajuda com isso"
> Perguntas:
> 
> 1. Qual é o objetivo final?
> 2. Para quem é a resposta?
> 3. Qual o prazo ou restrição?
> 
> Agora faça no texto que vou te enviar.
> ```
> 
