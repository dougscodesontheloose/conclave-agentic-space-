---
title: "Corner Office — Integração do Framework de Carreira e Samantha Staff"
date: 2026-05-20
type: feature_integration
era: "Memory & Log Optimization (v3)"
impact: high
---

# Corner Office — Integração do Framework de Carreira e Samantha Staff

## Contexto

<user_name> Moura está conduzindo uma transição estruturada de carreira de Comunicação/Marketing para Tecnologia de Dados e Inteligência Artificial com foco em Prompt/Context Engineering e Business Intelligence (BI). Para viabilizar e acelerar esse processo de reposicionamento profissional em nível global e local, fazia-se necessário incorporar o corpo de conhecimento da marca pessoal "Corner Office" no ecossistema Conclave.

## Decisão

Adotamos uma arquitetura de integração em duas camadas para separar as preocupações globais de inteligência de carreira das customizações e dados locais do usuário:

1. **Camada Global de Capacidades:**
   - Criação da skill 5 estrelas `skills/corner-office` com contratos formais para geração de Sobre (3 blocos), cases de CV (formato CAR de 5 linhas) e posts autorais no LinkedIn (micro-tese de 3-6 linhas).
   - Criação da agente especialista **Samantha Staff (Sam)**, com mais de 20 anos em recrutamento executivo, para conduzir análises frias e reposicionamentos de marca pessoal sem adulações.
   - Registro no catálogo unificado de capacidades (`SKILLS_INDEX.md`).

2. **Camada Local do Usuário:**
   - Injeção das diretrizes narrativas e dos assets prontos (LinkedIn headline, resumo em 3 blocos e experiências CAR para Wipro, Florença e Propagatur) no arquivo local e imutável `ambientes/corner-office/modes/_profile.md`. Isso permite que o pipeline local e os scripts de aplicação de vagas usem os dados consolidados e otimizados automaticamente.

## Capacidade Adicionada

- **Samantha Staff (Sam):** Agente global estruturada com mais de 100 linhas e equipada com todas as seções obrigatórias de qualidade Conclave.
- **Skill Corner Office:** Contrato estrito que valida e atesta a qualidade de posts do LinkedIn, cases profissionais e perfis, evitando termos vazios e garantindo compliance ATS.
- **Integração no Perfil Local:** Dados de branding estruturados em `modes/_profile.md` prontos para alimentar a automação de CV e de abordagens diretas (outreach).

## Impacto

O ecossistema Conclave passa a operar com inteligência nativa de RH. Toda geração de currículo ou texto profissional agora passa pela triagem crítica de Samantha Staff e pelas regras estritas da skill `corner-office`, blindando <user_name> Moura contra clichês e maximizando seu inbound de contratação no LinkedIn.
