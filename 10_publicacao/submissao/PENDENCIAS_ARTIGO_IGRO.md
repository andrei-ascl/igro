# Sugestões e Pendências — Artigo IGRO v2

> **Data de compilação:** 2026-05-28  
> **Status:** Compilação de sugestões apresentadas na revisão de refinamento  
> **Prioridade:** Organizada por seção e criticidade

---

## 📋 Resumo Executivo

**Total de pendências:** 23 itens  
**Implementadas nesta sessão:** 7  
**Pendentes:** 16

| Categoria | Pendentes | Prioridade |
|---|---|---|
| Figuras/Diagramas | 6 | Alta |
| Tabelas de dados | 3 | Alta |
| Dados faltantes (Goalposts) | 1 | Crítica |
| Refinamentos secionais | 4 | Média |
| Dados de sensibilidade | 1 | Alta |
| Referências (dados completos) | 2 | Média |

---

## 🎯 IMPLEMENTADO NESTA SESSÃO

✅ **Seção 2.1** — Citações Santos et al. (2019) e Andrade (2026) sobre papéis multidimensionais  
✅ **Seção 2.1** — Citação de impacto econômico (R$ 2 bilhões, PCP 2019-2025)  
✅ **Seção 2.2** — Citação COSO (2017) sobre gestão de riscos estratégica  
✅ **Seção 2.2** — Citação Goodhart (1975) — versão rigorosa ("regularidade estatística colapsará...")  
✅ **Seção 3.3** — Citação OCDE/JRC sobre transparência de goalposts em auditorias  
✅ **Seção 3.3** — Citação OCDE/JRC sobre média geométrica e não-compensabilidade  
✅ **Seção 3.6** — Limitações amostrais (validade estatística em pequenas amostras)  
✅ **Referências** — Reformatação padrão APA 7ª edição

---

## ⚠️ PENDÊNCIAS CRÍTICAS

### **P1: Goalposts de Qualidade (KRIs 3, 4, 5)**

**Localização:** Seção 3.3, Tabela de Parâmetros de Normalização (linhas 268–270)

**O que falta:**
```
| RP  | **[INSERIR DADOS: meta % e limite %]** | — | Direta (maior = melhor) |
| %RI | **[INSERIR DADOS: meta % e limite %]** | — | Inversa (menor = melhor) |
| NR  | **[INSERIR DADOS: meta NPS e limite NPS]** | — | Direta (maior = melhor) |
```

**Ação requerida:**
- Confirmar valores utilizados na normalização para KRI 3 (Resolutividade Percebida)
- Confirmar valores para KRI 4 (% Respostas Insatisfatórias)
- Confirmar escala de NPS e limites para KRI 5 (Nota de Recomendação)
- Identificar fonte: benchmark interno, literatura, ou documentação técnica

**Impacto:** Sem esses dados, a Tabela 3.3 fica incompleta e compromete reprodutibilidade

---

### **P2: Dados de Sensibilidade (Análise de Robustez)**

**Localização:** Seção 3.5 (linhas 319–333)

**O que falta:**

**Teste 1 — Variação de pesos:**
```
[INSERIR DADOS: Tabela com IGRO recalculado para os 51 órgãos nos três cenários:
- Cenário 1: Ponderação uniforme (w = 0,20 cada KRI)
- Cenário 2: Qualidade prioritária (wRP=0,25; wNR=0,25; w%RI=0,20; wTMR=0,15; wPMA=0,15)
- Cenário 3: Tempestividade prioritária (wTMR=0,25; wPMA=0,25; wRP=0,20; w%RI=0,15; wNR=0,15)

Incluir: Coeficiente de correlação de postos de Spearman (ρₛ) entre rankings, com p-valor]
```

**Teste 2 — Agregação alternativa:**
```
[INSERIR DADOS: Comparação IGRO (média geométrica) vs. média aritmética por órgão.
Identificar casos de mudança de faixa de risco (Verde→Amarelo, etc.)]
```

**Teste 3 — Bootstrap (Perturbação aleatória):**
```
[INSERIR DADOS: Intervalos de confiança (IC 90%) para IGRO dos 10 maiores e 10 menores órgãos.
Verificar sobreposição significativa entre posições no ranking.]
```

**Ação requerida:**
- Trazer base de KRIs normalizados por órgão (51 linhas)
- Executar recálculos com 3 cenários de ponderação
- Executar 1.000 iterações de bootstrap com variação aleatória ±10% nos pesos

**Impacto:** Crítico para validar robustez metodológica — exigido por OCDE/JRC

---

## 📊 FIGURAS E DIAGRAMAS (Não implementadas)

### **F1: Figura 1 — Estrutura Conceitual do IGRO**

**Localização:** Seção 1 (Introdução), linha 52

**Descrição requerida:**
- Diagrama hierárquico (top-down)
- IGRO no topo → Sub-IGRO_T (40%) e Sub-IGRO_Q (60%) → 5 KRIs
- Mostrar pesos locais e globais
- Cores por dimensão (azul = Tempestividade; verde = Qualidade)
- Incluir escalas de semaforização (Verde/Amarelo/Laranja/Vermelho)

**Prompt disponível:** Consultado na conversa anterior (seção "Prompt para Criação da Figura 1")

**Ferramentas sugeridas:** Figma, Draw.io, PowerPoint, Python (Graphviz)

**Tempo estimado:** 30–45 minutos

---

### **F2: Figura 2 — Ciclo de Governança do IGRO**

**Localização:** Seção 2.2, linha 161

**Descrição:**
- Fluxo cíclico: Manifestação → KRIs → IGRO → Matriz de Riscos → Decisão → Melhoria contínua
- Formato: Diagrama circular ou em espiral
- Indicar frequência: quadrimestral
- Conectar ao framework ISO 31000

---

### **F3: Figura 3 — Processo de Construção do IGRO**

**Localização:** Seção 3.3, linha 284

**Descrição:**
- Fluxo linear: Dados brutos → KRIs → Normalização (Distância à Meta) → Agregação (Média Geométrica) → IGRO
- Mostrar inputs, transformações e outputs em cada etapa

---

### **F4: Figura 5 — Fatores Determinantes para Elevado IGRO**

**Localização:** Seção 5.2, linha 531

**Descrição:**
- Cinco fatores críticos: (1) Integração tecnológica; (2) Capacidade técnica; (3) Comunicação; (4) Conformidade; (5) Monitoramento
- Formato: Radar chart, matriz de impacto ou ícones com pesos

---

### **F5: Figura 6 — Modelo Final de Governança Orientada por Risco**

**Localização:** Seção 6 (Conclusão), linha 563

**Descrição:**
- Fluxo final: Cidadão → Ouvidoria → KRIs → IGRO → Governança → Melhoria de políticas públicas
- Integrar com referencial ISO 31000 e COSO

---

### **F6: Gráfico 1 — Distribuição de Manifestações por Classe Operacional**

**Localização:** Seção 4.1, linha 379

**Dados disponíveis:**
- Cl.1: 47.821 manifestações (3 órgãos)
- Cl.2: 45.909 (7 órgãos)
- Cl.3: 12.735 (7 órgãos)
- Cl.4: 5.355 (15 órgãos)
- Cl.5: 819 (20 órgãos)

**Formato sugerido:** Gráfico de barras com % de concentração

---

### **F7: Gráfico 2 — Distribuição de TMR por Classe (Boxplot)**

**Localização:** Seção 4.2, linha 405

**Dados requeridos:**
- TMR médio por classe + distribuição (mín, Q1, mediana, Q3, máx)
- Adicionar valor consolidado (6,8 dias)

---

### **F8: Gráfico 3 — Percentual de Manifestações em Atraso (PMA)**

**Localização:** Seção 4.2, linha 411

**Dados requeridos:**
- PMA por classe e consolidado (2,3%)
- Mostrar desvio da meta (≤ 2,0%)

---

## 📋 TABELAS (Não implementadas)

### **T1: Tabela 1 — Principais Referenciais Normativos do IGRO**

**Localização:** Seção 2.1, linha 122

**Conteúdo:**
| Norma | Função |
|:------|:-------|
| Lei 13.460/2017 | Direitos do usuário |
| Lei 12.527/2011 | Acesso à informação |
| LGPD | Proteção de dados |
| ISO 31000 | Gestão de riscos |
| COSO | Governança e controle |
| Decreto Est. 10.466/2024 | Estruturação de ouvidorias (Goiás) |

---

### **T2: Tabela 2 — Etapas Metodológicas OCDE/JRC Aplicadas ao IGRO**

**Localização:** Seção 2.2, linha 187

**Conteúdo esperado:**
| Etapa OCDE/JRC | Aplicação no IGRO | Referência |
|:---|:---|:---|
| Seleção de indicadores | 5 KRIs definidos (TMR, PMA, RP, %RI, NR) | Desenho IGRO (arquivo 10) |
| Normalização | Distância à meta com goalposts | Seção 3.3 |
| Ponderação | Sub_T 40%, Sub_Q 60% | Desenho IGRO |
| Agregação | Média aritmética (intra) + geométrica (inter) | Seção 3.3 |
| Sensibilidade | 3 testes: variação pesos, método, bootstrap | Seção 3.5 |

---

### **T3: Tabela 3 — KRIs do IGRO (já parcialmente preenchida)**

**Localização:** Seção 3.2, linhas 219–227

**Status:** Estrutura presente, faltam detalhes nos indicadores de qualidade

---

### **T4: Tabela de Distribuição Operacional da Rede**

**Localização:** Seção 4.1, linha 381

**Status:** Parcialmente preenchida — confirmar IGRO médio por classe

---

### **T5: Tabela de Taxa de Resposta à Pesquisa**

**Localização:** Seção 3.6, linhas 349–355

**Conteúdo:**
| Classe operacional | Manifestações (n) | Respondentes pesquisa (n) | Taxa resposta (%) | Amostra adequada? |
|:---|:---|:---|:---|:---|
| Cl.1 | ... | ... | ... | Sim/Não |
| Cl.2 | ... | ... | ... | ... |
| Cl.3 | ... | ... | ... | ... |
| Cl.4 | ... | ... | ... | ... |
| Cl.5 | ... | ... | ... | ... |

**Nota:** Adicionar coluna "Amostra adequada?" (Sim/Não) baseada em limiar mínimo (ex: n ≥ 30)

---

## 📚 REFINAMENTOS SECIONAIS NÃO IMPLEMENTADOS

### **R1: Seção 3.1 — Rigor Metodológico de Pesquisa Exploratória**

**O que adicionar:**
- Citação sobre validade de estudos exploratórios (ex: Yin, 2014 — já adicionado à Bibliografia)
- Fundamentar por que abordagem descritiva-exploratória é apropriada para novo indicador
- Conectar com capítulo de Metodologia

**Texto sugerido:**
> "Yin (2014) argumenta que estudos exploratórios possuem validade metodológica mesmo sem pretensão inferencial causal, especialmente quando se trata de construtos novos ou contextos ainda não estudados. No caso do IGRO, essa abordagem é justificada pela inexistência de benchmarks consolidados para indicadores compostos de ouvidoria pública..."

---

### **R2: Seção 3.4 — Análise de Clustering (Agrupamento por Complexidade)**

**O que adicionar:**
- Fundamentar agrupamento em classes operacionais
- Citar Meyer & Rowan (1977) ou Mintzberg sobre tipologias organizacionais
- Explicar por que comparação dentro de clusters é mais robusta

**Texto sugerido:**
> "A segmentação em classes operacionais responde a um princípio conhecido em análise organizacional: unidades com diferentes níveis de complexidade, capacidade técnica e volume de demanda operam sob lógicas distintas. Meyer & Rowan (1977) demonstram que a comparação entre organizações com estruturas heterogêneas pode mascarar fatores contextuais relevantes. Assim, o agrupamento em cinco classes permitiu identificação de padrões específicos em cada estrato..."

---

### **R3: Seção 3.5 — Importância Metodológica da Sensibilidade**

**O que adicionar:**
- Citar Saltelli et al. (2008) sobre indicadores compostos
- Fundamentar por que sensibilidade é crítica para indicadores de política pública

**Texto sugerido:**
> "Saltelli et al. (2008) destacam que a análise de sensibilidade em modelos de suporte à decisão é etapa indispensável para verificar se os resultados são artefatos da metodologia ou refletem genuinamente a realidade observada. Sem aprovação em testes de robustez, um índice composto não é confiável para alocação de recursos ou definição de políticas..."

---

### **R4: Seção 3.6 — Tratamento Diferenciado para Classes 4 e 5**

**O que adicionar:**
- Recommendation para próximas rodadas: exclusão temporária ou ajuste estatístico
- Sugerir métodos: estimativa bayesiana, intervalo de confiança ampliado
- Criar nota de rodapé nos Resultados alertando sobre órgãos com amostra insuficiente

**Texto sugerido:**
> "Para melhorias futuras, recomenda-se implementar tratamento estatístico diferenciado para órgãos com amostra de respondentes inferior a 30 (Classes 4 e 5). Alternativas metodológicas incluem: (a) exclusão temporária do cálculo individual de NPS; (b) aplicação de estimativa bayesiana com prior informativo baseado na rede; (c) ampliação de intervalos de confiança refletindo incerteza amostral. Essa medida aumentaria a confiabilidade dos indicadores de qualidade para órgãos de pequeno porte."

---

## 📖 REFERÊNCIAS — DADOS INCOMPLETOS

### **REF1: Andrade (2026)**

**Citado como:**
- "sensor institucional de riscos e vetor de transformação administrativa"
- "economia total de mais de R$ 2 bilhões" (PCP 2019-2025)

**Dados faltantes:**
- [ ] Primeiro nome completo do autor
- [ ] Título exato da obra
- [ ] Editora
- [ ] Cidade de publicação
- [ ] Número de páginas (se necessário)
- [ ] DOI (se disponível)

**Formato esperado (APA):**
```
Andrade, [Inicial(is)]. (2026). [Título completo da obra]. [Editora].
```

---

### **REF2: Santos et al. (2019)**

**Citado como:**
- "As ouvidorias públicas visam promover a melhoria da qualidade do serviço público..."
- Menciona "aspectos funcionais, gerenciais e aspectos de cidadania"

**Dados faltantes:**
- [ ] Primeiro nome do autor principal
- [ ] Nomes dos co-autores (et al. — quantos?)
- [ ] Título exato
- [ ] Editora ou periódico
- [ ] Número de páginas
- [ ] DOI (se periódico)

**Formato esperado (APA):**
```
Santos, [Inicial]. et al. (2019). [Título]. [Periódico ou Editora], [volume(issue)], [páginas].
```

---

## 🔄 CHECKLIST DE PRÓXIMAS AÇÕES

### **Fase 1: Dados Críticos (AGORA)**
- [ ] Obter e preencher Goalposts de RP, %RI, NR (P1)
- [ ] Confirmar dados de Andrade (2026) e Santos et al. (2019)
- [ ] Trazer base de KRIs normalizados para análise de sensibilidade

### **Fase 2: Análise (1-2 semanas)**
- [ ] Executar 3 testes de sensibilidade (Seção 3.5)
- [ ] Gerar tabelas de distribuição operacional
- [ ] Compilar dados de taxa de resposta por classe

### **Fase 3: Visualização (Paralelo)**
- [ ] Gerar Figuras 1–6 (usando ferramenta de preferência)
- [ ] Gerar Gráficos 1–3 (usando R, Python, Excel ou BI)
- [ ] Validar qualidade de resolução (300 dpi para impressão)

### **Fase 4: Refinamento Final (1 semana)**
- [ ] Implementar refinamentos secionais (R1–R4)
- [ ] Adicionar notas de rodapé nos Resultados (alertas de amostra)
- [ ] Revisão final de coerência e citações

### **Fase 5: Produção (Final)**
- [ ] Validar todas as referências em APA
- [ ] Gerar PDF final com figuras integradas
- [ ] Submeter para revisão do Comitê

---

## 📝 NOTAS E OBSERVAÇÕES

### **Sobre Goalposts:**
Os valores de TMR e PMA estão definidos no arquivo `10_Desenho_IGRO.md`. Para RP, %RI e NR, verificar:
- Nota Técnica interna da CGE
- Documento de Benchmarking (`09_Benchmarking_KRIs_Ouvidorias_Estaduais.md`)
- Validação do GT de Riscos

### **Sobre Sensibilidade:**
O Handbook OCDE/JRC recomenda explicitamente análise de sensibilidade. Sem ela, o índice não passa em validação metodológica rigorosa.

### **Sobre Figuras:**
Todas as figuras devem ser **editáveis** em formato SVG ou source file (Figma, Draw.io) para que revisores possam sugerir ajustes.

### **Sobre Referências:**
Após preencher Andrade (2026) e Santos et al. (2019), revalidar todas as citações internas para garantir coerência (nomes, anos, páginas).

---

## 📞 Contatos e Responsabilidades

| Item | Responsável | Prazo estimado |
|---|---|---|
| Goalposts RP, %RI, NR | GT Riscos / Proprietário IGRO | Imediato |
| Base KRIs normalizados | Analista de dados / Proprietário | 3-5 dias |
| Dados Andrade (2026), Santos et al. (2019) | Pesquisador / Responsável | 1 semana |
| Sensibilidade (3 testes) | Analista / Data scientist | 1-2 semanas |
| Figuras 1–6 e Gráficos 1–3 | Designer / Analista BI | 2-3 semanas |

---

**Última atualização:** 2026-05-28  
**Versão:** 1.0  
**Status:** Compilação em progresso

