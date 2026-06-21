---
name: corner-office
description: Strategic career repositioning framework for Tech, Data, and AI transition. Optimizes LinkedIn profiles, resumes, and executive narratives to bypass ATS filters and attract premium recruiter inbound contacts.
type: prompt
version: 1.0.0
categories:
  - career
  - branding
  - resume
  - linkedin
contract:
  inputs:
    - name: career_goals
      required: true
      description: "Target role (e.g., Analytics Engineer, Senior Data Analyst, Growth BI), focus stack, and location requirements."
    - name: experience_history
      required: true
      description: "Raw career history (e.g., Wipro/Meta, Florença, Propagatur) containing metrics and outcomes."
  outputs:
    - name: profile_about_section
      format: markdown
      description: "Optimized 3-block LinkedIn 'Sobre' section."
    - name: cv_car_experiences
      format: markdown
      description: "CV/LinkedIn experience bullet points structured in the 5-line CAR case format."
    - name: linkedin_posts_drafts
      format: markdown
      description: "LinkedIn authority content structured in the 3-6 line micro-thesis format."
  quality_criteria:
    - "LinkedIn 'Sobre' is structured strictly into 3 thematic blocks (Origin/Transition, Core Business Value, Tech Stack & Vision)."
    - "Each professional experience is formatted as a 5-line CAR (Context, Action, Result) case study with a measurable outcome."
    - "LinkedIn posts are exactly 3 to 6 lines following the formula: Micro-thesis -> Supporting Data/Fact -> Business Implication -> Invitation to Interact."
    - "Absolute avoidance of empty self-flattery, buzzwords (e.g., 'ninja', 'expert', 'enthusiast') and sycophantic fillers."
    - "ATS-friendly keyword optimization integrating high-demand technical keywords (SQL, Python, Power BI, GA4, LLMs, RAG)."
  on_failure: retry_previous
---

# Corner Office — Skill de Reposicionamento Estratégico de Carreira

## Quando Usar

Utilize esta skill sempre que precisar analisar, atualizar ou gerar materiais de branding pessoal e posicionamento de carreira para <user_name> Moura. Isso inclui a otimização de perfis do LinkedIn, currículos (CVs), abordagens diretas a recrutadores (outreach) e produção de posts de autoridade.

## Diretrizes de Posicionamento e Narrativa

A transição de carreira de Comunicação/Marketing para Tecnologia de Dados e IA é sustentada por uma narrativa de **"Profissional Híbrido Pragmático"**. <user_name> Moura não é um acadêmico de estatística que aprendeu programação; ele é um estrategista de performance de negócios comprovado que incorporou dados e engenharia analítica para escalar operações de milhões de dólares.

### 1. Perfil do LinkedIn — Estrutura de "Sobre" em 3 Blocos
Para reter a atenção de recrutadores e hiring managers em 10 segundos, o resumo "Sobre" deve ser dividido em 3 seções lógicas, diretas e limpas:
- **Bloco 1: A Origem e Transição.** A união da visão criativa/marketing com a necessidade de escala analítica.
- **Bloco 2: O Impacto Comprovado.** Destaque para governança de portfólios analíticos, orçamentos gerenciados e aumento percentual de conversão.
- **Bloco 3: A Caixa de Ferramentas & Futuro.** O stack técnico consolidado e em desenvolvimento (SQL, Python, Power BI, GA4, LLMs, RAG) e a tese de impacto organizacional.

### 2. Experiências Profissionais — Modelo CAR de 5 Linhas
Todas as descrições de cargo no CV devem caber em um resumo executivo composto por blocos de 5 linhas exatas baseados no modelo **Contexto-Ação-Resultado (CAR)**:
- **Linha 1 (Contexto):** O tamanho da operação, responsabilidade e o problema a ser resolvido (ex: budget gerenciado, volume de anunciantes, fragmentação de dados).
- **Linha 2 (Ação - Engenharia/Análise):** O que foi construído ou otimizado tecnicamente (ex: modelo de alocação de verba, pipeline de Power BI, automação de ETL).
- **Linha 3 (Ação - Negócio/Comunicação):** Como isso se conectou à estratégia humana ou de negócios (ex: consultoria bilíngue, alinhamento com stakeholders).
- **Linha 4 (Resultado):** O ganho percentual ou monetário quantificável (ex: +30% QoQ na performance consolidada, redução de retrabalho).
- **Linha 5 (Ferramentas/Stack):** Tecnologias explicitamente empregadas no processo (ex: Power BI, GA4, SQL, A/B Testing).

### 3. Conteúdo no LinkedIn — Fórmula de Micro-Tese (3 a 6 Linhas)
Posts de autoridade devem respeitar rigorosamente o teto de 3 a 6 linhas para maximizar a retenção no feed mobile. A estrutura é:
- **Linha 1-2 (Micro-tese / Gancho):** Uma afirmação forte, polêmica ou contra-intuitiva sobre dados, marketing ou IA (sem começar com perguntas).
- **Linha 3-4 (Fato / Evidência):** Um dado, caso de uso prático ou aprendizado extraído de um experimento real.
- **Linha 5 (Implicação de Negócio):** O impacto prático dessa tese para a eficiência ou ROI de uma empresa.
- **Linha 6 (Convite ao Diálogo):** Uma provocação curta e assertiva para abrir debates na seção de comentários.

## Evitar (Anti-Patterns)

- **Clichês de Transição:** Frases de autopromoção genérica como "Profissional extremamente apaixonado por desafios e aprendizado contínuo" ou "Em busca de novos horizontes no mundo dos dados". Substitua por evidências e stacks.
- **Detalhamento Operacional de Mídia:** Ficar descrevendo botões de Meta Ads ou criação de artes. Em vez disso, fale de "Elasticidade de canais", "Modelagem de alocação de mídia" e "Governança analítica de funis".
- **Visual Bloat no LinkedIn:** Emojis em excesso, hashtags poluindo o texto ou introduções prolixas. A estética deve ser minimalista, elegante e executiva.
