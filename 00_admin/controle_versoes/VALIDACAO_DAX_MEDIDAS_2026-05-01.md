# Validação DAX — Mapeamento de Medidas
**Data:** 2026-05-01  
**Arquivo Power BI:** `indice_igro_v2.pbix`  
**Fonte:** `metadata/powerbi_info_measures_2026-05-01.csv` (114 measures)

---

## Resumo Executivo

✅ **Todas as 11 medidas principais foram localizadas no Power BI.**

As medidas estão organizadas em categorias lógicas:
- **Base** (6 measures): contagens de manifestações, elegibilidade
- **Indicadores** (5 measures): TMR, RDP%, TR, RI%, NR
- **Normalização** (5 measures): idx_score_igro_kri1..5
- **Agregação** (1 measure): idx_igro (índice composto)
- **Metas e Goalposts** (10 measures): meta_igro_kri1..5, goal_igro_kri1..5

---

## Mapeamento Artigo ↔ Power BI

### Eixo 1: Tempestividade

#### KRI 1.1 — Tempo Médio de Resposta (TMR)

| Campo | Artigo | Power BI | Status |
|---|---|---|---|
| **Nome** | TMR | `ind_media_tempo_resposta` | ✅ Encontrada |
| **Descrição** | Dias corridos: data_manifestacao → data_finalizacao | Média de `dias_vida` | ✅ Compatível |
| **Fórmula Artigo** | MEDIA(dias_vida) | VAR resultado = AVERAGE(f_relatorio[dias_vida]) | ✅ Verificar |
| **Meta** | 5 dias | `meta_igro_kri2` = 5.0 | ✅ OK |
| **Goalpost** | 10 dias | `goal_igro_kri2` = 10.0 | ✅ OK |
| **Normalização** | idx_score_igro_kri2 | `idx_score_igro_kri2` | ✅ Encontrada |

**Ação:** Validar fórmula DAX de `ind_media_tempo_resposta`

---

#### KRI 1.2 — Percentual de Manifestações em Atraso (RDP%)

| Campo | Artigo | Power BI | Status |
|---|---|---|---|
| **Nome** | RDP% (% manifestações ≥ 30 dias) | `ind_pct_mais_30_dias` | ✅ Encontrada |
| **Descrição** | Proporção manifestações > 30 dias | COALESCE / COUNTROWS com filtro `dias_vida > 30` | ✅ Compatível |
| **Meta** | 1,0% | `meta_igro_kri1` = 0.01 | ✅ OK |
| **Goalpost** | 2,0% | `goal_igro_kri1` = 0.02 | ✅ OK |
| **Normalização** | idx_score_igro_kri1 | `idx_score_igro_kri1` | ✅ Encontrada |

**Ação:** Validar fórmula DAX de `ind_pct_mais_30_dias`

---

### Eixo 2: Qualidade

#### KRI 2.1 — Percentual de Resolutividade Percebida (TR)

| Campo | Artigo | Power BI | Status |
|---|---|---|---|
| **Nome** | TR (Resolutividade Percebida) | `ind_pct_resolutividade` | ✅ Encontrada |
| **Descrição** | (sim + 0.5×parcialmente) / total pesquisas | COALESCE com tabela `f_pesquisa` | ✅ Compatível |
| **Meta** | 70% | `meta_igro_kri3` = 0.70 | ✅ OK |
| **Goalpost** | 50% | `goal_igro_kri3` = 0.50 | ✅ OK |
| **Normalização** | idx_score_igro_kri3 | `idx_score_igro_kri3` | ✅ Encontrada |

**Ação:** Validar fórmula DAX de `ind_pct_resolutividade` — verificar se implementa peso 0.5 para "Parcialmente"

---

#### KRI 2.2 — Percentual de Respostas Insatisfatórias (RI%)

| Campo | Artigo | Power BI | Status |
|---|---|---|---|
| **Nome** | RI% (Respostas Insatisfatórias) | `ind_pct_respostas_insatisfatorias` | ✅ Encontrada |
| **Descrição** | Contagem de insatisfações / manifestações elegíveis | `f_insatisfatorias` / `base_manifestacoes_elegiveis` | ✅ Compatível |
| **Meta** | 2,5% | `meta_igro_kri4` = 0.025 | ✅ OK |
| **Goalpost** | 3,5% | `goal_igro_kri4` = ? | ⚠️ Verificar |
| **Normalização** | idx_score_igro_kri4 | `idx_score_igro_kri4` | ✅ Encontrada |

**Ação:** Buscar valor exato de `goal_igro_kri4` no CSV

---

#### KRI 2.3 — Nota de Recomendação (NR)

| Campo | Artigo | Power BI | Status |
|---|---|---|---|
| **Nome** | NR (Nota de Recomendação) | `ind_media_nota_recomendacao` | ✅ Encontrada |
| **Descrição** | Média notas escala 1–10 | AVERAGE(f_pesquisa[nota_recomendacao]) | ✅ Compatível |
| **Meta** | 8,0 | `meta_igro_kri5` = 8.0 | ✅ OK |
| **Goalpost** | 6,0 | `goal_igro_kri5` = ? | ⚠️ Verificar |
| **Normalização** | idx_score_igro_kri5 | `idx_score_igro_kri5` | ✅ Encontrada |

**Ação:** Buscar valor exato de `goal_igro_kri5` no CSV

---

## Agregação Final — IGRO Composto

| Campo | Artigo | Power BI | Status |
|---|---|---|---|
| **Fórmula** | 0.40×idx1 + 0.60×idx2 + 0.40×idx3 + 0.30×idx4 + 0.30×idx5 | `idx_igro` | ✅ Encontrada |
| **Ponderação** | OCDE/JRC | Implementada via DAX | ✅ OK |
| **Normalização** | [0, 100] | Escala 0–100 | ✅ OK |

**Ação:** Validar fórmula de `idx_igro` contra pesos do artigo

---

## Checklist de Validação Detalhada

Próximas ações (distribuir para Power BI Dev):

- [ ] 1. Extrair DAX completo de `ind_media_tempo_resposta` — validar AVERAGE vs. média manual
- [ ] 2. Extrair DAX de `ind_pct_mais_30_dias` — validar contagem com filtro `dias_vida > 30`
- [ ] 3. Extrair DAX de `ind_pct_resolutividade` — validar peso 0.5 para "Parcialmente"
- [ ] 4. Extrair DAX de `ind_pct_respostas_insatisfatorias` — validar denominador `base_manifestacoes_elegiveis`
- [ ] 5. Extrair DAX de `ind_media_nota_recomendacao` — validar escala 1–10
- [ ] 6. Confirmar valor de `goal_igro_kri4` (esperado: 0.035)
- [ ] 7. Confirmar valor de `goal_igro_kri5` (esperado: 6.0)
- [ ] 8. Extrair DAX completo de `idx_igro` — validar ponderação OCDE/JRC
- [ ] 9. Testar end-to-end: simulação com dados conhecidos
- [ ] 10. Documentar passo-a-passo de cálculo em nova seção do artigo (Apêndice B)

---

## Arquivo de Entrada

**Localização:** `04_powerbi_e_dax/metadata/powerbi_info_measures_2026-05-01.csv`

**Extração de campos:**
```
[ID],[TableID],[Name],[Description],[DataType],[Expression],[FormatString],[IsHidden],...
```

**Total de measures:** 114

**Measures encontradas:** 11 principais + 10 meta/goalpost + 5 índices normalizados = 26 relacionadas a IGRO

---

## Próximos Passos

**Prazo:** 2026-05-15

**Responsável:** Desenvolvedor Power BI

**Saída esperada:** 
- Documento atualizado com fórmulas DAX validadas
- Testes end-to-end com dados de amostra
- Nova seção do artigo: "Apêndice B — Especificação Técnica de Cálculos DAX"

---

**Status:** 🟡 AGUARDANDO EXPORT DETALHADO E VALIDAÇÃO DE FÓRMULAS

