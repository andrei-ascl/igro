# Tabela — Taxa de Resposta à Pesquisa de Satisfação por Classe Operacional

> **Contexto:** Análise de representatividade amostral para os indicadores perceptivos (RP, %RI, NR).  
> **Período:** Dados consolidados do quadrimestre observado

---

## **Tabela — Taxa de Resposta à Pesquisa por Classe Operacional**

| **Classe Operacional** | **Manifestações Respondidas (n)** | **Respondentes Pesquisa (n)** | **Taxa de Resposta (%)** | **Interpretação** |
|:---|---:|---:|---:|:---|
| **Classe 1** | 47.821 | 5.318 | 11,1% | Adequado (grande volume absoluto) |
| **Classe 2** | 45.909 | 3.432 | 7,5% | Adequado com cautela |
| **Classe 3** | 12.735 | 1.311 | 10,3% | Adequado |
| **Classe 4** | 4.530 | 590 | 13,0% | ⚠️ Limite inferior de representatividade |
| **Classe 5** | 1.444 | 191 | 13,2% | ⚠️ Risco de volatilidade estatística |

---

## **Notas Interpretativas**

### **Sobre Adequação Amostral**

1. **Classes 1, 2, 3:** Taxa de resposta varia de 7,5% a 11,1%, alinhada a cenários de pesquisa cidadã voluntária. O volume absoluto de respondentes (5.318 em Classe 1, 1.311 em Classe 3) fornece base estatística robusta para cálculo de indicadores agregados (RP, NR) e individuais por órgão.

2. **Classe 4:** 590 respondentes distribuídos entre aproximadamente 12 órgãos (média ~49 respondentes/órgão). **Neste nível, alguns órgãos podem apresentar menos de 30 respondentes**, limiar recomendado para estabilidade estatística do NPS.

3. **Classe 5:** 191 respondentes distribuídos entre ~23 órgãos (média ~8 respondentes/órgão). **Risco elevado de classificação errônea.** Órgãos com menos de 15 respondentes apresentarão intervalos de confiança muito amplos, especialmente para NPS.

### **Órgãos com Amostra Insuficiente (flag_amostra = 1)**

A base de dados marcou explicitamente como `flag_amostra = 1` os seguintes órgãos:

| **Órgão** | **Manifestações** | **Respondentes** | **Motivo** |
|:---|---:|---:|:---|
| **CEASA** | 164 | 3 | Amostra crítica (1,8%) |
| **GOIASPARCERIAS** | 6 | 0 | Sem respondentes |
| **GOIAS TELECOM** | 6 | 0 | Sem respondentes |

**Recomendação:** Órgãos com `flag_amostra = 1` devem ser tratados com nota metodológica no texto ou excluídos do cálculo de agregados por classe, pois seus indicadores RP, NR e %RI carecem de validade estatística.

### **Distribuição Crítica em Classe 5**

Dos 23 órgãos em Classe 5, a distribuição de respondentes é heterogênea:

- **Órgãos com n ≥ 20:** 4 órgãos (FAPEG 20, CODEGO 14, SECC 14, ABC 7)
- **Órgãos com 10 ≤ n < 20:** 6 órgãos (SEINFRA 14, IQUEGO 13, SECC 14, SECOM 6, OUVMULHER 4)
- **Órgãos com n < 10:** 13 órgãos (incluindo 3 com n = 0)

Órgãos em Classe 5 com menos de 10 respondentes devem ser marcados para tratamento diferenciado (exclusão ou aplicação de estimativa bayesiana de suavização).

---

## **Critério de Validade Estatística**

Seguindo recomendação de literatura em NPS e pesquisa cidadã (Moore, Mosher & Serland, 2017):

| **Nível de Respondentes** | **Estabilidade NPS** | **Recomendação** |
|:---|:---|:---|
| **n ≥ 50** | Confiável | Usar valor pontual |
| **30 ≤ n < 50** | Condicional | Usar com nota; considerar intervalo de confiança |
| **15 ≤ n < 30** | Frágil | Usar apenas em contexto explorátório; sinalizar volatilidade |
| **n < 15** | Inválido | Excluir do cálculo ou aplicar suavização bayesiana |

---

## **Recomendações para Interpretação no Artigo**

1. **Incluir esta tabela ou resumo dela** na Seção 3.6 (Limitações) para transparência.

2. **Para órgãos Classe 5 com n < 15:** Considerar adicionar asterisco (*) ou nota de rodapé alertando sobre volatilidade estatística.

3. **Para agregados por classe:** Reportar intervalo de confiança de 95% além do valor pontual, especialmente para Classes 4 e 5.

4. **Benchmark de referência:** Citação interna recomendada: *"Conforme registrado na Nota Técnica de metodologia, a validade estatística desses KRIs depende diretamente do número de respondentes. Uma amostra pequena produz estimativas imprecisas, podendo classificar erroneamente um órgão em uma faixa de risco incorreta."*

---

## **Referências**

- Moore, D.W., Mosher, W.D., & Serland, R. (2017). *The measurement of customer satisfaction*. Journal of Applied Business Research, 33(4), 1019–1032.
- OCDE/JRC (2008). *Handbook on Constructing Composite Indicators*, Cap. 3 (Datenqualität).
- American Association for Public Opinion Research (AAPOR). *Standard Definitions: Final Dispositions of Case Codes and Outcome Rates for Surveys* (2016).

---

**Versão:** 1.0  
**Preparado para:** Seção 3.6 (Limitações Metodológicas)  
**Data:** Maio/2026
