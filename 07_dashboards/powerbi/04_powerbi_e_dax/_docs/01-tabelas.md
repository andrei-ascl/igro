# Catálogo de tabelas

## _medidas

> [Tabela técnica] Contêiner organizacional das medidas DAX do modelo. Não representa entidade de negócio e não deve ser usada como dimensão ou fato em visuais.
> Tipo: Tabela de medidas
> Origem: Tabela calculada de suporte

### Descrição
[Tabela técnica] Contêiner organizacional das medidas DAX do modelo. Não representa entidade de negócio e não deve ser usada como dimensão ou fato em visuais.

### Granularidade
Sem granularidade física: tabela técnica para hospedar DAX.

### Colunas

| Coluna | Tipo | Papel | Notas |
|---|---|---|---|
| `Value` | `n/d` | Atributo | — |

### Medidas hospedadas
- `base_qtd_manifestacoes_em_aberto`
- `base_qtd_manifestacoes`
- `base_qtd_manifestacoes_finalizadas`
- `base_qtd_mais_30_dias`
- `base_qtd_lai`
- `base_manifestacoes_elegiveis`
- `base_qtd_pesquisa`
- `base_qtd_sim`
- `base_qtd_parcialmente`
- `base_qtd_respostas_insatisfatorias`
- `base_qtd_resolvidas`
- `ind_media_tempo_resposta`
- `ind_media_nota_recomendacao`
- `ind_pct_mais_30_dias`
- `ind_pct_resolutividade`
- `ind_pct_respostas_insatisfatorias`
- `meta_igro_kri1`
- `goal_igro_kri1`
- `meta_igro_kri2`
- `goal_igro_kri2`
- `meta_igro_kri3`
- `goal_igro_kri3`
- `meta_igro_kri4`
- `goal_igro_kri4`
- `meta_igro_kri5`
- `goal_igro_kri5`
- `idx_score_igro_kri1`
- `idx_score_igro_kri2`
- `idx_score_igro_kri3`
- `idx_score_igro_kri4`
- `idx_score_igro_kri5`
- `idx_igro_sub_t`
- `idx_igro_sub_q`
- `idx_igro`
- `base_qtd_promotores`
- `base_qtd_neutros`
- `base_qtd_detratores`
- `base_qtd_procedente`
- `base_qtd_com_recurso`
- `ind_nps`
- `ind_pct_promotores`
- `ind_pct_neutros`
- `ind_pct_detratores`
- `ind_pct_procedencia`
- `ind_pct_recurso`
- `ind_pct_cobertura_reclamacao`
- `fmt_semaforo_nps`
- `fmt_cor_fundo_nps`
- `fmt_cor_fonte_nps`
- `fmt_semaforo_procedencia`
- `fmt_semaforo_recurso`
- `fmt_semaforo_igro`
- `fmt_semaforo_igro_sub_t`
- `fmt_semaforo_igro_sub_q`
- `fmt_cor_fundo_igro`
- `fmt_cor_fonte_igro`
- `fmt_cor_fundo_igro_sub_t`
- `fmt_cor_fundo_igro_sub_q`
- `var_tmr`
- `var_pct_mais_30_dias`
- `var_resolutividade`
- `var_insatisfatorias`
- `var_nota`
- `var_nps`
- `var_igro`
- `var_igro_sub_t`
- `var_igro_sub_q`
- `var_recurso`
- `var_cobertura_reclamacao`
- `sem_tmr`
- `sem_pct_mais_30_dias`
- `sem_resolutividade`
- `sem_insatisfatorias`
- `sem_nota`
- `sem_nps`
- `sem_igro`
- `sem_igro_sub_t`
- `sem_igro_sub_q`
- `sem_recurso`
- `sem_cobertura_reclamacao`
- `lbl_tmr`
- `lbl_pct_mais_30_dias`
- `lbl_resolutividade`
- `lbl_insatisfatorias`
- `lbl_nota`
- `lbl_nps`
- `lbl_igro`
- `lbl_igro_sub_t`
- `lbl_igro_sub_q`
- `_JSON Orgaos`
- `_JSON Tipos`
- `_JSON KPIs`
- `HTML Dashboard IGRO`
- `base_qtd_manifestacoes_aa`
- `ind_tmr_aa`
- `ind_var_pct_volume_aa`
- `base_qtd_manifestacoes_quadri_anterior`
- `ind_var_pct_volume_quadri`
- `base_qtd_manifestacoes_ytd`
- `ind_media_diaria_manifestacoes`
- `ind_indice_sazonalidade`
- `base_qtd_manifestacoes_dias_uteis`
- `base_qtd_manifestacoes_fim_semana`
- `ind_pct_fim_semana`
- `ind_media_movel_3m`
- `ind_var_vs_media_movel`
- `base_qtd_finalizadas_por_data_fin`
- `HTML Dashboard Final Base`
- `HTML Matriz Classes IGRO`
- `flag_amostra_insuficiente`
- `base_manifestacoes_identificadas`
- `HTML Dashboard Final Fonte Branca`
- `HTML Dashboard Final`
- `HTML Tabela Resultados IGRO CSV`
- `HTML Dashboard Final Backup`

### Source M (resumo)
```m
{ BLANK() }
```


## dCalendario

> [Dimensão] Calendário corporativo do modelo. Controla análises temporais por dia, mês, trimestre, quadrimestre, semestre e ano. A relação ativa principal usa f_relatorio[data_manifestacao].
> Tipo: Dimensão
> Origem: Consulta M custom

### Descrição
[Dimensão] Calendário corporativo do modelo. Controla análises temporais por dia, mês, trimestre, quadrimestre, semestre e ano. A relação ativa principal usa f_relatorio[data_manifestacao].

### Granularidade
1 linha por dia do calendário analítico.

### Colunas

| Coluna | Tipo | Papel | Notas |
|---|---|---|---|
| `Date` | `n/d` | Atributo | Ano da data. |
| `Ano = YEAR(dCalendario[Date])` | `int64` | Calculada | Número do mês (1–12). |
| `Mes = MONTH(dCalendario[Date])` | `int64` | Calculada | Dia do mês (1–31). |
| `Dia = DAY(dCalendario[Date])` | `int64` | Calculada | Nome do mês por extenso em português. |
| `NomeMes = SWITCH(MONTH(dCalendario[Date]),1,"Janeiro",2,"Fevereiro",3,"Março",4,"Abril",5,"Maio",6,"Junho",7,"Julho",8,"Agosto",9,"Setembro",10,"Outubro",11,"Novembro",12,"Dezembro")` | `string` | Calculada | Mês abreviado (3 letras) em português. |
| `MesAbrev = SWITCH(MONTH(dCalendario[Date]),1,"jan",2,"fev",3,"mar",4,"abr",5,"mai",6,"jun",7,"jul",8,"ago",9,"set",10,"out",11,"nov",12,"dez")` | `string` | Calculada | Chave numérica de ordenação ano-mês (ex: 202401). Usar para ordenar NomeMes e AnoMesLabel. |
| `AnoMes = YEAR(dCalendario[Date]) * 100 + MONTH(dCalendario[Date])` | `int64` | Calculada | Número do dia da semana (1=Seg, 7=Dom). ISO 8601. |
| `NumDiaSemana = WEEKDAY(dCalendario[Date], 2)` | `int64` | Calculada | Nome do dia da semana por extenso em português. |
| `NomeDiaSemana = SWITCH(WEEKDAY(dCalendario[Date],2),1,"Segunda-feira",2,"Terça-feira",3,"Quarta-feira",4,"Quinta-feira",5,"Sexta-feira",6,"Sábado",7,"Domingo")` | `string` | Calculada | Dia da semana abreviado (3 letras). |
| `DiaSemanaAbrev = SWITCH(WEEKDAY(dCalendario[Date],2),1,"Seg",2,"Ter",3,"Qua",4,"Qui",5,"Sex",6,"Sáb",7,"Dom")` | `string` | Calculada | Número da semana no ano (ISO 8601, semana começa na segunda-feira). |
| `NumSemanaAno = WEEKNUM(dCalendario[Date], 2)` | `int64` | Calculada | Chave numérica ano-semana para ordenação (ex: 202401). |
| `AnoSemana = YEAR(dCalendario[Date]) * 100 + WEEKNUM(dCalendario[Date], 2)` | `int64` | Calculada | Trimestre do ano (1–4). |
| `Trimestre = ROUNDUP(MONTH(dCalendario[Date]) / 3, 0)` | `int64` | Calculada | Quadrimestre do ano (1=jan-abr, 2=mai-ago, 3=set-dez). Base do Relatório de Gestão CGE-GO. |
| `Quadrimestre = SWITCH(TRUE(),MONTH(dCalendario[Date])<=4,1,MONTH(dCalendario[Date])<=8,2,3)` | `int64` | Calculada | Nome do quadrimestre por extenso. |
| `NomeQuadrimestre = SWITCH(TRUE(),MONTH(dCalendario[Date])<=4,"1º Quadrimestre",MONTH(dCalendario[Date])<=8,"2º Quadrimestre","3º Quadrimestre")` | `string` | Calculada | Chave numérica ano-quadrimestre para ordenação (ex: 20241). |
| `AnoQuadri = YEAR(dCalendario[Date])*10 + SWITCH(TRUE(),MONTH(dCalendario[Date])<=4,1,MONTH(dCalendario[Date])<=8,2,3)` | `int64` | Calculada | Semestre do ano (1 ou 2). |
| `Semestre = IF(MONTH(dCalendario[Date])<=6,1,2)` | `int64` | Calculada | TRUE se sábado ou domingo. |
| `FimDeSemana = WEEKDAY(dCalendario[Date],2) >= 6` | `boolean` | Calculada | TRUE se segunda a sexta-feira. |
| `DiaUtil = WEEKDAY(dCalendario[Date],2) <= 5` | `boolean` | Calculada | TRUE se é o primeiro dia do mês. |
| `PrimeiroDiaMes = DAY(dCalendario[Date]) = 1` | `boolean` | Calculada | TRUE se é o último dia do mês. |
| `UltimoDiaMes = dCalendario[Date] = EOMONTH(dCalendario[Date], 0)` | `boolean` | Calculada | TRUE se a data pertence ao ano corrente. |
| `AnoAtual = YEAR(dCalendario[Date]) = YEAR(TODAY())` | `boolean` | Calculada | TRUE se a data está nos últimos 12 meses a partir de hoje. |
| `Ultimos12Meses = dCalendario[Date] >= EDATE(TODAY(),-12) && dCalendario[Date] <= TODAY()` | `boolean` | Calculada | TRUE se a data está nos últimos 3 meses (um quadrimestre retroativo). |
| `UltimoQuadrimestre = dCalendario[Date] >= EDATE(TODAY(),-4) && dCalendario[Date] <= TODAY()` | `boolean` | Calculada | Número sequencial de meses desde jan/2024 (mês 1 = jan/2024). Usado em cálculos de tendência e regressão linear no contexto do SGOe. |
| `MesExercicio = IF(YEAR(dCalendario[Date])>=2024, (YEAR(dCalendario[Date])-2024)*12 + MONTH(dCalendario[Date]), BLANK())` | `int64` | Calculada | Número sequencial de quadrimestres desde Q1/2024 (1=Q1/2024, 2=Q2/2024...). Base para comparação entre relatórios de gestão. |
| `QuadriExercicio = IF(YEAR(dCalendario[Date])>=2024, (YEAR(dCalendario[Date])-2024)*3 + SWITCH(TRUE(),MONTH(dCalendario[Date])<=4,1,MONTH(dCalendario[Date])<=8,2,3), BLANK())` | `int64` | Calculada | Número do dia no ano (1–365/366). Útil para análise de sazonalidade intra-anual. |
| `DiaDoAno = DATEDIFF(DATE(YEAR(dCalendario[Date]),1,1), dCalendario[Date], DAY) + 1` | `int64` | Calculada | Dia útil do mês (1, 2, 3...). Conta apenas dias úteis (seg-sex). Útil para análise de prazo interno. |
| `DiaUtilDoMes = CALCULATE(COUNTROWS(dCalendario), dCalendario[Date] <= EARLIER(dCalendario[Date]), MONTH(dCalendario[Date]) = MONTH(EARLIER(dCalendario[Date])), YEAR(dCalendario[Date]) = YEAR(EARLIER(dCalendario[Date])), dCalendario[DiaUtil] = TRUE())` | `int64` | Calculada | Rótulo do trimestre para eixos (ex: T1/2024). |
| `TrimestreLabel = "T" & FORMAT(dCalendario[Trimestre], "0") & "/" & FORMAT(dCalendario[Ano], "0")` | `string` | Calculada | Rótulo compacto do quadrimestre para eixos (ex: Q1/2024). |
| `QuadriLabel = SWITCH(TRUE(), MONTH(dCalendario[Date])<=4, "Q1", MONTH(dCalendario[Date])<=8, "Q2", "Q3") & "/" & FORMAT(dCalendario[Ano], "0")` | `string` | Calculada | Rótulo compacto do semestre para eixos (ex: S1/2024). |
| `SemestreLabel = IF(MONTH(dCalendario[Date])<=6, "S1", "S2") & "/" & FORMAT(dCalendario[Ano], "0")` | `string` | Calculada | Rótulo mês/ano para eixos de gráficos (ex: jan/2024). |
| `AnoMesLabel = dCalendario[MesAbrev] & "/" & FORMAT(dCalendario[Ano], "0")` | `string` | Calculada | — |

### Medidas hospedadas
- —

### Source M (resumo)
```m
CALENDAR(DATE(2023,1,1), DATE(2027,12,31))
```


## dOrgao_igro

> [Dimensão] Cadastro analítico de órgãos da rede de ouvidorias para o IGRO. Classifica cada sigla por tipo, grupo e classe, servindo como eixo institucional dos rankings, filtros e comparações.
> Tipo: Dimensão
> Origem: Consulta M custom

### Descrição
[Dimensão] Cadastro analítico de órgãos da rede de ouvidorias para o IGRO. Classifica cada sigla por tipo, grupo e classe, servindo como eixo institucional dos rankings, filtros e comparações.

### Granularidade
1 linha por órgão/ouvidoria da rede IGRO.

### Colunas

| Coluna | Tipo | Papel | Notas |
|---|---|---|---|
| `Tipo` | `string` | Atributo | [Papel: Atributo] Agrupamento temático ou administrativo do órgão, usado para análises comparativas entre blocos institucionais. |
| `Grupo` | `string` | Atributo | [Papel: Atributo] Classe analítica do órgão no IGRO, usada para segmentar a matriz por complexidade, volume ou perfil operacional. |
| `Classe` | `string` | Atributo | [Papel: Chave] Sigla do órgão ou entidade. Chave da dimensão dOrgao_igro e destino do relacionamento ativo com f_relatorio[sigla]. Também é propagada por TREATAS para f_pesquisa e f_insatisfatorias em medidas DAX. |
| `sigla` | `string` | Atributo | Marca o grupo G20 para visualizacoes futuras: 15 ouvidorias setoriais mais as 5 adjuntas com maior volume de manifestacoes (AGEHAB, PC, OVG, DGPP e JUCEG). |
| `G20 =` | `string` | Calculada | — |

### Medidas hospedadas
- —

### Source M (resumo)
```m
let
				    Fonte = Table.FromRows(
				        {
				            {"ABC",              "Adjunta",  "C",   "5"},
				            {"AGEHAB",           "Adjunta",  "B",   "2"},
				            {"AGR",              "Setorial", "A",   "2"},
				            {"AGRODEFESA",       "Adjunta",  "B",   "4"},
				            {"CBM",              "Adjunta",  "B",   "4"},
				            {"CEASA",            "Adjunta",  "B",   "4"},
				            {"CELG GT",          "Inativa",  "N/A", "N/A"},
				            {"CELGPAR",          "Adjunta",  "C",   "5"},
				            {"CGE",              "Setorial", "A",   "3"},
				            {"CODEGO",           "Adjunta",  "C",   "5"},
				            {"DETRAN",           "Setorial", "A",   "1"},
				            {"DGPP",             "Adjunta",  "B",   "3"},
				            {"ECONOMIA",         "Setorial", "A",   "2"},
				            {"EMATER",           "Adjunta",  "B",   "4"},
				            {"ENEL",             "Inativa",  "N/A", "N/A"},
				            {"FAPEG",            "Adjunta",  "B",   "5"},
				            {"GOIAS TELECOM",    "Adjunta",  "C",   "5"},
				            {"GOIAS TURISMO",    "Adjunta",  "C",   "5"},
				            {"GOIÁSFOMENTO",     "Adjunta",  "B",   "5"},
				            {"GOIASGÁS",         "Adjunta",  "C",   "5"},
				            {"GOIASPARCERIAS",   "Adjunta",  "C",   "5"},
				            {"GOIASPREV",        "Adjunta",  "B",   "4"},
				            {"GOINFRA",          "Setorial", "A",   "3"},
				            {"IPASGO",           "Inativa",  "N/A", "N/A"},
				            {"IQUEGO",           "Adjunta",  "C",   "5"},
				            {"JUCEG",            "Adjunta",  "B",   "4"},
				            {"METROBUS",         "Adjunta",  "B",   "4"},
				            {"OUVMULHER",        "Adjunta",  "B",   "3"},
				    
```


## f_insatisfatorias

> [Fato] Subconjunto das manifestações cuja resposta foi avaliada como insatisfatória pela equipe da ouvidoria. Uma linha por resposta reprovada na revisão de qualidade. Base do KRI de respostas insatisfatórias.
> Tipo: Fato
> Origem: Consulta M custom

### Descrição
[Fato] Subconjunto das manifestações cuja resposta foi avaliada como insatisfatória pela equipe da ouvidoria. Uma linha por resposta reprovada na revisão de qualidade. Base do KRI de respostas insatisfatórias.

### Granularidade
1 linha por manifestação cuja resposta foi considerada insatisfatória.

### Colunas

| Coluna | Tipo | Papel | Notas |
|---|---|---|---|
| `id_manifestacao` | `int64` | Atributo | [Papel: Chave estrangeira] Protocolo da manifestação cuja resposta foi avaliada como insatisfatória. Relaciona f_insatisfatorias à tabela central f_relatorio. |
| `protocolo` | `string` | Atributo | Data de registro da manifestação. Permite análise temporal da incidência de respostas insatisfatórias. |
| `data_manifestacao` | `dateTime` | Atributo | Data de finalização da manifestação cuja resposta foi reprovada. |
| `data_finalizacao` | `dateTime` | Atributo | Data da revisão que identificou a resposta como insatisfatória. |
| `data_revisao` | `dateTime` | Atributo | Sigla do órgão responsável pela resposta avaliada como insatisfatória. |
| `sigla` | `string` | Atributo | Subdivisão do órgão responsável, permitindo identificar unidades com maior incidência de respostas inadequadas. |
| `suborgao` | `string` | Atributo | Indicação de sigilo da manifestação com resposta reprovada. |
| `sigilo` | `string` | Atributo | Prazo interno do órgão para a manifestação com resposta reprovada. |
| `prazo_interno` | `int64` | Atributo | Prazo externo normativo aplicável à manifestação com resposta inadequada. |
| `prazo_externo` | `int64` | Atributo | Dias de tramitação da manifestação com resposta insatisfatória. |
| `dias_vida` | `int64` | Atributo | Dias após reativação, quando aplicável. |
| `dias_reativacao` | `int64` | Atributo | [Papel: Métrica de linha] Dias de atraso em relação ao prazo da manifestação com resposta insatisfatória. Campo numérico nesta tabela; em f_relatorio o campo equivalente está como texto. |
| `dias_atraso` | `int64` | Atributo | Tipo da manifestação com resposta insatisfatória. Reclamações concentram a maior parte dos casos (68% do total). |
| `tipo_manifestacao` | `string` | Atributo | Município de origem da manifestação com resposta insatisfatória. |
| `municipio` | `string` | Atributo | Assunto da manifestação com resposta reprovada. Permite identificar temas com maior dificuldade de atendimento. |
| `tipificacao` | `string` | Atributo | Detalhamento do assunto dentro da tipificação, para análise de segundo nível das falhas de atendimento. |
| `sub_tipificacao` | `string` | Atributo | Área interna do órgão responsável pela resposta inadequada. |
| `area_tecnica` | `string` | Atributo | Canal de entrada da manifestação avaliada como insatisfatória. |
| `registro` | `string` | Atributo | Status da manifestação no momento da avaliação de qualidade. |
| `ds_status` | `string` | Atributo | Flag de publicação no portal de transparência. |
| `publicacao` | `int64` | Atributo | Resultado da análise de mérito da manifestação com resposta insatisfatória. |
| `procedente` | `string` | Atributo | Instância de recurso associada, se houver. |
| `recurso` | `string` | Atributo | Número SEI vinculado à manifestação com resposta insatisfatória. |
| `nm_sei` | `string` | Atributo | — |

### Medidas hospedadas
- —

### Source M (resumo)
```m
let
				    Fonte = Folder.Files("C:\\Users\\andre\\OneDrive\\sgoe-data-raw\\data\\powerbi\\f_insatisfatorias"),
				    #"Arquivos Ocultos Filtrados1" = Table.SelectRows(Fonte, each [Attributes]?[Hidden]? <> true),
				    #"Invocar Função Personalizada1" = Table.AddColumn(#"Arquivos Ocultos Filtrados1", "Transformar Arquivo (4)", each #"Transformar Arquivo (4)"([Content])),
				    #"Colunas Renomeadas1" = Table.RenameColumns(#"Invocar Função Personalizada1", {"Name", "Nome da Origem"}),
				    #"Outras Colunas Removidas1" = Table.SelectColumns(#"Colunas Renomeadas1", {"Nome da Origem", "Transformar Arquivo (4)"}),
				    #"Coluna de Tabela Expandida1" = Table.ExpandTableColumn(
				        #"Outras Colunas Removidas1",
				        "Transformar Arquivo (4)",
				        {"id_manifestacao", "protocolo", "data_manifestacao", "data_finalizacao", "data_revisao", "sigla", "suborgao", "sigilo", "prazo_interno", "prazo_externo", "dias_vida", "dias_reativacao", "dias_atraso", "tipo_manifestacao", "municipio", "tipificacao", "sub_tipificacao", "area_tecnica", "registro", "ds_status", "publicacao", "procedente", "recurso", "nm_sei"},
				        {"id_manifestacao", "protocolo", "data_manifestacao", "data_finalizacao", "data_revisao", "sigla", "suborgao", "sigilo", "prazo_interno", "prazo_externo", "dias_vida", "dias_reativacao", "dias_atraso", "tipo_manifestacao", "municipio", "tipificacao", "sub_tipificacao", "area_tecnica", "registro", "ds_status", "publicacao", "procedente", "recurso", "nm_sei"}
				    ),
				    #"Tipo Alterado" = Table.TransformColumnTypes(#"Coluna de Tabela Expandida1", {
				        {"id_manifestacao", Int64.Type},
				        {"protocolo", type text},
				        {"data_manifestacao", type datetime},
				        {"data_finalizacao", type datetime},
	
```


## f_pesquisa

> [Fato] Respostas da pesquisa de satisfação enviada ao cidadão após a finalização da manifestação. Uma linha por resposta recebida. Base dos indicadores de resolutividade, nota de recomendação, NPS e amostra de pesquisa.
> Tipo: Fato
> Origem: Consulta M custom

### Descrição
[Fato] Respostas da pesquisa de satisfação enviada ao cidadão após a finalização da manifestação. Uma linha por resposta recebida. Base dos indicadores de resolutividade, nota de recomendação, NPS e amostra de pesquisa.

### Granularidade
1 linha por resposta de pesquisa de satisfação.

### Colunas

| Coluna | Tipo | Papel | Notas |
|---|---|---|---|
| `protocolo` | `string` | Atributo | Data original de registro da manifestação avaliada. Permite análise temporal da satisfação. |
| `data_manifestacao` | `dateTime` | Atributo | Sigla do órgão responsável pela manifestação avaliada na pesquisa. |
| `sigla` | `string` | Atributo | Nome do cidadão respondente, quando informado. Campo sensível — verificar conformidade com LGPD antes de expor em visuais. |
| `nome` | `string` | Atributo | Subdivisão do órgão responsável, permitindo análise de satisfação em nível mais granular. |
| `suborgao` | `string` | Atributo | Tipo da manifestação avaliada, permitindo cruzar satisfação por categoria (Reclamação, Solicitação etc.). |
| `tipo_manifestacao` | `string` | Atributo | [Papel: Métrica categórica] Resposta do cidadão sobre resolução da demanda: Sim, Não ou Parcialmente. Base do cálculo de resolutividade do IGRO. |
| `finalizacao` | `string` | Atributo | [Papel: Métrica] Nota de 1 a 10 sobre recomendação do serviço de ouvidoria. Base da nota média de recomendação, do NPS e do KRI 5 do IGRO. |
| `recomendaria` | `int64` | Atributo | Justificativa textual fornecida pelo cidadão para a nota atribuída. Campo qualitativo com potencial para análise de NLP. |
| `motivo` | `string` | Atributo | Data em que o cidadão respondeu à pesquisa. Permite calcular o tempo de resposta pós-finalização. |
| `data_resposta_pesquisa` | `dateTime` | Atributo | — |

### Medidas hospedadas
- —

### Source M (resumo)
```m
let
				    Fonte = Folder.Files("C:\\Users\\andre\\OneDrive\\sgoe-data-raw\\data\\powerbi\\f_pesquisa"),
				    #"Arquivos Ocultos Filtrados1" = Table.SelectRows(Fonte, each [Attributes]?[Hidden]? <> true),
				    #"Invocar Função Personalizada1" = Table.AddColumn(#"Arquivos Ocultos Filtrados1", "Transformar Arquivo (3)", each #"Transformar Arquivo (3)"([Content])),
				    #"Colunas Renomeadas1" = Table.RenameColumns(#"Invocar Função Personalizada1", {"Name", "Nome da Origem"}),
				    #"Outras Colunas Removidas1" = Table.SelectColumns(#"Colunas Renomeadas1", {"Nome da Origem", "Transformar Arquivo (3)"}),
				    #"Coluna de Tabela Expandida1" = Table.ExpandTableColumn(
				        #"Outras Colunas Removidas1",
				        "Transformar Arquivo (3)",
				        {"protocolo", "data_manifestacao", "sigla", "nome", "suborgao", "tipo_manifestacao", "finalizacao", "recomendaria", "motivo", "data_resposta_pesquisa"},
				        {"protocolo", "data_manifestacao", "sigla", "nome", "suborgao", "tipo_manifestacao", "finalizacao", "recomendaria", "motivo", "data_resposta_pesquisa"}
				    ),
				    #"Tipo Alterado" = Table.TransformColumnTypes(#"Coluna de Tabela Expandida1", {
				        {"protocolo", type text},
				        {"data_manifestacao", type datetime},
				        {"sigla", type text},
				        {"nome", type text},
				        {"suborgao", type text},
				        {"tipo_manifestacao", type text},
				        {"finalizacao", type text},
				        {"recomendaria", Int64.Type},
				        {"motivo", type text},
				        {"data_resposta_pesquisa", type datetime}
				    }),
				    #"Origem Removida" = Table.RemoveColumns(#"Tipo Alterado", {"Nome da Origem"}),
				    #"Sigla Padronizada" = Table.ReplaceValue(#"Origem Removida", "GT", "GOIAS TELECOM", Repl
```


## f_relatorio

> [Fato] Tabela central do modelo. Contém todas as manifestações registradas no SGOe — uma linha por manifestação, independente do status. Base principal para volume, tempo, procedência, recursos e relacionamento com pesquisas e respostas insatisfatórias.
> Tipo: Fato
> Origem: Consulta M custom

### Descrição
[Fato] Tabela central do modelo. Contém todas as manifestações registradas no SGOe — uma linha por manifestação, independente do status. Base principal para volume, tempo, procedência, recursos e relacionamento com pesquisas e respostas insatisfatórias.

### Granularidade
1 linha por manifestação registrada no SGOe.

### Colunas

| Coluna | Tipo | Papel | Notas |
|---|---|---|---|
| `id_manifestacao` | `int64` | Atributo | [Papel: Chave] Identificador único de negócio da manifestação no SGOe. Chave primária lógica da tabela f_relatorio e destino dos relacionamentos com f_pesquisa[protocolo] e f_insatisfatorias[protocolo]. |
| `protocolo` | `string` | Atributo | Data e hora em que a manifestação foi registrada no sistema. Ponto de partida para cálculo do TMR e dias de vida. |
| `data_manifestacao` | `dateTime` | Atributo | Data e hora em que a manifestação foi encerrada pelo órgão. Usada para determinar manifestações finalizadas. |
| `data_finalizacao` | `dateTime` | Atributo | Data da última revisão ou atualização de status da manifestação pelo órgão ou pela ouvidoria. |
| `data_revisao` | `dateTime` | Atributo | [Papel: Chave/Atributo] Sigla do órgão responsável pelo tratamento da manifestação. Relaciona f_relatorio à dimensão dOrgao_igro e serve como principal eixo institucional do IGRO. |
| `sigla` | `string` | Atributo | Subdivisão ou unidade interna do órgão à qual a manifestação foi encaminhada. |
| `suborgao` | `string` | Atributo | Indica se a manifestação possui caráter sigiloso, restringindo a visibilidade de dados ao cidadão e ao público. |
| `sigilo` | `string` | Atributo | Prazo em dias definido internamente pelo órgão para tratamento da manifestação. |
| `prazo_interno` | `int64` | Atributo | Prazo em dias estabelecido pela normativa externa (INs da CGE) para resposta ao cidadão. |
| `prazo_externo` | `int64` | Atributo | [Papel: Métrica de linha] Número de dias corridos desde o registro até a finalização ou até a data de extração. Base do TMR e de indicadores de manifestações com mais de 30 dias. |
| `dias_vida` | `int64` | Atributo | Quantidade de dias decorridos após uma reativação da manifestação pelo cidadão ou pela ouvidoria. |
| `dias_reativacao` | `int64` | Atributo | Indicação de atraso em relação ao prazo definido. Armazenado como texto nesta tabela — diverge do tipo Int64 em f_insatisfatorias. |
| `dias_atraso` | `string` | Atributo | Classificação da manifestação conforme a Lei 13.460/2017: Reclamação, Denúncia, Solicitação, Sugestão, Elogio, LAI ou LGPD. |
| `tipo_manifestacao` | `string` | Atributo | Município de origem da manifestação ou ao qual o objeto da demanda se refere. |
| `municipio` | `string` | Atributo | Assunto principal da manifestação, conforme classificação temática do SGOe. Base para análise de ranking de assuntos. |
| `tipificacao` | `string` | Atributo | Detalhamento do assunto dentro da tipificação principal. Permite análise de segundo nível dos temas mais recorrentes. |
| `sub_tipificacao` | `string` | Atributo | Área técnica interna do órgão responsável pelo tratamento da demanda encaminhada. |
| `area_tecnica` | `string` | Atributo | Canal de entrada da manifestação: Expresso (web), Webservice, Sistema E-mail, Sistema Telefone ou Sistema Presencial. |
| `registro` | `string` | Atributo | Status atual da manifestação no fluxo do SGOe: Aberta, Respondida ou Fechada. |
| `ds_status` | `string` | Atributo | Flag numérico indicando se a manifestação foi publicada no portal de transparência (1 = publicada, 0 = não publicada). |
| `publicacao` | `int64` | Atributo | Resultado da análise de mérito pelo órgão: Sim, Não ou Em análise. Base do indicador ind_pct_procedencia. |
| `procedente` | `string` | Atributo | Instância de recurso interposto pelo cidadão (1, 2 ou 3). Vazio quando não há recurso. Base do indicador ind_pct_recurso. |
| `recurso` | `string` | Atributo | Número do processo no sistema SEI vinculado à manifestação, quando houver tramitação documental associada. |
| `nm_sei` | `string` | Atributo | — |

### Medidas hospedadas
- —

### Source M (resumo)
```m
let
				    Fonte = Folder.Files("C:\\Users\\andre\\OneDrive\\sgoe-data-raw\\data\\powerbi\\f_relatorio"),
				    #"Arquivos Ocultos Filtrados1" = Table.SelectRows(Fonte, each [Attributes]?[Hidden]? <> true),
				    #"Invocar Função Personalizada1" = Table.AddColumn(#"Arquivos Ocultos Filtrados1", "Transformar Arquivo (2)", each #"Transformar Arquivo (2)"([Content])),
				    #"Colunas Renomeadas1" = Table.RenameColumns(#"Invocar Função Personalizada1", {"Name", "Nome da Origem"}),
				    #"Outras Colunas Removidas1" = Table.SelectColumns(#"Colunas Renomeadas1", {"Nome da Origem", "Transformar Arquivo (2)"}),
				    #"Coluna de Tabela Expandida1" = Table.ExpandTableColumn(
				        #"Outras Colunas Removidas1",
				        "Transformar Arquivo (2)",
				        {"id_manifestacao", "protocolo", "data_manifestacao", "data_finalizacao", "data_revisao", "sigla", "suborgao", "sigilo", "prazo_interno", "prazo_externo", "dias_vida", "dias_reativacao", "dias_atraso", "tipo_manifestacao", "municipio", "tipificacao", "sub_tipificacao", "area_tecnica", "registro", "ds_status", "publicacao", "procedente", "recurso", "nm_sei"},
				        {"id_manifestacao", "protocolo", "data_manifestacao", "data_finalizacao", "data_revisao", "sigla", "suborgao", "sigilo", "prazo_interno", "prazo_externo", "dias_vida", "dias_reativacao", "dias_atraso", "tipo_manifestacao", "municipio", "tipificacao", "sub_tipificacao", "area_tecnica", "registro", "ds_status", "publicacao", "procedente", "recurso", "nm_sei"}
				    ),
				    #"Tipo Alterado" = Table.TransformColumnTypes(#"Coluna de Tabela Expandida1", {
				        {"id_manifestacao", Int64.Type},
				        {"protocolo", type text},
				        {"data_manifestacao", type datetime},
				        {"data_finalizacao", type datetime},
				   
```
