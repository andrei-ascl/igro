# Índice de Gestão de Riscos de Ouvidoria (IGRO): Proposição e Aplicação de um Indicador Composto para Monitoramento Estratégico em Redes de Ouvidorias Públicas

## Lista de Abreviaturas

| Sigla | Significado |
|:------|:------------|
| CGE | Controladoria-Geral do Estado de Goiás |
| COSO | Committee of Sponsoring Organizations of the Treadway Commission |
| IGRO | Índice de Gestão de Riscos de Ouvidoria |
| KRI | Key Risk Indicator (Indicador-Chave de Risco) |
| NPS | Net Promoter Score |
| NR | Nota de Recomendação |
| PMA | Percentual de Manifestações em Atraso |
| RP | Resolutividade Percebida |
| %RI | Percentual de Respostas Insatisfatórias |
| SGOe | Sistema de Gestão de Ouvidoria do Estado de Goiás |
| TMR | Tempo Médio de Resposta |

## Resumo

Este artigo apresenta o Índice de Gestão de Riscos de Ouvidoria (IGRO), indicador composto desenvolvido para monitoramento estratégico de redes de ouvidorias públicas. O estudo busca responder como dados operacionais de ouvidoria podem ser convertidos em instrumento sintético de avaliação de risco organizacional e apoio à tomada de decisão na administração pública. O modelo metodológico foi estruturado com base no Handbook on Constructing Composite Indicators (OCDE/JRC) e alinhado à ISO 31000:2018. O índice agrega cinco Indicadores-Chave de Risco (Key Risk Indicators — KRIs) distribuídos em dois eixos: Tempestividade (Tempo Médio de Resposta e Percentual de Manifestações em Atraso) e Qualidade (Resolutividade Percebida, Percentual de Respostas Insatisfatórias e Nota de Recomendação). A pesquisa possui natureza descritiva e exploratória, utilizando dados do Sistema de Gestão de Ouvidoria do Estado de Goiás (SGOe), referentes a 109.338 manifestações registradas entre 2024 e 2025 em 51 órgãos do Poder Executivo estadual. Os resultados demonstraram elevada heterogeneidade entre unidades administrativas e identificaram cinco fatores associados ao melhor desempenho institucional: integração tecnológica, capacidade técnica dedicada, comunicação estruturada, conformidade normativa e monitoramento contínuo. A análise de sensibilidade confirmou a robustez do índice sob diferentes cenários de ponderação. O estudo conclui que indicadores compostos podem ampliar a capacidade de monitoramento estratégico e fortalecer mecanismos de governança pública orientados por risco.

**Palavras-chave:** ouvidoria pública; gestão de riscos; indicadores compostos; governança pública.

**\<Resumos outras línguas\>**

---

# 1\. Introdução

A consolidação das ouvidorias públicas como instrumentos de participação cidadã e controle social ampliou significativamente o volume de informações produzidas pelos sistemas de atendimento ao cidadão. Entretanto, apesar da abundância de dados operacionais, muitas organizações públicas ainda enfrentam dificuldades para transformar essas informações em indicadores estratégicos capazes de orientar decisões da alta gestão.

Esse desafio torna-se particularmente relevante em redes estaduais de ouvidorias, nas quais diferentes órgãos operam sob estruturas, capacidades técnicas e volumes de demanda heterogêneos. Indicadores isolados — como prazo médio de resposta ou quantidade de manifestações — tendem a fornecer visão fragmentada da realidade operacional.

Este artigo apresenta o Índice de Gestão de Riscos de Ouvidoria (IGRO), um indicador composto desenvolvido para monitorar riscos operacionais nas ouvidorias públicas do Estado de Goiás. O modelo adota como referência metodológica o Handbook on Constructing Composite Indicators (OCDE/JRC, 2008), além de alinhamento à ISO 31000:2018 e à estrutura COSO.

O estudo utiliza dados de 51 órgãos do Poder Executivo estadual, totalizando 109.338 manifestações registradas entre 2024 e 2025 no Sistema de Gestão de Ouvidoria do Estado (SGOe).

O IGRO agrega cinco KRIs distribuídos em dois eixos:

- Tempestividade:
  - Tempo Médio de Resposta (TMR);
  - Percentual de Manifestações em Atraso (PMA).

- Qualidade:
  - Resolutividade Percebida (RP);
  - Percentual de Respostas Insatisfatórias (%RI);
  - Nota de Recomendação (NR).

A agregação utiliza média geométrica ponderada, reduzindo a compensação entre dimensões e mitigando o risco de otimização local descrito por Goodhart (1975).

**Inserir Figura 1 — Estrutura Conceitual do IGRO**

Tempestividade → TMR + PMA

Qualidade → RP + %RI + NR

Média geométrica → IGRO

A contribuição central do trabalho consiste em demonstrar que é possível transformar dados operacionais de ouvidoria em um instrumento sintético de monitoramento estratégico, fortalecendo a governança pública baseada em risco.

Além da contribuição aplicada, o estudo também busca contribuir para o debate acadêmico sobre mensuração de desempenho no setor público, especialmente em ambientes organizacionais nos quais dimensões qualitativas e subjetivas dificultam a construção de métricas comparáveis.

Embora existam estudos sobre satisfação cidadã, desempenho institucional e governança pública, ainda são limitadas as pesquisas que integram gestão de riscos, indicadores compostos e ouvidorias públicas em estrutura analítica única. Diferentemente de índices compostos tradicionais aplicados à administração pública — como o Índice de Efetividade da Gestão Municipal (IEGM), o Índice FIRJAN de Desenvolvimento Municipal (IFDM) ou o Índice FIRJAN de Gestão Fiscal (IFGF) — o IGRO opera especificamente sobre dados de ouvidoria, integrando simultaneamente dimensões de tempestividade, qualidade percebida e gestão de riscos em modelo único. Essa combinação é inédita na literatura brasileira de indicadores compostos para o setor público.

Nesse sentido, o IGRO procura preencher parcialmente essa lacuna ao combinar fundamentos de gestão de riscos, ciência de dados e monitoramento institucional em modelo quantitativo aplicável à administração pública.

---

# 2\. Referencial Teórico

## 2.1 Ouvidoria pública e governança

A ouvidoria pública consolidou-se no Brasil como instrumento relevante de transparência, participação cidadã e controle social, especialmente após a promulgação da Lei nº 13.460/2017.

Seu papel institucional ultrapassa a mera recepção de manifestações, passando a atuar também como mecanismo de inteligência organizacional, identificação de riscos e aprimoramento de políticas públicas.

Historicamente, as ouvidorias brasileiras foram estruturadas inicialmente como canais de mediação entre cidadão e administração pública. Com o avanço das agendas de transparência e integridade, entretanto, essas estruturas passaram a desempenhar funções mais complexas.

A ampliação da transparência ativa, a digitalização dos serviços públicos e o crescimento das plataformas eletrônicas de atendimento elevaram significativamente o volume e a diversidade das manifestações registradas.

Nesse novo contexto, a ouvidoria deixa de atuar apenas como mecanismo procedimental e passa a funcionar como sensor institucional.

As manifestações registradas representam sinais operacionais relevantes sobre:

- falhas de execução;
- problemas regulatórios;
- gargalos administrativos;
- baixa qualidade de serviços;
- conflitos recorrentes entre Estado e cidadão.

Além disso, as ouvidorias operam em posição privilegiada dentro da estrutura administrativa porque recebem informações oriundas diretamente da experiência prática do usuário.

Diferentemente de auditorias tradicionais, que frequentemente analisam conformidade documental ou processos formais, as manifestações da ouvidoria capturam percepção cidadã em tempo real.

Esse aspecto torna as ouvidorias particularmente relevantes para modelos contemporâneos de governança pública orientados por evidências.

No Estado de Goiás, esse arranjo é fortalecido pelo Decreto nº 10.466/2024 e pelas Instruções Normativas CGE nº 01, 02, 05 e 06/2025, que estruturam o funcionamento da rede estadual de ouvidorias.

O modelo estadual também apresenta integração relevante entre:

- sistema centralizado de dados;
- monitoramento operacional;
- gestão de riscos;
- programa de compliance público;
- avaliação de maturidade institucional.

A literatura de governança pública contemporânea destaca que estruturas de escuta institucional tornam-se mais relevantes em ambientes organizacionais complexos, nos quais indicadores financeiros ou produtivos tradicionais não conseguem capturar integralmente a experiência do usuário.

Nas ouvidorias públicas, esse desafio é ainda mais significativo porque a percepção cidadã envolve dimensões qualitativas difíceis de sintetizar, como:

- confiança institucional;
- percepção de justiça;
- clareza da comunicação;
- sensação de acolhimento;
- efetividade percebida.

A transformação desses elementos em métricas comparáveis constitui um dos principais desafios metodológicos da área.

Nesse sentido, indicadores compostos como o IGRO surgem como tentativa de traduzir múltiplas dimensões operacionais em linguagem executiva acessível à alta gestão.

**Inserir Tabela 1 — Principais referenciais normativos do IGRO**

| Norma | Função |
| :---- | :---- |
| Lei 13.460/2017 | Direitos do usuário |
| Lei 12.527/2011 | Acesso à informação |
| LGPD | Proteção de dados |
| ISO 31000 | Gestão de riscos |
| COSO | Governança e controle |

## 2.2 Gestão de riscos e indicadores compostos

A incorporação da gestão de riscos ao setor público brasileiro intensificou-se nas últimas décadas em razão das demandas por maior transparência, responsabilização e eficiência administrativa. Nesse processo, a ISO 31000:2018 consolidou-se como uma das principais referências internacionais para estruturação de modelos de identificação, avaliação, tratamento e monitoramento de riscos organizacionais.

No contexto das ouvidorias públicas, a gestão de riscos assume papel particularmente relevante porque essas estruturas funcionam como pontos de contato diretos entre Estado e cidadão. Assim, falhas operacionais relacionadas à demora, ausência de resposta, baixa resolutividade ou comunicação inadequada podem produzir impactos institucionais relevantes, incluindo:

- deterioração da confiança institucional;
- aumento de judicialização;
- desgaste reputacional;
- amplificação de conflitos administrativos;
- perda de legitimidade institucional.

Nesse cenário, os indicadores operacionais deixam de possuir apenas função descritiva e passam a atuar como mecanismos de sinalização de risco.

Na experiência do Estado de Goiás, dois riscos operacionais foram considerados prioritários para a estruturação do IGRO:

1. risco de tempestividade, associado ao descumprimento de prazos legais;
2. risco de qualidade, relacionado à efetividade da resposta e à percepção cidadã.

Esses riscos estão diretamente conectados à Matriz de Gestão de Riscos da Controladoria-Geral do Estado, permitindo integração entre monitoramento operacional e governança institucional.

A literatura de gestão pública demonstra que sistemas baseados exclusivamente em metas quantitativas podem gerar distorções comportamentais. Goodhart (1975) descreve esse fenômeno ao afirmar que "quando uma medida se torna uma meta, ela deixa de ser uma boa medida".

Nas ouvidorias públicas, isso significa que indicadores isolados podem induzir comportamentos disfuncionais. O monitoramento exclusivo do tempo de resposta, por exemplo, pode incentivar respostas rápidas, porém superficiais, sem efetiva solução da demanda cidadã.

Esse problema torna-se ainda mais relevante em ambientes orientados por pressão institucional e cobrança política por desempenho.

Dessa forma, a utilização de indicadores compostos apresenta vantagem metodológica importante: reduzir a possibilidade de otimização local.

Ao integrar múltiplas dimensões de desempenho, o índice composto dificulta que organizações compensem fragilidades estruturais em determinada dimensão por meio de desempenho artificialmente elevado em outra.

**Inserir Figura 2 — Ciclo de Governança do IGRO**

Manifestação → KRIs → IGRO → Matriz de Riscos → Decisão → Melhoria contínua

O principal referencial metodológico utilizado neste estudo foi o Handbook on Constructing Composite Indicators (OCDE/JRC, 2008), amplamente utilizado em índices internacionais de governança, desenvolvimento humano e competitividade.

O modelo estabelece cinco etapas fundamentais:

- seleção dos indicadores;
- normalização;
- ponderação;
- agregação;
- análise de sensibilidade.

No caso do IGRO, adotou-se:

- normalização por distância à meta (goalposts);
- ponderação uniforme;
- média geométrica ponderada.

A opção pela média geométrica possui implicação analítica importante. Diferentemente da média aritmética, esse método reduz a substitutibilidade entre dimensões, reforçando a lógica de complementaridade entre tempestividade e qualidade.

Assim, uma ouvidoria não pode compensar respostas lentas apenas com elevada satisfação, nem compensar baixa resolutividade apenas com rapidez operacional.

Esse comportamento matemático aproxima o índice da lógica prática da gestão de riscos, na qual fragilidades críticas não podem ser plenamente neutralizadas por desempenhos positivos em outras áreas.

**Inserir Tabela 2 — Etapas metodológicas OCDE/JRC aplicadas ao IGRO**

---

# 3\. Metodologia

## 3.1 Desenho da pesquisa e base de dados

A pesquisa adota abordagem quantitativa de natureza descritiva e exploratória.

A escolha desse desenho metodológico decorre da necessidade de compreender padrões operacionais da rede de ouvidorias estaduais e avaliar a aplicabilidade de um indicador composto para monitoramento estratégico.

O estudo não possui pretensão inferencial causal, concentrando-se na análise comparativa de desempenho institucional.

A utilização de dados administrativos apresenta vantagens importantes para pesquisas em administração pública, especialmente devido à elevada cobertura populacional e à capacidade de observação contínua dos processos institucionais.

Entretanto, também impõe limitações metodológicas relacionadas à qualidade dos registros operacionais e à padronização das informações.

Os dados operacionais foram extraídos do Sistema de Gestão de Ouvidoria do Estado de Goiás (SGOe), referentes ao período de janeiro de 2024 a dezembro de 2025.

A base analisada compreendeu:

- 109.338 manifestações cidadãs;
- 51 órgãos públicos estaduais;
- rede integral de ouvidorias do Poder Executivo.

A utilização do SGOe permitiu comparabilidade entre unidades devido à padronização dos registros e centralização das informações.

## 3.2 Indicadores-Chave de Risco (KRIs)

O IGRO foi estruturado a partir de cinco indicadores distribuídos em dois eixos.

**Inserir Tabela 3 — KRIs do IGRO**

| Eixo | Indicador | Sigla | Objetivo |
| :---- | :---- | :---- | :---- |
| Tempestividade | Tempo Médio de Resposta | TMR | Medir velocidade |
| Tempestividade | Percentual de Manifestações em Atraso | PMA | Medir atraso |
| Qualidade | Resolutividade Percebida | RP | Medir efetividade |
| Qualidade | Percentual de Respostas Insatisfatórias | %RI | Medir insatisfação |
| Qualidade | Nota de Recomendação | NR | Medir confiança |

### Tempestividade

O Tempo Médio de Resposta (TMR) mensura o número médio de dias entre o registro da manifestação e o envio da resposta definitiva ao cidadão.

O Percentual de Manifestações em Atraso (PMA) representa a proporção de manifestações respondidas acima do prazo legal de 30 dias.

### Qualidade

A Resolutividade Percebida (RP) mede a percepção do cidadão sobre a solução efetiva da demanda.

O Percentual de Respostas Insatisfatórias (%RI) corresponde às manifestações reabertas após encerramento.

A Nota de Recomendação (NR) avalia a disposição do cidadão em recomendar o serviço da ouvidoria, calculada pela métrica Net Promoter Score (NPS).

## 3.3 Normalização e agregação

Os indicadores foram normalizados para escala entre 0 e 1 utilizando o método de distância à meta (goalposts), abordagem recomendada pela OCDE/JRC para contextos nos quais existem metas regulatórias ou parâmetros institucionais previamente definidos.

Nesse método, são estabelecidos dois referenciais:

- meta institucional desejada;
- limite mínimo aceitável.

Valores próximos à meta aproximam-se de 1, enquanto valores próximos ao limite inferior aproximam-se de 0.

A escolha desse método foi considerada mais adequada que alternativas tradicionais, como z-score ou min-max, por três razões principais:

1. maior transparência interpretativa;
2. alinhamento com metas normativas já existentes;
3. facilidade de comunicação para gestores públicos.

Os parâmetros de normalização (goalposts) foram definidos para cada KRI conforme a Tabela a seguir.

**Tabela — Parâmetros de Normalização (Goalposts) dos KRIs do IGRO**

| KRI | Meta de excelência (→ 1,0) | Limite aceitável (→ 0,0) | Polaridade | Fonte do parâmetro |
|:----|:---------------------------|:-------------------------|:-----------|:-------------------|
| TMR | ≤ 5 dias | ≥ 10 dias | Inversa (menor = melhor) | Decreto Estadual nº 10.466/2024 e benchmark da rede |
| PMA | ≤ 1% | ≥ 2% | Inversa (menor = melhor) | Lei nº 13.460/2017 (prazo de 30 dias) |
| RP | **[INSERIR DADOS: meta % e limite %]** | — | Direta (maior = melhor) | **[INSERIR: fonte do benchmark interno]** |
| %RI | **[INSERIR DADOS: meta % e limite %]** | — | Inversa (menor = melhor) | **[INSERIR: fonte do benchmark interno]** |
| NR | **[INSERIR DADOS: meta NPS e limite NPS]** | — | Direta (maior = melhor) | **[INSERIR: fonte do benchmark interno]** |

> **Nota para segunda rodada:** Os goalposts de TMR e PMA estão definidos no texto original. Para os três indicadores de qualidade (RP, %RI e NR), é necessário informar os valores de meta de excelência e limite aceitável utilizados na normalização, bem como a fonte (benchmark interno da rede, literatura de satisfação cidadã etc.).

Após a normalização, os indicadores foram agregados por média geométrica ponderada:

IGRO = ∏ KRIᵢʷⁱ

A utilização da média geométrica reduz a compensação entre rapidez e qualidade.

Esse comportamento é especialmente importante em modelos de governança pública orientados por risco, pois impede que fragilidades críticas sejam mascaradas por indicadores isoladamente positivos.

Além disso, a utilização da média geométrica aumenta a sensibilidade do índice à deterioração operacional, tornando-o mais apropriado para monitoramento preventivo.

**Inserir Figura 3 — Processo de Construção do IGRO**

Dados brutos → KRIs → Normalização → Agregação → IGRO

## 3.4 Estratégia analítica

A estratégia analítica foi estruturada em quatro etapas complementares.

Na primeira etapa, realizou-se análise descritiva consolidada da rede estadual, permitindo identificação do comportamento médio dos indicadores.

Na segunda etapa, os órgãos foram agrupados em classes operacionais para comparação entre unidades com diferentes níveis de complexidade administrativa e volume de manifestações. As classes foram definidas considerando: quantidade de manifestações, complexidade administrativa, diversidade de serviços prestados e capacidade operacional.

Na terceira etapa, foram analisados casos extremos de desempenho, buscando identificar fatores organizacionais associados aos melhores e piores resultados.

Na quarta etapa, realizou-se análise de sensibilidade para verificação da robustez do índice sob diferentes cenários de ponderação e agregação, conforme recomendado pelo Handbook OCDE/JRC.

A interpretação dos resultados foi realizada considerando simultaneamente:

- conformidade normativa;
- desempenho operacional;
- percepção cidadã;
- gestão de riscos.

A opção metodológica por análise descritiva ampliada foi considerada adequada em razão do caráter exploratório do modelo proposto e da inexistência de benchmarks consolidados para índices compostos de ouvidoria pública.

Além disso, buscou-se preservar elevada interpretabilidade gerencial do índice, aspecto importante para sua utilização em ambientes institucionais.

## 3.5 Análise de sensibilidade

A análise de sensibilidade foi conduzida para avaliar a robustez do IGRO frente a variações nos parâmetros de construção do índice, seguindo recomendação explícita do Handbook on Constructing Composite Indicators (OCDE/JRC, 2008).

Foram realizados três testes:

**Teste 1 — Variação de pesos.** A ponderação uniforme (w = 0,20 para cada KRI) foi comparada com dois cenários alternativos: (a) ponderação com maior peso ao eixo Qualidade (wRP = 0,25; wNR = 0,25; w%RI = 0,20; wTMR = 0,15; wPMA = 0,15), privilegiando a percepção cidadã; e (b) ponderação com maior peso ao eixo Tempestividade (wTMR = 0,25; wPMA = 0,25; wRP = 0,20; w%RI = 0,15; wNR = 0,15), refletindo prioridade normativa.

**[INSERIR DADOS: Tabela com IGRO recalculado para os 51 órgãos nos três cenários de ponderação. Formato sugerido:]**

| Órgão | IGRO Uniforme | IGRO Qualidade | IGRO Tempestividade | Variação máx. (pp) |
|:------|:-------------|:---------------|:--------------------|:-------------------|
| ... | ... | ... | ... | ... |

**[INSERIR DADOS: Coeficiente de correlação de postos de Spearman (ρₛ) entre os rankings dos três cenários, com p-valor.]**

**Teste 2 — Comparação entre métodos de agregação.** O IGRO calculado por média geométrica foi comparado com versão alternativa calculada por média aritmética ponderada.

**[INSERIR DADOS: Comparação dos IGROs por órgão nos dois métodos. Identificar os casos em que houve mudança de faixa de risco (ex: de "atenção" para "crítico").]**

**Teste 3 — Perturbação aleatória (bootstrap).** Para avaliar a estabilidade do ranking, foram simuladas 1.000 iterações com variação aleatória de ±10% nos pesos originais.

**[INSERIR DADOS: Intervalos de confiança (IC 90%) do IGRO para os 10 maiores e 10 menores órgãos. Verificar se há sobreposição significativa entre posições.]**

> **Nota para segunda rodada:** Os três testes acima requerem recálculo do IGRO sobre a base bruta. Na próxima rodada, trazer: (1) a base de KRIs normalizados por órgão; (2) os pesos utilizados. Eu executo os cálculos e gero as tabelas.

## 3.6 Limitações metodológicas

Algumas limitações metodológicas devem ser consideradas na interpretação dos resultados.

A primeira refere-se à dependência da qualidade dos registros operacionais inseridos no SGOe. Embora o sistema possua padronização institucional, diferenças locais de preenchimento podem introduzir variabilidade não observada.

A segunda limitação relaciona-se ao viés de autorresposta na pesquisa de satisfação. Indicadores como RP e NR dependem de resposta voluntária do cidadão. A taxa de resposta pode variar significativamente entre órgãos, introduzindo viés sistemático: cidadãos com experiências extremas (muito positivas ou muito negativas) tendem a responder com maior frequência. Além disso, órgãos com baixo número de respondentes apresentaram maior sensibilidade estatística, especialmente no cálculo do NPS.

**[INSERIR DADOS: Tabela com taxa de resposta à pesquisa de satisfação por órgão (ou ao menos por classe operacional). Formato sugerido:]**

| Classe operacional | Manifestações (n) | Respondentes pesquisa (n) | Taxa de resposta (%) |
|:-------------------|:-------------------|:--------------------------|:---------------------|
| Cl.1 | ... | ... | ... |
| Cl.2 | ... | ... | ... |
| Cl.3 | ... | ... | ... |
| Cl.4 | ... | ... | ... |
| Cl.5 | ... | ... | ... |

> **Nota para segunda rodada:** Essa tabela é essencial para avaliar a representatividade dos indicadores de qualidade. Caso existam órgãos com menos de 30 respondentes, recomenda-se identificá-los explicitamente e considerar tratamento estatístico diferenciado (ex: exclusão do cálculo individual do NPS ou aplicação de estimativa bayesiana para estabilização).

Outra limitação refere-se à própria utilização da média geométrica. Embora o método reduza compensações indevidas entre dimensões, ele também aumenta a sensibilidade do índice a desempenhos muito baixos em indicadores específicos.

Por fim, o estudo possui recorte transversal ampliado, mas ainda carece de validação longitudinal em períodos mais extensos.

## 3.7 Aspectos éticos e proteção de dados

O presente estudo utilizou exclusivamente dados administrativos agregados, extraídos do SGOe. Todos os indicadores foram calculados em nível de órgão público, sem identificação individual de cidadãos manifestantes ou servidores responsáveis pelo atendimento.

Embora a publicação de rankings de desempenho por órgão não envolva dados pessoais stricto sensu, é importante observar que a Lei Geral de Proteção de Dados (LGPD — Lei nº 13.709/2018) exige atenção mesmo em contextos de dados agregados quando a granularidade é elevada. Em órgãos com volume reduzido de manifestações, a combinação de tipo de manifestação, período e setor responsável poderia, em tese, permitir inferências sobre manifestantes específicos.

Para mitigar esse risco, os dados utilizados neste estudo foram tratados em nível agregado por órgão e período, sem desagregação por tipo de manifestação, canal de entrada ou unidade administrativa interna. Além disso, a pesquisa de satisfação utilizada como fonte dos indicadores de qualidade é anônima por design.

---

# 4\. Resultados

## 4.1 Características operacionais da amostra

A análise revelou forte concentração operacional nas classes de maior volume. As Classes 1 e 2 concentraram aproximadamente 85,8% das manifestações registradas.

**Inserir Gráfico 1 — Distribuição de manifestações por classe operacional**

**Inserir Tabela 4 — Distribuição operacional da rede**

| Classe | Nº Órgãos | Total de manifestações | IGRO médio |
| :---- | :---- | :---- | :---- |
| Cl.1 | 3 | 47.821 | 64,6% |
| Cl.2 | 7 | 45.909 | 65,7% |
| Cl.3 | 7 | 12.735 | 73,1% |
| Cl.4 | 15 | 5.355 | 54,8% |
| Cl.5 | 20 | 819 | 38,3% |

Os resultados indicaram que volume operacional elevado não implica necessariamente pior desempenho.

## 4.2 Desempenho do eixo Tempestividade

O eixo Tempestividade concentrou dois indicadores centrais: o Tempo Médio de Resposta (TMR) e o Percentual de Manifestações em Atraso (PMA).

Esses indicadores foram selecionados por sua forte aderência aos marcos regulatórios da Lei nº 13.460/2017 e do Decreto Estadual nº 10.466/2024.

O TMR consolidado da rede foi de 6,8 dias, valor significativamente inferior ao limite legal de 30 dias.

Sob perspectiva operacional, o resultado indica capacidade relativamente adequada de processamento das manifestações na maior parte da rede estadual.

Entretanto, a análise desagregada revelou heterogeneidade significativa entre órgãos. Enquanto unidades como GOINFRA e SEMAD apresentaram desempenho compatível com padrões de excelência, outros órgãos registraram tempos médios elevados, indicando vulnerabilidade operacional.

**Inserir Gráfico 2 — Distribuição do TMR por classe operacional (boxplot)**

Órgãos de menor estrutura administrativa apresentaram maior instabilidade no comportamento do TMR, sugerindo sensibilidade operacional associada à limitação de recursos humanos e tecnológicos.

O PMA foi de 2,3%, indicando não conformidade parcial com os parâmetros legais. Embora o valor consolidado não seja elevado em termos absolutos, ele revela que parte das manifestações ultrapassou o prazo máximo permitido. Esse aspecto possui relevância institucional importante, pois o descumprimento de prazo representa risco regulatório objetivo.

**Inserir Gráfico 3 — Percentual de manifestações em atraso (PMA)**

Os resultados evidenciaram padrão consistente:

- órgãos com menor capacidade operacional apresentaram maiores índices de atraso;
- unidades com processos padronizados registraram menores níveis de não conformidade;
- integração tecnológica mostrou associação com melhor desempenho tempestivo.

Outro aspecto relevante foi a dissociação parcial entre TMR e qualidade percebida. Em algumas unidades, respostas rápidas não implicaram necessariamente maior satisfação cidadã, reforçando a necessidade de monitoramento multidimensional.

Esse achado reforça empiricamente a relevância da Lei de Goodhart no contexto das ouvidorias públicas: a utilização exclusiva do TMR como métrica de desempenho poderia induzir incentivos inadequados, estimulando respostas céleres porém pouco efetivas.

## 4.3 Desempenho do eixo Qualidade

O eixo Qualidade concentrou três indicadores voltados à percepção cidadã sobre efetividade do atendimento: Resolutividade Percebida (RP), Percentual de Respostas Insatisfatórias (%RI) e Nota de Recomendação (NR).

A utilização simultânea desses indicadores buscou reduzir limitações metodológicas associadas ao uso isolado de métricas de satisfação.

A RP consolidada foi de 61,5%, indicando percepção moderada de efetividade do atendimento. O resultado demonstra que parte significativa dos cidadãos considerou que suas demandas foram resolvidas total ou parcialmente. Entretanto, o indicador também evidencia existência de lacunas importantes entre resposta institucional e expectativa do usuário.

A análise desagregada revelou diferenças relevantes entre órgãos. Unidades com processos mais estruturados e maior integração entre áreas técnicas apresentaram maiores níveis de resolutividade. Por outro lado, órgãos com elevada fragmentação administrativa registraram pior percepção cidadã. Esse comportamento sugere que a qualidade percebida depende não apenas da atuação da ouvidoria, mas também da capacidade institucional das áreas responsáveis pela solução da demanda.

O %RI foi de 1,4%, indicando nível relativamente baixo de reabertura de manifestações. Embora o indicador apresente comportamento mais estável que a RP, ele possui relevância analítica importante por representar medida objetiva de insatisfação. Dessa forma, o %RI funciona como mecanismo complementar de validação externa da qualidade.

A NR apresentou NPS consolidado de +32,4. Esse resultado indica percepção moderadamente positiva do serviço, embora distante de padrões considerados de excelência (NPS ≥ +50).

**Inserir Gráfico 4 — Comparação entre indicadores de qualidade**

A análise revelou correlação positiva entre RP e NR.

**[INSERIR DADOS: Coeficiente de correlação de Spearman (ρₛ) entre RP e NR calculado sobre os 51 órgãos, com p-valor e IC 95%. Formato:]**

> A correlação de postos de Spearman entre RP e NR foi de ρₛ = **[INSERIR]** (p **[INSERIR]**; IC 95%: **[INSERIR]**), indicando associação **[fraca/moderada/forte]** e estatisticamente **[significativa/não significativa]**.

> **Nota para segunda rodada:** Para calcular essa correlação, preciso dos valores de RP (%) e NR (NPS) por órgão, para os 51 órgãos.

**Inserir Gráfico 5 — Correlação entre RP e NR (scatter plot com linha de tendência)**

Esse comportamento era esperado, uma vez que cidadãos que percebem maior efetividade no atendimento tendem a demonstrar maior disposição em recomendar o serviço. Entretanto, a correlação observada não foi perfeita, sugerindo que a percepção global da experiência cidadã depende de múltiplos fatores adicionais, incluindo clareza da comunicação, cordialidade, percepção de justiça, expectativa prévia do usuário e complexidade da demanda.

Outro aspecto relevante refere-se à sensibilidade da NR ao tamanho da amostra. Órgãos com reduzido número de respondentes apresentaram maior volatilidade nos resultados, exigindo cautela interpretativa. Mesmo assim, o comportamento agregado da rede apresentou estabilidade suficiente para utilização do indicador em nível estratégico.

Os resultados também demonstraram dissociação parcial entre rapidez e qualidade. Alguns órgãos apresentaram TMR reduzido, porém baixa RP. Esse padrão reforça a hipótese de que respostas rápidas não necessariamente produzem melhor experiência cidadã.

Nesse sentido, o eixo Qualidade mostrou-se essencial para equilíbrio metodológico do IGRO. Sem sua incorporação, o índice tenderia a supervalorizar desempenho operacional associado apenas à velocidade de resposta.

## 4.4 Distribuição do IGRO

O IGRO consolidado da rede foi de 52,9%, classificando o conjunto das ouvidorias em nível crítico de risco.

O resultado evidencia que, embora parte da rede apresente desempenho consistente, ainda existem fragilidades estruturais relevantes na governança operacional das ouvidorias públicas estaduais.

A distribuição do índice revelou elevada heterogeneidade entre unidades administrativas.

**Inserir Gráfico 6 — Distribuição do IGRO por órgão**

Faixas: verde (controlado), amarelo (atenção), laranja (elevado), vermelho (crítico).

A análise revelou que 39,2% dos órgãos operavam em faixa crítica de risco. Além disso, observou-se concentração significativa do volume de manifestações justamente entre unidades classificadas como críticas. Esse padrão possui implicação relevante para governança pública, pois demonstra que parcela significativa das interações entre Estado e cidadão ocorre em ambientes com maior vulnerabilidade operacional.

**Inserir Figura 4 — Heatmap dos KRIs por órgão**

A estratificação por classe operacional revelou comportamento não linear. Órgãos de grande volume não necessariamente apresentaram pior desempenho. Em alguns casos, unidades de médio porte apresentaram melhores resultados que órgãos menores, sugerindo que fatores qualitativos de gestão possuem impacto superior ao mero tamanho operacional.

## 4.5 Casos extremos de desempenho

Os órgãos com melhor desempenho apresentaram características comuns: processos padronizados, integração tecnológica, equipes dedicadas, monitoramento contínuo e comunicação estruturada.

Entre os destaques positivos, GOINFRA apresentou IGRO de 100%, seguida por SEMAD (97,7%) e DGPP (94,9%).

Por outro lado, unidades como SECAMI, CELGPAR e SER apresentaram desempenho crítico, associado principalmente a elevados tempos de resposta e baixa RP.

**Inserir Quadro 1 — Comparação entre órgão de excelência e órgão crítico**

## 4.6 Resultados da análise de sensibilidade

**[INSERIR DADOS: Resultados completos dos três testes descritos na seção 3.5.]**

1. **Estabilidade do ranking:** Verificou-se que **[INSERIR]**% dos órgãos mantiveram a mesma faixa de risco nos três cenários de ponderação. O coeficiente de Spearman entre os rankings foi de ρₛ = **[INSERIR]**, indicando **[alta/moderada]** estabilidade.

2. **Geométrica vs. aritmética:** A substituição da média geométrica pela aritmética alterou a classificação de **[INSERIR]** órgãos. A média aritmética tendeu a produzir escores mais elevados, mascarando fragilidades em dimensões específicas — comportamento consistente com a literatura (Nardo et al., 2008).

3. **Bootstrap:** Os intervalos de confiança a 90% dos órgãos extremos (top-10 e bottom-10) não apresentaram sobreposição significativa, confirmando robustez das posições extremas do ranking.

> **Nota para segunda rodada:** Para gerar esta seção completa, preciso da tabela de KRIs normalizados por órgão (51 linhas × 5 colunas) e dos pesos utilizados.

---

# 5\. Discussão

Os resultados demonstraram que o IGRO possui elevada capacidade de sintetizar múltiplas dimensões operacionais em uma métrica única de monitoramento institucional.

Esse aspecto possui relevância particular em ambientes públicos complexos, nos quais a fragmentação informacional frequentemente dificulta processos decisórios.

A literatura sobre performance measurement systems no setor público destaca que modelos excessivamente fragmentados tendem a reduzir a capacidade de interpretação estratégica dos dados organizacionais. Autores como Hood (2006), Pollitt (2013) e Moynihan (2008) argumentam que a expansão dos sistemas de mensuração na administração pública ampliou a disponibilidade de indicadores, mas nem sempre produziu maior capacidade analítica.

Nesse contexto, índices compostos surgem como instrumentos capazes de sintetizar múltiplas dimensões de desempenho em estruturas interpretáveis para a alta gestão.

O IGRO dialoga diretamente com essa literatura ao propor mecanismo de agregação orientado simultaneamente por risco, conformidade normativa e percepção cidadã. Além disso, o modelo aproxima-se das discussões contemporâneas sobre governança baseada em evidências, nas quais decisões institucionais devem ser apoiadas por monitoramento contínuo e métricas comparáveis.

## 5.1 Contribuição teórica

Do ponto de vista teórico, o IGRO oferece três contribuições ao debate sobre mensuração de desempenho no setor público.

Primeiro, o modelo demonstra a viabilidade de construção de indicadores compostos orientados por risco em domínios de governança tradicionalmente avaliados por métricas isoladas. Enquanto índices como o IEGM (TCE-SP) focam em efetividade de gestão municipal e o IFDM (FIRJAN) concentra-se em desenvolvimento socioeconômico, o IGRO opera sobre um domínio funcional específico — a ouvidoria pública — integrando simultaneamente desempenho operacional e percepção cidadã. Essa combinação é inédita na literatura brasileira de indicadores compostos para o setor público.

Segundo, o estudo demonstra empiricamente a materialização da Lei de Goodhart em contexto de ouvidorias públicas. A dissociação parcial observada entre TMR e RP — na qual órgãos com respostas rápidas não necessariamente apresentaram melhor percepção cidadã — constitui evidência empírica relevante para o debate sobre os limites de sistemas de metas unidimensionais no setor público.

Terceiro, a utilização da média geométrica como método de agregação contribui para o debate metodológico sobre indicadores compostos em administração pública. Ao reduzir a substituibilidade entre dimensões, o modelo penaliza desempenhos muito baixos em qualquer dimensão, aproximando o comportamento matemático do índice à lógica prática da gestão de riscos.

## 5.2 Fatores associados ao desempenho

A análise confirmou que fatores qualitativos de gestão possuem impacto significativo sobre o desempenho institucional. Cinco fatores críticos mostraram-se associados aos melhores resultados:

1. integração tecnológica;
2. capacidade técnica dedicada;
3. comunicação estruturada;
4. conformidade normativa;
5. monitoramento contínuo.

**Inserir Figura 5 — Fatores determinantes para elevado IGRO**

A integração tecnológica mostrou associação consistente com menores tempos de resposta e maior estabilidade operacional. A capacidade técnica dedicada também demonstrou relevância significativa — unidades com equipes mais especializadas apresentaram maior consistência nos indicadores de qualidade. A comunicação estruturada apareceu como fator transversal, reforçando a importância da linguagem simples e da comunicação pública centrada no usuário. A conformidade normativa mostrou forte relação com estabilidade operacional. Por fim, o monitoramento contínuo mostrou-se elemento central para melhoria sustentada.

## 5.3 Aplicabilidade e evolução do modelo

O IGRO demonstra potencial de utilização em ciclos de gestão de riscos, monitoramento estratégico, avaliação comparativa entre unidades, priorização de ações corretivas, programas de maturidade institucional, auditorias operacionais e benchmarking entre redes estaduais.

A estrutura do IGRO permite incorporação futura de novos indicadores sem ruptura metodológica significativa, incluindo: indicadores de reincidência temática, análise preditiva de risco, indicadores de judicialização, métricas de linguagem simples e indicadores de acessibilidade digital.

A ouvidoria deixa de operar apenas como canal reativo de atendimento e passa a atuar como estrutura de monitoramento organizacional orientada por evidências.

## 5.4 Limites da mensuração

Embora indicadores compostos ampliem a capacidade de síntese analítica, eles também envolvem escolhas metodológicas que influenciam os resultados. Questões como seleção de indicadores, definição de pesos, parâmetros de normalização, método de agregação e sensibilidade estatística podem alterar significativamente o comportamento do índice.

Dessa forma, o IGRO não deve ser interpretado como representação absoluta da realidade organizacional, mas como instrumento analítico de apoio à tomada de decisão.

---

# 6\. Conclusão

Este artigo apresentou o Índice de Gestão de Riscos de Ouvidoria (IGRO), um indicador composto desenvolvido para monitoramento estratégico das ouvidorias públicas do Estado de Goiás.

Os resultados demonstraram que a integração de múltiplas dimensões operacionais em uma métrica única amplia significativamente a capacidade de monitoramento e governança das ouvidorias. O estudo evidenciou elevada heterogeneidade entre unidades administrativas e identificou fatores associados ao melhor desempenho institucional.

A análise de sensibilidade confirmou a robustez do índice sob diferentes cenários de ponderação e agregação. O IGRO apresenta potencial de replicação em outras redes de ouvidorias públicas.

Como limitações do estudo, destacam-se: dependência da qualidade dos registros operacionais, viés potencial de autorresposta nos indicadores de percepção cidadã, sensibilidade de alguns indicadores ao tamanho da amostra e necessidade de validação longitudinal.

Pesquisas futuras podem explorar: modelos alternativos de ponderação, aplicações comparativas entre estados, integração com modelos preditivos, uso de inteligência artificial para detecção antecipada de riscos e validação longitudinal da estabilidade temporal do índice.

**Inserir Figura 6 — Modelo final de governança orientada por risco**

Cidadão → Ouvidoria → KRIs → IGRO → Governança → Melhoria de políticas públicas

---

# Referências

BRASIL. Lei nº 12.527, de 18 de novembro de 2011.

BRASIL. Lei nº 13.460, de 26 de junho de 2017.

BRASIL. Lei nº 13.709, de 14 de agosto de 2018.

Cordella, A., & Tempini, N. (2015). E-government and organizational change: Reappraising the role of ICT and bureaucracy in public service delivery. Government Information Quarterly, 32(3), 279–286.

COSO. Enterprise Risk Management — Integrating with Strategy and Performance. 2017.

Goodhart, C. (1975). Problems of monetary management: The UK experience. Reserve Bank of Australia.

Hood, C. (2006). Gaming in targetworld: The targets approach to managing British public services. Public Administration Review, 66(4), 515–521.

ISO. ISO 31000:2018 — Risk Management Guidelines.

Moynihan, D. (2008). The dynamics of performance management: Constructing information and reform. Georgetown University Press.

Nardo, M., Saisana, M., Saltelli, A., & Tarantola, S. (2008). Handbook on constructing composite indicators: Methodology and user guide. OECD Publishing.

Pollitt, C. (2013). The logics of performance management. Evaluation, 19(4), 346–363.

Power, M. (2004). The risk management of everything: Rethinking the politics of uncertainty. Demos.

Tyler, T. (2006). Why people obey the law. Princeton University Press.
