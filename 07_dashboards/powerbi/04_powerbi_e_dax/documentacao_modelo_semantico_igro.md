# Documentacao do modelo semantico IGRO

Atualizado em: 2026-05-18  
Modelo de referencia: `indice_igro_v2` no Power BI Desktop

Esta nota e um mapa funcional enxuto do modelo Power BI do IGRO. A ideia aqui nao e substituir o `.tmdl`, mas facilitar manutencao, auditoria e continuidade.

## Visao geral

| Grupo | Quantidade | Observacao |
|---|---:|---|
| Tabelas totais | 14 | Inclui tabelas automaticas de data do Power BI. |
| Tabelas de negocio visiveis | 6 | `f_relatorio`, `f_pesquisa`, `f_insatisfatorias`, `dCalendario`, `dOrgao_igro`, `_medidas`. |
| Medidas DAX | 117 | Inclui medidas tecnicas HTML/JSON usadas no dashboard. |
| Colunas | 165 | Inventario detalhado fica em `metadata/`. |
| Relacionamentos | 15 | Inclui relacoes ativas e inativas para analises temporais alternativas. |

## Estrutura do modelo

### Tabelas fato

| Tabela | Papel | Uso principal |
|---|---|---|
| `f_relatorio` | Fato central | Volume, tempo, procedencia, recursos e base principal do IGRO. |
| `f_pesquisa` | Fato de satisfacao | Resolutividade, nota de recomendacao, NPS e cobertura de pesquisa. |
| `f_insatisfatorias` | Fato de qualidade | Respostas reprovadas na revisao da ouvidoria. Base do KRI de insatisfacao. |

### Dimensoes

| Tabela | Papel | Uso principal |
|---|---|---|
| `dCalendario` | Calendario analitico | Eixo temporal oficial do modelo. |
| `dOrgao_igro` | Dimensao institucional | Filtros, rankings e comparacoes por orgao. |

### Tabela tecnica

| Tabela | Papel | Observacao |
|---|---|---|
| `_medidas` | Conteiner de medidas | Nao usar como fato ou dimensao em visuais. |

## Relacionamentos principais

| De | Para | Status | Uso |
|---|---|---|---|
| `f_relatorio[data_manifestacao]` | `dCalendario[Date]` | Ativo | Eixo temporal principal. |
| `f_relatorio[sigla]` | `dOrgao_igro[sigla]` | Ativo | Eixo institucional principal. |
| `f_pesquisa[protocolo]` | `f_relatorio[protocolo]` | Ativo | Liga pesquisa a manifestacoes. |
| `f_insatisfatorias[protocolo]` | `f_relatorio[protocolo]` | Ativo | Liga insatisfatorias a manifestacoes. |
| `f_relatorio[data_finalizacao]` | `dCalendario[Date]` | Inativo | Analise por data de finalizacao. |
| `f_relatorio[data_revisao]` | `dCalendario[Date]` | Inativo | Analise por data de revisao. |

Observacao:

- o modelo ainda contem relacionamentos com `LocalDateTable_*`, mas a referencia correta para analise e manutencao continua sendo `dCalendario`.

## Medidas

As medidas DAX da tabela `_medidas` podem ser lidas em tres camadas:

1. Operacional:
   `Volume`, `Pesquisa`, `Qualidade`, `Tempo`
2. Metodologica:
   `Metas`, `Scores`, `Subindices`, `Indice`
3. Visual:
   `Formatacao`, `Rotulo`, `JSON`, `HTML`

### Pastas de exibicao

| Pasta de exibicao | Quantidade | Finalidade |
|---|---:|---|
| `01 · Volume` | 6 | Contagens e bases de manifestacoes. |
| `02 · Pesquisa de Satisfacao` | 13 | Amostra, satisfacao, recomendacao e NPS. |
| `03 · Qualidade` | 7 | Qualidade da resposta e insatisfacao. |
| `04 · Tempo` | 17 | Prazo, TMR, dias de vida e atraso. |
| `05 · IGRO · Metas e Goalposts` | 11 | Metas e limites metodologicos. |
| `06 · IGRO · Scores KRI` | 5 | Scores normalizados dos KRIs. |
| `07 · IGRO · Indice` | 3 | Subindices e indice final. |
| `08 · Formatacao` | 12 | Semaforos, cores e apoio visual. |
| `09 · Variacao` | 11 | Comparacoes temporais. |
| `10 · Semaforo · Variacao` | 11 | Leitura semaforica das variacoes. |
| `11 · Rotulo · Cartao` | 9 | Rotulos textuais para cartoes. |
| `12 · JSON · Dashboard` | 11 | Saidas HTML/JSON para o dashboard e o infografico executivo. |

### Medidas centrais para manutencao

Observacao:

- a pasta visual `12 · JSON · Dashboard` passa a concentrar 12 medidas com a inclusao do painel `HTML Barras 3 Medidas IGRO`.

| Medida | Papel | Observacao |
|---|---|---|
| `idx_igro` | Indice principal | Resultado composto do IGRO. |
| `idx_igro_sub_t` | Subindice | Componente temporal do IGRO. |
| `idx_igro_sub_q` | Subindice | Componente de qualidade e satisfacao. |
| `idx_score_igro_kri1` a `idx_score_igro_kri5` | Scores | Normalizacao dos cinco KRIs. |
| `meta_igro_kri1` a `goal_igro_kri5` | Parametros | Metas e goalposts do modelo. |
| `fmt_semaforo_igro` | Formatacao | Regra visual de semaforo do indice. |
| `HTML Dashboard IGRO` | Entregavel visual | Dashboard HTML principal. |
| `HTML Dashboard Final` | Entregavel visual | Versao visual final do dashboard. |
| `HTML Infografico IGRO` | Entregavel visual | Infografico executivo com hierarquia `indice composto -> subindices -> KRIs`. |
| `HTML Barras 3 Medidas IGRO` | Entregavel visual | Painel HTML com tres graficos de barras por `QuadriLabel` para `idx_igro`, `idx_igro_sub_t` e `idx_igro_sub_q`. |

### Rodada de 2026-05-14

Mudancas registradas nesta rodada:

- auditoria do modelo semantico com artefatos em `_review/`;
- criacao da medida `HTML Infografico IGRO`;
- varias iteracoes visuais no modelo conectado para o infografico;
- criacao do guia `ajuste_manual_subs_html_igro.md` para ajuste manual dos subindices;
- uso combinado de iteracao no modelo conectado e sincronizacao do `.tmdl` apenas ao fim da sessao.

## Rodada de 2026-05-18

Mudancas registradas nesta rodada:

- criacao da medida `HTML Barras 3 Medidas IGRO`;
- composicao visual baseada no mesmo padrao premium escuro dos dashboards HTML ja existentes;
- reaproveitamento das medidas de semaforo e cor metodologica para colorir as barras dinamicamente;
- ajuste da medida para considerar os valores por quadrimestre, usando o contexto filtrado de `dCalendario[QuadriLabel]`.

## Colunas principais

Em vez de repetir o dicionario completo aqui, usar esta regra pratica:

- `f_relatorio` concentra `protocolo`, `sigla`, datas principais e metricas de prazo;
- `f_pesquisa` concentra campos de satisfacao, resolutividade e recomendacao;
- `f_insatisfatorias` concentra o subconjunto de respostas reprovadas;
- `dCalendario` e a dimensao temporal oficial;
- `dOrgao_igro` e a dimensao institucional oficial.

Se precisar do inventario completo de colunas, consultar:

- `metadata/powerbi_info_columns_2026-05-01.csv`

## Convencoes de continuidade

- `f_` para fatos
- `d` para dimensoes
- `_medidas` para medidas DAX
- novas medidas devem sempre nascer com `Description` e `DisplayFolder`
- apos alteracoes por MCP ou ferramenta externa, salvar o PBIX para persistir as mudancas
- quando a rodada visual terminar, gerar novo `.tmdl`

## Fontes de apoio

- `referencia_medidas_igro_2026-05-03.md`
- `metadata/powerbi_info_tables_2026-05-01.csv`
- `metadata/powerbi_info_columns_2026-05-01.csv`
- `metadata/powerbi_info_measures_2026-05-01.csv`
- `metadata/powerbi_info_relationships_2026-05-01.csv`
