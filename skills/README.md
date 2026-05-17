# Skills do Projeto IGRO

Esta pasta guarda uma copia local das skills mais uteis para desenvolver o IGRO. A ideia e facilitar o trabalho com agentes mantendo, dentro do proprio projeto, os fluxos mais relevantes para metodologia, planilhas, Power BI, relatorios e evolucao futura.

## Uso Imediato

| Skill | Utilidade no IGRO |
|---|---|
| `powerbi-codex-skills` | Pacote local com 3 skills para Power BI: documentar modelo PBIP, auditar qualidade do modelo e criar medidas DAX com base na estrutura existente. |
| `goias-data-viz` | Criar visualizacoes profissionais usando identidade visual do Governo de Goias; util para graficos do dashboard, relatorios gerenciais e materiais de apresentacao. |
| `xlsx` | Apoiar o MVP Excel-first previsto no PRD: planilhas auditaveis, formulas, abas de calculo, validacao, formatacao e graficos. |
| `pdf` | Ler, extrair texto/tabelas e processar PDFs de referencia, como o Handbook OCDE/JRC e guias metodologicos. |
| `docx` | Criar ou editar documentos Word, como notas tecnicas, relatorios formais e versoes para circulacao institucional. |
| `pptx` | Criar, revisar ou editar apresentacoes PowerPoint sobre o IGRO para GT Riscos, Comite Setorial ou alta gestao. |
| `gerador-slides` | Transformar documentos longos do IGRO em roteiros de slides mais visuais e objetivos. |
| `prd-manager` | Revisar, melhorar e manter o PRD do IGRO, especialmente escopo, requisitos, criterios de aceite e roadmap. |
| `doc-coauthoring` | Apoiar escrita colaborativa de documentos estruturados: desenho tecnico, especificacoes, notas de decisao e propostas. |
| `academic-paper-summarizer` | Resumir artigos cientificos e referencias metodologicas sobre indices compostos, KRIs, indicadores publicos e robustez. |
| `revisor-gramatical` | Revisar textos em portugues para publicacao ou compartilhamento institucional, preservando Markdown e estilo do autor. |
| `documentation-templates` | Melhorar README, documentacao tecnica, especificacoes e registros de decisao do projeto. |

## Uteis em Fases Futuras

| Skill | Quando usar |
|---|---|
| `api-patterns` | Quando o IGRO evoluir para uma integracao automatizada com APIs do SGOe ou outros sistemas. |
| `database-design` | Quando houver necessidade de armazenar historico dos KRIs, series quadrimestrais, metadados de extracao ou auditoria dos calculos. |
| `architecture` | Para tomar decisoes de arquitetura se o projeto sair do MVP Excel/Power BI e virar pipeline, aplicacao ou produto interno. |
| `software-architecture` | Complementar a `architecture` em discussoes mais amplas de desenho de sistema, modularizacao e evolucao tecnica. |
| `plan-writing` | Planejar fases de implementacao com tarefas pequenas, dependencias e criterios de verificacao. |
| `webapp-testing` | Testar uma eventual aplicacao web ou dashboard proprio, caso o IGRO evolua alem do Power BI. |
| `frontend-design` | Projetar uma interface web propria para consulta do IGRO, caso essa frente seja aberta no futuro. |
| `design-system` | Definir padroes visuais e componentes reutilizaveis se o projeto ganhar interfaces ou materiais digitais recorrentes. |

## Convencao

- Cada skill fica em uma subpasta propria.
- O arquivo principal de cada skill deve ser `SKILL.md`.
- Foram copiadas apenas as skills principais; subpastas duplicadas como `.agents` e `.claude` foram deixadas de fora para evitar peso e redundancia.
- Skills especificas do IGRO podem ser criadas aqui no futuro, por exemplo `igro-metodologia`, `igro-powerbi` e `igro-relatorio`.
- O pacote `powerbi-codex-skills/` agrega multiplas skills especializadas e deve ser tratado como conjunto funcional, nao como skill unica.
