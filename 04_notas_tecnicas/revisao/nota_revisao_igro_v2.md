# Nota de Revisão — Artigo IGRO v2

**Data:** 11 de maio de 2026  
**Arquivo revisado:** `10_publicacao/submissao/artigo_igro_v2_critica_aplicada.md`  
**Arquivo original:** `artigo_igro_revisado_gpt_com_indicacoes_visuais.md`  
**Crítica de referência:** `critica_cientifica_igro_2026-05-11.md`

---

## Melhorias aplicadas

| # | Melhoria | Status |
|---|----------|--------|
| 3.2 | Análise de sensibilidade (seção 3.5 + seção 4.6) | ✅ Estrutura criada — **aguarda dados** |
| 3.3 | Correlação RP×NR com Spearman, p-valor, IC 95% | ✅ Formato inserido — **aguarda dados** |
| 3.5 | Justificativa empírica da ponderação uniforme (3 cenários) | ✅ Desenho completo — **aguarda dados** |
| 3.6 | Tabela de goalposts com formato sugerido | ✅ TMR e PMA preenchidos — **RP, %RI, NR aguardam dados** |
| 3.7 | Eliminação de duplicações | ✅ Concluído (921 → 595 linhas, redução de 35%) |
| 3.8 | Padronização de siglas + lista de abreviaturas | ✅ Concluído (RDP→PMA, TR→RP padronizados) |
| 3.9 | Análise de viés de autorresposta | ✅ Tabela formato sugerido — **aguarda dados** |
| 3.10 | Seção LGPD (seção 3.7 do artigo) | ✅ Concluído |
| 3.11 | Contribuição teórica explícita (seção 5.1 do artigo) | ✅ Concluído |

---

## Dados necessários para a segunda rodada

Para preencher os 10 placeholders (`[INSERIR DADOS]`) restantes no artigo, são necessários:

### 1. Tabela de KRIs por órgão
- 51 linhas (uma por órgão) × 5 colunas (TMR, PMA, RP, %RI, NR)
- Valores **normalizados** (escala 0–1) ou **brutos** (eu normalizo)

### 2. Goalposts dos indicadores de qualidade
- **RP:** meta de excelência (%) e limite aceitável (%)
- **%RI:** meta de excelência (%) e limite aceitável (%)
- **NR:** meta de excelência (NPS) e limite aceitável (NPS)
- Fonte de cada parâmetro (benchmark interno, literatura etc.)

### 3. Taxa de resposta da pesquisa de satisfação
- Por órgão (ideal) ou por classe operacional (mínimo)
- Colunas: manifestações (n), respondentes (n), taxa (%)

### 4. Confirmação dos pesos
- Confirmar se os pesos são uniformes (w = 0,20 para cada KRI)

---

## O que será calculado com os dados

- Coeficiente de Spearman (ρₛ) entre RP e NR, com p-valor e IC 95%
- IGRO recalculado em 3 cenários de ponderação (uniforme, qualidade, tempestividade)
- Comparação média geométrica vs. aritmética
- Bootstrap com 1.000 iterações (±10% nos pesos)
- Identificação de órgãos com menos de 30 respondentes na pesquisa de satisfação
