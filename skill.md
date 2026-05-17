

### 1. Visão Geral

Este domínio de conhecimento concentra-se na **gestão estratégica de riscos operacionais em ouvidorias públicas**, especificamente através da implementação do **Índice de Gestão de Riscos de Ouvidorias (IGRO)**. O objetivo desta _skill_ é permitir que uma IA monitore, avalie e sinalize falhas na **tempestividade** e na **qualidade** do atendimento ao cidadão, transformando dados brutos em inteligência gerencial. A _skill_ resolve problemas de ineficiência administrativa, descumprimento de prazos legais (Lei 13.460/2017) e baixa resolutividade nas demandas sociais.

### 2. Princípios e Diretrizes

- **Fundamentação Metodológica:** Seguir rigorosamente a **ISO 31000:2018** para gestão de riscos e o manual da **OCDE/JRC** para a construção de indicadores compostos.
- **Complementaridade:** Os eixos de Tempestividade (IT) e Qualidade (IQ) são **não-substituíveis**; uma falha crítica em um anula a excelência do outro através da média geométrica.
- **Justiça Processual:** A rapidez e a eficácia na resposta são pilares da confiança institucional.
- **Evitar a Lei de Goodhart:** Não focar apenas na métrica de forma isolada para evitar distorções operacionais (_gaming_); o índice deve ser auditável e baseado em metas objetivas.

### 3. Definições e Conceitos-Chave

- **IGRO:** Índice sintético que agrega 5 Indicadores-Chave de Risco (KRIs).
- **KRI (Key Risk Indicator):** Métrica que sinaliza a materialização potencial de um risco.
- **Tempestividade (Risco 0044):** Risco de exposição à falha no cumprimento de prazos legais (30 dias).
- **Qualidade (Risco 0046):** Risco de inefetividade, baixa resolutividade e insatisfação cidadã.
- **SGOe:** Sistema de Gestão de Ouvidoria utilizado como fonte única de dados em Goiás.

### 4. Regras Operacionais

#### Fórmulas de Normalização (Intervalo)

A normalização utiliza a **Distância à Meta com Goalposts**:

- **TMR (Tempo Médio):** $max(0, 1 - (TMR - 8) / 12)$ | Meta: 8 dias; Piso: 20 dias.
- **%RDP (Prazo):** $max(0, (%RDP - 80) / 20)$ | Meta: 100%; Piso: 80%.
- **TR (Resolutividade):** $max(0, (TR - 50) / 50)$ | Meta: 80%; Piso: 50%.
- **%RI (Insatisfação):** $max(0, 1 - (%RI - 2) / 3)$ | Meta: 2%; Piso: 5%.
- **Nota de Recomendação:** $max(0, (NR - 6,0) / 2,5)$ | Meta: 8,5; Piso: 6,0.

#### Agregação

1. **Sub-índice de Tempestividade (IT):** $0,6 \times TMR_{norm} + 0,4 \times %RDP_{norm}$.
2. **Sub-índice de Qualidade (IQ):** $0,4 \times TR_{norm} + 0,3 \times %RI_{norm} + 0,3 \times NR_{norm}$.
3. **IGRO Final:** $\sqrt{IT \times IQ}$ (Média Geométrica).

#### Critérios de Interpretação

- **0,90 a 1,00:** Risco Controlado (Gestão Eficaz).
- **0,70 a 0,89:** Risco em Atenção (Gestão Adequada).
- **0,50 a 0,69:** Risco Elevado (Gestão Frágil).
- **0,00 a 0,49:** Risco Materializado (Gestão Crítica).

### 5. Fluxos de Trabalho

1. **Extração:** Coletar dados mensais/quadrimestrais das manifestações finalizadas no SGOe.
2. **Filtragem de Amostra:** Validar se o órgão possui $n \geq 30$ respondentes ou taxa de cobertura $\geq 5%$ das manifestações identificadas.
3. **Processamento:** Aplicar fórmulas de normalização para os 5 KRIs.
4. **Cálculo:** Gerar os sub-índices IT e IQ e agregar no IGRO final.
5. **Sinalização:** Identificar órgãos em faixas críticas para intervenção da alta gestão.

### 6. Estruturas de Resposta

- **Relatórios de Risco:** Devem apresentar o IGRO, os sub-índices (IT/IQ) e destacar qual KRI está penalizando o resultado (ex: TR baixo impactando o IQ).
- **Padrão de Escrita:** Utilizar terminologia técnica (ex: "exposição ao risco", "materialização", "consonância regulatória").
- **Sinalização Visual:** Alertas de "Amostra Insuficiente" para órgãos com dados estatísticos frágeis.

### 7. Boas Práticas

- **Exclusão de Anônimos:** Para o cálculo da cobertura da pesquisa de satisfação, excluir manifestações anônimas do denominador, pois estas não geram pesquisa.
- **Fator de Correção (FPC):** Em órgãos pequenos, considerar a correção para população finita para evitar penalizações injustas por amostras numericamente baixas, mas proporcionalmente altas.
- **Ciclos Quadrimestrais:** Sincronizar a avaliação com o planejamento institucional para permitir melhoria contínua.

### 8. Casos de Uso

- **Diagnóstico de Gargalos:** Identificar se um órgão responde rápido (IT alto), mas sem resolver o problema (IQ baixo), o que reduz o IGRO final.
- **Benchmarking Estadual:** Comparar o desempenho de 51 órgãos estaduais de forma padronizada e auditável.
- **Prevenção de Crises:** Detectar aumento no percentual de respostas insatisfatórias (%RI) antes que se torne uma crise reputacional.

### 9. Limitações e Cuidados

- **Vieses de Registro:** O índice depende da qualidade do preenchimento manual das áreas técnicas no SGOe.
- **Dimensão Cidadã:** O IGRO foca nas dimensões funcional e gerencial; não captura participação social ou engajamento democrático.
- **NPS Amostral:** Resultados de recomendação baseados em amostras pequenas possuem erro amostral elevado e devem ser sinalizados com _flags_ de alerta.

### 10. Checklist Operacional

- [ ] Verificou se o prazo legal de 30 dias foi respeitado na base de dados?
- [ ] O denominador para a taxa de cobertura exclui as manifestações anônimas?
- [ ] A média utilizada para a agregação final foi a geométrica?
- [ ] O órgão avaliado possui o número mínimo de 30 respondentes para validade dos KRIs de pesquisa?
- [ ] A pontuação normalizada está dentro do intervalo de 0,00 a 1,00?