# Normalização: Métodos e Técnicas

## Por que normalizar?

Os indicadores de uma Matriz de Gestão de Riscos possuem unidades e escalas completamente diferentes: percentuais (0,40%), dias (6,3), notas (7,3) e quantidades absolutas (14.837). Além disso, alguns indicadores são "quanto maior, melhor" (ex: Resolutividade) e outros "quanto menor, melhor" (ex: Prazo Médio de Resposta).

A normalização transforma todos os indicadores em uma escala comum e comparável, sendo um passo obrigatório antes da agregação.

---

## Métodos Principais

### 1. Min-Max (Rescalonamento)

Transforma os valores para o intervalo [0, 1] (ou [0, 100]):

```
X_normalizado = (X - X_min) / (X_max - X_min)
```

**Exemplo prático:**
Se o Prazo Médio de Resposta varia entre 3 dias (melhor) e 15 dias (pior):
- Valor atual: 6,3 dias
- Normalizado: (6,3 - 3) / (15 - 3) = 0,275

Para indicadores "quanto menor, melhor", inverte-se:
```
X_normalizado = (X_max - X) / (X_max - X_min)
```
- Prazo 6,3 dias invertido: (15 - 6,3) / (15 - 3) = 0,725 (bom desempenho)

**Vantagens:** Intuitivo, fácil de comunicar, mantém proporcionalidade
**Desvantagens:** Sensível a outliers, requer definição de limites (min/max)

---

### 2. Z-Score (Padronização)

Transforma os valores com base na média e desvio padrão:

```
Z = (X - média) / desvio_padrão
```

**Exemplo prático:**
Se a Resolutividade tem média 50% e desvio padrão 10%:
- Valor atual: 56%
- Z = (56 - 50) / 10 = 0,6 (0,6 desvios acima da média)

**Vantagens:** Não afetado por outliers extremos, não requer definição de limites
**Desvantagens:** Valores negativos podem confundir, não tem limites definidos, pressupõe distribuição aproximadamente normal

---

### 3. Distância à Meta (Distance to Target)

Normaliza com base na meta estabelecida:

```
X_normalizado = X / Meta  (para "quanto maior, melhor")
X_normalizado = Meta / X  (para "quanto menor, melhor")
```

**Exemplo prático (usando dados da Matriz):**
- Resolutividade: 56% / Meta 50% = 1,12 (112% da meta — atingida)
- Prazo Médio: Meta 10,0 / Valor 6,3 = 1,59 (63% melhor que a meta)
- % Insatisfatórias: Meta 2,5% / Valor 1,52% = 1,64 (61% da meta — atingida)

**Vantagens:** Diretamente ligada à gestão por metas, intuitiva para gestores
**Desvantagens:** Requer metas bem definidas para cada indicador

---

### 4. Ranking (Ordenação)

Substitui os valores pela posição relativa (1º, 2º, 3º...):

**Vantagens:** Não afetado por outliers, simples
**Desvantagens:** Perde informação sobre magnitude das diferenças

---

### 5. Percentual do Valor Máximo Teórico

Normaliza em relação ao máximo teórico possível:

```
X_normalizado = X / X_máximo_teórico
```

**Exemplo:**
- Nota de Recomendação: 7,3 / 10,0 = 0,73

---

## Recomendação para a Matriz de Gestão de Riscos

Para o contexto de gestão pública com metas estabelecidas, a abordagem mais adequada é uma combinação de:

1. **Distância à Meta** — quando há metas claras definidas (maioria dos indicadores da Matriz já possui metas)
2. **Min-Max** — para indicadores sem meta definida, usando limites "goalposts" definidos por especialistas

Essa abordagem é recomendada pelo Handbook OCDE/JRC para indicadores de políticas públicas, pois captura mudanças absolutas ao longo do tempo em relação a objetivos concretos.

### Tratamento da Direção

É fundamental inverter indicadores negativos (onde "menos é melhor") antes da agregação:

| Indicador | Direção | Tratamento |
|-----------|---------|------------|
| % Manifestações > 30 dias | Menor = melhor | Inverter |
| Prazo Médio de Resposta | Menor = melhor | Inverter |
| Resolutividade | Maior = melhor | Manter |
| % Respostas Insatisfatórias | Menor = melhor | Inverter |
| Nota de Recomendação | Maior = melhor | Manter |

---

## Fontes

- [COINr Documentation — Normalisation](https://bluefoxr.github.io/COINrDoc/normalisation.html)
- [Codecademy — Min-Max and Z-Score Normalization](https://www.codecademy.com/article/min-max-zscore-normalization)
- [OECD Handbook on Constructing Composite Indicators](https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf)
- [Developing Composite Indicators — Effect of Normalization (MDPI)](https://www.mdpi.com/2079-9276/6/4/66)
