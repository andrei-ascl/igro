# Ponderação: Métodos para Atribuição de Pesos

## O Problema da Ponderação

Segundo o JRC da Comissão Europeia, "não existe metodologia universalmente aceita para ponderar indicadores individuais antes de agregá-los." A escolha de pesos pode ter efeito significativo no ranking final — pesquisas mostram que, por exemplo, no Technology Achievement Index, a mudança de pesos afetou muitas unidades avaliadas, especialmente aquelas em posições intermediárias.

A ponderação reflete a importância relativa de cada indicador na composição do índice. Se todos os indicadores tiverem o mesmo peso, assume-se que todos são igualmente importantes.

---

## Métodos de Ponderação

### 1. Pesos Iguais (Equal Weighting)

Todos os indicadores recebem o mesmo peso: `w_i = 1/n`

**Quando usar:** Quando não há justificativa teórica ou empírica para diferenciar importâncias, ou quando a transparência é prioritária.

**Vantagens:** Simples, transparente, fácil de comunicar
**Desvantagens:** Ignora diferenças de relevância entre indicadores, pode não refletir prioridades da gestão

---

### 2. Análise de Componentes Principais (PCA)

Utiliza técnicas estatísticas para derivar pesos a partir da estrutura de variância dos dados:

- Realiza-se a PCA sobre os indicadores normalizados
- Os loadings (cargas fatoriais) do primeiro componente principal fornecem os pesos
- O primeiro componente explica a maior proporção da variância total

**Quando usar:** Quando se tem dados históricos suficientes e se deseja pesos baseados em dados (data-driven).

**Vantagens:** Objetivos, baseados em dados, reduzem subjetividade
**Desvantagens:** Requerem séries de dados, podem não refletir prioridades políticas, difíceis de comunicar para não-técnicos

---

### 3. Processo Analítico Hierárquico (AHP)

Desenvolvido por Thomas Saaty (1970s), o AHP utiliza comparações par-a-par entre critérios feitas por especialistas:

**Etapas:**
1. Definir hierarquia (objetivo → critérios → indicadores)
2. Especialistas comparam pares de indicadores: "O Prazo Médio de Resposta é mais importante que a Resolutividade para medir o risco?"
3. Usa-se escala de 1 a 9 (1 = igual importância, 9 = extremamente mais importante)
4. Calcula-se a matriz de comparação e extrai-se o vetor de pesos
5. Verifica-se a consistência das respostas (Razão de Consistência < 0,10)

**Exemplo de Matriz de Comparação para a Matriz de Riscos:**

|  | % > 30 dias | Prazo Médio | Resolutiv. | % Insatisf. | Nota Recom. |
|--|------------|-------------|------------|-------------|-------------|
| % > 30 dias | 1 | 1/3 | 1/5 | 1/3 | 1/5 |
| Prazo Médio | 3 | 1 | 1/3 | 1 | 1/3 |
| Resolutiv. | 5 | 3 | 1 | 3 | 1 |
| % Insatisf. | 3 | 1 | 1/3 | 1 | 1/3 |
| Nota Recom. | 5 | 3 | 1 | 3 | 1 |

(Exemplo hipotético — os valores reais devem ser definidos por especialistas da ouvidoria)

**Quando usar:** Quando há especialistas disponíveis e se deseja capturar prioridades institucionais.

**Vantagens:** Estruturado, incorpora conhecimento de especialistas, amplamente aceito
**Desvantagens:** Subjetivo, depende de especialistas, pode ser inconsistente

---

### 4. Alocação Orçamentária (Budget Allocation)

Especialistas distribuem um "orçamento" fixo (ex: 100 pontos) entre os indicadores:

**Exemplo:**
- Resolutividade: 30 pontos
- Nota de Recomendação: 25 pontos
- % Insatisfatórias: 20 pontos
- Prazo Médio: 15 pontos
- % > 30 dias: 10 pontos

**Quando usar:** Quando se deseja participação de stakeholders de forma intuitiva.

**Vantagens:** Muito intuitivo, fácil de implementar com stakeholders
**Desvantagens:** Pode ser impreciso, tende a pesos arredondados

---

### 5. Ponderação por Entropia

Baseia-se na teoria da informação — indicadores com maior variabilidade (mais "informativos") recebem pesos maiores:

```
E_i = -k × Σ(p_ij × ln(p_ij))   (Entropia de Shannon)
w_i = (1 - E_i) / Σ(1 - E_j)     (Peso do indicador i)
```

**Quando usar:** Quando se quer maximizar o poder discriminante do índice.

**Vantagens:** Objetivo, data-driven, maximiza discriminação
**Desvantagens:** Pode dar peso alto a indicadores irrelevantes com alta variância

---

### 6. Benefit of the Doubt (BOD / DEA)

Baseado em Data Envelopment Analysis, atribui os pesos mais favoráveis para cada unidade avaliada:

**Quando usar:** Quando se quer flexibilidade e não penalizar unidades por escolhas de pesos.

**Vantagens:** Cada unidade é avaliada no seu melhor cenário possível
**Desvantagens:** Diferentes unidades podem ter pesos diferentes, dificultando comparação

---

## Recomendação para a Matriz de Gestão de Riscos

Para o contexto de ouvidoria e gestão pública, recomenda-se uma abordagem em duas camadas:

1. **AHP ou Alocação Orçamentária** para capturar as prioridades institucionais, envolvendo gestores da ouvidoria e especialistas em gestão de riscos
2. **Análise de Sensibilidade** para verificar se diferentes conjuntos de pesos alteram significativamente os resultados

Uma estrutura hierárquica natural dos pesos poderia ser:

```
Índice de Gestão de Riscos (100%)
├── Risco 0044 - Tempestividade (40%)
│   ├── % Manifestações > 30 dias (15%)
│   └── Prazo Médio de Resposta (25%)
└── Risco 0046 - Qualidade (60%)
    ├── Resolutividade (25%)
    ├── % Insatisfatórias (15%)
    └── Nota de Recomendação (20%)
```

(Percentuais ilustrativos — devem ser validados por especialistas)

---

## Fontes

- [Greco et al. (2019) — On the Methodological Framework of Composite Indices](https://link.springer.com/article/10.1007/s11205-017-1832-9)
- [AHP — Analytic Hierarchy Process Overview](https://www.1000minds.com/decision-making/analytic-hierarchy-process-ahp)
- [COINr Documentation — Weighting](https://bluefoxr.github.io/COINrDoc/weighting-1.html)
- [SAW-Max-Entropy Hybrid Weighting (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10887757/)
- [OECD Handbook on Constructing Composite Indicators](https://www.oecd.org/en/publications/handbook-on-constructing-composite-indicators-methodology-and-user-guide_9789264043466-en.html)
