# Mapa de Migracao da Estrutura do IGRO

## Objetivo

Registrar como a estrutura original do projeto IGRO foi alinhada ao modelo padrao de estudos.

## Movimentos aplicados

- `01_pesquisa_metodologica` -> `03_estudos/metodologia/01_pesquisa_metodologica`
- `02_benchmarking_e_referencias_brasileiras` -> `01_referencias/artigos/02_benchmarking_e_referencias_brasileiras`
- `03_especificacao_e_produto` -> `00_admin/planejamento/03_especificacao_e_produto`
- `04_powerbi_e_dax` -> `07_dashboards/powerbi/04_powerbi_e_dax`
- `05_fontes_e_bibliografia` -> `01_referencias/livros/05_fontes_e_bibliografia`
- Conteudo de `06_dados/01_brutos` -> `02_dados/raw`
- Conteudo de `06_dados/02_tratados` -> `02_dados/processed`
- Conteudo de `06_dados/03_amostras` -> `02_dados/external/03_amostras`
- Conteudo de `07_entregaveis/01_relatorios` -> `09_resultados/relatorios`
- Conteudo de `07_entregaveis/02_apresentacoes` -> `08_apresentacoes/slides`
- Conteudo de `07_entregaveis/03_exports_powerbi` -> `09_resultados/exportacoes/03_exports_powerbi`
- Documentos de memoria e validacao da raiz -> `00_admin/controle_versoes`
- `04_powerbi_e_dax/indice_igro_v2.pbix` -> `07_dashboards/powerbi/04_powerbi_e_dax/indice_igro_v2.pbix`
- `06_dados/README.md` -> `02_dados/README_migrado_de_06_dados.md`
- `07_entregaveis/README.md` -> `09_resultados/README_migrado_de_07_entregaveis.md`

## Itens preservados na raiz

- `CLAUDE.md`
- `settings.local.json`
- `skill.md`
- `skills/`
- `README.md`

## Observacoes

- A migracao foi conservadora: somente itens com encaixe claro foram movidos.
- Pastas antigas vazias podem permanecer como referencia temporaria.
- O modelo padrao foi criado pelo script `criar_estrutura_estudo.py`, executado apontando para a propria pasta `igro`.
- As pastas vazias remanescentes da estrutura anterior foram removidas ao final da migracao.
