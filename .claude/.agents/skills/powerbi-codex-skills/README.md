# Power BI Codex Skills

Skills importadas de `xperiun/claude-code-powerbi-skills`:

- `pbi-modelo-review`
- `pbi-doc`
- `pbi-dax-create`

Origem:

- Repositório: `https://github.com/xperiun/claude-code-powerbi-skills`
- Variante instalada: `claude-code/`
- Data de importação: `2026-05-06`

Fonte externa de consulta indicada para este acervo:

- Vídeo YouTube: `https://www.youtube.com/watch?v=5FCG6PdBFEY`

Estrutura:

- Cada skill é self-contained e mantém seu próprio `SKILL.md`, `references/` e `templates/`.
- As skills foram copiadas para esta pasta do projeto para uso local e versionamento junto do repositório.

Como usar neste projeto:

- Abra uma nova sessão do Codex para que as skills sejam indexadas.
- Depois, use pedidos em linguagem natural que acionem cada skill, por exemplo:
  - `audita esse modelo`
  - `quero documentar esse projeto Power BI`
  - `cria uma medida DAX para ticket médio`

Pré-requisito funcional:

- Essas skills esperam um projeto Power BI em formato PBIP, com arquivos `.tmdl` acessíveis no projeto.
