# Agregação: Combinando Indicadores em um Índice Único

## O que é Agregação?

A agregação é a etapa em que os indicadores normalizados e ponderados são combinados em um valor único — o índice composto. A escolha do método de agregação tem implicações profundas sobre o que o índice realmente mede, especialmente em relação à **compensabilidade** (se um bom desempenho em um indicador pode compensar um mau desempenho em outro).

---

## Métodos Principais

### 1. Média Aritmética Ponderada (Linear / Aditiva)

```
IC = Σ(w_i × X_i)
```

onde `w_i` é o peso e `X_i` é o valor normalizado do indicador `i`.

**Exemplo com dados da Matriz (valores normalizados hipotéticos 0-1):**
```
IC = 0,25 × 0,73 + 0,15 × 0,72 + 0,25 × 0,56 + 0,15 × 0,84 + 0,20 × 0,73
IC = 0,183 + 0,108 + 0,140 + 0,126 + 0,146 = 0,703
```

**Compensabilidade:** TOTAL — um indicador excelente compensa totalmente um indicador péssimo. Uma unidade com scores (0, 10) recebe a mesma nota que uma com (5, 5).

**Vantagens:** Simples, intuitivo, amplamente utilizado
**Desvantagens:** Compensabilidade total pode mascarar deficiências graves

---

### 2. Média Geométrica Ponderada (Multiplicativa)

```
IC = Π(X_i ^ w_i)
```

**Exemplo:**
```
IC = 0,73^0,25 × 0,72^0,15 × 0,56^0,25 × 0,84^0,15 × 0,73^0,20
IC = 0,924 × 0,951 × 0,863 × 0,974 × 0,940 = 0,694
```

**Compensabilidade:** PARCIAL — valores baixos penalizam mais o resultado. A média geométrica "enfatiza o equilíbrio, penalizando valores baixos mais fortemente", o que impede que bons valores em alguns indicadores mascarem deficiências em outros.

O IDH adotou a média geométrica em 2010 exatamente por esta razão.

**Vantagens:** Penaliza desequilíbrios, recompensa melhorias em indicadores fracos
**Desvantagens:** Mais complexa, não aceita valores zero, menos intuitiva

---

### 3. Método de Mazziotta-Pareto (MPI)

Agrega usando a média aritmética com um fator de penalização pelo desequilíbrio:

```
MPI = M - σ × cv
```

onde `M` é a média, `σ` é o desvio padrão e `cv` é o coeficiente de variação entre os indicadores.

**Compensabilidade:** NÃO-COMPENSATÓRIA — penaliza fortemente o desequilíbrio.

**Vantagens:** Controle explícito da compensabilidade
**Desvantagens:** Mais complexo, menos conhecido

---

### 4. Agregação Multicritério (PROMETHEE, ELECTRE)

Métodos de outranking que comparam unidades par-a-par em cada indicador:

**Vantagens:** Evita compensabilidade, respeita preferências complexas
**Desvantagens:** Mais complexo, pode não produzir ranking completo

---

## Comparação: Compensabilidade

| Método | Compensabilidade | Indicado para |
|--------|-----------------|---------------|
| Média Aritmética | Total | Quando compensação é aceitável |
| Média Geométrica | Parcial | Quando se quer penalizar desequilíbrios |
| Mazziotta-Pareto | Mínima | Quando se quer exigir desempenho mínimo em todos |
| Multicritério | Nenhuma | Quando não se aceita compensação |

---

## Recomendação para a Matriz de Gestão de Riscos

No contexto de gestão de riscos de ouvidoria, a **compensabilidade total é problemática**: não deveria ser aceitável que um excelente prazo médio de resposta (6,3 dias) compense um percentual alto de respostas insatisfatórias. Um risco não gerido em uma dimensão não deveria ser "compensado" por bom desempenho em outra.

**Recomendação:** Usar **média geométrica ponderada** ou **MPI** para garantir que:
- Melhorias nos indicadores mais fracos tenham maior impacto
- Não haja compensação total entre dimensões de risco diferentes
- O índice incentive desempenho equilibrado

Alternativamente, pode-se adotar uma **estrutura hierárquica**:
1. Agregar indicadores dentro de cada risco (0044 e 0046) usando média aritmética
2. Agregar os sub-índices dos riscos usando média geométrica (sem compensação total entre riscos)

---

## Fontes

- [Aggregating Composite Indicators through the Geometric Mean (MDPI)](https://www.mdpi.com/2079-3197/10/4/64)
- [COINr Documentation — Aggregation](https://bluefoxr.github.io/COINrDoc/aggregation.html)
- [JRC — Step 7: Aggregating Indicators](https://knowledge4policy.ec.europa.eu/composite-indicators/10-step-guide/step-7-aggregating-indicators_en)
- [Greco et al. (2019) — Weighting, Aggregation, and Robustness](https://link.springer.com/article/10.1007/s11205-017-1832-9)
