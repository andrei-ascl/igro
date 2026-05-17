# Dashboards — Power BI e Visualizações

Concentra modelos Power BI, documentação técnica de medidas DAX e assets de visualização.

---

## Quick Start (5 min)

```bash
# 1. Abrir modelo Power BI
open powerbi/04_powerbi_e_dax/indice_igro_v2.pbix

# 2. Consultar documentação técnica
cat powerbi/04_powerbi_e_dax/documentacao_modelo_semantico_igro.md

# 3. Entender medidas DAX
cat powerbi/04_powerbi_e_dax/dax_enterprise_guide_basedadosouvidoria.md

# 4. Referenciar padrões (ponderação, agregação)
cat powerbi/04_powerbi_e_dax/medidas_dax_snake_case_camadas.md
```

---

## Estrutura de Subpastas

| Pasta | Conteúdo | Status |
|---|---|---|
| **`powerbi/04_powerbi_e_dax/`** | Modelos `.pbix`, documentação DAX, metadata | 🎯 Principal |
| **`powerbi/metadata/`** | Estrutura de dados, relacionamentos, tabelas | 📋 Descritivo |

---

## Arquivo Power BI Principal

| Arquivo | Versão | Status |
|---------|--------|--------|
| **`indice_igro_v2.pbix`** | v2 (atual) | ✅ Stable |
| **`indice_igro.pbix`** | v1 (referência) | 📦 Archive |

---

## Documentação Técnica

### Documentação Principal

| Arquivo | Propósito | Leitura |
|---------|-----------|---------|
| **`documentacao_modelo_semantico_igro.md`** | Especificação completa: tabelas, colunas, relacionamentos, medidas | 📖 Essential |
| **`dax_enterprise_guide_basedadosouvidoria.md`** | Guia DAX: padrões, convenções, boas práticas | 📖 Essential |
| **`medidas_dax_snake_case_camadas.md`** | Catálogo de medidas: nomes, fórmulas, camadas | 📋 Reference |
| **`nota_referencia_dax_obsidian.md`** | Notas rápidas: snippets, padrões comuns | 💡 Quick Ref |
| **`kit_comandos_mcp_powerbi.md`** | Comandos e scripts auxiliares para Power BI | 🔧 Tools |

### Estrutura de Metadata

```
metadata/
├── tabelas_fatos_dimensoes.md      # Star schema do IGRO
├── relacionamentos.md               # Relacionamentos entre tabelas
├── hierarquias.md                  # Hierarquias (período, órgão, tipo)
└── metricas_kri.md                 # Especificação de TMR, RES, RI, NPS
```

---

## Navegação por Objetivo

**Quero entender a estrutura do modelo:**
→ `documentacao_modelo_semantico_igro.md` (seções 1-3)

**Quero consultar uma medida DAX específica:**
→ `medidas_dax_snake_case_camadas.md` (catálogo)

**Quero criar nova medida DAX:**
→ `dax_enterprise_guide_basedadosouvidoria.md` (padrões e convenções)

**Quero saber a ponderação do IGRO:**
→ `documentacao_modelo_semantico_igro.md` (seção "Cálculo do Índice") ou `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md`

**Quero validar relacionamentos:**
→ `metadata/relacionamentos.md` ou abrir o modelo em Power BI Desktop

---

## Estrutura de Dados (Star Schema)

```
Tabelas Fato:
├── Fato_Manifestacoes (id_manifestacao, pk)
└── Fato_Indicadores (id_indicador, valor, data)

Dimensões:
├── Dim_Tempo (data, período, trimestre, ano)
├── Dim_Orgao (id_orgao, nome, tipo, hierarquia)
├── Dim_Tipo_Manifestacao (id_tipo, nome, categoria)
├── Dim_Segmento (id_segmento, categoria)
└── Dim_KRI (id_kri, nome, fórmula, unidade)

Agregações:
├── KRI_TMR (Tempo Médio Resposta em dias)
├── KRI_RES (Resolutividade em %)
├── KRI_RI (Respostas Insatisfatórias em %)
├── KRI_NPS (Net Promoter Score de -100 a +100)
└── IGRO (Índice Gestão Risco Ouvidoria: 0-100)
```

---

## Convenções

✅ **Fazer:**
- Medidas em snake_case: `kri_tmr_dias`, `igro_score`
- Documentar toda medida nova em `documentacao_modelo_semantico_igro.md`
- Atualizar `MEMORIA_PROJETO.md` quando alterar schema/relacionamentos
- Testar medida com amostra de dados antes de publicar
- Manter backup de versão anterior antes de mudanças grandes

❌ **NÃO fazer:**
- Hardcoded valores em medidas DAX (usar parâmetros)
- Medidas não-documentadas
- Alterar schema sem revisar impacto em outras medidas
- Sobrescrever `.pbix` sem versionamento

---

## Fluxo de Atualização

```
1. Nova base em 02_dados/processed/
2. Importar em Power BI Desktop
3. Validar relacionamentos
4. Revisar medidas (atualizar se necessário)
5. Testar saídas (gráficos, valores)
6. Documentar mudanças em documentacao_modelo_semantico_igro.md
7. Registrar em MEMORIA_PROJETO.md
8. Salvar como indice_igro_v2.pbix
9. Exportar gráficos para 09_resultados/
```

---

## Skills Auxiliares

Disponíveis em `skills/`:

| Skill | Utilidade |
|-------|----------|
| **powerbi-codex-skills** | Documentação PBIP, auditoria de modelo, criação de medidas |
| **goias-data-viz** | Identidade visual Goiás para gráficos, cores, tipografia |

---

## Integração com Projeto

**Consome:**
- `02_dados/processed/` — dados para importar
- `03_estudos/metodologia/` — fundamentação de ponderações
- `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md` — especificação

**Produz:**
- Visualizações para `09_resultados/artigo_igro_figuras_tabelas/` (exports)
- Documentação técnica para `00_admin/`

---

**Versão:** 2.0 (skill documentation-templates aplicada)  
**Atualizado:** 2026-05-16  
**Mantido por:** Especialista em Power BI / Business Analyst
