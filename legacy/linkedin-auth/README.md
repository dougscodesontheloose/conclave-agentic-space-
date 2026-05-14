# Legacy — LinkedIn Auth Scripts

Scripts de autenticação OAuth para LinkedIn. Quarentenados em 2026-05-07 para limpar a raiz do projeto.

## Arquivos

- `linkedin-auth.py`, `linkedin-auth2.py` — fluxos de OAuth para gerar `.linkedin_token`
- `test-auth.py` — sanity check do token
- `.linkedin_token` — token bearer (gitignored)

## Como continua sendo usado

[`squads/sexy_content/scripts/linkedin_publisher.py`](../../squads/sexy_content/scripts/linkedin_publisher.py) lê o token via env var `LINKEDIN_TOKEN_PATH` (default: `legacy/linkedin-auth/.linkedin_token`).

Para regenerar o token:

```bash
python legacy/linkedin-auth/linkedin-auth.py
```
