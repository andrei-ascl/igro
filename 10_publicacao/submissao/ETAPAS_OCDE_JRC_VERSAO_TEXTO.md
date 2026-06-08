# Etapas Metodológicas OCDE/JRC Aplicadas ao IGRO — Versão em Texto

> **Referência:** Handbook on Constructing Composite Indicators (OCDE/JRC, 2008)

---

## **Etapa 1: Seleção de Indicadores**

O IGRO foi estruturado a partir de cinco Indicadores-Chave de Risco (KRIs) distribuídos em dois eixos temáticos: Tempestividade (KRI 1 e KRI 2) e Qualidade (KRI 3, KRI 4 e KRI 5). Esta seleção foi validada por três fontes complementares: análise de benchmarking de ouvidorias estaduais, revisão de literatura especializada e consulta participativa na Oficina de Prototipação de Relatório das Ouvidorias (SEAD/Pequi Lab, 2023, com 29 participantes do GT Relatórios Gerenciais).

---

## **Etapa 2: Normalização**

Cada KRI foi convertido para escala uniforme [0, 1] utilizando o método de distância à meta com goalposts, conforme recomendado pelo Handbook OCDE/JRC para contextos nos quais existem metas regulatórias pré-definidas. Para indicadores onde "menor = melhor" (KRI 1, KRI 2, KRI 4), a fórmula aplicada foi: `score = (limite_máx − valor) / (limite_máx − meta)`, limitado ao intervalo [0, 1]. Os goalposts foram definidos através de triangulação entre três fontes: expertise de pesquisadores, benchmarking de ouvidorias estaduais e conformidade com marcos regulatórios (Lei nº 13.460/2017 e Decreto Estadual nº 10.466/2024).

---

## **Etapa 3: Ponderação**

A estrutura de pesos foi organizada em dois níveis hierárquicos. No primeiro nível, os dois sub-índices recebem pesos diferenciados: Sub-IGRO_T (Tempestividade) = 40% e Sub-IGRO_Q (Qualidade) = 60%, refletindo que qualidade é o principal driver de confiança cidadã. No segundo nível, dentro de cada sub-índice, os KRIs recebem pesos locais proporcionais à sua capacidade preditiva: KRI 1 (15% global), KRI 2 (25% global), KRI 3 (25% global), KRI 4 (15% global) e KRI 5 (20% global). Esta estrutura permite tanto síntese executiva quanto auditabilidade de qual dimensão específica gerou o alerta.

---

## **Etapa 4: Agregação**

A agregação foi implementada em dois níveis complementares. Dentro de cada sub-índice (agregação intra-dimensional), utilizou-se média aritmética ponderada, reconhecendo que indicadores do mesmo risco podem ser parcialmente substitutos. Entre os dois sub-índices (agregação inter-dimensional), adotou-se média geométrica ponderada segundo a fórmula: IGRO = Sub_T^0,40 × Sub_Q^0,60. Esta escolha é crítica: a média geométrica penaliza desequilíbrios, impedindo que excelência em Tempestividade compense falha crítica em Qualidade. Empiricamente, uma ouvidoria com Sub_T = 1,0 e Sub_Q = 0,40 recebe IGRO = 0,576 (risco alto), não 0,64 como resultaria de média aritmética. Este comportamento matemático alinha-se à lógica prática da gestão de riscos, onde fragilidades críticas não devem ser mascaradas por desempenhos isoladamente positivos.

---

## **Etapa 5: Análise de Sensibilidade e Robustez**

A robustez do IGRO foi avaliada através de três testes complementares. **Teste 1 (Variação de pesos):** recalcular o índice em três cenários alternativos de ponderação (uniforme, qualidade prioritária, tempestividade prioritária) e verificar se o ranking dos 51 órgãos se mantém estável, usando correlação de postos de Spearman. **Teste 2 (Método alternativo):** comparar o IGRO calculado por média geométrica com versão calculada por média aritmética, identificando órgãos que mudam de faixa de risco (Verde/Amarelo/Laranja/Vermelho). **Teste 3 (Bootstrap):** executar 1.000 iterações com perturbação aleatória de ±10% nos pesos originais, calcular intervalos de confiança de 90% para cada órgão e avaliar sobreposição significativa no ranking. O índice é considerado robusto quando a classificação de semaforização se mantém a mesma em pelo menos três dos quatro cenários testados.

---

## **Conformidade Metodológica**

O IGRO atende integralmente às cinco etapas recomendadas pelo Handbook OCDE/JRC (2008): (1) seleção de indicadores validada por literatura e participação; (2) normalização transparente e conectada a metas institucionais; (3) ponderação estruturada com justificativa teórica; (4) agregação híbrida que reflete lógica de risco; (5) análise de sensibilidade comprovando estabilidade dos resultados. Esta conformidade garante que o IGRO opera com padrão de qualidade metodológica internacional para indicadores compostos no setor público.

---

**Comprimento:** ~650 palavras  
**Adequado para:** Seção 2.2 (Referencial Teórico) ou Seção 3 (Metodologia)  
**Vantagem:** Flui naturalmente no texto, sem quebra de leitura típica de tabelas
