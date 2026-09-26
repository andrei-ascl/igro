# Documentacao do modelo semantico IGRO

Conteúdo estrutural original: 2026-05-18
Revisão de governança: 2026-08-10
Modelo de referencia: `indice_igro_v2` no Power BI Desktop

Esta nota e um mapa funcional enxuto do modelo Power BI do IGRO. A ideia aqui nao e substituir o `.tmdl`, mas facilitar manutencao, auditoria e continuidade.

> **Fonte de verdade metodológica:** o perfil canônico de trabalho foi definido no Desenho Técnico em 2026-08-10, as medidas centrais do TMDL e as referências de dados foram alinhadas nesta rodada. As tabelas fato selecionam o Parquet mais recente por prefixo em C:\Users\andrei.lima\OneDrive\Claude-Work\Projects\igro\06_dados\01_brutos. O PBIP agora declara compatibilityLevel 1606 e pode ser reaberto para refresh/salvamento; as saídas históricas ainda precisam ser recalculadas e validadas.

## Visao geral

| Grupo | Quantidade | Observacao |
|---|---:|---|
| Tabelas totais | 14 | Inclui tabelas automaticas de data do Power BI. |
| Tabelas de negocio visiveis | 6 | `f_relatorio`, `f_pesquisa`, `f_insatisfatorias`, `dCalendario`, `dOrgao_igro`, `_medidas`. |
| Medidas DAX | 117 | Inclui medidas tecnicas HTML/JSON usadas no dashboard. |
| Colunas | 165 | Inventario detalhado fica em `metadata/`. |
| Relacionamentos | 15 | Inclui relacoes ativas e inativas para analises temporais alternativas. |

### Painel individual — análise setorial

O mockup da página `Análise setorial` foi revisado e aprovado para continuidade em 2026-08-22. O arquivo está em `_mockups/analise_setorial_mockup.html`.

Escopo visual definido:

- filtros por `dOrgao_igro`, `dCalendario[Ano]` e `dCalendario[QuadriLabel]`;
- modo de visão do período e modo de evolução histórica;
- IGRO como KPI principal, com Sub-T, Sub-Q e alertas como contexto;
- leitura executiva orientada ao KRI prioritário e à ação gerencial;
- tabela dos cinco KRIs com resultado, referência, score e situação;
- mini-cards de evidência com volumes, denominadores e cobertura explícitos.

O mockup usa valores ilustrativos e não representa uma saída recalculada do modelo. Nenhuma página, medida ou relacionamento foi acrescentado ao PBIP nesta etapa. A implementação será retomada em sessão posterior.

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
| `HTML Evolucao Quadrimestral IGRO` | Entregavel visual | Painel unico com tres graficos de linha empilhados sobre eixo de tempo comum, por `QuadriLabel`. Ver `medida_html_evolucao_quadrimestral.dax`. |
| `HTML IGRO Ano a Ano` | Entregavel visual | Evolucao ano a ano em pele escura. Vive na tabela `_medidas JSON - Dashboard`, nao em `_medidas`. |

> **Correcao de registro (2026-08-21):** a medida `HTML Barras 3 Medidas IGRO`, descrita nas rodadas de 2026-05-18, **nao existe no TMDL atual** — foi perdida em alguma sincronizacao entre 05/2026 e 08/2026. O painel quadrimestral foi reconstruido do zero como `HTML Evolucao Quadrimestral IGRO`, em linha empilhada e nao em barras.

### Rodada de 2026-05-14

Mudancas registradas nesta rodada:

- auditoria do modelo semantico com artefatos em `_review/`;
- criacao da medida `HTML Infografico IGRO`;
- varias iteracoes visuais no modelo conectado para o infografico;
- criacao do guia `ajuste_manual_subs_html_igro.md` para ajuste manual dos subindices;
- uso combinado de iteracao no modelo conectado e sincronizacao do `.tmdl` apenas ao fim da sessao.

## Rodada de 2026-08-21

Mudancas registradas nesta rodada:

- criacao da medida `HTML Evolucao Quadrimestral IGRO` (pasta `12 · JSON · Dashboard`): tres graficos de linha empilhados sobre eixo de tempo comum, escala vertical compartilhada e calculada a partir dos dados, quadrimestre em curso desenhado tracejado com ponto vazado;
- **correcao de paleta**: `#f5b11f` (Sub-T) e `#e99020` (Sub-Q) estavam a ΔE 8,4 em visao normal — abaixo do piso de 15 — e a 7,5 sob deuteranopia. Nao eram distinguiveis lado a lado. A tripla passou a `#0891b2` / `#c2410c` / `#6d28d9`, aprovada nos seis checks de acessibilidade cromatica;
- criacao das sete medidas de data de atualizacao (`dt_ultima_atualizacao_dados` e os seis rodapes `html_rodape_*`);
- correcao de seis `lineageTag` malformados gravados nos rodapes (continham caracteres fora do hexadecimal);
- correcao de um `lineageTag` malformado **pre-existente** em `idx_igro_sub_q`: `2a762a4d-37bc-41f8-ad98-b8e9ce7e056` tinha 11 caracteres no ultimo grupo em vez de 12, aparentemente truncado. Reparado para `...b8e9ce7e0560`. O valor antigo nao era referenciado em nenhum outro ponto do PBIP, e o novo foi conferido contra os 300 `lineageTag` do modelo para descartar colisao.

Estado dos identificadores apos a rodada: 300 `lineageTag` no modelo semantico, **nenhum malformado e nenhum duplicado**. Em `_medidas.tmdl`: 126 medidas, 126 descricoes `///`, 127 `lineageTag` (126 medidas + a coluna tecnica `Value`).

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
