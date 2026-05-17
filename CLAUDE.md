# CLAUDE.md

This file provides operational guidance to Claude Code and similar agents when working in this repository.

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

## Estrutura Atual Relevante

Usar a estrutura atual do projeto, e nao a estrutura antiga pre-migracao:

- `00_admin/planejamento/` -> desenho tecnico, PRD, mapa de migracao
- `00_admin/controle_versoes/` -> memoria e registros de validacao
- `01_referencias/` -> benchmarking, bibliografia e documentos-base
- `02_dados/` -> raw, processed, external, schema
- `03_estudos/` -> metodologia, analises e validacao
- `07_dashboards/powerbi/04_powerbi_e_dax/` -> arquivos Power BI, DAX, metadata e documentacao tecnica
- `09_resultados/relatorios/` -> relatorios e artigo em desenvolvimento
- `skills/` -> skills locais do projeto

Se encontrar referencias para pastas antigas como `04_powerbi_e_dax/` ou `07_entregaveis/`, tratar isso como legado documental e priorizar os caminhos novos.

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
