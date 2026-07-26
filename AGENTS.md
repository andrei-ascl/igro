# AGENTS.md

Este arquivo orienta agentes como Codex e Claude ao trabalhar neste repositório. Ele funciona como uma camada geral de operação do projeto e deve ser lido em conjunto com o contexto da tarefa, com o `README.md` e, quando relevante, com o `CLAUDE.md`.

## Objetivo do repositório

O projeto `igro` reúne pesquisa, especificação, documentação e artefatos de Power BI ligados ao **IGRO - Índice de Gestão de Riscos da Ouvidoria**.

O foco do trabalho costuma ser:

- organizar e evoluir documentos metodológicos;
- manter consistência entre pesquisa, PRD e desenho técnico;
- apoiar documentação e revisão do modelo Power BI;
- estruturar entregáveis e materiais publicáveis;
- preservar rastreabilidade do raciocínio metodológico.

Não é um repositório de aplicação tradicional. Em geral, não há build, app executável, suíte de testes ou pipeline de deploy para validar mudanças.

## Fontes de verdade

Antes de editar, usar esta ordem de referência:

1. Instrução explícita do usuário.
2. Este `AGENTS.md`.
3. `README.md` da raiz para navegação e estrutura atual.
4. `CLAUDE.md` para contexto operacional adicional.
5. Documentos centrais do projeto, especialmente:
   - `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md`
   - `00_admin/planejamento/03_especificacao_e_produto/11_PRD_IGRO.md`
   - `07_dashboards/powerbi/04_powerbi_e_dax/documentacao_modelo_semantico_igro.md`
   - `00_admin/planejamento/MAPA_MIGRACAO_ESTRUTURA_2026-05-06.md`

Se houver conflito entre documentos antigos e a estrutura atual, priorizar a estrutura descrita no `README.md` e no mapa de migração.

## Estrutura do projeto

Usar a estrutura atual como padrão:

- `00_admin/` para planejamento, memória, validações e rastreabilidade administrativa.
- `01_referencias/` para bibliografia, benchmarking e materiais normativos/conceituais.
- `02_dados/` para dados brutos, tratados, externos e schema.
- `03_estudos/` para conteúdo metodológico, análises e validação.
- `04_notas_tecnicas/` para rascunhos e versões formais.
- `05_scripts/` para scripts, automações e apoio técnico.
- `06_notebooks/` para notebooks e protótipos analíticos.
- `07_dashboards/` para Power BI, DAX, metadata e artefatos de dashboard.
- `08_apresentacoes/` para slides, roteiros e infográficos.
- `09_resultados/` para relatórios, tabelas e exportações.
- `10_publicacao/` para versão final, anexos e submissão.
- `skills/` para skills locais do projeto.

Não recriar a estrutura antiga (`01_pesquisa_metodologica`, `04_powerbi_e_dax`, `07_entregaveis` etc.) a menos que o usuário peça explicitamente.

## Como trabalhar aqui

- Escrever preferencialmente em português do Brasil.
- Manter siglas e termos técnicos consagrados quando fizer sentido: `KRI`, `KPI`, `PBIP`, `Power BI`, `DAX`, `Min-Max`, `Z-score`.
- Preferir mudanças pequenas, claras e rastreáveis.
- Preservar links internos, referências cruzadas e nomes já estabilizados.
- Ao reorganizar conteúdo, registrar o racional quando a mudança afetar navegação, localização ou fluxo de trabalho.
- Ao criar novos documentos, colocá-los na pasta conceitualmente correta em vez de acumular arquivos soltos na raiz.

## O que pode alterar

Normalmente é seguro:

- editar arquivos `.md`;
- criar documentação auxiliar;
- reorganizar documentos quando a nova localização for claramente melhor e consistente com a estrutura atual;
- criar ou ajustar arquivos de apoio em `05_scripts/`, `06_notebooks/`, `08_apresentacoes/`, `09_resultados/` e `10_publicacao/`;
- atualizar documentação derivada do modelo Power BI;
- adicionar skills novas em `skills/`.

## O que exige cuidado extra

- arquivos `.pbix`;
- arquivos `.tmdl` e estruturas PBIP;
- exports de metadata em `07_dashboards/powerbi/04_powerbi_e_dax/metadata/`;
- documentos centrais de definição metodológica e de produto;
- arquivos da raiz usados por ferramentas locais.

Antes de mexer nesses itens, confirmar que a alteração é realmente necessária para cumprir a tarefa.

## O que não deve alterar sem necessidade explícita

- `settings.local.json`
- `skill.md`
- configurações locais usadas por ferramentas
- artefatos binários de Power BI apenas por “organização estética”
- textos metodológicos centrais de forma substantiva sem preservar coerência com os demais documentos

Evitar também:

- apagar histórico documental sem necessidade;
- sobrescrever arquivos importantes com templates genéricos;
- mover arquivos centrais sem atualizar referências;
- criar conteúdo inventado para preencher lacunas metodológicas sem sinalizar que é proposta/inferência.

## Regras específicas para Power BI

- Priorizar a pasta `07_dashboards/powerbi/04_powerbi_e_dax/`.
- Considerar `documentacao_modelo_semantico_igro.md` e `metadata/` como referências operacionais do modelo.
- Se houver trabalho em PBIP/TMDL, preservar estrutura, encoding e nomes existentes.
- Se houver edição assistida por ferramenta externa no modelo, relatar claramente o que foi alterado.
- Não assumir que um `.pbix` pode ser modificado com segurança sem o usuário pedir isso.

As skills importadas em `skills/powerbi-codex-skills/` são a referência preferencial para tarefas de:

- documentação do modelo;
- auditoria do modelo;
- criação de medidas DAX.

## Regras para documentação

- Preferir Markdown.
- Títulos e seções devem ser objetivos e navegáveis.
- Não transformar documentos técnicos em texto promocional.
- Ao resumir material metodológico, manter fidelidade ao conteúdo-fonte.
- Ao propor melhorias, separar claramente fato, interpretação e recomendação.

## Validação de entregas

Como este repositório é majoritariamente documental, validar por evidência adequada ao tipo de mudança:

- Para documentação:
  - verificar links internos e caminhos mencionados;
  - conferir coerência com a estrutura atual do projeto;
  - revisar consistência terminológica.
- Para reorganização de arquivos:
  - confirmar que o destino é compatível com o mapa de estrutura;
  - verificar se referências importantes continuam corretas;
  - registrar a mudança quando ela afetar navegação.
- Para Power BI / metadata:
  - confirmar que arquivos esperados existem no local correto;
  - não declarar sucesso sem checar os artefatos gerados.
- Para scripts:
  - executar quando for seguro e fizer sentido;
  - se não executar, deixar isso explícito.

## Forma de resposta esperada do agente

Ao concluir uma tarefa, o agente deve informar de forma concisa:

- o que mudou;
- onde mudou;
- como validou;
- o que ficou pendente, se houver.

Se uma decisão envolver trade-off relevante, o agente deve explicitar a escolha e o motivo.

## Em caso de dúvida

- Escolher a alternativa mais conservadora.
- Preservar conteúdo e rastreabilidade.
- Favorecer a estrutura atual do projeto.
- Perguntar ao usuário apenas quando a decisão puder causar perda, ambiguidade forte ou retrabalho relevante.

