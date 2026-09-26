---
board_sync: true
board_item: "IGRO"
hub: "CGE"
state: "active"
phase: "pós-submissão — fonte comum TMDL e correção do painel IGRO validadas no Desktop; mockup da Análise Setorial aprovado"
next_action: "Implementar filtros temporais e a Análise Setorial no PBIP; depois recalcular resultados históricos e obter as validações institucionais pendentes"
deadline: null
progress: 87
meta: "Artigo não aceito; as três tabelas fato selecionam uma rodada comum priorizando o Hub; usuário confirmou o refresh após o reapontamento e verificou o painel IGRO corrigido no Desktop em 2026-09-26; implementação da Análise Setorial, recálculo histórico e validação institucional pendentes"
updated: "2026-09-26"
---

# Memory — igro

**Última atualização:** 2026-09-26

---

## Status Geral

| Campo | Valor |
|-------|-------|
| **Projeto** | igro |
| **Status** | Em andamento (artigo submetido à Revista da CGU e não aceito; reposicionamento em curso) |
| **Progresso** | 87% (base metodológica e artigo completos; nova etapa de comunicação executiva e submissão) |
| **Próximo marco** | Resultados históricos recalculados e comparados com os derivados antigos |
| **Bloqueadores** | Recálculo histórico; validação formal de metas e goalposts pelo GT de Gestão de Riscos; aprovação da inclusão na Matriz pelo Comitê Setorial |

---

## Indicadores

| Indicador | Valor | Tendência | Meta |
|-----------|-------|-----------|------|
| Progresso (%) | 87 | ↑ Crescente | Reaproveitamento executivo + nova submissão |
| Última Entrega | Submissão à Revista da CGU | Concluída | Artigo não aceito |
| Próxima Entrega | Resumo executivo/apresentação para alta gestão | Planejada | Definir narrativa executiva e próximos veículos |

---

## Contexto e Notas

### Atividade Recente
- **2026-09-26 (painel IGRO):** `_JSON Orgaos` passou a iterar a dimensão institucional; os cartões da rede usam as medidas canônicas; amostras insuficientes permanecem como `null`/“Sem cálculo” e não entram no ranking. A revisão estática não encontrou bloqueadores e o usuário abriu o PBIP no Desktop e confirmou que o painel estava correto. A confirmação visual não registrou o ID carregado nem as contagens das três tabelas.
- **2026-09-26 (fonte TMDL):** `f_relatorio`, `f_pesquisa` e `f_insatisfatorias` selecionam um único ID comum, priorizando `sgoe_hub/data/processed/` e mantendo o fallback local. O usuário confirmou o refresh após o reapontamento; o Hub não emitirá novas cópias de compatibilidade do IGRO.
- **2026-09-26 (checagem pré-refresh, checkpoint superado):** não foi identificado processo de ETL e os Parquets da rodada `2026-09-26T1626` e o manifesto ficaram estáveis em duas verificações. Naquele momento o Desktop não estava aberto; a validação posterior está registrada acima.
- **2026-09-26:** reconciliado o estado com o gate humano registrado em 2026-09-18: PBIP/TMDL alinhado e refresh validado. Permanecem pendentes a implementação dos filtros temporais e do painel Análise Setorial, o recálculo/comparação dos resultados históricos e as validações institucionais previstas na decisão canônica.
- **2026-09-22:** revisão de memória confirmou o estado pós-submissão e o mockup da Análise Setorial; detectada atividade no PBIP (28/08, 7ª página criada no relatório e cache do SemanticModel atualizado) e depósito da base `relatorio_2026-08-31.parquet`; governança alinhada com AGENTS.md, briefing.md e decisoes.md.
- **2026-08-28:** sessão no Power BI Desktop adicionou uma 7ª página ao relatório (`Página 1`) e atualizou os metadados/cache do modelo PBIP.
- **2026-08-22:** criado, revisado e salvo o mockup da página `Análise setorial` em `07_dashboards/powerbi/04_powerbi_e_dax/_mockups/analise_setorial_mockup.html`. A revisão reforçou a hierarquia do IGRO, substituiu barras heterogêneas por mini-cards de evidência, ampliou microtextos, padronizou rótulos, destacou a exceção de 18,4% acima de 30 dias contra referência de 10% e reservou laranja para alertas. O mockup foi aprovado para continuidade; o PBIP não foi alterado.
- **2026-08-21:** criada a medida `HTML Evolucao Quadrimestral IGRO` — painel único com `idx_igro`, `idx_igro_sub_t` e `idx_igro_sub_q` em três gráficos de linha empilhados sobre eixo de tempo comum, escala vertical calculada dos dados, quadrimestre em curso tracejado. Gravada no TMDL; falta abrir o Desktop, validar e posicionar na página EVOLUÇÃO IGRO. Fonte legível em `07_dashboards/powerbi/04_powerbi_e_dax/medida_html_evolucao_quadrimestral.dax`. Na mesma rodada: sete medidas de data de atualização (`dt_ultima_atualizacao_dados` + seis `html_rodape_*`) e saneamento dos identificadores — seis `lineageTag` malformados criados na rodada, mais um pré-existente em `idx_igro_sub_q` (truncado em 11 caracteres). O modelo fechou com 300 `lineageTag`, nenhum malformado, nenhum duplicado.
- **2026-08-21 (achado):** a paleta do infográfico reprovava em acessibilidade cromática — `#f5b11f` (Sub-T) e `#e99020` (Sub-Q) a ΔE 8,4 em visão normal, piso 15; 7,5 sob deuteranopia. Substituída por `#0891b2` / `#c2410c` / `#6d28d9` no painel novo. **O infográfico e o dashboard antigos ainda usam a paleta reprovada.**
- **2026-08-05:** auditoria consolidar-ativo identificou três perfis metodológicos e lacunas na documentação de dados. Foram registrados a auditoria, a decisão canônica e o contrato de métricas.
- **2026-08-10:** referências quebradas do PBIP/TMDL foram corrigidas para 06_dados/01_brutos, com seleção do Parquet mais recente por prefixo; o Power BI Desktop deve ser reaberto apenas para refresh e salvamento.
- **2026-08-10:** o PBIP foi atualizado de compatibilityLevel 1600 para 1606, compatível com o Power BI Desktop 2.156.951.0.
- **2026-08-10:** a medida HTML Infografico IGRO foi reorganizada com cabeçalho institucional, resumo hierárquico, grade de KRIs 3+2, status textual acessível e tratamento de valores sem amostra como —.
- **2026-07-25:** base analítica expandida como preparação para o resumo executivo — análise de sensibilidade e gráficos por quadrimestre exportados, tabela suplementar (ranking completo dos 51 órgãos) gerada. `10_publicacao/` reorganizada pós-rejeição: `artigo_igro_cgu_revisado_final.docx` movido de `submissao/` para `versao_final/`. Removido scaffolding do BMad Method e estado transitório `.reversa/`. Documentação do projeto auditada; contradições corrigidas em `00_admin/controle_versoes/MEMORIA_PROJETO.md`. `README.md` (raiz) atualizado no mesmo lote.
- **2026-07-16:** registrado que o artigo submetido à Revista da CGU não foi aceito. Próximo ciclo: preparar resumo executivo/apresentação para alta gestão e, depois, pesquisar novo periódico para submissão.
- **2026-07-16:** pendências documentais menores revisadas: README raiz, `10_publicacao/README.md` e `10_publicacao/cgu_revista_submissao/README.md` atualizados para refletir o pós-submissão e o status "não aceito".
- **2026-06-08:** artigo submetido à Revista da CGU, conforme README atualizado.
- **2026-05-26 (Fase P — Documentação):**
  - ✅ P2: Validado — artigo menciona **51 órgãos** (confirmado linhas 37, 212)
  - ✅ P3: Criadas 4 READMEs (04_notas_tecnicas/, 05_scripts/, 08_apresentacoes/, 10_publicacao/)
  - ✅ P4: Consolidado README_migrado → README.md em 02_dados/; deletado arquivo legado
  - ✅ P6: Validadas 17 paths em README.md (raiz); corrigidas rutas para Power BI v2; atualizado README.md v2.1 → v2.2
- **2026-05-26 (Fase P1 — Consolidação anterior):**
  - Deletadas pastas legadas: `04_powerbi_e_dax/`, `06_dados/`, `07_entregaveis/` (migração verificada)
  - Criado `LEGACY.md` documentando migração (antes → depois)
  - Atualizado `CLAUDE.md` (traduzido + estrutura consolidada)
  - Atualizado `memory.md` (progresso 15% → 75%)
- **2026-05-18:** Reorganizados artefatos soltos de apresentação da raiz
- **2026-05-16:** Estrutura consolidada com READMEs em cada pasta

### Bloqueadores e Riscos
- 🔴 **Bloqueadores remanescentes:** recálculo e comparação dos resultados históricos; validação formal de metas e goalposts pelo GT de Gestão de Riscos; aprovação da inclusão do IGRO na Matriz pelo Comitê Setorial.
- ⚠️ **Risco de rastreabilidade:** a estrutura documentada de dados diverge da estrutura real (`raw/`, `processed/`, `schema/`) e os CSVs processados atuais não devem ser tratados como fonte tabular estável.

### Próximos Passos

🔄 **FASE R — Reposicionamento pós-submissão (ATUAL):**
1. ✅ Registrar a auditoria, a decisão canônica e o contrato de métricas (2026-08-10).
2. ✅ Validar perfil canônico, regra amostral, período/universo e escopo de comparação (2026-08-10).
3. ✅ Atualizar PBIP, desenho técnico e materiais de artigo após a decisão; fontes do PBIP corrigidas em 2026-08-10.
4. ✅ Adicionar data de atualização dos dados em todas as 6 páginas do modelo com rodapés HTML personalizados (2026-08-21).
5. ✅ Criar, revisar e salvar o mockup da página Análise setorial (2026-08-22).
6. ✅ Atualizar o modelo no Desktop após o reapontamento das fontes e verificar visualmente a correção do painel IGRO (2026-09-26); o usuário confirmou o resultado. O ID carregado e as contagens não foram transcritos nesta memória.
7. Implementar os filtros temporais e o painel Análise Setorial no PBIP em `07_dashboards/powerbi/`.
8. Recalcular os resultados históricos e compará-los com os derivados antigos.
9. Preparar resumo executivo/apresentação para alta gestão e, depois, pesquisar novo periódico e adaptar o artigo.

✅ **FASE P — Documentação (CONCLUÍDA em 2026-05-26):**
1. ✅ P2: Validação de órgãos — artigo menciona **51 órgãos** consistentemente (linhas 37, 212)
2. ✅ P3: READMEs criadas para 04_notas_tecnicas/, 05_scripts/, 08_apresentacoes/, 10_publicacao/
3. ✅ P4: README_migrado_de_06_dados.md consolidado → README.md em 02_dados/; arquivo antigo deletado
4. ✅ P6: Validação de paths — todas 17 referências em README.md confirmadas; corrigidas rutas para Power BI v2 (04_powerbi_e_dax/)

### Dependências e Stakeholders
- Dependências: estrutura atual documentada em `README.md`, `AGENTS.md` e mapa de migração
- Stakeholders-chave: mantenedor do repositório e fluxo de trabalho de documentação/Power BI

---

## Histórico de Atualizações

| Data | Status | Progresso | Nota |
|------|--------|-----------|------|
| 2026-09-26 | Em andamento | 87% | Usuário confirmou refresh após o reapontamento das fontes e conferiu no Desktop o painel IGRO corrigido; recálculo histórico e validações institucionais permanecem pendentes. A confirmação visual não registrou ID/contagens numéricas. |
| 2026-09-26 | Em andamento | 87% | Checkpoints anteriores da mesma data registravam refresh pós-TMDL pendente; foram superados pela validação posterior no Desktop. |
| 2026-09-22 | Em andamento | 87% | Revisão confirmou estado pós-submissão e mockup da Análise Setorial; detectada atividade no PBIP (28/08) e base parquet de 31/08; governança alinhada |
| 2026-08-22 | Em andamento | 87% | Mockup revisado e aprovado para continuidade; implementação do painel individual e filtros temporais ficou para a próxima sessão |
| 2026-08-21 | Em andamento | 88% | Rodapés HTML com data de atualização adicionados em todas as 6 páginas; refresh validado |
| 2026-08-10 | Em andamento | 87% | Decisão canônica registrada; PBIP/TMDL e caminhos Parquet corrigidos; refresh, recálculo e validação institucional pendentes |
| 2026-08-05 | Em andamento | 85% | Auditoria de consolidação; contrato de métricas registrado e governança documental atualizada |
| 2026-07-25 | Em andamento | 85% | Base analítica expandida (sensibilidade, quadrimestres, tabela suplementar) como preparação para o resumo executivo; publicação reorganizada pós-rejeição; documentação auditada |
| 2026-07-16 | Em andamento | 85% | Artigo submetido à Revista da CGU não foi aceito; próximo ciclo é briefing executivo/apresentação para alta gestão e busca de novo periódico |
| 2026-06-08 | Em andamento | 85% | Artigo submetido à Revista da CGU |
| 2026-05-26 | Em andamento | 80% | **Fase P Documentação Concluída** — P2/P3/P4/P6 implementadas; READMEs criadas; paths validadas; artigo 51 órgãos confirmado |
| 2026-05-26 (anterior) | Em andamento | 75% | **P1 Consolidado** — Pastas legadas deletadas; LEGACY.md criado; CLAUDE.md traduzido |
| 2026-05-18 | Em andamento | 15% | Raiz reorganizada de forma conservadora; README atualizado |
| 2026-05-16 | Em andamento | 0% | Inicialização |
