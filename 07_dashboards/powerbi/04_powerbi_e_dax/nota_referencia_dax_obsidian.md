# 📊 Nota de Referência — Arquitetura de Medidas DAX (BaseDadosOuvidoria)

## 🎯 Objetivo desta nota
Este documento serve como referência estratégica para uso no Obsidian, explicando dois artefatos fundamentais do modelo de dados:

1. **Medidas organizadas por camadas (`medidas_dax_snake_case_camadas.md`)**
2. **Guia de governança DAX nível enterprise (`dax_enterprise_guide_basedadosouvidoria.md`)**

---

# 🧱 1. Arquivo: Medidas por Camadas

## 📌 O que é
Um catálogo completo de medidas DAX:
- padronizadas em `snake_case`
- organizadas por **camadas semânticas**
- otimizadas para performance e manutenção

---

## 🧠 Lógica de construção

As medidas seguem uma arquitetura em camadas:

```
camada_base → camada_indicadores → camada_tempo/ranking → camada_indices → camada_auxiliares → camada_formatacao
```

---

## 🧩 Cada camada representa:

### 🔹 camada_base
- Dados brutos calculados
- Contagens e médias fundamentais
- Exemplo: `base_qtd_manifestacoes`

👉 **Importância:**
Base única de verdade (single source of truth)

---

### 🔹 camada_indicadores
- Percentuais e métricas derivadas
- Exemplo: `ind_pct_resolutividade`

👉 **Importância:**
Transforma dados em informação

---

### 🔹 camada_tempo
- Inteligência temporal (ex: ano anterior)

👉 **Importância:**
Permite análise comparativa e tendência

---

### 🔹 camada_ranking
- Ranking e Top N

👉 **Importância:**
Identificação de prioridades e concentração de problemas

---

### 🔹 camada_indices
- Índices compostos (IQO, IGRO)

👉 **Importância:**
Síntese executiva para tomada de decisão

---

### 🔹 camada_auxiliares
- Títulos e helpers

👉 **Importância:**
Melhora a experiência do usuário

---

### 🔹 camada_formatacao
- Semáforos e cores

👉 **Importância:**
Comunicação visual e leitura rápida

---

## 🚀 Benefícios

- Alta legibilidade
- Facilidade de manutenção
- Reuso de lógica
- Redução de erros
- Escalabilidade do modelo

---

# 🏛️ 2. Arquivo: Guia Enterprise DAX

## 📌 O que é
Um guia de governança para garantir que o modelo siga padrões corporativos.

---

## 🧠 O que ele define

### 🔹 Convenção de nomes
Padronização com prefixos:
- `base_`, `ind_`, `rank_`, `idx_`, `meta_`, `fmt_`

👉 Evita ambiguidade e melhora manutenção

---

### 🔹 Arquitetura do modelo
Define como as medidas devem ser organizadas e dependentes entre si

---

### 🔹 Boas práticas DAX
- uso de `VAR`
- uso de `DIVIDE`
- uso de `COALESCE`
- uso de `KEEPFILTERS`

---

### 🔹 Anti-patterns evitados
- `FILTER` em tabela inteira sem necessidade
- `+ 0` para tratar BLANK
- repetição de lógica
- mistura de escalas em índices

---

### 🔹 Checklist de qualidade
Antes de publicar uma medida:
- nome padronizado
- semântica correta
- performance adequada
- dependência respeitada

---

## 🚀 Benefícios

- Governança do modelo
- Padronização entre equipes
- Facilidade de auditoria
- Redução de dívida técnica
- Sustentabilidade do BI

---

# 🔗 3. Relação entre os dois arquivos

| Arquivo | Papel |
|--------|------|
| Medidas por camadas | Implementação prática |
| Guia enterprise | Regras e governança |

👉 Um define **como fazer**
👉 O outro define **como deve ser feito**

---

# 🧠 4. Como usar no dia a dia

### 📊 No Power BI / Tabular Editor
- usar o arquivo de medidas como base de implementação
- seguir o guia para criar novas medidas

---

### 📘 No Obsidian
- usar esta nota como referência central
- linkar com:
  - projetos de BI
  - dashboards
  - indicadores estratégicos

---

### 🧩 Em novos projetos
- replicar a estrutura de camadas
- aplicar naming convention desde o início
- evitar retrabalho

---

# ⚠️ 5. Pontos de atenção

[Inferência]
- O modelo depende da qualidade do modelo dimensional (relacionamentos e tipos de dados)
- Índices como IQO exigem validação metodológica contínua
- Uso de "-" como data pode indicar problema de modelagem

---

# 🏁 Conclusão

Esses dois arquivos representam a evolução de um modelo:

### 🔹 De:
Modelo funcional

### 🔹 Para:
Modelo **estruturado, governado e escalável**

---

# 💡 Insight final

Um bom modelo responde perguntas.  
Um modelo enterprise **permite que novas perguntas sejam feitas sem quebrar o sistema**.
