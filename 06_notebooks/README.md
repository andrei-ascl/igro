# Notebooks — Exploração e Prototipagem

Contém notebooks Jupyter para exploração de dados, modelagem e geração de outputs analíticos.

---

## Quick Start (5 min)

```bash
# 1. Abrir notebook principal
jupyter notebook exploracao/artigo_igro_graficos_tabelas.ipynb

# 2. Configurar entrada (célula 1)
ARQUIVO_ENTRADA = "manifestacoes_2026_05.csv"
PASTA_SAIDA = "../09_resultados/artigo_igro_figuras_tabelas/"

# 3. Executar
Kernel → Restart & Run All

# 4. Conferir saída
ls ../09_resultados/artigo_igro_figuras_tabelas/
```

---

## Notebooks Disponíveis

| Notebook | Propósito | Status |
|----------|-----------|--------|
| **`exploracao/artigo_igro_graficos_tabelas.ipynb`** | 📊 Principal: calcula indicadores, gera tabelas e gráficos para o artigo | ✅ Operacional |
| **`exploracao/*_analise_*.ipynb`** | 🔬 Análises exploratórias, testes de sensibilidade | 📝 Variado |
| **`prototipagem/teste_*.ipynb`** | 🧪 Protótipos e experimentos | 📝 Variado |

---

## Notebook Principal

**Localização:** `exploracao/artigo_igro_graficos_tabelas.ipynb`

### Estrutura de Células

| Seção | Propósito |
|-------|-----------|
| **1. Setup** | Configuração de caminho, imports, variáveis globais |
| **2. Carregar dados** | Ler CSV/XLSX de `02_dados/processed/` |
| **3. Exploração** | Verificar estrutura, valores NULL, estatísticas |
| **4. Cálculos** | Computar TMR, RES, RI, NPS, outros indicadores |
| **5. Tabulação** | Agrupar por órgão, período, tipo |
| **6. Visualização** | Criar 10 gráficos com identidade Goiás |
| **7. Exportação** | Salvar tabelas CSV/XLSX e gráficos PNG |

---

## Configuração

**Editar na célula 1:**

```python
# ENTRADA
ARQUIVO_ENTRADA = "manifestacoes_2026_05.csv"  # Nome do arquivo em 02_dados/processed/
PASTA_DADOS_ENTRADA = "../02_dados/processed/"

# SAÍDA
PASTA_SAIDA = "../09_resultados/artigo_igro_figuras_tabelas/"

# TEMA
from igro.style import apply_goias_theme
apply_goias_theme()

# PERÍODO (filtro)
DATA_INICIO = "2026-01-01"
DATA_FIM = "2026-05-31"
```

---

## Dependências

```bash
# Instalar (primeira vez)
pip install -r requirements.txt

# Ou manualmente:
pip install pandas numpy matplotlib seaborn jupyter openpyxl scipy scikit-learn
```

**Pacotes principais:**
- `pandas` — manipulação de dados
- `matplotlib`, `seaborn` — visualização com tema Goiás
- `openpyxl` — exportar para Excel
- `scipy`, `scikit-learn` — análises estatísticas

---

## Fluxo de Trabalho

```
1. Receber base nova em 02_dados/raw/
2. Processar em script/notebook → 02_dados/processed/
3. Abrir artigo_igro_graficos_tabelas.ipynb
4. Configurar ARQUIVO_ENTRADA
5. Executar Kernel → Restart & Run All
6. Saídas aparecem em 09_resultados/artigo_igro_figuras_tabelas/
7. Incorporar gráficos/tabelas ao artigo
```

---

## Troubleshooting

| Erro | Solução |
|------|---------|
| **FileNotFoundError** | Verificar nome e caminho de ARQUIVO_ENTRADA |
| **KeyError em coluna** | Validar schema em `02_dados/schema/` |
| **Gráfico não salva** | Verificar permissão em PASTA_SAIDA |
| **Kernel morreu (MemoryError)** | Reduzir período DATA_INICIO/DATA_FIM ou amostra |

**Dica:** Sempre executar células em sequência; não pule nenhuma.

---

## Convenções

✅ **Fazer:**
- Nomes descritivos para notebooks: `artigo_igro_graficos_tabelas.ipynb`
- Documentar cada célula com comentários claros
- Incluir output: tabelas salvas, gráficos com data
- Versionar: manter backup de notebooks que funcionaram

❌ **NÃO fazer:**
- Alterar dados direto no notebook (ler de `02_dados/`, não editar aqui)
- Deixar hardcoded caminhos absolutos
- Guardar saídas neste diretório (usar `09_resultados/`)
- Notebooks soltos sem documentação

---

## Integração com Projeto

**Lê de:**
- `02_dados/processed/` — dados processados
- `05_scripts/` — estilos, utilitários Python
- `01_referencias/` — contexto (se usar)

**Escreve em:**
- `09_resultados/artigo_igro_figuras_tabelas/` — tabelas e gráficos

**Referenciado por:**
- `09_resultados/relatorios/memoria_trabalho_proximos_passos.md` (log de execuções)
- `04_notas_tecnicas/` (artigo inclui outputs)

---

**Versão:** 2.0 (skill documentation-templates aplicada)  
**Atualizado:** 2026-05-16  
**Mantido por:** Analista de Dados / Cientista de Dados
