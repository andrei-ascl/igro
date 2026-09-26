---
title: Dicionário de dados IGRO
project: IGRO
status: staging
updated: 2026-08-05
---

# Dicionário de dados IGRO

> Este dicionário é uma referência conceitual de staging. A confirmação campo a campo ainda depende da inspeção do schema físico das fontes Parquet e do TMDL ativo. Não usar esta versão, isoladamente, para promover uma nova fórmula do IGRO.

## Fontes identificadas

| Arquivo | Entidade | Papel |
|---|---|---|
| `../raw/relatorio_2026-05-05.parquet` | `f_relatorio` | Manifestações, prazos, status e órgão |
| `../raw/pesquisa_2026-05-05.parquet` | `f_pesquisa` | Respostas de pesquisa e qualidade percebida |
| `../raw/insatisfatorio_2026-05-05.parquet` | `f_insatisfatorias` | Registros/classificações de insatisfação |
| `../processed/geral.csv` | Exportação derivada | Atualmente encapsulada em HTML/JavaScript; não é CSV tabular estável |
| `../processed/matriz_orgao.csv` | Exportação derivada | Atualmente encapsulada em HTML/JavaScript; não é CSV tabular estável |

## Entidades e campos conhecidos

### `f_relatorio`

| Campo/atributo | Tipo esperado | Uso | Status |
|---|---|---|---|
| `protocolo` | identificador/texto | Chave de manifestação e ligação entre fatos | Confirmar nome e unicidade |
| `sigla` | texto | Órgão e ligação com `dOrgao_igro` | Presente no modelo conceitual; confirmar domínio |
| Datas de manifestação, finalização e revisão | data/hora | Período, prazo e calendário | Confirmar nomes físicos |
| `status` | categórico | Elegibilidade e situação da manifestação | Confirmar valores |
| `dias_atraso`/medida equivalente | numérico | Risco 0044 e TMR | Confirmar se é coluna ou medida |

### `f_pesquisa`

| Campo/atributo | Tipo esperado | Uso | Status |
|---|---|---|---|
| `protocolo` | identificador/texto | Ligação com manifestação, quando disponível | Confirmar nome e cobertura |
| Resolutividade | categórico/numérico | Subíndice de qualidade (RES) | Confirmar codificação e denominador |
| Nota de recomendação/satisfação | numérico | Qualidade percebida e cenário de sensibilidade | Confirmar campo físico |
| NPS ou componentes equivalentes | numérico/categórico | Indicador de qualidade | Confirmar regra de cálculo |

### `f_insatisfatorias`

| Campo/atributo | Tipo esperado | Uso | Status |
|---|---|---|---|
| `protocolo` | identificador/texto | Ligação com manifestação, quando disponível | Confirmar nome e cobertura |
| Classificação/resposta insatisfatória | categórico | Risco 0046 e indicador RI | Confirmar domínio |
| Data e órgão | data/texto | Recorte temporal e agregação por órgão | Confirmar campos físicos |

### Dimensões do modelo semântico

| Entidade | Campos/atributos conhecidos | Uso |
|---|---|---|
| `dCalendario` | `Date`, `QuadriLabel` | Relação temporal e quadrimestres |
| `dOrgao_igro` | `sigla` | Dimensão de órgãos e agregação |
| `_medidas` | Medidas DAX | Camada de cálculo do modelo PBIP |

## Métricas e rastreabilidade

| KRI/subíndice | Entidade(s) de origem | Direção | Ponto de atenção |
|---|---|---|---|
| TMR / risco 0044 | `f_relatorio` | Menor atraso é melhor | Definir elegibilidade e tratamento de prazos |
| RES | `f_pesquisa` e/ou campos derivados de `f_relatorio` | Maior resolutividade é melhor | Confirmar numerador/denominador |
| RI | `f_insatisfatorias` | Menor insatisfação é melhor | Confirmar classificação e denominador |
| NPS/qualidade percebida | `f_pesquisa` | Maior valor é melhor | Separar indicador de cenário de sensibilidade |
| IGRO | Subíndices T e Q | Conforme perfil canônico | A fórmula e os pesos ainda estão pendentes |

## Regras de qualidade que precisam acompanhar o dado

- data da extração e período de referência;
- universo de 51 órgãos no escopo geral;
- subconjunto de 47 órgãos completos na análise de sensibilidade;
- presença de duplicidades, nulos e chaves sem correspondência;
- numeradores e denominadores por KRI;
- regra de amostra pequena (`flag_amostra`, exclusão, suavização ou sinalização);
- perfil de parâmetros utilizado para normalização, pesos e agregação;
- formato real das saídas em `processed/`.

## Lacunas abertas

1. Confirmar os nomes físicos e tipos de todos os campos no Parquet.
2. Registrar o mapeamento completo entre campos físicos e entidades do TMDL.
3. Definir a regra de inclusão de amostras pequenas.
4. Resolver a variante canônica do método antes de publicar novos índices.
5. Substituir ou renomear os CSVs encapsulados em HTML/JavaScript para evitar uso indevido.

## Referências de governança

- [`../../00_admin/controle_versoes/AUDITORIA_CONSOLIDAR_ATIVO_IGRO_2026-08-05.md`](../../00_admin/controle_versoes/AUDITORIA_CONSOLIDAR_ATIVO_IGRO_2026-08-05.md)
- [`../../00_admin/controle_versoes/DECISAO_CANONICA_IGRO.md`](../../00_admin/controle_versoes/DECISAO_CANONICA_IGRO.md)
- [`../../00_admin/planejamento/03_especificacao_e_produto/CONTRATO_METRICAS_IGRO.md`](../../00_admin/planejamento/03_especificacao_e_produto/CONTRATO_METRICAS_IGRO.md)
