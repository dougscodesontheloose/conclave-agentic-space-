# Protocolo Exodus: Conclave Open Source

**Este é o protocolo restrito de sanitização e higienização para exportar a versão pública (Open Source) do Conclave.**

> [!WARNING]  
> Operar em Sua Hostia: A higienização precisa ser abrangente, expressiva, com looping de redundância e verificação plena para conferir a remoção completa de padrões de identidade historicamente associados ao Criador do Projeto (<user_name>, <user_name> ou <user_name>).

## 1. Exclusão de Diretórios (O que NÃO vai para o Open Source)

Além das exclusões do `.gitignore` original, os seguintes diretórios e escopos **inteiros** devem ser expurgados da árvore a ser enviada ao GitHub público:

- **Pasta inteira `references/`**: Nenhum MD, nenhum brand style, nenhum visual style, nenhum arquivo de mídia. Ignorado sumariamente por razões de preferências artísticas/pessoais do usuário criador.
- **Pasta inteira `ambientes/` e `projetos/`**: Nenhum ambiente será incluído. Exemplos específicos que ficam de fora:
  - Alexandria
  - Wazhar
  - Cliff Palace (Gestão e manutenção financeira)
  - Corner Office
  - Lazarus
  - Subprojetos de estatificação de dados de busca de oportunidade de emprego.
  - Todas as versões de ensino de idiomas (Arcade House, Tive Di Amo, Adopo / Ensino de Italiano, Gosaimassio / Japonês, Hablando Demais / Espanhol, I'd like some tea / Inglês, Lojinha, etc).

## 2. Higienização de Identidade (Loops de Redundância)

Ao rodar a checagem Open Source, a IA deve inspecionar os arquivos remanescentes e realizar as seguintes substituições/purificações:

1. **Dados Sensíveis e Chaves**: Remoção total de chaves de API reais, logins e senhas.
2. **Atribuição Pessoal ("<user_name>", "<user_name>" ou "<user_name>")**: 
   - Na versão Open Source, o nome e os padrões do criador só podem constar no arquivo `README.md` principal, creditando-o como o idealizador, função e motivação do ambiente.
   - Em *todos os outros elementos* do sistema (prompts de agentes, rotinas, etc), substitua as menções a <user_name> ou <user_name> por rótulos genéricos como `<user_name>`, `<user_data>`, para que novos usuários utilizem o comando `Conclave.init` e o sistema seja repopulado e reanimado pelos *elementos pessoais deles*.
3. **Padrões de Comportamento e Estilo**: Sanitizar preferências pessoais de formatação de texto, preferências de design, padrões de escrita, padrões visuais e artísticos associados ao criador.
4. **Logs e Memórias Globais**:
   - `logs de sessão` devem estar estritamente **vazios**.
   - Padrões de memória do usuário nos squads (`memories.md`) devem ser limpos/higienizados.
   - Os parâmetros globais (`global-preferences.md`, etc) devem conter apenas a parametrização estrutural (chave) para a execução técnica da pipeline, **sem conter informações sensíveis, opiniões, inferências ou preferências de <user_name> ou <user_name>**.

## 3. Objetivo da Liberação

A versão Open Source é um esqueleto metodológico e funcional. O ambiente deve iniciar sem memória de vidas passadas, forçando a IA do novo usuário a moldar-se ao novo hospedeiro sem vieses oriundos da incubação original do projeto.

## ⚠️ Troubleshooting de Higienização (Lições Aprendidas)
Para evitar falhas de publicação em repositórios abertos, a seguinte restrição foi homologada na memória do sistema:
- **Proteção Ativa Contra Vazamento de Segredos (GitHub Rule GH013):** O GitHub audita estruturalmente commits para bloquear subidas contendo Client Secrets e API Keys. Em versões passadas, a heurística falhou por só procurar chaves modernas (`sk-ant-api`, `sk-proj-`). **Regra absoluta:** O loop de higienização da IA deve rastrear ativamente códigos "legacy" (`legacy/`, `scripts/`) em busca de `client_secret`, `access_token` e chaves OAuth antigas do LinkedIn, Google ou Meta, mascarando-as antes da indexação no Git do ambiente open source.
