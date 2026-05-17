# Medidas DAX — BaseDadosOuvidoria (snake_case · ordem por camadas)

> Estrutura organizada por camadas: `base` → `indicadores` → `tempo` → `ranking` → `indices` → `auxiliares` → `formatacao`.

---

## camada_base

```dax
base_qtd_manifestacoes =
VAR resultado =
    COUNTROWS ( fRelatorio )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_manifestacoes_em_aberto =
VAR resultado =
    CALCULATE (
        COUNTROWS ( fRelatorio ),
        KEEPFILTERS ( fRelatorio[Data_finalizacao] = "-" )
    )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_manifestacoes_finalizadas =
VAR total_manifestacoes = [base_qtd_manifestacoes]
VAR em_aberto = [base_qtd_manifestacoes_em_aberto]
RETURN
    total_manifestacoes - em_aberto


base_qtd_manifestacao_inativada =
VAR resultado =
    CALCULATE (
        [base_qtd_manifestacoes],
        KEEPFILTERS ( fRelatorio[Tipificacao] = "Manifestação inativada" )
    )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_mais_30_dias =
VAR resultado =
    CALCULATE (
        COUNTROWS ( fRelatorio ),
        KEEPFILTERS ( fRelatorio[Dias_vida] > 30 )
    )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_lai =
VAR resultado =
    CALCULATE (
        [base_qtd_manifestacoes_finalizadas],
        KEEPFILTERS ( fRelatorio[Tipo_manifestacao] = "L.A.I." )
    )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_comunicacao =
VAR resultado =
    CALCULATE (
        [base_qtd_manifestacoes_finalizadas],
        KEEPFILTERS ( fRelatorio[Tipo_manifestacao] = "Comunicação" )
    )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_finalizadas_sem_lai =
VAR finalizadas = [base_qtd_manifestacoes_finalizadas]
VAR lai = [base_qtd_lai]
RETURN
    finalizadas - lai


base_qtd_pesquisa =
VAR resultado =
    COUNTROWS ( fPesquisa )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_sim =
VAR resultado =
    CALCULATE (
        COUNTROWS ( fPesquisa ),
        KEEPFILTERS ( fPesquisa[Finalizacao] = "sim" )
    )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_parcialmente =
VAR resultado =
    CALCULATE (
        COUNTROWS ( fPesquisa ),
        KEEPFILTERS ( fPesquisa[Finalizacao] = "Parcialmente" )
    )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_respostas_insatisfatorias =
VAR resultado =
    COUNTROWS ( fInsatisfatorias )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_prazo_interno_mais_35_dias =
VAR resultado =
    CALCULATE (
        COUNTROWS ( fPrazosInternos ),
        KEEPFILTERS ( fPrazosInternos[Prazo_interno] > 35 )
    )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_manifestacoes_ranking =
VAR resultado =
    COUNTROWS ( fRanking )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_ranking_inativada =
VAR resultado =
    CALCULATE (
        [base_qtd_manifestacoes_ranking],
        KEEPFILTERS ( fRanking[Assunto] = "Manifestação inativada" )
    )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_ranking_abertas =
VAR resultado =
    CALCULATE (
        COUNTROWS ( fRanking ),
        KEEPFILTERS ( fRanking[Data_finalizacao] = "-" )
    )
RETURN
    COALESCE ( resultado, 0 )


base_qtd_resolvidas =
VAR qtd_parcial = [base_qtd_parcialmente]
VAR qtd_total_sim = [base_qtd_sim]
RETURN
    qtd_total_sim + 0.5 * qtd_parcial


base_manifestacoes_elegiveis =
VAR total_finalizadas = [base_qtd_manifestacoes_finalizadas]
VAR total_lai = [base_qtd_lai]
RETURN
    total_finalizadas - total_lai


base_diff_ranking =
VAR total = [base_qtd_manifestacoes]
VAR inativada = [base_qtd_manifestacao_inativada]
VAR em_aberto = [base_qtd_manifestacoes_em_aberto]
RETURN
    total - inativada - em_aberto
```

---

## camada_indicadores

```dax
ind_media_tempo_resposta =
VAR resultado =
    AVERAGE ( fRelatorio[Dias_vida] )
RETURN
    COALESCE ( resultado, 0 )


ind_media_nota_recomendacao =
VAR resultado =
    AVERAGE ( fPesquisa[Recomendaria] )
RETURN
    COALESCE ( resultado, 0 )


ind_pct_mais_30_dias =
VAR numerador = [base_qtd_mais_30_dias]
VAR denominador = [base_qtd_manifestacoes]
RETURN
    DIVIDE ( numerador, denominador, 0 )


ind_pct_resolutividade =
VAR numerador = [base_qtd_resolvidas]
VAR denominador = [base_qtd_pesquisa]
RETURN
    DIVIDE ( numerador, denominador, 0 )


ind_pct_pesquisas_respondidas =
VAR numerador = [base_qtd_pesquisa]
VAR denominador = [base_qtd_manifestacoes_finalizadas] - [base_qtd_comunicacao]
RETURN
    DIVIDE ( numerador, denominador, 0 )


ind_pct_respostas_insatisfatorias =
VAR numerador = [base_qtd_respostas_insatisfatorias]
VAR denominador = [base_manifestacoes_elegiveis]
RETURN
    DIVIDE ( numerador, denominador, 0 )


ind_pct_manifestacao_inativada =
VAR numerador = [base_qtd_manifestacao_inativada]
VAR denominador = [base_manifestacoes_elegiveis]
RETURN
    DIVIDE ( numerador, denominador, 0 )


ind_pct_prazo_interno_mais_35_dias =
VAR numerador = [base_qtd_prazo_interno_mais_35_dias]
VAR denominador = [base_qtd_manifestacoes] - [base_qtd_lai]
RETURN
    DIVIDE ( numerador, denominador, 0 )
```

---

## camada_tempo

```dax
tempo_base_qtd_manifestacoes_aa =
VAR resultado =
    CALCULATE (
        [base_qtd_manifestacoes],
        PREVIOUSYEAR ( dCalendario[Data] )
    )
RETURN
    COALESCE ( resultado, 0 )


tempo_ind_media_tempo_resposta_aa =
VAR resultado =
    CALCULATE (
        [ind_media_tempo_resposta],
        PREVIOUSYEAR ( dCalendario[Data] )
    )
RETURN
    COALESCE ( resultado, 0 )


tempo_ind_pct_resolutividade_aa =
VAR resultado =
    CALCULATE (
        [ind_pct_resolutividade],
        PREVIOUSYEAR ( dCalendario[Data] )
    )
RETURN
    COALESCE ( resultado, 0 )


tempo_ind_media_nota_recomendacao_aa =
VAR resultado =
    CALCULATE (
        [ind_media_nota_recomendacao],
        PREVIOUSYEAR ( dCalendario[Data] )
    )
RETURN
    COALESCE ( resultado, 0 )


tempo_ind_pct_pesquisas_respondidas_aa =
VAR resultado =
    CALCULATE (
        [ind_pct_pesquisas_respondidas],
        PREVIOUSYEAR ( dCalendario[Data] )
    )
RETURN
    COALESCE ( resultado, 0 )
```

---

## camada_ranking

```dax
rank_assuntos =
RANKX (
    ALL ( fRelatorio[Tipificacao] ),
    [base_qtd_manifestacoes],
    ,
    DESC,
    DENSE
)


rank_subassuntos =
RANKX (
    ALL ( fRelatorio[Sub_tipificacao] ),
    [base_qtd_manifestacoes],
    ,
    DESC,
    DENSE
)


rank_top_3_assuntos =
CALCULATE (
    [base_qtd_manifestacoes],
    KEEPFILTERS (
        FILTER (
            VALUES ( fRelatorio[Tipificacao] ),
            [rank_assuntos] <= 3
        )
    )
)


rank_top_3_subassuntos =
CALCULATE (
    [base_qtd_manifestacoes],
    KEEPFILTERS (
        FILTER (
            VALUES ( fRelatorio[Sub_tipificacao] ),
            [rank_subassuntos] <= 3
        )
    )
)


rank_exibir_top_3_assuntos =
VAR ranking_atual = [rank_assuntos]
RETURN
    IF ( ranking_atual <= 3, [base_qtd_manifestacoes] )


rank_exibir_top_3_subassuntos =
VAR ranking_atual = [rank_subassuntos]
RETURN
    IF ( ranking_atual <= 3, [base_qtd_manifestacoes] )


rank_ranking_assuntos =
RANKX (
    ALL ( fRanking[Assunto] ),
    [base_qtd_manifestacoes_ranking],
    ,
    DESC,
    DENSE
)


rank_top_3_ranking_assuntos =
CALCULATE (
    [base_qtd_manifestacoes_ranking],
    KEEPFILTERS (
        FILTER (
            VALUES ( fRanking[Assunto] ),
            [rank_ranking_assuntos] <= 3
        )
    )
)


rank_ranking_subassuntos =
RANKX (
    ALL ( fRanking[SubAssunto] ),
    [base_qtd_manifestacoes_ranking],
    ,
    DESC,
    DENSE
)


rank_top_3_ranking_subassuntos =
CALCULATE (
    [base_qtd_manifestacoes_ranking],
    KEEPFILTERS (
        FILTER (
            VALUES ( fRanking[SubAssunto] ),
            [rank_ranking_subassuntos] <= 3
        )
    )
)
```

---

## camada_indices

```dax
meta_percentual_atraso = 0.02
meta_percentual_respostas_insatisfatorias = 0.05
meta_resolutividade = 0.50
meta_nota_recomendacao = 7.0

peso_pesquisas = 0.04
peso_resolutividade = 0.48
peso_nota = 0.48


idx_score_iqo_pesquisas =
VAR valor = [ind_pct_pesquisas_respondidas]
VAR meta = 0.15
VAR goalpost = 0.02
VAR score = DIVIDE ( valor - goalpost, meta - goalpost, 0 )
RETURN
    MIN ( MAX ( score, 0 ), 1 )


idx_score_iqo_resolutividade =
VAR valor = [ind_pct_resolutividade]
VAR meta = 0.70
VAR goalpost = 0.30
VAR score = DIVIDE ( valor - goalpost, meta - goalpost, 0 )
RETURN
    MIN ( MAX ( score, 0 ), 1 )


idx_score_iqo_nota =
VAR valor = DIVIDE ( [ind_media_nota_recomendacao], 10, 0 )
VAR meta = 0.70
VAR goalpost = 0.40
VAR score = DIVIDE ( valor - goalpost, meta - goalpost, 0 )
RETURN
    MIN ( MAX ( score, 0 ), 1 )


idx_iqo =
VAR score_nota = [idx_score_iqo_nota]
VAR score_pesquisas = [idx_score_iqo_pesquisas]
VAR score_resolutividade = [idx_score_iqo_resolutividade]
VAR peso_total_nota = [peso_nota]
VAR peso_total_pesquisas = [peso_pesquisas]
VAR peso_total_resolutividade = [peso_resolutividade]
RETURN
    score_nota * peso_total_nota
        + score_pesquisas * peso_total_pesquisas
        + score_resolutividade * peso_total_resolutividade


meta_igro_kri1 = 0.02
goal_igro_kri1 = 0.15
meta_igro_kri2 = 10.0
goal_igro_kri2 = 30.0
meta_igro_kri3 = 0.70
goal_igro_kri3 = 0.30
meta_igro_kri4 = 0.025
goal_igro_kri4 = 0.20
meta_igro_kri5 = 7.5
goal_igro_kri5 = 4.0


idx_score_igro_kri1 =
VAR valor = [ind_pct_mais_30_dias]
VAR meta = [meta_igro_kri1]
VAR goalpost = [goal_igro_kri1]
VAR score = DIVIDE ( goalpost - valor, goalpost - meta, 0 )
RETURN
    MIN ( MAX ( score, 0 ), 1 )


idx_score_igro_kri2 =
VAR valor = [ind_media_tempo_resposta]
VAR meta = [meta_igro_kri2]
VAR goalpost = [goal_igro_kri2]
VAR score = DIVIDE ( goalpost - valor, goalpost - meta, 0 )
RETURN
    MIN ( MAX ( score, 0 ), 1 )


idx_score_igro_kri3 =
VAR valor = [ind_pct_resolutividade]
VAR meta = [meta_igro_kri3]
VAR goalpost = [goal_igro_kri3]
VAR score = DIVIDE ( valor - goalpost, meta - goalpost, 0 )
RETURN
    MIN ( MAX ( score, 0 ), 1 )


idx_score_igro_kri4 =
VAR valor = [ind_pct_respostas_insatisfatorias]
VAR meta = [meta_igro_kri4]
VAR goalpost = [goal_igro_kri4]
VAR score = DIVIDE ( goalpost - valor, goalpost - meta, 0 )
RETURN
    MIN ( MAX ( score, 0 ), 1 )


idx_score_igro_kri5 =
VAR valor = [ind_media_nota_recomendacao]
VAR meta = [meta_igro_kri5]
VAR goalpost = [goal_igro_kri5]
VAR score = DIVIDE ( valor - goalpost, meta - goalpost, 0 )
RETURN
    MIN ( MAX ( score, 0 ), 1 )


idx_igro_sub_t =
VAR numerador =
    0.15 * [idx_score_igro_kri1]
        + 0.25 * [idx_score_igro_kri2]
VAR resultado =
    DIVIDE ( numerador, 0.40, 0 )
RETURN
    MIN ( MAX ( resultado, 0 ), 1 )


idx_igro_sub_q =
VAR numerador =
    0.25 * [idx_score_igro_kri3]
        + 0.15 * [idx_score_igro_kri4]
        + 0.20 * [idx_score_igro_kri5]
VAR resultado =
    DIVIDE ( numerador, 0.60, 0 )
RETURN
    MIN ( MAX ( resultado, 0 ), 1 )


idx_igro =
VAR sub_t = [idx_igro_sub_t]
VAR sub_q = [idx_igro_sub_q]
VAR resultado =
    IF (
        AND ( sub_t > 0, sub_q > 0 ),
        POWER ( sub_t, 0.40 ) * POWER ( sub_q, 0.60 ),
        0
    )
RETURN
    MIN ( MAX ( resultado, 0 ), 1 )
```

---

## camada_auxiliares

```dax
aux_titulo_relatorio =
VAR sigla = SELECTEDVALUE ( dOrgao[Sigla], "Todos os órgãos" )
VAR ano = SELECTEDVALUE ( dCalendario[Ano], "Todos os anos" )
RETURN
    sigla & " | " & ano


aux_titulo_relatorio_quadri =
VAR sigla = SELECTEDVALUE ( dOrgao[Sigla], "Todos os órgãos" )
VAR quadrimestre = SELECTEDVALUE ( dCalendario[NomeQuadrimestre], "Todos os quadrimestres" )
VAR ano = SELECTEDVALUE ( dCalendario[Ano], "Todos os anos" )
RETURN
    sigla & " | " & quadrimestre & " | " & ano
```

---

## camada_formatacao

```dax
fmt_semaforo_igro =
VAR valor = [idx_igro]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "Verde — Risco Baixo",
        valor >= 0.60, "Amarelo — Risco Moderado",
        valor >= 0.40, "Laranja — Risco Alto",
        "Vermelho — Risco Crítico"
    )


fmt_semaforo_igro_sub_t =
VAR valor = [idx_igro_sub_t]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "Verde — Risco Baixo",
        valor >= 0.60, "Amarelo — Risco Moderado",
        valor >= 0.40, "Laranja — Risco Alto",
        "Vermelho — Risco Crítico"
    )


fmt_semaforo_igro_sub_q =
VAR valor = [idx_igro_sub_q]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "Verde — Risco Baixo",
        valor >= 0.60, "Amarelo — Risco Moderado",
        valor >= 0.40, "Laranja — Risco Alto",
        "Vermelho — Risco Crítico"
    )


fmt_cor_fundo_igro =
VAR valor = [idx_igro]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "#EAF3DE",
        valor >= 0.60, "#FAEEDA",
        valor >= 0.40, "#FAECE7",
        "#FCEBEB"
    )


fmt_cor_fonte_igro =
VAR valor = [idx_igro]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "#27500A",
        valor >= 0.60, "#633806",
        valor >= 0.40, "#712B13",
        "#791F1F"
    )


fmt_cor_fundo_igro_sub_t =
VAR valor = [idx_igro_sub_t]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "#EAF3DE",
        valor >= 0.60, "#FAEEDA",
        valor >= 0.40, "#FAECE7",
        "#FCEBEB"
    )


fmt_cor_fundo_igro_sub_q =
VAR valor = [idx_igro_sub_q]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "#EAF3DE",
        valor >= 0.60, "#FAEEDA",
        valor >= 0.40, "#FAECE7",
        "#FCEBEB"
    )


fmt_cor_fundo_igro_kri1 =
VAR valor = [idx_score_igro_kri1]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "#EAF3DE",
        valor >= 0.60, "#FAEEDA",
        valor >= 0.40, "#FAECE7",
        "#FCEBEB"
    )


fmt_cor_fundo_igro_kri2 =
VAR valor = [idx_score_igro_kri2]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "#EAF3DE",
        valor >= 0.60, "#FAEEDA",
        valor >= 0.40, "#FAECE7",
        "#FCEBEB"
    )


fmt_cor_fundo_igro_kri3 =
VAR valor = [idx_score_igro_kri3]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "#EAF3DE",
        valor >= 0.60, "#FAEEDA",
        valor >= 0.40, "#FAECE7",
        "#FCEBEB"
    )


fmt_cor_fundo_igro_kri4 =
VAR valor = [idx_score_igro_kri4]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "#EAF3DE",
        valor >= 0.60, "#FAEEDA",
        valor >= 0.40, "#FAECE7",
        "#FCEBEB"
    )


fmt_cor_fundo_igro_kri5 =
VAR valor = [idx_score_igro_kri5]
RETURN
    SWITCH (
        TRUE (),
        valor >= 0.80, "#EAF3DE",
        valor >= 0.60, "#FAEEDA",
        valor >= 0.40, "#FAECE7",
        "#FCEBEB"
    )
```
