# Prompt para Criação da Figura 2 — Ciclo de Governança do IGRO

> **Descrição visual requerida:** Diagrama cíclico que representa o fluxo de transformação de dados operacionais da ouvidoria em instrumento de governança

---

## **PROMPT EXECUTIVO**

```
Crie um diagrama cíclico que represente o Ciclo de Governança do IGRO — 
o fluxo de transformação de manifestações cidadãs em decisões de gestão 
de risco e melhoria contínua.

CICLO OPERACIONAL (6 ETAPAS):

1. MANIFESTAÇÃO
   ↓
2. KRIs (Indicadores-Chave de Risco)
   ↓
3. IGRO (Índice Composto)
   ↓
4. MATRIZ DE RISCOS
   ↓
5. DECISÃO / AÇÃO
   ↓
6. MELHORIA CONTÍNUA
   ↓ [retorna a 1]

PERIODICIDADE: Ciclo quadrimestral

ATORES/RESPONSÁVEIS:
- Etapa 1: Cidadão + Ouvidoria (SGOe)
- Etapas 2-3: Proprietário do risco / Analista
- Etapa 4: Comitê Setorial / GT Riscos
- Etapa 5: Gestão setorial / Comitê
- Etapa 6: Executivo / Operacional
```

---

## **ESPECIFICAÇÕES DETALHADAS**

### **1. ESTRUTURA E LAYOUT**

**Formato:** Diagrama circular/cíclico com fluxo unidirecional no sentido horário

**Disposição das etapas:**
```
           [MANIFESTAÇÃO]
                ↓
     [KRIs]          [MELHORIA]
       ↓                ↑
   [IGRO] ←→ [MATRIZ] ←→ [DECISÃO]
```

**Alternativa (espiral):** Se preferir dinamismo, usar formato de espiral expandida para sugerir melhoria contínua e evolução

**Profundidade visual:** 
- Use perspectiva ligeira (2.5D) ou manter plano (2D)
- Prioridade: clareza sobre estética

---

### **2. ELEMENTOS VISUAIS POR ETAPA**

#### **Etapa 1: MANIFESTAÇÃO**
- **Ícone:** Ícone de usuário + balão de fala ou envelope
- **Cor:** Azul claro (#3498DB) — origem/entrada
- **Descrição:** "109.338 manifestações registradas"
- **Dados:** "51 órgãos | 2024-2025"

#### **Etapa 2: KRIs**
- **Ícone:** 5 indicadores lado a lado (ou gráfico de painel)
- **Cor:** Cinza-azulado (#34495E)
- **Descrição:** "5 Indicadores-Chave de Risco"
- **Componentes destacados:**
  - TMR + PMA (Tempestividade)
  - RP + %RI + NR (Qualidade)

#### **Etapa 3: IGRO**
- **Ícone:** Medidor/velocímetro ou semáforo
- **Cor:** Verde → Amarelo → Laranja → Vermelho (representando faixas de risco)
- **Descrição:** "Índice Composto [0–1]"
- **Legenda de cores:**
  - Verde (0,80–1,00) = Risco Baixo
  - Amarelo (0,60–0,79) = Risco Moderado
  - Laranja (0,40–0,59) = Risco Alto
  - Vermelho (0,00–0,39) = Risco Crítico

#### **Etapa 4: MATRIZ DE RISCOS**
- **Ícone:** Matriz 2×2 ou tabela (Riscos 0044 e 0046)
- **Cor:** Roxo/lavanda (#8E44AD)
- **Descrição:** "Avaliação na Matriz CGE"
- **Nota:** Conectar visualmente ao IGRO (média geométrica dos sub-índices)

#### **Etapa 5: DECISÃO / AÇÃO**
- **Ícone:** Pessoa em discussão, check mark, ou símbolo de aprovação
- **Cor:** Laranja (#E67E22)
- **Descrição:** "Decisão Comitê Setorial"
- **Possíveis ações:** Monitoramento | Plano de Ação | Intervenção | Escalação

#### **Etapa 6: MELHORIA CONTÍNUA**
- **Ícone:** Seta circular, gráfico crescente, ou engrenagem
- **Cor:** Verde-escuro (#27AE60)
- **Descrição:** "Ciclo quadrimestral"
- **Destaque:** Mostrar que volta para Etapa 1 (realimentação)

---

### **3. SETAS E CONECTORES**

**Tipo de fluxo:**
- Use setas robustas (espessura: 3–5px)
- Mostrar direcionamento claro (apenas sentido horário)
- Cores das setas:
  - Cinza médio (#95A5A6) entre etapas operacionais
  - Verde (#27AE60) na volta para Manifestação (reforçar ciclo)

**Rótulos nas setas (opcional):**
- "Extração" (Manifestação → KRIs)
- "Cálculo" (KRIs → IGRO)
- "Integração" (IGRO → Matriz)
- "Avaliação" (Matriz → Decisão)
- "Execução" (Decisão → Melhoria)
- "Implementação" (Melhoria → Manifestação)

---

### **4. INFORMAÇÕES COMPLEMENTARES**

#### **Cronograma visível:**
Adicionar faixa lateral mostrando prazos (quadrimestral):
```
Dia 1–5 pós-trimestre: Coleta KRIs
Dia 6–10: Cálculo IGRO
Dia 11–15: Análise (Compliance)
Dia 16–30: Aprovação Comitê
Dia 31–120: Execução/Melhoria
```

#### **Referências normativas (rodapé ou legenda):**
- ISO 31000:2018 (Gestão de Riscos)
- COSO (Governança)
- Lei 13.460/2017 (Direitos do Usuário)
- Matriz de Gestão de Riscos CGE-GO

#### **Responsáveis por etapa (opcional, em pequeno):**
```
[Cidadão]  [Proprietário]  [Compliance]  [Comitê]  [Executivo]
```

---

### **5. PALETA DE CORES RECOMENDADA**

| Elemento | Cor | Hex | Significado |
|---|---|---|---|
| Fundo | Branco/cinza claro | #F8F9FA | Neutro |
| Manifestação | Azul claro | #3498DB | Origem |
| KRIs | Cinza-azulado | #34495E | Transição |
| IGRO | Multicolor (semáforo) | Verde/Amarelo/Laranja/Vermelho | Risco |
| Matriz | Roxo | #8E44AD | Integração |
| Decisão | Laranja | #E67E22 | Ação |
| Melhoria | Verde-escuro | #27AE60 | Evolução |
| Setas | Cinza médio | #95A5A6 | Fluxo |
| Setas retorno | Verde | #27AE60 | Ciclo |
| Texto | Preto/cinza escuro | #2C3E50 | Legibilidade |

---

### **6. TIPOGRAFIA E HIERARQUIA**

**Títulos de etapas:**
- Fonte: Sans-serif (Helvetica, Arial, Roboto)
- Peso: Bold (600–700)
- Tamanho: 14–16px
- Cor: Preto (#2C3E50)

**Descrições:**
- Tamanho: 11–12px
- Peso: Regular (400)
- Cor: Cinza escuro (#34495E)

**Dados/números:**
- Tamanho: 10px
- Peso: Light (300)
- Cor: Cinza médio (#7F8C8D)

**Legenda:**
- Tamanho: 9–10px
- Posição: Rodapé ou lateral direita
- Inclua: Cronograma, atores, referências normativas

---

### **7. DIMENSÕES E RESOLUÇÃO**

**Proporção:** 16:9 (paisagem) ou 1:1 (quadrado, para slides)

**Tamanho mínimo:** 800px × 600px (para apresentação)

**Tamanho print:** 1600px × 1200px (300 dpi para A4)

**Formato de exportação:**
- [ ] PNG (RGB, transparência, 300 dpi)
- [ ] SVG (vetorizado, editável)
- [ ] PDF (alta qualidade)
- [ ] Arquivo nativo (Figma, Draw.io, PowerPoint) para futuras edições

---

### **8. VARIAÇÕES SUGERIDAS**

**Variação A: Ciclo simples (minimalista)**
- Apenas 6 caixas + setas + cores
- Sem ícones
- Texto descritivo mínimo
- **Uso:** Slides executivos, relatórios gerenciais

**Variação B: Ciclo detalhado (técnico)**
- Incluir ícones
- Adicionar responsáveis por etapa
- Cronograma lateral
- Referências normativas
- **Uso:** Documentação técnica, treinamento

**Variação C: Ciclo interativo (para dashboard Power BI)**
- Cores dinâmicas baseadas em status real do IGRO
- Números atualizáveis (ex: "109.338 manifestações")
- Links para dados detalhados
- **Uso:** Dashboard executivo, monitoramento em tempo real

---

### **9. ELEMENTOS OPCIONAIS (Add-ons)**

**Se quiser adicionar contexto:**

- [ ] **Caixa de "Atores"** lateral: Cidadão → Ouvidoria → Proprietário → Comitê → Executivo
- [ ] **Caixa de "Ferramentas"** inferior: SGOe | Excel | Power BI | Matriz de Riscos
- [ ] **Legenda de tempo**: "Ciclo: 30–45 dias" destacado
- [ ] **Indicador de frequência**: "Quadrimestral" em destaque visual
- [ ] **Mini semáforo**: Exemplo de como cores mudam ao longo do ciclo
- [ ] **Zoom em IGRO**: Detalhe visual mostrando Sub_T e Sub_Q dentro do índice

---

### **10. VALIDAÇÃO E QUALIDADE**

**Antes de finalizar, verificar:**

- [ ] Ciclo segue sentido horário consistentemente
- [ ] Todas as 6 etapas estão claramente identificadas
- [ ] Cores são distinguíveis para daltônicos (teste WCAG AA)
- [ ] Textos estão em português brasileiro e sem erros
- [ ] Ícones são consistentes em estilo e peso visual
- [ ] Setas indicam fluxo unidirecional clara
- [ ] Resolução adequada (não pixelado, não muito grande)
- [ ] Funciona em preto e branco (se impressão sem cor)
- [ ] Arquivo editável está disponível (não apenas PNG)

---

### **11. CASOS DE USO**

**Onde esta figura aparece:**

1. **Seção 2.2** — Referencial Teórico (Gestão de Riscos)
2. **Apresentação ao Comitê Setorial** — Para validação da metodologia
3. **Documentação de processos** — Manual de operação do IGRO
4. **Treinamento de usuários** — Explicar fluxo ao GT Riscos
5. **Dashboard Power BI** — Como versão interativa

---

### **12. PRÓXIMAS ETAPAS APÓS CRIAÇÃO**

1. Validar com Comitê Setorial
2. Criar versão simplificada (sem detalhes) para slides
3. Criar versão com dados reais (números atualizados)
4. Desenvolver versão interativa para Power BI
5. Traduzir para inglês (se necessário para publicação)

---

## **RESUMO DO PROMPT**

**Tipo de diagrama:** Cíclico com 6 etapas  
**Estilo:** Profissional, científico, auditável  
**Foco:** Mostrar transformação de dados em ação  
**Primoridades:** Clareza > Estética  
**Público:** Gestores públicos, Comitê Setorial, pesquisadores

---

## **FERRAMENTAS RECOMENDADAS**

| Ferramenta | Vantagens | Tempo |
|---|---|---|
| **Figma** | Colaborativo, versões, exportação | 45–60 min |
| **Draw.io** | Gratuito, intuitivo, templates | 30–40 min |
| **PowerPoint** | Integrado, fácil edição pós-criação | 20–30 min |
| **Miro** | Interativo, prototipagem | 45–60 min |
| **Python (Plotly/Graphviz)** | Automatizável, reproduzível | 30–50 min |
| **Adobe Illustrator** | Polimento final, qualidade | 60–90 min |

---

## **RESULTADO ESPERADO**

Um diagrama cíclico claro, legível, e facilmente integrável ao artigo que:

✅ Mostra o fluxo completo: Manifestação → Melhoria Contínua → Manifestação  
✅ Identifica as 6 etapas e responsáveis  
✅ Destaca a periodicidade quadrimestral  
✅ Usa cores semanticamente (verde = melhoria, vermelho = risco)  
✅ Integra referências normativas (ISO 31000, COSO)  
✅ É acessível (WCAG AA mínimo)  
✅ Funciona em preto e branco  
✅ É editável para futuras atualizações

---

**Pronto para criar? Qual ferramenta você prefere usar?**
