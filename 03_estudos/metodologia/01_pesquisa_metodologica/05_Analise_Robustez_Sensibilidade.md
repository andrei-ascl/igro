# Análise de Robustez e Sensibilidade

## Por que testar a robustez?

Um índice composto envolve diversas escolhas metodológicas subjetivas: método de normalização, atribuição de pesos e técnica de agregação. A análise de robustez verifica se os resultados (ranking, classificação) são estáveis diante de variações nessas escolhas. Se pequenas mudanças nos pesos ou no método alteram drasticamente o resultado, o índice não é confiável.

---

## Análise de Incerteza

Estima a incerteza nos outputs (scores, rankings) dadas as incertezas nos inputs (decisões metodológicas, pesos etc.). Os resultados incluem intervalos de confiança sobre os rankings, rankings medianos e distribuições de probabilidade.

**Perguntas que responde:**
- Qual a variabilidade do meu índice dado diferentes cenários de pesos?
- Posso confiar que a unidade X realmente tem desempenho melhor que Y?
- Quão estável é o resultado ao longo do tempo?

---

## Análise de Sensibilidade

Vai além da análise de incerteza: identifica **quais** incertezas são as mais relevantes para a variabilidade do resultado.

**Perguntas que responde:**
- Mudar os pesos da Resolutividade afeta mais o índice do que mudar os pesos do Prazo Médio?
- A escolha entre Min-Max e Z-Score altera significativamente o resultado?
- Qual decisão metodológica precisa de mais atenção?

### Método de Monte Carlo

A técnica principal é o **método de Monte Carlo**: recalcular o índice composto centenas ou milhares de vezes, variando aleatoriamente os parâmetros incertos a cada iteração.

**Etapas:**
1. Definir os parâmetros incertos e suas faixas de variação
2. Gerar N conjuntos aleatórios de parâmetros (ex: N = 500 a 1000)
3. Recalcular o índice para cada conjunto
4. Analisar a distribuição dos resultados
5. Calcular índices de sensibilidade (ex: Sobol indices)

**Exemplo prático:**
- Variar pesos: w_resolutividade ∈ [0,15; 0,35] em vez de fixo em 0,25
- Variar método de normalização: Min-Max vs Z-Score vs Distância à Meta
- Variar agregação: Aritmética vs Geométrica

### Interação entre incertezas

"Pode-se pensar que a análise de sensibilidade pode ser feita variando uma premissa de cada vez; no entanto, as incertezas interagem entre si." Por isso o Monte Carlo varia todos os parâmetros simultaneamente.

---

## Testes Práticos Recomendados

### 1. Teste de Remoção de Indicador (Leave-one-out)
Remover um indicador por vez e verificar se o resultado muda significativamente.

### 2. Teste de Variação de Pesos
Usar 3-5 cenários de pesos diferentes:
- Cenário base (pesos definidos por especialistas)
- Pesos iguais
- Cenário com peso dobrado para tempestividade
- Cenário com peso dobrado para qualidade

### 3. Teste de Método de Normalização
Calcular o índice com Min-Max, Z-Score e Distância à Meta e comparar resultados.

### 4. Teste de Agregação
Calcular com média aritmética e geométrica e comparar.

---

## Critérios de Robustez

O índice é considerado robusto quando:

- O ranking/classificação se mantém estável em pelo menos 80% dos cenários testados
- Nenhuma decisão metodológica individual domina a variabilidade do resultado
- Os intervalos de confiança dos scores não se sobrepõem significativamente entre unidades classificadas diferentemente

---

## Ferramentas

### COINr (R Package)
Pacote desenvolvido pelo JRC da Comissão Europeia especificamente para construção e análise de indicadores compostos. Inclui módulos para:
- Normalização, ponderação e agregação
- Análise de sensibilidade global automatizada
- Visualização de resultados
- [Site oficial](https://bluefoxr.github.io/COINr/)

### Planilhas Excel
Para análises mais simples, cenários de pesos podem ser testados em planilhas com macros ou tabelas de sensibilidade.

---

## Fontes

- [COINr — Sensitivity Analysis](https://cran.r-project.org/web/packages/COINr/vignettes/sensitivity.html)
- [COINr Documentation — Chapter 14](https://bluefoxr.github.io/COINrDoc/sensitivity-analysis.html)
- [Robustness and Sensitivity of Weighting and Aggregation (Ecological Indicators)](https://www.sciencedirect.com/science/article/abs/pii/S1470160X13000034)
- [OECD Handbook — Uncertainty and Sensitivity Analysis](https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf)
