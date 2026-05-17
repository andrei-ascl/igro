# Changelog — IGRO Índice de Gestão de Riscos da Ouvidoria

Todas as mudanças importantes neste projeto estão documentadas aqui.
Formato: [Keep a Changelog](https://keepachangelog.com/)

---

## [Unreleased]

### Added
- `llms.txt` — Índice amigável para IA (Core Objective, Critical Files, Key Concepts, Quick Start)
- `CHANGELOG.md` — Rastreamento de versões (Keep a Changelog format)
- READMEs atualizados com skill documentation-templates (00_admin/, 01_referencias/, 02_dados/, 03_estudos/, 06_notebooks/, 07_dashboards/, 09_resultados/)
- Status de documentação consolidado em README.md

### Changed
- `README.md` — Reformulado com Quick Start, O que é o IGRO, Estrutura de Pastas, Navegação Rápida, Fluxo Recomendado
- Convenções documentadas em cada pasta README
- Troncos de subpastas agora linkados ao README principal

### Planned
- Artigo final em 10_publicacao/submissao/ (após revisão crítica)
- Validação de órgãos (52 vs. 51 mencionado)
- Entrega pós-Prêmio das Ouvidorias (2026-05-23)

---

## [1.0.0] — 2026-05-16

### Status
Operacional com estrutura consolidada e documentação integral.

### Added
- Estrutura de pastas (00_admin a 10_publicacao) + skills/
- Notebook principal: `06_notebooks/exploracao/artigo_igro_graficos_tabelas.ipynb`
- Referências: artigos sobre KRIs, benchmarking ouvidorias, OCDE/JRC
- Dados: schema de SGOe, dicionário de campos, amostras
- Scripts: Power Query, utilitários Python, estilos Goiás
- Documentação principal:
  - `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md`
  - `00_admin/planejamento/03_especificacao_e_produto/11_PRD_IGRO.md`
  - `07_dashboards/powerbi/04_powerbi_e_dax/documentacao_modelo_semantico_igro.md`
  - `01_referencias/artigos/02_benchmarking_e_referencias_brasileiras/09_Benchmarking_KRIs_Ouvidorias_Estaduais.md`

### Documentation
- `README.md` — Guia de entrada para colaboradores
- Mapa de migração de estrutura (00_admin/)
- Memória do projeto e cronograma (00_admin/controle_versoes/)
- Pesquisa metodológica sobre índices compostos (03_estudos/metodologia/)
- Instruções para Power BI (07_dashboards/)

### Notes
- Estrutura permite reelaboração com novas extrações SGOe
- Rastreabilidade completa: dados → cálculos (notebook) → Power BI → artigo
- Tema Goiás aplicado em todos os gráficos (seaborn style)
- Validações de robustez documentadas (Z-score, ponderações, testes)

---

## [0.5.0] — 2026-05-05

### Status
Estrutura em construção. Notebook esqueleto pronto.

### Added
- Pasta base com 11 categorias (00_admin … 10_publicacao + skills/)
- Notebook esqueleto com células: setup, load, clean, calculate, plot, export
- Estilo visual Goiás pronto (`goias_seaborn_style.py`)
- Planejamento inicial em `00_admin/`
- Documentação base (README, ARVORE)
- Power BI: modelo v1 com medidas iniciais

### In Progress
- Preenchimento de dados em 02_dados/processed/
- Testes do notebook principal
- Validação completa de metodologia

---

## [0.1.0] — 2026-05-01

### Status
Iniciação. Ideia aprovada pelo comitê.

### Added
- Repositório criado em `Claude-Work/Projects/igro/`
- Objetivo definido: criar índice composto para monitorar riscos de ouvidoria (TMR, RES, RI, NPS)
- Escopo: pesquisa metodológica + modelo Power BI + documentação + artigo

### Notes
- Origem: Prêmio das Ouvidorias 2026 (necessidade de demonstrar expertise em indicadores)
- Visão: pipeline reproduzível com nova extração SGOe

---

## Convenção de Versionamento

- **[X.Y.Z]** — Semantic Versioning
  - X = Mudança estrutural (nova pasta, novo fluxo, reescrita do escopo)
  - Y = Novo recurso ou melhoria (novo gráfico, nova métrica, documentação expandida)
  - Z = Correção ou ajuste menor (typo, fórmula refinada, documentação corrigida)

- **[Unreleased]** — Mudanças na branch atual não lançadas ainda

- **Status descritivo:** Iniciação / Em Construção / Operacional / Congelado / Descontinuado

---

## Como Usar Este Changelog

**Para colaboradores:**
1. Ao adicionar um recurso, atualize `## [Unreleased]` → `### Added`
2. Ao corrigir bug, atualize `## [Unreleased]` → `### Fixed`
3. Ao mudar comportamento, atualize `## [Unreleased]` → `### Changed`

**Para gestores:**
1. Ver últimas mudanças: Verifique `## [Unreleased]`
2. Ver versão anterior: Verifique `## [X.Y.Z]` mais recente
3. Ver histórico: Leia para trás (mudanças mais antigas)

**Quando lançar nova versão:**
1. Mude `## [Unreleased]` para `## [X.Y.Z] — YYYY-MM-DD`
2. Adicione nova seção `## [Unreleased]` vazia
3. Comite com mensagem: "Release X.Y.Z"

---

## Integração com Documentação

Este changelog é lido por:
- `README.md` — Referencia status atual
- `00_admin/controle_versoes/MEMORIA_PROJETO.md` — Consulta para próximos passos
- `00_admin/planejamento/MAPA_MIGRACAO_ESTRUTURA_2026-05-06.md` — Rastreia marcos

Mantenha em sincronia (revisar juntos na próxima atualização de documentação).

---

**Mantido por:** Andrei Azevedo de Souza da Cunha Lima  
**Política:** Atualizar a cada mudança estrutural ou versão nova  
**Última atualização:** 2026-05-16
