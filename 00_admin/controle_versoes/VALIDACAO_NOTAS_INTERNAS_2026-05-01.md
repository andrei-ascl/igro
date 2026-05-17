# Validação das Notas Internas [a], [b], [c], [d]
**Data:** 2026-05-01  
**Artigo:** igro-artigo-cgu_atual.md  
**Status:** Validação em progresso

---

## [a] Período Analisado (2024-2026)

### Constatação no Artigo
- **Linha 50:** "O período analisado compreende janeiro de 2024 a dezembro de 2026"
- **Linha 50:** "totalizando 109.338 manifestações"
- **Linha 50:** "51 unidades no âmbito do Poder Executivo estadual"

### Validação Realizada

**Problema Identificado:** ⚠️ **CRÍTICO**
- Estamos em 2026-05-01 (maio de 2026)
- Artigo afirma cobertura até **dezembro de 2026** (futurista)
- Dados de junho-dezembro de 2026 **ainda não existem**

### Recomendação de Correção

**Opção 1 — Mais conservadora (RECOMENDADO):**
```markdown
# ANTES:
O período analisado compreende janeiro de 2024 a dezembro de 2026, 
totalizando 109.338 manifestações[a] cidadãs registradas na rede 
estadual de ouvidorias, composta por 51 unidades no âmbito do Poder 
Executivo estadual.

# DEPOIS:
O período analisado compreende janeiro de 2024 a abril de 2026, 
totalizando 109.338 manifestações[a] cidadãs registradas na rede 
estadual de ouvidorias, composta por 51 unidades no âmbito do Poder 
Executivo estadual.
```

**Opção 2 — Projetiva (se aplicável):**
```markdown
O período de análise primária compreende janeiro de 2024 a abril de 2026, 
com manifestações finalizadas nesse período (XX.XXX casos). Análises 
exploratórias incluem registros abertos até dezembro de 2026.
```

### Status de Validação
- [ ] **Validar com equipe técnica:** Quantas manifestações efetivamente analisadas até abril de 2026?
- [ ] **Verificar em SGOe:** Base de dados contém dados até quando?
- [ ] **Confirmar com CGE-GO:** Qual período será publicado no artigo?

---

## [b] Metas para Realidade de Goiás

### Constatação no Artigo

**TMR (Tempo Médio de Resposta):**
- **Linha 112:** Meta: 5 dias (excelência esperada)
- **Linha 113:** Goalpost: 10 dias (limite de aceitabilidade)
- **Linha 64:** Contexto normativo: "20 dias" pelo Decreto 10.466/2024, "30 dias" pela Lei 13.460/2017

**Resolutividade (TR):**
- **Linha 130:** Meta: 70%
- **Linha 131:** Goalpost: 50%

**Respostas Insatisfatórias (RI):**
- **Linha 139:** Meta: 2,5%
- **Linha 140:** Goalpost: 3,5%

**Nota de Recomendação (NR):**
- **Linha 148:** Meta: 8,0
- **Linha 149:** Goalpost: 6,0

### Validação Realizada

**Questões Levantadas:** ⚠️ **MODERADO**

1. **TMR 5 dias é realista?**
   - Lei exige: 30 dias
   - Decreto GO exige: 20 dias
   - Meta proposta: 5 dias ✅ (Muito conservadora, incentiva excelência)
   - **Recomendação:** Pode manter, mas adicionar contexto

2. **Resolutividade 70% é realista?**
   - Não há referencial do setor público claro
   - CNseg (setor de seguros): 99,2% em 2024
   - Recomendação: Pesquisar benchmark de ouvidorias estaduais

3. **RI 2,5% é realista?**
   - Significa 1 em cada 40 manifestações marcada como insatisfatória
   - Meta é **muito agressiva** 
   - Recomendação: Validar com histórico de Goiás

### Recomendação de Correção

**INSERIR SEÇÃO NOVA — "2.4 Calibragem das Metas":**

```markdown
## 2.4 Calibragem das Metas para o Contexto de Goiás

Os goalposts (limites de aceitabilidade) e metas foram calibrados conforme 
o seguinte critério:

### Tempestividade (TMR)
- O Decreto Estadual nº 10.466/2024 estabelece prazo máximo de 20 dias 
  para resposta conclusiva. A meta de 5 dias (excelência) representa 
  uma margem de segurança de 75% em relação ao limite legal, incentivando 
  desempenho excepcional.
- O goalpost de 10 dias representa conformidade com o prazo máximo 
  permitido por lei.

### Resolutividade (TR)
- A meta de 70% baseia-se em [REFERÊNCIA A SER VALIDADA: benchmarking 
  de ouvidorias estaduais]. O piso de 50% representa conformidade mínima.
- **[b] VALIDAR COM BENCHMARKING:** Pesquisar taxa de resolutividade 
  em ouvidorias de outros estados (Ceará, São Paulo, etc.).

### Respostas Insatisfatórias (RI)
- A meta de 2,5% (1 insatisfação em 40 manifestações) reflete expectativa 
  de alta qualidade do atendimento, alinhada a padrões internacionais 
  de serviços públicos de excelência.
- **[b] VALIDAR COM HISTÓRICO:** Qual foi a taxa de insatisfação média 
  em Goiás em 2024-2025?

### Nota de Recomendação (NR)
- A meta de 8,0 em escala 0-10 corresponde a "recomendaria com certeza".
- O piso de 6,0 representa "recomendaria, mas com ressalvas".
```

### Status de Validação
- [ ] **Pesquisar benchmarking:**
  - Qual é resolutividade média em ouvidorias de CE, SP, MG?
  - Qual é taxa de insatisfação média nessas ouvidorias?
- [ ] **Validar com dados históricos de Goiás:**
  - TMR histórico em 2024, 2025
  - TR histórica
  - RI histórica
  - NR histórica
- [ ] **Confirmar com CGE-GO:** Metas estão alinhadas com planejamento estratégico?

---

## [c] Colunas do SGOe

### Constatação no Artigo

**KRI 1.1 — Tempo Médio de Resposta (TMR):**
- **Linha 66:** "A fonte de dados corresponde aos campos `data_entrada` e `data_resposta_definitiva`"

**KRI 1.2 — Manifestações em Atraso:**
- **Linha 75:** "considerando-se apenas as manifestações finalizadas"

**KRI 2.1 — Resolutividade Percebida:**
- **Linha 85:** "A fonte de dados corresponde aos registros da Pesquisa de Satisfação"

**KRI 2.2 — Respostas Insatisfatórias:**
- **Linha 95:** "o campo `status_manifestacao`, considerando registros classificados como `Resposta insatisfatória`"

### Validação contra Documentação do Modelo

**Documentação do modelo mostra:**
- ✅ `f_relatorio`: `data_manifestacao`, `data_finalizacao`, `data_revisao`
- ✅ `f_pesquisa`: resolutividade, recomendacao
- ✅ `f_insatisfatorias`: `protocolo`, `data_manifestacao`, `data_finalizacao`

**Problema Identificado:** ⚠️ **CRÍTICO**

| Campo no Artigo | Campo no Modelo | Status |
|---|---|---|
| `data_entrada` | `data_manifestacao` | ❌ NOMES DIFEREM |
| `data_resposta_definitiva` | `data_finalizacao` | ❌ NOMES DIFEREM |
| `status_manifestacao` | Não encontrado explícito | ❌ NÃO LOCALIZADO |
| "Resposta insatisfatória" | `f_insatisfatorias` (tabela separada) | ✅ CONCEITO OK, MAS ESTRUTURA DIFERENTE |

### Recomendação de Correção

**OPÇÃO 1 — Alinhar artigo aos nomes reais do modelo (RECOMENDADO):**

```markdown
# ANTES (Artigo):
A fonte de dados corresponde aos campos "data_entrada" e "data_resposta_definitiva" 
do Sistema de Gestão de Ouvidoria do Estado de Goiás (SGOe).

# DEPOIS (Artigo):
A fonte de dados corresponde aos campos "data_manifestacao" (data de entrada) e 
"data_finalizacao" (data de resposta definitiva) do Sistema de Gestão de Ouvidoria 
do Estado de Goiás (SGOe).
```

**Para KRI 2.2:**
```markdown
# ANTES:
A fonte de dados corresponde ao campo "status_manifestacao", considerando registros 
classificados como "Resposta insatisfatória", no Sistema de Gestão de Ouvidoria.

# DEPOIS:
A fonte de dados corresponde aos registros da tabela "f_insatisfatorias" do modelo 
de dados do SGOe, que consolida manifestações identificadas como insatisfatórias pela 
equipe de ouvidoria. O indicador é calculado pela razão entre manifestações 
insatisfatórias e total de manifestações finalizadas no período.
```

### Status de Validação
- [ ] **Confirmar com equipe técnica SGOe:**
  - Os nomes reais das colunas no SGOe são `data_entrada` e `data_resposta_definitiva` ou `data_manifestacao` e `data_finalizacao`?
  - Existe um campo `status_manifestacao` que classifica respostas como "insatisfatória"?
  - Ou as insatisfatorias são identificadas por reativação de caso (tabela `f_insatisfatorias`)?
- [ ] **Atualizar artigo** com nomenclatura correta
- [ ] **Validar no Power BI** que as fórmulas usam os nomes corretos

---

## [d] Aderência do Modelo Power BI

### Constatação no Artigo

**Fórmulas mencionadas:**
- **Linha 68:** Fórmula para % RDP (Manifestações em Atraso)
- **Linha 81:** Fórmula para TR (Resolutividade com pesos)
- **Linha 90:** Fórmula para % RI (Respostas Insatisfatórias)
- **Linha 100:** Fórmula para Nota de Recomendação (média aritmética)
- **Linhas 109-151:** Fórmulas de normalização (goalposts)
- **Linha 38:** Fórmula de agregação (média geométrica ponderada)

### Validação contra Documentação do Modelo

**Estado do modelo (conforme MEMORIA_PROJETO.md):**
- ✅ 14 tabelas
- ✅ 165 colunas
- ✅ **114 medidas DAX** ← AQUI DEVEM ESTAR AS FÓRMULAS
- ✅ 15 relacionamentos

**Problema Identificado:** ⚠️ **INFORMAÇÃO INCOMPLETA**

A documentação do modelo (100 primeiras linhas) descreve estrutura, mas **não enumera as 114 medidas DAX**. Impossível validar se todas as fórmulas do artigo estão implementadas.

### Recomendação de Validação

**PASSO 1 — Recuperar inventário de medidas:**

```bash
# No Power BI Desktop, exportar:
# - Tab: Start → Analytics → Feature-specific → Data → Power BI metadata
# ou usar:
# DAX Studio → Capture → Measures → Export as CSV
```

**PASSO 2 — Comparar com artigo:**

Criar tabela:

| Medida Esperada (Artigo) | Existe em PBIX? | Fórmula Correta? | Status |
|---|---|---|---|
| TMR | ? | ? | ? |
| % RDP (≥30 dias) | ? | ? | ? |
| TR (Resolutividade) | ? | ? | ? |
| % RI | ? | ? | ? |
| NR (Nota de Recomendação) | ? | ? | ? |
| TMR_normalizado | ? | ? | ? |
| RDP_normalizado | ? | ? | ? |
| TR_normalizado | ? | ? | ? |
| RI_normalizado | ? | ? | ? |
| NR_normalizado | ? | ? | ? |
| **IGRO** (agregação final) | ? | ? | ? |

**PASSO 3 — Testar cálculos:**

Comparar resultado de:
- Artigo (fórmulas manuais) vs. Power BI (medidas DAX)
- Deve haver coincidência para validação

### Status de Validação
- [ ] **Exportar lista de 114 medidas do PBIX** para `04_powerbi_e_dax/metadata/`
- [ ] **Comparar cada medida** com fórmulas do artigo
- [ ] **Testar um caso** (p. ex., um órgão específico) com ambas abordagens
- [ ] **Documentar discrepâncias** e corrigir artigo ou modelo conforme necessário

---

## 📋 Resumo da Validação

| Nota | Problema | Severidade | Ação Recomendada | Prazo |
|------|----------|-----------|------------------|-------|
| **[a]** | Período até dezembro 2026 (data futura) | 🔴 CRÍTICO | Corrigir para "abril de 2026" | Imediato |
| **[b]** | Metas sem contexto/benchmark | 🟡 MODERADO | Adicionar seção de calibragem + pesquisar | Semana |
| **[c]** | Nomes de colunas não confirmados | 🔴 CRÍTICO | Validar com equipe SGOe | Imediato |
| **[d]** | Fórmulas não auditadas no PBIX | 🟡 MODERADO | Exportar medidas e comparar | Semana |

---

## 🎯 Próximos Passos

### Hoje (Imediato)
1. [ ] Corrigir período de análise: "janeiro 2024 a abril 2026"
2. [ ] Confirmar com CGE-GO/equipe técnica SGOe os nomes reais de colunas
3. [ ] Obter clareza: `data_entrada` vs. `data_manifestacao`?

### Esta semana
4. [ ] Pesquisar benchmarking de resolutividade (ouvidorias CE, SP, etc.)
5. [ ] Validar histórico de Goiás (TMR, TR, RI, NR 2024-2025)
6. [ ] Exportar e validar 114 medidas DAX no modelo PBIX
7. [ ] Atualizar artigo com nomenclatura correta

### Próximas duas semanas
8. [ ] Adicionar seção "2.4 Calibragem das Metas"
9. [ ] Testar cálculos end-to-end (artigo vs. PBIX)
10. [ ] Gerar documento final pronto para publicação

---

**Próximo revisor:** Equipe técnica CGE-GO / Controladoria-Geral  
**Data alvo de resolução:** 2026-05-15

