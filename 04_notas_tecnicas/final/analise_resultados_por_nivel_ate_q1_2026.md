# Análise dos resultados por nível até Q1/2026

## Escopo

Esta nota amplia a leitura anterior e organiza a análise do IGRO em três níveis hierárquicos:

1. `Nível 1`: índice composto (`IGRO`)
2. `Nível 2`: subíndices (`Subíndice de Tempestividade` e `Subíndice de Qualidade`)
3. `Nível 3`: indicadores-base do modelo (`KRI 1` a `KRI 5`)

Por solicitação do usuário, o ponto `Q2/2026` foi desconsiderado. A análise cobre, portanto, o período de `Q1/2024` a `Q1/2026`.

## Base de cálculo utilizada

Esta nota foi construída com base em duas fontes do próprio projeto:

- os dados brutos em `06_dados/01_brutos/`
- as fórmulas do modelo ativo do dashboard em [\_medidas.tmdl](C:/Users/andre/OneDrive/Claude-Work/Projects/igro/07_dashboards/powerbi/04_powerbi_e_dax/indice_igro_v2.SemanticModel/definition/tables/_medidas.tmdl)

Isso é importante porque a análise por nível abaixo reproduz a lógica efetivamente usada no dashboard atual, incluindo:

- metas e goalposts dos cinco KRIs;
- pesos do `Subíndice de Tempestividade`: `KRI 1 = 40%` e `KRI 2 = 60%`;
- pesos do `Subíndice de Qualidade`: `KRI 3 = 40%`, `KRI 4 = 30%` e `KRI 5 = 30%`;
- agregação final do `IGRO` por média geométrica simples entre os dois subíndices.

## Série consolidada até Q1/2026

| Período | IGRO | Sub-T | Sub-Q | KRI 1 % > 30 dias | KRI 2 TMR | KRI 3 Resolutividade | KRI 4 % RI | KRI 5 Nota |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Q1/2024 | 69,1 | 73,8 | 64,6 | 0,76% | 7,18 | 57,59% | 1,41% | 7,29 |
| Q2/2024 | 79,6 | 91,0 | 69,7 | 0,81% | 5,75 | 58,34% | 1,43% | 7,53 |
| Q3/2024 | 72,7 | 73,7 | 71,7 | 0,49% | 7,19 | 59,50% | 1,51% | 7,51 |
| Q1/2025 | 68,0 | 75,3 | 61,5 | 0,58% | 7,06 | 56,10% | 1,60% | 7,28 |
| Q2/2025 | 75,3 | 84,4 | 67,2 | 0,61% | 6,30 | 57,28% | 1,27% | 7,51 |
| Q3/2025 | 71,2 | 83,8 | 60,4 | 0,40% | 6,35 | 55,31% | 1,51% | 7,32 |
| Q1/2026 | 62,3 | 87,7 | 44,2 | 0,35% | 6,03 | 50,17% | 1,50% | 6,92 |

## Nível 1: índice composto

No nível do índice final, a série mostra um comportamento oscilante até `Q3/2025`, mas com inflexão negativa clara no fechamento em `Q1/2026`. O `IGRO` sai de `69,1` em `Q1/2024`, alcança pico em `Q2/2024` (`79,6`) e encerra o recorte em `62,3`, com queda de `8,9 p.p.` em relação ao quadrimestre imediatamente anterior.

O principal ponto de leitura executiva é que o índice composto não caiu por deterioração generalizada de todos os componentes. Ele caiu porque houve forte perda na camada de qualidade, suficiente para superar a melhora ocorrida na camada de tempestividade.

## Nível 2: subíndices

### Subíndice de Tempestividade

O `Subíndice de Tempestividade` evolui de `73,8` para `87,7` entre `Q1/2024` e `Q1/2026`. A série apresenta oscilação, mas a tendência geral é favorável, com ganho acumulado de `13,8 p.p.`.

Essa trajetória indica melhora operacional no componente de tempo, especialmente puxada pelo `KRI 2`, que tem maior peso interno no subíndice. Em termos gerenciais, a dimensão temporal não explica a piora final do IGRO; ao contrário, ela amortece parte da deterioração global.

### Subíndice de Qualidade

O `Subíndice de Qualidade` é o principal foco de atenção. Ele parte de `64,6`, alcança `71,7` em `Q3/2024`, mas depois entra em trajetória de enfraquecimento, fechando `Q1/2026` em `44,2`.

Os dois sinais mais críticos são:

- perda acumulada de `20,4 p.p.` no período analisado;
- queda de `16,2 p.p.` apenas entre `Q3/2025` e `Q1/2026`.

Isso mostra que a deterioração do IGRO no trecho final é, essencialmente, uma deterioração da qualidade do atendimento.

## Nível 3: KRIs do modelo

### KRI 1: percentual de manifestações com mais de 30 dias

O `KRI 1` melhora ao longo da série: cai de `0,76%` para `0,35%`. No modelo ativo, todos os valores observados ficam melhores que a meta de `1,0%`, o que mantém o score normalizado em `100%` ao longo de todo o período.

Leitura:

- é um indicador estável e favorável;
- não pressiona negativamente o subíndice de tempestividade;
- não explica a piora do IGRO no fechamento.

### KRI 2: tempo médio de resposta

O `KRI 2` também melhora no período: sai de `7,18` dias e chega a `6,03` dias em `Q1/2026`. Embora ainda permaneça acima da meta de excelência de `5` dias, há avanço relevante no score normalizado, que sobe de `56,4%` para `79,4%`.

Leitura:

- é o principal motor da melhora do `Subíndice de Tempestividade`;
- por ter peso interno maior que o `KRI 1`, sua evolução positiva é decisiva para levar o subíndice a `87,7`;
- seu comportamento confirma que o problema final do índice não está no tempo, mas em outra dimensão.

### KRI 3: resolutividade

O `KRI 3` é o indicador mais crítico da série. Ele parte de `57,59%`, oscila em faixa intermediária até `Q3/2025` e desaba para `50,17%` em `Q1/2026`. Como a meta do modelo é `70%` e o goalpost inferior é `50%`, o score normalizado praticamente zera no último ponto (`0,85%`).

Leitura:

- é o principal vetor de deterioração do `Subíndice de Qualidade`;
- responde pela ruptura mais forte da série no fechamento;
- sugere perda concreta de capacidade de resolver a demanda do cidadão na percepção capturada pela pesquisa.

Entre todos os KRIs, este é o que mais explica a piora estrutural do IGRO até `Q1/2026`.

### KRI 4: percentual de respostas insatisfatórias

O `KRI 4` oscila pouco, entre `1,27%` e `1,60%`, permanecendo sempre abaixo da meta de `2,5%`. Por isso, no modelo ativo, seu score normalizado permanece em `100%` durante toda a série analisada.

Leitura:

- o indicador não se configura como fator de pressão para o índice no recorte observado;
- há variação operacional, mas ela não ultrapassa o limiar metodológico definido no dashboard;
- sua estabilidade ajuda a conter a queda do `Subíndice de Qualidade`, mas não compensa a piora em resolutividade e recomendação.

### KRI 5: nota de recomendação

O `KRI 5` apresenta deterioração moderada, porém contínua no fechamento da série. A nota média vai de `7,29` em `Q1/2024` para `6,92` em `Q1/2026`, o que reduz o score normalizado de `64,6%` para `46,2%`.

Leitura:

- é o segundo principal vetor de deterioração da qualidade;
- a queda não é tão abrupta quanto a da resolutividade, mas reforça a piora do subíndice;
- sugere perda de confiança ou enfraquecimento da experiência global do usuário com a ouvidoria.

## Síntese analítica por nível

Quando os três níveis são lidos em conjunto, o diagnóstico fica mais claro:

1. No `Nível 1`, o `IGRO` piora no trecho final e encerra `Q1/2026` em patamar inferior ao início da série.
2. No `Nível 2`, a `Tempestividade` melhora, enquanto a `Qualidade` se deteriora fortemente.
3. No `Nível 3`, a piora se concentra em dois indicadores de qualidade:
   - `KRI 3 - Resolutividade`, como fator principal;
   - `KRI 5 - Nota de Recomendação`, como fator secundário relevante.

Em sentido oposto, os dois indicadores de menor pressão no período são:

- `KRI 1 - % acima de 30 dias`
- `KRI 4 - % de respostas insatisfatórias`

Ambos permanecem em faixa metodologicamente confortável no modelo ativo.

## Conclusão executiva

Desconsiderando `Q2/2026`, o resultado até `Q1/2026` pode ser resumido da seguinte forma:

- o `IGRO` piora no fechamento da série, mas essa piora não é generalizada;
- o componente de `Tempestividade` evolui favoravelmente e ajuda a amortecer a queda do índice;
- o componente de `Qualidade` sofre deterioração relevante e é o verdadeiro ponto de ruptura;
- no nível dos KRIs, o problema central está em `Resolutividade`, reforçado pela queda da `Nota de Recomendação`;
- a prioridade analítica e gerencial deve se concentrar na recuperação da efetividade percebida da resposta, e não apenas na velocidade de tramitação.

## Observação final

Como esta nota foi reconstruída a partir do modelo ativo do dashboard, ela é a referência mais adequada para dialogar com as telas atualmente produzidas no Power BI. Se fizer sentido, o próximo passo natural é gerar uma terceira nota com recomendações de ação por KRI e por subíndice.
