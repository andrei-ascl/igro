# Catálogo de medidas

## 01 · Volume

### base_manifestacoes_elegiveis

`_medidas.base_manifestacoes_elegiveis` · #,0 · 01 · Volume

**O que faz:**
Total de respostas recebidas na pesquisa de satisfação (linhas em f_pesquisa). TREATAS propaga filtro de dOrgao_igro[sigla].

**DAX:**
```dax
VAR finalizadas = [base_qtd_manifestacoes_finalizadas]
VAR lai = [base_qtd_lai]
RETURN
finalizadas - lai
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_lai, base_qtd_manifestacoes_finalizadas.

**Usa:** `base_qtd_lai`, `base_qtd_manifestacoes_finalizadas`
**É usada por:** `ind_pct_respostas_insatisfatorias`


### base_manifestacoes_identificadas

`_medidas.base_manifestacoes_identificadas` · #,0 · 01 · Volume

**O que faz:**
Versão do Dashboard Final com override de CSS para fonte branca em textos que apareciam pretos.

**DAX:**
```dax
CALCULATE(
[base_qtd_manifestacoes_finalizadas],
f_relatorio[sigilo] <> "An" & UNICHAR(244) & "nimo"
)
```

**Como funciona:**
Usa 1 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes_finalizadas.

**Usa:** `base_qtd_manifestacoes_finalizadas`, `f_relatorio[sigilo]`
**É usada por:** `flag_amostra_insuficiente`


### base_qtd_lai

`_medidas.base_qtd_lai` · #,0 · 01 · Volume

**O que faz:**
Manifestações finalizadas descontando as LAI. Denominador base para KRI 3 e KRI 4.

**DAX:**
```dax
VAR resultado =
CALCULATE (
[base_qtd_manifestacoes_finalizadas],
KEEPFILTERS ( f_relatorio[tipo_manifestacao] = "L.A.I." )
)
RETURN
COALESCE ( resultado, 0 )
```

**Como funciona:**
Usa 1 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes_finalizadas.

**Usa:** `base_qtd_manifestacoes_finalizadas`, `f_relatorio[tipo_manifestacao]`
**É usada por:** `base_manifestacoes_elegiveis`


### base_qtd_manifestacoes

`_medidas.base_qtd_manifestacoes` · #,0 · 01 · Volume

**O que faz:**
Manifestações com status Fechada ou Respondida no SGOe.

**DAX:**
```dax
VAR resultado =
COUNTROWS ( f_relatorio )
RETURN
COALESCE ( resultado, 0 )
```

**Como funciona:**
Usa 0 medida(s) e 0 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** —
**É usada por:** `HTML Dashboard Final Base`, `HTML Matriz Classes IGRO`, `HTML Tabela Resultados IGRO CSV`, `_JSON KPIs`, `_JSON Orgaos`, `_JSON Tipos`, `base_qtd_manifestacoes_aa`, `base_qtd_manifestacoes_dias_uteis`, `base_qtd_manifestacoes_fim_semana`, `base_qtd_manifestacoes_finalizadas`, `base_qtd_manifestacoes_quadri_anterior`, `base_qtd_manifestacoes_ytd`, `base_qtd_procedente`, `ind_indice_sazonalidade`, `ind_media_diaria_manifestacoes`, `ind_media_movel_3m`, `ind_pct_fim_semana`, `ind_pct_mais_30_dias`, `ind_var_pct_volume_aa`, `ind_var_pct_volume_quadri`, `ind_var_vs_media_movel`


### base_qtd_manifestacoes_em_aberto

`_medidas.base_qtd_manifestacoes_em_aberto` · #,0 · 01 · Volume

**O que faz:**
Total de manifestações registradas no período, independente do status.

**DAX:**
```dax
VAR resultado =
CALCULATE (
COUNTROWS ( f_relatorio ),
KEEPFILTERS ( f_relatorio[ds_status] = "Em Aberto" )
)
RETURN
COALESCE ( resultado, 0 )
```

**Como funciona:**
Usa 0 medida(s) e 1 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** `f_relatorio[ds_status]`
**É usada por:** `HTML Tabela Resultados IGRO CSV`, `base_qtd_manifestacoes_finalizadas`


### base_qtd_manifestacoes_finalizadas

`_medidas.base_qtd_manifestacoes_finalizadas` · #,0 · 01 · Volume

**O que faz:**
Manifestações com mais de 30 dias de vida (dias_vida > 30). Numerador do KRI 1.

**DAX:**
```dax
VAR total_manifestacoes = [base_qtd_manifestacoes]
VAR em_aberto = [base_qtd_manifestacoes_em_aberto]
RETURN
total_manifestacoes - em_aberto
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes, base_qtd_manifestacoes_em_aberto.

**Usa:** `base_qtd_manifestacoes`, `base_qtd_manifestacoes_em_aberto`
**É usada por:** `HTML Tabela Resultados IGRO CSV`, `base_manifestacoes_elegiveis`, `base_manifestacoes_identificadas`, `base_qtd_com_recurso`, `base_qtd_finalizadas_por_data_fin`, `base_qtd_lai`, `ind_pct_cobertura_reclamacao`, `ind_pct_procedencia`, `ind_pct_recurso`


## 02 · Pesquisa de Satisfação

### base_qtd_detratores

`_medidas.base_qtd_detratores` · #,0 · 02 · Pesquisa de Satisfação

**O que faz:**
Manifestações finalizadas com procedente = 'Sim'.

**DAX:**
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

**Como funciona:**
Usa 0 medida(s) e 3 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** `KEEPFILTERS(f_pesquisa[recomendaria]`, `VALUES(dOrgao_igro[sigla]`, `f_pesquisa[sigla]`
**É usada por:** `HTML Dashboard Final Base`, `ind_nps`, `ind_pct_detratores`


### base_qtd_neutros

`_medidas.base_qtd_neutros` · #,0 · 02 · Pesquisa de Satisfação

**O que faz:**
Respostas de pesquisa com nota de recomendação entre 1 e 6. Subtraídas no cálculo do NPS. TREATAS propaga filtro de dOrgao_igro[sigla].

**DAX:**
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

**Como funciona:**
Usa 0 medida(s) e 3 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** `KEEPFILTERS(f_pesquisa[recomendaria]`, `VALUES(dOrgao_igro[sigla]`, `f_pesquisa[sigla]`
**É usada por:** `HTML Dashboard Final Base`, `ind_pct_neutros`


### base_qtd_parcialmente

`_medidas.base_qtd_parcialmente` · #,0 · 02 · Pesquisa de Satisfação

**O que faz:**
Total de linhas em f_insatisfatorias. Respostas reprovadas na revisão de qualidade. TREATAS propaga filtro de dOrgao_igro[sigla].

**DAX:**
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

**Como funciona:**
Usa 0 medida(s) e 3 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** `KEEPFILTERS(f_pesquisa[finalizacao]`, `VALUES(dOrgao_igro[sigla]`, `f_pesquisa[sigla]`
**É usada por:** `base_qtd_resolvidas`


### base_qtd_pesquisa

`_medidas.base_qtd_pesquisa` · #,0 · 02 · Pesquisa de Satisfação

**O que faz:**
Pesquisas em que o cidadão respondeu que a demanda foi resolvida totalmente (finalizacao = 'Sim'). TREATAS propaga filtro de dOrgao_igro[sigla].

**DAX:**
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

**Como funciona:**
Usa 0 medida(s) e 2 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** `VALUES(dOrgao_igro[sigla]`, `f_pesquisa[sigla]`
**É usada por:** `HTML Dashboard Final Base`, `HTML Matriz Classes IGRO`, `HTML Tabela Resultados IGRO CSV`, `_JSON KPIs`, `_JSON Tipos`, `flag_amostra_insuficiente`, `ind_nps`, `ind_pct_cobertura_reclamacao`, `ind_pct_detratores`, `ind_pct_neutros`, `ind_pct_promotores`, `ind_pct_resolutividade`


### base_qtd_promotores

`_medidas.base_qtd_promotores` · #,0 · 02 · Pesquisa de Satisfação

**O que faz:**
Respostas de pesquisa com nota de recomendação entre 7 e 8. Não entram no cálculo do NPS. TREATAS propaga filtro de dOrgao_igro[sigla].

**DAX:**
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

**Como funciona:**
Usa 0 medida(s) e 3 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** `KEEPFILTERS(f_pesquisa[recomendaria]`, `VALUES(dOrgao_igro[sigla]`, `f_pesquisa[sigla]`
**É usada por:** `HTML Dashboard Final Base`, `ind_nps`, `ind_pct_promotores`


### base_qtd_resolvidas

`_medidas.base_qtd_resolvidas` · #,0.0 · 02 · Pesquisa de Satisfação

**O que faz:**
Média de dias_vida das manifestações. Tempo Médio de Resposta (TMR). Numerador do KRI 2.

**DAX:**
```dax
VAR qtd_total_sim = [base_qtd_sim]
VAR qtd_parcial = [base_qtd_parcialmente]
RETURN
qtd_total_sim + 0.5 * qtd_parcial
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_parcialmente, base_qtd_sim.

**Usa:** `base_qtd_parcialmente`, `base_qtd_sim`
**É usada por:** `ind_pct_resolutividade`


### base_qtd_sim

`_medidas.base_qtd_sim` · #,0 · 02 · Pesquisa de Satisfação

**O que faz:**
Pesquisas em que o cidadão respondeu que a demanda foi resolvida parcialmente (finalizacao = 'Parcialmente'). TREATAS propaga filtro de dOrgao_igro[sigla].

**DAX:**
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

**Como funciona:**
Usa 0 medida(s) e 3 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** `KEEPFILTERS(f_pesquisa[finalizacao]`, `VALUES(dOrgao_igro[sigla]`, `f_pesquisa[sigla]`
**É usada por:** `base_qtd_resolvidas`


### ind_media_nota_recomendacao

`_medidas.ind_media_nota_recomendacao` · #,0.0 · 02 · Pesquisa de Satisfação

**O que faz:**
Percentual de manifestações com mais de 30 dias de vida sobre o total. Indicador do KRI 1.

**DAX:**
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

**Como funciona:**
Usa 0 medida(s) e 3 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** `AVERAGE(f_pesquisa[recomendaria]`, `VALUES(dOrgao_igro[sigla]`, `f_pesquisa[sigla]`
**É usada por:** `HTML Dashboard Final Base`, `HTML Tabela Resultados IGRO CSV`, `_JSON KPIs`, `_JSON Orgaos`, `idx_score_igro_kri5`, `lbl_nota`, `var_nota`


### ind_nps

`_medidas.ind_nps` · #,0.0 · 02 · Pesquisa de Satisfação

**O que faz:**
Percentual de promotores (nota 9–10) sobre o total de pesquisas respondidas.

**DAX:**
```dax
VAR promotores = DIVIDE([base_qtd_promotores], [base_qtd_pesquisa], 0)
VAR detratores = DIVIDE([base_qtd_detratores], [base_qtd_pesquisa], 0)
RETURN
(promotores - detratores) * 100
```

**Como funciona:**
Usa 3 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_detratores, base_qtd_pesquisa, base_qtd_promotores.

**Usa:** `base_qtd_detratores`, `base_qtd_pesquisa`, `base_qtd_promotores`, `DIVIDE([base_qtd_detratores]`, `DIVIDE([base_qtd_promotores]`
**É usada por:** `HTML Dashboard Final Base`, `HTML Matriz Classes IGRO`, `HTML Tabela Resultados IGRO CSV`, `_JSON KPIs`, `_JSON Orgaos`, `fmt_cor_fonte_nps`, `fmt_cor_fundo_nps`, `fmt_semaforo_nps`, `lbl_nps`, `var_nps`


### ind_pct_detratores

`_medidas.ind_pct_detratores` · 0.0% · 02 · Pesquisa de Satisfação

**O que faz:**
Percentual de manifestações com análise procedente sobre o total de finalizadas.

**DAX:**
```dax
DIVIDE([base_qtd_detratores], [base_qtd_pesquisa], 0)
```

**Como funciona:**
Usa 2 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_detratores, base_qtd_pesquisa.

**Usa:** `base_qtd_detratores`, `base_qtd_pesquisa`, `DIVIDE([base_qtd_detratores]`
**É usada por:** `HTML Dashboard Final Base`, `HTML Tabela Resultados IGRO CSV`


### ind_pct_neutros

`_medidas.ind_pct_neutros` · 0.0% · 02 · Pesquisa de Satisfação

**O que faz:**
Percentual de detratores (nota 1–6) sobre o total de pesquisas respondidas.

**DAX:**
```dax
DIVIDE([base_qtd_neutros], [base_qtd_pesquisa], 0)
```

**Como funciona:**
Usa 2 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_neutros, base_qtd_pesquisa.

**Usa:** `base_qtd_neutros`, `base_qtd_pesquisa`, `DIVIDE([base_qtd_neutros]`
**É usada por:** `HTML Dashboard Final Base`, `HTML Tabela Resultados IGRO CSV`


### ind_pct_promotores

`_medidas.ind_pct_promotores` · 0.0% · 02 · Pesquisa de Satisfação

**O que faz:**
Percentual de neutros (nota 7–8) sobre o total de pesquisas respondidas.

**DAX:**
```dax
DIVIDE([base_qtd_promotores], [base_qtd_pesquisa], 0)
```

**Como funciona:**
Usa 2 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_pesquisa, base_qtd_promotores.

**Usa:** `base_qtd_pesquisa`, `base_qtd_promotores`, `DIVIDE([base_qtd_promotores]`
**É usada por:** `HTML Dashboard Final Base`, `HTML Tabela Resultados IGRO CSV`


### ind_pct_resolutividade

`_medidas.ind_pct_resolutividade` · 0.00% · 02 · Pesquisa de Satisfação

**O que faz:**
Percentual de respostas insatisfatórias sobre as manifestações elegíveis. Indicador do KRI 4.

**DAX:**
```dax
VAR numerador = [base_qtd_resolvidas]
VAR denominador = [base_qtd_pesquisa]
RETURN
DIVIDE ( numerador, denominador, 0 )
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_pesquisa, base_qtd_resolvidas.

**Usa:** `base_qtd_pesquisa`, `base_qtd_resolvidas`
**É usada por:** `HTML Dashboard Final Base`, `HTML Matriz Classes IGRO`, `HTML Tabela Resultados IGRO CSV`, `_JSON KPIs`, `_JSON Orgaos`, `idx_score_igro_kri3`, `lbl_resolutividade`, `var_resolutividade`


## 03 · Qualidade

### base_qtd_com_recurso

`_medidas.base_qtd_com_recurso` · #,0 · 03 · Qualidade

**O que faz:**
NPS calculado: (% promotores − % detratores) × 100. Escala de −90 a +100.

**DAX:**
```dax
VAR resultado =
CALCULATE(
[base_qtd_manifestacoes_finalizadas],
KEEPFILTERS(f_relatorio[recurso] <> BLANK())
)
RETURN
COALESCE(resultado, 0)
```

**Como funciona:**
Usa 1 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes_finalizadas.

**Usa:** `base_qtd_manifestacoes_finalizadas`, `KEEPFILTERS(f_relatorio[recurso]`
**É usada por:** `ind_pct_recurso`


### base_qtd_procedente

`_medidas.base_qtd_procedente` · #,0 · 03 · Qualidade

**O que faz:**
Manifestações finalizadas que geraram ao menos um recurso (campo recurso preenchido).

**DAX:**
```dax
VAR resultado =
CALCULATE(
[base_qtd_manifestacoes],
KEEPFILTERS(f_relatorio[procedente] = "Sim")
)
RETURN
COALESCE(resultado, 0)
```

**Como funciona:**
Usa 1 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes.

**Usa:** `base_qtd_manifestacoes`, `KEEPFILTERS(f_relatorio[procedente]`
**É usada por:** `ind_pct_procedencia`


### base_qtd_respostas_insatisfatorias

`_medidas.base_qtd_respostas_insatisfatorias` · #,0 · 03 · Qualidade

**O que faz:**
Combinação ponderada de respostas: base_qtd_sim + 0,5 × base_qtd_parcialmente. Numerador da resolutividade.

**DAX:**
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

**Como funciona:**
Usa 0 medida(s) e 2 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** `VALUES(dOrgao_igro[sigla]`, `f_insatisfatorias[sigla]`
**É usada por:** `_JSON Tipos`, `ind_pct_respostas_insatisfatorias`


### ind_pct_cobertura_reclamacao

`_medidas.ind_pct_cobertura_reclamacao` · 0.00% · 03 · Qualidade

**O que faz:**
Rótulo de semáforo para o NPS: Verde (≥50), Amarelo (0–49), Laranja (-49 a -1), Vermelho (<-50).

**DAX:**
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

**Como funciona:**
Usa 2 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes_finalizadas, base_qtd_pesquisa.

**Usa:** `base_qtd_manifestacoes_finalizadas`, `base_qtd_pesquisa`, `KEEPFILTERS(f_relatorio[tipo_manifestacao]`
**É usada por:** `var_cobertura_reclamacao`


### ind_pct_procedencia

`_medidas.ind_pct_procedencia` · 0.00% · 03 · Qualidade

**O que faz:**
Percentual de manifestações que geraram recurso sobre o total de finalizadas. Indicador de retrabalho.

**DAX:**
```dax
DIVIDE([base_qtd_procedente], [base_qtd_manifestacoes_finalizadas], 0)
```

**Como funciona:**
Usa 2 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes_finalizadas, base_qtd_procedente.

**Usa:** `base_qtd_manifestacoes_finalizadas`, `base_qtd_procedente`, `DIVIDE([base_qtd_procedente]`
**É usada por:** `_JSON KPIs`, `fmt_semaforo_procedencia`


### ind_pct_recurso

`_medidas.ind_pct_recurso` · 0.00% · 03 · Qualidade

**O que faz:**
Percentual de Reclamações finalizadas que receberam resposta na pesquisa de satisfação.

**DAX:**
```dax
DIVIDE([base_qtd_com_recurso], [base_qtd_manifestacoes_finalizadas], 0)
```

**Como funciona:**
Usa 2 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_com_recurso, base_qtd_manifestacoes_finalizadas.

**Usa:** `base_qtd_com_recurso`, `base_qtd_manifestacoes_finalizadas`, `DIVIDE([base_qtd_com_recurso]`
**É usada por:** `_JSON KPIs`, `fmt_semaforo_recurso`, `var_recurso`


### ind_pct_respostas_insatisfatorias

`_medidas.ind_pct_respostas_insatisfatorias` · 0.00% · 03 · Qualidade

**O que faz:**
Meta do KRI 1 (% RDP): máximo de 1,0% de manifestações com mais de 30 dias. Valor 1 quando RDP <= 1,0%.

**DAX:**
```dax
VAR numerador = [base_qtd_respostas_insatisfatorias]
VAR denominador = [base_manifestacoes_elegiveis]
RETURN
DIVIDE ( numerador, denominador, 0 )
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: base_manifestacoes_elegiveis, base_qtd_respostas_insatisfatorias.

**Usa:** `base_manifestacoes_elegiveis`, `base_qtd_respostas_insatisfatorias`
**É usada por:** `HTML Dashboard Final Base`, `HTML Matriz Classes IGRO`, `HTML Tabela Resultados IGRO CSV`, `_JSON KPIs`, `_JSON Orgaos`, `idx_score_igro_kri4`, `lbl_insatisfatorias`, `var_insatisfatorias`


## 04 · Tempo

### base_qtd_finalizadas_por_data_fin

`_medidas.base_qtd_finalizadas_por_data_fin` · #,0 · 04 · Tempo

**O que faz:**
Dashboard HTML IGRO·NPS v3 — corrige JSON inválido (ano nulo) e filtra anos sem dados.

**DAX:**
```dax
CALCULATE(
[base_qtd_manifestacoes_finalizadas],
USERELATIONSHIP(
f_relatorio[data_finalizacao],
dCalendario[Date]
)
)
```

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes_finalizadas.

**Usa:** `base_qtd_manifestacoes_finalizadas`, `dCalendario[Date]`, `f_relatorio[data_finalizacao]`
**É usada por:** —


### base_qtd_mais_30_dias

`_medidas.base_qtd_mais_30_dias` · #,0 · 04 · Tempo

**O que faz:**
Manifestações do tipo LAI (Lei de Acesso à Informação), excluídas de alguns indicadores.

**DAX:**
```dax
VAR resultado =
CALCULATE (
COUNTROWS ( f_relatorio ),
KEEPFILTERS ( f_relatorio[dias_vida] > 30 )
)
RETURN
COALESCE ( resultado, 0 )
```

**Como funciona:**
Usa 0 medida(s) e 1 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** `f_relatorio[dias_vida]`
**É usada por:** `ind_pct_mais_30_dias`


### base_qtd_manifestacoes_aa

`_medidas.base_qtd_manifestacoes_aa` · #,0 · 04 · Tempo

**O que faz:**
TMR médio no mesmo período do ano anterior. Funciona com qualquer granularidade de dCalendario.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 3 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes.

**Usa:** `base_qtd_manifestacoes`, `MAX(dCalendario[Date]`, `MIN(dCalendario[Date]`, `dCalendario[Date]`
**É usada por:** `ind_var_pct_volume_aa`


### base_qtd_manifestacoes_dias_uteis

`_medidas.base_qtd_manifestacoes_dias_uteis` · #,0 · 04 · Tempo

**O que faz:**
Manifestações registradas em fins de semana (sábado e domingo).

**DAX:**
```dax
CALCULATE(
[base_qtd_manifestacoes],
dCalendario[DiaUtil] = TRUE()
)
```

**Como funciona:**
Usa 1 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes.

**Usa:** `base_qtd_manifestacoes`, `dCalendario[DiaUtil]`
**É usada por:** —


### base_qtd_manifestacoes_fim_semana

`_medidas.base_qtd_manifestacoes_fim_semana` · #,0 · 04 · Tempo

**O que faz:**
Percentual do volume registrado fora de dias úteis. Indica pressão sobre canais digitais (Expresso/Webservice) no final de semana.

**DAX:**
```dax
CALCULATE(
[base_qtd_manifestacoes],
dCalendario[FimDeSemana] = TRUE()
)
```

**Como funciona:**
Usa 1 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes.

**Usa:** `base_qtd_manifestacoes`, `dCalendario[FimDeSemana]`
**É usada por:** `ind_pct_fim_semana`


### base_qtd_manifestacoes_quadri_anterior

`_medidas.base_qtd_manifestacoes_quadri_anterior` · #,0 · 04 · Tempo

**O que faz:**
Variação percentual do volume em relação ao quadrimestre anterior.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes.

**Usa:** `base_qtd_manifestacoes`, `SELECTEDVALUE(dCalendario[AnoQuadri]`, `dCalendario[AnoQuadri]`
**É usada por:** `ind_var_pct_volume_quadri`


### base_qtd_manifestacoes_ytd

`_medidas.base_qtd_manifestacoes_ytd` · #,0 · 04 · Tempo

**O que faz:**
Volume médio diário de manifestações no período selecionado. Útil para comparar períodos de tamanhos diferentes.

**DAX:**
```dax
CALCULATE(
[base_qtd_manifestacoes],
DATESYTD(dCalendario[Date])
)
```

**Como funciona:**
Usa 1 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes.

**Usa:** `base_qtd_manifestacoes`, `DATESYTD(dCalendario[Date]`
**É usada por:** —


### ind_indice_sazonalidade

`_medidas.ind_indice_sazonalidade` · #,0.00 · 04 · Tempo

**O que faz:**
Manifestações registradas em dias úteis (segunda a sexta).

**DAX:**
```dax
VAR _ano_ctx    = MAX(dCalendario[Ano])
VAR _vol_mes    = [base_qtd_manifestacoes]
VAR _soma_ano   = CALCULATE([base_qtd_manifestacoes], FILTER(ALL(dCalendario), dCalendario[Ano] = _ano_ctx))
VAR _media_mes  = DIVIDE(_soma_ano, 12, 1)
RETURN DIVIDE(_vol_mes, _media_mes, 1)
```

**Como funciona:**
Usa 1 medida(s) e 3 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes.

**Usa:** `base_qtd_manifestacoes`, `CALCULATE([base_qtd_manifestacoes]`, `MAX(dCalendario[Ano]`, `dCalendario[Ano]`
**É usada por:** —


### ind_media_diaria_manifestacoes

`_medidas.ind_media_diaria_manifestacoes` · #,0.0 · 04 · Tempo

**O que faz:**
Indica se o mês está acima ou abaixo da média mensal do ano. 1.0 = média, >1.0 = pico sazonal, <1.0 = vale. Requer contexto mensal no visual.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 4 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes.

**Usa:** `base_qtd_manifestacoes`, `DIVIDE([base_qtd_manifestacoes]`, `MAX(dCalendario[Date]`, `VALUES(dCalendario[Date]`, `dCalendario[Date]`
**É usada por:** —


### ind_media_movel_3m

`_medidas.ind_media_movel_3m` · #,0.0 · 04 · Tempo

**O que faz:**
Compara o volume do mês atual com a média móvel de 3 meses. Positivo = acima da tendência, negativo = abaixo.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 3 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes.

**Usa:** `base_qtd_manifestacoes`, `CALCULATE([base_qtd_manifestacoes]`, `MAX(dCalendario[AnoMes]`, `dCalendario[AnoMes]`
**É usada por:** `ind_var_vs_media_movel`


### ind_media_tempo_resposta

`_medidas.ind_media_tempo_resposta` · #,0.0 · 04 · Tempo

**O que faz:**
Média das notas de recomendação (1–10) nas pesquisas respondidas. Numerador do KRI 5. TREATAS propaga filtro de dOrgao_igro[sigla].

**DAX:**
```dax
VAR resultado =
AVERAGE ( f_relatorio[dias_vida] )
RETURN
COALESCE ( resultado, 0 )
```

**Como funciona:**
Usa 0 medida(s) e 1 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** `f_relatorio[dias_vida]`
**É usada por:** `HTML Dashboard Final Base`, `HTML Matriz Classes IGRO`, `HTML Tabela Resultados IGRO CSV`, `_JSON KPIs`, `_JSON Orgaos`, `idx_score_igro_kri2`, `ind_tmr_aa`, `lbl_tmr`, `var_tmr`


### ind_pct_fim_semana

`_medidas.ind_pct_fim_semana` · 0.0% · 04 · Tempo

**O que faz:**
Média móvel de 3 meses do volume de manifestações. Usa janela deslizante de AnoMes. Requer contexto mensal no visual.

**DAX:**
```dax
DIVIDE(
[base_qtd_manifestacoes_fim_semana],
[base_qtd_manifestacoes],
0
)
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes, base_qtd_manifestacoes_fim_semana.

**Usa:** `base_qtd_manifestacoes`, `base_qtd_manifestacoes_fim_semana`
**É usada por:** —


### ind_pct_mais_30_dias

`_medidas.ind_pct_mais_30_dias` · 0.00% · 04 · Tempo

**O que faz:**
Percentual de resolução: (sim + 0,5 × parcialmente) / total de pesquisas. Indicador do KRI 3.

**DAX:**
```dax
VAR numerador = [base_qtd_mais_30_dias]
VAR denominador = [base_qtd_manifestacoes]
RETURN
DIVIDE ( numerador, denominador, 0 )
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_mais_30_dias, base_qtd_manifestacoes.

**Usa:** `base_qtd_mais_30_dias`, `base_qtd_manifestacoes`
**É usada por:** `HTML Dashboard Final Base`, `HTML Tabela Resultados IGRO CSV`, `_JSON KPIs`, `idx_score_igro_kri1`, `lbl_pct_mais_30_dias`, `var_pct_mais_30_dias`


### ind_tmr_aa

`_medidas.ind_tmr_aa` · #,0.0 · 04 · Tempo

**O que faz:**
Variação percentual do volume de manifestações em relação ao mesmo período do ano anterior.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 3 coluna(s) referenciada(s) diretamente. Dependências principais: ind_media_tempo_resposta.

**Usa:** `ind_media_tempo_resposta`, `MAX(dCalendario[Date]`, `MIN(dCalendario[Date]`, `dCalendario[Date]`
**É usada por:** —


### ind_var_pct_volume_aa

`_medidas.ind_var_pct_volume_aa` · +0.0%;-0.0%;0.0% · 04 · Tempo

**O que faz:**
Volume de manifestações no quadrimestre anterior ao período selecionado.

**DAX:**
```dax
VAR atual = [base_qtd_manifestacoes]
VAR anterior = [base_qtd_manifestacoes_aa]
RETURN DIVIDE(atual - anterior, anterior, BLANK())
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes, base_qtd_manifestacoes_aa.

**Usa:** `base_qtd_manifestacoes`, `base_qtd_manifestacoes_aa`
**É usada por:** —


### ind_var_pct_volume_quadri

`_medidas.ind_var_pct_volume_quadri` · +0.0%;-0.0%;0.0% · 04 · Tempo

**O que faz:**
Acumulado de manifestações no ano até a data máxima do contexto (YTD).

**DAX:**
```dax
VAR atual = [base_qtd_manifestacoes]
VAR anterior = [base_qtd_manifestacoes_quadri_anterior]
RETURN DIVIDE(atual - anterior, anterior, BLANK())
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes, base_qtd_manifestacoes_quadri_anterior.

**Usa:** `base_qtd_manifestacoes`, `base_qtd_manifestacoes_quadri_anterior`
**É usada por:** —


### ind_var_vs_media_movel

`_medidas.ind_var_vs_media_movel` · +0.0%;-0.0%;0.0% · 04 · Tempo

**O que faz:**
Volume de manifestações usando a data de finalização como eixo temporal. Requer USERELATIONSHIP com dCalendario[Date] via relacionamento inativo.

**DAX:**
```dax
VAR _atual = [base_qtd_manifestacoes]
VAR _mm3   = [ind_media_movel_3m]
RETURN DIVIDE(_atual - _mm3, _mm3, BLANK())
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes, ind_media_movel_3m.

**Usa:** `base_qtd_manifestacoes`, `ind_media_movel_3m`
**É usada por:** —


## 05 · IGRO · Metas e Goalposts

### flag_amostra_insuficiente

`_medidas.flag_amostra_insuficiente` · 0 · 05 · IGRO · Metas e Goalposts

**O que faz:**
Base de manifestacoes finalizadas identificadas (exclui Anonimo). Denominador correto para taxa de cobertura da pesquisa de satisfacao.

**DAX:**
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

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: base_manifestacoes_identificadas, base_qtd_pesquisa.

**Usa:** `base_manifestacoes_identificadas`, `base_qtd_pesquisa`
**É usada por:** `HTML Matriz Classes IGRO`, `HTML Tabela Resultados IGRO CSV`


### goal_igro_kri1

`_medidas.goal_igro_kri1` · 0.00% · 05 · IGRO · Metas e Goalposts

**O que faz:**
Meta do KRI 2 (TMR): 5 dias ou menos como excelência esperada. Valor 1 quando TMR <= 5 dias.

**DAX:**
```dax
0.02
```

**Como funciona:**
Usa 0 medida(s) e 0 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** —
**É usada por:** `idx_score_igro_kri1`


### goal_igro_kri2

`_medidas.goal_igro_kri2` · #,0.0 · 05 · IGRO · Metas e Goalposts

**O que faz:**
Meta do KRI 3 (TR - Resolutividade): 70% ou mais como resolutividade esperada. Valor 1 quando TR >= 70%.

**DAX:**
```dax
10.0
```

**Como funciona:**
Usa 0 medida(s) e 0 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** —
**É usada por:** `idx_score_igro_kri2`


### goal_igro_kri3

`_medidas.goal_igro_kri3` · 0.00% · 05 · IGRO · Metas e Goalposts

**O que faz:**
Meta do KRI 4 (% RI): 2,5% ou inferior como baixíssima insatisfação. Valor 1 quando RI <= 2,5%.

**DAX:**
```dax
0.50
```

**Como funciona:**
Usa 0 medida(s) e 0 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** —
**É usada por:** `idx_score_igro_kri3`


### goal_igro_kri4

`_medidas.goal_igro_kri4` · 0.00% · 05 · IGRO · Metas e Goalposts

**O que faz:**
Meta do KRI 5 (Nota de Recomendação): 8,0 ou mais como excelente recomendação. Valor 1 quando NR >= 8,0.

**DAX:**
```dax
0.035
```

**Como funciona:**
Usa 0 medida(s) e 0 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** —
**É usada por:** `idx_score_igro_kri4`


### goal_igro_kri5

`_medidas.goal_igro_kri5` · #,0.0 · 05 · IGRO · Metas e Goalposts

**O que faz:**
Score normalizado de 0 a 1 para o KRI 1 (% RDP): valor 1 quando RDP <= 1,0%; valor 0 quando RDP >= 2,0%.

**DAX:**
```dax
6.0
```

**Como funciona:**
Usa 0 medida(s) e 0 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** —
**É usada por:** `idx_score_igro_kri5`


### meta_igro_kri1

`_medidas.meta_igro_kri1` · 0.00% · 05 · IGRO · Metas e Goalposts

**O que faz:**
Goalpost do KRI 1 (% RDP): 2,0% como limite de aceitabilidade. Valor 0 quando RDP >= 2,0%.

**DAX:**
```dax
0.01
```

**Como funciona:**
Usa 0 medida(s) e 0 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** —
**É usada por:** `idx_score_igro_kri1`


### meta_igro_kri2

`_medidas.meta_igro_kri2` · #,0.0 · 05 · IGRO · Metas e Goalposts

**O que faz:**
Goalpost do KRI 2 (TMR): 10 dias como limite de aceitabilidade. Valor 0 quando TMR >= 10 dias.

**DAX:**
```dax
5.0
```

**Como funciona:**
Usa 0 medida(s) e 0 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** —
**É usada por:** `idx_score_igro_kri2`


### meta_igro_kri3

`_medidas.meta_igro_kri3` · 0.00% · 05 · IGRO · Metas e Goalposts

**O que faz:**
Goalpost do KRI 3 (TR - Resolutividade): 50% como piso aceitável. Valor 0 quando TR <= 50%.

**DAX:**
```dax
0.70
```

**Como funciona:**
Usa 0 medida(s) e 0 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** —
**É usada por:** `idx_score_igro_kri3`


### meta_igro_kri4

`_medidas.meta_igro_kri4` · 0.00% · 05 · IGRO · Metas e Goalposts

**O que faz:**
Goalpost do KRI 4 (% RI): 3,5% como piso aceitável de insatisfação. Valor 0 quando RI >= 3,5%.

**DAX:**
```dax
0.025
```

**Como funciona:**
Usa 0 medida(s) e 0 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** —
**É usada por:** `idx_score_igro_kri4`


### meta_igro_kri5

`_medidas.meta_igro_kri5` · #,0.0 · 05 · IGRO · Metas e Goalposts

**O que faz:**
Goalpost do KRI 5 (Nota de Recomendação): 6,0 como recomendação aceitável. Valor 0 quando NR <= 6,0.

**DAX:**
```dax
8.0
```

**Como funciona:**
Usa 0 medida(s) e 0 coluna(s) referenciada(s) diretamente. É uma medida-base do modelo ou depende só de colunas.

**Usa:** —
**É usada por:** `idx_score_igro_kri5`


## 06 · IGRO · Scores KRI

### idx_score_igro_kri1

`_medidas.idx_score_igro_kri1` · 0.00% · 06 · IGRO · Scores KRI

**O que faz:**
Score normalizado de 0 a 1 para o KRI 2 (TMR): valor 1 quando TMR <= 5 dias; valor 0 quando TMR >= 10 dias.

**DAX:**
```dax
VAR valor = [ind_pct_mais_30_dias]
VAR meta = [meta_igro_kri1]
VAR goalpost = [goal_igro_kri1]
VAR score = DIVIDE ( goalpost - valor, goalpost - meta, 0 )
RETURN
MIN ( MAX ( score, 0 ), 1 )
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: goal_igro_kri1, ind_pct_mais_30_dias, meta_igro_kri1.

**Usa:** `goal_igro_kri1`, `ind_pct_mais_30_dias`, `meta_igro_kri1`
**É usada por:** `HTML Tabela Resultados IGRO CSV`, `_JSON Orgaos`, `idx_igro_sub_t`


### idx_score_igro_kri2

`_medidas.idx_score_igro_kri2` · 0.00% · 06 · IGRO · Scores KRI

**O que faz:**
Score normalizado de 0 a 1 para o KRI 3 (TR): valor 1 quando TR >= 70%; valor 0 quando TR <= 50%.

**DAX:**
```dax
VAR valor = [ind_media_tempo_resposta]
VAR meta = [meta_igro_kri2]
VAR goalpost = [goal_igro_kri2]
VAR score = DIVIDE ( goalpost - valor, goalpost - meta, 0 )
RETURN
MIN ( MAX ( score, 0 ), 1 )
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: goal_igro_kri2, ind_media_tempo_resposta, meta_igro_kri2.

**Usa:** `goal_igro_kri2`, `ind_media_tempo_resposta`, `meta_igro_kri2`
**É usada por:** `HTML Tabela Resultados IGRO CSV`, `_JSON Orgaos`, `idx_igro_sub_t`


### idx_score_igro_kri3

`_medidas.idx_score_igro_kri3` · 0.00% · 06 · IGRO · Scores KRI

**O que faz:**
Score normalizado de 0 a 1 para o KRI 4 (% RI): valor 1 quando RI <= 2,5%; valor 0 quando RI >= 3,5%.

**DAX:**
```dax
VAR valor = [ind_pct_resolutividade]
VAR meta = [meta_igro_kri3]
VAR goalpost = [goal_igro_kri3]
VAR score = DIVIDE ( valor - goalpost, meta - goalpost, 0 )
RETURN
MIN ( MAX ( score, 0 ), 1 )
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: goal_igro_kri3, ind_pct_resolutividade, meta_igro_kri3.

**Usa:** `goal_igro_kri3`, `ind_pct_resolutividade`, `meta_igro_kri3`
**É usada por:** `HTML Tabela Resultados IGRO CSV`, `_JSON Orgaos`, `idx_igro_sub_q`


### idx_score_igro_kri4

`_medidas.idx_score_igro_kri4` · 0.00% · 06 · IGRO · Scores KRI

**O que faz:**
Score normalizado de 0 a 1 para o KRI 5 (Nota de Recomendação): valor 1 quando NR >= 8,0; valor 0 quando NR <= 6,0.

**DAX:**
```dax
VAR valor = [ind_pct_respostas_insatisfatorias]
VAR meta = [meta_igro_kri4]
VAR goalpost = [goal_igro_kri4]
VAR score = DIVIDE ( goalpost - valor, goalpost - meta, 0 )
RETURN
MIN ( MAX ( score, 0 ), 1 )
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: goal_igro_kri4, ind_pct_respostas_insatisfatorias, meta_igro_kri4.

**Usa:** `goal_igro_kri4`, `ind_pct_respostas_insatisfatorias`, `meta_igro_kri4`
**É usada por:** `HTML Tabela Resultados IGRO CSV`, `_JSON Orgaos`, `idx_igro_sub_q`


### idx_score_igro_kri5

`_medidas.idx_score_igro_kri5` · 0.00% · 06 · IGRO · Scores KRI

**O que faz:**
Subíndice de Tempestividade (IT): média ponderada TMR=60% e % RDP=40%.

**DAX:**
```dax
VAR valor = [ind_media_nota_recomendacao]
VAR meta = [meta_igro_kri5]
VAR goalpost = [goal_igro_kri5]
VAR score = DIVIDE ( valor - goalpost, meta - goalpost, 0 )
RETURN
MIN ( MAX ( score, 0 ), 1 )
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: goal_igro_kri5, ind_media_nota_recomendacao, meta_igro_kri5.

**Usa:** `goal_igro_kri5`, `ind_media_nota_recomendacao`, `meta_igro_kri5`
**É usada por:** `HTML Tabela Resultados IGRO CSV`, `_JSON Orgaos`, `idx_igro_sub_q`


## 07 · IGRO · Índice

### idx_igro

`_medidas.idx_igro` · 0.00% · 07 · IGRO · Índice

**O que faz:**
Respostas de pesquisa com nota de recomendação entre 9 e 10. Numerador do NPS. TREATAS propaga filtro de dOrgao_igro[sigla].

**DAX:**
```dax
VAR sub_t = [idx_igro_sub_t]
VAR sub_q = [idx_igro_sub_q]
VAR resultado =
IF (
AND ( sub_t > 0, sub_q > 0 ),
SQRT ( sub_t * sub_q ),
0
)
RETURN
MIN ( MAX ( resultado, 0 ), 1 )
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro_sub_q, idx_igro_sub_t.

**Usa:** `idx_igro_sub_q`, `idx_igro_sub_t`
**É usada por:** `HTML Dashboard Final Base`, `HTML Matriz Classes IGRO`, `HTML Tabela Resultados IGRO CSV`, `_JSON KPIs`, `_JSON Orgaos`, `fmt_cor_fonte_igro`, `fmt_cor_fundo_igro`, `fmt_semaforo_igro`, `lbl_igro`, `var_igro`


### idx_igro_sub_q

`_medidas.idx_igro_sub_q` · 0.00% · 07 · IGRO · Índice

**O que faz:**
Índice de Gestão de Riscos de Ouvidorias. Média geométrica simples: √(IT × IQ). Conforme metodologia IGRO — artigo CGU.

**DAX:**
```dax
VAR numerador =
0.40 * [idx_score_igro_kri3]
+ 0.30 * [idx_score_igro_kri4]
+ 0.30 * [idx_score_igro_kri5]
RETURN
MIN ( MAX ( numerador, 0 ), 1 )
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_score_igro_kri3, idx_score_igro_kri4, idx_score_igro_kri5.

**Usa:** `idx_score_igro_kri3`, `idx_score_igro_kri4`, `idx_score_igro_kri5`
**É usada por:** `HTML Dashboard Final Base`, `HTML Matriz Classes IGRO`, `HTML Tabela Resultados IGRO CSV`, `_JSON KPIs`, `_JSON Orgaos`, `fmt_cor_fundo_igro_sub_q`, `fmt_semaforo_igro_sub_q`, `idx_igro`, `lbl_igro_sub_q`, `var_igro_sub_q`


### idx_igro_sub_t

`_medidas.idx_igro_sub_t` · 0.00% · 07 · IGRO · Índice

**O que faz:**
Subíndice de Qualidade (IQ): média ponderada TR=40%, % RI=30% e Nota de Recomendação=30%.

**DAX:**
```dax
VAR numerador =
0.60 * [idx_score_igro_kri2]
+ 0.40 * [idx_score_igro_kri1]
RETURN
MIN ( MAX ( numerador, 0 ), 1 )
```

**Como funciona:**
Usa 2 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_score_igro_kri1, idx_score_igro_kri2.

**Usa:** `idx_score_igro_kri1`, `idx_score_igro_kri2`
**É usada por:** `HTML Dashboard Final Base`, `HTML Matriz Classes IGRO`, `HTML Tabela Resultados IGRO CSV`, `_JSON KPIs`, `_JSON Orgaos`, `fmt_cor_fundo_igro_sub_t`, `fmt_semaforo_igro_sub_t`, `idx_igro`, `lbl_igro_sub_t`, `var_igro_sub_t`


## 08 · Formatação

### fmt_cor_fonte_igro

`_medidas.fmt_cor_fonte_igro` · sem format string · 08 · Formatação

**O que faz:**
Cor de fundo hexadecimal para o Sub-T conforme faixas da metodologia IGRO (artigo CGU).

**DAX:**
```dax
VAR v = [idx_igro]
RETURN SWITCH(TRUE(), v >= 0.80, "#27500A", v >= 0.60, "#633806", v >= 0.40, "#712B13", "#791F1F")
```

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro.

**Usa:** `idx_igro`
**É usada por:** —


### fmt_cor_fonte_nps

`_medidas.fmt_cor_fonte_nps` · sem format string · 08 · Formatação

**O que faz:**
Rótulo de semáforo para ind_pct_procedencia: Verde (≥60%), Amarelo (40–59%), Laranja (20–39%), Vermelho (<20%).

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: ind_nps.

**Usa:** `ind_nps`
**É usada por:** —


### fmt_cor_fundo_igro

`_medidas.fmt_cor_fundo_igro` · @ · 08 · Formatação

**O que faz:**
Cor de fonte hexadecimal para o IGRO conforme faixa de risco. Usar em formatação condicional de cor de fonte.

**DAX:**
```dax
VAR v = [idx_igro]
RETURN
IF ( ISBLANK(v), BLANK(),
IF ( v >= 0.90, "#27AE60",
IF ( v >= 0.70, "#F39C12",
IF ( v >= 0.50, "#E67E22", "#E74C3C" ))))
```

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro.

**Usa:** `idx_igro`
**É usada por:** —


### fmt_cor_fundo_igro_sub_q

`_medidas.fmt_cor_fundo_igro_sub_q` · @ · 08 · Formatação

**O que faz:**
Variação absoluta do TMR vs. período anterior. Negativo = melhora (menos dias).

**DAX:**
```dax
VAR v = [idx_igro_sub_q]
RETURN
IF ( ISBLANK(v), BLANK(),
IF ( v >= 0.90, "#27AE60",
IF ( v >= 0.70, "#F39C12",
IF ( v >= 0.50, "#E67E22", "#E74C3C" ))))
```

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro_sub_q.

**Usa:** `idx_igro_sub_q`
**É usada por:** —


### fmt_cor_fundo_igro_sub_t

`_medidas.fmt_cor_fundo_igro_sub_t` · @ · 08 · Formatação

**O que faz:**
Cor de fundo hexadecimal para o Sub-Q conforme faixas da metodologia IGRO (artigo CGU).

**DAX:**
```dax
VAR v = [idx_igro_sub_t]
RETURN
IF ( ISBLANK(v), BLANK(),
IF ( v >= 0.90, "#27AE60",
IF ( v >= 0.70, "#F39C12",
IF ( v >= 0.50, "#E67E22", "#E74C3C" ))))
```

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro_sub_t.

**Usa:** `idx_igro_sub_t`
**É usada por:** —


### fmt_cor_fundo_nps

`_medidas.fmt_cor_fundo_nps` · sem format string · 08 · Formatação

**O que faz:**
Cor de fonte hexadecimal para o NPS conforme faixa.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: ind_nps.

**Usa:** `ind_nps`
**É usada por:** —


### fmt_semaforo_igro

`_medidas.fmt_semaforo_igro` · @ · 08 · Formatação

**O que faz:**
Rótulo de semáforo para o Sub-T com faixas da metodologia IGRO (artigo CGU).

**DAX:**
```dax
VAR v = [idx_igro]
RETURN
IF ( ISBLANK(v), BLANK(),
IF ( v >= 0.90, "Controlado",
IF ( v >= 0.70, "Em atenção",
IF ( v >= 0.50, "Elevado", "Crítico" ))))
```

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro.

**Usa:** `idx_igro`
**É usada por:** —


### fmt_semaforo_igro_sub_q

`_medidas.fmt_semaforo_igro_sub_q` · @ · 08 · Formatação

**O que faz:**
Cor de fundo hexadecimal para o IGRO conforme faixas da metodologia (artigo CGU). Controlado=#27AE60, Em atenção=#F39C12, Elevado=#E67E22, Crítico=#E74C3C.

**DAX:**
```dax
VAR v = [idx_igro_sub_q]
RETURN
IF ( ISBLANK(v), BLANK(),
IF ( v >= 0.90, "Controlado",
IF ( v >= 0.70, "Em atenção",
IF ( v >= 0.50, "Elevado", "Crítico" ))))
```

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro_sub_q.

**Usa:** `idx_igro_sub_q`
**É usada por:** —


### fmt_semaforo_igro_sub_t

`_medidas.fmt_semaforo_igro_sub_t` · @ · 08 · Formatação

**O que faz:**
Rótulo de semáforo para o Sub-Q com faixas da metodologia IGRO (artigo CGU).

**DAX:**
```dax
VAR v = [idx_igro_sub_t]
RETURN
IF ( ISBLANK(v), BLANK(),
IF ( v >= 0.90, "Controlado",
IF ( v >= 0.70, "Em atenção",
IF ( v >= 0.50, "Elevado", "Crítico" ))))
```

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro_sub_t.

**Usa:** `idx_igro_sub_t`
**É usada por:** —


### fmt_semaforo_nps

`_medidas.fmt_semaforo_nps` · sem format string · 08 · Formatação

**O que faz:**
Cor de fundo hexadecimal para o NPS conforme faixa.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: ind_nps.

**Usa:** `ind_nps`
**É usada por:** —


### fmt_semaforo_procedencia

`_medidas.fmt_semaforo_procedencia` · sem format string · 08 · Formatação

**O que faz:**
Rótulo de semáforo para ind_pct_recurso: Verde (≤1%), Amarelo (1–3%), Laranja (3–5%), Vermelho (>5%).

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: ind_pct_procedencia.

**Usa:** `ind_pct_procedencia`
**É usada por:** —


### fmt_semaforo_recurso

`_medidas.fmt_semaforo_recurso` · sem format string · 08 · Formatação

**O que faz:**
Rótulo de semáforo para o IGRO conforme faixas da metodologia (artigo CGU): Verde ≥90%, Amarelo 70–89%, Laranja 50–69%, Vermelho <50%.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: ind_pct_recurso.

**Usa:** `ind_pct_recurso`
**É usada por:** —


## 09 · Variação

### var_cobertura_reclamacao

`_medidas.var_cobertura_reclamacao` · 0.00% · 09 · Variação

**O que faz:**
Semáforo do TMR com polaridade negativa: 🟢 quando cai (melhora), 🔴 quando sobe (piora). Neutro quando variação = 0 ou BLANK.

**DAX:**
```dax
VAR atual = [ind_pct_cobertura_reclamacao]
VAR anterior = CALCULATE([ind_pct_cobertura_reclamacao], PREVIOUSYEAR(f_pesquisa[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: ind_pct_cobertura_reclamacao.

**Usa:** `ind_pct_cobertura_reclamacao`, `CALCULATE([ind_pct_cobertura_reclamacao]`, `PREVIOUSYEAR(f_pesquisa[data_manifestacao]`
**É usada por:** `sem_cobertura_reclamacao`


### var_igro

`_medidas.var_igro` · 0.00% · 09 · Variação

**O que faz:**
Variação absoluta do Sub-T vs. período anterior. Positivo = melhora.

**DAX:**
```dax
VAR atual = [idx_igro]
VAR anterior = CALCULATE([idx_igro], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro.

**Usa:** `idx_igro`, `CALCULATE([idx_igro]`, `PREVIOUSYEAR(f_relatorio[data_manifestacao]`
**É usada por:** `lbl_igro`, `sem_igro`


### var_igro_sub_q

`_medidas.var_igro_sub_q` · 0.00% · 09 · Variação

**O que faz:**
Variação absoluta do % de recurso vs. período anterior. Negativo = melhora.

**DAX:**
```dax
VAR atual = [idx_igro_sub_q]
VAR anterior = CALCULATE([idx_igro_sub_q], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro_sub_q.

**Usa:** `idx_igro_sub_q`, `CALCULATE([idx_igro_sub_q]`, `PREVIOUSYEAR(f_relatorio[data_manifestacao]`
**É usada por:** `lbl_igro_sub_q`, `sem_igro_sub_q`


### var_igro_sub_t

`_medidas.var_igro_sub_t` · 0.00% · 09 · Variação

**O que faz:**
Variação absoluta do Sub-Q vs. período anterior. Positivo = melhora.

**DAX:**
```dax
VAR atual = [idx_igro_sub_t]
VAR anterior = CALCULATE([idx_igro_sub_t], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro_sub_t.

**Usa:** `idx_igro_sub_t`, `CALCULATE([idx_igro_sub_t]`, `PREVIOUSYEAR(f_relatorio[data_manifestacao]`
**É usada por:** `lbl_igro_sub_t`, `sem_igro_sub_t`


### var_insatisfatorias

`_medidas.var_insatisfatorias` · 0.00% · 09 · Variação

**O que faz:**
Variação absoluta da nota média de recomendação vs. período anterior. Positivo = melhora.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 3 coluna(s) referenciada(s) diretamente. Dependências principais: ind_pct_respostas_insatisfatorias.

**Usa:** `ind_pct_respostas_insatisfatorias`, `MAX(dCalendario[Date]`, `MIN(dCalendario[Date]`, `dCalendario[Date]`
**É usada por:** `lbl_insatisfatorias`, `sem_insatisfatorias`


### var_nota

`_medidas.var_nota` · #,0.0 · 09 · Variação

**O que faz:**
Variação absoluta do NPS vs. período anterior. Positivo = melhora.

**DAX:**
```dax
VAR atual = [ind_media_nota_recomendacao]
VAR anterior = CALCULATE([ind_media_nota_recomendacao], PREVIOUSYEAR(f_pesquisa[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: ind_media_nota_recomendacao.

**Usa:** `ind_media_nota_recomendacao`, `CALCULATE([ind_media_nota_recomendacao]`, `PREVIOUSYEAR(f_pesquisa[data_manifestacao]`
**É usada por:** `lbl_nota`, `sem_nota`


### var_nps

`_medidas.var_nps` · #,0.0 · 09 · Variação

**O que faz:**
Variação absoluta do IGRO vs. período anterior. Positivo = melhora.

**DAX:**
```dax
VAR atual = [ind_nps]
VAR anterior = CALCULATE([ind_nps], PREVIOUSYEAR(f_pesquisa[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: ind_nps.

**Usa:** `ind_nps`, `CALCULATE([ind_nps]`, `PREVIOUSYEAR(f_pesquisa[data_manifestacao]`
**É usada por:** `HTML Dashboard Final Base`, `lbl_nps`, `sem_nps`


### var_pct_mais_30_dias

`_medidas.var_pct_mais_30_dias` · 0.00% · 09 · Variação

**O que faz:**
Variação absoluta da resolutividade vs. período anterior. Positivo = melhora.

**DAX:**
```dax
VAR atual = [ind_pct_mais_30_dias]
VAR anterior = CALCULATE([ind_pct_mais_30_dias], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: ind_pct_mais_30_dias.

**Usa:** `ind_pct_mais_30_dias`, `CALCULATE([ind_pct_mais_30_dias]`, `PREVIOUSYEAR(f_relatorio[data_manifestacao]`
**É usada por:** `lbl_pct_mais_30_dias`, `sem_pct_mais_30_dias`


### var_recurso

`_medidas.var_recurso` · 0.00% · 09 · Variação

**O que faz:**
Variação absoluta da cobertura de pesquisa em Reclamações vs. período anterior. Positivo = melhora.

**DAX:**
```dax
VAR atual = [ind_pct_recurso]
VAR anterior = CALCULATE([ind_pct_recurso], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: ind_pct_recurso.

**Usa:** `ind_pct_recurso`, `CALCULATE([ind_pct_recurso]`, `PREVIOUSYEAR(f_relatorio[data_manifestacao]`
**É usada por:** `sem_recurso`


### var_resolutividade

`_medidas.var_resolutividade` · 0.00% · 09 · Variação

**O que faz:**
Variação absoluta do % de respostas insatisfatórias vs. período anterior. Negativo = melhora. Eixo temporal via dCalendario (corrigido).

**DAX:**
```dax
VAR atual = [ind_pct_resolutividade]
VAR anterior = CALCULATE([ind_pct_resolutividade], PREVIOUSYEAR(f_pesquisa[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: ind_pct_resolutividade.

**Usa:** `ind_pct_resolutividade`, `CALCULATE([ind_pct_resolutividade]`, `PREVIOUSYEAR(f_pesquisa[data_manifestacao]`
**É usada por:** `lbl_resolutividade`, `sem_resolutividade`


### var_tmr

`_medidas.var_tmr` · #,0.0 · 09 · Variação

**O que faz:**
Variação absoluta do % de manifestações com mais de 30 dias vs. período anterior. Negativo = melhora.

**DAX:**
```dax
VAR atual = [ind_media_tempo_resposta]
VAR anterior = CALCULATE([ind_media_tempo_resposta], PREVIOUSYEAR(f_relatorio[data_manifestacao]))
RETURN IF(ISBLANK(anterior), BLANK(), atual - anterior)
```

**Como funciona:**
Usa 1 medida(s) e 2 coluna(s) referenciada(s) diretamente. Dependências principais: ind_media_tempo_resposta.

**Usa:** `ind_media_tempo_resposta`, `CALCULATE([ind_media_tempo_resposta]`, `PREVIOUSYEAR(f_relatorio[data_manifestacao]`
**É usada por:** `lbl_tmr`, `sem_tmr`


## 10 · Semáforo · Variação

### sem_cobertura_reclamacao

`_medidas.sem_cobertura_reclamacao` · sem format string · 10 · Semáforo · Variação

**O que faz:**
Rótulo completo para cartão do TMR: valor atual + semáforo + delta formatado.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: var_cobertura_reclamacao.

**Usa:** `var_cobertura_reclamacao`
**É usada por:** —


### sem_igro

`_medidas.sem_igro` · sem format string · 10 · Semáforo · Variação

**O que faz:**
Semáforo do Sub-T com polaridade positiva.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: var_igro.

**Usa:** `var_igro`
**É usada por:** `lbl_igro`


### sem_igro_sub_q

`_medidas.sem_igro_sub_q` · sem format string · 10 · Semáforo · Variação

**O que faz:**
Semáforo do % de recurso com polaridade negativa: 🟢 quando cai.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: var_igro_sub_q.

**Usa:** `var_igro_sub_q`
**É usada por:** `lbl_igro_sub_q`


### sem_igro_sub_t

`_medidas.sem_igro_sub_t` · sem format string · 10 · Semáforo · Variação

**O que faz:**
Semáforo do Sub-Q com polaridade positiva.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: var_igro_sub_t.

**Usa:** `var_igro_sub_t`
**É usada por:** `lbl_igro_sub_t`


### sem_insatisfatorias

`_medidas.sem_insatisfatorias` · sem format string · 10 · Semáforo · Variação

**O que faz:**
Semáforo da nota média com polaridade positiva: 🟢 quando sobe.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: var_insatisfatorias.

**Usa:** `var_insatisfatorias`
**É usada por:** `lbl_insatisfatorias`


### sem_nota

`_medidas.sem_nota` · sem format string · 10 · Semáforo · Variação

**O que faz:**
Semáforo do NPS com polaridade positiva: 🟢 quando sobe.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: var_nota.

**Usa:** `var_nota`
**É usada por:** `lbl_nota`


### sem_nps

`_medidas.sem_nps` · sem format string · 10 · Semáforo · Variação

**O que faz:**
Semáforo do IGRO com polaridade positiva: 🟢 quando sobe.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: var_nps.

**Usa:** `var_nps`
**É usada por:** `lbl_nps`


### sem_pct_mais_30_dias

`_medidas.sem_pct_mais_30_dias` · sem format string · 10 · Semáforo · Variação

**O que faz:**
Semáforo da resolutividade com polaridade positiva: 🟢 quando sobe.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: var_pct_mais_30_dias.

**Usa:** `var_pct_mais_30_dias`
**É usada por:** `lbl_pct_mais_30_dias`


### sem_recurso

`_medidas.sem_recurso` · sem format string · 10 · Semáforo · Variação

**O que faz:**
Semáforo da cobertura de pesquisa em Reclamações com polaridade positiva: 🟢 quando sobe.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: var_recurso.

**Usa:** `var_recurso`
**É usada por:** —


### sem_resolutividade

`_medidas.sem_resolutividade` · sem format string · 10 · Semáforo · Variação

**O que faz:**
Semáforo das respostas insatisfatórias com polaridade negativa: 🟢 quando cai.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: var_resolutividade.

**Usa:** `var_resolutividade`
**É usada por:** `lbl_resolutividade`


### sem_tmr

`_medidas.sem_tmr` · sem format string · 10 · Semáforo · Variação

**O que faz:**
Semáforo do % +30 dias com polaridade negativa: 🟢 quando cai.

**DAX:**
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

**Como funciona:**
Usa 1 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: var_tmr.

**Usa:** `var_tmr`
**É usada por:** `lbl_tmr`


## 11 · Rótulo · Cartão

### lbl_igro

`_medidas.lbl_igro` · sem format string · 11 · Rótulo · Cartão

**O que faz:**
Rótulo completo para cartão do Sub-T.

**DAX:**
```dax
VAR valor = [idx_igro]
VAR delta = [var_igro]
VAR emoji = [sem_igro]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro, sem_igro, var_igro.

**Usa:** `idx_igro`, `sem_igro`, `var_igro`
**É usada por:** —


### lbl_igro_sub_q

`_medidas.lbl_igro_sub_q` · sem format string · 11 · Rótulo · Cartão

**O que faz:**
Array JSON com IGRO e KRIs por órgão, ordenado por IGRO desc. Usa SUMMARIZE com colunas calculadas.

**DAX:**
```dax
VAR valor = [idx_igro_sub_q]
VAR delta = [var_igro_sub_q]
VAR emoji = [sem_igro_sub_q]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro_sub_q, sem_igro_sub_q, var_igro_sub_q.

**Usa:** `idx_igro_sub_q`, `sem_igro_sub_q`, `var_igro_sub_q`
**É usada por:** —


### lbl_igro_sub_t

`_medidas.lbl_igro_sub_t` · sem format string · 11 · Rótulo · Cartão

**O que faz:**
Rótulo completo para cartão do Sub-Q.

**DAX:**
```dax
VAR valor = [idx_igro_sub_t]
VAR delta = [var_igro_sub_t]
VAR emoji = [sem_igro_sub_t]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: idx_igro_sub_t, sem_igro_sub_t, var_igro_sub_t.

**Usa:** `idx_igro_sub_t`, `sem_igro_sub_t`, `var_igro_sub_t`
**É usada por:** —


### lbl_insatisfatorias

`_medidas.lbl_insatisfatorias` · sem format string · 11 · Rótulo · Cartão

**O que faz:**
Rótulo completo para cartão da nota média.

**DAX:**
```dax
VAR valor = [ind_pct_respostas_insatisfatorias]
VAR delta = [var_insatisfatorias]
VAR emoji = [sem_insatisfatorias]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: ind_pct_respostas_insatisfatorias, sem_insatisfatorias, var_insatisfatorias.

**Usa:** `ind_pct_respostas_insatisfatorias`, `sem_insatisfatorias`, `var_insatisfatorias`
**É usada por:** —


### lbl_nota

`_medidas.lbl_nota` · sem format string · 11 · Rótulo · Cartão

**O que faz:**
Rótulo completo para cartão do NPS.

**DAX:**
```dax
VAR valor = [ind_media_nota_recomendacao]
VAR delta = [var_nota]
VAR emoji = [sem_nota]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0") & ")")
RETURN
emoji & " " & FORMAT(valor, "0.0") & delta_fmt
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: ind_media_nota_recomendacao, sem_nota, var_nota.

**Usa:** `ind_media_nota_recomendacao`, `sem_nota`, `var_nota`
**É usada por:** —


### lbl_nps

`_medidas.lbl_nps` · sem format string · 11 · Rótulo · Cartão

**O que faz:**
Rótulo completo para cartão do IGRO.

**DAX:**
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

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: ind_nps, sem_nps, var_nps.

**Usa:** `ind_nps`, `sem_nps`, `var_nps`
**É usada por:** —


### lbl_pct_mais_30_dias

`_medidas.lbl_pct_mais_30_dias` · sem format string · 11 · Rótulo · Cartão

**O que faz:**
Rótulo completo para cartão da resolutividade.

**DAX:**
```dax
VAR valor = [ind_pct_mais_30_dias]
VAR delta = [var_pct_mais_30_dias]
VAR emoji = [sem_pct_mais_30_dias]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: ind_pct_mais_30_dias, sem_pct_mais_30_dias, var_pct_mais_30_dias.

**Usa:** `ind_pct_mais_30_dias`, `sem_pct_mais_30_dias`, `var_pct_mais_30_dias`
**É usada por:** —


### lbl_resolutividade

`_medidas.lbl_resolutividade` · sem format string · 11 · Rótulo · Cartão

**O que faz:**
Rótulo completo para cartão das respostas insatisfatórias.

**DAX:**
```dax
VAR valor = [ind_pct_resolutividade]
VAR delta = [var_resolutividade]
VAR emoji = [sem_resolutividade]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0%") & ")")
RETURN
emoji & " " & FORMAT(valor, "0.0%") & delta_fmt
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: ind_pct_resolutividade, sem_resolutividade, var_resolutividade.

**Usa:** `ind_pct_resolutividade`, `sem_resolutividade`, `var_resolutividade`
**É usada por:** —


### lbl_tmr

`_medidas.lbl_tmr` · sem format string · 11 · Rótulo · Cartão

**O que faz:**
Rótulo completo para cartão do % +30 dias.

**DAX:**
```dax
VAR valor = [ind_media_tempo_resposta]
VAR delta = [var_tmr]
VAR emoji = [sem_tmr]
VAR sinal = IF(delta > 0, "+", "")
VAR delta_fmt = IF(ISBLANK(delta), "", " (" & sinal & FORMAT(delta, "0.0") & "d)")
RETURN
emoji & " " & FORMAT(valor, "0.0") & "d" & delta_fmt
```

**Como funciona:**
Usa 3 medida(s) e 0 coluna(s) referenciada(s) diretamente. Dependências principais: ind_media_tempo_resposta, sem_tmr, var_tmr.

**Usa:** `ind_media_tempo_resposta`, `sem_tmr`, `var_tmr`
**É usada por:** —


## 12 · JSON · Dashboard

### _JSON KPIs

`_medidas._JSON KPIs` · sem format string · 12 · JSON · Dashboard

**O que faz:**
Dashboard HTML interativo do IGRO. Tema dark, cards KPI, ranking de órgãos, distribuição por tipo, tabela com busca e export CSV.

**DAX:**
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
VAR _pesq  = SUBSTITUTE(FORMAT([base_qtd_pesquisa], "0"), ",", ".")
VAR _prc   = SUBSTITUTE(FORMAT([ind_pct_procedencia], "0.0000"), ",", ".")
VAR _rec   = SUBSTITUTE(FORMAT([ind_pct_recurso], "0.0000"), ",", ".")
RETURN
"{" &
"""igro"": "    & _igro  & "," &
"""sub_t"": "   & _sub_t & "," &
"""sub_q"": "   & _sub_q & "," &
"""tmr"": "     & _tmr   & "," &
"""res"": "     & _res   & "," &
"""nota"": "    & _nota  & "," &
"""ins"": "     & _ins   & "," &
"""nps"": "     & _nps   & "," &
"""p30"": "     & _p30   & "," &
"""total"": "   & _tot   & "," &
"""pesq"": "    & _pesq  & "," &
"""proc"": "    & _prc   & "," &
"""recurso"": " & _rec   &
"}"
```

**Como funciona:**
Usa 13 medida(s) e 13 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes, base_qtd_pesquisa, idx_igro, idx_igro_sub_q, idx_igro_sub_t, ind_media_nota_recomendacao, ind_media_tempo_resposta, ind_nps.

**Usa:** `base_qtd_manifestacoes`, `base_qtd_pesquisa`, `idx_igro`, `idx_igro_sub_q`, `idx_igro_sub_t`, `ind_media_nota_recomendacao`, `ind_media_tempo_resposta`, `ind_nps`, `ind_pct_mais_30_dias`, `ind_pct_procedencia`, `ind_pct_recurso`, `ind_pct_resolutividade`
**É usada por:** —


### _JSON Orgaos

`_medidas._JSON Orgaos` · sem format string · 12 · JSON · Dashboard

**O que faz:**
Array JSON com distribuição por tipo de manifestação.

**DAX:**
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
"_ins",   [ind_pct_respostas_insatisfatorias],
"_nps",   [ind_nps],
"_k1",    [idx_score_igro_kri1],
"_k2",    [idx_score_igro_kri2],
"_k3",    [idx_score_igro_kri3],
"_k4",    [idx_score_igro_kri4],
"_k5",    [idx_score_igro_kri5]
)
VAR _s = TOPN(60, _t, [_igro], DESC)
RETURN
"[" &
CONCATENATEX(
_s,
"{" &
"""s"":"""
& SUBSTITUTE(f_relatorio[sigla], """", "'") & """," &
"""n"":" & SUBSTITUTE(FORMAT([_qtd],  "0"),      ",", ".") & "," &
"""i"":" & SUBSTITUTE(FORMAT([_igro], "0.0000"), ",", ".") & "," &
"""t"":" & SUBSTITUTE(FORMAT([_sub_t],"0.0000"), ",", ".") & "," &
"""q"":" & SUBSTITUTE(FORMAT([_sub_q],"0.0000"), ",", ".") & "," &
"""m"":" & SUBSTITUTE(FORMAT([_tmr],  "0.00"),   ",", ".") & "," &
"""r"":" & SUBSTITUTE(FORMAT([_res],  "0.0000"), ",", ".") & "," &
"""a"":" & SUBSTITUTE(FORMAT([_nota], "0.00"),   ",", ".") & "," &
"""x"":" & SUBSTITUTE(FORMAT([_ins],  "0.0000"), ",", ".") & "," &
"""p"":" & SUBSTITUTE(FORMAT([_nps],  "0.00"),   ",", ".") & "," &
"""k1"":"& SUBSTITUTE(FORMAT([_k1],  "0.0000"), ",", ".") & "," &
"""k2"":"& SUBSTITUTE(FORMAT([_k2],  "0.0000"), ",", ".") & "," &
"""k3"":"& SUBSTITUTE(FORMAT([_k3],  "0.0000"), ",", ".") & "," &
"""k4"":"& SUBSTITUTE(FORMAT([_k4],  "0.0000"), ",", ".") & "," &
"""k5"":"& SUBSTITUTE(FORMAT([_k5],  "0.0000"), ",", ".") &
"}",
",",
[_igro], DESC
) &
"]"
```

**Como funciona:**
Usa 14 medida(s) e 16 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes, idx_igro, idx_igro_sub_q, idx_igro_sub_t, idx_score_igro_kri1, idx_score_igro_kri2, idx_score_igro_kri3, idx_score_igro_kri4.

**Usa:** `base_qtd_manifestacoes`, `idx_igro`, `idx_igro_sub_q`, `idx_igro_sub_t`, `idx_score_igro_kri1`, `idx_score_igro_kri2`, `idx_score_igro_kri3`, `idx_score_igro_kri4`, `idx_score_igro_kri5`, `ind_media_nota_recomendacao`, `ind_media_tempo_resposta`, `ind_nps`
**É usada por:** `HTML Dashboard IGRO`


### _JSON Tipos

`_medidas._JSON Tipos` · sem format string · 12 · JSON · Dashboard

**O que faz:**
Array JSON com KPIs globais da rede para injeção direta nos cards do dashboard.

**DAX:**
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
"[" &
CONCATENATEX(
_s,
"{" &
"""tipo"":"""
& SUBSTITUTE(f_relatorio[tipo_manifestacao], """", "'") & """," &
"""n"":"    & SUBSTITUTE(FORMAT([_qtd],  "0"),      ",", ".") & "," &
"""ins"":"  & SUBSTITUTE(FORMAT([_ins],  "0"),      ",", ".") & "," &
"""pesq"":" & SUBSTITUTE(FORMAT([_pesq], "0"),      ",", ".") & "," &
"""pct"":"  & SUBSTITUTE(FORMAT(DIVIDE([_qtd], _tot, 0), "0.0000"), ",", ".") &
"}",
",",
[_qtd], DESC
) &
"]"
```

**Como funciona:**
Usa 3 medida(s) e 6 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes, base_qtd_pesquisa, base_qtd_respostas_insatisfatorias.

**Usa:** `base_qtd_manifestacoes`, `base_qtd_pesquisa`, `base_qtd_respostas_insatisfatorias`, `SUBSTITUTE(FORMAT(DIVIDE([_qtd]`, `SUBSTITUTE(FORMAT([_ins]`, `SUBSTITUTE(FORMAT([_pesq]`, `SUBSTITUTE(FORMAT([_qtd]`, `SUBSTITUTE(f_relatorio[tipo_manifestacao]`, `f_relatorio[tipo_manifestacao]`
**É usada por:** `HTML Dashboard IGRO`


### HTML Dashboard Final

`_medidas.HTML Dashboard Final` · sem format string · 12 · JSON · Dashboard

**O que faz:**
Tabela/matriz HTML com dados em literal JS, filtros e exportação CSV dos resultados calculados por órgão.

**DAX:**
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
VAR _html1 = SUBSTITUTE ( _htmlIg, _oldNps, _newNps )
VAR _html2 = SUBSTITUTE ( _html1, _oldDist, _newDist )
VAR _html3 = SUBSTITUTE ( _html2, _oldComp, _newComp )
VAR _renderOld = "function render(d,label){el('nps-v').textContent=parseFloat(d.n).toFixed(0);"
VAR _renderNew = "function render(d,label){const _n=parseFloat(d.n);const _fmtNps=_n<0?'-'+Math.abs(Math.round(_n)):String(Math.round(_n));const _igp=parseFloat(d.ig)*100;const _igLbl=_igp>=90?'Controlado':_igp>=70?'Em atencao':_igp>=50?'Elevado':'Critico';const _igCls=_igp>=90?'ok':_igp>=70?'att':_igp>=50?'elev':'crit';if(el('ig-badge')){el('ig-badge').textContent=_igLbl;el('ig-badge').className='ig-badge '+_igCls;}const _norm=Math.min(1,Math.max(0,(_n+100)/200));const _ang=Math.PI-(Math.PI*_norm);const _nx=160+84*Math.cos(_ang);const _ny=160-84*Math.sin(_ang);if(el('nps-needle')){el('nps-needle').setAttribute('x2',_nx.toFixed(1));el('nps-needle').setAttribute('y2',_ny.toFixed(1));}if(el('nps-band')){el('nps-band').textContent=_n>=50?'Alto':_n>=0?'Medio':'Baixo';}if(el('dist-nps')){el('dist-nps').textContent=_fmtNps;}if(el('dist-nps-2')){el('dist-nps-2').textContent=_fmtNps;}if(el('dist-q')){el('dist-q').textContent=fn0(d.q);}if(el('dist-q2')){el('dist-q2').textContent=fn0(d.q);}const clamp=(x)=>Math.max(0,Math.min(1,x));const _m=parseFloat(d.m),_t=parseFloat(d.t),_r=parseFloat(d.r),_i=parseFloat(d.i),_nt=parseFloat(d.nt);const _rk1=clamp(_m<=0.01?1:_m>=0.02?0:(0.02-_m)/0.01);const _rk2=clamp(_t<=5?1:_t>=10?0:(10-_t)/5);const _rk3=clamp(_r>=0.70?1:_r<=0.50?0:(_r-0.50)/0.20);const _rk4=clamp(_i<=0.025?1:_i>=0.035?0:(0.035-_i)/0.01);const _rk5=clamp(_nt>=8?1:_nt<=6?0:(_nt-6)/2);const _angles=[-90,-18,54,126,198],_vals=[_rk1,_rk2,_rk3,_rk4,_rk5],_pts=[];for(let j=0;j<5;j++){const a=_angles[j]*Math.PI/180,x=120+76*_vals[j]*Math.cos(a),y=105+76*_vals[j]*Math.sin(a);_pts.push(x.toFixed(1)+','+y.toFixed(1));const c=el('ra-'+(j+1));if(c){c.setAttribute('cx',x.toFixed(1));c.setAttribute('cy',y.toFixed(1));}}if(el('ra-poly')){el('ra-poly').setAttribute('points',_pts.join(' '));}if(el('rk1')){el('rk1').textContent=Math.round(_rk1*100)+'%';el('rv1').textContent='Atual: '+(_m*100).toFixed(1)+'%';el('rk2').textContent=Math.round(_rk2*100)+'%';el('rv2').textContent='Atual: '+_t.toFixed(2)+' dias';el('rk3').textContent=Math.round(_rk3*100)+'%';el('rv3').textContent='Atual: '+(_r*100).toFixed(1)+'%';el('rk4').textContent=Math.round(_rk4*100)+'%';el('rv4').textContent='Atual: '+(_i*100).toFixed(1)+'%';el('rk5').textContent=Math.round(_rk5*100)+'%';el('rv5').textContent='Atual: '+_nt.toFixed(2);}el('nps-v').textContent=_fmtNps;"
VAR _html4 = SUBSTITUTE ( _html3, _renderOld, _renderNew )
RETURN
_html4
& "<style>"
& "body,.dash,.card,.card span,.card b,.donut-leg,.donut-leg span,.donut-leg b,.leg-item,.bar-label,.bar-label span,.sub b,.ctx-badge{color:#e2e8f0!important;}"
& ".card .sub,.ksub,.lbl,.fbar label{color:#b8cad1!important;}"
& ".bar-label span[id],#bar-p,#bar-n,#bar-d,#nota-v,#lg-p,#lg-n,#lg-d,#qtd-t,#tot-v{color:#ffffff!important;}"
& ".grid2{align-items:stretch!important}.card{background:#10373b!important;border-color:#1f646d!important;border-radius:14px!important}"
& ".ig-card-top{display:flex;justify-content:center;align-items:center;gap:8px;margin-bottom:4px}.ig-card-top .lbl{margin-bottom:0}.ig-badge{display:inline-flex;align-items:center;border-radius:999px;padding:3px 8px;font-size:9px;font-weight:800;text-transform:uppercase;letter-spacing:.35px;border:1px solid rgba(255,255,255,.16)}.ig-badge.ok{color:#10b981!important;background:rgba(16,185,129,.12);border-color:rgba(16,185,129,.35)}.ig-badge.att{color:#f2c94c!important;background:rgba(242,201,76,.12);border-color:rgba(242,201,76,.4)}.ig-badge.elev{color:#fb923c!important;background:rgba(251,146,60,.12);border-color:rgba(251,146,60,.35)}.ig-badge.crit{color:#ef4444!important;background:rgba(239,68,68,.12);border-color:rgba(239,68,68,.35)}"
& ".nps-alt{background:radial-gradient(circle at 20% 0,rgba(34,211,238,.20),transparent 32%),linear-gradient(145deg,#083545,#07313b)!important;border-color:#2b7180!important;display:grid;grid-template-columns:1.55fr .95fr;gap:16px;min-height:250px}"
& ".nps-copy{font-size:12px;line-height:1.35;color:#e5f6fa!important;margin-bottom:8px;max-width:290px}"
& ".nps-gauge svg{width:100%;max-width:330px;height:auto;display:block;margin:auto}.arc{fill:none;stroke-width:36;stroke-linecap:butt}.arc-low{stroke:#ff4d2d}.arc-mid{stroke:#f7b941}.arc-high{stroke:#d9ed1f}.tick{stroke:#9fb9c2;stroke-width:1}.needle{stroke:#f8fafc;stroke-width:5;stroke-linecap:round}.hub{fill:#f8fafc;stroke:#0a3440;stroke-width:4}"
& ".legend-inline{display:flex;justify-content:center;gap:10px;margin-top:-4px;font-size:11px}.lg{display:flex;align-items:center;gap:5px;color:#fff!important}.dot{width:11px;height:11px;border-radius:50%;display:inline-block}.dot.low{background:#ff4d2d}.dot.mid{background:#f7b941}.dot.high{background:#d9ed1f}"
& ".nps-side{display:flex;flex-direction:column;justify-content:center;gap:9px}.bands{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;font-size:13px}.bands b{color:#fff!important}.hero-score{font-family:'Montserrat',sans-serif;font-size:52px;font-weight:950;line-height:1;color:#f2c94c!important}.score-caption{border-top:2px solid rgba(255,255,255,.75);padding-top:7px;max-width:130px;font-size:13px;font-weight:800;line-height:1.05;color:#fff!important}.micro{font-size:11px;color:#cbd5e1!important}"
& ".dist-card{background:radial-gradient(circle at 10% 5%,rgba(34,211,238,.22),transparent 35%),linear-gradient(145deg,#0f3337,#082327)!important;border-color:#2c717a!important}.dist-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}.score-chip{border:1px solid rgba(242,201,76,.55);border-radius:999px;color:#fef3c7!important;padding:6px 10px;font-size:12px;background:rgba(242,201,76,.1)}.dist-premium{display:grid;grid-template-columns:128px 1fr;gap:18px;align-items:center}.donut-wrap2{display:flex;flex-direction:column;align-items:center;justify-content:center}.dn-label{fill:#cbd5e1;font-size:8px;text-transform:uppercase;letter-spacing:.4px}.dn-value{fill:#f2c94c;font-size:18px;font-weight:900;letter-spacing:0}.donut-total{margin-top:10px;font-size:11px;color:#b7c7cf!important}.dist-row{margin-bottom:13px}.barlabel{display:flex;justify-content:space-between;align-items:center;font-size:13px;margin-bottom:6px;color:#fff!important}.dist-name{display:flex;align-items:center;gap:7px;font-weight:700;color:#fff!important}.sw{width:9px;height:9px;border-radius:999px;display:inline-block}.sw.prom{background:#10b981}.sw.neut{background:#94a3b8}.sw.det{background:#ef4444}.pct-pill{min-width:58px;text-align:center;border-radius:999px;padding:4px 8px;font-weight:800;background:rgba(255,255,255,.09);color:#fff!important}.bartrack{height:10px;background:rgba(5,24,27,.86);box-shadow:inset 0 1px 3px rgba(0,0,0,.55);border-radius:99px;overflow:hidden}.barfill{height:100%;border-radius:99px}.prom-fill{background:linear-gradient(90deg,#10b981,#22d3ee)}.neut-fill{background:linear-gradient(90deg,#94a3b8,#cbd5e1)}.det-fill{background:linear-gradient(90deg,#ef4444,#fb7185)}.note-row{display:flex;justify-content:space-between;align-items:center;margin-top:15px;padding-top:11px;border-top:1px solid rgba(255,255,255,.1);font-size:13px;color:#fff}.note-value{font-size:22px;font-weight:900;color:#f2c94c!important}.survey-total{margin-top:4px;font-size:11px;color:#b7c7cf!important;letter-spacing:.2px}"
& ".radar-card{display:grid!important;grid-template-columns:300px 1fr;gap:22px;align-items:center}.radar-wrap{display:flex;justify-content:center}.radar-grid{fill:none;stroke:#2b5960;stroke-width:1}.radar-axis{stroke:#21484e;stroke-width:1}.radar-poly{fill:rgba(242,201,76,.24);stroke:#f2c94c;stroke-width:3}.radar-dot{fill:#06d6a0;stroke:#071b1d;stroke-width:2}.radar-label{font-size:10px;fill:#dff8ff;font-weight:700}.kr-list{display:grid;grid-template-columns:1fr 1fr;gap:12px}.kr{background:#0b292d;border:1px solid #1b4c53;border-radius:10px;padding:12px}.kr-name{font-size:12px;color:#dff8ff!important;text-transform:uppercase;letter-spacing:.5px}.kr-score{font-family:'Montserrat',sans-serif;font-size:22px;font-weight:800;color:#f2c94c!important;margin:4px 0}.kr-real{font-size:11px;color:#cbd5e1!important}"
& "@media(max-width:760px){.nps-alt,.dist-premium,.radar-card,.kr-list{grid-template-columns:1fr!important}}"
& "</style>"
```

**Como funciona:**
Usa 1 medida(s) e 3 coluna(s) referenciada(s) diretamente. Dependências principais: HTML Dashboard Final Base.

**Usa:** `HTML Dashboard Final Base`, `_angles[j]`, `_vals[j]`, `span[id]`
**É usada por:** —


### HTML Dashboard Final Backup

`_medidas.HTML Dashboard Final Backup` · sem format string · 12 · JSON · Dashboard

**O que faz:**
[Papel: Técnico] Coluna dummy criada para viabilizar a tabela calculada _medidas. Não possui significado analítico e não deve ser usada em visuais.

**DAX:**
```dax
[HTML Dashboard Final Base]
& "<style>"
& "body,.dash,.card,.card span,.card b,.donut-leg,.donut-leg span,.donut-leg b,.leg-item,.bar-label,.bar-label span,.sub b,.ctx-badge{color:#e2e8f0!important;}"
& ".card .sub,.ksub,.lbl,.fbar label{color:#b8cad1!important;}"
& ".bar-label span[id],#bar-p,#bar-n,#bar-d,#nota-v,#lg-p,#lg-n,#lg-d,#qtd-t,#tot-v{color:#ffffff!important;}"
& "</style>"
```

**Como funciona:**
Usa 1 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: HTML Dashboard Final Base.

**Usa:** `HTML Dashboard Final Base`, `span[id]`
**É usada por:** —


### HTML Dashboard Final Base

`_medidas.HTML Dashboard Final Base` · sem format string · 12 · JSON · Dashboard

**O que faz:**
Matriz HTML por Classe IGRO v8 - texto da tabela em branco para melhor contraste.

**DAX:**
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
VAR _pp = IF ( ISBLANK ( [ind_pct_promotores] ), 0, [ind_pct_promotores] )
VAR _pn = IF ( ISBLANK ( [ind_pct_neutros] ), 0, [ind_pct_neutros] )
VAR _pd = IF ( ISBLANK ( [ind_pct_detratores] ), 0, [ind_pct_detratores] )
VAR _qt = IF ( ISBLANK ( [base_qtd_pesquisa] ), 0, [base_qtd_pesquisa] )
VAR _qp = IF ( ISBLANK ( [base_qtd_promotores] ), 0, [base_qtd_promotores] )
VAR _qn = IF ( ISBLANK ( [base_qtd_neutros] ), 0, [base_qtd_neutros] )
VAR _qd = IF ( ISBLANK ( [base_qtd_detratores] ), 0, [base_qtd_detratores] )
VAR _nt = IF ( ISBLANK ( [ind_media_nota_recomendacao] ), 0, [ind_media_nota_recomendacao] )
VAR _tm = IF ( ISBLANK ( [ind_media_tempo_resposta] ), 0, [ind_media_tempo_resposta] )
VAR _m3 = IF ( ISBLANK ( [ind_pct_mais_30_dias] ), 0, [ind_pct_mais_30_dias] )
VAR _re = IF ( ISBLANK ( [ind_pct_resolutividade] ), 0, [ind_pct_resolutividade] )
VAR _in = IF ( ISBLANK ( [ind_pct_respostas_insatisfatorias] ), 0, [ind_pct_respostas_insatisfatorias] )
VAR _ig = IF ( ISBLANK ( [idx_igro] ), 0, [idx_igro] )
VAR _st = IF ( ISBLANK ( [idx_igro_sub_t] ), 0, [idx_igro_sub_t] )
VAR _sq = IF ( ISBLANK ( [idx_igro_sub_q] ), 0, [idx_igro_sub_q] )
VAR _vn = IF ( ISBLANK ( [var_nps] ), 0, [var_nps] )
VAR _tot = IF ( ISBLANK ( [base_qtd_manifestacoes] ), 0, [base_qtd_manifestacoes] )

VAR _bj =
"{"
& _Q & "a" & _Q & ":0"
& _c & _Q & "n" & _Q & ":" & SUBSTITUTE ( FORMAT ( _nps, _F2 ), _c, _d )
& _c & _Q & "pp" & _Q & ":" & SUBSTITUTE ( FORMAT ( _pp, _F4 ), _c, _d )
& _c & _Q & "pn" & _Q & ":" & SUBSTITUTE ( FORMAT ( _pn, _F4 ), _c, _d )
& _c & _Q & "pd" & _Q & ":" & SUBSTITUTE ( FORMAT ( _pd, _F4 ), _c, _d )
& _c & _Q & "q" & _Q & ":" & FORMAT ( _qt, _F0 )
& _c & _Q & "qp" & _Q & ":" & FORMAT ( _qp, _F0 )
& _c & _Q & "qn" & _Q & ":" & FORMAT ( _qn, _F0 )
& _c & _Q & "qd" & _Q & ":" & FORMAT ( _qd, _F0 )
& _c & _Q & "nt" & _Q & ":" & SUBSTITUTE ( FORMAT ( _nt, _F2 ), _c, _d )
& _c & _Q & "t" & _Q & ":" & SUBSTITUTE ( FORMAT ( _tm, _F2 ), _c, _d )
& _c & _Q & "m" & _Q & ":" & SUBSTITUTE ( FORMAT ( _m3, _F4 ), _c, _d )
& _c & _Q & "r" & _Q & ":" & SUBSTITUTE ( FORMAT ( _re, _F4 ), _c, _d )
& _c & _Q & "i" & _Q & ":" & SUBSTITUTE ( FORMAT ( _in, _F4 ), _c, _d )
& _c & _Q & "ig" & _Q & ":" & SUBSTITUTE ( FORMAT ( _ig, _F4 ), _c, _d )
& _c & _Q & "st" & _Q & ":" & SUBSTITUTE ( FORMAT ( _st, _F4 ), _c, _d )
& _c & _Q & "sq" & _Q & ":" & SUBSTITUTE ( FORMAT ( _sq, _F4 ), _c, _d )
& _c & _Q & "vn" & _Q & ":" & SUBSTITUTE ( FORMAT ( _vn, _F2 ), _c, _d )
& _c & _Q & "tot" & _Q & ":" & FORMAT ( _tot, _F0 )
& "}"

VAR _at_raw =
ADDCOLUMNS (
FILTER ( VALUES ( dCalendario[Ano] ), NOT ISBLANK ( dCalendario[Ano] ) ),
"n_", CALCULATE ( IF ( ISBLANK ( [ind_nps] ), 0, [ind_nps] ) ),
"pp_", CALCULATE ( IF ( ISBLANK ( [ind_pct_promotores] ), 0, [ind_pct_promotores] ) ),
"pn_", CALCULATE ( IF ( ISBLANK ( [ind_pct_neutros] ), 0, [ind_pct_neutros] ) ),
"pd_", CALCULATE ( IF ( ISBLANK ( [ind_pct_detratores] ), 0, [ind_pct_detratores] ) ),
"q_", CALCULATE ( IF ( ISBLANK ( [base_qtd_pesquisa] ), 0, [base_qtd_pesquisa] ) ),
"qp_", CALCULATE ( IF ( ISBLANK ( [base_qtd_promotores] ), 0, [base_qtd_promotores] ) ),
"qn_", CALCULATE ( IF ( ISBLANK ( [base_qtd_neutros] ), 0, [base_qtd_neutros] ) ),
"qd_", CALCULATE ( IF ( ISBLANK ( [base_qtd_detratores] ), 0, [base_qtd_detratores] ) ),
"nt_", CALCULATE ( IF ( ISBLANK ( [ind_media_nota_recomendacao] ), 0, [ind_media_nota_recomendacao] ) ),
"t_", CALCULATE ( IF ( ISBLANK ( [ind_media_tempo_resposta] ), 0, [ind_media_tempo_resposta] ) ),
"m_", CALCULATE ( IF ( ISBLANK ( [ind_pct_mais_30_dias] ), 0, [ind_pct_mais_30_dias] ) ),
"r_", CALCULATE ( IF ( ISBLANK ( [ind_pct_resolutividade] ), 0, [ind_pct_resolutividade] ) ),
"i_", CALCULATE ( IF ( ISBLANK ( [ind_pct_respostas_insatisfatorias] ), 0, [ind_pct_respostas_insatisfatorias] ) ),
"ig_", CALCULATE ( IF ( ISBLANK ( [idx_igro] ), 0, [idx_igro] ) ),
"st_", CALCULATE ( IF ( ISBLANK ( [idx_igro_sub_t] ), 0, [idx_igro_sub_t] ) ),
"sq_", CALCULATE ( IF ( ISBLANK ( [idx_igro_sub_q] ), 0, [idx_igro_sub_q] ) ),
"vn_", CALCULATE ( IF ( ISBLANK ( [var_nps] ), 0, [var_nps] ) ),
"tot_", CALCULATE ( IF ( ISBLANK ( [base_qtd_manifestacoes] ), 0, [base_qtd_manifestacoes] ) )
)
VAR _at = FILTER ( _at_raw, [tot_] > 0 )
VAR _ja =
"["
& CONCATENATEX (
_at,
"{"
& _Q & "a" & _Q & ":" & [Ano]
& _c & _Q & "n" & _Q & ":" & SUBSTITUTE ( FORMAT ( [n_], _F2 ), _c, _d )
& _c & _Q & "pp" & _Q & ":" & SUBSTITUTE ( FORMAT ( [pp_], _F4 ), _c, _d )
& _c & _Q & "pn" & _Q & ":" & SUBSTITUTE ( FORMAT ( [pn_], _F4 ), _c, _d )
& _c & _Q & "pd" & _Q & ":" & SUBSTITUTE ( FORMAT ( [pd_], _F4 ), _c, _d )
& _c & _Q & "q" & _Q & ":" & FORMAT ( [q_], _F0 )
& _c & _Q & "qp" & _Q & ":" & FORMAT ( [qp_], _F0 )
& _c & _Q & "qn" & _Q & ":" & FORMAT ( [qn_], _F0 )
& _c & _Q & "qd" & _Q & ":" & FORMAT ( [qd_], _F0 )
& _c & _Q & "nt" & _Q & ":" & SUBSTITUTE ( FORMAT ( [nt_], _F2 ), _c, _d )
& _c & _Q & "t" & _Q & ":" & SUBSTITUTE ( FORMAT ( [t_], _F2 ), _c, _d )
& _c & _Q & "m" & _Q & ":" & SUBSTITUTE ( FORMAT ( [m_], _F4 ), _c, _d )
& _c & _Q & "r" & _Q & ":" & SUBSTITUTE ( FORMAT ( [r_], _F4 ), _c, _d )
& _c & _Q & "i" & _Q & ":" & SUBSTITUTE ( FORMAT ( [i_], _F4 ), _c, _d )
& _c & _Q & "ig" & _Q & ":" & SUBSTITUTE ( FORMAT ( [ig_], _F4 ), _c, _d )
& _c & _Q & "st" & _Q & ":" & SUBSTITUTE ( FORMAT ( [st_], _F4 ), _c, _d )
& _c & _Q & "sq" & _Q & ":" & SUBSTITUTE ( FORMAT ( [sq_], _F4 ), _c, _d )
& _c & _Q & "vn" & _Q & ":" & SUBSTITUTE ( FORMAT ( [vn_], _F2 ), _c, _d )
& _c & _Q & "tot" & _Q & ":" & FORMAT ( [tot_], _F0 )
& "}",
_c,
[Ano]
)
& "]"

VAR _stbl =
ADDCOLUMNS (
VALUES ( dOrgao_igro[sigla] ),
"n_", CALCULATE ( IF ( ISBLANK ( [ind_nps] ), 0, [ind_nps] ) ),
"pp_", CALCULATE ( IF ( ISBLANK ( [ind_pct_promotores] ), 0, [ind_pct_promotores] ) ),
"pn_", CALCULATE ( IF ( ISBLANK ( [ind_pct_neutros] ), 0, [ind_pct_neutros] ) ),
"pd_", CALCULATE ( IF ( ISBLANK ( [ind_pct_detratores] ), 0, [ind_pct_detratores] ) ),
"q_", CALCULATE ( IF ( ISBLANK ( [base_qtd_pesquisa] ), 0, [base_qtd_pesquisa] ) ),
"qp_", CALCULATE ( IF ( ISBLANK ( [base_qtd_promotores] ), 0, [base_qtd_promotores] ) ),
"qn_", CALCULATE ( IF ( ISBLANK ( [base_qtd_neutros] ), 0, [base_qtd_neutros] ) ),
"qd_", CALCULATE ( IF ( ISBLANK ( [base_qtd_detratores] ), 0, [base_qtd_detratores] ) ),
"nt_", CALCULATE ( IF ( ISBLANK ( [ind_media_nota_recomendacao] ), 0, [ind_media_nota_recomendacao] ) ),
"t_", CALCULATE ( IF ( ISBLANK ( [ind_media_tempo_resposta] ), 0, [ind_media_tempo_resposta] ) ),
"m_", CALCULATE ( IF ( ISBLANK ( [ind_pct_mais_30_dias] ), 0, [ind_pct_mais_30_dias] ) ),
"r_", CALCULATE ( IF ( ISBLANK ( [ind_pct_resolutividade] ), 0, [ind_pct_resolutividade] ) ),
"i_", CALCULATE ( IF ( ISBLANK ( [ind_pct_respostas_insatisfatorias] ), 0, [ind_pct_respostas_insatisfatorias] ) ),
"ig_", CALCULATE ( IF ( ISBLANK ( [idx_igro] ), 0, [idx_igro] ) ),
"st_", CALCULATE ( IF ( ISBLANK ( [idx_igro_sub_t] ), 0, [idx_igro_sub_t] ) ),
"sq_", CALCULATE ( IF ( ISBLANK ( [idx_igro_sub_q] ), 0, [idx_igro_sub_q] ) ),
"vn_", CALCULATE ( IF ( ISBLANK ( [var_nps] ), 0, [var_nps] ) ),
"tot_", CALCULATE ( IF ( ISBLANK ( [base_qtd_manifestacoes] ), 0, [base_qtd_manifestacoes] ) )
)
VAR _js2 =
"["
& CONCATENATEX (
FILTER ( _stbl, [q_] > 0 ),
"{"
& _Q & "s" & _Q & ":" & _Q & [sigla] & _Q
& _c & _Q & "n" & _Q & ":" & SUBSTITUTE ( FORMAT ( [n_], _F2 ), _c, _d )
& _c & _Q & "pp" & _Q & ":" & SUBSTITUTE ( FORMAT ( [pp_], _F4 ), _c, _d )
& _c & _Q & "pn" & _Q & ":" & SUBSTITUTE ( FORMAT ( [pn_], _F4 ), _c, _d )
& _c & _Q & "pd" & _Q & ":" & SUBSTITUTE ( FORMAT ( [pd_], _F4 ), _c, _d )
& _c & _Q & "q" & _Q & ":" & FORMAT ( [q_], _F0 )
& _c & _Q & "qp" & _Q & ":" & FORMAT ( [qp_], _F0 )
& _c & _Q & "qn" & _Q & ":" & FORMAT ( [qn_], _F0 )
& _c & _Q & "qd" & _Q & ":" & FORMAT ( [qd_], _F0 )
& _c & _Q & "nt" & _Q & ":" & SUBSTITUTE ( FORMAT ( [nt_], _F2 ), _c, _d )
& _c & _Q & "t" & _Q & ":" & SUBSTITUTE ( FORMAT ( [t_], _F2 ), _c, _d )
& _c & _Q & "m" & _Q & ":" & SUBSTITUTE ( FORMAT ( [m_], _F4 ), _c, _d )
& _c & _Q & "r" & _Q & ":" & SUBSTITUTE ( FORMAT ( [r_], _F4 ), _c, _d )
& _c & _Q & "i" & _Q & ":" & SUBSTITUTE ( FORMAT ( [i_], _F4 ), _c, _d )
& _c & _Q & "ig" & _Q & ":" & SUBSTITUTE ( FORMAT ( [ig_], _F4 ), _c, _d )
& _c & _Q & "st" & _Q & ":" & SUBSTITUTE ( FORMAT ( [st_], _F4 ), _c, _d )
& _c & _Q & "sq" & _Q & ":" & SUBSTITUTE ( FORMAT ( [sq_], _F4 ), _c, _d )
& _c & _Q & "vn" & _Q & ":" & SUBSTITUTE ( FORMAT ( [vn_], _F2 ), _c, _d )
& _c & _Q & "tot" & _Q & ":" & FORMAT ( [tot_], _F0 )
& "}",
_c,
[sigla]
)
& "]"

VAR _head =
"<!DOCTYPE html><html lang='pt-BR'><head><meta charset='UTF-8'>"
& "<link href='https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@600;700;800&display=swap' rel='stylesheet'>"
& "<style>*{box-sizing:border-box;margin:0;padding:0}body{background:#0a1a1d;color:#e2e8f0;font-family:'Inter',sans-serif;padding:16px;min-height:100vh}.dash{max-width:960px;margin:0 auto}h1{font-family:'Montserrat',sans-serif;font-size:18px;font-weight:700;color:#f2c94c;margin-bottom:16px;letter-spacing:.5px}.fbar{display:flex;gap:16px;margin-bottom:20px;align-items:center;background:#0f2f33;padding:12px 16px;border-radius:12px;border:1px solid #1e4a50;flex-wrap:wrap}.fbar label{font-size:12px;color:#94a3b8;font-weight:600;text-transform:uppercase;letter-spacing:.5px}.fbar select{background:#132a2d;color:#e2e8f0;border:1px solid #1e4a50;border-radius:6px;padding:5px 10px;font-size:13px;font-family:'Inter',sans-serif;cursor:pointer;outline:none}.fbar select:hover,.fbar select:focus{border-color:#f2c94c}.fbar .rst{background:transparent;color:#64748b;border:1px solid #1e4a50;border-radius:6px;padding:5px 12px;font-size:12px;cursor:pointer;margin-left:auto}.fbar .rst:hover{color:#f2c94c;border-color:#f2c94c}.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px}.card{background:#0f2f33;border:1px solid #1e4a50;border-radius:12px;padding:20px}.card.accent{border-color:#f2c94c66}.card.full{grid-column:1/-1}.lbl{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.8px;color:#94a3b8;margin-bottom:8px}.big{font-family:'Montserrat',sans-serif;font-size:52px;font-weight:800;line-height:1}.sub{font-size:13px;color:#64748b;margin-top:4px}.vr{font-size:14px;font-weight:600;margin-top:8px}.pos{color:#10b981}.neg{color:#ef4444}.neu{color:#94a3b8}.bar-wrap{margin-bottom:10px}.bar-label{display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px}.bar-track{background:#132a2d;border-radius:99px;height:8px;overflow:hidden}.bar-fill{height:100%;border-radius:99px;transition:width .4s ease}.fp{background:#10b981}.fn{background:#94a3b8}.fd{background:#ef4444}.donut-wrap{display:flex;align-items:center;gap:24px}.donut-leg{display:flex;flex-direction:column;gap:10px;flex:1}.leg-item{display:flex;align-items:center;gap:8px;font-size:13px}.leg-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}.kgrid{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-bottom:16px}.kcard{background:#0f2f33;border:1px solid #1e4a50;border-radius:10px;padding:14px}.kval{font-family:'Montserrat',sans-serif;font-size:22px;font-weight:700;color:#f2c94c;margin:4px 0}.ksub{font-size:11px;color:#64748b}.igrid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px}.ig-main{background:#0f2f33;border:1px solid #f2c94c33;border-radius:10px;padding:16px;text-align:center}.ig-val{font-family:'Montserrat',sans-serif;font-size:32px;font-weight:800;color:#f2c94c}.ig-bar{background:#132a2d;border-radius:99px;height:6px;margin-top:10px;overflow:hidden}.ig-fill{height:100%;background:linear-gradient(90deg,#f2c94c,#06b6d4);border-radius:99px;transition:width .4s ease}.ctx-badge{display:inline-block;background:#132a2d;border:1px solid #1e4a50;border-radius:6px;padding:3px 10px;font-size:11px;color:#94a3b8;margin-bottom:12px}</style></head>"

VAR _body =
"<body><div class='dash'><h1>Dashboard IGRO &#183; NPS</h1><div class='fbar'><label>Ano</label><select id='sel-a'><option value='all'>Todos os anos</option></select><label>&#211;rg&#227;o</label><select id='sel-s'><option value='all'>Todos os &#243;rg&#227;os</option></select><button class='rst' id='btn-rst'>&#10006; Limpar</button></div><div id='ctx-info' class='ctx-badge' style='display:none'></div><div class='lbl' style='margin-bottom:12px'>&#205;ndice IGRO</div><div class='igrid'><div class='ig-main'><div class='lbl'>IGRO</div><div class='ig-val' id='ig-val'>--</div><div class='ig-bar'><div class='ig-fill' id='ig-bl' style='width:0'></div></div></div><div class='ig-main'><div class='lbl'>Sub-&#237;ndice Tempo</div><div class='ig-val' id='st-val'>--</div><div class='ig-bar'><div class='ig-fill' id='st-bl' style='width:0'></div></div></div><div class='ig-main'><div class='lbl'>Sub-&#237;ndice Qualidade</div><div class='ig-val' id='sq-val'>--</div><div class='ig-bar'><div class='ig-fill' id='sq-bl' style='width:0'></div></div></div></div><div class='lbl' style='margin-bottom:12px'>Indicadores de Qualidade</div><div class='kgrid'><div class='kcard'><div class='lbl'>Tempo M&#233;dio Resposta</div><div class='kval' id='kv1'>--</div><div class='ksub'>dias</div></div><div class='kcard'><div class='lbl'>Mais de 30 Dias</div><div class='kval' id='kv2'>--</div><div class='ksub'>% das respostas</div></div><div class='kcard'><div class='lbl'>Resolutividade</div><div class='kval' id='kv3'>--</div><div class='ksub'>% resolvidos</div></div><div class='kcard'><div class='lbl'>Resp. Insatisfat&#243;rias</div><div class='kval' id='kv4'>--</div><div class='ksub'>% insatisfat&#243;rias</div></div><div class='kcard'><div class='lbl'>Nota de Recomenda&#231;&#227;o</div><div class='kval' id='kv5'>--</div><div class='ksub'>m&#233;dia</div></div></div><div class='grid2'><div class='card accent'><div class='lbl'>NPS &#183; &#205;ndice de Satisfa&#231;&#227;o</div><div class='big' id='nps-v' style='color:#f2c94c'>--</div><div class='sub'>Respostas: <b id='qtd-t'>--</b> &nbsp;|&nbsp; Manifesta&#231;&#245;es: <b id='tot-v'>--</b></div><div class='vr neu' id='nps-var'>--</div></div><div class='card'><div class='lbl'>Distribui&#231;&#227;o de Respondentes</div><div class='bar-wrap'><div class='bar-label'><span style='color:#10b981'>Promotores</span><span id='bar-p'>--</span></div><div class='bar-track'><div class='bar-fill fp' id='bar-p-c' style='width:0'></div></div></div><div class='bar-wrap'><div class='bar-label'><span style='color:#94a3b8'>Neutros</span><span id='bar-n'>--</span></div><div class='bar-track'><div class='bar-fill fn' id='bar-n-c' style='width:0'></div></div></div><div class='bar-wrap'><div class='bar-label'><span style='color:#ef4444'>Detratores</span><span id='bar-d'>--</span></div><div class='bar-track'><div class='bar-fill fd' id='bar-d-c' style='width:0'></div></div></div><div class='sub' style='margin-top:8px'>Nota m&#233;dia: <b id='nota-v'>--</b></div></div><div class='card full'><div class='lbl'>Composi&#231;&#227;o NPS</div><div class='donut-wrap'><svg id='svg-nps' viewBox='0 0 100 100' width='150' height='150'><circle cx='50' cy='50' r='45' fill='none' stroke='#132a2d' stroke-width='10'/><circle id='sa-p' cx='50' cy='50' r='45' fill='none' stroke='#10b981' stroke-width='10' stroke-dasharray='0 283' stroke-dashoffset='0' transform='rotate(-90 50 50)'/><circle id='sa-n' cx='50' cy='50' r='45' fill='none' stroke='#94a3b8' stroke-width='10' stroke-dasharray='0 283' stroke-dashoffset='0' transform='rotate(-90 50 50)'/><circle id='sa-d' cx='50' cy='50' r='45' fill='none' stroke='#ef4444' stroke-width='10' stroke-dasharray='0 283' stroke-dashoffset='0' transform='rotate(-90 50 50)'/></svg><div class='donut-leg'><div class='leg-item'><div class='leg-dot' style='background:#10b981'></div><span>Promotores: <b id='lg-p'>--</b></span></div><div class='leg-item'><div class='leg-dot' style='background:#94a3b8'></div><span>Neutros: <b id='lg-n'>--</b></span></div><div class='leg-item'><div class='leg-dot' style='background:#ef4444'></div><span>Detratores: <b id='lg-d'>--</b></span></div></div></div></div></div></div>"

VAR _js =
"<" & _sc & ">try{"
& "const base=" & _bj & ";"
& "const anos=" & _ja & ";"
& "const siglas=" & _js2 & ";"
& "const sa=document.getElementById('sel-a');"
& "const ss=document.getElementById('sel-s');"
& "const ctx=document.getElementById('ctx-info');"
& "anos.sort((a,b)=>b.a-a.a).forEach(r=>{const o=document.createElement('option');o.value=r.a;o.textContent=r.a;sa.appendChild(o);});"
& "siglas.sort((a,b)=>a.s.localeCompare(b.s)).forEach(r=>{const o=document.createElement('option');o.value=r.s;o.textContent=r.s;ss.appendChild(o);});"
& "function pct(v){return (parseFloat(v)*100).toFixed(1)+'%';}"
& "function f2(v){return parseFloat(v).toFixed(2);}"
& "function fn0(v){return Number(v).toLocaleString('pt-BR');}"
& "function npsColor(n){const v=parseFloat(n);return v>=75?'#10b981':v>=50?'#f2c94c':v>=0?'#f97316':'#ef4444';}"
& "function el(id){return document.getElementById(id);}"
& "const C=282.74;"
& "function render(d,label){el('nps-v').textContent=parseFloat(d.n).toFixed(0);el('nps-v').style.color=npsColor(d.n);el('qtd-t').textContent=fn0(d.q);el('tot-v').textContent=fn0(d.tot||0);const vn=parseFloat(d.vn);el('nps-var').textContent=(vn>0?'+':'')+f2(vn)+' pts vs anterior';el('nps-var').className='vr '+(vn>0?'pos':vn<0?'neg':'neu');const pp=parseFloat(d.pp),pn=parseFloat(d.pn),pd=parseFloat(d.pd);el('bar-p').textContent=pct(pp);el('bar-n').textContent=pct(pn);el('bar-d').textContent=pct(pd);el('bar-p-c').style.width=(pp*100).toFixed(1)+'%';el('bar-n-c').style.width=(pn*100).toFixed(1)+'%';el('bar-d-c').style.width=(pd*100).toFixed(1)+'%';el('nota-v').textContent=f2(d.nt);el('lg-p').textContent=pct(pp)+' ('+fn0(d.qp)+')';el('lg-n').textContent=pct(pn)+' ('+fn0(d.qn)+')';el('lg-d').textContent=pct(pd)+' ('+fn0(d.qd)+')';const dp=pp*C,dn=pn*C,dd=pd*C;el('sa-p').setAttribute('stroke-dasharray',dp.toFixed(2)+' '+(C-dp).toFixed(2));el('sa-n').setAttribute('stroke-dasharray',dn.toFixed(2)+' '+(C-dn).toFixed(2));el('sa-n').setAttribute('stroke-dashoffset',(-dp).toFixed(2));el('sa-d').setAttribute('stroke-dasharray',dd.toFixed(2)+' '+(C-dd).toFixed(2));el('sa-d').setAttribute('stroke-dashoffset',(-(dp+dn)).toFixed(2));el('kv1').textContent=f2(d.t);el('kv2').textContent=pct(d.m);el('kv3').textContent=pct(d.r);el('kv4').textContent=pct(d.i);el('kv5').textContent=f2(d.nt);const ig=parseFloat(d.ig),st=parseFloat(d.st),sq=parseFloat(d.sq);el('ig-val').textContent=(ig*100).toFixed(1)+'%';el('st-val').textContent=(st*100).toFixed(1)+'%';el('sq-val').textContent=(sq*100).toFixed(1)+'%';el('ig-bl').style.width=(ig*100).toFixed(1)+'%';el('st-bl').style.width=(st*100).toFixed(1)+'%';el('sq-bl').style.width=(sq*100).toFixed(1)+'%';if(label){ctx.textContent='Filtro: '+label;ctx.style.display='inline-block';}else{ctx.style.display='none';}}"
& "function getD(){const av=sa.value,sv=ss.value;if(sv!=='all'){const r=siglas.find(x=>x.s===sv);return [r||base,'Org: '+sv];}if(av!=='all'){const r=anos.find(x=>String(x.a)===av);return [r||base,'Ano: '+av];}return [base,null];}"
& "function update(){const out=getD();render(out[0],out[1]);}"
& "sa.onchange=()=>{ss.value='all';update();};"
& "ss.onchange=()=>{sa.value='all';update();};"
& "document.getElementById('btn-rst').onclick=()=>{sa.value='all';ss.value='all';update();};"
& "render(base,null);}catch(e){document.body.innerHTML='<div style=\'padding:20px;color:#ef4444;font-family:monospace\'>Erro ao carregar dados: '+e.message+'</div>'; }"
& "<" & _scx & ">"

RETURN
_head & _body & _js & "</body></html>"
```

**Como funciona:**
Usa 18 medida(s) e 4 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_detratores, base_qtd_manifestacoes, base_qtd_neutros, base_qtd_pesquisa, base_qtd_promotores, idx_igro, idx_igro_sub_q, idx_igro_sub_t.

**Usa:** `base_qtd_detratores`, `base_qtd_manifestacoes`, `base_qtd_neutros`, `base_qtd_pesquisa`, `base_qtd_promotores`, `idx_igro`, `idx_igro_sub_q`, `idx_igro_sub_t`, `ind_media_nota_recomendacao`, `ind_media_tempo_resposta`, `ind_nps`, `ind_pct_detratores`
**É usada por:** `HTML Dashboard Final`, `HTML Dashboard Final Backup`, `HTML Dashboard Final Fonte Branca`


### HTML Dashboard Final Fonte Branca

`_medidas.HTML Dashboard Final Fonte Branca` · sem format string · 12 · JSON · Dashboard

**O que faz:**
Dashboard HTML IGRO·NPS com badge dinamica de classificacao no cartao IGRO, filtros preservados, gauge NPS e distribuicao premium.

**DAX:**
```dax
[HTML Dashboard Final Base]
& "<style>"
& "body,.dash,.card,.card span,.card b,.donut-leg,.donut-leg span,.donut-leg b,.leg-item,.bar-label,.bar-label span,.sub b,.ctx-badge{color:#e2e8f0!important;}"
& ".card .sub,.ksub,.lbl,.fbar label{color:#b8cad1!important;}"
& ".bar-label span[id],#bar-p,#bar-n,#bar-d,#nota-v,#lg-p,#lg-n,#lg-d,#qtd-t,#tot-v{color:#ffffff!important;}"
& "</style>"
```

**Como funciona:**
Usa 1 medida(s) e 1 coluna(s) referenciada(s) diretamente. Dependências principais: HTML Dashboard Final Base.

**Usa:** `HTML Dashboard Final Base`, `span[id]`
**É usada por:** —


### HTML Dashboard IGRO

`_medidas.HTML Dashboard IGRO` · sem format string · 12 · JSON · Dashboard

**O que faz:**
Volume de manifestações no mesmo período do ano anterior. Funciona com qualquer granularidade de dCalendario (dia, mês, quadrimestre).

**DAX:**
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
"button:hover{background:#1e3a5f;border-color:#3b82f6}" &
".ticker-wrap{overflow:hidden;background:#000;border-top:1px solid #1f2937;border-bottom:1px solid #1f2937;height:28px;margin-bottom:10px}" &
".ticker-run{display:flex;white-space:nowrap;animation:tickerMove 40s linear infinite}" &
".ticker-run:hover{animation-play-state:paused}" &
".tk-item{display:inline-flex;align-items:center;padding:0 18px;font-size:11px;color:#93c5fd;height:28px;gap:5px;border-right:1px solid #222}" &
"@keyframes tickerMove{from{transform:translateX(0)}to{transform:translateX(-50%)}}" &
".kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:8px;margin-bottom:10px}" &
".card{background:#111;border-radius:8px;padding:11px;border:1px solid #1f2937;border-top:3px solid #3b82f6}" &
".card-lbl{font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.4px;margin-bottom:3px}" &
".card-val{font-size:19px;font-weight:700;color:#f9fafb}" &
".card-sub{font-size:10px;margin-top:3px}" &
".up{color:#34d399}.dn{color:#f87171}.neu{color:#9ca3af}" &
".charts{display:grid;grid-template-columns:2fr 1fr;gap:8px;margin-bottom:10px}" &
".cbox{background:#111;border-radius:8px;padding:11px;border:1px solid #1f2937}" &
".cbox h3{font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.4px;margin-bottom:8px}" &
".bar-wrap{display:flex;flex-direction:column;gap:3px}" &
".brow{display:flex;align-items:center;gap:5px}" &
".blbl{font-size:10px;color:#9ca3af;width:100px;min-width:100px;text-align:right;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}" &
".bbg{flex:1;background:#1c1c1e;border-radius:3px;overflow:hidden;height:14px}" &
".bfil{height:100%;border-radius:3px}" &
".bval{font-size:10px;color:#e5e7eb;min-width:38px;text-align:right}" &
".badge{display:inline-block;padding:1px 6px;border-radius:9px;font-size:10px;font-weight:600}" &
".bg-g{background:#065f46;color:#6ee7b7}.bg-y{background:#78350f;color:#fde68a}" &
".bg-o{background:#7c2d12;color:#fdba74}.bg-r{background:#7f1d1d;color:#fca5a5}" &
".tbl-wrap{background:#111;border-radius:8px;border:1px solid #1f2937;overflow:hidden}" &
".tc{display:flex;gap:8px;padding:9px;border-bottom:1px solid #1f2937;flex-wrap:wrap;align-items:center}" &
".tc input{background:#1c1c1e;color:#e5e7eb;border:1px solid #333;border-radius:5px;padding:4px 9px;font-size:11px;flex:1;min-width:150px}" &
"table{width:100%;border-collapse:collapse;font-size:11px}" &
"thead th{background:#161616;padding:6px 8px;text-align:left;color:#6b7280;font-weight:500;border-bottom:1px solid #1f2937;white-space:nowrap}" &
"tbody tr:hover{background:#161616}" &
"tbody td{padding:5px 8px;border-bottom:1px solid #111;color:#e5e7eb;white-space:nowrap}" &
".pag{display:flex;gap:6px;padding:7px 9px;align-items:center;font-size:11px;color:#6b7280}" &
".pag button{padding:2px 7px;font-size:11px}" &
"</style>"

VAR _body =
"<div class='topbar'>" &
"<h1>&#128202; IGRO &mdash; Índice de Gestão e Risco Operacional das Ouvidorias</h1>" &
"<select id='dsv' onchange='applyF()'><option value=''>Todos os órgãos</option></select>" &
"<button onclick='resetF()'>&#8635; Reset</button>" &
"</div>" &
"<div class='ticker-wrap'><div class='ticker-run' id='tkr'></div></div>" &
"<div class='kpis'>" &
"<div class='card'><div class='card-lbl'>IGRO Rede</div><div class='card-val' id='k_igro'>--</div><div class='card-sub' id='b_igro'></div></div>" &
"<div class='card'><div class='card-lbl'>Sub-T Tempo</div><div class='card-val' id='k_subt'>--</div><div class='card-sub' id='b_subt'></div></div>" &
"<div class='card'><div class='card-lbl'>Sub-Q Qualidade</div><div class='card-val' id='k_subq'>--</div><div class='card-sub' id='b_subq'></div></div>" &
"<div class='card'><div class='card-lbl'>TMR Médio</div><div class='card-val' id='k_tmr'>--</div><div class='card-sub' id='b_tmr'></div></div>" &
"<div class='card'><div class='card-lbl'>Resolutividade</div><div class='card-val' id='k_res'>--</div><div class='card-sub' id='b_res'></div></div>" &
"<div class='card'><div class='card-lbl'>Nota Média</div><div class='card-val' id='k_nota'>--</div><div class='card-sub' id='b_nota'></div></div>" &
"<div class='card'><div class='card-lbl'>NPS</div><div class='card-val' id='k_nps'>--</div><div class='card-sub' id='b_nps'></div></div>" &
"<div class='card'><div class='card-lbl'>Insatisfatórias</div><div class='card-val' id='k_ins'>--</div><div class='card-sub' id='b_ins'></div></div>" &
"</div>" &
"<div class='charts'>" &
"<div class='cbox'><h3>Ranking IGRO por órgão (top 20)</h3><div class='bar-wrap' id='rank_wrap'></div></div>" &
"<div class='cbox'><h3>Distribuição por tipo</h3><div class='bar-wrap' id='tipo_wrap'></div></div>" &
"</div>" &
"<div class='tbl-wrap'>" &
"<div class='tc'>" &
"<input type='text' id='bsc' placeholder='Buscar órgão...' oninput='rn()'>" &
"<button onclick='xcsv()'>&#11015; CSV</button>" &
"<span id='pag_info' style='margin-left:auto;font-size:11px;color:#6b7280'></span>" &
"</div>" &
"<table><thead><tr>" &
"<th>Órgão</th><th>Manif.</th><th>IGRO</th><th>Sub-T</th><th>Sub-Q</th>" &
"<th>TMR</th><th>Resolut.</th><th>Nota</th><th>Insatisf.</th><th>NPS</th><th>Risco</th>" &
"</tr></thead><tbody id='tb'></tbody></table>" &
"<div class='pag'><button onclick='gp(-1)'>&#9664;</button><span id='pag_lbl'>Pág 1</span><button onclick='gp(1)'>&#9654;</button></div>" &
"</div>"

VAR _js1 =
"<" & _sc & ">" &
"const ORG=" & [_JSON Orgaos] & ";" &
"const TIP=" & [_JSON Tipos] & ";" &
"let fd=ORG,pg=1,pp=20;" &
"function pct(v){return(v*100).toFixed(1)+'%'}" &
"function cor(v){return v>=0.8?'bg-g':v>=0.6?'bg-y':v>=0.4?'bg-o':'bg-r'}" &
"function lbl(v){return v>=0.8?'Baixo':v>=0.6?'Moderado':v>=0.4?'Alto':'Cr\u00edtico'}" &
"function buildTicker(){" &
"  const it=ORG.slice(0,20).map(o=>'<span class=\'tk-item\'>'+o.s+' <b>'+pct(+o.i)+'</b></span>').join('');" &
"  document.getElementById('tkr').innerHTML=it.repeat(2);}" &
"function buildSelects(){" &
"  const sv=document.getElementById('dsv');" &
"  ORG.forEach(o=>{const op=document.createElement('option');op.value=o.s;op.textContent=o.s;sv.appendChild(op);});}" &
"function setCard(id,val,subId,subHtml){" &
"  document.getElementById(id).textContent=val;" &
"  document.getElementById(subId).innerHTML=subHtml;}" &
"function renderKPIs(){" &
"  const tot=fd.reduce((a,o)=>a+ +o.n,0)||1;" &
"  const wi=fd.reduce((a,o)=>a+ +o.i* +o.n,0)/tot;" &
"  const wt=fd.reduce((a,o)=>a+ +o.t* +o.n,0)/tot;" &
"  const wq=fd.reduce((a,o)=>a+ +o.q* +o.n,0)/tot;" &
"  const tm=fd.reduce((a,o)=>a+ +o.m* +o.n,0)/tot;" &
"  const re=fd.reduce((a,o)=>a+ +o.r* +o.n,0)/tot;" &
"  const nt=fd.reduce((a,o)=>a+ +o.a* +o.n,0)/tot;" &
"  const np=fd.reduce((a,o)=>a+ +o.p* +o.n,0)/tot;" &
"  const ix=fd.reduce((a,o)=>a+ +o.x* +o.n,0)/tot;" &
"  setCard('k_igro',pct(wi),'b_igro','<span class=\'badge '+cor(wi)+'\'>'+lbl(wi)+'</span>');" &
"  setCard('k_subt',pct(wt),'b_subt','<span class=\'badge '+cor(wt)+'\'>'+lbl(wt)+'</span>');" &
"  setCard('k_subq',pct(wq),'b_subq','<span class=\'badge '+cor(wq)+'\'>'+lbl(wq)+'</span>');" &
"  setCard('k_tmr',tm.toFixed(1)+'d','b_tmr',tm<=10?'<span class=\'up\'>&#10003; meta 10d</span>':'<span class=\'dn\'>&#9888; acima 10d</span>');" &
"  setCard('k_res',pct(re),'b_res',re>=0.7?'<span class=\'up\'>&#10003; meta 70%</span>':'<span class=\'dn\'>&#9888; abaixo 70%</span>');" &
"  setCard('k_nota',nt.toFixed(1),'b_nota',nt>=7.5?'<span class=\'up\'>&#10003; meta 7,5</span>':'<span class=\'dn\'>&#9888; abaixo 7,5</span>');" &
"  setCard('k_nps',(np>=0?'+':'')+np.toFixed(1),'b_nps',np>=50?'<span class=\'up\'>Excelente</span>':np>=0?'<span class=\'neu\'>Razo\u00e1vel</span>':'<span class=\'dn\'>Cr\u00edtico</span>');" &
"  setCard('k_ins',pct(ix),'b_ins',ix<=0.025?'<span class=\'up\'>&#10003; meta 2,5%</span>':'<span class=\'dn\'>&#9888; acima 2,5%</span>');}"

VAR _js2 =
"function buildRanking(){" &
"  const mx=Math.max(...fd.map(o=> +o.i))||1;" &
"  const cl=['#34d399','#fbbf24','#f97316','#f87171'];" &
"  const html=fd.slice(0,20).map(o=>{" &
"    const v= +o.i;const w=Math.round(v/mx*100);" &
"    const c=v>=0.8?cl[0]:v>=0.6?cl[1]:v>=0.4?cl[2]:cl[3];" &
"    return '<div class=\'brow\'><div class=\'blbl\' title=\''+o.s+'\'>'+o.s+'</div>'" &
"      +'<div class=\'bbg\'><div class=\'bfil\' style=\'width:'+w+'%;background:'+c+';\'></div></div>'" &
"      +'<div class=\'bval\'>'+pct(v)+'</div></div>';}).join('');" &
"  document.getElementById('rank_wrap').innerHTML=html;}" &
"function buildTipos(){" &
"  const mx=Math.max(...TIP.map(t=> +t.n))||1;" &
"  const cs=['#3b82f6','#f59e0b','#10b981','#8b5cf6','#ef4444','#06b6d4','#f97316'];" &
"  const html=TIP.map((t,i)=>{" &
"    const w=Math.round( +t.n/mx*100);" &
"    return '<div class=\'brow\'><div class=\'blbl\'>'+t.tipo+'</div>'" &
"      +'<div class=\'bbg\'><div class=\'bfil\' style=\'width:'+w+'%;background:'+cs[i%7]+';\'></div></div>'" &
"      +'<div class=\'bval\'>'+(+ t.n).toLocaleString('pt-BR')+'</div></div>';}).join('');" &
"  document.getElementById('tipo_wrap').innerHTML=html;}" &
"function rn(){" &
"  const q=(document.getElementById('bsc').value||'').toLowerCase();" &
"  const rows=fd.filter(o=>o.s.toLowerCase().includes(q));" &
"  const tot=rows.length;const pages=Math.ceil(tot/pp)||1;" &
"  if(pg>pages)pg=pages;" &
"  document.getElementById('pag_lbl').textContent='P\u00e1g '+pg+'/'+pages;" &
"  document.getElementById('pag_info').textContent=tot+' \u00f3rg\u00e3os';" &
"  const sl=rows.slice((pg-1)*pp,pg*pp);" &
"  const html=sl.map(o=>{" &
"    const v= +o.i;const c=cor(v);" &
"    return '<tr>'" &
"      +'<td><b>'+o.s+'</b></td>'" &
"      +'<td>'+(+ o.n).toLocaleString('pt-BR')+'</td>'" &
"      +'<td><span class=\'badge '+c+'\'>'+pct(v)+'</span></td>'" &
"      +'<td>'+pct(+o.t)+'</td>'" &
"      +'<td>'+pct(+o.q)+'</td>'" &
"      +'<td>'+(+o.m).toFixed(1)+'d</td>'" &
"      +'<td>'+pct(+o.r)+'</td>'" &
"      +'<td>'+(+o.a).toFixed(1)+'</td>'" &
"      +'<td>'+pct(+o.x)+'</td>'" &
"      +'<td>'+((+o.p)>=0?'+':'')+(+o.p).toFixed(1)+'</td>'" &
"      +'<td><span class=\'badge '+c+'\'>'+lbl(v)+'</span></td>'" &
"      +'</tr>';}).join('');" &
"  document.getElementById('tb').innerHTML=html;}" &
"function gp(d){pg+=d;if(pg<1)pg=1;rn();}" &
"function applyF(){" &
"  const sv=document.getElementById('dsv').value;" &
"  fd=sv?ORG.filter(o=>o.s===sv):ORG;" &
"  pg=1;renderKPIs();buildRanking();rn();}" &
"function resetF(){" &
"  document.getElementById('dsv').value='';" &
"  document.getElementById('bsc').value='';" &
"  fd=ORG;pg=1;renderKPIs();buildRanking();rn();}" &
"function xcsv(){" &
"  const h='Orgao,Manif,IGRO,SubT,SubQ,TMR,Resolutividade,Nota,Insatisf,NPS\n';" &
"  const r=fd.map(o=>[o.s,o.n,o.i,o.t,o.q,o.m,o.r,o.a,o.x,o.p].join(',')).join('\n');" &
"  const a=document.createElement('a');" &
"  a.href='data:text/csv;charset=utf-8,'+encodeURIComponent(h+r);" &
"  a.download='igro.csv';a.click();}" &
"function init(){buildTicker();buildSelects();renderKPIs();buildRanking();buildTipos();rn();}" &
"init();" &
"<" & _scx & ">"

RETURN _css & _body & _js1 & _js2
```

**Como funciona:**
Usa 2 medida(s) e 5 coluna(s) referenciada(s) diretamente. Dependências principais: _JSON Orgaos, _JSON Tipos.

**Usa:** `_JSON Orgaos`, `_JSON Tipos`, `cl[0]`, `cl[1]`, `cl[2]`, `cl[3]`, `cs[i%7]`
**É usada por:** —


### HTML Matriz Classes IGRO

`_medidas.HTML Matriz Classes IGRO` · sem format string · 12 · JSON · Dashboard

**O que faz:**
Flag de amostra insuficiente para KRIs de pesquisa (v3 FPC corrigido). Denominador exclui manifestacoes anonimas, que nao podem gerar pesquisa de satisfacao. Flag=1 quando n_obs < 30 E taxa < 5% das finalizadas identificadas.

**DAX:**
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
&& NOT ISBLANK(dOrgao_igro[Classe])
&& dOrgao_igro[Classe] <> "N/A"
),
"_manif", CALCULATE([base_qtd_manifestacoes]),
"_nps", COALESCE(CALCULATE([ind_nps]), 0),
"_tmr", COALESCE(CALCULATE([ind_media_tempo_resposta]), 0),
"_res", COALESCE(CALCULATE([ind_pct_resolutividade]), 0),
"_ri", COALESCE(CALCULATE([ind_pct_respostas_insatisfatorias]), 0),
"_pesq", COALESCE(CALCULATE([base_qtd_pesquisa]), 0),
"_subt", COALESCE(CALCULATE([idx_igro_sub_t]), 0),
"_subq", COALESCE(CALCULATE([idx_igro_sub_q]), 0),
"_igro", COALESCE(CALCULATE([idx_igro]), 0),
"_flag", COALESCE(CALCULATE([flag_amostra_insuficiente]), 0)
)
VAR _total = COUNTROWS(_tbl)
VAR _controlado = COUNTROWS(FILTER(_tbl, [_igro] >= 0.9))
VAR _atencao = COUNTROWS(FILTER(_tbl, [_igro] >= 0.7 && [_igro] < 0.9))
VAR _elevado = COUNTROWS(FILTER(_tbl, [_igro] >= 0.5 && [_igro] < 0.7))
VAR _critico = COUNTROWS(FILTER(_tbl, [_igro] < 0.5))
VAR _media = AVERAGEX(_tbl, [_igro])
VAR _CSS =
"<style>*{box-sizing:border-box;margin:0;padding:0}body{background:#061f20;color:#e2e8f0;font-family:Segoe UI,Arial,sans-serif;padding:14px}.w{max-width:1200px;margin:0 auto}h1{font-size:18px;font-weight:800;color:#f2c94c;margin-bottom:6px}.sub{font-size:11px;color:#8aa0aa;margin-bottom:14px}.note{font-size:10px;color:#78909a;margin-bottom:12px}.sb{display:grid;grid-template-columns:repeat(6,minmax(110px,1fr));gap:8px;margin-bottom:16px}.sc{background:#0d3436;border:1px solid #1f5559;border-radius:8px;padding:9px 12px}.v{font-size:18px;font-weight:800}.l{font-size:10px;color:#91a7b0;text-transform:uppercase;margin-top:2px}.cb{margin-bottom:18px}.ch{display:flex;align-items:center;gap:12px;background:#0d3436;border-left:4px solid #f2c94c;border-radius:8px;padding:9px 12px;margin-bottom:7px}.ch h2{font-size:13px;color:#f2c94c}.ch .m{font-size:10px;color:#91a7b0}.cs{margin-left:auto;display:flex;gap:14px;font-size:10px;color:#91a7b0}.cs b{color:#e2e8f0}.tw{overflow-x:auto;border:1px solid #1f5559;border-radius:8px}.tbl{width:100%;border-collapse:collapse;font-size:11px;color:#e2e8f0}.tbl th{background:#0a292b;color:#b8cad1;text-align:left;text-transform:uppercase;font-size:9px;padding:8px 9px;border-bottom:1px solid #1f5559;white-space:nowrap}.tbl td{color:#e2e8f0;padding:7px 9px;border-bottom:1px solid #0c2b2d;white-space:nowrap}.tbl td b{color:inherit}.tbl tr:last-child td{border-bottom:none}.tbl tr:hover td{background:#0d3436;color:#ffffff}.bar{height:5px;background:#11383b;border-radius:99px;overflow:hidden;margin-top:3px}.fill{height:100%;border-radius:99px}.flag{display:inline-block;width:7px;height:7px;border-radius:50%;background:#f97316;margin-left:5px}.empty{padding:28px;text-align:center;color:#78909a}</style>"
VAR _summary =
"<div class='sb'>"
& "<div class='sc'><div class='v' style='color:#f2c94c'>" & FORMAT(_total, "#,0") & "</div><div class='l'>Orgaos</div></div>"
& "<div class='sc'><div class='v' style='color:#10b981'>" & FORMAT(_controlado, "#,0") & "</div><div class='l'>Controlado</div></div>"
& "<div class='sc'><div class='v' style='color:#f2c94c'>" & FORMAT(_atencao, "#,0") & "</div><div class='l'>Em Atencao</div></div>"
& "<div class='sc'><div class='v' style='color:#f97316'>" & FORMAT(_elevado, "#,0") & "</div><div class='l'>Elevado</div></div>"
& "<div class='sc'><div class='v' style='color:#ef4444'>" & FORMAT(_critico, "#,0") & "</div><div class='l'>Critico</div></div>"
& "<div class='sc'><div class='v' style='color:#f2c94c'>" & FORMAT(_media, "0.0%") & "</div><div class='l'>IGRO medio</div></div>"
& "</div>"
VAR _classes = DATATABLE("Classe", STRING, "Rotulo", STRING, {{"1","Cl.1 Alta Complexidade"},{"2","Cl.2 Volume Expressivo"},{"3","Cl.3 Media Complexidade"},{"4","Cl.4 Adjuntas Diversas"},{"5","Cl.5 Menor Estrutura"}})
VAR _matrix =
CONCATENATEX(
_classes,
VAR _cl = [Classe]
VAR _rotulo = [Rotulo]
VAR _rows = FILTER(_tbl, [Classe] = _cl)
VAR _n = COUNTROWS(_rows)
VAR _avg = AVERAGEX(_rows, [_igro])
VAR _manif = SUMX(_rows, [_manif])
VAR _body =
CONCATENATEX(
_rows,
VAR _ig = [_igro]
VAR _subt = [_subt]
VAR _subq = [_subq]
VAR _nps = [_nps]
VAR _tmr = [_tmr]
VAR _corIg = SWITCH(TRUE(), _ig >= 0.9, "#10b981", _ig >= 0.7, "#f2c94c", _ig >= 0.5, "#f97316", "#ef4444")
VAR _corNps = SWITCH(TRUE(), _nps >= 50, "#10b981", _nps >= 0, "#f2c94c", _nps >= -50, "#f97316", "#ef4444")
VAR _corTmr = SWITCH(TRUE(), _tmr <= 5, "#10b981", _tmr <= 10, "#f2c94c", "#ef4444")
VAR _flag = IF([_flag] = 1, "<span class='flag'></span>", "")
RETURN
"<tr>"
& "<td><b>" & [sigla] & "</b>" & _flag & "</td>"
& "<td>" & [Tipo] & "</td>"
& "<td>" & FORMAT([_manif], "#,0") & "</td>"
& "<td><b>" & FORMAT(_subt, "0.0%") & "</b><div class='bar'><div class='fill' style='width:" & FORMAT(_subt, "0.0%") & ";background:#38bdf8'></div></div></td>"
& "<td><b>" & FORMAT(_subq, "0.0%") & "</b><div class='bar'><div class='fill' style='width:" & FORMAT(_subq, "0.0%") & ";background:#a3e635'></div></div></td>"
& "<td><b style='color:" & _corIg & "'>" & FORMAT(_ig, "0.0%") & "</b></td>"
& "<td><b style='color:" & _corNps & "'>" & IF(_nps >= 0, "+", "") & FORMAT(_nps, "0") & "</b></td>"
& "<td><span style='color:" & _corTmr & "'>" & FORMAT(_tmr, "0.00") & "d</span></td>"
& "<td>" & FORMAT([_res], "0.0%") & "</td>"
& "<td>" & FORMAT([_ri], "0.0%") & "</td>"
& "<td>" & FORMAT([_pesq], "#,0") & "</td>"
& "</tr>",
"",
[_igro], DESC,
[sigla], ASC
)
RETURN
IF(
_n = 0,
"",
"<section class='cb'><div class='ch'><div><h2>" & _rotulo & "</h2><div class='m'>" & FORMAT(_n, "#,0") & " orgaos</div></div><div class='cs'><span>IGRO: <b>" & FORMAT(_avg, "0.0%") & "</b></span><span>Manif.: <b>" & FORMAT(_manif, "#,0") & "</b></span></div></div><div class='tw'><table class='tbl'><thead><tr><th>Sigla</th><th>Tipo</th><th>Manif.</th><th>Sub-T</th><th>Sub-Q</th><th>IGRO</th><th>NPS</th><th>TMR</th><th>Resolut.</th><th>% RI</th><th>Pesq.</th></tr></thead><tbody>" & _body & "</tbody></table></div></section>"
),
"",
[Classe], ASC
)
RETURN
"<!DOCTYPE html><html lang='pt-BR'><head><meta charset='UTF-8'>" & _CSS & "</head><body><div class='w'><h1>Matriz de Orgaos por Classe · IGRO</h1><p class='sub'>Rede estadual de ouvidorias · Goias</p><p class='note'>Renderizacao estatica para compatibilidade com o visual HTML do Power BI.</p>" & _summary & IF(_total = 0, "<div class='empty'>Nenhum resultado.</div>", _matrix) & "</div></body></html>"
```

**Como funciona:**
Usa 10 medida(s) e 19 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes, base_qtd_pesquisa, flag_amostra_insuficiente, idx_igro, idx_igro_sub_q, idx_igro_sub_t, ind_media_tempo_resposta, ind_nps.

**Usa:** `base_qtd_manifestacoes`, `base_qtd_pesquisa`, `flag_amostra_insuficiente`, `idx_igro`, `idx_igro_sub_q`, `idx_igro_sub_t`, `ind_media_tempo_resposta`, `ind_nps`, `ind_pct_resolutividade`, `ind_pct_respostas_insatisfatorias`, `CALCULATE([base_qtd_manifestacoes]`, `COALESCE(CALCULATE([base_qtd_pesquisa]`
**É usada por:** —


### HTML Tabela Resultados IGRO CSV

`_medidas.HTML Tabela Resultados IGRO CSV` · sem format string · 12 · JSON · Dashboard

**O que faz:**
Backup estatico da medida HTML Dashboard Final antes da substituicao do card NPS mantendo filtros.

**DAX:**
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
),
dOrgao_igro[Tipo] <> "Inativa"
&& NOT ISBLANK(dOrgao_igro[Classe])
&& dOrgao_igro[Classe] <> "N/A"
),
"_manif", COALESCE(CALCULATE([base_qtd_manifestacoes]), 0),
"_final", COALESCE(CALCULATE([base_qtd_manifestacoes_finalizadas]), 0),
"_aberto", COALESCE(CALCULATE([base_qtd_manifestacoes_em_aberto]), 0),
"_pesq", COALESCE(CALCULATE([base_qtd_pesquisa]), 0),
"_tmr", COALESCE(CALCULATE([ind_media_tempo_resposta]), 0),
"_rdp", COALESCE(CALCULATE([ind_pct_mais_30_dias]), 0),
"_tr", COALESCE(CALCULATE([ind_pct_resolutividade]), 0),
"_ri", COALESCE(CALCULATE([ind_pct_respostas_insatisfatorias]), 0),
"_nota", COALESCE(CALCULATE([ind_media_nota_recomendacao]), 0),
"_nps", COALESCE(CALCULATE([ind_nps]), 0),
"_prom", COALESCE(CALCULATE([ind_pct_promotores]), 0),
"_neut", COALESCE(CALCULATE([ind_pct_neutros]), 0),
"_det", COALESCE(CALCULATE([ind_pct_detratores]), 0),
"_s1", COALESCE(CALCULATE([idx_score_igro_kri1]), 0),
"_s2", COALESCE(CALCULATE([idx_score_igro_kri2]), 0),
"_s3", COALESCE(CALCULATE([idx_score_igro_kri3]), 0),
"_s4", COALESCE(CALCULATE([idx_score_igro_kri4]), 0),
"_s5", COALESCE(CALCULATE([idx_score_igro_kri5]), 0),
"_subt", COALESCE(CALCULATE([idx_igro_sub_t]), 0),
"_subq", COALESCE(CALCULATE([idx_igro_sub_q]), 0),
"_igro", COALESCE(CALCULATE([idx_igro]), 0),
"_flag", COALESCE(CALCULATE([flag_amostra_insuficiente]), 0)
)
VAR _data =
"[" &
CONCATENATEX(
_tbl,
"{sigla:" & _q & [sigla] & _q &
",tipo:" & _q & [Tipo] & _q &
",grupo:" & _q & [Grupo] & _q &
",classe:" & _q & [Classe] & _q &
",manifestacoes:" & FORMAT([_manif], "0") &
",finalizadas:" & FORMAT([_final], "0") &
",abertas:" & FORMAT([_aberto], "0") &
",pesquisas:" & FORMAT([_pesq], "0") &
",tmr:" & SUBSTITUTE(FORMAT([_tmr], "0.00"), ",", ".") &
",rdp:" & SUBSTITUTE(FORMAT([_rdp], "0.0000"), ",", ".") &
",tr:" & SUBSTITUTE(FORMAT([_tr], "0.0000"), ",", ".") &
",ri:" & SUBSTITUTE(FORMAT([_ri], "0.0000"), ",", ".") &
",nota:" & SUBSTITUTE(FORMAT([_nota], "0.00"), ",", ".") &
",nps:" & SUBSTITUTE(FORMAT([_nps], "0.00"), ",", ".") &
",promotores:" & SUBSTITUTE(FORMAT([_prom], "0.0000"), ",", ".") &
",neutros:" & SUBSTITUTE(FORMAT([_neut], "0.0000"), ",", ".") &
",detratores:" & SUBSTITUTE(FORMAT([_det], "0.0000"), ",", ".") &
",score_rdp:" & SUBSTITUTE(FORMAT([_s1], "0.0000"), ",", ".") &
",score_tmr:" & SUBSTITUTE(FORMAT([_s2], "0.0000"), ",", ".") &
",score_tr:" & SUBSTITUTE(FORMAT([_s3], "0.0000"), ",", ".") &
",score_ri:" & SUBSTITUTE(FORMAT([_s4], "0.0000"), ",", ".") &
",score_nr:" & SUBSTITUTE(FORMAT([_s5], "0.0000"), ",", ".") &
",sub_t:" & SUBSTITUTE(FORMAT([_subt], "0.0000"), ",", ".") &
",sub_q:" & SUBSTITUTE(FORMAT([_subq], "0.0000"), ",", ".") &
",igro:" & SUBSTITUTE(FORMAT([_igro], "0.0000"), ",", ".") &
",flag_amostra:" & FORMAT([_flag], "0") &
"}",
",",
[_igro], DESC,
[sigla], ASC
) & "]"
VAR _css =
"<style>*{box-sizing:border-box}body{margin:0;background:#061f20;color:#e2e8f0;font-family:Segoe UI,Arial,sans-serif;padding:14px}.wrap{max-width:1280px;margin:0 auto}h1{font-size:18px;color:#f2c94c;margin:0 0 4px;font-weight:800}.sub{font-size:11px;color:#9fb4bc;margin-bottom:12px}.toolbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;background:#0d3436;border:1px solid #1f5559;border-radius:8px;padding:10px;margin-bottom:10px}input,select,button{background:#092b2d;color:#e2e8f0;border:1px solid #1f5559;border-radius:6px;padding:6px 9px;font-size:12px}button{cursor:pointer;color:#fff;font-weight:700}.count{margin-left:auto;font-size:11px;color:#b8cad1}.tablebox{border:1px solid #1f5559;border-radius:8px;overflow:auto;max-height:620px}table{width:100%;border-collapse:collapse;font-size:11px;min-width:1500px}th{position:sticky;top:0;background:#0a292b;color:#b8cad1;text-align:left;text-transform:uppercase;font-size:9px;padding:8px;border-bottom:1px solid #1f5559;white-space:nowrap}td{color:#e2e8f0;padding:7px 8px;border-bottom:1px solid #0c2b2d;white-space:nowrap;text-align:right}td:first-child,td:nth-child(2),td:nth-child(3),td:nth-child(4){text-align:left}tr:hover td{background:#0d3436;color:#fff}.foot{font-size:10px;color:#78909a;margin-top:8px}</style>"
VAR _html =
"<!DOCTYPE html><html lang='pt-BR'><head><meta charset='UTF-8'>" & _css & "</head><body><div class='wrap'><h1>Tabela de Resultados Calculados · IGRO</h1><div class='sub'>Resultados por orgao com exportacao CSV</div><div class='toolbar'><input id='q' placeholder='Buscar orgao...'><select id='cl'><option value='all'>Todas as classes</option><option value='1'>Classe 1</option><option value='2'>Classe 2</option><option value='3'>Classe 3</option><option value='4'>Classe 4</option><option value='5'>Classe 5</option></select><select id='tp'><option value='all'>Todos os tipos</option><option value='Setorial'>Setorial</option><option value='Adjunta'>Adjunta</option></select><button id='csv'>Exportar CSV</button><span class='count' id='count'></span></div><div class='tablebox'><table><thead id='thead'></thead><tbody id='tbody'></tbody></table></div><div class='foot'>Campos percentuais exportados no mesmo formato exibido na tabela.</div></div>"
VAR _js =
"<script>const D=" & _data & ";const cols=[['sigla','Orgao'],['tipo','Tipo'],['grupo','Grupo'],['classe','Classe'],['manifestacoes','Manif.'],['finalizadas','Finalizadas'],['abertas','Abertas'],['pesquisas','Pesq.'],['tmr','TMR'],['rdp','% RDP'],['tr','TR'],['ri','% RI'],['nota','Nota'],['nps','NPS'],['promotores','% Prom.'],['neutros','% Neut.'],['detratores','% Detr.'],['score_rdp','Score RDP'],['score_tmr','Score TMR'],['score_tr','Score TR'],['score_ri','Score RI'],['score_nr','Score NR'],['sub_t','Sub-T'],['sub_q','Sub-Q'],['igro','IGRO'],['flag_amostra','Amostra insuf.']];function pct(v){return (Number(v)*100).toFixed(1)+'%'}function n2(v){return Number(v).toLocaleString('pt-BR',{maximumFractionDigits:2})}function fmt(k,v){if(['rdp','tr','ri','promotores','neutros','detratores','score_rdp','score_tmr','score_tr','score_ri','score_nr','sub_t','sub_q','igro'].includes(k))return pct(v);if(['tmr','nota','nps'].includes(k))return n2(v);if(k==='flag_amostra')return v==1?'Sim':'Nao';return v}function rows(){const q=(document.getElementById('q').value||'').toLowerCase();const cl=document.getElementById('cl').value;const tp=document.getElementById('tp').value;return D.filter(r=>(!q||r.sigla.toLowerCase().includes(q))&&(cl==='all'||r.classe===cl)&&(tp==='all'||r.tipo===tp));}function render(){const R=rows();document.getElementById('count').textContent=R.length+' orgaos';document.getElementById('thead').innerHTML='<tr>'+cols.map(c=>'<th>'+c[1]+'</th>').join('')+'</tr>';document.getElementById('tbody').innerHTML=R.map(r=>'<tr>'+cols.map(c=>'<td>'+fmt(c[0],r[c[0]])+'</td>').join('')+'</tr>').join('')}function csv(){const R=rows();const head=cols.map(c=>c[1]).join(';');const lines=R.map(r=>cols.map(c=>String(fmt(c[0],r[c[0]]))).join(';'));const blob=new Blob(['\ufeff'+[head].concat(lines).join('\n')],{type:'text/csv;charset=utf-8'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='resultados_igro.csv';a.click();URL.revokeObjectURL(a.href)}document.getElementById('q').addEventListener('input',render);document.getElementById('cl').addEventListener('change',render);document.getElementById('tp').addEventListener('change',render);document.getElementById('csv').addEventListener('click',csv);render();</script></body></html>"
RETURN _html & _js
```

**Como funciona:**
Usa 22 medida(s) e 56 coluna(s) referenciada(s) diretamente. Dependências principais: base_qtd_manifestacoes, base_qtd_manifestacoes_em_aberto, base_qtd_manifestacoes_finalizadas, base_qtd_pesquisa, flag_amostra_insuficiente, idx_igro, idx_igro_sub_q, idx_igro_sub_t.

**Usa:** `base_qtd_manifestacoes`, `base_qtd_manifestacoes_em_aberto`, `base_qtd_manifestacoes_finalizadas`, `base_qtd_pesquisa`, `flag_amostra_insuficiente`, `idx_igro`, `idx_igro_sub_q`, `idx_igro_sub_t`, `idx_score_igro_kri1`, `idx_score_igro_kri2`, `idx_score_igro_kri3`, `idx_score_igro_kri4`
**É usada por:** —
