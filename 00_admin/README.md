# Administração — Planejamento e Controle

Concentra documentação de planejamento, decisões, versões e histórico administrativo do projeto IGRO.

---

## Quick Start (5 min)

```bash
# 1. Entender escopo e desenho
cat planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md

# 2. Conferir PRD e requisitos
cat planejamento/03_especificacao_e_produto/11_PRD_IGRO.md

# 3. Ver o que foi decidido/feito
cat controle_versoes/MEMORIA_PROJETO.md

# 4. Consultar estrutura de migração
cat planejamento/MAPA_MIGRACAO_ESTRUTURA_2026-05-06.md
```

---

## Estrutura de Subpastas

| Pasta | O quê | Tipo |
|---|---|---|
| **`planejamento/`** | Cronograma, desenho técnico, PRD, objetivos | 📋 Documentação |
| **`controle_versoes/`** | Memória do projeto, decisões, validações | 📝 Log vivo |
| **`validacoes/`** | Checklists, critérios de aceite, registros de validação | ✅ Rastreabilidade |

---

## Documentos Centrais

### `planejamento/03_especificacao_e_produto/`

| Arquivo | Propósito |
|---------|-----------|
| **10_Desenho_IGRO.md** | O quê é IGRO, por quê, componentes, riscos cobertos, metodologia |
| **11_PRD_IGRO.md** | Escopo funcional, requisitos técnicos, critérios de aceite, roadmap |
| **MAPA_MIGRACAO_ESTRUTURA_2026-05-06.md** | Estrutura anterior vs. atual, onde cada coisa foi movida |

### `controle_versoes/`

| Arquivo | Propósito |
|---------|-----------|
| **MEMORIA_PROJETO.md** | Log vivo: status, decisões tomadas, bloqueadores, próximas ações |
| **VALIDACOES_*.md** | Resultado de validações de metodologia, dados, modelo Power BI |

---

## Navegação por Objetivo

**Preciso entender o projeto:**
→ Leia `planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md` (30 min)

**Preciso conhecer requisitos e escopo:**
→ Leia `planejamento/03_especificacao_e_produto/11_PRD_IGRO.md` (20 min)

**Preciso saber o que foi feito/decidido:**
→ Leia `controle_versoes/MEMORIA_PROJETO.md` (10 min)

**Preciso validar metodologia:**
→ Consulte `validacoes/` ou `MEMORIA_PROJETO.md` (Seção "Decisões Metodológicas")

---

## Convenções

✅ **Fazer:**
- Documentar toda decisão importante em `MEMORIA_PROJETO.md`
- Manter cronograma/roadmap em `planejamento/`
- Registrar mudanças de escopo no PRD
- Validar antes de finalizar (deixar evidências em `validacoes/`)

❌ **NÃO fazer:**
- Guardar dados ou notebooks aqui (ficam em `02_dados/`, `06_notebooks/`)
- Deixar decisões não-documentadas
- Arquivos soltos na raiz (organizar em subpastas)

---

## Integração com Projeto

**Quem lê daqui:**
- Novos colaboradores (entender projeto)
- Project manager (acompanhar cronograma)
- Auditores (rastreabilidade de decisões)

**Quem escreve aqui:**
- Product owner (PRD, escopo)
- Project manager (memória, cronograma)
- Líder técnico (decisões, validações)

---

**Versão:** 2.0 (skill documentation-templates aplicada)  
**Atualizado:** 2026-05-16  
**Mantido por:** Gerente de Projeto / Product Owner
