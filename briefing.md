# Briefing — IGRO

## Finalidade

O IGRO (Índice de Gestão de Riscos da Ouvidoria) consolida KRIs para monitorar
riscos de atendimento em ouvidorias públicas, combinando metodologia,
dados, modelo Power BI, documentação técnica e entregáveis institucionais.

## Escopo confirmado

- Pesquisa e especificação metodológica do índice.
- Preparação e validação de dados, com rastreabilidade de fontes, períodos,
  universo, denominadores e regra amostral.
- Modelo Power BI, medidas DAX, metadata e documentação do modelo semântico.
- Relatórios, artigo, apresentações e materiais de publicação derivados do
  perfil metodológico adotado.

## Público e entregáveis

O núcleo atende o mantenedor do projeto, revisores metodológicos e os
destinatários institucionais dos relatórios e apresentações de gestão de
riscos. As saídas incluem tabelas, gráficos, documentação técnica, relatórios,
apresentações e versões de publicação, conforme o fluxo descrito no
`README.md`.

## Fontes canônicas de trabalho

- `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md` —
  desenho técnico e perfil metodológico.
- `00_admin/planejamento/03_especificacao_e_produto/11_PRD_IGRO.md` — escopo e
  requisitos.
- `00_admin/planejamento/03_especificacao_e_produto/CONTRATO_METRICAS_IGRO.md`
  — parâmetros, proveniência, pré-condições e gates de qualidade.
- `00_admin/controle_versoes/DECISAO_CANONICA_IGRO.md` — decisão metodológica e
  dependências institucionais.
- `07_dashboards/powerbi/04_powerbi_e_dax/documentacao_modelo_semantico_igro.md`
  — medidas, relacionamentos e documentação operacional do modelo.

## Fluxo de trabalho

1. Auditar fontes e registrar a decisão canônica.
2. Conferir escopo, requisitos, período, universo e regra amostral.
3. Preparar dados e validações em `02_dados/` e `03_estudos/`.
4. Atualizar notebooks, modelo Power BI e documentação técnica somente quando
   a tarefa autorizar.
5. Gerar e revisar resultados em `09_resultados/`.
6. Preparar publicação e apresentação em `10_publicacao/` e
   `08_apresentacoes/`.
7. Registrar estado e próximos passos em `memory.md` e na memória narrativa,
   sem usar esses arquivos como substitutos da decisão canônica.

## Estado no corte desta revisão

O perfil do Desenho Técnico foi adotado como baseline canônico de trabalho em
2026-08-10. A confirmação do gate desta revisão — PBIP/TMDL alinhado e refresh
validado — foi dada pelo usuário em 2026-09-18 e está registrada no plano de
revisão em `%USERPROFILE%\OneDrive\Claude-Work\Projects\auditoria-governanca-nucleos\docs\planos\2026-09-18-plano-revisao-nucleos-em-ondas.md`.

O `README.md`, `memory.md` e a decisão canônica ainda contêm referências
históricas a refresh, recálculo ou validações pendentes. Esses documentos não
foram reescritos neste lote; qualquer consolidação textual futura deve
reconciliar explicitamente essa divergência.

## Fronteiras

- Não tratar derivados antigos como comparáveis ao perfil canônico sem declarar
  a parametrização usada.
- Não assumir que um `.pbix`, `.pbip`, `.tmdl` ou metadata pode ser alterado
  com segurança sem autorização específica.
- Não inventar metas, goalposts, fontes, resultados ou decisões institucionais
  para preencher lacunas.
- Para instruções de operação e limites, seguir `AGENTS.md`; para estado
  volátil, consultar `memory.md`; para decisões estruturais futuras, consultar
  `decisoes.md`.
