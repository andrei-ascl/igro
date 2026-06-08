# CLAUDE.md

> **Contexto central:** identidade, voz, regras e marca vivem em `C:\Users\andre\OneDrive\_contexto-ia\` — leia antes de tarefas estratégicas ou de conteúdo.

Este arquivo fornece orientação operacional para Claude Code e agentes similares ao trabalhar neste repositório.

## Sobre Este Repositorio

O repositorio `igro` concentra a pesquisa, a especificacao e os artefatos tecnicos do **IGRO - Indice de Gestao de Riscos da Ouvidoria**.

O trabalho aqui e majoritariamente:

- documental;
- metodologico;
- analitico;
- orientado a Power BI e DAX.

Nao ha, em geral, aplicacao executavel, build tradicional ou suite de testes automatizados.

## Ordem de Referencia

Ao iniciar uma tarefa, seguir esta prioridade:

1. pedido explicito do usuario;
2. `AGENTS.md`;
3. `README.md`;
4. este `CLAUDE.md`;
5. documentos centrais do projeto.

## Estrutura Atual — Consolidada

A partir de **2026-05-26**, a estrutura foi consolidada removendo redundâncias. Use APENAS esta estrutura:

- `00_admin/planejamento/` → desenho técnico, PRD, cronograma
- `00_admin/controle_versoes/` → memória e registros de validação
- `01_referencias/` → benchmarking, bibliografia, documentos-base
- `02_dados/` → raw, processed, external, schema
- `03_estudos/` → metodologia, análises, validação
- `04_notas_tecnicas/` → rascunhos e versões finais
- `05_scripts/` → automações, Power Query, utilitários
- `06_notebooks/` → exploração, modelagem, prototipagem
- `07_dashboards/powerbi/04_powerbi_e_dax/` → arquivos Power BI, DAX, metadata
- `08_apresentacoes/` → slides, roteiros, pacotes de apresentação
- `09_resultados/` → relatórios, artigo, exportações
- `10_publicacao/` → versão final, anexos, submissão
- `skills/` → skills locais do projeto

**⚠️ Pastas legadas deletadas:** `04_powerbi_e_dax/`, `06_dados/`, `07_entregaveis/` foram consolidadas em 2026-05-26. Consulte `LEGACY.md` para o mapeamento completo.

## Documentos Centrais

- `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md`
- `00_admin/planejamento/03_especificacao_e_produto/11_PRD_IGRO.md`
- `07_dashboards/powerbi/04_powerbi_e_dax/documentacao_modelo_semantico_igro.md`
- `01_referencias/artigos/02_benchmarking_e_referencias_brasileiras/09_Benchmarking_KRIs_Ouvidorias_Estaduais.md`
- `01_referencias/livros/05_fontes_e_bibliografia/08_Bibliografia_Links.md`
- `00_admin/controle_versoes/MEMORIA_PROJETO.md`

## Convencoes de Trabalho

- Escrever preferencialmente em portugues brasileiro.
- Manter termos tecnicos em ingles quando fizer sentido: `KRI`, `KPI`, `PBIP`, `Power BI`, `DAX`, `Min-Max`, `Z-score`.
- Preferir Markdown para documentos editaveis.
- Evitar criar arquivos soltos na raiz sem necessidade real.
- Antes de mover ou renomear arquivos centrais, verificar referencias cruzadas.
- Ao reorganizar documentacao, preservar rastreabilidade.

## Power BI

O local principal de trabalho do modelo e:

- `07_dashboards/powerbi/04_powerbi_e_dax/`

Referencias importantes:

- `documentacao_modelo_semantico_igro.md`
- `metadata/`
- `indice_igro.pbix`
- `indice_igro_v2.pbix`

Se houver alteracoes assistidas no modelo:

- documentar claramente o que foi mudado;
- nao presumir persistencia no `.pbix` sem confirmacao;
- lembrar que metadados alterados fora do arquivo podem exigir salvamento manual no Power BI Desktop.

## Skills Relevantes

Nesta base, as skills mais uteis costumam estar em:

- `skills/README.md`
- `skills/powerbi-codex-skills/`

O pacote `powerbi-codex-skills` concentra as skills preferenciais para:

- auditoria de modelo;
- documentacao de PBIP;
- criacao de medidas DAX.

## Validacao

Como a maioria das tarefas e documental, validar com evidencias apropriadas:

- conferir caminhos e links citados;
- revisar coerencia terminologica;
- checar se os arquivos esperados existem no destino;
- deixar explicito quando algo nao foi executado ou nao pode ser validado.
