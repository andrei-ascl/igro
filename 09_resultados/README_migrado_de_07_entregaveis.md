# Resultados — Entregáveis Finais

Organiza relatórios, tabelas, gráficos e exportações finalizadas do projeto IGRO.

---

## Quick Start (5 min)

```bash
# 1. Encontrar resultado específico
ls relatorios/
ls artigo_igro_figuras_tabelas/

# 2. Acessar última versão
cat relatorios/memoria_trabalho_proximos_passos.md

# 3. Exportar para apresentação/publicação
# Copiar de aqui para 10_publicacao/
```

---

## Estrutura de Entregáveis

| Subpasta | Conteúdo | Status |
|----------|----------|--------|
| **`relatorios/`** | Relatórios técnicos, notas finais, memória de trabalho | 📝 Vivo |
| **`artigo_igro_figuras_tabelas/`** | Tabelas e gráficos do artigo científico (saída do notebook) | 📊 Regenerado |
| **`apresentacoes/`** | Slides finais para reuniões, GT Riscos, Alta Gestão | 🎯 Conforme demanda |
| **`exports_powerbi/`** | PDFs, imagens, planilhas exportadas do dashboard | 📥 Ad-hoc |

---

## O que Há em Cada Pasta

### `relatorios/`

| Arquivo | Descrição |
|---------|-----------|
| `memoria_trabalho_proximos_passos.md` | 📝 Log vivo: o que foi feito, próximas ações, decisões |
| `artigo_igro_v2_critica_aplicada.md` | 📄 Artigo científico (versão em desenvolvimento) |
| `notas_tecnicas_igro_*.md` | 📋 Notas técnicas e explicativas |
| `relatorio_artigo_*.pdf` | 📑 Versão PDF formatada (quando finalizar) |

### `artigo_igro_figuras_tabelas/`

Saída automática do notebook `06_notebooks/exploracao/artigo_igro_graficos_tabelas.ipynb`

| Tipo | Exemplo |
|------|---------|
| **Tabelas** | `tabela_kri_por_orgao_2026_q1.csv` |
| **Gráficos** | `figura_01_evolucao_nps_temporal.png` (300 dpi) |
| **Índices** | `indice_igro_consolidado.xlsx` |

---

## Fluxo de Trabalho

```
02_dados/processed/
  ↓ [Notebook lê]
06_notebooks/exploracao/artigo_igro_graficos_tabelas.ipynb
  ↓ [Executa: calcula, cria tabelas, plota gráficos]
09_resultados/artigo_igro_figuras_tabelas/ [Saída]
  ↓
[Insere em relatório/artigo]
  ↓
relatorios/artigo_igro_v2_critica_aplicada.md
  ↓
[Aprova e finaliza]
  ↓
10_publicacao/ [Versão final para submissão/entrega]
```

---

## Convenções

✅ **Fazer:**
- Manter versões de trabalho em `04_notas_tecnicas/rascunho/` enquanto em revisão
- Registrar data, público-alvo e fonte de dados quando aprove versão
- Nomes claros com data: `artigo_igro_v2_2026_05_16.md`
- Tabelas e gráficos sempre com metadata (período, órgãos inclusos, filtros)
- Atualizar `memoria_trabalho_proximos_passos.md` regularmente

❌ **NÃO fazer:**
- Guardar versões de trabalho aqui (use `04_notas_tecnicas/`)
- Deixar originais sem documentação de origem/filtros
- Publicar direto sem passar por 10_publicacao/
- Sobrescrever arquivos sem versão anterior (manter histórico)

---

## Checklist para Resultados Finais

Antes de considerar um resultado "pronto":

- [ ] Arquivo nomeado com data (YYYY-MM-DD)
- [ ] Metadata documentada (período, órgãos, filtros, data_extracao)
- [ ] Tabelas com headers claros, sem NULL não documentado
- [ ] Gráficos com resolução 300 dpi, legenda completa, fonte citada
- [ ] Números verificados: amostra vs. população
- [ ] Revisão gramatical/técnica completada
- [ ] Pronto para copiar a `10_publicacao/`

---

## Integração com Projeto

| Origem | Consome de | Produz para |
|--------|-----------|-------------|
| Notebook `06_notebooks/` | `02_dados/processed/` | `artigo_igro_figuras_tabelas/` |
| Relatório `04_notas_tecnicas/` | `artigo_igro_figuras_tabelas/` | `relatorios/` |
| Publicação | `relatorios/` | `10_publicacao/` |
| Apresentações | Qualquer subpasta acima | `apresentacoes/` |

---

**Versão:** 2.0 (skill documentation-templates aplicada)  
**Atualizado:** 2026-05-16  
**Mantido por:** Analista/Auditor de Qualidade
