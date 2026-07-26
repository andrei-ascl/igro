# Memoria do Projeto IGRO

Atualizado em: 2026-07-25

Este arquivo registra o estado operacional do projeto para continuidade entre sessoes.

## Objetivo do projeto

Construir, documentar e comunicar o **IGRO - Indice de Gestao de Riscos da Ouvidoria**, com foco principal em dois riscos:

- Risco 0044: atendimento fora do prazo
- Risco 0046: baixa qualidade no atendimento

## Situacao atual do repositorio

Em 2026-05-06, o projeto foi consolidado na estrutura padrao de estudos (`00_admin` a `10_publicacao`), com migracao dos conteudos legados para os caminhos atuais.

Referencias de navegacao:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `00_admin/planejamento/MAPA_MIGRACAO_ESTRUTURA_2026-05-06.md`

## Estrutura operacional atual

- `00_admin/planejamento/` -> desenho tecnico, PRD e mapa de migracao
- `00_admin/controle_versoes/` -> memoria e validacoes
- `01_referencias/` -> bibliografia, benchmarking e referencias brasileiras
- `02_dados/` -> raw, processed, external, schema
- `03_estudos/` -> metodologia, analises e validacao
- `07_dashboards/powerbi/04_powerbi_e_dax/` -> arquivos Power BI, metadata e documentacao tecnica
- `09_resultados/relatorios/` -> artigo e relatorios
- `skills/` -> skills locais do projeto

## Power BI

Local principal:

- `07_dashboards/powerbi/04_powerbi_e_dax/`

Arquivos e documentacao relevantes:

- `07_dashboards/powerbi/04_powerbi_e_dax/indice_igro.pbix`
- `07_dashboards/powerbi/04_powerbi_e_dax/indice_igro_v2.pbix`
- `07_dashboards/powerbi/04_powerbi_e_dax/documentacao_modelo_semantico_igro.md`
- `07_dashboards/powerbi/04_powerbi_e_dax/metadata/README.md`

Inventario exportado em 2026-05-01:

- 14 tabelas
- 165 colunas
- 114 medidas DAX
- 15 relacionamentos

Arquivos de metadata:

- `powerbi_info_tables_2026-05-01.csv`
- `powerbi_info_columns_2026-05-01.csv`
- `powerbi_info_measures_2026-05-01.csv`
- `powerbi_info_relationships_2026-05-01.csv`
- `dOrgao_igro_referencia_2026-05-03.csv`

Observacao importante:

- apos alteracoes de metadados feitas por ferramentas externas ou MCP, salvar o PBIX no Power BI Desktop para persistir no arquivo.
- na rodada de refinamento do infografico HTML, a estrategia passou a ser iterar primeiro no modelo conectado e sincronizar `.tmdl` apenas ao final da sessao.

Atualizacao operacional registrada em 2026-05-14:

- foi realizada auditoria do modelo semantico do IGRO com geracao de artefatos em `07_dashboards/powerbi/04_powerbi_e_dax/_review/`;
- foi criada a medida `HTML Infografico IGRO` na pasta `12 · JSON · Dashboard`;
- a medida passou por varias iteracoes visuais para representar a hierarquia `indice composto -> subindices -> KRIs`;
- foi criado o guia `07_dashboards/powerbi/04_powerbi_e_dax/ajuste_manual_subs_html_igro.md` para ajuste manual dos subindices no HTML;
- o procedimento combinado para continuidade e: ajustar primeiro no modelo conectado, validar visualmente e gerar novo `.tmdl` apenas no encerramento da rodada.

## Documentacao central

Estado atual dos documentos principais:

- `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md` -> especificacao tecnica do indice
- `00_admin/planejamento/03_especificacao_e_produto/11_PRD_IGRO.md` -> escopo, MVP, dependencias e roadmap
- `07_dashboards/powerbi/04_powerbi_e_dax/documentacao_modelo_semantico_igro.md` -> mapa do modelo Power BI
- `01_referencias/artigos/02_benchmarking_e_referencias_brasileiras/09_Benchmarking_KRIs_Ouvidorias_Estaduais.md` -> benchmarking e metas de referencia
- `01_referencias/livros/05_fontes_e_bibliografia/08_Bibliografia_Links.md` -> bibliografia principal

## Submissao do artigo

Artigo submetido em **08 de junho de 2026** para a Revista da CGU.

- Portal de acompanhamento: https://revista.cgu.gov.br/
- Arquivos submetidos: `10_publicacao/submissao/`
  - `artigo_igro_cgu_revisado_final.docx` — corpo do texto
  - `capa_anonimizada.docx` — folha de rosto
  - `tabela_suplementar_igro_51_orgaos.xlsx` — arquivo suplementar (ranking 51 orgaos)
- Checklist e guias de submissao: `10_publicacao/cgu_revista_submissao/`
- Status esperado: revisao por pares; prazo estimado ~6 meses para decisao

**Atualizacao (2026-07-16):** resultado registrado — submissao **nao aceita**. Ver `memory.md` (raiz) e `README.md` para o status atual e proximos passos (resumo executivo + novo periodico).

**Atualizacao (2026-07-25):** na reorganizacao pos-rejeicao, `artigo_igro_cgu_revisado_final.docx` foi movido de `10_publicacao/submissao/` para `10_publicacao/versao_final/`, junto com os PDFs finais. `10_publicacao/submissao/` mantem os demais arquivos originais da submissao (capa anonimizada, checklist, notas de preparacao).

## Artigo e resultados

O material do artigo e dos artefatos publicaveis passou a se concentrar principalmente em:

- `10_publicacao/submissao/`
- `04_notas_tecnicas/revisao/`
- `06_notebooks/exploracao/`
- `09_resultados/`

Estado operacional registrado em 2026-05-13:

- o artigo em desenvolvimento foi consolidado em `10_publicacao/submissao/artigo_igro_v2_critica_aplicada.md`;
- as notas criticas e de revisao foram movidas para `04_notas_tecnicas/revisao/`;
- foi criado o notebook `06_notebooks/exploracao/artigo_igro_graficos_tabelas.ipynb` para geracao de tabelas e graficos do artigo;
- o notebook foi desenhado para ler os arquivos de `02_dados/processed/`, inclusive no formato atual encapsulado em HTML/JavaScript;
- a rodada atual foi encerrada como checkpoint de preparacao analitica, pendente apenas de execucao e revisao manual antes da segunda rodada.

Observacoes metodologicas relevantes para continuidade:

- a base processada atual indica `52` orgaos, enquanto o texto do artigo menciona `51`; essa divergencia precisa ser resolvida editorial ou metodologicamente antes da versao final; **RESOLVIDO em 2026-05-26** — validado que o artigo menciona 51 orgaos consistentemente (linhas 37, 212); ver `memory.md`;
- o notebook assume, de forma explicita, que `rdp` corresponde ao indicador editorial tratado como `PMA`; essa equivalencia deve ser confirmada na revisao;
- as figuras e tabelas finais ainda dependem da execucao do notebook e da validacao visual/analitica dos resultados exportados.

## Skills disponiveis localmente

Referencias principais:

- `skills/README.md`
- `skills/powerbi-codex-skills/README.md`

Pacote novo instalado em 2026-05-06:

- `pbi-modelo-review`
- `pbi-doc`
- `pbi-dax-create`

Essas skills foram copiadas para `skills/powerbi-codex-skills/` para uso local e apoio continuo em tarefas de Power BI.

Atualizacao operacional em 2026-05-08:

- skills locais relevantes de `skills/` foram sincronizadas para `C:\Users\andre\OneDrive\Claude-Work\.agents\skills\`, que funciona como pasta global ativa do ambiente;
- a suite `powerbi-codex-skills` ativa foi revisada;
- `pbi-doc` e `pbi-modelo-review` ja estavam em variante `Rebel Analytics`;
- `pbi-dax-create` foi alinhada para o mesmo estilo, com ajuste de tom, branding e versao para `v0.2-local`, mantendo a logica operacional da skill.

## Validacoes registradas

Documentos consolidados em `00_admin/controle_versoes/`:

- `HEALTH_CHECK_2026-05-01.md`
- `PROXIMOS_PASSOS_VALIDACAO_IGRO_2026-05-01.md`
- `VALIDACAO_DAX_MEDIDAS_2026-05-01.md`
- `VALIDACAO_NOTAS_INTERNAS_2026-05-01.md`

Status ainda relevante:

- calibracao de metas ainda depende de benchmarking complementar;
- validacao de medidas DAX continua sendo um ponto de atencao quando o modelo evoluir;
- documentacao principal deve ser mantida sincronizada com qualquer mudanca estrutural.

## Proximos cuidados

- manter `README.md`, `AGENTS.md`, `CLAUDE.md` e esta memoria sincronizados quando houver mudancas relevantes;
- atualizar `documentacao_modelo_semantico_igro.md` apos mudancas estruturais no modelo;
- gerar novos exports em `metadata/` quando tabelas, colunas, medidas ou relacionamentos mudarem;
- preservar versoes datadas de relatorios, validacoes e materiais publicaveis.

## Proximo checkpoint recomendado

- acompanhar decisao editorial em https://revista.cgu.gov.br/ (prazo ~6 meses);
- responder prontamente a eventuais solicitacoes de revisao pelos pares;
- manter `09_resultados/artigo_igro_figuras_tabelas/` com os arquivos finais para referencia;
- explorar expansao do IGRO para ciclos quadrimestrais (notebook `igro_graficos_quadrimestres.ipynb` disponivel).
