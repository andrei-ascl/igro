# Referências — Pesquisa e Benchmarking

Reúne bibliografia, artigos, normas, benchmarking e documentos de referência para a metodologia do IGRO.

---

## Quick Start (5 min)

```bash
# 1. Benchmarking de KRIs em ouvidorias brasileiras
cat artigos/02_benchmarking_e_referencias_brasileiras/09_Benchmarking_KRIs_Ouvidorias_Estaduais.md

# 2. Índice completo de fontes
cat livros/05_fontes_e_bibliografia/08_Bibliografia_Links.md

# 3. Referências sobre KRIs (Key Risk Indicators)
cat artigos/02_benchmarking_e_referencias_brasileiras/07_KRI_Indicadores_Chave_Risco.md

# 4. Índices Compostos (metodologia)
ls metodologia/pesquisa_metodologica/
```

---

## Estrutura de Subpastas

| Pasta | Conteúdo | Tipo |
|---|---|---|
| **`artigos/`** | Pesquisa sobre metodologia, benchmarking, riscos em ouvidoria | 📄 Documentos |
| **`livros/`** | Bibliografia, guias (OCDE/JRC), fundamentos teóricos | 📚 Referências |
| **`metodologia/`** | Pesquisa sobre índices compostos, ponderação, agregação | 🔬 Estudos |
| **`normas/`** | LAI, LGPD, padrões de ouvidoria pública, resoluções | ⚖️ Normativo |

---

## Documentos Principais

### Benchmarking & KRIs

| Arquivo | Propósito |
|---------|-----------|
| **09_Benchmarking_KRIs_Ouvidorias_Estaduais.md** | Pesquisa de indicadores em ouvidorias estaduais (base para IGRO) |
| **07_KRI_Indicadores_Chave_Risco.md** | O que é um KRI, como construir, exemplos de TMR, RES, RI |
| **06_Referencias_Brasileiras_Gestao_Publica.md** | Padrões brasileiros: SISP, e-SIC, Poder360, ouvidoria pública |

### Metodologia

| Arquivo | Propósito |
|---------|-----------|
| **01_Visao_Geral_Indices_Compostos.md** | O que é índice composto, estrutura, aplicações |
| **02_Normalizacao_Metodos.md** | Técnicas de normalização: Min-Max, Z-score, Percentil |
| **03_Ponderacao_Metodos.md** | Como pesar dimensões e indicadores |
| **04_Agregacao_Metodos.md** | Fórmulas de agregação: média, PCA, outros |
| **05_Analise_Robustez_Sensibilidade.md** | Validação: testes de robustez, sensibilidade |

### Fontes & Guias

| Arquivo | Propósito |
|---------|-----------|
| **08_Bibliografia_Links.md** | Índice completo: OCDE, JRC, artigos, links para downloads |
| **referencias_indice_ouvidoria.md** | Documentação base sobre construção de índices |

---

## Navegação por Tema

**Preciso entender KRIs:**
→ `artigos/02_benchmarking_e_referencias_brasileiras/07_KRI_Indicadores_Chave_Risco.md`

**Preciso ver benchmarking em ouvidorias brasileiras:**
→ `artigos/02_benchmarking_e_referencias_brasileiras/09_Benchmarking_KRIs_Ouvidorias_Estaduais.md`

**Preciso aprender metodologia de índices compostos:**
→ `metodologia/pesquisa_metodologica/` (ler 01 a 05 em sequência)

**Preciso validar robustez do IGRO:**
→ `metodologia/pesquisa_metodologica/05_Analise_Robustez_Sensibilidade.md`

**Preciso encontrar fonte específica (OCDE, artigo, guia):**
→ `livros/05_fontes_e_bibliografia/08_Bibliografia_Links.md` (índice completo)

---

## Padrão de Organização

```
artigos/
├── 01_metodologia_indices/
│   ├── Como construir índices compostos
│   └── Padrões internacionais
├── 02_benchmarking_e_referencias_brasileiras/
│   ├── Pesquisa de KRIs em ouvidorias
│   └── Padrões brasileiros (e-SIC, LAI, etc.)

livros/
├── 05_fontes_e_bibliografia/
│   ├── Handbook OCDE/JRC (downloads)
│   ├── Artigos acadêmicos
│   └── Índice completo de links

metodologia/
└── pesquisa_metodologica/
    ├── 01_Visao_Geral_Indices_Compostos.md
    ├── 02_Normalizacao_Metodos.md
    ├── 03_Ponderacao_Metodos.md
    ├── 04_Agregacao_Metodos.md
    └── 05_Analise_Robustez_Sensibilidade.md
```

---

## Convenções

✅ **Fazer:**
- Manter PDFs, artigos e guias organizados por tema
- Documentar origem de cada arquivo (URL, autor, data)
- Referenciar na memória do projeto quando usar como fundamentação
- Adicionar link em `08_Bibliografia_Links.md` quando nova fonte chegar

❌ **NÃO fazer:**
- Duplicar arquivos (manter versão única)
- Guardar arquivos sem documentar origem
- Deixar soltos na raiz (organizar em subpastas)

---

## Integração com Projeto

**Quem lê daqui:**
- Metodólogo (validar abordagem)
- Auditores (verificar fundamentação)
- Novos colaboradores (aprender conceitos)

**Citação no projeto:**
- Referências metodológicas → `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md`
- Validação de robustez → `03_estudos/metodologia/` ou `MEMORIA_PROJETO.md`

---

**Versão:** 2.0 (skill documentation-templates aplicada)  
**Atualizado:** 2026-05-16  
**Mantido por:** Pesquisador / Metodólogo
