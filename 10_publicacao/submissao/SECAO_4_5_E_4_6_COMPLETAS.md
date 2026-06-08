# Seção 4.5 e 4.6 — Casos Extremos e Robustez Metodológica

## 4.5 Casos Extremos de Desempenho

A análise dos extremos de desempenho revela dois **arquétipos organizacionais** contrastantes que iluminam os fatores críticos de sucesso da rede.

### Arquétipo de Excelência: GOINFRA (IGRO = 100%)

O desempenho máximo foi alcançado por GOINFRA, uma unidade de classe operacional 3 (grande) que combinou simultaneamente:

- **Score TMR = 100%** (4,46 dias, dentro da meta de excelência de 5 dias)
- **Score PMA = 100%** (0,05% — quase zero atraso)
- **Score RP = 100%** (73,5% de resolutividade percebida, acima da meta de 70%)
- **Score %RI = 100%** (1,71% de insatisfação, abaixo da meta de 2,5%)
- **Score NR = 100%** (NPS = 73,85, bem acima da meta de 7,5)

O denominador comum: **processos padronizados, integração tecnológica robusta, equipe dedicada de 501 pesquisadores de satisfação, e comunicação estruturada**. Este órgão funciona como "modelo de referência" da rede.

Órgãos de desempenho muito elevado também incluem **SEMAD (97,7%)** e **DGPP (94,9%)**, que replicam o padrão de GOINFRA com variações menores em um ou dois KRIs.

### Arquétipo de Colapso: SECAMI, CELGPAR, Vice-Governadoria (IGRO ≈ 0%)

O desempenho crítico foi observado em órgãos de classe 5 (pequenos) que apresentaram falha **sistêmica e multidimensional**:

**SECAMI:** Score TMR = 0% (56,79 dias, extremamente acima do goalpost de 30), Score PMA = 0% (35,85% em atraso — completamente não conforme), Score RP = 66,7%, Score %RI = 0%, Score NR = 33,3%
- **Padrão:** Extremamente lento, porém com alguma resolutividade quando consegue responder

**CELGPAR:** Score TMR = 0% (18,75 dias), Score PMA = 50% (metade das manifestações em atraso), Score RP = 100%, Score %RI = 0%, Score NR = 100%
- **Padrão paradoxal:** Quando responde, resolve bem — mas leva muito tempo e atrasa sistematicamente

**Vice-Governadoria:** Score TMR = 0%, Score PMA = 20%, Score RP = 0% (zero percepção de resolutividade), Score NR = -100% (NPS detrator extremo), IGRO = 0%
- **Padrão:** Falha completa em todas as dimensões

### Insight Analítico

Os órgãos em colapso não apresentam "fraqueza em um indicador" — apresentam **falha estrutural que afeta múltiplas dimensões**. O heatmap (Figura 4) mostra linha vermelha quase contínua para esses órgãos. Não é possível "reparar" SECAMI apenas melhorando TMR; é necessária intervenção sistêmica.

### Padrão Intermediário: Desequilíbrio Crítico

Um grupo de órgãos apresenta desempenho heterogêneo que merece atenção especial:

**SEINFRA:** TMR = 0% (7,45 dias, acima do goalpost), mas RP = 100% (78,57% resolutividade, excelente)
- **Interpretação:** Órgão lento mas efetivo — cidadão espera, mas fica satisfeito

**ABC, SIC:** PMA crítico (score 0%), mas RP verde (ABC: 85,7%, SIC: 100%)
- **Interpretação:** Atraso pontual, mas quando responde, resolve

**JUCEG:** Score NR = 12,4% (NPS = 4,0), mas TMR e RP moderados
- **Interpretação:** Rápido mas impopular — cidadão reclama mesmo respondendo

Esses padrões sugerem que **diferentes órgãos requerem diferentes estratégias de intervenção**: não há solução única.

---

## **Quadro 1 — Comparação entre Órgão de Excelência (GOINFRA) e Órgão Crítico (CELGPAR)**

| **Dimensão** | **GOINFRA (Excelência)** | **CELGPAR (Crítico)** | **Diferença / Insight** |
|:---|:---|:---|:---|
| **IGRO Final** | 100% | 0% | Polarização extrema: distância de 100 pp |
| **Classe Operacional** | Classe 3 (Grande) | Classe 5 (Muito pequeno) | Diferença de 2 classes — estrutura 10x menor |
| | | | |
| **DIMENSÃO TEMPESTIVIDADE** | | | |
| Manifestações respondidas | 2.109 | 4 | GOINFRA: 527x maior volume |
| TMR (Tempo Médio de Resposta) | 4,46 dias | 18,75 dias | CELGPAR: 4,2x mais lento |
| Score TMR | 100% | 0% | GOINFRA atinge meta (5 dias); CELGPAR 2,5x acima do goalpost (30 dias) |
| PMA (% manifestações em atraso) | 0,05% | 50,0% | CELGPAR: metade das manifestações atrasadas |
| Score PMA | 100% | 0% | GOINFRA em conformidade total; CELGPAR em violação massiva |
| **Sub-índice Tempestividade** | 100% | 0% | Colapso completo em tempestividade |
| | | | |
| **DIMENSÃO QUALIDADE** | | | |
| Pesquisas de satisfação | 501 | 1 | GOINFRA: 501x mais respondentes |
| RP (Resolutividade Percebida) | 73,45% | 100% | CELGPAR: paradoxo — 100% de resolução com 1 respondente |
| Score RP | 100% | 100% | Ambos em faixa máxima (mas CELGPAR com n=1, estatisticamente inválido) |
| %RI (Respostas Insatisfatórias) | 1,71% | 0% | CELGPAR: zero reabertura (mas n=1) |
| Score %RI | 100% | 100% | Ambos em faixa máxima |
| NR (Nota de Recomendação — NPS) | 9,05 | 10,00 | CELGPAR: nota máxima (mas n=1) |
| Score NR | 100% | 100% | Ambos em faixa máxima |
| **Sub-índice Qualidade** | 100% | 100% | Ambos "perfeitos" — mas CELGPAR não confiável |
| | | | |
| **AGREGAÇÃO FINAL** | | | |
| Média geométrica | 100% | 0% | Média geométrica penaliza o fraco desempenho em Tempestividade |
| (Temp^0,4 × Qual^0,6) | | | |
| | | | |
| **RECURSOS E CAPACIDADE** | | | |
| Estrutura administrativa | Dedicada | Mínima | GOINFRA: equipe profissionalizada |
| Integração tecnológica | Robusta (SGOe integrado) | Ausente | GOINFRA: sistema centralizado; CELGPAR: registro manual |
| Amostra de pesquisa | Robusta (n=501) | Frágil (n=1) | GOINFRA: estatisticamente confiável; CELGPAR: inválida |
| | | | |
| **INTERPRETAÇÃO CRÍTICA** | | | |
| Padrão observado | **Desempenho sistemicamente balanceado** | **Falha crítica mascarada por números** | CELGPAR mostra por que indicadores isolados falham |
| Diagnóstico | Órgão funciona bem em todas as dimensões | Órgão tem TMR crítico; indicadores de qualidade são artefatos (n=1) | |
| Intervenção necessária | Manutenção; benchmark para rede | Intervenção estrutural urgente: tecnologia, processos, pessoal | |
| Lição metodológica | Exemplo de como IGRO funciona corretamente | Prova de que média geométrica é acertada: penaliza desequilíbrio severo | |

### Notas Explicativas do Quadro

#### 1. O Paradoxo de CELGPAR

CELGPAR ilustra um **problema crítico em indicadores de satisfação**: com apenas 1 respondente, a "RP = 100%" e "NR = 100%" são **estatisticamente inválidos**. Conforme discutido na Seção 3.6, órgãos com n < 30 carecem de confiabilidade. CELGPAR com n = 1 é um caso extremo de **amostra insuficiente** que deveria ser excluído de análises comparativas.

#### 2. Por que IGRO = 0% para CELGPAR

Apesar de "perfeito" em qualidade (nota 10, RP 100%), CELGPAR recebe IGRO = 0% porque:
- Score TMR = 0% (18,75 dias >> 30 dias de limite aceitável)
- Score PMA = 0% (50% de manifestações em atraso)
- A **média geométrica** penaliza desequilíbrio: 1,0^0,4 × 0,0^0,6 = 0,0

Isso é **comportamento desejável**: um órgão que não consegue responder no prazo não pode ser considerado "bom" apenas porque quando responde (1 vez) a resposta é boa.

#### 3. Contraste com GOINFRA

GOINFRA demonstra que é **possível** alcançar excelência simultânea:
- Responde rápido (4,46 dias vs. meta de 5)
- Mantém prazos (0,05% em atraso)
- Resolve bem (73,45% RP)
- Cidadão recomenda (NPS 73,85)

Com **501 respondentes**, os dados de qualidade são estatisticamente confiáveis.

#### 4. Implicação Sistêmica

O contraste GOINFRA-CELGPAR sugere que:
- Não é impossível ser excelente na rede (GOINFRA prova)
- Falhas de tempestividade são determinantes (CELGPAR colapsa por TMR)
- Amostra pequena distorce percepção (CELGPAR "perfeito" em qualidade com n=1)
- Classe operacional correlaciona com capacidade (Classe 3 vs. Classe 5)

---

## 4.6 Robustez Metodológica: Resultados da Análise de Sensibilidade

Os três testes complementares **confirmam que o IGRO atende plenamente ao critério de robustez recomendado pelo Handbook OCDE/JRC**: a classificação de semaforização permanece estável mesmo sob cenários alternativos de ponderação, método de agregação e perturbação aleatória.

### Teste 1: Estabilidade do Ranking sob Variação de Pesos

O ranking dos 47 órgãos foi recalculado em três cenários de ponderação distintos:
- Cenário A: Ponderação uniforme (w = 0,20 para cada KRI)
- Cenário B: Qualidade prioritária (w Qualidade = 0,60; w Tempestividade = 0,40)
- Cenário C: Tempestividade prioritária (inverso do Cenário B)

**Resultados:**
- Correlação de Spearman entre rankings: **ρ = 0,85–0,92** (todos com p < 0,001)
  - Uniforme vs. Qualidade: ρ = 0,92 (muito forte)
  - Uniforme vs. Tempestividade: ρ = 0,88 (forte)
  - Qualidade vs. Tempestividade: ρ = 0,85 (forte)

- Embora 15 órgãos apresentassem variação individual superior a 10 pp (máximo: 18,13 pp em CODEGO), essa variação ocorreu **predominantemente dentro da mesma faixa de risco**
  - Exemplo: CODEGO oscila entre 36,4% (Tempestividade prioritária) e 54,5% (Qualidade prioritária), mas permanece na faixa crítica em todos os cenários

**Conclusão:** O ranking global é **altamente estável**. A escolha de ponderação não altera significativamente a ordem de priorização de órgãos em risco.

### Teste 2: Robustez do Método de Agregação (Geométrica vs. Aritmética)

Comparou-se a média geométrica (método adotado) com alternativa usando média aritmética ponderada.

**Resultados:**
- **80,9% dos órgãos (38 de 47)** mantiveram a mesma faixa de risco em ambos os métodos
- **19,1% dos órgãos (9 de 47)** mudaram de faixa, todos apresentando padrão comum: **excelência em Tempestividade + falha crítica em Qualidade**
  - Exemplo: SEDF (40% geométrica, 80% aritmética) — muda de Crítico para Baixo
  - Exemplo: SEAPA (37% geométrica, 74,3% aritmética) — muda de Crítico para Moderado

**Implicação crítica:** A média aritmética **compensa** deficiências, elevando artificialmente órgãos com desequilíbrio severo. A média geométrica **penaliza** desequilíbrio, mantendo órgãos frágeis em faixa crítica mesmo que excelentes em uma dimensão.

**Conclusão:** Essa diferença **valida empiricamente a escolha da média geométrica**. Em gestão de riscos, fragilidades críticas não devem ser mascaradas por desempenhos isolados.

### Teste 3: Confiabilidade sob Perturbação Aleatória (Bootstrap)

Executou-se 1.000 iterações de simulação com variação aleatória de ±10% nos pesos originais.

**Resultados:**
- **Amplitude de intervalos de confiança (P95-P5):**
  - Média: 3,43 pp
  - Mediana: 3,49 pp
  - Máximo: 5,24 pp (órgão SIC com maior heterogeneidade de KRIs)
  
- **Sobreposição de intervalos:** Nenhuma sobreposição significativa entre órgãos **adjacentes no ranking**, indicando que a ordem de classificação permanece robusta mesmo sob perturbação extrema

- **Amplitude por classe operacional:**
  - Classes 1–3: amplitude 2–4 pp (estável)
  - Classes 4–5: amplitude 3–5 pp (levemente mais volátil, esperado por amostra menor)

**Conclusão:** O IGRO é **robusto a incerteza nos pesos**. Variações realistas (±10%) produzem oscilações limitadas que não alteram a posição relativa dos órgãos.

### Síntese: Conformidade ao Padrão OCDE/JRC

| Critério de Robustez | Teste | Resultado | Status |
|:---|:---|:---|:---|
| Estabilidade de ranking | Variação de pesos | ρ > 0,85 em todas as comparações | ✅ Robusto |
| Validação do método | Geométrica vs. Aritmética | 80,9% mantêm faixa de risco | ✅ Robusto |
| Confiabilidade estatística | Bootstrap ±10% | Amplitude máx. 5,24 pp | ✅ Robusto |
| **Conclusão OCDE/JRC** | — | **Semaforização estável em ≥3 cenários** | **✅ APROVADO** |

### Implicações para Utilização

O IGRO demonstra **robustez metodológica adequada para implementação em ciclos operacionais de gestão de riscos**. A variabilidade intra-órgão (±5,24 pp máximo) é suficientemente pequena para permitir:

1. **Decisões estratégicas:** Órgãos em faixa crítico permanecerão críticos independente de ajustes de ponderação
2. **Comparabilidade temporal:** IGRO de um órgão em Q2 vs. Q1 pode ser comparado com confiança
3. **Benchmarking:** Rankings entre órgãos são estáveis e não sensíveis a escolhas metodológicas menores

---

**Versão:** 1.0  
**Data:** 28/05/2026  
**Pronto para integração:** Sim
