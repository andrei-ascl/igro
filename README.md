# IGRO — Índice de Gestão de Riscos da Ouvidoria

> Pipeline analítico para consolidar KRIs relacionados a riscos de atendimento (prazos e qualidade) em ouvidorias públicas, com metodologia, modelo Power BI, documentação técnica e entregáveis institucionais.

---

## Quick Start (5 min)

**Para novos colaboradores:**

1. Leia [AGENTS.md](AGENTS.md) para orientação geral
2. Explore estrutura em [Estrutura de Pastas](#estrutura-de-pastas) abaixo
3. Consulte [CLAUDE.md](CLAUDE.md) para contexto operacional
4. Comece por: `00_admin/planejamento/` → `07_dashboards/` → `09_resultados/`

**Para continuar trabalho em progresso:**

1. Verifique status atual em `00_admin/controle_versoes/MEMORIA_PROJETO.md`
2. Abra notebook: `06_notebooks/exploracao/artigo_igro_graficos_tabelas.ipynb`
3. Verifique dados processados em `02_dados/processed/`
4. Consulte resultados em `09_resultados/relatorios/` e `09_resultados/tabelas/`

---

## O que é o IGRO?

IGRO consolidida **KRIs (Key Risk Indicators)** para monitorar dois riscos principais:

- 🎯 **Risco 0044:** Atendimento fora do prazo (TMR — Tempo Médio Resposta)
- 📊 **Risco 0046:** Baixa qualidade no atendimento (RES — Resolutividade, RI — Respostas Insatisfatórias)

**Combina:**
- Pesquisa metodológica sobre índices compostos (normalização, ponderação, agregação)
- Benchmarking de KRIs em ouvidorias estaduais brasileiras
- Desenho técnico e PRD com especificação completa
- Modelo Power BI com DAX, metadata e documentação
- Relatórios, artigo científico e materiais institucionais

---

## Estado Atual

**Ponto de trabalho principal:** Artigo científico

| Item | Status | Localização |
|------|--------|-------------|
| **Artigo em desenvolvimento** | 📝 Revisão crítica | `10_publicacao/submissao/artigo_igro_v2_critica_aplicada.md` |
| **Notebook (tabelas/gráficos)** | ✅ Operacional | `06_notebooks/exploracao/artigo_igro_graficos_tabelas.ipynb` |
| **Dados processados** | ✅ Disponíveis | `02_dados/processed/` |
| **Power BI (modelo)** | ✅ v2 estável | `07_dashboards/powerbi/04_powerbi_e_dax/indice_igro_v2.pbix` |
| **Documentação técnica** | ✅ Consolidada | `07_dashboards/powerbi/04_powerbi_e_dax/documentacao_modelo_semantico_igro.md` |

**ℹ️ Observações importantes:**
- Artigo validado: consistente em 51 órgãos do Poder Executivo estadual
- Outputs analíticos do notebook armazenados em `09_resultados/relatorios/` e `09_resultados/tabelas/`
- Dados fonte processados disponíveis em `02_dados/processed/`

---

## Estrutura de Pastas

| Pasta | O quê | Mantém documentação? |
|---|---|---|
| `00_admin/planejamento/` | Desenho técnico, PRD, cronograma, mapa de migração | ✅ Sim |
| `00_admin/controle_versoes/` | Memória do projeto, validações, histórico | ✅ Sim |
| `01_referencias/` | Bibliografia, benchmarking, guias OCDE/JRC, referências normativas | ✅ Sim |
| `02_dados/` | Brutos, processados, amostras, schema, dicionário | ✅ Sim |
| `03_estudos/` | Pesquisa metodológica, análises, validações de robustez | ✅ Sim |
| `04_notas_tecnicas/` | Rascunhos, revisões, versões finais | ✅ Sim |
| `05_scripts/` | Automações, Power Query, utilitários e scripts de apoio a apresentações | — |
| `06_notebooks/` | Exploração, modelagem, prototipagem | ✅ Sim |
| `07_dashboards/powerbi/` | Power BI, DAX, metadata, documentação técnica | ✅ Sim |
| `08_apresentacoes/` | Slides, roteiros, infográficos e pacotes de apresentação | — |
| `09_resultados/relatorios/` | Relatórios finais, artigo, memorandos | ✅ Sim |
| `10_publicacao/` | Versões finais, anexos, submissão | ✅ Sim |
| `skills/` | Skills locais (powerbi-codex, goias-data-viz, etc.) | ✅ Sim |

---

## Navegação Rápida

**Para entender o projeto:**
- 📋 [Desenho Técnico](00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md) — O quê, por quê, como
- 📑 [PRD Interno](00_admin/planejamento/03_especificacao_e_produto/11_PRD_IGRO.md) — Escopo, requisitos, critérios
- 📊 [Documentação Modelo Semântico](07_dashboards/powerbi/04_powerbi_e_dax/documentacao_modelo_semantico_igro.md) — Medidas DAX, relacionamentos

**Para benchmarking e metodologia:**
- 🔍 [Benchmarking de KRIs](01_referencias/artigos/02_benchmarking_e_referencias_brasileiras/09_Benchmarking_KRIs_Ouvidorias_Estaduais.md) — Indicadores em ouvidorias estaduais
- 📚 [Bibliografia Completa](01_referencias/livros/05_fontes_e_bibliografia/08_Bibliografia_Links.md) — Fontes, OCDE/JRC, artigos

**Para acompanhamento:**
- 📝 [Memória do Projeto](00_admin/controle_versoes/MEMORIA_PROJETO.md) — Status, decisões, próximos passos
- 🗺️ [Mapa de Migração](00_admin/planejamento/MAPA_MIGRACAO_ESTRUTURA_2026-05-06.md) — Estrutura antiga vs. nova

**Para trabalhar com dados:**
- 📂 [Documentação de Dados](02_dados/README.md) — Schema, convenções, processamento
- 📓 [Estudos Metodológicos](03_estudos/README.md) — Normalização, ponderação, agregação

**Para Power BI:**
- 🔧 [Skills para Power BI](skills/README.md) — Documentação, auditoria, DAX
- 🎯 [Trabalho Principal em Power BI](07_dashboards/powerbi/) — Modelos, metadata, documentação técnica

**Para apresentações:**
- 🎞️ [Pacote de Apresentação IGRO](08_apresentacoes/entregas/pacote_apresentacao_igro/) — PPTX, notas, resumo executivo e HTML
- 🛠️ [Scripts de Apresentações](05_scripts/python/apresentacoes/) — scripts Python para gerar e atualizar os arquivos

---

## Fluxo Recomendado

Para consolidar uma release:

1. **Decisões metodológicas** → `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md`
2. **Escopo e requisitos** → `00_admin/planejamento/03_especificacao_e_produto/11_PRD_IGRO.md`
3. **Dados e validação** → `02_dados/` + `03_estudos/` (schema, processamento, robustez)
4. **Modelo e medidas** → `07_dashboards/powerbi/04_powerbi_e_dax/`
5. **Relatórios e artigos** → `09_resultados/relatorios/` + `10_publicacao/`
6. **Registro e memória** → `00_admin/controle_versoes/MEMORIA_PROJETO.md`

---

## Power BI — Local de Trabalho

**Pasta principal:** `07_dashboards/powerbi/04_powerbi_e_dax/`

| Artefato | Descrição |
|----------|-----------|
| `indice_igro_v2.pbix` | ✅ Modelo atual (stable) |
| `indice_igro_v2.pbip` | 📦 Projeto Git-first (Power BI Projects) |
| `indice_igro.pbix` | 📦 Versão anterior (referência) |
| `documentacao_modelo_semantico_igro.md` | 📋 Especificação de medidas e relacionamentos |
| `metadata/` | 🗂️ Metadados estruturados |

**Skills auxiliares:**
- [skills/powerbi-codex-skills/](skills/powerbi-codex-skills/) — Documentação, auditoria e criação de medidas DAX
- [skills/goias-data-viz/](skills/goias-data-viz/) — Identidade visual Goiás para visualizações

---

## Convenções

| Aspecto | Padrão |
|---------|--------|
| **Linguagem** | Português brasileiro para conteúdo e comentários |
| **Formato documentos** | Markdown (preferencialmente); Word e PDF para entrega institucional |
| **Versionamento** | CHANGELOG.md com Keep a Changelog format |
| **Arquivos Power BI** | `07_dashboards/powerbi/` |
| **Referências externas** | `01_referencias/` (PDFs, artigos, guias) |
| **Skills do projeto** | `skills/` (cópias locais com documentação) |
| **Documentação operacional** | `AGENTS.md`, `CLAUDE.md`, raiz do repositório |
| **Pacotes de apresentação** | `08_apresentacoes/entregas/` |
| **Scripts de apresentação** | `05_scripts/python/apresentacoes/` |

---

## Status da Documentação

| Item | Status | Localização |
|------|--------|-------------|
| README (raiz) | ✅ v2.1 | [Aqui](README.md) |
| AGENTS | ✅ Operacional | [AGENTS.md](AGENTS.md) |
| CLAUDE | ✅ Operacional | [CLAUDE.md](CLAUDE.md) |
| Estrutura de pastas | ✅ Documentada | [Acima](#estrutura-de-pastas) |
| READMEs de subpastas | 🔄 Em andamento | 02_dados/, 09_resultados/, etc. |
| llms.txt | ✅ Disponível | `llms.txt` |
| CHANGELOG.md | ✅ Disponível | `CHANGELOG.md` |
| Pacote de apresentação IGRO | ✅ Reorganizado | `08_apresentacoes/entregas/pacote_apresentacao_igro/` |

---

**Versão:** 2.2  
**Atualizado:** 2026-05-26  
**Mantido por:** Andrei Azevedo de Souza da Cunha Lima
