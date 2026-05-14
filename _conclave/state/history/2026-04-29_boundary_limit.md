---
date: 2026-04-29
type: security_boundary
author: Conclave Core
---

# Registro de Fronteira: "City Limits"

## Contexto
Para garantir a higiene organizacional e a segurança de dados fora do escopo de trabalho, foi estabelecido um limite físico de acesso para o sistema Conclave e seus agentes.

## Decisão
O sistema agora opera sob um pacto de "City Limits" (Limites da Cidade).

**Caminho Autorizado:**
`/Users/douglasdepaulamoura/Documents/Bancada/`

## Regras de Engajamento
1. **Acesso Interno:** Todos os subdiretórios dentro de `Bancada/` são considerados zona de operação livre.
2. **Acesso Externo:** Qualquer tentativa de leitura, escrita ou execução de ferramentas fora deste caminho está estritamente proibida, a menos que uma autorização de "Nível Vermelho" seja concedida explicitamente pelo usuário em tempo real.
3. **Persistência:** Este limite é permanente e deve ser respeitado por todos os agentes carregados pelo Conclave.

## Impacto Arquitetural
- Redução do risco de vazamento de dados pessoais/financeiros localizados em outras pastas do sistema.
- Maior foco contextual nos projetos contidos em `Bancada/`.


---
**Tags:** #security #boundary #privacy #safeguard
