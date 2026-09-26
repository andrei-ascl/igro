# Dados — Input/Output Management

Organiza as fontes de ouvidoria, as saídas processadas e o contrato de dados usado por notebooks, estudos e Power BI.

> **Status de reconciliação — 2026-08-05:** a estrutura de dados deste projeto é `raw/`, `processed/` e `schema/`. Os nomes legados `01_brutos/`, `02_tratados/` e `03_amostras/` não devem ser usados em novos arquivos.
>
> **Entrada compartilhada do PBIP — 2026-09-26:** o modelo IGRO prioriza snapshots versionados em `../sgoe_hub/data/processed/`; o usuário confirmou que o refresh após o reapontamento foi realizado com sucesso. Os destinos de compatibilidade do IGRO foram removidos do Hub. Parquets antigos em `06_dados/01_brutos/` foram preservados como fallback local; não os apague sem aprovação.

---

## Quick Start (5 min)

```text
1. Preserve a extração original em raw/.
2. Consulte schema/dicionario_dados.md e o contrato de métricas antes de processar.
3. Execute o notebook/script responsável e grave derivados em processed/.
4. Valide período, universo, amostra, campos obrigatórios e rastreabilidade.
5. Só depois consuma a saída em estudos, resultados ou Power BI.
```

O contrato provisório está em [`00_admin/planejamento/03_especificacao_e_produto/CONTRATO_METRICAS_IGRO.md`](../00_admin/planejamento/03_especificacao_e_produto/CONTRATO_METRICAS_IGRO.md).

## Fontes atualmente presentes

Os Parquets listados abaixo são fontes locais preservadas para processamento e fallback. Para o PBIP, a fonte preferida é o snapshot canônico compartilhado do Hub (`../sgoe_hub/data/processed/`).

- `raw/relatorio_2026-05-05.parquet`
- `raw/pesquisa_2026-05-05.parquet`
- `raw/insatisfatorio_2026-05-05.parquet`

Não sobrescreva os arquivos em `raw/`. Se houver nova extração, preserve data e origem no nome.

## Estrutura de Pastas

| Pasta | O quê | Imutável? | Quem escreve |
|---|---|---|---|
| **`raw/`** | Extrações originais em Parquet | ✅ Sim | Entrada/manual |
| **`processed/`** | Saídas derivadas para notebooks, estudos e dashboards | ❌ Não | Notebook/script |
| **`schema/`** | Dicionário, entidades, mapeamentos e contrato de dados | ⚠️ Revisar quando a base muda | Documentador |
| **`external/`** | Não existe como pasta vigente; criar somente se uma fonte externa for incorporada | — | Manual, com registro |

Os arquivos `processed/geral.csv` e `processed/matriz_orgao.csv` atualmente contêm encapsulamento HTML/JavaScript, não um CSV tabular estável. Eles devem ser tratados como exportações a corrigir ou renomear, e não como fonte tabular canônica.

## Fluxo de Dados

```text
raw/ (Parquet original)
  ↓ [notebook/script]
padronização, filtros e derivação
  ↓
processed/ (saídas derivadas, com formato validado)
  ↓
03_estudos/ + 09_resultados/ + 07_dashboards/

sgoe_hub/data/processed/ (snapshots canônicos compartilhados)
  ↓ [TMDL do IGRO; refresh pós-migração confirmado em 2026-09-26]
07_dashboards/powerbi/
```

## Regras de Ouro

✅ **Fazer:**

- preservar `raw/` sem modificações;
- documentar origem, período, filtros e schema antes de processar;
- registrar a extração no nome do arquivo;
- gerar saídas reproduzíveis via notebook/script;
- validar se a saída é realmente tabular antes de chamá-la de CSV;
- registrar a variante metodológica usada e a regra de inclusão amostral.

❌ **Não fazer:**

- editar arquivos em `raw/` manualmente;
- usar caminhos legados como se fossem a estrutura atual;
- tratar `processed/` como fonte bruta;
- misturar os resultados de 51 órgãos com a análise de sensibilidade de 47 órgãos sem declarar a regra;
- promover resultados antes da decisão canônica do IGRO.

## Schema & Dicionário

O dicionário provisório está em [`schema/dicionario_dados.md`](schema/dicionario_dados.md). Ele separa entidades conhecidas do modelo e campos que ainda precisam de confirmação no schema físico/TMDL.

| Entidade conceitual | Papel | Fonte/uso |
|---|---|---|
| `f_relatorio` | Manifestações, prazos, status e órgão | `raw/relatorio_*.parquet`; TMR e risco 0044 |
| `f_pesquisa` | Respostas de pesquisa e indicadores de qualidade | `raw/pesquisa_*.parquet`; RES, NPS e risco 0046 |
| `f_insatisfatorias` | Registros/classificações de insatisfação | `raw/insatisfatorio_*.parquet`; RI |
| `dCalendario` | Datas e quadrimestres | Modelo semântico Power BI |
| `dOrgao_igro` | Dimensão de órgãos por `sigla` | Referência do IGRO |

## Configuração para Nova Extração

1. Preservar a nova fonte em `raw/` sem modificações.
2. Registrar data, período, origem, universo e arquivos em `schema/`.
3. Atualizar o dicionário se entidades, campos ou codificações mudarem.
4. Processar pelo notebook/script responsável, sem escrever manualmente em `processed/`.
5. Validar numeradores, denominadores, duplicidades, nulos, período e regra amostral.

## Checklist de Qualidade

- [ ] Fonte original preservada em `raw/`
- [ ] Schema e dicionário atualizados
- [ ] Período e data de extração registrados
- [ ] Universo declarado (51 órgãos no escopo geral ou subconjunto explicitamente justificado)
- [ ] Regra para os 47 órgãos completos da sensibilidade registrada quando aplicável
- [ ] Campos obrigatórios, tipos, nulos e duplicidades verificados
- [ ] Numeradores e denominadores dos KRIs reconciliados
- [ ] Saída de `processed/` validada como formato declarado
- [ ] Perfil de parâmetros/fórmula registrado
- [ ] Qualquer amostra pequena sinalizada, excluída ou suavizada conforme decisão aprovada

## Integração com Projeto

| Componente | Lê de | Escreve em |
|---|---|---|
| `06_notebooks/` | `raw/` e `processed/` | `processed/` e `09_resultados/` |
| `03_estudos/` | `raw/`, `processed/` e schema | Validações e análises |
| `07_dashboards/powerbi/` | Saídas processadas e modelo semântico | Power BI Desktop/PBIP |
| `09_resultados/` | Saídas validadas | Gráficos, tabelas e relatórios |

**Sincronização:** toda nova extração deve ser processada uma vez, com registro suficiente para reproduzir a saída.

## Manutenção

- [ ] A estrutura real continua sendo `raw/`, `processed/`, `schema/`?
- [ ] O dicionário acompanha a base física e o TMDL?
- [ ] Os arquivos processados têm formato coerente com a extensão?
- [ ] O contrato de métricas e a decisão canônica estão vinculados?
- [ ] Os links de rastreabilidade estão atualizados?

---

**Versão:** 2.1 (reconciliação da estrutura real e do contrato de dados)
**Atualizado:** 2026-08-05
**Mantido por:** Analista de Dados
