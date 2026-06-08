# LEGACY — Histórico de Migração Estrutural

**Data da Consolidação:** 2026-05-26

---

## O Que Aconteceu

A estrutura do projeto IGRO foi reorganizada em **2026-05-06** para melhorar navegação e consistência. Pastas com nomenclatura legada (numeração 00-10 sem contexto) foram consolidadas em uma estrutura moderna e bem documentada.

---

## Pastas Deletadas

As seguintes pastas foram **completamente migradas** e deletadas em 2026-05-26:

### 1️⃣ `04_powerbi_e_dax/` → `07_dashboards/powerbi/04_powerbi_e_dax/`

**Conteúdo migrado:**
- `indice_igro.pbix` — Modelo Power BI v1
- `indice_igro_v2.pbix` — Modelo Power BI v2 (estável)
- `indice_igro_v2.pbip` — Projeto PBIP Git-first
- `documentacao_modelo_semantico_igro.md` — Especificação técnica
- `metadata/` — Exportações de estrutura DAX
- Documentação: `dax_enterprise_guide_*.md`, `medidas_dax_*.md`

**Status:** ✅ 100% migrado. Novo local operacional.

---

### 2️⃣ `06_dados/` → `02_dados/`

**Conteúdo migrado:**
- `01_brutos/` → `02_dados/raw/`
- `02_tratados/` → `02_dados/processed/`
- `03_amostras/` → `02_dados/external/`
- Schema e dicionário → `02_dados/schema/`

**Status:** ✅ 100% migrado. Novo local operacional.

---

### 3️⃣ `07_entregaveis/` → `09_resultados/`

**Conteúdo migrado:**
- `01_relatorios/` → `09_resultados/relatorios/`
- `02_apresentacoes/` → `08_apresentacoes/entregas/`
- `03_exports_powerbi/` → `09_resultados/exportacoes/`

**Status:** ✅ 100% migrado. Novo local operacional.

---

## Por Que Migrar?

| Problema Antigo | Solução Nova |
|---|---|
| Pastas sem contexto (números soltos) | Contexto claro (00_admin, 02_dados, 07_dashboards, etc.) |
| Dispersão entre raiz e subpastas | Hierarquia organizada: **00-10 + skills/** |
| Dificuldade de navegação para novos colaboradores | Quick Start e READMEs em cada pasta |
| Referências cruzadas desatualizadas | Mapa de migração + documentação clara |

---

## Referências Atualizadas

A migração foi documentada em:
- **`00_admin/planejamento/MAPA_MIGRACAO_ESTRUTURA_2026-05-06.md`** — Mapeamento completo: antes → depois
- **`CLAUDE.md`** — Guia operacional com estrutura atual apenas
- **`README.md`** — Atualizado com caminhos novos

---

## Se Você Encontrar Referências Antigas

Se ao ler documentação antiga encontrar caminhos como:
- `04_powerbi_e_dax/...`
- `06_dados/...`
- `07_entregaveis/...`

**Traduza para:**
- `07_dashboards/powerbi/04_powerbi_e_dax/...`
- `02_dados/...`
- `09_resultados/...` ou `08_apresentacoes/...`

Ou consulte `MAPA_MIGRACAO_ESTRUTURA_2026-05-06.md`.

---

## Validação da Limpeza

Deletado em 2026-05-26:
- ✅ Pastas 04_powerbi_e_dax, 06_dados, 07_entregaveis removidas
- ✅ Nenhum arquivo perdido (todos migraram antes)
- ✅ Estrutura moderna ativa e operacional

**Resultado:** Repositório mais limpo, navegação mais clara, sem redundância.

---

**Mantido por:** Andrei Azevedo  
**Data:** 2026-05-26  
**Status:** Migração consolidada
