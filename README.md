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
2. Leia a [auditoria de consolidação](00_admin/controle_versoes/AUDITORIA_CONSOLIDAR_ATIVO_IGRO_2026-08-05.md), a [decisão canônica](00_admin/controle_versoes/DECISAO_CANONICA_IGRO.md) e o [contrato de métricas](00_admin/planejamento/03_especificacao_e_produto/CONTRATO_METRICAS_IGRO.md)
3. Só então abra o notebook: `06_notebooks/exploracao/artigo_igro_graficos_tabelas.ipynb`
4. Verifique dados processados em `02_dados/processed/`
5. Consulte resultados em `09_resultados/relatorios/` e `09_resultados/tabelas/`

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

> **Governança metodológica — 2026-08-10:** o perfil do Desenho Técnico foi adotado como baseline canônico de trabalho. As medidas centrais e as referências de dados do PBIP/TMDL foram alinhadas; ainda faltam o refresh no Power BI Desktop, o recálculo histórico e a reconciliação das extrações. Não trate derivados antigos como comparáveis ao novo perfil sem declarar a parametrização usada. A decisão está registrada em [DECISAO_CANONICA_IGRO.md](00_admin/controle_versoes/DECISAO_CANONICA_IGRO.md).

| Item | Status | Localização |
|------|--------|-------------|
| **Artigo científico** | Pós-submissão: não aceito pela Revista da CGU | `10_publicacao/versao_final/artigo_igro_cgu_revisado_final.docx` |
| **Notebook (tabelas/gráficos)** | ✅ Operacional | `06_notebooks/exploracao/artigo_igro_graficos_tabelas.ipynb` |
| **Tabela suplementar** | ✅ Gerada | `09_resultados/artigo_igro_figuras_tabelas/tabelas/tabela_suplementar_igro_51_orgaos.xlsx` |
| **Dados processados** | ✅ Disponíveis | `02_dados/processed/` |
| **Power BI (modelo)** | ✅ PBIP alinhado ao perfil canônico; refresh e recálculo pendentes | 07_dashboards/powerbi/04_powerbi_e_dax/indice_igro_v2.pbix |
| **Documentação técnica** | 🔄 Baseline canônico e contrato definidos; fontes físicas em reconciliação | [Contrato de métricas](00_admin/planejamento/03_especificacao_e_produto/CONTRATO_METRICAS_IGRO.md) |

**Submissão — Revista da CGU**
- Submetido em: **08 de junho de 2026**
- Resultado registrado em: **16 de julho de 2026**
- Status: **não aceito**
- Número/status detalhado da submissão: não registrado localmente
- Próximo ciclo: preparar resumo executivo/apresentação para alta gestão; depois pesquisar novo periódico para submissão.
- Arquivos de submissão e versão final: `10_publicacao/submissao/`, `10_publicacao/cgu_revista_submissao/` e `10_publicacao/versao_final/`

---

## Estrutura de Pastas

| Pasta | O quê | Mantém documentação? |
|---|---|---|
| `00_admin/planejamento/` | Desenho técnico, PRD, cronograma, mapa de migração | ✅ Sim |
| `00_admin/controle_versoes/` | Memória do projeto, validações, histórico | ✅ Sim |
| `01_referencias/` | Bibliografia, benchmarking, guias OCDE/JRC, referências normativas | ✅ Sim |
| `02_dados/` | `raw/`, `processed/`, `schema/` e dicionário; `external/` não vigente | ✅ Sim |
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
- 📌 [memory.md](memory.md) — Status estruturado e sincronizável (raiz do repositório, convenção fixa — nunca mover para subpasta)
- 📝 [Memória do Projeto](00_admin/controle_versoes/MEMORIA_PROJETO.md) — Histórico narrativo, decisões, próximos passos
- 🧭 [Auditoria do ativo](00_admin/controle_versoes/AUDITORIA_CONSOLIDAR_ATIVO_IGRO_2026-08-05.md) — Evidências, derivados e bloqueadores
- ⚖️ [Decisão canônica](00_admin/controle_versoes/DECISAO_CANONICA_IGRO.md) — Baseline metodológico e parâmetros aprovados no projeto
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

1. **Auditoria e decisão canônica** → `00_admin/controle_versoes/` + [contrato de métricas](00_admin/planejamento/03_especificacao_e_produto/CONTRATO_METRICAS_IGRO.md)
2. **Decisões metodológicas** → `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md`
3. **Escopo e requisitos** → `00_admin/planejamento/03_especificacao_e_produto/11_PRD_IGRO.md`
4. **Dados e validação** → `02_dados/` + `03_estudos/` (schema, processamento, robustez)
5. **Modelo e medidas** → `07_dashboards/powerbi/04_powerbi_e_dax/`
6. **Relatórios e artigos** → `09_resultados/relatorios/` + `10_publicacao/`
7. **Registro e memória** → `00_admin/controle_versoes/MEMORIA_PROJETO.md`

---

## Power BI — Local de Trabalho

**Pasta principal:** `07_dashboards/powerbi/04_powerbi_e_dax/`

| Artefato | Descrição |
|----------|-----------|
| `indice_igro_v2.pbix` | ✅ Modelo atual (stable); fórmula ainda não canônica |
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
| README (raiz) | ✅ v2.5 | [Aqui](README.md) |
| AGENTS | ✅ Operacional | [AGENTS.md](AGENTS.md) |
| CLAUDE | ✅ Operacional | [CLAUDE.md](CLAUDE.md) |
| Estrutura de pastas | ✅ Documentada | [Acima](#estrutura-de-pastas) |
| READMEs de subpastas | 🔄 Em andamento | 02_dados/, 09_resultados/, etc. |
| llms.txt | ✅ Disponível | `llms.txt` |
| CHANGELOG.md | ✅ Disponível | `CHANGELOG.md` |
| Pacote de apresentação IGRO | ✅ Reorganizado | `08_apresentacoes/entregas/pacote_apresentacao_igro/` |

---

**Versão:** 2.5  
**Atualizado:** 2026-08-05
**Mantido por:** Andrei Azevedo de Souza da Cunha Lima
