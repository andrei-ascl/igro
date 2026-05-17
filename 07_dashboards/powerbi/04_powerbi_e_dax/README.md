# Power BI e DAX

Esta pasta concentra os artefatos do modelo semantico e do dashboard IGRO no Power BI.

## Arquivos principais

| Arquivo ou pasta | Finalidade |
|---|---|
| `indice_igro_v2.pbix` | Versao atual de trabalho do dashboard/modelo IGRO. |
| `indice_igro.pbix` | Versao anterior ou alternativa do PBIX. |
| `documentacao_modelo_semantico_igro.md` | Documentacao funcional do modelo: tabelas, classificacao, colunas, papeis, medidas e relacionamentos. |
| `metadata/` | Exports de auditoria do modelo gerados via DAX `INFO.*`. |
| `medidas_dax_snake_case_camadas.md` | Referencia das medidas DAX e organizacao por camadas. |
| `dax_enterprise_guide_basedadosouvidoria.md` | Guia de referencia para padronizacao DAX no contexto da base de ouvidoria. |
| `kit_comandos_mcp_powerbi.md` | Comandos e fluxo de trabalho com MCP Power BI. |
| `nota_referencia_dax_obsidian.md` | Nota de referencia para uso das medidas e documentacao em Obsidian. |

## Manutencao recomendada

1. Salvar o PBIX sempre que descricoes de tabelas, colunas ou medidas forem alteradas no modelo semantico.
2. Atualizar `documentacao_modelo_semantico_igro.md` quando houver nova tabela, coluna relevante, medida central ou relacionamento.
3. Exportar novos CSVs para `metadata/` apos mudancas estruturais usando:
   - `EVALUATE INFO.TABLES()`
   - `EVALUATE INFO.COLUMNS()`
   - `EVALUATE INFO.MEASURES()`
   - `EVALUATE INFO.RELATIONSHIPS()`
4. Registrar a data nos nomes dos arquivos de inventario para manter historico de revisao.

## Estado atual da documentacao

Revisao de 2026-05-01:

- 14 tabelas inventariadas.
- 165 colunas inventariadas.
- 114 medidas DAX inventariadas.
- 15 relacionamentos inventariados.
- Tabelas classificadas como fato, dimensao, tabela tecnica ou sistema.
- Medidas verificadas com descricao preenchida no modelo semantico.

