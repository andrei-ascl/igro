# indice_igro_v2 — Overview

> **Modelo de inteligência de ouvidoria pública para o IGRO, combinando volume, tempo de resposta, resolutividade, satisfação e qualidade em um índice composto por KRIs.**
> Documentação gerada por Claude Code + `/pbi-doc` em 07 mai 2026

**Arquivo:** `indice_igro_v2.pbip`

---

## Métricas

| Métrica | Valor |
|---|---|
| Tabelas reais | **6** |
| Medidas | **115** |
| Relacionamentos | **15** |
| Colunas totais | **96** |
| Tamanho .pbip | **~16005.0 KB** |

---

## Inventário de tabelas

| Tabela | Tipo | Colunas | Medidas | Source |
|---|---|---|---|---|
| `_medidas` | Tabela de medidas | 1 | 115 | Tabela calculada de suporte |
| `dCalendario` | Dimensão | 32 | 0 | Consulta M custom |
| `dOrgao_igro` | Dimensão | 5 | 0 | Consulta M custom |
| `f_insatisfatorias` | Fato | 24 | 0 | Consulta M custom |
| `f_pesquisa` | Fato | 10 | 0 | Consulta M custom |
| `f_relatorio` | Fato | 24 | 0 | Consulta M custom |

---

## Fontes de dados



---

## Configurações relevantes do modelo

| Configuração | Valor |
|---|---|
| Cultura | `pt-BR` |
| Data source version | `powerBI_V3` |
| Auto Date/Time | **ON** |

---

- [01 · Tabelas](01-tabelas.md)
- [02 · Medidas](02-medidas.md)
- [03 · Relacionamentos](03-relacionamentos.md)
- [04 · Dependências](04-dependencias.md)
