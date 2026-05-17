# Estudos — Pesquisa Metodológica e Validação

Concentra análises metodológicas, estudos de robustez e trilhas de validação do IGRO.

---

## Quick Start (5 min)

```bash
# 1. Entender metodologia de índices compostos
ls metodologia/pesquisa_metodologica/

# 2. Validar robustez e sensibilidade
cat metodologia/pesquisa_metodologica/05_Analise_Robustez_Sensibilidade.md

# 3. Ver análises complementares
ls analises/

# 4. Conferir validações já realizadas
find . -name "validacao*.md" -o -name "*teste*.md"
```

---

## Estrutura de Subpastas

| Pasta | Conteúdo | Tipo |
|---|---|---|
| **`metodologia/`** | Pesquisa sobre índices compostos, normalização, ponderação, agregação | 🔬 Estudos |
| **`analises/`** | Análises exploratórias, estudos de sensibilidade, comparações | 📊 Análises |
| **`validacoes/`** | Testes de robustez, critérios de validação, resultados | ✅ Testes |

---

## Documentos por Tipo

### Metodologia de Índices Compostos

Leitura sequencial (01 → 05):

| Arquivo | O quê |
|---------|-------|
| **01_Visao_Geral_Indices_Compostos.md** | Conceitos, estrutura, aplicações de índices compostos |
| **02_Normalizacao_Metodos.md** | Min-Max, Z-score, Percentil — por que normalizar |
| **03_Ponderacao_Metodos.md** | Como atribuir pesos a indicadores |
| **04_Agregacao_Metodos.md** | Fórmulas: média ponderada, PCA, outras técnicas |
| **05_Analise_Robustez_Sensibilidade.md** | Validar o índice: testes de estabilidade, sensibilidade |

### Análises Complementares

| Arquivo | Propósito |
|---------|-----------|
| **analises/correlacao_kris_ouvidoria.md** | Correlação entre TMR, RES, RI, NPS |
| **analises/comparacao_metodos_agregacao.md** | Qual método (média, PCA) funciona melhor? |
| **analises/impacto_ponderacoes.md** | Como diferentes pesos afetam o índice final? |

### Validações

| Tipo | Localização |
|------|-------------|
| **Robustez** | `validacoes/teste_robustez_igro_2026_q1.md` |
| **Sensibilidade** | `validacoes/teste_sensibilidade_ponderacoes.md` |
| **Dados** | `validacoes/validacao_dados_sgoe_2026_q1.md` |

---

## Fluxo de Pesquisa

```
Definir problema (KRIs para ouvidoria)
  ↓
Pesquisar metodologia (01 a 05)
  ↓
Propor abordagem → Desenho IGRO
  ↓
Testar com dados reais → Análises
  ↓
Validar robustez → Testes
  ↓
Documentar decisões → Memória do Projeto
```

---

## Navegação por Objetivo

**Quero aprender sobre índices compostos:**
→ Leia `metodologia/pesquisa_metodologica/` (01 a 05) em sequência

**Quero entender por que usamos Z-score:**
→ `metodologia/pesquisa_metodologica/02_Normalizacao_Metodos.md`

**Quero saber como o IGRO foi ponderado:**
→ `metodologia/pesquisa_metodologica/03_Ponderacao_Metodos.md` + `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md`

**Quero validar estabilidade do índice:**
→ `metodologia/pesquisa_metodologica/05_Analise_Robustez_Sensibilidade.md` + `validacoes/`

**Quero explorar dados:**
→ `analises/` ou `06_notebooks/` (notebooks de exploração)

---

## Convenções

✅ **Fazer:**
- Documentar toda hipótese testada, não só conclusões
- Registrar dados usados (período, órgãos, filtros)
- Manter reprodutibilidade: referência a célula de notebook ou script
- Atualizar `MEMORIA_PROJETO.md` quando conclusões forem relevantes

❌ **NÃO fazer:**
- Guardar dados brutos aqui (ficam em `02_dados/`)
- Deixar scripts/notebooks aqui (ficam em `06_notebooks/`)
- Escrever análises soltas sem contexto (contextualizar sempre)

---

## Integração com Projeto

**Alimenta:**
- `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md` (fundamentação)
- `00_admin/controle_versoes/MEMORIA_PROJETO.md` (decisões metodológicas)
- `07_dashboards/powerbi/04_powerbi_e_dax/documentacao_modelo_semantico_igro.md` (ponderações, agregações)

**Usa:**
- `02_dados/processed/` (dados para validar)
- `01_referencias/` (literatura de suporte)
- `06_notebooks/` (código de análise)

---

**Versão:** 2.0 (skill documentation-templates aplicada)  
**Atualizado:** 2026-05-16  
**Mantido por:** Pesquisador / Estatístico
