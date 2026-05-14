# Diretrizes de Identidade Visual: O Design da "Poética Racional"

**Baseado na análise do repositório `/ref_visual_style/`**
**Data de Extração:** Abril de 2026

---

## 1. A Filosofia Visual (A Vibe)

As imagens de referência (mixando Teenage Engineering, Nothing Phone, posters da NASA e a arquitetura orgânica de Oscar Niemeyer e Atelier Pierre Thibault) revelam uma estética que cruza o **Industrialismo Tecnológico** com o **Modernismo Orgânico**.

A identidade de design não é puramente "tech fria", mas sim uma **engenharia com alma** — onde os "mecanismos internos" (transparências, grids, tipografia mono) convivem com formas naturais elegantes, luz volumétrica e respiro.

**Palavras-chave:**
Minimalismo Industrial, Brutalismo Orgânico, Transparency (Vidro/Translúcido), Alta Engenharia, Contraste Extremo, Luz Natural.

---

## 2. Padrões Estruturais & Layout (Grid e Respiro)

- **Espaço Negativo Massivo:** O "vazio" não é falta de conteúdo, é a moldura funcional. Elementos principais ocupam fatias muito definidas, deixando vastas áreas em branco, preto-profundo ou texturas naturais.
- **Grids e Metadados Visíveis:** Inspirado no design da *Nothing* e de "blueprints" (plantas baixas). Gosto de exibir "falsos metadados" (linhas de grade sutis, marcações ao lado das imagens, códigos de barras falsos, assinaturas de arquivo tipo "01/06").
- **Assimetria Funcional:** O texto muitas vezes fica alinhado à esquerda no topo ou na base, ancorando composições pesadas em um dos lados (como a engrenagem preta cortada na imagem da vaga de engenheiro).
- **Integração Orgânico-Mecânico:** Estruturas rígidas (réguas, caixas, textos técnicos) interagem com formas fluídas (como a curva da Terra no espaço da NASA ou as curvas de concreto em Niemeyer).

---

## 3. A Paleta de Cores (O Contraste)

O esquema de cores é contido, operando na regra 80/15/5 (Base/Contraste/Acento):

- **[Base 1] Black / Charcoal Void:** Preto profundo sem reflexo (`#0A0A0A` a `#121212`) para criar profundeza espacial ou elegância noturna.
- **[Base 2] Engineering White / Silver:** Branco puro, cinza prata ou placa translúcida (`#F5F5F5` a `#E0E0E0`).
- **[Elemento Orgânico] Wood & Nature:** Tons quentes da fotografia de arquitetura (marrom envelhecido, verde musgo, pedra) que quebram o visual "computadorizado". (Idealmente representados através de ruído/textura fotográfica ou uso do modo Glassmorphism por cima de imagens naturais).
- **[Acento Técnico] Neon Orange ou Mint Green:** Uma única cor muito vibrante (`#FF6B00` ou `#00FF88`) usada como apontador a laser — apenas para 1% da composição (ex: grifar uma palavra, um underline, um asterisco).

---

## 4. Tipografia (A Voz Gráfica)

A tipografia espelha a dualidade:

- **Display (Títulos e Oganização):** Sans-serif neo-grotesca, forte, fria e objetiva (ex: *Inter*, *Helvetica Neue*, *Space Grotesk*, *Cabinet Grotesk*). Usadas frequentemente no estilo "Swiss Design" (peso sólido, sem firulas).
- **Detalhes e Acabamentos (Metadados):** Fontes Monoespaçadas (ex: *JetBrains Mono*, *SF Mono*, *Space Mono*). Essa tipografia é usada para dar aquele ar de "máquina escrevendo" (fichas técnicas, números de versão, citações).
- *(Opcional, porém forte no "Lirismo")* **Serifa Clássica/Moderna:** Uma fonte serifada de alto contraste (*Lora*, *Playfair*) ocasionalmente inserida para citações profundas, fazendo um paradoxo proposital com o grid tecnológico de fundo.

---

## 5. Elementos de Assinatura (Tokens de Design a Implementar)

Para os próximos carrosséis, implementaremos:

1. **Fundo Base:** Ou um preto absoluto com textura granulada (ruído ISO fotográfico) ou um branco com grid técnico hiper-fino (linhas cinzas clarinhas).
2. **Cards / Containers:** Uso de *Glassmorphism* (blur) misturado ao brutalismo (bordas finas e duras, sem shadows super suaves ou redondas demais). Mais parecido com uma placa de acrílico ou vidro.
3. **Typography "Code & Poetry":** Títulos com a precisão suíça sans-serif versus metadados em Monoespaçado puro. Um toque de laranja (ou verde-menta) para destaque.
4. **Alinhamento:** Ancoragens assimétricas. O título começa brutalmente alinhado na esquerda ou direita, contrastando com áreas em branco absurdas.

---
**Status da Implementação:** Pronta para ser vetorizada no `carousel_html_renderer` como a estética definitiva ou para ser referenciada pelo `create-html-carousel`.

---

## 6. Dicionário de Estilos e Match Visual-Conteúdo

Para orquestrar a produção de imagens nos pipelines do Conclave, cada Padrão Visual Listado abaixo atua como um gatilho. Antes de gerar qualquer arte, o Ash Visuals executará o **Semantic Style Scouter**: uma varredura cruzando o texto do conteúdo gerado com a "Nuvem de Match" para sugerir o melhor template.

### 6.0. O Elemento de Conexão: Semantic Style Matcher

- **Responsabilidade:** Ash Visuals.
- **Input:** Copy final gerada pelo Gibson Writer.
- **Processo:** Extrair a "vibe" predominante (Nuvem de Palavras) e comparar com as nuvens de match abaixo.
- **Critério de Decisão:** Se o conteúdo for majoritariamente técnico/lógico, usa Pacote 6.1 ou 6.3. Se for reflexivo/humano, usa Pacote 6.4 (Claudinho) ou 6.2.

### 6.1. Padrão: Minimalismo Industrial & Teenage Engineering

- **Nuvem de Design (Elementos):** Grid técnico, metadados expostos, transparência, vidro acrílico, botões analógicos (knobs/sliders), fone transparente (Nothing), circuitos aparentes, tipografia monoespaçada fina, minimalismo utilitário.
- **Nuvem de Match (Conteúdo):** Hacks técnicos, passo a passo, tutorial prático, engenharia de prompts, "como funciona por dentro", lógica, sistemas de automação, ferramentas, eficiência operacional, setup, configurações avançadas.
- **Paleta de Cores Associada:** Engineering White, Prata Metálico, Fundo Preto Absoluto (Dark Mode dominante) com Acentos precisos em Neon Orange ou Vermelho Urgência (apontamento a laser).

### 6.2. Padrão: Modernismo Orgânico & Paramétrico

- **Nuvem de Design (Elementos):** Curvas suaves, repetição matemática (Panda Tower/MetaHive), elementos em madeira clara, texturas orgânicas, fachadas de terracota, iluminação natural volumétrica, design de espaços acolhedores, formas paramétricas responsivas a luz.
- **Nuvem de Match (Conteúdo):** Reflexões filosóficas sobre design, sustentabilidade tecnológica, histórias de evolução em carreira, cultura e comportamento humano, liderança suave, fluidez e adaptação, impacto criativo a longo prazo, mentalidade de crescimento ("growth").
- **Paleta de Cores Associada:** Tons terrosos (Earthy olive, Golden amber, Burnt brown), Beges (FFF4EB), Branco Quente, Verde Menta (Mint/95B388).

### 6.3. Padrão: NASA Punk & Brutalismo Void

- **Nuvem de Design (Elementos):** Estética de maquinário aeroespacial obsoleto/robusto, contraste extremo de luz, fotografias com alto contraste e baixo nível de negros (crushed blacks), tipografia gigantesca espremendo as margens, assimetria intencional, interfaces utilitárias frias.
- **Nuvem de Match (Conteúdo):** Alertas severos ("Hot takes"), avisos de disrupção de mercado, lançamentos urgentes (ex: Claude 2.1.97 release, Veo 3.1), mudanças de paradigma definitivas, previsões de tecnologia "hard", manifestos e opiniões impopulares.
- **Paleta de Cores Associada:** Charcoal Void massivo, Charcoal Escuro (#3D372F), Branco Frio 100%, Vermelhos e Bordôs pesados (Red Gradient Capsules).

### 6.4. Padrão: Claudinho Vibes — Soft Minimal Anthropic
>
> 📂 Referências em: `/ref_visual_style/claudinho_vibes/` — estética usada pela Anthropic no produto Claude AI.

- **Nuvem de Design (Elementos):** Fundos em pastel terroso quente (bege, areia, sage, terracota apagada), cards off-white com bordas extremamente arredondadas (border-radius 16–32px), sombras ultra-suaves e etéreas (shadows like floating paper), serifa editorial de alto contraste para títulos ("academic luxury"), sans-serif geométrica limpa para UI e labels, ícones com traço "scribble" (mão-levantada), símbolo-flor/asterisco como marca recorrente, mockups abstraídos (nunca screenshots literais), espaçamento generoso e respiração urbana, micro-italics serifs em rodapés e legendas.
- **Nuvem de Match (Conteúdo):** Conteúdo reflexivo sobre IA e humanidade, posts educacionais suaves, narrativas de produto e lançamentos com tom empático, threads filosóficas sobre criatividade e cognição, peças que precisam de acolhimento e não de impacto agressivo, conteúdo em tom de "conversa entre pessoas inteligentes", tutoriais gentis e guias de onboarding, carrosséis sobre escrita, leitura ou pensamento crítico.
- **Paleta de Cores Associada:**
  - `[Fundo Principal]` Warm Beige/Tan: `#F7F5F0` / `#D2CBBF`
  - `[Fundo Secundário]` Muted Sage Green: `#BFC7C1`
  - `[Acento Quente]` Terracota Suave/Burnt Orange: `#D97757`
  - `[Elemento de Alta Densidade]` Charcoal Soft: `#1A1A1A` (botões, texto primário)
  - `[Detalhe de Status/Data]` Emerald, Teal, Mustard Muted (usado em gráficos e badges)
- **Tipografia Específica do Padrão:**
  - Display/Marca: Serifa editorial de alto contraste — ex: *Lora*, *Editorial New*, *Cormorant* — pesos 400/700
  - Corpo e UI: Sans-serif geométrica neutra — ex: *DM Sans*, *Plus Jakarta Sans* — pesos 400/500
  - Micro-labels: Italic serif leve para legendas e notas de rodapé
- **Sintaxe de Layout:**
  - Composição majoritariamente centralizada com respiro simétrico
  - Cards flutuantes sobrepostos em layers suaves
  - Jamais tipografia sangrada nas bordas — sempre padding generoso
  - Elementos decorativos (scribbles, flores, asteriscos) como adornos sutis, nunca dominantes

### 6.5. Padrão: Japandi & Tropical Brutalism

- **Nuvem de Design (Elementos):** Arquitetura orgânica, madeira natural, jardins zen (Kyoto/Osaka), concreto aparente sob sol rasante (Oaxaca vibes), pedras vulcânicas, folhagens tropicais densas, harmonia rígida com a natureza.
- **Nuvem de Match (Conteúdo):** Sustentabilidade, ambientes de alta performance, bem-estar, cultura corporativa saudável, minimalismo essencialista, evolução de carreira com viés calmo/reflexivo.
- **Paleta de Cores Associada:** Beges, terracota, verdes naturais (jardim e musgo), madeira clara e cinza cimento quente.

### 6.6. Padrão: Retro-Tactical & Mecha (Anime/80s)

- **Nuvem de Design (Elementos):** Dispositivos modulares, visores monocromáticos de LCD, fios aparentes, estética "Cassette Futurism" (Casio/Sony/Nothing), neon ácido, cores de mechas (roxo/verde EVA Unit 01), Cyberpunk, teclas grossas e táteis.
- **Nuvem de Match (Conteúdo):** Tutoriais de "hard-code", curadoria de automações raízes, "hacks" de produtividade, ferramentas open-source, setup nerd de mesa, dicas práticas para developers.
- **Paleta de Cores Associada:** Verde Limão, Roxos elétricos, Cyan profundo, Preto massivo, Laranjas neon de alto contraste.

### 6.7. Padrão: Editorial High-Fashion & Cinematic Neon

- **Nuvem de Design (Elementos):** Layouts de revista de alto luxo, fotos com iluminação dramática de estúdio, tipografia serifada absurda e elegante, cores "Cinematic" neon de rua, posters de alto impacto (GT poster), estética "anne_hathaway_editorial".
- **Nuvem de Match (Conteúdo):** Thought leadership executivo, disrupções de mercado (hot takes luxuosos), opiniões de diretor de marketing, análises macroeconômicas ou "manifestos de marca" que exigem extrema sofisticação.
- **Paleta de Cores Associada:** Tons profundos misturados com magenta, laranjas de Palm Springs, pretos fotográficos sem grão, contrastes fotográficos absolutos.

### 6.8. Padrão: Cyberpunk Noir & Tech-Dystopia (Pacote I)

> 📂 Referências em: `/ref_visual_style/Ficção e Cinema/` e `/ref_visual_style/Vídeos/ficcao_cinema/`

- **Nuvem de Design (Elementos):** Cidades noturnas chuvosas, neon contrastando com escuridão total, fumaça/neblina volumétrica, interfaces glitchy, fios soltos, letreiros orientais misturados com tech ocidental.
- **Nuvem de Match (Conteúdo):** Alertas sobre o futuro da IA, análises preditivas sombrias, "o lado oculto" da tecnologia, narrativas de sobrevivência no mercado.
- **Paleta de Cores Associada:** Preto abissal, azul elétrico (Cyan), magenta neon, amarelo perigo (Warning Yellow).

### 6.9. Padrão: Beleza Editorial & Portraiture (Pacote J)

> 📂 Referências em: `/ref_visual_style/Beleza e Retratos/` e `/ref_visual_style/Vídeos/beleza_retratos/`

- **Nuvem de Design (Elementos):** Fotografias centradas no rosto humano, iluminação de estúdio meticulosa, texturas de pele reais (sem blur artificial), olhar penetrante, contato visual forte, enquadramentos clássicos de retrato.
- **Nuvem de Match (Conteúdo):** Histórias pessoais profundas, empatia no trabalho, liderança centrada no humano, vulnerabilidade, o papel da criatividade humana vs máquina.
- **Paleta de Cores Associada:** Tons de pele naturais, iluminação quente (Rembrandt lighting), fundos escurecidos neutros para destaque do sujeito.

### 6.10. Padrão: Anime Pop & Eastern Aesthetic (Pacote K)

> 📂 Referências em: `/ref_visual_style/Mangá e Anime/` e `/ref_visual_style/Ilustração e Arte Digital/`

- **Nuvem de Design (Elementos):** Estilo Ghibli (paisagens exuberantes, nuvens pintadas à mão), mechas vibrantes, linhas de ação dinâmicas, cel shading, expressões faciais exageradas mas precisas.
- **Nuvem de Match (Conteúdo):** Reflexões sobre "a jornada do herói", masterização de habilidades, superação de limites, tutoriais de animação/motion, cultura otaku aplicada à disciplina profissional.
- **Paleta de Cores Associada:** Azuis cerúleos brilhantes (céu anime), verdes vibrantes de grama, tons pastéis nostálgicos, luzes estelares/lens flares.
