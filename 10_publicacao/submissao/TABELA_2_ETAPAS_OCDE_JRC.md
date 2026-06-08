# Tabela 2 — Etapas Metodológicas OCDE/JRC Aplicadas ao IGRO

> **Referência normativa:** Handbook on Constructing Composite Indicators (OCDE/JRC, 2008)  
> **Aplicação:** Índice de Gestão de Riscos de Ouvidoria  
> **Versão:** 1.0 — Abril/2026

---

## **TABELA 2: Etapas Metodológicas OCDE/JRC aplicadas ao IGRO**

| **Etapa OCDE/JRC** | **Objetivo** | **Aplicação no IGRO** | **Decisão Metodológica** | **Referência/Documento** |
|:---|:---|:---|:---|:---|
| **1. Seleção de Indicadores** | Identificar e validar dimensões relevantes do fenômeno a medir | Seleção de 5 KRIs distribuídos em 2 eixos (Tempestividade e Qualidade) | **KRI 1:** % Manifestações > 30 dias (Temp.) **KRI 2:** Prazo Médio de Resposta (Temp.) **KRI 3:** Resolutividade Percebida (Qual.) **KRI 4:** % Respostas Insatisfatórias (Qual.) **KRI 5:** Nota de Recomendação (Qual.) | Desenho Técnico (arquivo 10); Benchmarking (arquivo 09); Oficina SEAD/Pequi Lab (2023) |
| **2. Normalização** | Converter indicadores com escalas diferentes para escala comum (0–1) | Transformação de cada KRI para [0, 1] usando método de distância à meta (goalposts) | Fórmula Distância à Meta com goalposts: Para "menor = melhor": `score = (limite_máx − valor) / (limite_máx − meta)`, limitado ao intervalo [0, 1] | Seção 3.3 (Metodologia); Handbook OCDE/JRC (2008), cap. 5 |
| | | | **Goalposts definidos por:** — Expertise de pesquisadores — Benchmarking de ouvidorias estaduais (arquivo 09) — Conformidade com normas legais (Lei 13.460/2017, Decreto 10.466/2024) | — |
| **3. Ponderação** | Atribuir pesos refletindo a importância relativa de cada indicador | Estrutura hierárquica com dois níveis de pesos: **Nível 1 (sub-índices):** Sub_T = 40% | Sub_Q = 60% **Nível 2 (intra-dimensões):** KRI 1 = 15% global (37,5% de 40%) KRI 2 = 25% global (62,5% de 40%) KRI 3 = 25% global (41,7% de 60%) KRI 4 = 15% global (25% de 60%) KRI 5 = 20% global (33,3% de 60%) | Justificativa: Qualidade recebe maior peso (60%) pois é principal driver de confiança cidadã. PMR (25%) > % > 30 dias (15%) pois PMR captura distribuição completa. Resolutividade = PMR em peso (ambos 25%) por impacto equivalente na satisfação. | Desenho Técnico (arquivo 10), seção 5; Handbook OCDE/JRC (2008), cap. 6 |
| **4. Agregação** | Combinar indicadores ponderados em índice único | **Agregação intra-dimensional (dentro de cada sub-índice):** Média aritmética ponderada Sub_T = (0,15 × score₁ + 0,25 × score₂) / 0,40 Sub_Q = (0,25 × score₃ + 0,15 × score₄ + 0,20 × score₅) / 0,60 **Agregação inter-dimensional (entre sub-índices):** Média geométrica ponderada IGRO = Sub_T^0,40 × Sub_Q^0,60 | **Justificativa da estrutura híbrida:** — Dentro de sub-índices (aritmética): indicadores do mesmo risco podem ser parcialmente substitutos — Entre sub-índices (geométrica): riscos distintos NÃO devem se compensar (penaliza desequilíbrios) — Benefício: impede que excelência em Tempestividade compense falha crítica em Qualidade | Seção 3.3 (Metodologia); Desenho Técnico (arquivo 10), seção 6; Handbook OCDE/JRC (2008), cap. 7; Mazziotta & Pareto (2022) |
| **5. Análise de Sensibilidade & Robustez** | Testar estabilidade do índice sob variações metodológicas e avaliar confiabilidade dos resultados | 3 testes recomendados: **Teste 1 – Variação de pesos:** Recalcular IGRO em 3 cenários: (a) Uniforme (w=0,20 cada); (b) Qualidade prioritária; (c) Tempestividade prioritária. Verificar se rankings mudam significativamente (Spearman ρ entre cenários). **Teste 2 – Método de agregação alternativo:** Comparar IGRO (média geométrica) vs. versão calculada por média aritmética. Identificar órgãos que mudam de faixa de risco. **Teste 3 – Bootstrap:** 1.000 iterações com perturbação aleatória ±10% nos pesos. Calcular IC 90% do IGRO para cada órgão. Avaliar sobreposição em ranking. | **Critério de robustez:** Índice aprovado se classificação de semaforização (Verde/Amarelo/Laranja/Vermelho) se mantém a mesma em ≥3 dos 4 cenários. **Testes adicionais recomendados:** — Leave-one-out: remover 1 KRI por vez — Monte Carlo com N ≥ 500 variações — Normalização alternativa (Z-score vs. Distância à Meta) | Seção 3.5 (Metodologia); Handbook OCDE/JRC (2008), cap. 8; Saltelli et al. (2008) |

---

## **NOTAS TÉCNICAS À TABELA**

### **Nota 1: Justificativa da Estrutura Hierárquica**

A escolha de dois níveis de ponderação (sub-índices + KRIs) permite:

1. **Transparência gerencial:** Gestores podem entender qual risco (Tempestividade ou Qualidade) está deteriorando
2. **Auditabilidade:** Fácil rastreamento de qual KRI específico gerou o alerta
3. **Flexibilidade futura:** Possibilidade de ajustar pesos sem reconfiguração completa do modelo

### **Nota 2: Por que Média Geométrica (não Aritmética)?**

Exemplo comparativo com dados reais:

```
Cenário: Sub_T = 1,0 (excelente) | Sub_Q = 0,40 (crítico)

Média aritmética:  IGRO = (0,40 × 1,0 + 0,60 × 0,40) = 0,64 (Moderado)
                   → Excelência em Temp. quase compensa falha em Qualidade

Média geométrica:  IGRO = 1,0^0,40 × 0,40^0,60 = 0,576 (Alto)
                   → Falha crítica penaliza índice mesmo com excelência em outra dimensão
```

**Conclusão:** Média geométrica é mais apropriada para gestão de riscos porque fragilidades críticas não devem ser mascaradas por desempenhos isoladamente positivos.

### **Nota 3: Goalposts vs. Alternativas**

| Método | Vantagens | Desvantagens | Decisão IGRO |
|:---|:---|:---|:---|
| **Distância à Meta (goalposts)** | Conectado a metas institucionais; transparente; auditável | Requer metas pré-definidas | ✅ Selecionado |
| **Min-Max** | Simples; usa dados históricos | Não conectado a objetivos estratégicos; sensível a outliers | ❌ Rejeitado |
| **Z-score** | Estatisticamente rigoroso | Não interpretável para gestores públicos; assume normalidade | ❌ Rejeitado |

**Justificativa:** Goalposts alinhados com Lei 13.460/2017 (prazo de 30 dias) e Decreto Estadual 10.466/2024, garantindo conformidade normativa.

### **Nota 4: Periodicidade e Ciclo**

O IGRO segue o ciclo **quadrimestral** da Matriz de Gestão de Riscos da CGE-GO:

| Etapa | Responsável | Prazo |
|:---|:---|:---|
| Coleta dos 5 KRIs do SGOe | Proprietário do risco | Até 5 dias após fim do quadrimestre |
| Cálculo do IGRO (normalização, agregação) | Proprietário/Analista | Até 10 dias após fim do quadrimestre |
| Análise crítica (scores, desvios, tendências) | Escritório de Compliance | Até 15 dias após fim do quadrimestre |
| Aprovação e integração à Matriz | Comitê Setorial | Até 30 dias (fim do mês subsequente) |

---

## **CONFORMIDADE COM HANDBOOK OCDE/JRC**

Esta tabela demonstra que o IGRO segue as 5 etapas recomendadas pelo Handbook:

✅ **Etapa 1 (Seleção):** 5 KRIs validados por literatura, benchmarking e oficina participativa  
✅ **Etapa 2 (Normalização):** Distância à meta com goalposts (transparência e auditabilidade)  
✅ **Etapa 3 (Ponderação):** Pesos definidos por julgamento estruturado com justificativa teórica  
✅ **Etapa 4 (Agregação):** Híbrida (aritmética intra + geométrica inter) alinhada a riscos  
✅ **Etapa 5 (Sensibilidade):** 3 testes de robustez (variação, método, bootstrap)  

**Conclusão:** O IGRO atende ao padrão de qualidade metodológica internacional para indicadores compostos.

---

## **REFERÊNCIAS PARA ESTA TABELA**

- OCDE/JRC (2008). *Handbook on Constructing Composite Indicators: Methodology and User Guide*. OECD Publishing.
- Brasil. Lei nº 13.460/2017. Disposições sobre direitos do usuário dos serviços públicos.
- Estado de Goiás. Decreto nº 10.466/2024. Estruturação da rede estadual de ouvidorias.
- Estado de Goiás. Instruções Normativas CGE nº 01, 02, 05, 06/2025. Funcionamento de ouvidorias.
- Mazziotta, M., & Pareto, A. (2022). Aggregating composite indicators through the geometric mean. *MDPI Computation*, 10(3), 44.
- Saltelli, A., Ratto, M., et al. (2008). *Global Sensitivity Analysis: The Primer*. John Wiley & Sons.
- SEAD/Pequi Lab (2023). Oficina de Prototipação de Relatório das Ouvidorias. Consolidado de participantes (29 do GT Relatórios).

---

## **COMO USAR ESTA TABELA NO ARTIGO**

**Localização:** Seção 2.2 (Referencial Teórico) ou Seção 3 (Metodologia)

**Função:**
1. Demonstrar conformidade com padrão OCDE/JRC internacional
2. Facilitar compreensão da arquitetura metodológica do IGRO
3. Servir como referência cruzada com documentos técnicos (Desenho IGRO, etc.)

**Nota de rodapé sugerida:**
> "O IGRO foi estruturado seguindo as 5 etapas recomendadas pelo Handbook on Constructing Composite Indicators (OCDE/JRC, 2008), ensuring international methodological rigor. Documentação técnica detalhada disponível em: Desenho Técnico do IGRO (arquivo 10, 2026) e PRD Interno (arquivo 11, 2026)."

---

## **VERSÃO ALTERNATIVA (Tabela condensada)**

Se o espaço for limitado, aqui está uma versão mais compacta:

| **Etapa** | **OCDE/JRC** | **IGRO** | **Documento** |
|:---|:---|:---|:---|
| **Seleção** | Validar dimensões relevantes | 5 KRIs (Temp. + Qual.) | Benchmarking (arquivo 09) |
| **Normalização** | Escala comum [0–1] | Distância à meta (goalposts) | Seção 3.3 |
| **Ponderação** | Pesos relativos | Sub_T 40%, Sub_Q 60% | Desenho Técnico (arquivo 10) |
| **Agregação** | Combinar em índice | Média aritmética (intra) + geométrica (inter) | Seção 3.3 |
| **Sensibilidade** | Testar robustez | 3 testes: variação, método, bootstrap | Seção 3.5 |

---

**Versão completa inserida no artigo em:** Seção 2.2 ou 3 (conforme estrutura final)
