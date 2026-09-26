# Referencia de medidas DAX do modelo IGRO

Inventário original: 2026-05-14
Revisão de governança: 2026-08-10
Modelo conectado: `indice_igro_v2` no Power BI Desktop  
Escopo: inventario funcional das 116 medidas da tabela tecnica `_medidas`

Esta nota serve como referencia rapida para manutencao, auditoria metodologica e futuras evolucoes do dashboard. O agrupamento abaixo segue a `displayFolder` definida no modelo.

> **Nota de uso:** esta referência foi atualizada junto com o alinhamento das medidas centrais do PBIP ao perfil canônico. O PBIX ainda precisa ser salvo/atualizado no Power BI Desktop e os resultados históricos precisam ser recalculados. Consulte a decisão canônica e o contrato de métricas.

## 01 - Volume

| Medida | Descricao |
|---|---|
| `base_qtd_manifestacoes_em_aberto` | Manifestacoes com status Aberta no SGOe. |
| `base_qtd_manifestacoes` | Total de manifestacoes registradas no periodo, independente do status. |
| `base_qtd_manifestacoes_finalizadas` | Manifestacoes com status Fechada ou Respondida no SGOe. |
| `base_qtd_lai` | Manifestacoes do tipo LAI (Lei de Acesso a Informacao), excluidas de alguns indicadores. |
| `base_manifestacoes_elegiveis` | Manifestacoes finalizadas descontando as LAI. Denominador base para KRI 3 e KRI 4. |
| `base_manifestacoes_identificadas` | Base de manifestacoes finalizadas identificadas (exclui Anonimo). Denominador correto para taxa de cobertura da pesquisa de satisfacao. |

## 02 - Pesquisa de Satisfacao

| Medida | Descricao |
|---|---|
| `base_qtd_pesquisa` | Total de respostas recebidas na pesquisa de satisfacao (linhas em `f_pesquisa`). `TREATAS` propaga filtro de `dOrgao_igro[sigla]`. |
| `base_qtd_sim` | Pesquisas em que o cidadao respondeu que a demanda foi resolvida totalmente (`finalizacao = "Sim"`). `TREATAS` propaga filtro de `dOrgao_igro[sigla]`. |
| `base_qtd_parcialmente` | Pesquisas em que o cidadao respondeu que a demanda foi resolvida parcialmente (`finalizacao = "Parcialmente"`). `TREATAS` propaga filtro de `dOrgao_igro[sigla]`. |
| `base_qtd_resolvidas` | Combinacao ponderada de respostas: `base_qtd_sim + 0,5 x base_qtd_parcialmente`. Numerador da resolutividade. |
| `ind_media_nota_recomendacao` | Media das notas de recomendacao (1-10) nas pesquisas respondidas. Numerador do KRI 5. `TREATAS` propaga filtro de `dOrgao_igro[sigla]`. |
| `ind_pct_resolutividade` | Percentual de resolucao: `(sim + 0,5 x parcialmente) / total de pesquisas`. Indicador do KRI 3. |
| `base_qtd_promotores` | Respostas de pesquisa com nota de recomendacao entre 9 e 10. Numerador do NPS. `TREATAS` propaga filtro de `dOrgao_igro[sigla]`. |
| `base_qtd_neutros` | Respostas de pesquisa com nota de recomendacao entre 7 e 8. Nao entram no calculo do NPS. `TREATAS` propaga filtro de `dOrgao_igro[sigla]`. |
| `base_qtd_detratores` | Respostas de pesquisa com nota de recomendacao entre 1 e 6. Subtraidas no calculo do NPS. `TREATAS` propaga filtro de `dOrgao_igro[sigla]`. |
| `ind_nps` | NPS calculado: `(% promotores - % detratores) x 100`. Escala de `-90` a `+100`. |
| `ind_pct_promotores` | Percentual de promotores (nota 9-10) sobre o total de pesquisas respondidas. |
| `ind_pct_neutros` | Percentual de neutros (nota 7-8) sobre o total de pesquisas respondidas. |
| `ind_pct_detratores` | Percentual de detratores (nota 1-6) sobre o total de pesquisas respondidas. |

## 03 - Qualidade

| Medida | Descricao |
|---|---|
| `base_qtd_respostas_insatisfatorias` | Total de linhas em `f_insatisfatorias`. Respostas reprovadas na revisao de qualidade. `TREATAS` propaga filtro de `dOrgao_igro[sigla]`. |
| `ind_pct_respostas_insatisfatorias` | Percentual de respostas insatisfatorias sobre as manifestacoes elegiveis. Indicador do KRI 4. |
| `base_qtd_procedente` | Manifestacoes finalizadas com `procedente = "Sim"`. |
| `base_qtd_com_recurso` | Manifestacoes finalizadas que geraram ao menos um recurso (campo `recurso` preenchido). |
| `ind_pct_procedencia` | Percentual de manifestacoes com analise procedente sobre o total de finalizadas. |
| `ind_pct_recurso` | Percentual de manifestacoes que geraram recurso sobre o total de finalizadas. Indicador de retrabalho. |
| `ind_pct_cobertura_reclamacao` | Percentual de Reclamacoes finalizadas que receberam resposta na pesquisa de satisfacao. |

## 04 - Tempo

| Medida | Descricao |
|---|---|
| `base_qtd_mais_30_dias` | Manifestacoes com mais de 30 dias de vida (`dias_vida > 30`). Numerador do KRI 1. |
| `ind_media_tempo_resposta` | Media de `dias_vida` das manifestacoes. Tempo Medio de Resposta (TMR). Numerador do KRI 2. |
| `ind_pct_mais_30_dias` | Percentual de manifestacoes com mais de 30 dias de vida sobre o total. Indicador do KRI 1. |
| `base_qtd_manifestacoes_aa` | Volume de manifestacoes no mesmo periodo do ano anterior. Funciona com qualquer granularidade de `dCalendario` (dia, mes, quadrimestre). |
| `ind_tmr_aa` | TMR medio no mesmo periodo do ano anterior. Funciona com qualquer granularidade de `dCalendario`. |
| `ind_var_pct_volume_aa` | Variacao percentual do volume de manifestacoes em relacao ao mesmo periodo do ano anterior. |
| `base_qtd_manifestacoes_quadri_anterior` | Volume de manifestacoes no quadrimestre anterior ao periodo selecionado. |
| `ind_var_pct_volume_quadri` | Variacao percentual do volume em relacao ao quadrimestre anterior. |
| `base_qtd_manifestacoes_ytd` | Acumulado de manifestacoes no ano ate a data maxima do contexto (YTD). |
| `ind_media_diaria_manifestacoes` | Volume medio diario de manifestacoes no periodo selecionado. Util para comparar periodos de tamanhos diferentes. |
| `ind_indice_sazonalidade` | Indica se o mes esta acima ou abaixo da media mensal do ano. `1.0 = media`, `>1.0 = pico sazonal`, `<1.0 = vale`. Requer contexto mensal no visual. |
| `base_qtd_manifestacoes_dias_uteis` | Manifestacoes registradas em dias uteis (segunda a sexta). |
| `base_qtd_manifestacoes_fim_semana` | Manifestacoes registradas em fins de semana (sabado e domingo). |
| `ind_pct_fim_semana` | Percentual do volume registrado fora de dias uteis. Indica pressao sobre canais digitais (`Expresso/Webservice`) no final de semana. |
| `ind_media_movel_3m` | Media movel de 3 meses do volume de manifestacoes. Usa janela deslizante de `AnoMes`. Requer contexto mensal no visual. |
| `ind_var_vs_media_movel` | Compara o volume do mes atual com a media movel de 3 meses. Positivo = acima da tendencia, negativo = abaixo. |
| `base_qtd_finalizadas_por_data_fin` | Volume de manifestacoes usando a data de finalizacao como eixo temporal. Requer `USERELATIONSHIP` com `dCalendario[Date]` via relacionamento inativo. |

## 05 - IGRO - Metas e Goalposts

| Medida | Descricao |
|---|---|
| meta_igro_kri1 | Meta canônica do KRI 1: máximo de 2,0% de manifestações acima de 30 dias. Valor 1 quando RDP <= 2,0%. |
| goal_igro_kri1 | Goalpost canônico do KRI 1: 15,0% como deterioração severa. Valor 0 quando RDP >= 15,0%. |
| meta_igro_kri2 | Meta canônica do KRI 2: 10 dias ou menos. Valor 1 quando TMR <= 10 dias. |
| goal_igro_kri2 | Goalpost canônico do KRI 2: 30 dias como deterioração severa. Valor 0 quando TMR >= 30 dias. |
| meta_igro_kri3 | Meta canônica do KRI 3: 70% ou mais de resolutividade. |
| goal_igro_kri3 | Goalpost canônico do KRI 3: 30% como deterioração severa. Valor 0 quando TR <= 30%. |
| meta_igro_kri4 | Meta canônica do KRI 4: 2,5% ou menos de respostas insatisfatórias. |
| goal_igro_kri4 | Goalpost canônico do KRI 4: 20,0% como deterioração severa. Valor 0 quando RI >= 20,0%. |
| meta_igro_kri5 | Meta canônica do KRI 5: nota de recomendação 7,5 ou mais. |
| goal_igro_kri5 | Goalpost canônico do KRI 5: nota 4,0 como deterioração severa. Valor 0 quando NR <= 4,0. |
| `flag_amostra_insuficiente` | Flag de amostra insuficiente para KRIs de pesquisa (v3 FPC corrigido). Denominador exclui manifestacoes anonimas, que nao podem gerar pesquisa de satisfacao. `Flag = 1` quando `n_obs < 30` e taxa `< 5%` das finalizadas identificadas. |

## 06 - IGRO - Scores KRI

| Medida | Descricao |
|---|---|
| idx_score_igro_kri1 | Score canônico do KRI 1: 1 quando RDP <= 2,0%; 0 quando RDP >= 15,0%. |
| idx_score_igro_kri2 | Score canônico do KRI 2: 1 quando TMR <= 10 dias; 0 quando TMR >= 30 dias. |
| idx_score_igro_kri3 | Score canônico do KRI 3: 1 quando TR >= 70%; 0 quando TR <= 30%; sem cálculo com amostra insuficiente. |
| idx_score_igro_kri4 | Score canônico do KRI 4: 1 quando RI <= 2,5%; 0 quando RI >= 20,0%. |
| idx_score_igro_kri5 | Score canônico do KRI 5: 1 quando NR >= 7,5; 0 quando NR <= 4,0; sem cálculo com amostra insuficiente. |

## 07 - IGRO - Indice

| Medida | Descricao |
|---|---|
| idx_igro_sub_t | Subíndice canônico de Tempestividade: pesos globais KRI 1 = 15% e KRI 2 = 25%. |
| idx_igro_sub_q | Subíndice canônico de Qualidade: pesos globais KRI 3 = 25%, KRI 4 = 15% e KRI 5 = 20%; sem cálculo com amostra insuficiente. |
| `idx_igro` | Indice de Gestao de Riscos de Ouvidorias. Media geometrica simples: `sqrt(IT x IQ)`. Conforme metodologia IGRO - artigo CGU. |

## 08 - Formatacao

| Medida | Descricao |
|---|---|
| `fmt_semaforo_nps` | Rotulo de semaforo para o NPS: Verde (`>=50`), Amarelo (`0-49`), Laranja (`-49 a -1`), Vermelho (`<-50`). |
| `fmt_cor_fundo_nps` | Cor de fundo hexadecimal para o NPS conforme faixa. |
| `fmt_cor_fonte_nps` | Cor de fonte hexadecimal para o NPS conforme faixa. |
| `fmt_semaforo_procedencia` | Rotulo de semaforo para `ind_pct_procedencia`: Verde (`>=60%`), Amarelo (`40-59%`), Laranja (`20-39%`), Vermelho (`<20%`). |
| `fmt_semaforo_recurso` | Rotulo de semaforo para `ind_pct_recurso`: Verde (`<=1%`), Amarelo (`1-3%`), Laranja (`3-5%`), Vermelho (`>5%`). |
| `fmt_semaforo_igro` | Rotulo de semaforo para o IGRO conforme faixas da metodologia (artigo CGU): Verde `>=90%`, Amarelo `70-89%`, Laranja `50-69%`, Vermelho `<50%`. |
| `fmt_semaforo_igro_sub_t` | Rotulo de semaforo para o Sub-T com faixas da metodologia IGRO (artigo CGU). |
| `fmt_semaforo_igro_sub_q` | Rotulo de semaforo para o Sub-Q com faixas da metodologia IGRO (artigo CGU). |
| `fmt_cor_fundo_igro` | Cor de fundo hexadecimal para o IGRO conforme faixas da metodologia (artigo CGU). `Controlado = #27AE60`, `Em atencao = #F39C12`, `Elevado = #E67E22`, `Critico = #E74C3C`. |
| `fmt_cor_fonte_igro` | Cor de fonte hexadecimal para o IGRO conforme faixa de risco. Usar em formatacao condicional de cor de fonte. |
| `fmt_cor_fundo_igro_sub_t` | Cor de fundo hexadecimal para o Sub-T conforme faixas da metodologia IGRO (artigo CGU). |
| `fmt_cor_fundo_igro_sub_q` | Cor de fundo hexadecimal para o Sub-Q conforme faixas da metodologia IGRO (artigo CGU). |

## 09 - Variacao

| Medida | Descricao |
|---|---|
| `var_tmr` | Variacao absoluta do TMR vs. periodo anterior. Negativo = melhora (menos dias). |
| `var_pct_mais_30_dias` | Variacao absoluta do `% de manifestacoes com mais de 30 dias` vs. periodo anterior. Negativo = melhora. |
| `var_resolutividade` | Variacao absoluta da resolutividade vs. periodo anterior. Positivo = melhora. |
| `var_insatisfatorias` | Variacao absoluta do `% de respostas insatisfatorias` vs. periodo anterior. Negativo = melhora. Eixo temporal via `dCalendario` (corrigido). |
| `var_nota` | Variacao absoluta da nota media de recomendacao vs. periodo anterior. Positivo = melhora. |
| `var_nps` | Variacao absoluta do NPS vs. periodo anterior. Positivo = melhora. |
| `var_igro` | Variacao absoluta do IGRO vs. periodo anterior. Positivo = melhora. |
| `var_igro_sub_t` | Variacao absoluta do Sub-T vs. periodo anterior. Positivo = melhora. |
| `var_igro_sub_q` | Variacao absoluta do Sub-Q vs. periodo anterior. Positivo = melhora. |
| `var_recurso` | Variacao absoluta do `% de recurso` vs. periodo anterior. Negativo = melhora. |
| `var_cobertura_reclamacao` | Variacao absoluta da cobertura de pesquisa em Reclamacoes vs. periodo anterior. Positivo = melhora. |

## 10 - Semaforo - Variacao

| Medida | Descricao |
|---|---|
| `sem_tmr` | Semaforo do TMR com polaridade negativa: verde quando cai (melhora), vermelho quando sobe (piora). Neutro quando variacao = `0` ou `BLANK`. |
| `sem_pct_mais_30_dias` | Semaforo do `% +30 dias` com polaridade negativa: verde quando cai. |
| `sem_resolutividade` | Semaforo da resolutividade com polaridade positiva: verde quando sobe. |
| `sem_insatisfatorias` | Semaforo das respostas insatisfatorias com polaridade negativa: verde quando cai. |
| `sem_nota` | Semaforo da nota media com polaridade positiva: verde quando sobe. |
| `sem_nps` | Semaforo do NPS com polaridade positiva: verde quando sobe. |
| `sem_igro` | Semaforo do IGRO com polaridade positiva: verde quando sobe. |
| `sem_igro_sub_t` | Semaforo do Sub-T com polaridade positiva. |
| `sem_igro_sub_q` | Semaforo do Sub-Q com polaridade positiva. |
| `sem_recurso` | Semaforo do `% de recurso` com polaridade negativa: verde quando cai. |
| `sem_cobertura_reclamacao` | Semaforo da cobertura de pesquisa em Reclamacoes com polaridade positiva: verde quando sobe. |

## 11 - Rotulo - Cartao

| Medida | Descricao |
|---|---|
| `lbl_tmr` | Rotulo completo para cartao do TMR: valor atual + semaforo + delta formatado. |
| `lbl_pct_mais_30_dias` | Rotulo completo para cartao do `% +30 dias`. |
| `lbl_resolutividade` | Rotulo completo para cartao da resolutividade. |
| `lbl_insatisfatorias` | Rotulo completo para cartao das respostas insatisfatorias. |
| `lbl_nota` | Rotulo completo para cartao da nota media. |
| `lbl_nps` | Rotulo completo para cartao do NPS. |
| `lbl_igro` | Rotulo completo para cartao do IGRO. |
| `lbl_igro_sub_t` | Rotulo completo para cartao do Sub-T. |
| `lbl_igro_sub_q` | Rotulo completo para cartao do Sub-Q. |

## 12 - JSON - Dashboard

| Medida | Descricao |
|---|---|
| `_JSON Orgaos` | Array JSON com IGRO e KRIs por orgao, ordenado por IGRO desc. Usa `SUMMARIZE` com colunas calculadas. |
| `_JSON Tipos` | Array JSON com distribuicao por tipo de manifestacao. |
| `_JSON KPIs` | Array JSON com KPIs globais da rede para injecao direta nos cards do dashboard. |
| `HTML Dashboard IGRO` | Dashboard HTML interativo do IGRO. Tema dark, cards KPI, ranking de orgaos, distribuicao por tipo, tabela com busca e export CSV. |
| `HTML Dashboard Final Base` | Dashboard HTML `IGRO-NPS v3` - corrige JSON invalido (ano nulo) e filtra anos sem dados. |
| `HTML Matriz Classes IGRO` | Matriz HTML por Classe IGRO `v8` - texto da tabela em branco para melhor contraste. |
| `HTML Dashboard Final Fonte Branca` | Versao do Dashboard Final com override de CSS para fonte branca em textos que apareciam pretos. |
| `HTML Dashboard Final` | Dashboard HTML `IGRO-NPS` com override de CSS para textos em branco/claro. |
| `HTML Tabela Resultados IGRO CSV` | Tabela/matriz HTML com dados em literal JS, filtros e exportacao CSV dos resultados calculados por orgao. |
| `HTML Infografico IGRO` | Infografico HTML executivo do IGRO com hierarquia visual entre indice composto, subindices e KRIs. Foi usado para iteracoes de layout e alinhamento visual no dashboard. |
| `HTML Dashboard Final Backup` | Backup tecnico da medida `HTML Dashboard Final` antes de ajustes visuais posteriores. Manter apenas como referencia de seguranca. |

## Observacoes de uso

- Esta referencia e um catalogo funcional das medidas. Ela foi gerada a partir das `displayFolders`, nomes tecnicos e descricoes cadastradas no modelo.
- As medidas HTML/JSON foram mantidas no inventario porque fazem parte do modelo e sustentam artefatos do dashboard.
- Se voce quiser, no proximo passo eu posso gerar uma segunda nota complementar apenas com as formulas DAX das medidas criticas do IGRO (`KRIs`, `scores`, `subindices` e `indice final`).
