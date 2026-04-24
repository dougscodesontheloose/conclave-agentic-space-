---
name: React Best Practices
description: Linter semântico e refatorador focado em React. Enforça separação de UI/Lógica (Custom Hooks), hooks rules e otimização. Requer autorização explícita do usuário baseada em relatório de impacto.
type: linting_refactoring
---

# Skill: React Best Practices

Esta skill atua como um Arquiteto Frontend Sênior focado em React. O objetivo é analisar componentes existentes ou recém-criados e garantir que eles atendam ao padrão de excelência de mercado, focando em manutenibilidade, legibilidade e performance.

## Diretrizes de Excelência

1. **Separação de Preocupações (SoC):** Lógica complexa de estado e efeitos colaterais deve ser extraída para Custom Hooks, deixando o componente apenas responsável por renderização.
2. **Memoização Consciente:** Avaliar a necessidade real de `useMemo` e `useCallback` para evitar re-renderizações desnecessárias sem poluir o código com otimizações prematuras.
3. **Estruturação Padrão:** Garantir que importações, declarações de tipos (TypeScript, se aplicável) e a organização de pastas sigam as convenções modernas do ecossistema React.

## OBRIGATÓRIO: Relatório Comparativo (Gatekeeper)

**Atenção:** Você NÂO tem permissão para alterar os arquivos ou aplicar as refatorações de imediato. Esta skill é opinativa e pode entrar em atrito com arquiteturas locais.

Antes de qualquer refatoração, você DEVE gerar um **Relatório Comparativo de Refatoração** e exibi-lo ao usuário.

O relatório deve conter:
- **Estado Atual vs Proposto:** O que está sendo mudado em alto nível.
- **Prós:** Ganhos em performance, legibilidade ou escalabilidade.
- **Contras:** Aumento de complexidade, overhead inicial.
- **O Que Pode Quebrar (Riscos):** Dependências, props de componentes pai, efeitos colaterais.
- **Trecho de Código (Diff):** Uma pequena demonstração do "Antes" e "Depois".

Após gerar o relatório, **PARE** a execução e aguarde. A **Palavra Final é do Usuário**. Somente com um explícito "Aprovado" ou "Pode rodar", você aplicará as mudanças propostas no código.
