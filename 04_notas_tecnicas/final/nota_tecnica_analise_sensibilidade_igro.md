# Nota técnica: análise de sensibilidade do IGRO

## 1. Objetivo

Esta nota técnica consolida a análise de sensibilidade do IGRO com três finalidades:

1. registrar, de forma metodologicamente explícita, por que a análise de sensibilidade é necessária em indicadores compostos;
2. apresentar os resultados empíricos obtidos para o IGRO a partir da base de 2024-2025;
3. oferecer texto-base para preenchimento das seções `3.5` e `4.6` do artigo.

## 2. Conceito e importância da análise de sensibilidade

A análise de sensibilidade é a etapa em que se verifica quanto o resultado de um indicador composto depende de escolhas metodológicas do pesquisador, como pesos, método de agregação e pequenas perturbações nos parâmetros. No referencial da `OCDE/JRC`, essa etapa é importante porque índices compostos não são resultados "naturais" dos dados; eles são construções analíticas que combinam decisões substantivas e matemáticas.

No caso do IGRO, essa verificação é especialmente relevante por três razões:

1. o índice combina dimensões heterogêneas de `Tempestividade` e `Qualidade`;
2. escolhas de peso podem alterar a ênfase relativa entre conformidade normativa e percepção cidadã;
3. o método de agregação pode ampliar ou reduzir a compensação entre indicadores.

Em termos práticos, a análise de sensibilidade responde a uma pergunta central: o diagnóstico produzido pelo índice permanece semelhante quando fazemos ajustes metodológicos plausíveis? Quando a resposta é positiva, aumenta a confiança de que o índice está captando um padrão substantivo da realidade, e não apenas um artefato da parametrização escolhida.

## 3. Base e desenho analítico

Os testes foram executados no notebook `06_notebooks/exploracao/igro_analise_sensibilidade_pesos.ipynb`, com exportação dos resultados para `09_resultados/exportacoes/analise_sensibilidade_pesos_igro/`.

O recorte empírico adotado foi:

- período: `2024-01-01` a `2025-12-31`;
- universo original do artigo: `51 órgãos`;
- base válida para os testes de sensibilidade: `47 órgãos`.

Os testes foram executados sobre `47 órgãos` porque `4` não possuíam informação completa para os cinco KRIs no recorte utilizado. Para a redação do artigo, essa restrição deve ser informada explicitamente na seção metodológica ou em nota de rodapé, para evitar inconsistência com a descrição geral da base.

Foram aplicados três testes.

### 3.1 Teste 1: variação de pesos

Foram comparados quatro cenários:

- `uniforme`: `0,20` para cada KRI;
- `qualidade`: `RP 0,25`, `NR 0,25`, `%RI 0,20`, `TMR 0,15`, `PMA 0,15`;
- `tempestividade`: `TMR 0,25`, `PMA 0,25`, `RP 0,20`, `%RI 0,15`, `NR 0,15`;
- `desenho_tecnico`: cenário adicional de referência operacional, usado para comparação interna.

Para o artigo, os resultados centrais devem enfatizar os três primeiros cenários, pois eles correspondem diretamente ao desenho já inserido na crítica aplicada.

### 3.2 Teste 2: método de agregação

Comparou-se o cálculo do IGRO por:

- média geométrica ponderada;
- média aritmética ponderada.

O objetivo foi verificar se a troca do agregador alteraria substancialmente os escores e a classificação de risco.

### 3.3 Teste 3: perturbação aleatória dos pesos

Foi executado um `bootstrap` com `1.000` iterações, introduzindo variação aleatória de `±10%` nos pesos originais, para observar a estabilidade dos escores sob pequenas flutuações paramétricas.

## 4. Resultados

### 4.1 Robustez sob diferentes cenários de peso

Os resultados indicam alta estabilidade do índice frente a variações plausíveis de ponderação.

- `89,4%` dos órgãos (`42` de `47`) mantiveram a mesma faixa de risco nos três cenários centrais do artigo (`uniforme`, `qualidade` e `tempestividade`).
- A mudança de classe foi pequena nas comparações par a par:
- `2` órgãos mudaram de faixa entre `uniforme` e `qualidade`;
- `3` órgãos mudaram de faixa entre `uniforme` e `tempestividade`;
- `5` órgãos mudaram de faixa entre `qualidade` e `tempestividade`.

As correlações de Spearman entre os rankings foram muito elevadas:

- `uniforme` × `qualidade`: `ρₛ = 0,9912` (`p < 0,001`);
- `uniforme` × `tempestividade`: `ρₛ = 0,9732` (`p < 0,001`);
- `qualidade` × `tempestividade`: `ρₛ = 0,9564` (`p < 0,001`).

Esses resultados indicam que a ordenação relativa dos órgãos permanece substantivamente estável, mesmo quando a ênfase do índice é deslocada em favor de uma das dimensões.

Em termos agregados, as estatísticas descritivas dos cenários também variaram pouco:

| Cenário | Média do IGRO | Mediana | Desvio-padrão |
|:--|--:|--:|--:|
| Uniforme | 36,94 | 43,07 | 38,98 |
| Qualidade | 37,04 | 40,44 | 38,87 |
| Tempestividade | 36,38 | 36,40 | 38,66 |
| Desenho técnico | 35,73 | 41,99 | 37,83 |

As maiores amplitudes entre cenários concentraram-se em poucos órgãos, o que sugere sensibilidade localizada, e não instabilidade sistêmica. Os maiores valores de variação máxima observados foram:

- `CODEGO`: `18,13 p.p.`
- `SEDS`: `17,83 p.p.`
- `SIC`: `15,35 p.p.`
- `EMATER`: `13,57 p.p.`
- `DETRAN`: `9,87 p.p.`

O padrão observado é consistente com a expectativa metodológica: órgãos com desempenho mais desequilibrado entre rapidez e qualidade tendem a ser mais sensíveis quando o vetor de pesos é alterado.

### 4.2 Geométrica versus aritmética

O segundo teste mostrou que a escolha do método de agregação produz efeito materialmente relevante.

- A substituição da média geométrica pela aritmética alterou a classe de risco de `29` dos `47` órgãos.
- O acréscimo médio do escore foi de `30,96 p.p.`
- A mediana do acréscimo foi de `21,49 p.p.`
- A diferença máxima observada foi de `79,60 p.p.`

Esse resultado confirma que a média aritmética tende a produzir escores mais altos, permitindo maior compensação entre indicadores. Em outras palavras, desempenhos muito baixos em um ou mais KRIs podem ser mascarados por resultados positivos em outros componentes.

Para um índice orientado por risco, esse comportamento é problemático. A lógica substantiva do IGRO pressupõe que fragilidades críticas em qualquer dimensão devam penalizar o resultado final, e não ser absorvidas integralmente por bons resultados parciais. Por isso, a média geométrica permanece mais coerente com a racionalidade do instrumento.

### 4.3 Bootstrap e estabilidade dos extremos

No teste de perturbação aleatória dos pesos, a estabilidade geral também foi elevada.

- amplitude média dos escores no bootstrap: `1,28 p.p.`
- amplitude mediana: `0,36 p.p.`
- percentil `90`: `3,68 p.p.`
- amplitude máxima: `5,24 p.p.`

Os casos de maior sensibilidade no bootstrap foram:

- `SIC`: `5,24 p.p.`
- `EMATER`: `4,64 p.p.`
- `SEDS`: `4,42 p.p.`
- `DETRAN`: `3,93 p.p.`
- `CODEGO`: `3,73 p.p.`

Apesar dessas variações localizadas, os extremos do ranking permaneceram bem separados. Considerando o `top-10` e o `bottom-10` do cenário uniforme, o menor limite inferior (`p05`) do grupo superior foi `82,81`, enquanto o maior limite superior (`p95`) do grupo inferior foi `0,00` quando arredondado a duas casas, o que indica ausência de sobreposição substantiva entre as posições extremas. Isso reforça a robustez do índice para distinguir situações muito favoráveis e muito desfavoráveis.

## 5. Interpretação metodológica

Os três testes convergem para uma leitura consistente.

Primeiro, o IGRO é robusto a mudanças plausíveis de pesos. A alta estabilidade de faixa e as correlações muito elevadas entre rankings indicam que a mensagem substantiva do índice não depende de forma decisiva da escolha entre um cenário mais neutro, mais orientado à qualidade ou mais orientado à tempestividade.

Segundo, o método de agregação importa mais do que pequenas variações de pesos. Enquanto os cenários de ponderação produziram mudanças limitadas e concentradas, a troca da média geométrica pela aritmética alterou fortemente os escores e a classificação de risco de grande parte dos órgãos.

Terceiro, a incerteza paramétrica residual mostrou-se baixa na maior parte dos casos. As amplitudes do bootstrap foram pequenas para a maioria dos órgãos e não comprometeram a separação entre extremos.

Em conjunto, esses achados sustentam a conclusão de que o IGRO possui boa robustez estrutural, mas depende criticamente da manutenção de um agregador não compensatório.

## 6. Sugestão final de ajuste

A recomendação metodológica final é:

1. manter a `média geométrica` como agregador principal do IGRO;
2. adotar `pesos uniformes` como especificação principal no artigo;
3. tratar os cenários `qualidade` e `tempestividade` como testes de robustez, e não como substitutos do modelo principal.

Essa recomendação se justifica por quatro razões:

1. os pesos uniformes são mais simples de explicar e defender academicamente;
2. os testes mostraram que o índice permanece estável sob cenários alternativos, o que reduz a necessidade de uma ponderação mais complexa para fins de artigo;
3. a média geométrica mostrou-se essencial para evitar compensações indevidas entre dimensões;
4. a combinação `pesos uniformes + média geométrica` produz o melhor equilíbrio entre parcimônia, interpretabilidade e coerência com a lógica de gestão de riscos.

Se houver interesse em manter a modelagem operacional do dashboard com parametrização própria do desenho técnico, isso pode continuar como uso gerencial interno. Para o artigo científico, porém, a especificação principal mais defensável é a versão com pesos uniformes e validação por sensibilidade.

## 7. Sugestão de texto para a seção 3.5 do artigo

Texto sugerido:

> A análise de sensibilidade foi conduzida para avaliar a robustez do IGRO frente a variações nos parâmetros de construção do índice, seguindo recomendação explícita do *Handbook on Constructing Composite Indicators* (OCDE/JRC, 2008). Os testes foram executados sobre os 47 órgãos que apresentaram informação completa para os cinco KRIs no recorte 2024-2025.
>
> Foram realizados três testes. No primeiro, a ponderação uniforme (`w = 0,20` para cada KRI) foi comparada com dois cenários alternativos: (a) ponderação com maior peso ao eixo Qualidade (`wRP = 0,25`; `wNR = 0,25`; `w%RI = 0,20`; `wTMR = 0,15`; `wPMA = 0,15`), privilegiando a percepção cidadã; e (b) ponderação com maior peso ao eixo Tempestividade (`wTMR = 0,25`; `wPMA = 0,25`; `wRP = 0,20`; `w%RI = 0,15`; `wNR = 0,15`), refletindo prioridade normativa. Em seguida, foram comparados os rankings resultantes por meio do coeficiente de correlação de postos de Spearman.
>
> No segundo teste, o IGRO calculado por média geométrica ponderada foi comparado com versão alternativa baseada em média aritmética ponderada, com o objetivo de verificar o grau de substitutibilidade introduzido pelo método de agregação.
>
> No terceiro teste, foi executado procedimento de perturbação aleatória dos pesos (`bootstrap`) com `1.000` iterações e variação de `±10%` em torno dos pesos originais, para avaliar a estabilidade dos escores e a robustez das posições extremas do ranking.

## 8. Sugestão de texto para a seção 4.6 do artigo

Texto sugerido:

> A análise de sensibilidade confirmou elevada robustez do IGRO sob cenários plausíveis de ponderação. Verificou-se que `89,4%` dos órgãos (`42` de `47`) mantiveram a mesma faixa de risco nos três cenários testados (`uniforme`, `qualidade` e `tempestividade`). As correlações de Spearman entre os rankings também foram muito elevadas: `ρₛ = 0,9912` entre os cenários uniforme e qualidade, `ρₛ = 0,9732` entre uniforme e tempestividade, e `ρₛ = 0,9564` entre qualidade e tempestividade (`p < 0,001` em todos os casos). Esses resultados indicam alta estabilidade ordinal do índice, mesmo quando se altera a ênfase relativa entre conformidade normativa e percepção cidadã.
>
> Em contraste, a substituição da média geométrica pela média aritmética produziu alterações substantivas. A classificação de risco mudou em `29` dos `47` órgãos, e a média aritmética elevou os escores em `30,96` pontos percentuais, em média. Esse padrão mostra que a agregação aritmética aumenta a compensação entre dimensões e tende a mascarar fragilidades relevantes em indicadores específicos, o que é indesejável em um instrumento orientado por risco.
>
> No teste de perturbação aleatória, a amplitude média dos escores foi de `1,28` ponto percentual, com mediana de `0,36` e máximo de `5,24`. Além disso, os intervalos de confiança a `90%` dos órgãos situados nos extremos do ranking não apresentaram sobreposição substantiva, confirmando estabilidade das posições mais altas e mais baixas. Em conjunto, os resultados sugerem que o IGRO é robusto a variações plausíveis de ponderação, mas depende da manutenção de um agregador não compensatório para preservar sua coerência substantiva.

## 9. Observação editorial

Se o artigo mantiver, nas seções anteriores, a formulação de que a base abrange `51 órgãos`, recomenda-se acrescentar uma frase curta na seção `3.5` esclarecendo que os testes de sensibilidade foram executados sobre `47 órgãos com dados completos para os cinco KRIs`, a fim de preservar consistência metodológica entre universo original e amostra analítica efetiva.
