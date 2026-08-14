# Documentação Técnica — Medidas DAX do Modelo `indice_igro_v2`

Este documento reúne a documentação técnica das 119 medidas DAX do modelo semântico `indice_igro_v2`, usado para medir indicadores de qualidade de ouvidorias públicas — o Índice de Gestão de Riscos de Ouvidorias (IGRO), o NPS e os KRIs de tempestividade e qualidade. Cada medida está organizada por categoria (`displayFolder`) e traz nome técnico, descrição de negócio, formato de exibição (quando aplicável) e a expressão DAX real extraída do modelo.

## Sumário

- [01 · Volume](#01-volume) (6 medidas)
- [02 · Pesquisa de Satisfação](#02-pesquisa-de-satisfação) (13 medidas)
- [03 · Qualidade](#03-qualidade) (7 medidas)
- [04 · Tempo](#04-tempo) (17 medidas)
- [05 · IGRO · Metas e Goalposts](#05-igro-metas-e-goalposts) (11 medidas)
- [06 · IGRO · Scores KRI](#06-igro-scores-kri) (5 medidas)
- [07 · IGRO · Índice](#07-igro-índice) (3 medidas)
- [08 · Formatação](#08-formatação) (12 medidas)
- [09 · Variação](#09-variação) (11 medidas)
- [10 · Semáforo · Variação](#10-semáforo-variação) (11 medidas)
- [11 · Rótulo · Cartão](#11-rótulo-cartão) (9 medidas)
- [12 · JSON · Dashboard](#12-json-dashboard) (12 medidas)
- [Sem categoria / Ocultas](#sem-categoria-ocultas) (2 medidas)

## 01 · Volume

#### base_qtd_manifestacoes_em_aberto

Manifestações com status Aberta no SGOe.

**Formato:** `#,0`

```dax
VAR resultado =
    CALCULATE (
        COUNTROWS ( f_relatorio ),
        KEEPFILTERS ( f_relatorio[ds_status] = "Em Aberto" )
    )
RETURN
    COALESCE ( resultado, 0 )
```

#### base_qtd_manifestacoes

Total de manifestações registradas no período, independente do status.

**Formato:** `#,0`

```dax
VAR resultado =
    COUNTROWS ( f_relatorio )
RETURN
    COALESCE ( resultado, 0 )
```

#### base_qtd_manifestacoes_finalizadas

Manifestações com status Fechada ou Respondida no SGOe.

**Formato:** `#,0`

```dax
VAR total_manifestacoes = [base_qtd_manifestacoes]
VAR em_aberto = [base_qtd_manifestacoes_em_aberto]
RETURN
    total_manifestacoes - em_aberto
```

#### base_qtd_lai

Manifestações do tipo LAI (Lei de Acesso à Informação), excluídas de alguns indicadores.

**Formato:** `#,0`

```dax
VAR resultado =
    CALCULATE (
        [base_qtd_manifestacoes_finalizadas],
        KEEPFILTERS ( f_relatorio[tipo_manifestacao] = "L.A.I." )
    )
RETURN
    COALESCE ( resultado, 0 )
```

#### base_manifestacoes_elegiveis

Manifestações finalizadas descontando as LAI. Denominador base para KRI 3 e KRI 4.

**Formato:** `#,0`

```dax
VAR finalizadas = [base_qtd_manifestacoes_finalizadas]
VAR lai = [base_qtd_lai]
RETURN
    finalizadas - lai
```

#### base_manifestacoes_identificadas

Base de manifestacoes finalizadas identificadas (exclui Anonimo). Denominador correto para taxa de cobertura da pesquisa de satisfacao.

**Formato:** `#,0`

```dax
CALCULATE(
    [base_qtd_manifestacoes_finalizadas],
    f_relatorio[sigilo] <> "An" & UNICHAR(244) & "nimo"
)
```


## 02 · Pesquisa de Satisfação

#### base_qtd_pesquisa

Total de respostas recebidas na pesquisa de satisfação (linhas em f_pesquisa). TREATAS propaga filtro de dOrgao_igro[sigla].

**Formato:** `#,0`

```dax
VAR _siglas = VALUES(dOrgao_igro[sigla])
VAR resultado =
    CALCULATE(
        COUNTROWS(f_pesquisa),
        TREATAS(_siglas, f_pesquisa[sigla])
    )
RETURN
    COALESCE(resultado, 0)
```

#### base_qtd_sim

Pesquisas em que o cidadão respondeu que a demanda foi resolvida totalmente (finalizacao = 'Sim'). TREATAS propaga filtro de dOrgao_igro[sigla].

**Formato:** `#,0`

```dax
VAR _siglas = VALUES(dOrgao_igro[sigla])
VAR resultado =
    CALCULATE(
        COUNTROWS(f_pesquisa),
        TREATAS(_siglas, f_pesquisa[sigla]),
        KEEPFILTERS(f_pesquisa[finalizacao] = "Sim")
    )
RETURN
    COALESCE(resultado, 0)
```

#### base_qtd_parcialmente

Pesquisas em que o cidadão respondeu que a demanda foi resolvida parcialmente (finalizacao = 'Parcialmente'). TREATAS propaga filtro de dOrgao_igro[sigla].

**Formato:** `#,0`

```dax
VAR _siglas = VALUES(dOrgao_igro[sigla])
VAR resultado =
    CALCULATE(
        COUNTROWS(f_pesquisa),
        TREATAS(_siglas, f_pesquisa[sigla]),
        KEEPFILTERS(f_pesquisa[finalizacao] = "Parcialmente")
    )
RETURN
    COALESCE(resultado, 0)
```

#### base_qtd_resolvidas

Combinação ponderada de respostas: base_qtd_sim + 0,5 × base_qtd_parcialmente. Numerador da resolutividade.

**Formato:** `#,0.0`

```dax
VAR qtd_total_sim = [base_qtd_sim]
VAR qtd_parcial = [base_qtd_parcialmente]
RETURN
    qtd_total_sim + 0.5 * qtd_parcial
```

#### ind_media_nota_recomendacao

Média das notas de recomendação (1–10) nas pesquisas respondidas. Numerador do KRI 5. TREATAS propaga filtro de dOrgao_igro[sigla].

**Formato:** `#,0.0`

```dax
VAR _siglas = VALUES(dOrgao_igro[sigla])
VAR resultado =
    CALCULATE(
        AVERAGE(f_pesquisa[recomendaria]),
        TREATAS(_siglas, f_pesquisa[sigla])
    )
RETURN
    COALESCE(resultado, 0)
```

#### ind_pct_resolutividade

Percentual de resolução: (sim + 0,5 × parcialmente) / total de pesquisas. Indicador do KRI 3.

**Formato:** `0.00%`

```dax
VAR numerador = [base_qtd_resolvidas]
VAR denominador = [base_qtd_pesquisa]
RETURN
    DIVIDE ( numerador, denominador, 0 )
```

#### base_qtd_promotores

Respostas de pesquisa com nota de recomendação entre 9 e 10. Numerador do NPS. TREATAS propaga filtro de dOrgao_igro[sigla].

**Formato:** `#,0`

```dax
VAR _siglas = VALUES(dOrgao_igro[sigla])
VAR resultado =
    CALCULATE(
        COUNTROWS(f_pesquisa),
        TREATAS(_siglas, f_pesquisa[sigla]),
        KEEPFILTERS(f_pesquisa[recomendaria] >= 9)
    )
RETURN
    COALESCE(resultado, 0)
```

#### base_qtd_neutros

Respostas de pesquisa com nota de recomendação entre 7 e 8. Não entram no cálculo do NPS. TREATAS propaga filtro de dOrgao_igro[sigla].

**Formato:** `#,0`

```dax
VAR _siglas = VALUES(dOrgao_igro[sigla])
VAR resultado =
    CALCULATE(
        COUNTROWS(f_pesquisa),
        TREATAS(_siglas, f_pesquisa[sigla]),
        KEEPFILTERS(f_pesquisa[recomendaria] >= 7),
        KEEPFILTERS(f_pesquisa[recomendaria] <= 8)
    )
RETURN
    COALESCE(resultado, 0)
```

#### base_qtd_detratores

Respostas de pesquisa com nota de recomendação entre 1 e 6. Subtraídas no cálculo do NPS. TREATAS propaga filtro de dOrgao_igro[sigla].

**Formato:** `#,0`

```dax
VAR _siglas = VALUES(dOrgao_igro[sigla])
VAR resultado =
    CALCULATE(
        COUNTROWS(f_pesquisa),
        TREATAS(_siglas, f_pesquisa[sigla]),
        KEEPFILTERS(f_pesquisa[recomendaria] <= 6)
    )
RETURN
    COALESCE(resultado, 0)
```

#### ind_nps

NPS calculado: (% promotores − % detratores) × 100. Escala de −90 a +100.

**Formato:** `#,0.0`

```dax
VAR promotores = DIVIDE([base_qtd_promotores], [base_qtd_pesquisa], 0)
VAR detratores = DIVIDE([base_qtd_detratores], [base_qtd_pesquisa], 0)
RETURN
    (promotores - detratores) * 100
```

#### ind_pct_promotores

Percentual de promotores (nota 9–10) sobre o total de pesquisas respondidas.

**Formato:** `0.0%`

```dax
DIVIDE([base_qtd_promotores], [base_qtd_pesquisa], 0)
```

#### ind_pct_neutros

Percentual de neutros (nota 7–8) sobre o total de pesquisas respondidas.

**Formato:** `0.0%`

```dax
DIVIDE([base_qtd_neutros], [base_qtd_pesquisa], 0)
```

#### ind_pct_detratores

Percentual de detratores (nota 1–6) sobre o total de pesquisas respondidas.

**Formato:** `0.0%`

```dax
DIVIDE([base_qtd_detratores], [base_qtd_pesquisa], 0)
```


## 03 · Qualidade

#### base_qtd_respostas_insatisfatorias

Total de linhas em f_insatisfatorias. Respostas reprovadas na revisão de qualidade. TREATAS propaga filtro de dOrgao_igro[sigla].

**Formato:** `#,0`

```dax
VAR _siglas = VALUES(dOrgao_igro[sigla])
VAR resultado =
    CALCULATE(
        COUNTROWS(f_insatisfatorias),
        TREATAS(_siglas, f_insatisfatorias[sigla])
    )
RETURN
    COALESCE(resultado, 0)
```

#### ind_pct_respostas_insatisfatorias

Percentual de respostas insatisfatórias sobre as manifestações elegíveis. Indicador do KRI 4.

**Formato:** `0.00%`

```dax
VAR numerador = [base_qtd_respostas_insatisfatorias]
VAR denominador = [base_manifestacoes_elegiveis]
RETURN
    DIVIDE ( numerador, denominador, 0 )
```

#### base_qtd_procedente

Manifestações finalizadas com procedente = 'Sim'.

**Formato:** `#,0`

```dax
VAR resultado =
    CALCULATE(
        [base_qtd_manifestacoes],
        KEEPFILTERS(f_relatorio[procedente] = "Sim")
    )
RETURN
    COALESCE(resultado, 0)
```

#### base_qtd_com_recurso

Manifestações finalizadas que geraram ao menos um recurso (campo recurso preenchido).

**Formato:** `#,0`

```dax
VAR resultado =
    CALCULATE(
        [base_qtd_manifestacoes_finalizadas],
        KEEPFILTERS(f_relatorio[recurso] <> BLANK())
    )
RETURN
    COALESCE(resultado, 0)
```

#### ind_pct_procedencia

Percentual de manifestações com análise procedente sobre o total de finalizadas.

**Formato:** `0.00%`

```dax
DIVIDE([base_qtd_procedente], [base_qtd_manifestacoes_finalizadas], 0)
```

#### ind_pct_recurso

Percentual de manifestações que geraram recurso sobre o total de finalizadas. Indicador de retrabalho.

**Formato:** `0.00%`

```dax
DIVIDE([base_qtd_com_recurso], [base_qtd_manifestacoes_finalizadas], 0)
```

#### ind_pct_cobertura_reclamacao

Percentual de Reclamações finalizadas que receberam resposta na pesquisa de satisfação.

**Formato:** `0.00%`

```dax
VAR pesquisas =
    CALCULATE(
        [base_qtd_pesquisa],
        KEEPFILTERS(f_relatorio[tipo_manifestacao] = "Reclamação")
    )
VAR demandas =
    CALCULATE(
        [base_qtd_manifestacoes_finalizadas],
        KEEPFILTERS(f_relatorio[tipo_manifestacao] = "Reclamação")
    )
RETURN
    DIVIDE(pesquisas, demandas, 0)
```


## 04 · Tempo

#### base_qtd_mais_30_dias

Manifestações com mais de 30 dias de vida (dias_vida > 30). Numerador do KRI 1.

**Formato:** `#,0`

```dax
VAR resultado =
    CALCULATE (
        COUNTROWS ( f_relatorio ),
        KEEPFILTERS ( f_relatorio[dias_vida] > 30 )
    )
RETURN
    COALESCE ( resultado, 0 )
```

#### ind_media_tempo_resposta

Média de dias_vida das manifestações. Tempo Médio de Resposta (TMR). Numerador do KRI 2.

**Formato:** `#,0.0`

```dax
VAR resultado =
    AVERAGE ( f_relatorio[dias_vida] )
RETURN
    COALESCE ( resultado, 0 )
```

#### ind_pct_mais_30_dias

Percentual de manifestações com mais de 30 dias de vida sobre o total. Indicador do KRI 1.

**Formato:** `0.00%`

```dax
VAR numerador = [base_qtd_mais_30_dias]
VAR denominador = [base_qtd_manifestacoes]
RETURN
    DIVIDE ( numerador, denominador, 0 )
```

#### base_qtd_manifestacoes_aa

Volume de manifestações no mesmo período do ano anterior. Funciona com qualquer granularidade de dCalendario (dia, mês, quadrimestre).

**Formato:** `#,0`

```dax
VAR _min_data = MIN(dCalendario[Date])
VAR _max_data = MAX(dCalendario[Date])
RETURN
    CALCULATE(
        [base_qtd_manifestacoes],
        FILTER(
            ALL(dCalendario),
            dCalendario[Date] >= DATE(YEAR(_min_data)-1, MONTH(_min_data), DAY(_min_data)) &&
            dCalendario[Date] <= DATE(YEAR(_max_data)-1, MONTH(_max_data), DAY(_max_data))
        )
    )
```

#### ind_tmr_aa

TMR médio no mesmo período do ano anterior. Funciona com qualquer granularidade de dCalendario.

**Formato:** `#,0.0`

```dax
VAR _min_data = MIN(dCalendario[Date])
VAR _max_data = MAX(dCalendario[Date])
RETURN
    CALCULATE(
        [ind_media_tempo_resposta],
        FILTER(
            ALL(dCalendario),
            dCalendario[Date] >= DATE(YEAR(_min_data)-1, MONTH(_min_data), DAY(_min_data)) &&
            dCalendario[Date] <= DATE(YEAR(_max_data)-1, MONTH(_max_data), DAY(_max_data))
        )
    )
```

#### ind_var_pct_volume_aa

Variação percentual do volume de manifestações em relação ao mesmo período do ano anterior.

**Formato:** `+0.0%;-0.0%;0.0%`

```dax
VAR atual = [base_qtd_manifestacoes]
VAR anterior = [base_qtd_manifestacoes_aa]
RETURN DIVIDE(atual - anterior, anterior, BLANK())
```

#### base_qtd_manifestacoes_quadri_anterior

Volume de manifestações no quadrimestre anterior ao período selecionado.

**Formato:** `#,0`

```dax
VAR _quadri_atual =
    SELECTEDVALUE(dCalendario[AnoQuadri])
VAR _ano =
    INT(_quadri_atual / 10)
VAR _q =
    MOD(_quadri_atual, 10)
VAR _q_ant = IF(_q = 1, _ano * 10 - 10 + 3, _ano * 10 + _q - 1)
RETURN
    CALCULATE(
        [base_qtd_manifestacoes],
        FILTER(
            ALL(dCalendario),
            dCalendario[AnoQuadri] = _q_ant
        )
    )
```

#### ind_var_pct_volume_quadri

Variação percentual do volume em relação ao quadrimestre anterior.

**Formato:** `+0.0%;-0.0%;0.0%`

```dax
VAR atual = [base_qtd_manifestacoes]
VAR anterior = [base_qtd_manifestacoes_quadri_anterior]
RETURN DIVIDE(atual - anterior, anterior, BLANK())
```

#### base_qtd_manifestacoes_ytd

Acumulado de manifestações no ano até a data máxima do contexto (YTD).

**Formato:** `#,0`

```dax
CALCULATE(
    [base_qtd_manifestacoes],
    DATESYTD(dCalendario[Date])
)
```

#### ind_media_diaria_manifestacoes

Volume médio diário de manifestações no período selecionado. Útil para comparar períodos de tamanhos diferentes.

**Formato:** `#,0.0`

```dax
VAR _dias =
    COUNTROWS(
        FILTER(
            VALUES(dCalendario[Date]),
            dCalendario[Date] <= MAX(dCalendario[Date])
        )
    )
RETURN DIVIDE([base_qtd_manifestacoes], _dias, 0)
```

#### ind_indice_sazonalidade

Indica se o mês está acima ou abaixo da média mensal do ano. 1.0 = média, >1.0 = pico sazonal, <1.0 = vale. Requer contexto mensal no visual.

**Formato:** `#,0.00`

```dax
VAR _ano_ctx    = MAX(dCalendario[Ano])
VAR _vol_mes    = [base_qtd_manifestacoes]
VAR _soma_ano   = CALCULATE([base_qtd_manifestacoes], FILTER(ALL(dCalendario), dCalendario[Ano] = _ano_ctx))
VAR _media_mes  = DIVIDE(_soma_ano, 12, 1)
RETURN DIVIDE(_vol_mes, _media_mes, 1)
```

#### base_qtd_manifestacoes_dias_uteis

Manifestações registradas em dias úteis (segunda a sexta).

**Formato:** `#,0`

```dax
CALCULATE(
    [base_qtd_manifestacoes],
    dCalendario[DiaUtil] = TRUE()
)
```

#### base_qtd_manifestacoes_fim_semana

Manifestações registradas em fins de semana (sábado e domingo).

**Formato:** `#,0`

```dax
CALCULATE(
    [base_qtd_manifestacoes],
    dCalendario[FimDeSemana] = TRUE()
)
```

#### ind_pct_fim_semana

Percentual do volume registrado fora de dias úteis. Indica pressão sobre canais digitais (Expresso/Webservice) no final de semana.

**Formato:** `0.0%`

```dax
DIVIDE(
    [base_qtd_manifestacoes_fim_semana],
    [base_qtd_manifestacoes],
    0
)
```

#### ind_media_movel_3m

Média móvel de 3 meses do volume de manifestações. Usa janela deslizante de AnoMes. Requer contexto mensal no visual.

**Formato:** `#,0.0`

```dax
VAR _anoMes_max = MAX(dCalendario[AnoMes])
VAR _ano_max    = INT(_anoMes_max / 100)
VAR _mes_max    = MOD(_anoMes_max, 100)
VAR _anoMes_m1  =
    IF(_mes_max >= 2,
        _ano_max * 100 + _mes_max - 1,
        (_ano_max - 1) * 100 + 12)
VAR _anoMes_m2  =
    IF(_mes_max >= 3,
        _ano_max * 100 + _mes_max - 2,
        IF(_mes_max = 2,
            (_ano_max - 1) * 100 + 12,
            (_ano_max - 1) * 100 + 11))
VAR _vol0 = [base_qtd_manifestacoes]
VAR _vol1 = CALCULATE([base_qtd_manifestacoes], FILTER(ALL(dCalendario), dCalendario[AnoMes] = _anoMes_m1))
VAR _vol2 = CALCULATE([base_qtd_manifestacoes], FILTER(ALL(dCalendario), dCalendario[AnoMes] = _anoMes_m2))
RETURN DIVIDE(_vol0 + _vol1 + _vol2, 3, BLANK())
```

#### ind_var_vs_media_movel

Compara o volume do mês atual com a média móvel de 3 meses. Positivo = acima da tendência, negativo = abaixo.

**Formato:** `+0.0%;-0.0%;0.0%`

```dax
VAR _atual = [base_qtd_manifestacoes]
VAR _mm3   = [ind_media_movel_3m]
RETURN DIVIDE(_atual - _mm3, _mm3, BLANK())
```

#### base_qtd_finalizadas_por_data_fin

Volume de manifestações usando a data de finalização como eixo temporal. Requer USERELATIONSHIP com dCalendario[Date] via relacionamento inativo.

**Formato:** `#,0`

```dax
CALCULATE(
    [base_qtd_manifestacoes_finalizadas],
    USERELATIONSHIP(
        f_relatorio[data_finalizacao],
        dCalendario[Date]
    )
)
```


## 05 · IGRO · Metas e Goalposts

#### meta_igro_kri1

Meta canônica do KRI 1 (% RDP): máximo de 2,0% de manifestações com mais de 30 dias.

**Formato:** `0.00%`

```dax
0.02
```

#### goal_igro_kri1

Goalpost canônico do KRI 1 (% RDP): 15,0% como limite de deterioração severa.

**Formato:** `0.00%`

```dax
0.15
```

#### meta_igro_kri2

Meta canônica do KRI 2 (TMR): 10 dias ou menos.

**Formato:** `#,0.0`

```dax
10.0
```

#### goal_igro_kri2

Goalpost canônico do KRI 2 (TMR): 30 dias como limite de deterioração severa.

**Formato:** `#,0.0`

```dax
30.0
```

#### meta_igro_kri3

Meta canônica do KRI 3 (TR - Resolutividade): 70% ou mais.

**Formato:** `0.00%`

```dax
0.70
```

#### goal_igro_kri3

Goalpost canônico do KRI 3 (TR - Resolutividade): 30% como piso de deterioração severa.

**Formato:** `0.00%`

```dax
0.30
```

#### meta_igro_kri4

Meta canônica do KRI 4 (% RI): 2,5% ou inferior.

**Formato:** `0.00%`

```dax
0.025
```

#### goal_igro_kri4

Goalpost canônico do KRI 4 (% RI): 20,0% como deterioração severa.

**Formato:** `0.00%`

```dax
0.20
```

#### meta_igro_kri5

Meta canônica do KRI 5 (Nota de Recomendação): 7,5 ou mais.

**Formato:** `#,0.0`

```dax
7.5
```

#### goal_igro_kri5

Goalpost canônico do KRI 5 (Nota de Recomendação): 4,0 como piso de deterioração severa.

**Formato:** `#,0.0`

```dax
4.0
```

#### flag_amostra_insuficiente

Flag canônica de amostra insuficiente: n_obs < 30 E taxa < 5% das finalizadas identificadas. Denominador exclui manifestações anônimas.

**Formato:** `0`

```dax
VAR n_obs  = [base_qtd_pesquisa]
VAR N_id   = [base_manifestacoes_identificadas]
VAR tx     = DIVIDE(n_obs, N_id, 0)
RETURN
    IF(
        n_obs >= 30 || tx >= 0.05,
        0,
        1
    )
```


## 06 · IGRO · Scores KRI

#### idx_score_igro_kri1

Score canônico de 0 a 1 para o KRI 1 (% RDP): valor 1 quando RDP <= 2,0%; valor 0 quando RDP >= 15,0%.

**Formato:** `0.00%`

```dax
VAR valor = [ind_pct_mais_30_dias]
VAR meta = [meta_igro_kri1]
VAR goalpost = [goal_igro_kri1]
VAR score = DIVIDE ( goalpost - valor, goalpost - meta, 0 )
RETURN
    MIN ( MAX ( score, 0 ), 1 )
```

#### idx_score_igro_kri2

Score canônico de 0 a 1 para o KRI 2 (TMR): valor 1 quando TMR <= 10 dias; valor 0 quando TMR >= 30 dias.

**Formato:** `0.00%`

```dax
VAR valor = [ind_media_tempo_resposta]
VAR meta = [meta_igro_kri2]
VAR goalpost = [goal_igro_kri2]
VAR score = DIVIDE ( goalpost - valor, goalpost - meta, 0 )
RETURN
    MIN ( MAX ( score, 0 ), 1 )
```

#### idx_score_igro_kri3

Score canônico de 0 a 1 para o KRI 3 (TR): valor 1 quando TR >= 70%; valor 0 quando TR <= 30%.

**Formato:** `0.00%`

```dax
VAR valor = [ind_pct_resolutividade]
VAR meta = [meta_igro_kri3]
VAR goalpost = [goal_igro_kri3]
VAR score = DIVIDE ( valor - goalpost, meta - goalpost, 0 )
VAR amostra_insuficiente = [flag_amostra_insuficiente] = 1
RETURN
    IF (
        amostra_insuficiente,
        BLANK(),
        MIN ( MAX ( score, 0 ), 1 )
    )
```

#### idx_score_igro_kri4

Score canônico de 0 a 1 para o KRI 4 (% RI): valor 1 quando RI <= 2,5%; valor 0 quando RI >= 20,0%.

**Formato:** `0.00%`

```dax
VAR valor = [ind_pct_respostas_insatisfatorias]
VAR meta = [meta_igro_kri4]
VAR goalpost = [goal_igro_kri4]
VAR score = DIVIDE ( goalpost - valor, goalpost - meta, 0 )
RETURN
    MIN ( MAX ( score, 0 ), 1 )
```

#### idx_score_igro_kri5

Score canônico de 0 a 1 para o KRI 5 (Nota de Recomendação): valor 1 quando NR >= 7,5; valor 0 quando NR <= 4,0.

**Formato:** `0.00%`

```dax
VAR valor = [ind_media_nota_recomendacao]
VAR meta = [meta_igro_kri5]
VAR goalpost = [goal_igro_kri5]
VAR score = DIVIDE ( valor - goalpost, meta - goalpost, 0 )
VAR amostra_insuficiente = [flag_amostra_insuficiente] = 1
RETURN
    IF (
        amostra_insuficiente,
        BLANK(),
        MIN ( MAX ( score, 0 ), 1 )
    )
```


## 07 · IGRO · Índice

#### idx_igro_sub_t

Subíndice canônico de Tempestividade (Sub-T): pesos globais KRI 1=15% e KRI 2=25%.

**Formato:** `0.00%`

```dax
VAR numerador =
    0.15 * [idx_score_igro_kri1]
        + 0.25 * [idx_score_igro_kri2]
VAR resultado =
    DIVIDE ( numerador, 0.40, 0 )
RETURN
    MIN ( MAX ( resultado, 0 ), 1 )
```

#### idx_igro_sub_q

Subíndice canônico de Qualidade (Sub-Q): pesos globais KRI 3=25%, KRI 4=15% e KRI 5=20%.

**Formato:** `0.00%`

```dax
VAR numerador =
    0.25 * [idx_score_igro_kri3]
        + 0.15 * [idx_score_igro_kri4]
        + 0.20 * [idx_score_igro_kri5]
VAR resultado =
    DIVIDE ( numerador, 0.60, 0 )
VAR amostra_insuficiente = [flag_amostra_insuficiente] = 1
RETURN
    IF (
        amostra_insuficiente,
        BLANK(),
        MIN ( MAX ( resultado, 0 ), 1 )
    )
```

#### idx_igro

Índice canônico de Gestão de Riscos de Ouvidorias: média geométrica ponderada Sub-T^0,40 × Sub-Q^0,60.

**Formato:** `0.00%`

```dax
VAR sub_t = [idx_igro_sub_t]
VAR sub_q = [idx_igro_sub_q]
VAR resultado =
    IF (
        OR ( ISBLANK ( sub_t ), ISBLANK ( sub_q ) ),
        BLANK(),
        POWER ( sub_t, 0.40 ) * POWER ( sub_q, 0.60 )
    )
RETURN
    IF ( ISBLANK ( resultado ), BLANK(), MIN ( MAX ( resultado, 0 ), 1 ) )
```


## 08 · Formatação

#### fmt_semaforo_nps

Rótulo de semáforo para o NPS: Verde (≥50), Amarelo (0–49), Laranja (-49 a -1), Vermelho (<-50).

```dax
VAR v = [ind_nps]
RETURN
    SWITCH(
        TRUE(),
        v >= 50,  "Verde — Excelente",
        v >= 0,   "Amarelo — Razonável",
        v >= -50, "Laranja — Ruim",
        "Vermelho — Crítico"
    )
```

#### fmt_cor_fundo_nps

Cor de fundo hexadecimal para o NPS conforme faixa.

```dax
VAR v = [ind_nps]
RETURN
    SWITCH(
        TRUE(),
        v >= 50,  "#EAF3DE",
        v >= 0,   "#FAEEDA",
        v >= -50, "#FAECE7",
        "#FCEBEB"
    )
```

#### fmt_cor_fonte_nps

Cor de fonte hexadecimal para o NPS conforme faixa.

```dax
VAR v = [ind_nps]
RETURN
    SWITCH(
        TRUE(),
        v >= 50,  "#27500A",
        v >= 0,   "#633806",
        v >= -50, "#712B13",
        "#791F1F"
    )
```

#### fmt_semaforo_procedencia

Rótulo de semáforo para ind_pct_procedencia: Verde (≥60%), Amarelo (40–59%), Laranja (20–39%), Vermelho (<20%).

```dax
VAR v = [ind_pct_procedencia]
RETURN
    SWITCH(
        TRUE(),
        v >= 0.60, "Verde — Alta",
        v >= 0.40, "Amarelo — Média",
        v >= 0.20, "Laranja — Baixa",
        "Vermelho — Muito baixa"
    )
```

#### fmt_semaforo_recurso

Rótulo de semáforo para ind_pct_recurso: Verde (≤1%), Amarelo (1–3%), Laranja (3–5%), Vermelho (>5%).

```dax
VAR v = [ind_pct_recurso]
RETURN
    SWITCH(
        TRUE(),
        v <= 0.01, "Verde — Baixo",
        v <= 0.03, "Amarelo — Moderado",
        v <= 0.05, "Laranja — Alto",
        "Vermelho — Crítico"
    )
```

#### fmt_semaforo_igro

Rótulo de semáforo canônico para o IGRO: Verde (>=80%), Amarelo (60–79%), Laranja (40–59%), Vermelho (<40%).

**Formato:** `@`

```dax
VAR v = [idx_igro]
RETURN
    IF ( ISBLANK(v), BLANK(),
    IF ( v >= 0.80, "Risco Baixo",
    IF ( v >= 0.60, "Risco Moderado",
    IF ( v >= 0.40, "Risco Alto", "Risco Crítico" ))))
```

#### fmt_semaforo_igro_sub_t

Rótulo de semáforo canônico para o Sub-T: Verde (>=80%), Amarelo (60–79%), Laranja (40–59%), Vermelho (<40%).

**Formato:** `@`

```dax
VAR v = [idx_igro_sub_t]
RETURN
    IF ( ISBLANK(v), BLANK(),
    IF ( v >= 0.80, "Risco Baixo",
    IF ( v >= 0.60, "Risco Moderado",
    IF ( v >= 0.40, "Risco Alto", "Risco Crítico" ))))
```

#### fmt_semaforo_igro_sub_q

Rótulo de semáforo canônico para o Sub-Q: Verde (>=80%), Amarelo (60–79%), Laranja (40–59%), Vermelho (<40%).

**Formato:** `@`

```dax
VAR v = [idx_igro_sub_q]
RETURN
    IF ( ISBLANK(v), BLANK(),
    IF ( v >= 0.80, "Risco Baixo",
    IF ( v >= 0.60, "Risco Moderado",
    IF ( v >= 0.40, "Risco Alto", "Risco Crítico" ))))
```

#### fmt_cor_fundo_igro

Cor de fundo canônica para o IGRO: Risco Baixo=#EAF3DE, Moderado=#FAEEDA, Alto=#FAECE7, Crítico=#FCEBEB.

**Formato:** `@`

```dax
VAR v = [idx_igro]
RETURN
    IF ( ISBLANK(v), BLANK(),
    IF ( v >= 0.80, "#EAF3DE",
    IF ( v >= 0.60, "#FAEEDA",
    IF ( v >= 0.40, "#FAECE7", "#FCEBEB" ))))
```

#### fmt_cor_fonte_igro

Cor de fonte hexadecimal para o IGRO conforme faixa de risco. Usar em formatação condicional de cor de fonte.

```dax
VAR v = [idx_igro]
RETURN SWITCH(TRUE(), v >= 0.80, "#27500A", v >= 0.60, "#633806", v >= 0.40, "#712B13", "#791F1F")
```

#### fmt_cor_fundo_igro_sub_t

Cor de fundo canônica para o Sub-T.

**Formato:** `@`

```dax
VAR v = [idx_igro_sub_t]
RETURN
    IF ( ISBLANK(v), BLANK(),
    IF ( v >= 0.80, "#EAF3DE",
    IF ( v >= 0.60, "#FAEEDA",
    IF ( v >= 0.40, "#FAECE7", "#FCEBEB" ))))
```

#### fmt_cor_fundo_igro_sub_q

Cor de fundo canônica para o Sub-Q.

**Formato:** `@`

```dax
VAR v = [idx_igro_sub_q]
RETURN
    IF ( ISBLANK(v), BLANK(),
    IF ( v >= 0.80, "#EAF3DE",
    IF ( v >= 0.60, "#FAEEDA",
    IF ( v >= 0.40, "#FAECE7", "#FCEBEB" ))))
```


## 09 · Variação

#### var_tmr

Variação absoluta do TMR vs. período anterior. Negativo = melhora (menos dias).

**Formato:** `#,0.0`

```dax
VAR atual = [ind_media_tempo_resposta]
VAR anterior = CALCULATE([ind_media_tempo_resposta], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

#### var_pct_mais_30_dias

Variação absoluta do % de manifestações com mais de 30 dias vs. período anterior. Negativo = melhora.

**Formato:** `0.00%`

```dax
VAR atual = [ind_pct_mais_30_dias]
VAR anterior = CALCULATE([ind_pct_mais_30_dias], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

#### var_resolutividade

Variação absoluta da resolutividade vs. período anterior. Positivo = melhora.

**Formato:** `0.00%`

```dax
VAR atual = [ind_pct_resolutividade]
VAR anterior = CALCULATE([ind_pct_resolutividade], PREVIOUSYEAR(f_pesquisa[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

#### var_insatisfatorias

Variação absoluta do % de respostas insatisfatórias vs. período anterior. Negativo = melhora. Eixo temporal via dCalendario (corrigido).

**Formato:** `0.00%`

```dax
VAR atual = [ind_pct_respostas_insatisfatorias]
VAR _min_data = MIN(dCalendario[Date])
VAR _max_data = MAX(dCalendario[Date])
VAR anterior =
    CALCULATE(
        [ind_pct_respostas_insatisfatorias],
        FILTER(
            ALL(dCalendario),
            dCalendario[Date] >= DATE(YEAR(_min_data)-1, MONTH(_min_data), DAY(_min_data)) &&
            dCalendario[Date] <= DATE(YEAR(_max_data)-1, MONTH(_max_data), DAY(_max_data))
        )
    )
RETURN
    IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

#### var_nota

Variação absoluta da nota média de recomendação vs. período anterior. Positivo = melhora.

**Formato:** `#,0.0`

```dax
VAR atual = [ind_media_nota_recomendacao]
VAR anterior = CALCULATE([ind_media_nota_recomendacao], PREVIOUSYEAR(f_pesquisa[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

#### var_nps

Variação absoluta do NPS vs. período anterior. Positivo = melhora.

**Formato:** `#,0.0`

```dax
VAR atual = [ind_nps]
VAR anterior = CALCULATE([ind_nps], PREVIOUSYEAR(f_pesquisa[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

#### var_igro

Variação absoluta do IGRO vs. período anterior. Positivo = melhora.

**Formato:** `0.00%`

```dax
VAR atual = [idx_igro]
VAR anterior = CALCULATE([idx_igro], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

#### var_igro_sub_t

Variação absoluta do Sub-T vs. período anterior. Positivo = melhora.

**Formato:** `0.00%`

```dax
VAR atual = [idx_igro_sub_t]
VAR anterior = CALCULATE([idx_igro_sub_t], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

#### var_igro_sub_q

Variação absoluta do Sub-Q vs. período anterior. Positivo = melhora.

**Formato:** `0.00%`

```dax
VAR atual = [idx_igro_sub_q]
VAR anterior = CALCULATE([idx_igro_sub_q], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

#### var_recurso

Variação absoluta do % de recurso vs. período anterior. Negativo = melhora.

**Formato:** `0.00%`

```dax
VAR atual = [ind_pct_recurso]
VAR anterior = CALCULATE([ind_pct_recurso], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

#### var_cobertura_reclamacao

Variação absoluta da cobertura de pesquisa em Reclamações vs. período anterior. Positivo = melhora.

**Formato:** `0.00%`

```dax
VAR atual = [ind_pct_cobertura_reclamacao]
VAR anterior = CALCULATE([ind_pct_cobertura_reclamacao], PREVIOUSYEAR(f_pesquisa[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```


## 10 · Semáforo · Variação

#### sem_tmr

Semáforo do TMR com polaridade negativa: verde quando cai (melhora), vermelho quando sobe (piora). Neutro quando variação = 0 ou BLANK.

```dax
VAR delta = [var_tmr]
VAR polaridade = -1
RETURN
    IF(
        ISBLANK(delta), "⏸️",
        IF(delta = 0, "⏹️",
            IF(delta * polaridade > 0, "🟢", "🔴")
        )
    )
```

#### sem_pct_mais_30_dias

Semáforo do % +30 dias com polaridade negativa: verde quando cai.

```dax
VAR delta = [var_pct_mais_30_dias]
VAR polaridade = -1
RETURN
    IF(
        ISBLANK(delta), "⏸️",
        IF(delta = 0, "⏹️",
            IF(delta * polaridade > 0, "🟢", "🔴")
        )
    )
```

#### sem_resolutividade

Semáforo da resolutividade com polaridade positiva: verde quando sobe.

```dax
VAR delta = [var_resolutividade]
VAR polaridade = 1
RETURN
    IF(
        ISBLANK(delta), "⏸️",
        IF(delta = 0, "⏹️",
            IF(delta * polaridade > 0, "🟢", "🔴")
        )
    )
```

#### sem_insatisfatorias

Semáforo das respostas insatisfatórias com polaridade negativa: verde quando cai.

```dax
VAR delta = [var_insatisfatorias]
VAR polaridade = -1
RETURN
    IF(
        ISBLANK(delta), "⏸️",
        IF(delta = 0, "⏹️",
            IF(delta * polaridade > 0, "🟢", "🔴")
        )
    )
```

#### sem_nota

Semáforo da nota média com polaridade positiva: verde quando sobe.

```dax
VAR delta = [var_nota]
VAR polaridade = 1
RETURN
    IF(
        ISBLANK(delta), "⏸️",
        IF(delta = 0, "⏹️",
            IF(delta * polaridade > 0, "🟢", "🔴")
        )
    )
```

#### sem_nps

Semáforo do NPS com polaridade positiva: verde quando sobe.

```dax
VAR delta = [var_nps]
VAR polaridade = 1
RETURN
    IF(
        ISBLANK(delta), "⏸️",
        IF(delta = 0, "⏹️",
            IF(delta * polaridade > 0, "🟢", "🔴")
        )
    )
```

#### sem_igro

Semáforo do IGRO com polaridade positiva: verde quando sobe.

```dax
VAR delta = [var_igro]
VAR polaridade = 1
RETURN
    IF(
        ISBLANK(delta), "⏸️",
        IF(delta = 0, "⏹️",
            IF(delta * polaridade > 0, "🟢", "🔴")
        )
    )
```

#### sem_igro_sub_t

Semáforo do Sub-T com polaridade positiva.

```dax
VAR delta = [var_igro_sub_t]
VAR polaridade = 1
RETURN
    IF(
        ISBLANK(delta), "⏸️",
        IF(delta = 0, "⏹️",
            IF(delta * polaridade > 0, "🟢", "🔴")
        )
    )
```

#### sem_igro_sub_q

Semáforo do Sub-Q com polaridade positiva.

```dax
VAR delta = [var_igro_sub_q]
VAR polaridade = 1
RETURN
    IF(
        ISBLANK(delta), "⏸️",
        IF(delta = 0, "⏹️",
            IF(delta * polaridade > 0, "🟢", "🔴")
        )
    )
```

#### sem_recurso

Semáforo do % de recurso com polaridade negativa: verde quando cai.

```dax
VAR delta = [var_recurso]
VAR polaridade = -1
RETURN
    IF(
        ISBLANK(delta), "⏸️",
        IF(delta = 0, "⏹️",
            IF(delta * polaridade > 0, "🟢", "🔴")
        )
    )
```

#### sem_cobertura_reclamacao

Semáforo da cobertura de pesquisa em Reclamações com polaridade positiva: verde quando sobe.

```dax
VAR delta = [var_cobertura_reclamacao]
VAR polaridade = 1
RETURN
    IF(
        ISBLANK(delta), "⏸️",
        IF(delta = 0, "⏹️",
            IF(delta * polaridade > 0, "🟢", "🔴")
        )
    )
```


## 11 · Rótulo · Cartão

#### lbl_tmr

Rótulo completo para cartão do TMR: valor atual + semáforo + delta formatado.

```dax
VAR valor = [ind_media_tempo_resposta]
VAR delta = [var_tmr]
VAR emoji = [sem_tmr]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0") & "d)")
RETURN
    emoji & " " & FORMAT(valor, "0.0") & "d" & delta_fmt
```

#### lbl_pct_mais_30_dias

Rótulo completo para cartão do % +30 dias.

```dax
VAR valor = [ind_pct_mais_30_dias]
VAR delta = [var_pct_mais_30_dias]
VAR emoji = [sem_pct_mais_30_dias]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
    emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```

#### lbl_resolutividade

Rótulo completo para cartão da resolutividade.

```dax
VAR valor = [ind_pct_resolutividade]
VAR delta = [var_resolutividade]
VAR emoji = [sem_resolutividade]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
    emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```

#### lbl_insatisfatorias

Rótulo completo para cartão das respostas insatisfatórias.

```dax
VAR valor = [ind_pct_respostas_insatisfatorias]
VAR delta = [var_insatisfatorias]
VAR emoji = [sem_insatisfatorias]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
    emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```

#### lbl_nota

Rótulo completo para cartão da nota média.

```dax
VAR valor = [ind_media_nota_recomendacao]
VAR delta = [var_nota]
VAR emoji = [sem_nota]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0") & ")")
RETURN
    emoji & " " & FORMAT(valor, "0.0") & delta_fmt
```

#### lbl_nps

Rótulo completo para cartão do NPS.

```dax
VAR valor = [ind_nps]
VAR delta = [var_nps]
VAR emoji = [sem_nps]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0") & ")")
VAR sinal_valor = IF(valor > 0, "+", "")
RETURN
    emoji & " " & sinal_valor & FORMAT(valor, "0.0") & delta_fmt
```

#### lbl_igro

Rótulo completo para cartão do IGRO.

```dax
VAR valor = [idx_igro]
VAR delta = [var_igro]
VAR emoji = [sem_igro]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
    emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```

#### lbl_igro_sub_t

Rótulo completo para cartão do Sub-T.

```dax
VAR valor = [idx_igro_sub_t]
VAR delta = [var_igro_sub_t]
VAR emoji = [sem_igro_sub_t]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
    emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```

#### lbl_igro_sub_q

Rótulo completo para cartão do Sub-Q.

```dax
VAR valor = [idx_igro_sub_q]
VAR delta = [var_igro_sub_q]
VAR emoji = [sem_igro_sub_q]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
    emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```


## 12 · JSON · Dashboard

#### _JSON Orgaos

Array JSON com IGRO e KRIs por órgão, ordenado por IGRO desc. Usa SUMMARIZE com colunas calculadas.

```dax
VAR _t =
    ADDCOLUMNS(
        SUMMARIZE(f_relatorio, f_relatorio[sigla]),
        "_qtd",   [base_qtd_manifestacoes],
        "_igro",  [idx_igro],
        "_sub_t", [idx_igro_sub_t],
        "_sub_q", [idx_igro_sub_q],
        "_tmr",   [ind_media_tempo_resposta],
        "_res",   [ind_pct_resolutividade],
        "_nota",  [ind_media_nota_recomendacao],
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### _JSON Tipos

Array JSON com distribuição por tipo de manifestação.

```dax
VAR _tot = [base_qtd_manifestacoes]
VAR _t =
    ADDCOLUMNS(
        SUMMARIZE(f_relatorio, f_relatorio[tipo_manifestacao]),
        "_qtd",  [base_qtd_manifestacoes],
        "_ins",  [base_qtd_respostas_insatisfatorias],
        "_pesq", [base_qtd_pesquisa]
    )
VAR _s = TOPN(10, _t, [_qtd], DESC)
RETURN
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### _JSON KPIs

Array JSON com KPIs globais da rede para injeção direta nos cards do dashboard.

```dax
VAR _igro  = SUBSTITUTE(FORMAT([idx_igro], "0.0000"), ",", ".")
VAR _sub_t = SUBSTITUTE(FORMAT([idx_igro_sub_t], "0.0000"), ",", ".")
VAR _sub_q = SUBSTITUTE(FORMAT([idx_igro_sub_q], "0.0000"), ",", ".")
VAR _tmr   = SUBSTITUTE(FORMAT([ind_media_tempo_resposta], "0.00"), ",", ".")
VAR _res   = SUBSTITUTE(FORMAT([ind_pct_resolutividade], "0.0000"), ",", ".")
VAR _nota  = SUBSTITUTE(FORMAT([ind_media_nota_recomendacao], "0.00"), ",", ".")
VAR _ins   = SUBSTITUTE(FORMAT([ind_pct_respostas_insatisfatorias], "0.0000"), ",", ".")
VAR _nps   = SUBSTITUTE(FORMAT([ind_nps], "0.00"), ",", ".")
VAR _p30   = SUBSTITUTE(FORMAT([ind_pct_mais_30_dias], "0.0000"), ",", ".")
VAR _tot   = SUBSTITUTE(FORMAT([base_qtd_manifestacoes], "0"), ",", ".")
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### HTML Dashboard IGRO

Dashboard HTML interativo do IGRO. Tema dark, cards KPI, ranking de órgãos, distribuição por tipo, tabela com busca e export CSV.

```dax
VAR _sc = "scr" & "ipt"
VAR _scx = "/scr" & "ipt"

VAR _css =
"<style>" &
"*{box-sizing:border-box;margin:0;padding:0;font-family:'Segoe UI',sans-serif}" &
"body{background:#0d0d0d;color:#e5e7eb;padding:10px}" &
".topbar{display:flex;align-items:center;gap:8px;margin-bottom:10px;flex-wrap:wrap}" &
".topbar h1{font-size:14px;font-weight:600;flex:1;color:#f9fafb}" &
"select,button{background:#1c1c1e;color:#e5e7eb;border:1px solid #333;border-radius:5px;padding:4px 10px;font-size:11px;cursor:pointer}" &
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### HTML Dashboard Final Base

Dashboard HTML IGRO·NPS v3 — corrige JSON inválido (ano nulo) e filtra anos sem dados.

```dax
VAR _F4 = "0.0000"
VAR _F2 = "0.00"
VAR _F0 = "0"
VAR _Q = """"
VAR _c = ","
VAR _d = "."
VAR _sc = "scr" & "ipt"
VAR _scx = "/scr" & "ipt"

VAR _nps = IF ( ISBLANK ( [ind_nps] ), 0, [ind_nps] )
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### HTML Matriz Classes IGRO

Matriz HTML por Classe IGRO v8 - texto da tabela em branco para melhor contraste.

```dax
VAR _tbl =
    ADDCOLUMNS(
        FILTER(
            SUMMARIZE(
                dOrgao_igro,
                dOrgao_igro[Classe],
                dOrgao_igro[Tipo],
                dOrgao_igro[sigla]
            ),
            dOrgao_igro[Tipo] <> "Inativa"
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### HTML Dashboard Final Fonte Branca

Versão do Dashboard Final com override de CSS para fonte branca em textos que apareciam pretos.

```dax
[HTML Dashboard Final Base]
    & "<style>"
    & "body,.dash,.card,.card span,.card b,.donut-leg,.donut-leg span,.donut-leg b,.leg-item,.bar-label,.bar-label span,.sub b,.ctx-badge{color:#e2e8f0!important;}"
    & ".card .sub,.ksub,.lbl,.fbar label{color:#b8cad1!important;}"
    & ".bar-label span[id],#bar-p,#bar-n,#bar-d,#nota-v,#lg-p,#lg-n,#lg-d,#qtd-t,#tot-v{color:#ffffff!important;}"
    & "</style>"
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### HTML Dashboard Final

Dashboard HTML IGRO·NPS com badge dinamica de classificacao no cartao IGRO, filtros preservados, gauge NPS e distribuicao premium.

```dax
VAR _html0 = [HTML Dashboard Final Base]
VAR _oldIg = "<div class='ig-main'><div class='lbl'>IGRO</div><div class='ig-val' id='ig-val'>--</div><div class='ig-bar'><div class='ig-fill' id='ig-bl' style='width:0'></div></div></div>"
VAR _newIg = "<div class='ig-main ig-card-main'><div class='ig-card-top'><div class='lbl'>IGRO</div><div class='ig-badge' id='ig-badge'>--</div></div><div class='ig-val' id='ig-val'>--</div><div class='ig-bar'><div class='ig-fill' id='ig-bl' style='width:0'></div></div></div>"
VAR _oldNps = "<div class='card accent'><div class='lbl'>NPS &#183; &#205;ndice de Satisfa&#231;&#227;o</div><div class='big' id='nps-v' style='color:#f2c94c'>--</div><div class='sub'>Respostas: <b id='qtd-t'>--</b> &nbsp;|&nbsp; Manifesta&#231;&#245;es: <b id='tot-v'>--</b></div><div class='vr neu' id='nps-var'>--</div></div>"
VAR _newNps = "<div class='card nps-alt'><div><div class='lbl'>NPS &#183; &#205;ndice de Satisfa&#231;&#227;o</div><div class='nps-copy'>Mede o quanto os usuarios estao dispostos a recomendar o servico. O resultado varia de baixo a alto: quanto maior o NPS, maior a satisfacao e a confianca no servico.</div><div class='nps-gauge'><svg viewBox='0 0 320 190' role='img' aria-label='Velocimetro NPS'><path class='arc arc-low' d='M 40 160 A 120 120 0 0 1 160 40'/><path class='arc arc-mid' d='M 160 40 A 120 120 0 0 1 244.9 75.1'/><path class='arc arc-high' d='M 244.9 75.1 A 120 120 0 0 1 280 160'/><line class='tick' x1='40' y1='160' x2='28' y2='160'/><line class='tick' x1='160' y1='40' x2='160' y2='27'/><line class='tick' x1='280' y1='160' x2='292' y2='160'/><line class='needle' id='nps-needle' x1='160' y1='160' x2='160' y2='76'/><circle class='hub' cx='160' cy='160' r='10'/></svg></div><div class='legend-inline'><span class='lg'><i class='dot low'></i>Baixo</span><span class='lg'><i class='dot mid'></i>Medio</span><span class='lg'><i class='dot high'></i>Alto</span></div></div><div class='nps-side'><div class='bands'><b>Baixo</b><span>-100 a -1</span><b>Medio</b><span>0 a 49</span><b>Alto</b><span>50 a 100</span></div><div><div class='hero-score' id='nps-v'>--</div><div class='score-caption'>Net Promoter<br>Score</div></div><div class='micro'>Faixa atual: <b id='nps-band'>--</b><br>Respostas: <b id='qtd-t'>--</b><br>Manifesta&#231;&#245;es: <b id='tot-v'>--</b><br><span class='vr neu' id='nps-var'>--</span></div></div></div>"
VAR _oldDist = "<div class='card'><div class='lbl'>Distribui&#231;&#227;o de Respondentes</div><div class='bar-wrap'><div class='bar-label'><span style='color:#10b981'>Promotores</span><span id='bar-p'>--</span></div><div class='bar-track'><div class='bar-fill fp' id='bar-p-c' style='width:0'></div></div></div><div class='bar-wrap'><div class='bar-label'><span style='color:#94a3b8'>Neutros</span><span id='bar-n'>--</span></div><div class='bar-track'><div class='bar-fill fn' id='bar-n-c' style='width:0'></div></div></div><div class='bar-wrap'><div class='bar-label'><span style='color:#ef4444'>Detratores</span><span id='bar-d'>--</span></div><div class='bar-track'><div class='bar-fill fd' id='bar-d-c' style='width:0'></div></div></div><div class='sub' style='margin-top:8px'>Nota m&#233;dia: <b id='nota-v'>--</b></div></div>"
VAR _newDist = "<div class='card dist-card'><div class='dist-head'><div class='lbl'>Distribui&#231;&#227;o de Respondentes</div><div class='score-chip'>NPS <span id='dist-nps'>--</span></div></div><div class='dist-premium'><div class='donut-wrap2'><svg viewBox='0 0 100 100' width='128' height='128'><circle cx='50' cy='50' r='45' fill='none' stroke='#132a2d' stroke-width='12'/><circle id='sa-p' cx='50' cy='50' r='45' fill='none' stroke='#10b981' stroke-width='12' stroke-dasharray='0 283' stroke-dashoffset='0' transform='rotate(-90 50 50)'/><circle id='sa-n' cx='50' cy='50' r='45' fill='none' stroke='#94a3b8' stroke-width='12' stroke-dasharray='0 283' stroke-dashoffset='0' transform='rotate(-90 50 50)'/><circle id='sa-d' cx='50' cy='50' r='45' fill='none' stroke='#ef4444' stroke-width='12' stroke-dasharray='0 283' stroke-dashoffset='0' transform='rotate(-90 50 50)'/><circle cx='50' cy='50' r='28' fill='#0b292d'/><text x='50' y='42' text-anchor='middle' class='dn-label'>NPS</text><text x='50' y='60' text-anchor='middle' class='dn-value' id='dist-nps-2'>--</text></svg><div class='donut-total'><b id='dist-q'>--</b> pesquisas</div></div><div><div class='dist-row'><div class='barlabel'><span class='dist-name'><i class='sw prom'></i>Promotores</span><b class='pct-pill' id='bar-p'>--</b></div><div class='bartrack'><div class='barfill prom-fill' id='bar-p-c' style='width:0'></div></div></div><div class='dist-row'><div class='barlabel'><span class='dist-name'><i class='sw neut'></i>Neutros</span><b class='pct-pill' id='bar-n'>--</b></div><div class='bartrack'><div class='barfill neut-fill' id='bar-n-c' style='width:0'></div></div></div><div class='dist-row'><div class='barlabel'><span class='dist-name'><i class='sw det'></i>Detratores</span><b class='pct-pill' id='bar-d'>--</b></div><div class='bartrack'><div class='barfill det-fill' id='bar-d-c' style='width:0'></div></div></div><div class='note-row'><span>Nota media</span><b class='note-value' id='nota-v'>--</b></div><div class='survey-total'>Total de pesquisas: <b id='dist-q2'>--</b></div><div style='display:none'><span id='lg-p'></span><span id='lg-n'></span><span id='lg-d'></span></div></div></div></div>"
VAR _oldComp = "<div class='card full'><div class='lbl'>Composi&#231;&#227;o NPS</div><div class='donut-wrap'><svg id='svg-nps' viewBox='0 0 100 100' width='150' height='150'><circle cx='50' cy='50' r='45' fill='none' stroke='#132a2d' stroke-width='10'/><circle id='sa-p' cx='50' cy='50' r='45' fill='none' stroke='#10b981' stroke-width='10' stroke-dasharray='0 283' stroke-dashoffset='0' transform='rotate(-90 50 50)'/><circle id='sa-n' cx='50' cy='50' r='45' fill='none' stroke='#94a3b8' stroke-width='10' stroke-dasharray='0 283' stroke-dashoffset='0' transform='rotate(-90 50 50)'/><circle id='sa-d' cx='50' cy='50' r='45' fill='none' stroke='#ef4444' stroke-width='10' stroke-dasharray='0 283' stroke-dashoffset='0' transform='rotate(-90 50 50)'/></svg><div class='donut-leg'><div class='leg-item'><div class='leg-dot' style='background:#10b981'></div><span>Promotores: <b id='lg-p'>--</b></span></div><div class='leg-item'><div class='leg-dot' style='background:#94a3b8'></div><span>Neutros: <b id='lg-n'>--</b></span></div><div class='leg-item'><div class='leg-dot' style='background:#ef4444'></div><span>Detratores: <b id='lg-d'>--</b></span></div></div></div></div>"
VAR _newComp = "<div class='card full radar-card'><div><div class='lbl'>Radar dos KRIs</div><div class='radar-wrap'><svg viewBox='0 0 240 220' width='280' height='250' role='img' aria-label='Radar dos KRIs'><polygon class='radar-grid' points='120,86 138,99 131,120 109,120 102,99'/><polygon class='radar-grid' points='120,67 156,93 143,136 97,136 84,93'/><polygon class='radar-grid' points='120,48 174,87 154,151 86,151 66,87'/><polygon class='radar-grid' points='120,29 192,82 165,166 75,166 48,82'/><line class='radar-axis' x1='120' y1='105' x2='120' y2='29'/><line class='radar-axis' x1='120' y1='105' x2='192' y2='82'/><line class='radar-axis' x1='120' y1='105' x2='165' y2='166'/><line class='radar-axis' x1='120' y1='105' x2='75' y2='166'/><line class='radar-axis' x1='120' y1='105' x2='48' y2='82'/><polygon class='radar-poly' id='ra-poly' points='120,105 120,105 120,105 120,105 120,105'/><circle class='radar-dot' id='ra-1' cx='120' cy='105' r='4'/><circle class='radar-dot' id='ra-2' cx='120' cy='105' r='4'/><circle class='radar-dot' id='ra-3' cx='120' cy='105' r='4'/><circle class='radar-dot' id='ra-4' cx='120' cy='105' r='4'/><circle class='radar-dot' id='ra-5' cx='120' cy='105' r='4'/><text class='radar-label' x='111' y='18'>KRI 1</text><text class='radar-label' x='196' y='82'>KRI 2</text><text class='radar-label' x='158' y='186'>KRI 3</text><text class='radar-label' x='48' y='186'>KRI 4</text><text class='radar-label' x='17' y='82'>KRI 5</text></svg></div></div><div class='kr-list'><div class='kr'><div class='kr-name'>KRI 1 | +30 DIAS</div><div class='kr-score' id='rk1'>--</div><div class='kr-real' id='rv1'>Atual: --</div></div><div class='kr'><div class='kr-name'>KRI 2 | TMR</div><div class='kr-score' id='rk2'>--</div><div class='kr-real' id='rv2'>Atual: --</div></div><div class='kr'><div class='kr-name'>KRI 3 | RESOLUTIVIDADE</div><div class='kr-score' id='rk3'>--</div><div class='kr-real' id='rv3'>Atual: --</div></div><div class='kr'><div class='kr-name'>KRI 4 | INSATISFATORIAS</div><div class='kr-score' id='rk4'>--</div><div class='kr-real' id='rv4'>Atual: --</div></div><div class='kr'><div class='kr-name'>KRI 5 | NOTA</div><div class='kr-score' id='rk5'>--</div><div class='kr-real' id='rv5'>Atual: --</div></div></div></div>"
VAR _htmlIg = SUBSTITUTE ( _html0, _oldIg, _newIg )
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### HTML Tabela Resultados IGRO CSV

Tabela/matriz HTML com dados em literal JS, filtros e exportação CSV dos resultados calculados por órgão.

```dax
VAR _q = "'"
VAR _tbl =
    ADDCOLUMNS(
        FILTER(
            SUMMARIZE(
                dOrgao_igro,
                dOrgao_igro[sigla],
                dOrgao_igro[Tipo],
                dOrgao_igro[Grupo],
                dOrgao_igro[Classe]
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### HTML Dashboard Final Backup

Backup estatico da medida HTML Dashboard Final antes da substituicao do card NPS mantendo filtros.

```dax
[HTML Dashboard Final Base]
    & "<style>"
    & "body,.dash,.card,.card span,.card b,.donut-leg,.donut-leg span,.donut-leg b,.leg-item,.bar-label,.bar-label span,.sub b,.ctx-badge{color:#e2e8f0!important;}"
    & ".card .sub,.ksub,.lbl,.fbar label{color:#b8cad1!important;}"
    & ".bar-label span[id],#bar-p,#bar-n,#bar-d,#nota-v,#lg-p,#lg-n,#lg-d,#qtd-t,#tot-v{color:#ffffff!important;}"
    & "</style>"
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### HTML Infografico IGRO

Infografico HTML do IGRO com cabecalho institucional, resumo hierarquico e grade acessivel de KRIs.

```dax
VAR _igro = [idx_igro]
VAR _subT = [idx_igro_sub_t]
VAR _subQ = [idx_igro_sub_q]
VAR _kri1 = [ind_pct_mais_30_dias]
VAR _kri2 = [ind_media_tempo_resposta]
VAR _kri3 = [ind_pct_resolutividade]
VAR _kri4 = [ind_pct_respostas_insatisfatorias]
VAR _kri5 = [ind_media_nota_recomendacao]
VAR _s1 = [idx_score_igro_kri1]
VAR _s2 = [idx_score_igro_kri2]
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### HTML Infografico IGRO Simplificado

[Papel: Técnico] Coluna dummy criada para viabilizar a tabela calculada _medidas. Não possui significado analítico e não deve ser usada em visuais.

```dax
VAR _igro = COALESCE([idx_igro], 0)
VAR _subT = COALESCE([idx_igro_sub_t], 0)
VAR _subQ = COALESCE([idx_igro_sub_q], 0)
VAR _kri1 = COALESCE([ind_pct_mais_30_dias], 0)
VAR _kri2 = COALESCE([ind_media_tempo_resposta], 0)
VAR _kri3 = COALESCE([ind_pct_resolutividade], 0)
VAR _kri4 = COALESCE([ind_pct_respostas_insatisfatorias], 0)
VAR _kri5 = COALESCE([ind_media_nota_recomendacao], 0)
VAR _s1 = COALESCE([idx_score_igro_kri1], 0)
VAR _s2 = COALESCE([idx_score_igro_kri2], 0)
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```


## Sem categoria / Ocultas

#### _JSON IGRO Anos

JSON array com dados IGRO por ano para uso no visual HTML

```dax
VAR _dados =
    ADDCOLUMNS (
        FILTER (
            SUMMARIZE ( 'dCalendario', 'dCalendario'[Ano] ),
            'dCalendario'[Ano] > 2000
        ),
        "@i", [idx_igro],
        "@t", [idx_igro_sub_t],
        "@q", [idx_igro_sub_q],
        "@m", [ind_media_tempo_resposta],
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

#### HTML IGRO Ano a Ano

Visual HTML estatico: evolucao ano a ano do IGRO com tendencia, KRIs e tabela comparativa

```dax
VAR _dados =
    ADDCOLUMNS (
        FILTER (
            SUMMARIZE ( 'dCalendario', 'dCalendario'[Ano] ),
            'dCalendario'[Ano] > 2000
        ),
        "@i", [idx_igro],
        "@t", [idx_igro_sub_t],
        "@q", [idx_igro_sub_q],
        "@m", [ind_media_tempo_resposta],
[...expressão truncada — gera código HTML/JS extenso para visual customizado...]
```

