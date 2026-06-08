# Parâmetros de Normalização dos KRIs do IGRO

Este documento consolida, em formato editorial, os parâmetros de normalização por distância à meta com goalposts utilizados no IGRO. O objetivo é facilitar a reutilização do conteúdo no artigo principal e em outros materiais de submissão.

## Tabela pronta para uso

**Tabela X — Parâmetros de normalização (goalposts) dos KRIs do IGRO**

| KRI | Indicador | Direção desejável | Meta (score = 1,0) | Goalpost (score = 0,0) |
| :-- | :-- | :-- | :-- | :-- |
| KRI 1 | Percentual de Manifestações em Atraso (PMA) | Menor é melhor | 1,0% | 2,0% |
| KRI 2 | Tempo Médio de Resposta (TMR) | Menor é melhor | 5,0 dias | 10,0 dias |
| KRI 3 | Resolutividade Percebida (RP) | Maior é melhor | 70,0% | 50,0% |
| KRI 4 | Percentual de Respostas Insatisfatórias (%RI) | Menor é melhor | 2,5% | 3,5% |
| KRI 5 | Nota de Recomendação (NR) | Maior é melhor | 8,0 | 6,0 |

## Texto de apoio

Os KRIs foram normalizados por distância à meta com goalposts, de modo que cada indicador assume valor entre 0 e 1. A meta representa o nível de desempenho considerado satisfatório (`score = 1,0`), enquanto o goalpost representa o limite inferior de aceitabilidade (`score = 0,0`). Para indicadores em que menor valor representa melhor desempenho, a normalização decresce entre meta e goalpost; para indicadores em que maior valor representa melhor desempenho, a normalização cresce entre goalpost e meta.

## Evidência de origem

Os parâmetros foram localizados nos seguintes notebooks do projeto:

- `06_notebooks/exploracao/igro_graficos_quadrimestres.ipynb`
- `06_notebooks/exploracao/igro_analise_sensibilidade_pesos.ipynb`
- `06_notebooks/exploracao/artigo_igro_graficos_tabelas.ipynb` (referência visual do TMR)

Valores identificados:

- KRI 1: `meta = 0.01` e `goalpost = 0.02`
- KRI 2: `meta = 5.0` e `goalpost = 10.0`
- KRI 3: `meta = 0.70` e `goalpost = 0.50`
- KRI 4: `meta = 0.025` e `goalpost = 0.035`
- KRI 5: `meta = 8.0` e `goalpost = 6.0`

## Observação editorial

Se a tabela for incorporada ao artigo principal, recomenda-se posicioná-la na seção metodológica, logo após a apresentação dos cinco KRIs ou na subseção de normalização, para reforçar a transparência do cálculo do índice.
