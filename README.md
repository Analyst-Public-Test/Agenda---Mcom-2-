# Agenda SETEL

Gera `dados/agenda-setel.json` com a agenda do Secretário de Telecomunicações, **de 2026 em diante** (2024 e 2025 ficam fixos no HTML).

| Fonte | O que traz | Como é lida |
|---|---|---|
| e-Agendas (CGU) | compromissos | página pública da autoridade (sem captcha) |
| Portal da Transparência | viagens (PCDP, processo, motivo) | zip anual `.../download-de-dados/viagens/ANO` → `ANO_Viagem.csv` |

- **Automático:** todo dia às 8h e 14h (Brasília), ou manual em *Actions → Agenda SETEL → Run workflow*. Em 2027 não precisa mexer em nada: o ano novo entra sozinho.
- **Se uma fonte falhar:** o que já estava no JSON é mantido.
- **Plano B:** coloque `.xlsx`/`.csv` do e-Agendas em `dados/entrada/` e o zip/csv de viagens em `dados/entrada/viagens/` (o nome do arquivo de viagens deve conter o ano).
- **Autoridade:** `config/setel.json` (trocar de secretário = trocar nome, `servidor_id` e cargo).
- **Correção manual:** `config/ajustes.json` (nunca é sobrescrito). Por ID do compromisso: `cats`, `tem`, `lugar` ou `ocultar` (compromisso duplicado no e-Agendas).
- **Revisar:** `pendencias_de_lugar` e `pendencias_de_pais` no JSON listam o que o robô não conseguiu identificar.
- **Dependência:** o HTML da SETEL lê `https://raw.githubusercontent.com/Analyst-Public-Test/Agenda-SETEL/main/dados/agenda-setel.json`. Se o repositório mudar de nome, troque a constante `URL_JSON` no HTML.
