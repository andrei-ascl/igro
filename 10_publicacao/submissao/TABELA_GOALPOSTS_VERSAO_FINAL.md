# Parâmetros de Normalização (Goalposts) dos KRIs do IGRO

> **Fonte das metas:** Planejamento Estratégico da CGE-GO  
> **Fonte dos limites aceitáveis:** Matriz de Gestão de Riscos (gestão de riscos da instituição)  
> **Documento técnico:** Desenho IGRO (arquivo 10), seção 4.3

---

## **Tabela — Parâmetros de Normalização (Goalposts) dos KRIs do IGRO**

| # | KRI | Meta de Excelência (→ 1,0) | Limite Aceitável (→ 0,0) | Polaridade | Fonte do Parâmetro |
|---|---|---|---|---|---|
| **1** | % Manifestações > 30 dias | ≤ 2,0% | ≥ 15,0% | Inversa (menor = melhor) | Meta: Planejamento Estratégico CGE \| Limite: Gestão de Riscos |
| **2** | Prazo Médio de Resposta (dias) | ≤ 10,0 | ≥ 30,0 | Inversa (menor = melhor) | Meta: Planejamento Estratégico CGE \| Limite: Lei 13.460/2017 (20 dias úteis) |
| **3** | Resolutividade Percebida (%) | ≥ 70,0% | ≤ 30,0% | Direta (maior = melhor) | Meta: Planejamento Estratégico CGE \| Limite: Gestão de Riscos |
| **4** | % Respostas Insatisfatórias | ≤ 2,5% | ≥ 20,0% | Inversa (menor = melhor) | Meta: Planejamento Estratégico CGE \| Limite: Gestão de Riscos |
| **5** | Nota de Recomendação (NPS) | ≥ 7,5 | ≤ 4,0 | Direta (maior = melhor) | Meta: Planejamento Estratégico CGE \| Limite: Gestão de Riscos |

---

## **Fundamentação dos Goalposts**

### **Estrutura de Referência (Dois Pontos de Ancoragem)**

Cada KRI é normalizado para a escala [0, 1] utilizando dois pontos de referência:

1. **Meta de Excelência (score = 1,0):** O valor desejável conforme objetivos estratégicos da CGE-GO. Representa o nível de desempenho alinhado com a visão institucional.

2. **Limite Aceitável / Goalpost (score = 0,0):** O valor mínimo aceitável conforme a Matriz de Gestão de Riscos, representando o ponto a partir do qual a instituição considera haver risco materializado. Abaixo deste limite, o KRI sinaliza deterioração significativa.

---

## **Justificativa por KRI**

### **KRI 1: % Manifestações > 30 dias**

**Meta de excelência:** 2,0%  
**Limite aceitável:** 15,0%

A meta de 2,0% reflete o Planejamento Estratégico da CGE-GO de manter prazos de resposta curtos. O limite de 15,0% foi definido na Matriz de Gestão de Riscos como o ponto de alerta severo para o Risco 0044 (atendimento fora do prazo). Acima deste limite, há materialização inequívoca de risco operacional.

---

### **KRI 2: Prazo Médio de Resposta (dias)**

**Meta de excelência:** 10,0 dias  
**Limite aceitável:** 30,0 dias

A meta de 10 dias provém do Planejamento Estratégico da CGE-GO e é mais rigorosa que o limite legal. O limite de 30 dias corresponde ao prazo máximo legal estabelecido pela Lei nº 13.460/2017 (20 dias úteis, aproximadamente 30 dias corridos), ponto a partir do qual há descumprimento normativo e risco regulatório elevado.

---

### **KRI 3: Resolutividade Percebida (%)**

**Meta de excelência:** 70,0%  
**Limite aceitável:** 30,0%

A meta de 70,0% alinha-se com o Planejamento Estratégico da CGE-GO e com boas práticas internacionais de resolutividade em atendimento cidadão. O limite de 30,0% foi estabelecido na Matriz de Gestão de Riscos como o patamar abaixo do qual há falha sistêmica no atendimento (Risco 0046 — qualidade). Abaixo de 30%, a instituição falha em resolver a maioria das demandas dos cidadãos.

---

### **KRI 4: % Respostas Insatisfatórias**

**Meta de excelência:** 2,5%  
**Limite aceitável:** 20,0%

A meta de 2,5% reflete o Planejamento Estratégico da CGE-GO de maximizar a qualidade percebida das respostas. O limite de 20,0% foi definido na Matriz de Gestão de Riscos como o ponto de alerta severo para o Risco 0046 (qualidade). Acima deste percentual, há materialização evidente de insatisfação cidadã.

---

### **KRI 5: Nota de Recomendação (NPS)**

**Meta de excelência:** 7,5 (em escala 0–10)  
**Limite aceitável:** 4,0 (em escala 0–10)

A meta de 7,5 provém do Planejamento Estratégico da CGE-GO e reflete o objetivo de alta reputação institucional. O limite de 4,0 foi estabelecido na Matriz de Gestão de Riscos como o patamar abaixo do qual há sinal de alerta para a confiança institucional. Notas abaixo de 6,0 sinalizam deterioração significativa da percepção cidadã.

---

## **Fórmulas de Cálculo**

### **Para KRIs "Inversa" (menor = melhor):**
```
score_i = (limite_máx_i − valor_i) / (limite_máx_i − meta_i)
score_i = max(0, min(1, score_i))
```
Aplicado a: KRI 1, KRI 2, KRI 4

### **Para KRIs "Direta" (maior = melhor):**
```
score_i = (valor_i − limite_mín_i) / (meta_i − limite_mín_i)
score_i = max(0, min(1, score_i))
```
Aplicado a: KRI 3, KRI 5

---

## **Exemplo de Normalização (Dados Reais)**

| KRI | Valor Observado | Meta | Goalpost | Fórmula | Score | Interpretação |
|---|---|---|---|---|---|---|
| **1** | 0,40% | 2,0% | 15,0% | (15 - 0,40) / (15 - 2) | **1,00** | ✅ Acima da meta |
| **2** | 6,3 dias | 10,0 | 30,0 | (30 - 6,3) / (30 - 10) | **1,00** | ✅ Acima da meta |
| **3** | 56,0% | 70,0% | 30,0% | (56 - 30) / (70 - 30) | **0,65** | ⚠️ Abaixo da meta |
| **4** | 1,52% | 2,5% | 20,0% | (20 - 1,52) / (20 - 2,5) | **1,00** | ✅ Acima da meta |
| **5** | 7,3 | 7,5 | 4,0 | (7,3 - 4,0) / (7,5 - 4,0) | **0,943** | ✅ Próximo da meta |

**Leitura:** KRIs 1, 2 e 4 estão no nível esperado (score = 1,0 ou próximo). KRI 3 apresenta score de 0,65 (amarelo), indicando que a Resolutividade está abaixo da meta em 14 pontos percentuais (56% vs. 70%). KRI 5 está praticamente na meta (7,3 vs. 7,5).

---

## **Rastreabilidade Metodológica**

| Parâmetro | Origem | Documento | Frequência de Revisão |
|---|---|---|---|
| **Metas dos KRIs** | Planejamento Estratégico CGE-GO | PDI ou documento equivalente | Anual (revisão junto ao GT Riscos) |
| **Limites aceitáveis** | Matriz de Gestão de Riscos | Matriz de Gestão de Riscos CGE-GO | Quadrimestral (ciclo de revisão) |
| **Goalposts** | Consolidação meta + limite | Desenho IGRO (arquivo 10) | Quadrimestral (com validação anual) |

---

## **Considerações para Futuras Revisões**

1. **Estabilidade temporal:** Os goalposts devem ser mantidos constantes ao longo dos quadrimestres iniciais (4–6) para permitir série histórica comparável.

2. **Calibração com dados reais:** Após acumular 4–6 quadrimestres de dados, os goalposts devem ser revistos à luz da realidade operacional da ouvidoria estadual, podendo ser ajustados com aprovação do GT de Gestão de Riscos.

3. **Alinhamento normativo:** Qualquer mudança em marcos legais (ex: alteração do prazo na Lei 13.460/2017) deve disparar revisão dos goalposts correspondentes.

4. **Benchmarking externo:** Periodicamente (anual), validar se os goalposts continuam alinhados com padrões de excelência em ouvidorias públicas brasileiras.

---

## **Referências**

- **CGE-GO.** Planejamento Estratégico da CGE-GO (disponível internamente)
- **CGE-GO.** Matriz de Gestão de Riscos — Riscos 0044 e 0046 (disponível internamente)
- **Brasil.** Lei nº 13.460/2017. Lei que dispõe sobre direitos e deveres do usuário dos serviços públicos
- **OCDE/JRC.** Handbook on Constructing Composite Indicators: Methodology and User Guide (2008)
- **CGE-GO.** Desenho Técnico do IGRO — arquivo 10 (documento interno)

---

**Versão:** 1.0  
**Data:** Maio/2026  
**Status:** Pronto para inserção no artigo
