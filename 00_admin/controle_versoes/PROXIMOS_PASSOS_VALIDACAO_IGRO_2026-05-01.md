# Próximos Passos — Validação Técnica IGRO 
**Data:** 2026-05-01  
**Status:** Pós-Validação de Notas Internas [a], [b], [c], [d]

---

## Resumo Executivo

Após validação completa das 4 notas internas do artigo IGRO, 3 itens **críticos** e 1 item **moderado** foram identificados. Este documento organiza os próximos passos e responsabilidades técnicas.

### Status das Correções
- [x] **[a] Período de Análise** — CORRIGIDO: "janeiro 2024 - dezembro 2026" → "janeiro 2024 - abril 2026"
- [x] **[c] Nomenclatura de Colunas** — CORRIGIDO: `data_entrada`/`data_resposta_definitiva` → `data_manifestacao`/`data_finalizacao`; `status_manifestacao` → `f_insatisfatorias`
- [ ] **[b] Calibração de Metas** — PENDENTE: Pesquisa + nova seção do artigo
- [ ] **[d] Fórmulas DAX** — PENDENTE: Export + validação de 114 measures

---

## 1️⃣ ✅ RESOLVIDO: Confirmação de Nomes de Colunas SGOe [c]

### Validação Confirmada (2026-05-01)
As colunas do Power BI são as válidas:

| Campo Anterior | Campo Correto (Power BI) | Uso | Status |
|---|---|---|---|
| `data_entrada` | `data_manifestacao` | Início da contagem de prazos (TMR, seção 3.3) | ✅ CORRIGIDO |
| `data_resposta_definitiva` | `data_finalizacao` | Fim da contagem de prazos (TMR, seção 3.3) | ✅ CORRIGIDO |
| `status_manifestacao` | `f_insatisfatorias` (tabela) | Classificação de insatisfação (RI%, seção 3.5) | ✅ CORRIGIDO |

### Ações Tomadas
1. ✅ Artigo atualizado com nomes corretos de colunas
2. ✅ Validação técnica concluída (confirmado com CGE-GO)
3. ✅ Nomenclatura alinhada: artigo ↔ modelo Power BI ↔ banco dados SGOe

---

## 2️⃣ CRÍTICO: Validação de Período de Dados Reais

### Confirmação Necessária
- ✅ **Período:** 2026-05-01 → artigo corrigido para "jan 2024 - abr 2026"
- ❓ **Total de manifestações:** 109.338 é o número real em abril de 2026?
- ❓ **Cobertura:** Os dados cobrem todas as 51 unidades do Executivo estadual?

### Ação Requerida
**Responsável:** Gestor de dados SGOe

1. Exportar contagem total de manifestações (jan 2024 - abr 2026)
2. Validar cobertura de unidades administrativas
3. Confirmar se há gaps ou períodos com dados faltantes

**Prazo Sugerido:** 2026-05-10

---

## 3️⃣ MODERADO: Calibração de Metas [b]

### Problema
O artigo especifica 4 metas operacionais sem justificativa ou benchmarking:

| Indicador | Meta | Limite Aceitável | Justificativa no Artigo |
|---|---|---|---|
| TMR | 5 dias | 10 dias | ❌ NÃO EXPLICADA |
| TR | 70% | 50% | ❌ NÃO EXPLICADA |
| RI | 2,5% | 3,5% | ❌ NÃO EXPLICADA |
| NR | 8,0 | 6,0 | ❌ NÃO EXPLICADA |

### Oportunidade
Adicionar **nova seção 2.4 "Calibração de Metas para Contexto de Goiás"** com:

1. **Benchmarking comparativo:**
   - Resolutividade em CE, SP, MG (outras ouvidorias estaduais)
   - Performance histórica Goiás (2024-2025)
   - Normas legais (Lei 13.460, Decreto 10.466)

2. **Justificativa técnica:**
   - TMR 5d = prazo legal 20d ÷ 4 (fator de excelência)
   - TR 70% = target de resolutividade para ouvidoria moderna
   - RI 2,5% = limite aceitável de retrabalho
   - NR 8,0 = score mínimo de satisfação aceitável

3. **Processo de validação:**
   - Checklist de calibração técnica
   - Feedback da equipe CGE-GO
   - Consenso institucional

### Ação Requerida
**Responsável:** Analista IGRO (Claude) + CGE-GO

1. Pesquisar benchmarks comparativos (ouvidorias CE, SP, MG)
2. Documentar histórico de performance Goiás 2024-2025
3. Redatar seção 2.4 com justificativas técnicas
4. Validar com gestor CGE-GO

**Prazo Sugerido:** 2026-05-15

**Referências para pesquisa:**
- OMD (Ouvidoria do Ministério da Defesa) — dados de comparação
- Decreto 12.304/2024 (Goiás) — normas recentes
- Relatório OECD 2025 sobre ouvidorias públicas

---

## 4️⃣ MODERADO: Validação de Fórmulas DAX [d]

### Contexto
O artigo especifica 11 medidas (ou derivadas delas):
1. TMR (dias)
2. RDP% (%)
3. TR (%)
4. RI% (%)
5. NR (score)
6. TMR_norm (0-1)
7. RDP%_norm (0-1)
8. TR_norm (0-1)
9. RI%_norm (0-1)
10. NR_norm (0-1)
11. IGRO (índice composto 0-100)

**Problema:** O modelo Power BI contém **114 measures DAX**. Sem export completo da lista, não é possível validar se:
- Todas as 11 medidas do artigo estão implementadas corretamente
- Os nomes DAX correspondem aos nomes do artigo
- As fórmulas de normalização (min-max com goalposts) estão corretas
- A agregação final IGRO segue o referencial OCDE/JRC

### Ação Requerida
**Responsável:** Desenvolvedor Power BI / CGE-GO

1. **Export de medidas:** Exportar lista completa de 114 measures com:
   - Nome do measure
   - Fórmula DAX
   - Descrição
   - Categorização (base, normalização, agregação)

2. **Mapeamento artigo ↔ Power BI:**
   - Verificar correspondência 1:1 para as 11 medidas principais
   - Validar nomenclatura e sintaxe DAX
   - Testar cálculos end-to-end

3. **Documentação:**
   - Atualizar `documentacao_modelo_semantico_igro.md` com fórmulas validadas
   - Criar seção de validação de cálculos no artigo

**Prazo Sugerido:** 2026-05-15

---

## Timeline de Execução

```
2026-05-01  ✅ Período de análise corrigido
2026-05-10  🔵 Confirmação de nomes de colunas + dados reais
2026-05-15  🔵 Calibração de metas + export DAX measures
2026-05-20  🔵 Redação final artigo + validação cruzada
2026-05-27  🟢 Artigo final pronto para publicação
```

---

## Matriz de Responsabilidades

| Item | Severidade | Resp. | Prazo | Bloqueador? |
|---|---|---|---|---|
| [a] Período | CRÍTICO | ✅ Feito | — | ❌ Não |
| [c] Colunas SGOe | CRÍTICO | ✅ Feito | — | ❌ Não |
| [d] Export DAX | MODERADO | Power BI Dev | 2026-05-15 | ✅ Sim* |
| [b] Metas | MODERADO | Claude + CGE-GO | 2026-05-15 | ❌ Não |

*Bloqueador apenas se validação DAX resultar em correções estruturais

---

## Documentos Relacionados

- `VALIDACAO_NOTAS_INTERNAS_2026-05-01.md` — Relatório detalhado de validação
- `AVALIACAO_ARTIGO_IGRO_2026-05-01.md` — Avaliação de referências
- `04_powerbi_e_dax/documentacao_modelo_semantico_igro.md` — Modelo técnico

---

**Próxima revisão:** 2026-05-10 (após feedback CGE-GO sobre nomes de colunas)
