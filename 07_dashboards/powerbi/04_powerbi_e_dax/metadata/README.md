# Inventario de metadados do modelo IGRO

Exportacao gerada em 2026-05-01 a partir do modelo aberto no Power BI Desktop `indice_igro_v2`, usando consultas DAX `INFO.*` pelo MCP Power BI.

## Arquivos

| Arquivo | Conteudo | Uso recomendado |
|---|---|---|
| `powerbi_info_tables_2026-05-01.csv` | Inventario completo das tabelas do modelo, incluindo tabelas ocultas do Power BI. | Conferir classificacao, visibilidade e descricoes de tabelas. |
| `powerbi_info_columns_2026-05-01.csv` | Inventario completo das colunas, incluindo tipo, descricao, ocultacao, ordenacao e propriedades tecnicas. | Manter dicionario de dados, localizar lacunas de descricao e revisar papeis das colunas. |
| `powerbi_info_measures_2026-05-01.csv` | Inventario completo das medidas DAX, pastas de exibicao, expressoes e descricoes. | Auditar medidas, documentar formulas e verificar padronizacao por camadas. |
| `powerbi_info_relationships_2026-05-01.csv` | Inventario dos relacionamentos do modelo. | Revisar cardinalidade, relacoes ativas/inativas e dependencias entre fatos e dimensoes. |

## Como atualizar

1. Abra o PBIX no Power BI Desktop.
2. Conecte via MCP Power BI ao modelo aberto.
3. Reexecute:
   - `EVALUATE INFO.TABLES()`
   - `EVALUATE INFO.COLUMNS()`
   - `EVALUATE INFO.MEASURES()`
   - `EVALUATE INFO.RELATIONSHIPS()`
4. Copie os CSVs gerados para esta pasta com a data da nova revisao.
5. Atualize `../documentacao_modelo_semantico_igro.md` quando houver mudanca estrutural relevante.

