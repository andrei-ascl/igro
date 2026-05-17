# Desenho Técnico do IGRO — Índice de Gestão de Riscos da Ouvidoria

> Especificação técnica completa. Consolida as decisões metodológicas dos arquivos 01–09.
> Versão 1.0 — Abril/2026

---

## 1. O que é o IGRO

O **IGRO** é um índice composto que agrega os cinco indicadores-chave de risco (KRIs) da Matriz de Gestão de Riscos da Ouvidoria em um único valor numérico, organizado em dois sub-índices correspondentes aos riscos mapeados.

**Propósito:** sinalizar, de forma sintética e auditável, o nível de materialização dos riscos de atendimento — funcionando como painel de alerta para a alta gestão e como complemento quantitativo ao ciclo quadrimestral da Matriz.

**O que o IGRO NÃO é:** não substitui a análise qualitativa das manifestações, as ações de controle (A01xx) ou a avaliação de efetividade dos controles. É um instrumento de sinalização — não de diagnóstico completo.

---

## 2. Estrutura hierárquica

```
IGRO — Índice de Gestão de Riscos da Ouvidoria  [0 – 1]
│
├── Sub-IGRO_T — Tempestividade (Risco 0044)     peso: 40%
│   ├── KRI 1 — % Manifestações > 30 dias        peso: 15%
│   └── KRI 2 — Prazo Médio de Resposta (dias)   peso: 25%
│
└── Sub-IGRO_Q — Qualidade (Risco 0046)          peso: 60%
    ├── KRI 3 — Resolutividade (%)               peso: 25%
    ├── KRI 4 — % Respostas Insatisfatórias       peso: 15%
    └── KRI 5 — Nota de Recomendação (0–10)       peso: 20%
```

**Justificativa da hierarquia:** A decomposição em sub-índices preserva a identidade de cada risco na comunicação com a gestão. A agregação geométrica entre sub-índices impede que bom desempenho em Tempestividade compense mau desempenho em Qualidade — penalizando desequilíbrios entre riscos.

---

## 3. KRIs: definições e metas

| # | KRI | Unidade | Direção | Meta | Fonte da meta |
|---|-----|---------|---------|------|---------------|
| 1 | % Manifestações com mais de 30 dias sem resposta conclusiva | % | Menor = melhor | ≤ 2,0% | Boa prática — ver arquivo 09 |
| 2 | Prazo Médio de Resposta (PMR) | dias corridos | Menor = melhor | ≤ 10,0 dias | Meta institucional da Matriz |
| 3 | Resolutividade | % | Maior = melhor | ≥ 70,0% | Boa prática — ver arquivo 09 |
| 4 | % Respostas Insatisfatórias | % | Menor = melhor | ≤ 2,5% | Meta institucional da Matriz |
| 5 | Nota de Recomendação (NPS simplificado) | escala 0–10 | Maior = melhor | ≥ 7,5 | Boa prática — ver arquivo 09 |

> **Revisão de metas:** As metas devem ser validadas pela equipe gestora e revisadas anualmente. As metas do benchmarking (arquivo 09) são referências de boas práticas — substituir pelas metas institucionais formalizadas na Matriz quando disponíveis.

---

## 4. Normalização: Distância à Meta com Goalposts

### 4.1 Método selecionado

**Distância à Meta (Distance to Target)** com goalposts — recomendado pelo Handbook OCDE/JRC para indicadores de políticas públicas com metas concretas.

Diferença em relação à fórmula simples: além da meta (ponto alvo), define-se um **piso de referência** (valor mínimo aceitável — goalpost inferior) para capturar deteriorações além do esperado. Isso evita o efeito de "índice flat" quando todos os KRIs superam a meta.

### 4.2 Fórmulas

**Para KRIs onde "menor = melhor" (KRI 1, KRI 2, KRI 4):**

```
score_i = (limite_máx_i - valor_i) / (limite_máx_i - meta_i)

Limitado ao intervalo [0, 1]:
  score_i = max(0, min(1, score_i))
```

- `valor_i` = valor observado no quadrimestre
- `meta_i` = meta do KRI (ponto onde score = 1,0)
- `limite_máx_i` = pior valor aceitável (goalpost — ponto onde score = 0,0)

**Para KRIs onde "maior = melhor" (KRI 3, KRI 5):**

```
score_i = (valor_i - limite_mín_i) / (meta_i - limite_mín_i)

Limitado ao intervalo [0, 1]:
  score_i = max(0, min(1, score_i))
```

- `valor_i` = valor observado no quadrimestre
- `meta_i` = meta do KRI (ponto onde score = 1,0)
- `limite_mín_i` = pior valor de referência (goalpost — ponto onde score = 0,0)

> **Por que capturar ao máximo em 1,0?** Superar a meta é desejável, mas não deve compensar déficits em outros KRIs. O índice mede *cumprimento de metas de risco*, não *excelência relativa*.

### 4.3 Goalposts (limites de referência)

| # | KRI | Meta (score = 1,0) | Goalpost (score = 0,0) | Justificativa do goalpost |
|---|-----|--------------------|------------------------|--------------------------|
| 1 | % > 30 dias | 2,0% | 15,0% | Sinal de alerta severo do arquivo 09: > 10% |
| 2 | PMR | 10,0 dias | 30,0 dias | Limite legal: 20 dias úteis ≈ 30 dias corridos |
| 3 | Resolutividade | 70,0% | 30,0% | Abaixo de 30% = falha sistêmica |
| 4 | % Insatisfatórias | 2,5% | 20,0% | > 10% = sinal de alerta severo (arquivo 09) |
| 5 | Nota Recomendação | 7,5 | 4,0 | Abaixo de 6,0 = sinal de alerta (arquivo 09) |

### 4.4 Exemplo de normalização (dados reais da Matriz)

| # | KRI | Valor obs. | Meta | Goalpost | Score |
|---|-----|-----------|------|----------|-------|
| 1 | % > 30 dias | 0,40% | 2,0% | 15,0% | (15 - 0,40) / (15 - 2) = **1,00** |
| 2 | PMR | 6,3 dias | 10,0 | 30,0 | (30 - 6,3) / (30 - 10) = **1,00** |
| 3 | Resolutividade | 56,0% | 70,0% | 30,0% | (56 - 30) / (70 - 30) = **0,65** |
| 4 | % Insatisfatórias | 1,52% | 2,5% | 20,0% | (20 - 1,52) / (20 - 2,5) = **1,00** |
| 5 | Nota Recomendação | 7,3 | 7,5 | 4,0 | (7,3 - 4,0) / (7,5 - 4,0) = **0,943** |

> **Leitura:** KRIs 1, 2 e 4 estão acima da meta (score = 1,0). KRI 3 (Resolutividade) está abaixo da meta: 56% vs. meta de 70% — score de 0,65. KRI 5 (Nota) está próximo da meta: 7,3 vs. 7,5.

---

## 5. Ponderação

### 5.1 Pesos adotados

| Sub-índice | Peso | KRI | Peso local | Peso global |
|-----------|------|-----|-----------|-------------|
| Sub-IGRO_T (Tempestividade) | 40% | KRI 1 — % > 30 dias | 37,5% | **15%** |
| | | KRI 2 — PMR | 62,5% | **25%** |
| Sub-IGRO_Q (Qualidade) | 60% | KRI 3 — Resolutividade | 41,7% | **25%** |
| | | KRI 4 — % Insatisfatórias | 25,0% | **15%** |
| | | KRI 5 — Nota Recomendação | 33,3% | **20%** |

### 5.2 Justificativa da estrutura de pesos

**Por que Qualidade (60%) > Tempestividade (40%)?**
- Resolutividade, satisfação e qualidade da resposta são os principais drivers de confiança do cidadão na ouvidoria (base: GCOuv, Oficina de Prototipação SEAD/Pequi Lab — 2023)
- Atender no prazo sem resolver o problema é pior do que atrasar com qualidade

**Por que PMR (25%) > % > 30 dias (15%)?**
- PMR captura a distribuição de prazo de toda a base; % > 30 dias captura apenas os casos extremos
- PMR é mais sensível a deteriorações graduais; % > 30 dias detecta rupturas pontuais

**Por que Resolutividade (25%) = PMR (25%)?**
- São os dois indicadores com maior poder preditivo de insatisfação do cidadão — confirmado pela Oficina de Prototipação (2023): "Qualidade da resposta / Resolutividade / Prazo" foram os mais mencionados como indicadores de sucesso

### 5.3 Revisão dos pesos

Os pesos devem ser validados pelo GT de Gestão de Riscos. Alternativas metodológicas disponíveis (arquivo 03): AHP, Alocação Orçamentária, PCA com dados históricos. A análise de sensibilidade (seção 8) avalia o impacto de variações.

---

## 6. Agregação

### 6.1 Método selecionado: estrutura híbrida

**Dentro de cada sub-índice:** média aritmética ponderada — indicadores do mesmo risco podem ser parcialmente substitutos.

**Entre sub-índices:** média geométrica ponderada — riscos distintos (Tempestividade e Qualidade) não devem compensar-se mutuamente.

### 6.2 Fórmulas

**Sub-IGRO_T (Tempestividade):**

```
Sub_T = (w₁ × score₁ + w₂ × score₂) / (w₁ + w₂)
      = (0,15 × score₁ + 0,25 × score₂) / 0,40
```

**Sub-IGRO_Q (Qualidade):**

```
Sub_Q = (w₃ × score₃ + w₄ × score₄ + w₅ × score₅) / (w₃ + w₄ + w₅)
      = (0,25 × score₃ + 0,15 × score₄ + 0,20 × score₅) / 0,60
```

**IGRO (índice final):**

```
IGRO = Sub_T^0,40 × Sub_Q^0,60
```

> A média geométrica penaliza desequilíbrios: se Sub_T = 1,0 e Sub_Q = 0,40, o IGRO = 1,0^0,40 × 0,40^0,60 = 0,576 — não há compensação total. O IDH adotou a mesma abordagem em 2010.

### 6.3 Exemplo numérico completo (dados reais da Matriz)

**Scores normalizados:** score₁ = 1,00 · score₂ = 1,00 · score₃ = 0,65 · score₄ = 1,00 · score₅ = 0,943

```
Sub_T = (0,15 × 1,00 + 0,25 × 1,00) / 0,40
      = (0,15 + 0,25) / 0,40 = 0,40 / 0,40 = 1,000

Sub_Q = (0,25 × 0,65 + 0,15 × 1,00 + 0,20 × 0,943) / 0,60
      = (0,163 + 0,150 + 0,189) / 0,60 = 0,502 / 0,60 = 0,836

IGRO = 1,000^0,40 × 0,836^0,60
     = 1,000 × 0,900 = 0,900
```

**Resultado: IGRO = 0,900 → Risco Baixo (Verde)**

**Leitura:** Tempestividade em nível ótimo. Qualidade levemente abaixo do ideal puxada pela Resolutividade (56% vs. meta 70%). O IGRO global de 0,900 reflete bom desempenho, com alerta para Resolutividade.

---

## 7. Semaforização

| Faixa | Classificação | Cor | Ação recomendada |
|-------|--------------|-----|-----------------|
| 0,80 – 1,00 | Risco Baixo | Verde | Monitoramento rotineiro; manter ações preventivas |
| 0,60 – 0,79 | Risco Moderado | Amarelo | Revisão dos controles; plano de ação em até 30 dias |
| 0,40 – 0,59 | Risco Alto | Laranja | Intervenção necessária; acionar gestão setorial |
| 0,00 – 0,39 | Risco Crítico | Vermelho | Ação imediata; escalada ao Comitê Setorial |

A semaforização aplica-se também a cada sub-índice e a cada KRI individualmente — permitindo identificar qual dimensão ou indicador específico está gerando o alerta.

**Semaforização do exemplo:**

| Componente | Valor | Classificação |
|-----------|-------|--------------|
| KRI 3 — Resolutividade | 0,65 | Amarelo |
| KRI 5 — Nota Recomendação | 0,943 | Verde |
| Sub-IGRO_T | 1,000 | Verde |
| Sub-IGRO_Q | 0,836 | Verde |
| **IGRO** | **0,900** | **Verde** |

---

## 8. Análise de robustez — cenários de pesos

Quatro cenários a serem executados no ciclo de validação inicial:

| Cenário | Descrição | Sub_T / Sub_Q |
|---------|-----------|---------------|
| Base | Pesos propostos neste documento | 40% / 60% |
| Equilibrado | Igual peso para os dois riscos | 50% / 50% |
| Tempestividade prioritária | Prazo como risco principal | 60% / 40% |
| Qualidade prioritária | Qualidade como risco principal | 30% / 70% |

**Critério de robustez:** o IGRO é considerado robusto quando a classificação de semaforização (Verde/Amarelo/Laranja/Vermelho) se mantém a mesma em pelo menos 3 dos 4 cenários.

**Testes adicionais recomendados (arquivo 05):**
- Leave-one-out: remover um KRI por vez e verificar estabilidade
- Normalização alternativa: Z-Score vs. Distância à Meta
- Monte Carlo com N ≥ 500 variações aleatórias dos pesos (faixa: ± 5 pp de cada peso)

---

## 9. Ciclo de monitoramento

O IGRO segue o ciclo quadrimestral da Matriz de Gestão de Riscos:

| Etapa | Responsável | Prazo |
|-------|------------|-------|
| Coleta dos 5 KRIs do SGOe | Proprietário do risco | Até 5 dias após fim do quadrimestre |
| Cálculo do IGRO | Proprietário do risco / Analista | Até 10 dias após fim do quadrimestre |
| Análise crítica (scores, semaforização, desvios) | Escritório de Compliance | Até 15 dias após fim do quadrimestre |
| Aprovação e registro na Matriz | Comitê Setorial | Até o fim do mês subsequente |

---

## 10. Tabela de decisões metodológicas

| Decisão | Opção selecionada | Alternativa considerada | Justificativa |
|---------|------------------|------------------------|---------------|
| Normalização | Distância à Meta com goalposts | Min-Max; Z-score | Conectada às metas institucionais; interpretável para gestores |
| Goalposts | Definidos por especialistas + benchmarking | Mín/máx histórico | Mín/máx histórico não disponível; benchmarking fornece referências sólidas |
| Pesos | Alocação por julgamento estruturado | AHP; PCA; Pesos iguais | Simples, auditável, alinhado às prioridades institucionais sem exigir sessão formal de AHP |
| Agregação intra-risco | Média aritmética | Média geométrica | Indicadores do mesmo risco podem ser parcialmente substitutos |
| Agregação entre riscos | Média geométrica | Média aritmética | Impede compensação total entre dimensões de risco distintas |
| Compensabilidade | Parcial | Total; Nenhuma | Equilibrio entre penalizar desequilíbrios e manter inteligibilidade |
| Periodicidade | Quadrimestral | Mensal; Semestral | Alinhamento com ciclo da Matriz de Gestão de Riscos |
| Teto do score | 1,0 (superar meta não compensa) | Sem teto | Evita gaming; o índice mede cumprimento de metas, não excelência |

---

## 11. Limitações e pontos de atenção

1. **Resolutividade como KRI:** A definição de "resolutividade" varia entre sistemas. Verificar se o valor do SGOe corresponde à percepção do cidadão (resolutividade declarada via pesquisa) ou ao julgamento do ouvidor. Usar definição consistente ao longo do tempo. A escolha tem impacto direto na limitação nº 2 abaixo.

2. **Concentração de 45% do peso na pesquisa de satisfação:** KRI 3 (Resolutividade, 25%) e KRI 5 (Nota de Recomendação, 20%) compartilham o mesmo denominador — pesquisas respondidas. Consequências:
   - Baixa taxa de resposta compromete 45% do IGRO de uma vez, por viés de não-resposta — não por deterioração real do atendimento
   - Os dois KRIs tendem a se mover juntos (mesma base de respondentes), reduzindo a independência dentro do Sub-IGRO_Q
   - O limiar mínimo de cálculo para ambos é n ≥ 20 pesquisas respondidas (não manifestações totais)
   - **Mitigação possível:** usar resolutividade do ouvidor (cobertura 100%) para KRI 3, reservando a pesquisa apenas para KRI 5 — resolve a dependência estrutural mas requer resolução de D1

3. **Ausência de dados históricos:** Na ausência de série histórica, os goalposts foram definidos por benchmarking externo (arquivo 09). Após 4–6 quadrimestres, revisar os goalposts com base na realidade local.

4. **KRI ausente — Volume de manifestações:** O número absoluto de manifestações foi intencionalmente excluído do IGRO por ter polaridade ambígua (maior volume pode ser sinal positivo de acesso OU negativo de problemas sistêmicos). Monitorar separadamente.

5. **Dados do SGOe:** O cálculo do IGRO depende da qualidade dos dados do SGOe. Inconsistências no registro (manifestações duplicadas, erros de tipologia) afetam diretamente os KRIs.

6. **Comparabilidade entre órgãos:** O IGRO com estes parâmetros compara a ouvidoria **com ela mesma ao longo do tempo** — não entre órgãos, que têm metas e realidades distintas.

---

## 12. Fontes do inbox compiladas

A **Oficina de Prototipação de Relatório das Ouvidorias** (SEAD/Pequi Lab, jun/2023, 29 participantes do GT Relatórios Gerenciais da OGE-GO) forneceu validação qualitativa da seleção de KRIs:

- **Confirmação dos KRIs selecionados:** Todos os grupos participantes citaram espontaneamente "Tempo de Resposta / Resolutividade / Pesquisa de Satisfação" como os indicadores essenciais — exatamente os 5 KRIs do IGRO
- **Dúvida levantada na oficina:** "Deve conter informações monitoradas nos riscos?" — o IGRO responde diretamente a essa lacuna
- **Polaridade ambígua de volume:** A oficina identificou que o Número de Manifestações tem polaridade invertida dependendo do órgão — justifica sua exclusão do IGRO como KRI
- **Público-alvo:** Consenso de que o relatório deve ser para a **alta gestão** — reforça a necessidade de um índice sintético (IGRO) em vez de exposição dos 5 KRIs individuais

---

## 13. Próximos passos

1. **Validar metas** com o GT de Gestão de Riscos — confirmar se as metas da Matriz são as mesmas ou atualizá-las
2. **Calcular retroativamente** com os dados dos quadrimestres disponíveis (série histórica do SGOe) para calibrar goalposts
3. **Executar análise de robustez** (4 cenários de pesos + leave-one-out) — planilha Excel suficiente
4. **Apresentar ao Comitê Setorial** para aprovação como instrumento complementar da Matriz
5. **Integrar ao relatório gerencial quadrimestral** — o IGRO deve aparecer no cabeçalho do relatório com o semáforo e os sub-índices

---

## 14. Referências

- OECD/JRC (2008). *Handbook on Constructing Composite Indicators* — capítulos 5 (Normalização), 6 (Ponderação), 7 (Agregação), 8 (Robustez)
- Mazziotta & Pareto (2022). Aggregating Composite Indicators through the Geometric Mean — MDPI Computation
- SEAD/Pequi Lab (2023). Consolidado da Oficina de Prototipação de Relatório das Ouvidorias — arquivo `00_inbox/archives/`
- Benchmarking de metas: arquivo `09_Benchmarking_KRIs_Ouvidorias_Estaduais.md`
- Metodologia de normalização: arquivo `02_Normalizacao_Metodos.md`
- Ponderação: arquivo `03_Ponderacao_Metodos.md`
- Agregação: arquivo `04_Agregacao_Metodos.md`
- Robustez: arquivo `05_Analise_Robustez_Sensibilidade.md`
