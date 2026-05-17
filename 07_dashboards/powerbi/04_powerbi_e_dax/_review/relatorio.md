<!--
  TEMPLATE Â· /pbi-modelo-review Â· relatorio.md
  VersÃ£o markdown do relatÃ³rio (versionÃ¡vel Git, lÃª em qualquer editor)

  Como usar:
  1. Substituir placeholders {{VAR}} pelos valores reais
  2. Repetir bloco {{ISSUE_BLOCK}} pra cada issue (manter a estrutura)
  3. Salvar como _review/relatorio.md na raiz do projeto Power BI

  Esse markdown Ã© o "irmÃ£o" do index.html â€” mesmo conteÃºdo, mesma ordem, sem visual.
  Pra commit em Git, code review, leitura no editor.
-->

# Auditoria Â· indice_igro_v2.SemanticModel

> **Score: 90/100 â€” Bom**
> Gerado por Claude Code + `/pbi-modelo-review` em 13 mai 2026 Â· 21:03

**Modelo:** 14 tabelas Â· 117 medidas Â· 15 relacionamentos Â· ~16 MB

---

## Veredicto

O modelo do IGRO estÃ¡ acima da mÃ©dia em organizaÃ§Ã£o semÃ¢ntica: hÃ¡ fatos e dimensÃµes reconhecÃ­veis, as medidas estÃ£o bem descritas e o DAX bÃ¡sico foi escrito com bastante disciplina. O que puxa o score para baixo Ã© dÃ­vida estrutural escondida: Auto Date/Time ainda estÃ¡ governando vÃ¡rias colunas de data, as queries M dependem de caminhos pessoais no OneDrive e o PBIP em disco jÃ¡ nÃ£o bate perfeitamente com a sessÃ£o aberta do Desktop.

| MÃ©trica | Valor |
|---|---|
| Issues totais | **6** |
| CrÃ­ticos | **1** |
| Tempo estimado de correÃ§Ã£o | **4â€“8h** |

---

## Severidade

| NÃ­vel | Quantidade | Quando resolver |
|---|---|---|
| â–² **CrÃ­tico** | 1 | Resolva primeiro â€” quebram refresh em produÃ§Ã£o, comprometem performance ou geram resultado errado |
| â— **MÃ©dio** | 4 | PrÃ³xima sprint â€” anti-patterns que pioram conforme modelo cresce |
| â—‹ **Leve** | 1 | Quando der tempo â€” boas prÃ¡ticas, padronizaÃ§Ã£o, naming |

---

## DistribuiÃ§Ã£o por categoria

| Categoria | Issues |
|---|---|
| DocumentaÃ§Ã£o | 3 |
| Modelagem | 1 |
| Performance | 1 |
| Relacionamentos | 1 |

<!--
  Formato esperado de DISTRIBUTION_TABLE:
  | Categoria | Issues |
  |---|---|
  | Performance | 14 |
  | Relacionamentos | 11 |
  | ...
-->

---

## Issues priorizados

Issues abaixo estÃ£o **ordenados por severidade** (crÃ­tico â†’ mÃ©dio â†’ leve) e **agrupados por categoria** (concentraÃ§Ã£o = prioridade de refator).

### [CRÃ­TICO] Â· [Modelagem] Â· Auto Date/Time continua mandando no modelo apesar de existir dCalendario

**Onde:** `definition/model.tmdl:31; definition/relationships.tmdl:1-24; tables/f_relatorio.tmdl:42-60; tables/f_pesquisa.tmdl:22-25,101-104; tables/f_insatisfatorias.tmdl:32-65`

**Por que importa:**
VocÃª jÃ¡ fez a parte certa e criou a dCalendario, mas o modelo continua carregando DateTableTemplate e sete LocalDateTable_*. Pior: vÃ¡rias colunas de data das fatos ainda apontam sua hierarquia padrÃ£o para essas tabelas automÃ¡ticas. Isso Ã© o pior dos mundos: paga o custo do calendÃ¡rio corporativo e continua herdando ambiguidade, memÃ³ria extra e comportamento inconsistente de time intelligence.

**Como corrigir:**
Desligue o Auto Date/Time no Desktop, remova as variations que apontam para LocalDateTable_* e deixe a dCalendario como Ãºnica referÃªncia temporal. Onde precisar de mÃºltiplos eixos de data, mantenha relacionamentos explÃ­citos com dCalendario e use USERELATIONSHIP sÃ³ no ponto cirÃºrgico.

`	mdl
table dCalendario
    dataCategory: Time

    column Date
        dataType: dateTime
        isKey: true
        // sem variation apontando para LocalDateTable_*
`
"@
        SnippetHtml = @"
<pre><span class="c">// Mantenha um Ãºnico calendÃ¡rio real no modelo</span>
table <span class="f">dCalendario</span>
    dataCategory: <span class="s">Time</span>

    column <span class="f">Date</span>
        dataType: <span class="s">dateTime</span>
        isKey: <span class="k">true</span>
        <span class="c">// sem variation apontando para LocalDateTable_*</span></pre>

---

### [MÃ©DIO] Â· [Performance] Â· Sete LocalDateTable_* e um DateTableTemplate_* estÃ£o inflando o modelo Ã  toa

**Onde:** `definition/model.tmdl:48-60; definition/relationships.tmdl:1-24,45-50`

**Por que importa:**
Mesmo num modelo pequeno, oito tabelas de data automÃ¡ticas sÃ£o ruÃ­do estrutural desnecessÃ¡rio. Isso aumenta a superfÃ­cie do modelo, polui o lineage, dificulta leitura por quem herdar o projeto e vira multiplicador de dor quando o PBIP crescer ou ganhar mais colunas temporais.

**Como corrigir:**
Depois de desligar Auto Date/Time, salve o PBIP novamente para eliminar as LocalDateTable_* do projeto. O alvo aqui Ã© ficar sÃ³ com dCalendario e com os relacionamentos de negÃ³cio que realmente importam.

`	ext
Objetivo pÃ³s-limpeza:
- manter apenas dCalendario como dimensÃ£o temporal
- remover DateTableTemplate_* e LocalDateTable_*
- regravar o PBIP para persistir a limpeza
`
"@
        SnippetHtml = @"
<pre><span class="c">// Objetivo pÃ³s-limpeza</span>
- manter apenas <span class="f">dCalendario</span> como dimensÃ£o temporal
- remover <span class="f">DateTableTemplate_*</span> e <span class="f">LocalDateTable_*</span>
- regravar o PBIP para persistir a limpeza</pre>

---

### [MÃ©DIO] Â· [DocumentaÃ§Ã£o] Â· As queries M estÃ£o presas ao seu caminho pessoal no OneDrive

**Onde:** `definition/expressions.tmdl:19,50,101,134; tables/f_relatorio.tmdl:244; tables/f_pesquisa.tmdl:112; tables/f_insatisfatorias.tmdl:250`

**Por que importa:**
Hoje o refresh depende de caminhos como C:\Users\andre\OneDrive\sgoe-data-raw\data\powerbi. Isso funciona na sua mÃ¡quina e quebra no primeiro handoff, na primeira VM limpa ou quando outra pessoa tenta abrir o projeto. Ã‰ o tipo de dÃ­vida que nÃ£o aparece no print do dashboard, mas explode exatamente na hora em que alguÃ©m precisa reproduzir o modelo.

**Como corrigir:**
Parametrize o caminho-base das pastas de origem ou mova a ingestÃ£o para uma origem compartilhada. Se o objetivo Ã© portabilidade de projeto, caminho pessoal hardcoded precisa sair do modelo.

`	mdl
expression CaminhoBase = "" meta [
    IsParameterQuery=true,
    Type="Text",
    IsParameterQueryRequired=true
]
`
"@
        SnippetHtml = @"
<pre><span class="k">expression</span> <span class="f">CaminhoBase</span> = <span class="s">""</span> meta [
    IsParameterQuery=<span class="k">true</span>,
    Type=<span class="s">"Text"</span>,
    IsParameterQueryRequired=<span class="k">true</span>
]</pre>

---

### [MÃ©DIO] Â· [DocumentaÃ§Ã£o] Â· As dimensÃµes principais nÃ£o marcam a chave de negÃ³cio com isKey: true

**Onde:** `tables/dCalendario.tmdl:7-13; tables/dOrgao_igro.tmdl:33-39`

**Por que importa:**
dCalendario[Date] estÃ¡ como isUnique, e dOrgao_igro[sigla] estÃ¡ descrita como chave no texto, mas nenhuma das duas usa isKey: true no TMDL. Isso deixa a semÃ¢ntica formal mais fraca do que a semÃ¢ntica narrada. Para quem herdar, a pergunta vira imediata: qual coluna o modelo considera oficialmente como chave?

**Como corrigir:**
Marque explicitamente as business keys nas duas dimensÃµes. NÃ£o Ã© perfumaria: isso reduz ambiguidade, ajuda revisÃ£o automatizada e deixa o PBIP falar por si sem depender de documentaÃ§Ã£o paralela.

`	mdl
column Date
    isKey: true

column sigla
    isKey: true
`
"@
        SnippetHtml = @"
<pre>column <span class="f">Date</span>
    isKey: <span class="k">true</span>

column <span class="f">sigla</span>
    isKey: <span class="k">true</span></pre>

---

### [MÃ©DIO] Â· [DocumentaÃ§Ã£o] Â· PBIP em disco e sessÃ£o aberta do Desktop jÃ¡ mostram sinais de drift

**Onde:** `definition/model.tmdl; definition/relationships.tmdl; conexÃ£o viva PBIDesktop-indice_igro_v2-50796`

**Por que importa:**
No PBIP em disco aparecem 14 tabelas e 15 relacionamentos; na sessÃ£o conectada do Desktop apareceram 11 tabelas, 11 relacionamentos e outra contagem operacional de artefatos. Quando arquivo e sessÃ£o viva deixam de bater, revisÃ£o, debug e handoff comeÃ§am a falar idiomas diferentes. VocÃª corrige uma coisa e testa outra.

**Como corrigir:**
Escolha um fluxo de verdade Ãºnico para revisÃ£o: ou salva e reabre o PBIP antes de auditar, ou exporta a metadata da sessÃ£o imediatamente antes do review. O importante Ã© nÃ£o misturar arquivo antigo com modelo vivo mais novo.

`	ext
Fluxo seguro de auditoria:
1. salvar PBIP
2. reabrir o projeto
3. reconectar via XMLA/local instance
4. rodar auditoria e export de metadata no mesmo estado
`
"@
        SnippetHtml = @"
<pre><span class="c">// Fluxo seguro de auditoria</span>
1. salvar PBIP
2. reabrir o projeto
3. reconectar via XMLA/local instance
4. rodar auditoria e export de metadata no mesmo estado</pre>

---

### [LEVE] Â· [Relacionamentos] Â· HÃ¡ relacionamentos inativos com dCalendario sem uso explÃ­cito nas medidas

**Onde:** `definition/relationships.tmdl:57-69; tables/_medidas.tmdl:1478-1483`

**Por que importa:**
Relacionamento inativo nÃ£o Ã© pecado quando existe uma medida que o ativa com USERELATIONSHIP. O problema Ã© deixar vÃ¡rios pendurados sem uso observÃ¡vel. Hoje encontrei uso explÃ­cito para data_finalizacao em f_relatorio, mas nÃ£o apareceu uso equivalente para data_revisao, f_pesquisa[data_manifestacao] e f_insatisfatorias[data_manifestacao]. Isso vira ruÃ­do cognitivo para quem tenta entender o modelo.

**Como corrigir:**
Se esses relacionamentos sÃ£o estratÃ©gicos, documente quais medidas os consomem. Se nÃ£o forem mais necessÃ¡rios, limpe o excesso. Modelo semÃ¢ntico bom nÃ£o coleciona peÃ§a â€œvai que um diaâ€.

`dax
Base por Data de FinalizaÃ§Ã£o =
CALCULATE(
    [base_qtd_manifestacoes_finalizadas],
    USERELATIONSHIP(f_relatorio[data_finalizacao], dCalendario[Date])
)
`
"@
        SnippetHtml = @"
<pre><span class="f">Base por Data de FinalizaÃ§Ã£o</span> =
<span class="k">CALCULATE</span>(
    [base_qtd_manifestacoes_finalizadas],
    <span class="f">USERELATIONSHIP</span>(f_relatorio[data_finalizacao], dCalendario[Date])
)</pre>

---

<!--
  Formato esperado de cada ISSUE_BLOCK:

  ### [SEVERIDADE] Â· [CATEGORIA] Â· {TÃ­tulo do issue}

  **Onde:** `path/do/arquivo.tmdl[:linha]`

  **Por que importa:**
  {Texto explicando por que isso Ã© problema, adaptado ao contexto real do projeto.}

  **Como corrigir:**
  {Passo prÃ¡tico.}

  ```{tmdl|dax}
  // Snippet sugerido (opcional)
  ```

  ---

  Repetir o bloco pra cada issue.
-->

---

## Como rodar de novo

Quando quiser re-auditar (depois de aplicar correÃ§Ãµes, ou pra acompanhar evoluÃ§Ã£o):

```
claude code  # na pasta raiz do projeto Power BI
> /pbi-modelo-review
```

A skill **sobrescreve** este relatÃ³rio a cada execuÃ§Ã£o. Pra acompanhar evoluÃ§Ã£o, commite cada versÃ£o no Git e use `git diff _review/relatorio.md` pra ver o que mudou entre auditorias.

---

## Sobre essa skill

Auditoria gerada por **`/pbi-modelo-review`** â€” uma skill open-source da **Xperiun**, parte do toolkit Claude Code para Power BI.

- OperaÃ§Ã£o 100% local Â· zero rede Â· zero XMLA Â· LGPD-compatÃ­vel
- LÃª apenas arquivos `.tmdl` (texto puro do PBIP)
- NÃ£o modifica nada em `SemanticModel/` ou `Report/` â€” somente leitura

Saiba mais: **[pages.xperiun.com](https://pages.xperiun.com)**

---

*XPERIUN Â· O Sistema Operacional dos IncomparÃ¡veis*

