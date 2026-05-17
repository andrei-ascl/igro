# Mapa de relacionamentos

O modelo usa `dCalendario` e `dOrgao_igro` como dimensões principais, além de manter relacionamentos automáticos com `LocalDateTable_*` criados pelo Power BI.

| # | From | To | Cardinalidade | Direção | Ativo | Notas |
|---|---|---|---|---|---|---|
| 1 | `f_pesquisa[data_resposta_pesquisa]` | `LocalDateTable_57787129-2bcd-48d2-807b-2fbedee7bd7d[Date]` | N:1 | singleDirection | ✓ | — |
| 2 | `f_insatisfatorias[data_manifestacao]` | `LocalDateTable_39814db9-3be3-4799-a6e9-766140062061[Date]` | N:1 | singleDirection | ✓ | — |
| 3 | `f_insatisfatorias[data_finalizacao]` | `LocalDateTable_19139d03-23fa-4bfa-91e8-4fe9100c0b7c[Date]` | N:1 | singleDirection | ✓ | — |
| 4 | `f_insatisfatorias[data_revisao]` | `LocalDateTable_89d62a24-1048-4894-9db0-6307d404f36e[Date]` | N:1 | singleDirection | ✓ | — |
| 5 | `f_pesquisa[data_manifestacao]` | `LocalDateTable_c6d333d1-ec5f-4b92-8fde-71e466729d16[Date]` | N:1 | singleDirection | ✓ | — |
| 6 | `f_insatisfatorias[protocolo]` | `f_relatorio[protocolo]` | N:1 | singleDirection | ✓ | — |
| 7 | `f_pesquisa[protocolo]` | `f_relatorio[protocolo]` | N:1 | singleDirection | ✓ | — |
| 8 | `f_relatorio[data_manifestacao]` | `dCalendario[Date]` | N:1 | singleDirection | ✓ | — |
| 9 | `f_relatorio[sigla]` | `dOrgao_igro[sigla]` | N:1 | singleDirection | ✓ | — |
| 10 | `f_relatorio[data_finalizacao]` | `LocalDateTable_c5428810-d49e-4c18-b272-7882a599a119[Date]` | N:1 | singleDirection | ✓ | — |
| 11 | `f_relatorio[data_revisao]` | `LocalDateTable_3e180244-5cb5-4814-8de3-11412ceb1457[Date]` | N:1 | singleDirection | ✓ | — |
| 12 | `f_relatorio[data_finalizacao]` | `dCalendario[Date]` | N:1 | singleDirection | — | inativo |
| 13 | `f_relatorio[data_revisao]` | `dCalendario[Date]` | N:1 | singleDirection | — | inativo |
| 14 | `f_pesquisa[data_manifestacao]` | `dCalendario[Date]` | N:1 | singleDirection | — | inativo |
| 15 | `f_insatisfatorias[data_manifestacao]` | `dCalendario[Date]` | N:1 | singleDirection | — | inativo |
