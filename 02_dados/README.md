# Dados — Input/Output Management

Organiza entradas (extrações de ouvidoria) e saídas (bases processadas, amostras, metadados).

---

## Quick Start (5 min)

```bash
# 1. Nova extração do SGOe chega
cp ~/Downloads/manifestacoes_2026_05.xlsx 01_brutos/

# 2. Documentar schema/filtros (se houver)
# Editar schema_sgoe.md com nomes de colunas

# 3. Processar base (script ou notebook em 06_notebooks/)
# Lê de 01_brutos/ e escreve em 02_tratados/

# 4. Validar saída
ls 02_tratados/*.csv
ls 03_amostras/
```

---

## Estrutura de Pastas

| Pasta | O quê | Imutável? | Quem escreve |
|---|---|---|---|
| **`01_brutos/`** | Extrações SGOe originais | ✅ Sim | Apenas entrada manual |
| **`02_tratados/`** | Bases processadas (limpas, padronizadas) | ❌ Não | Notebook/script (executado) |
| **`03_amostras/`** | Amostras para teste, validação, documentação | ❌ Não | Notebook/script (executado) |
| **`04_external/`** | Referências externas (tabelas de lookup, catálogos) | ✅ Sim | Manual (quando necessário) |
| **`schema/`** | Dicionário, mapeamentos, estrutura de dados | ⚠️ Quando base muda | Documentador |

---

## Fluxo de Dados (5 passos)

```
01_brutos/ (SGOe)
  ↓ [notebook/script lê]
[padroniza colunas, tipos, segmentações]
  ↓
02_tratados/ [salva base processada]
  ↓
[calcula indicadores: TMR, RES, RI, NPS]
  ↓
03_amostras/ [amostras para validação]
  ↓
06_notebooks/ + 07_dashboards/ [Power BI consome]
```

---

## Regras de Ouro

✅ **Fazer:**
- Salvar base original em `01_brutos/` sem modificações (read-only)
- Documentar schema em `schema/` **antes** de processar
- Incluir data de extração no nome do arquivo: `manifestacoes_2026_05_16.csv`
- Gerar saídas reproduzíveis via notebook (jamais manual)
- Documentar filtros aplicados (períodos, órgãos, tipos)

❌ **NÃO fazer:**
- Editar arquivos em `01_brutos/` manualmente
- Guardar scripts ou notebooks nesta pasta (ficam em `06_notebooks/`)
- Deixar saídas espalhadas (concentre em `02_tratados/`)
- Processar sem documentar origin, filtros e data

---

## Schema & Dicionário

**Antes de processar, documentar em `schema/`:**

| Campo | Tipo | Origem | Uso |
|---|---|---|---|
| `id_manifestacao` | int | SGOe | ID único |
| `data_entrada` | date | SGOe | Temporal (TMR) |
| `data_resposta` | date | SGOe | Cálculo TMR |
| `orgao_destino` | string | SGOe | Segmentação |
| `tipo_manifestacao` | string | SGOe | Segmentação |
| `avaliacao_satisfacao` | int | SGOe | NPS, média |
| `respondida` | boolean | SGOe | Resolutividade |

**Guardar em:** `schema/dicionario_campos_sgoe.md`

---

## Configuração para Nova Extração

Quando nova base chega do SGOe:

1. **Receber:** Copiar em `01_brutos/nome_data.xlsx` (sem modificações)
2. **Documentar schema:** 
   - Quais colunas existem?
   - Quais valores estão NULL?
   - Quais foram renomeadas/recodificadas?
   - Período coberto?
3. **Registrar em:** `schema/dicionario_campos_sgoe.md` + `schema/metadados_extracao.md`
4. **Processar:** Abrir notebook em `06_notebooks/` e definir `ARQUIVO_ENTRADA`
5. **Validar:** Checar `02_tratados/` e `03_amostras/` para sucessos

---

## Checklist de Qualidade

- [ ] Base original em `01_brutos/` sem modificação
- [ ] Schema documentado em `schema/`
- [ ] Nenhum NULL nas colunas obrigatórias (id, data, tipo)
- [ ] Datas em formato ISO (YYYY-MM-DD)
- [ ] Categorias padronizadas (sem typos: "Reclamação" vs "Reclamaçao")
- [ ] Organismo/órgão codificado ou mapeado
- [ ] Saídas em `02_tratados/` com ✅ sucesso
- [ ] Amostra em `03_amostras/` pronta para testes
- [ ] Nomes de arquivo claros + data (manifestacoes_2026_05_16.csv)

---

## Integração com Projeto

| Componente | Lê de | Escreve em |
|---|---|---|
| `06_notebooks/` | `01_brutos/` + `02_tratados/` | `02_tratados/` + `03_amostras/` |
| `07_dashboards/powerbi/` | `02_tratados/` | — (Power BI Desktop) |
| `09_resultados/` | `02_tratados/` | Gráficos, tabelas, exports |
| `03_estudos/` | `02_tratados/` + `03_amostras/` | Validações, análises |

**Sincronização:** Sempre que nova extração SGOe é recebida, processar uma vez via notebook.

---

## Manutenção

Quando skill de documentação revisar:
- [ ] `01_brutos/` ainda é ponto oficial de entrada?
- [ ] Schema em `schema/` acompanha a base atual?
- [ ] Nomes de arquivos seguem convenção (com data)?
- [ ] Links de rastreabilidade estão atualizados (qual célula gera qual saída)?

---

**Versão:** 2.0 (skill documentation-templates aplicada)  
**Atualizado:** 2026-05-16  
**Mantido por:** Analista de Dados
