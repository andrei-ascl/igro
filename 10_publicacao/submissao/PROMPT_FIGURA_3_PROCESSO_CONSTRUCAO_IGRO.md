# Prompt para Criação da Figura 3 — Processo de Construção do IGRO

> **Descrição visual requerida:** Diagrama linear que represente o fluxo de transformação dos dados operacionais brutos em índice composto de risco para uso gerencial.

---

## **PROMPT EXECUTIVO**

```text
Crie um diagrama linear e horizontal que represente o Processo de Construção do IGRO,
mostrando como os dados operacionais brutos da ouvidoria são transformados em um índice
composto de gestão de riscos.

FLUXO PRINCIPAL (5 ETAPAS):

1. DADOS BRUTOS
   ↓
2. KRIs
   ↓
3. NORMALIZAÇÃO
   ↓
4. AGREGAÇÃO
   ↓
5. IGRO

Rótulos completos das etapas:
- Dados brutos
- KRIs (Indicadores-Chave de Risco)
- Normalização (Distância à Meta com Goalposts)
- Agregação (Média Geométrica Ponderada)
- IGRO (Índice de Gestão de Riscos de Ouvidoria)

Objetivo visual:
mostrar claramente inputs, transformações analíticas e output final,
com linguagem adequada para artigo acadêmico e boa legibilidade em página A4.
```

---

## **ESPECIFICAÇÕES DETALHADAS**

### **1. ESTRUTURA E LAYOUT**

**Formato:** Fluxo linear horizontal, da esquerda para a direita.

**Estrutura sugerida:**

```text
[DADOS BRUTOS] → [KRIs] → [NORMALIZAÇÃO] → [AGREGAÇÃO] → [IGRO]
```

**Alternativa aceitável:**
- fluxo horizontal com caixas retangulares conectadas;
- ou funil analítico em cinco blocos sequenciais;
- evitar forma cíclica, radial ou muito decorativa.

**Prioridade visual:**
- clareza metodológica;
- leitura rápida;
- aparência técnica e acadêmica.

---

### **2. CONTEÚDO DE CADA ETAPA**

#### **Etapa 1: DADOS BRUTOS**

**Título:** `Dados brutos`

**Subtítulo sugerido:**
- `Registros operacionais do SGOe`

**Elementos internos possíveis:**
- manifestações registradas;
- pesquisas de satisfação;
- respostas insatisfatórias;
- datas, protocolos, órgãos, status.

**Exemplos de microtexto:**
- `109.338 manifestações`
- `51 órgãos`
- `2024–2025`

**Ícone sugerido:**
- banco de dados;
- tabela;
- arquivo com registros.

**Cor sugerida:** azul médio ou azul institucional.

---

#### **Etapa 2: KRIs**

**Título:** `KRIs`

**Subtítulo sugerido:**
- `Indicadores-Chave de Risco`

**Listar os cinco KRIs de forma compacta:**
- TMR
- PMA
- RP
- %RI
- NR

**Agrupamentos internos opcionais:**
- `Tempestividade: TMR + PMA`
- `Qualidade: RP + %RI + NR`

**Ícone sugerido:**
- painel analítico;
- barras/medidores;
- cinco indicadores resumidos.

**Cor sugerida:** cinza-azulado.

---

#### **Etapa 3: NORMALIZAÇÃO**

**Título:** `Normalização`

**Subtítulo obrigatório:**
- `Distância à Meta com Goalposts`

**Mensagem central da etapa:**
- transformar indicadores com escalas diferentes em scores comparáveis entre `0` e `1`.

**Elementos que podem aparecer dentro da caixa:**
- `Meta = score 1,0`
- `Goalpost = score 0,0`
- `Escala comum: 0–1`

**Exemplos discretos opcionais:**
- TMR: meta `5 dias`, goalpost `10 dias`
- RP: meta `70%`, goalpost `50%`

**Ícone sugerido:**
- régua;
- barra de escala;
- conversão numérica.

**Cor sugerida:** roxo suave ou azul-violeta.

---

#### **Etapa 4: AGREGAÇÃO**

**Título:** `Agregação`

**Subtítulo obrigatório:**
- `Média geométrica ponderada`

**Mensagem central da etapa:**
- combinar os scores dos KRIs em um índice sintético;
- reduzir compensação excessiva entre dimensões.

**Elementos opcionais:**
- pesos dos KRIs;
- pesos dos subíndices;
- referência à não compensabilidade.

**Se desejar detalhar:**
- `Sub-IGRO_T`
- `Sub-IGRO_Q`
- `pesos globais dos 5 KRIs`

**Ícone sugerido:**
- engrenagem analítica;
- função matemática;
- blocos convergindo.

**Cor sugerida:** laranja moderado.

---

#### **Etapa 5: IGRO**

**Título:** `IGRO`

**Subtítulo sugerido:**
- `Índice composto final`

**Mensagem central da etapa:**
- output executivo para monitoramento de risco.

**Elementos opcionais:**
- faixa `0–1`;
- semaforização por risco;
- uso gerencial e comparativo entre órgãos.

**Legenda opcional de risco:**
- verde = baixo
- amarelo = moderado
- laranja = alto
- vermelho = crítico

**Ícone sugerido:**
- velocímetro;
- semáforo;
- scorecard final.

**Cor sugerida:** gradiente de risco ou verde em destaque com apoio de faixas semafóricas.

---

### **3. SETAS E CONECTORES**

**Estilo das setas:**
- espessura média;
- direção única da esquerda para a direita;
- visual limpo e acadêmico.

**Textos opcionais sobre as setas:**
- `extração`
- `cálculo`
- `padronização`
- `síntese`

**Sugestão de uso:**
- não rotular todas as setas se isso poluir a figura;
- priorizar limpeza visual.

---

### **4. INFORMAÇÕES COMPLEMENTARES**

#### **Legenda inferior opcional**

Adicionar pequena legenda com:

- `Fonte: elaboração própria a partir do modelo metodológico do IGRO`
- `Base conceitual: OCDE/JRC (2008), ISO 31000:2018`

#### **Nota metodológica opcional**

Inserir discretamente abaixo da figura:

`Os dados brutos são convertidos em cinco KRIs, normalizados em escala comum de 0 a 1 e posteriormente agregados por média geométrica ponderada para composição do IGRO.`

---

### **5. PALETA DE CORES RECOMENDADA**

| Elemento | Cor sugerida | Hex aproximado | Função |
|---|---|---|---|
| Fundo | Branco ou cinza muito claro | `#F8F9FA` | Neutralidade |
| Dados brutos | Azul | `#3A86FF` | Origem dos dados |
| KRIs | Azul petróleo / cinza-azulado | `#355070` | Indicadores |
| Normalização | Roxo suave | `#6D597A` | Transformação |
| Agregação | Laranja | `#E07A5F` | Síntese |
| IGRO | Verde com apoio semafórico | `#2A9D8F` | Resultado final |
| Setas | Cinza médio | `#98A2B3` | Fluxo |
| Texto | Cinza escuro | `#1F2937` | Legibilidade |

---

### **6. TIPOGRAFIA E HIERARQUIA**

**Títulos das caixas:**
- sans-serif;
- negrito;
- tamanho maior que o texto secundário;
- alta legibilidade em impressão.

**Subtítulos e descrições:**
- tamanho intermediário;
- cor secundária;
- no máximo 2 a 3 linhas por caixa.

**Regra importante:**
- evitar excesso de texto;
- privilegiar palavras-chave e microdescrições.

---

### **7. DIMENSÕES E SAÍDA**

**Proporção recomendada:**
- paisagem horizontal;
- ideal para artigo e apresentação.

**Tamanho sugerido:**
- `1600 × 900 px` ou superior para boa nitidez;
- versão vetorial preferencial (`SVG` ou `PDF`).

**Formatos desejáveis:**
- `SVG`
- `PNG`
- `PDF`
- arquivo editável (`Figma`, `PowerPoint`, `Draw.io` ou equivalente)

---

### **8. VARIAÇÕES SUGERIDAS**

**Variação A — Acadêmica minimalista**
- caixas retangulares;
- poucas cores;
- sem ícones;
- ênfase em legibilidade e sobriedade.

**Variação B — Técnica ilustrada**
- ícones discretos em cada etapa;
- destaque visual para normalização e agregação;
- legenda inferior metodológica.

**Variação C — Executiva**
- visual mais limpo e sintético;
- foco em narrativa: dado → indicador → índice.

---

### **9. RESTRIÇÕES IMPORTANTES**

- Não usar visual excessivamente publicitário.
- Não usar 3D exagerado, sombras fortes ou efeitos decorativos desnecessários.
- Não transformar o diagrama em fluxograma burocrático complexo.
- Não usar texto demais dentro das caixas.
- Não perder a lógica sequencial do processo analítico.

---

### **10. CHECKLIST DE VALIDAÇÃO**

- [ ] O fluxo vai claramente de `Dados brutos` até `IGRO`
- [ ] As cinco etapas estão nomeadas corretamente
- [ ] A normalização menciona explicitamente `Distância à Meta com Goalposts`
- [ ] A agregação menciona explicitamente `Média Geométrica Ponderada`
- [ ] Os cinco KRIs aparecem ou são ao menos referenciados
- [ ] A figura funciona em tamanho reduzido no artigo
- [ ] As cores preservam contraste e legibilidade
- [ ] O resultado final tem aparência acadêmica e profissional

---

## **VERSÃO CURTA DO PROMPT**

```text
Crie uma figura acadêmica em formato de fluxo linear horizontal para representar o
Processo de Construção do IGRO. A figura deve mostrar cinco etapas sequenciais:
Dados brutos → KRIs → Normalização → Agregação → IGRO.

Use os seguintes rótulos completos:
- Dados brutos
- KRIs (Indicadores-Chave de Risco)
- Normalização (Distância à Meta com Goalposts)
- Agregação (Média Geométrica Ponderada)
- IGRO (Índice de Gestão de Riscos de Ouvidoria)

Na etapa de KRIs, referencie os cinco indicadores: TMR, PMA, RP, %RI e NR.
Na etapa de normalização, destaque a conversão para escala 0–1.
Na etapa de agregação, destaque a média geométrica ponderada.
No resultado final, represente o IGRO como índice composto para monitoramento de risco.

Estilo visual: técnico, limpo, acadêmico, com boa legibilidade em artigo científico.
Formato preferencial: horizontal, com caixas conectadas por setas da esquerda para a direita.
```
