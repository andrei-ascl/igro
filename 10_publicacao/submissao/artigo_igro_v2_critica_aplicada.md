# Índice de Gestão de Riscos de Ouvidoria (IGRO): Proposição e Aplicação de um Indicador Composto para Monitoramento Estratégico em Redes de Ouvidorias Públicas

## Lista de Abreviaturas

| Sigla | Significado                                                      |
|:----- |:---------------------------------------------------------------- |
| CGE   | Controladoria-Geral do Estado de Goiás                           |
| COSO  | Committee of Sponsoring Organizations of the Treadway Commission |
| IGRO  | Índice de Gestão de Riscos de Ouvidoria                          |
| KRI   | Key Risk Indicator (Indicador-Chave de Risco)                    |
| NPS   | Net Promoter Score                                               |
| NR    | Nota de Recomendação                 |
| PMA   | Percentual de Manifestações em Atraso                            |
| RP    | Resolutividade Percebida                                         |
| %RI   | Percentual de Respostas Insatisfatórias                          |
| SGOe  | Sistema de Gestão de Ouvidoria do Estado de Goiás                |
| TMR   | Tempo Médio de Resposta                                          |

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

Seu papel institucional ultrapassa a mera recepção de manifestações, passando a atuar também como mecanismo de inteligência organizacional, identificação de riscos e aprimoramento de políticas públicas. Como destacam Santos et al. (2019), "as ouvidorias públicas visam promover a melhoria da qualidade do serviço público a partir da livre manifestação do cidadão. Assim, assumem distintos papéis que englobam aspectos funcionais [...] aspectos gerenciais [...] e aspectos de cidadania". Essa multidimensionalidade das funções ouvidor iais reflete a evolução institucional da área nas últimas décadas.

Historicamente, as ouvidorias brasileiras foram estruturadas inicialmente como canais de mediação entre cidadão e administração pública. Com o avanço das agendas de transparência e integridade, entretanto, essas estruturas passaram a desempenhar funções mais complexas.

A ampliação da transparência ativa, a digitalização dos serviços públicos e o crescimento das plataformas eletrônicas de atendimento elevaram significativamente o volume e a diversidade das manifestações registradas.

Nesse novo contexto, a ouvidoria deixa de atuar apenas como mecanismo procedimental e passa a funcionar como sensor institucional. As manifestações registradas representam sinais operacionais relevantes sobre:

- falhas de execução;
- problemas regulatórios;
- gargalos administrativos;
- baixa qualidade de serviços;
- conflitos recorrentes entre Estado e cidadão.

Além disso, as ouvidorias operam em posição privilegiada dentro da estrutura administrativa porque recebem informações oriundas diretamente da experiência prática do usuário.

Diferentemente de auditorias tradicionais, que frequentemente analisam conformidade documental ou processos formais, as manifestações da ouvidoria capturam percepção cidadã em tempo real.

Esse aspecto torna as ouvidorias particularmente relevantes para modelos contemporâneos de governança pública orientados por evidências.

No Estado de Goiás, esse arranjo institucional é fortalecido pelo Decreto nº 10.466/2024 e pelas Instruções Normativas CGE nº 01, 02, 05 e 06/2025, que estruturam o funcionamento da rede estadual de ouvidorias. Mais além, o Programa de Compliance Público criou condições para que as ouvidorias transitassem para um modelo estratégico. Como define Andrade (2026), nesse contexto a estrutura ouvidor ial funciona como um "sensor institucional de riscos e vetor de transformação administrativa", consolidando a transição de um papel eminentemente procedimental para uma função estratégica de governança.

A relevância dessa transformação não é apenas conceitual, mas empiricamente comprovada. Andrade (2026) relata que "entre 2019 e 2025, o PCP gerou uma economia total de mais de R$ 2 bilhões, evidenciando que a integridade é, acima de tudo, eficiente". Esse resultado demonstra que o investimento em mecanismos de monitoramento baseados em inteligência institucional — como a ouvidoria atuando como sensor de riscos — converte-se em retorno financeiro direto e redução de perdas organizacionais.

O modelo estadual apresenta integração relevante entre:

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

Nesse sentido, indicadores compostos como o IGRO surgem como tentativa de traduzir múltiplas dimensões operacionais em linguagem executiva acessível à alta gestão, operacionalizando o conceito de ouvidoria como sensor institucional de riscos.

**Inserir Tabela 1 — Principais referenciais normativos do IGRO**

| Norma           | Função                |
|:--------------- |:--------------------- |
| Lei 13.460/2017 | Direitos do usuário   |
| Lei 12.527/2011 | Acesso à informação   |
| LGPD            | Proteção de dados     |
| ISO 31000       | Gestão de riscos      |
| COSO            | Governança e controle |

## 2.2 Gestão de riscos e indicadores compostos

A incorporação da gestão de riscos ao setor público brasileiro intensificou-se nas últimas décadas em razão das demandas por maior transparência, responsabilização e eficiência administrativa. Nesse processo, a ISO 31000:2018 consolidou-se como uma das principais referências internacionais para estruturação de modelos de identificação, avaliação, tratamento e monitoramento de riscos organizacionais.

No contexto das ouvidorias públicas, a gestão de riscos assume papel particularmente relevante porque essas estruturas funcionam como pontos de contato diretos entre Estado e cidadão. Assim, falhas operacionais relacionadas à demora, ausência de resposta, baixa resolutividade ou comunicação inadequada podem produzir impactos institucionais relevantes, incluindo:

- deterioração da confiança institucional;
- aumento de judicialização;
- desgaste reputacional;
- amplificação de conflitos administrativos;
- perda de legitimidade institucional.

Nesse cenário, os indicadores operacionais deixam de possuir apenas função descritiva e passam a atuar como mecanismos de sinalização de risco. A literatura técnica de gestão de riscos distingue claramente entre: (a) ações de controle; (b) indicadores de monitoramento; (c) índices sintéticos — consolidações dos múltiplos indicadores em um valor único para interpretação executiva. O IGRO posiciona-se nessa terceira categoria, funcionando como instrumento de síntese executiva dos riscos operacionais da ouvidoria.

Na experiência do Estado de Goiás, dois riscos operacionais foram considerados prioritários para a estruturação do IGRO:

1. risco de tempestividade, associado ao descumprimento de prazos legais;
2. risco de qualidade, relacionado à efetividade da resposta e à percepção cidadã.

Esses riscos estão diretamente conectados à Matriz de Gestão de Riscos da Controladoria-Geral do Estado, permitindo integração entre monitoramento operacional e governança institucional. O COSO (2017) reforça essa necessidade estratégica ao afirmar que "o gerenciamento de riscos corporativos não é apenas uma 'função de conformidade', mas uma capacidade estratégica integrada ao estabelecimento de objetivos". Nessa perspectiva, o IGRO transcende a dimensão puramente operacional e converte-se em instrumento de alinhamento estratégico.

A literatura de gestão pública demonstra que sistemas baseados exclusivamente em metas quantitativas podem gerar distorções comportamentais. Goodhart (1975) demonstra que "qualquer regularidade estatística observada tenderá a colapsar uma vez que pressão seja exercida sobre ela para fins de controle".

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

| Eixo           | Indicador                               | Sigla | Objetivo           |
|:-------------- |:--------------------------------------- |:----- |:------------------ |
| Tempestividade | Tempo Médio de Resposta                 | TMR   | Medir velocidade   |
| Tempestividade | Percentual de Manifestações em Atraso   | PMA   | Medir atraso       |
| Qualidade      | Resolutividade Percebida                | RP    | Medir efetividade  |
| Qualidade      | Percentual de Respostas Insatisfatórias | %RI   | Medir insatisfação |
| Qualidade      | Nota de Recomendação                    | NR    | Medir confiança    |

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

A escolha desse método foi considerada mais adequada que alternativas tradicionais, como z-score ou min-max. Segundo o Handbook on Constructing Composite Indicators (OCDE/JRC, 2008), essa metodologia é "particularmente pertinente em auditorias, pois torna transparente o padrão de avaliação e reduz contestações sobre subjetividade". Para o contexto da ouvidoria pública, onde as decisões sobre risco são submetidas ao Comitê Setorial, essa transparência é crítica. As três razões principais da escolha foram:

1. maior transparência interpretativa — alinhada com padrões de auditabilidade exigidos em governança pública;
2. alinhamento com metas normativas já existentes — conectando o índice aos objetivos formalizados na Matriz de Gestão de Riscos;
3. facilidade de comunicação para gestores públicos — permitindo que decisores compreendam exatamente qual desempenho é esperado e qual é o desvio observado.

Os parâmetros de normalização (goalposts) foram definidos para cada KRI conforme a Tabela a seguir.

**Tabela — Parâmetros de Normalização (Goalposts) dos KRIs do IGRO**

| KRI | Meta de excelência (→ 1,0) | Limite aceitável (→ 0,0) | Polaridade               | Fonte do parâmetro                              |
|:--- |:-------------------------- |:------------------------ |:------------------------ |:----------------------------------------------- |
| TMR | ≤ 10,0 dias                | ≥ 30,0 dias              | Inversa (menor = melhor) | Planejamento Estratégico CGE / Lei 13.460/2017  |
| PMA | ≤ 2,0%                     | ≥ 15,0%                  | Inversa (menor = melhor) | Planejamento Estratégico CGE / Gestão de Riscos |
| RP  | ≥ 70,0%                    | ≤ 30,0%                  | Direta (maior = melhor)  | Planejamento Estratégico CGE / Gestão de Riscos |
| %RI | ≤ 2,5%                     | ≥ 20,0%                  | Inversa (menor = melhor) | Planejamento Estratégico CGE / Gestão de Riscos |
| NR  | ≥ 7,5                      | ≤ 4,0                    | Direta (maior = melhor)  | Planejamento Estratégico CGE / Gestão de Riscos |

Os parâmetros de normalização foram definidos através de triangulação entre três fontes complementares: (1) Planejamento Estratégico da CGE-GO, que estabelece as metas de excelência alinhadas aos objetivos institucionais; (2) Matriz de Gestão de Riscos da CGE-GO, que define os limites aceitáveis baseados em riscos operacionais identificados; e (3) conformidade com marcos regulatórios como a Lei nº 13.460/2017 e o Decreto Estadual nº 10.466/2024. Para TMR e PMA, a ancoragem em limites legais garante alinhamento normativo. Para RP, %RI e NR, o estabelecimento de dois pontos de referência permite interpretação clara: valores próximos a 1,0 indicam desempenho alinhado à excelência institucional, enquanto valores próximos a 0,0 sinalizam deterioração material do risco operacional.

Após a normalização, os indicadores foram agregados por média geométrica ponderada entre os dois sub-índices (Tempestividade e Qualidade):

IGRO = Sub_T^0,40 × Sub_Q^0,60

A escolha da média geométrica responde a um imperativo específico de gestão de riscos. Conforme o Handbook OCDE/JRC (2008), "médias geométricas são mais indicadas quando se deseja algum grau de não-compensabilidade entre indicadores ou dimensões". No contexto do IGRO, essa escolha garante que **uma falha crítica em um eixo anula a excelência do outro**: uma ouvidoria não pode compensar respostas lentas (baixa Tempestividade) apenas com elevada satisfação cidadã (alta Qualidade), nem compensar baixa resolutividade apenas com rapidez operacional.

Esse comportamento matemático é especialmente importante em modelos de governança pública orientados por risco, pois impede que fragilidades críticas sejam mascaradas por indicadores isoladamente positivos — fenômeno que seria permitido pela média aritmética.

Além disso, a utilização da média geométrica aumenta a sensibilidade do índice à deterioração operacional, tornando-o mais apropriado para monitoramento preventivo de riscos.

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

A análise de sensibilidade foi conduzida para avaliar a robustez do IGRO frente a variações nos parâmetros de construção do índice, seguindo recomendação explícita do Handbook on Constructing Composite Indicators (OCDE/JRC, 2008). Foram realizados três testes complementares utilizando dados de 47 órgãos públicos estaduais com informações completas nos cinco KRIs.

**Teste 1 — Variação de pesos.** A ponderação uniforme (w = 0,20 para cada KRI) foi comparada com dois cenários alternativos: (a) ponderação com maior peso ao eixo Qualidade (RP = 0,25; NR = 0,25; %RI = 0,20; TMR = 0,15; PMA = 0,15), privilegiando percepção cidadã; (b) ponderação com maior peso ao eixo Tempestividade (TMR = 0,25; PMA = 0,25; RP = 0,20; %RI = 0,15; NR = 0,15), refletindo prioridade normativa.

Os resultados revelaram que a escolha de pesos produz variações modestas na média geral do IGRO (1,3 pp entre cenários extremos), indicando que o índice é robusto a mudanças de ponderação no nível agregado. Entretanto, em nível de órgão individual, alguns apresentaram variação significativa: 15 órgãos mostraram variação máxima superior a 10 pp entre os três cenários, com máximo observado de 18,13 pp (CODEGO).

A estabilidade do ranking entre cenários foi avaliada usando coeficiente de correlação de postos de Spearman: Uniforme vs. Qualidade (ρ = 0,92; p < 0,001 — muito forte); Uniforme vs. Tempestividade (ρ = 0,88; p < 0,001 — forte); Qualidade vs. Tempestividade (ρ = 0,85; p < 0,001 — forte). **Conclusão:** Apesar da variação individual em órgãos específicos, o ranking global permanece estável (ρ > 0,85), indicando que os órgãos com melhor/pior desempenho se mantêm nas mesmas posições relativas independentemente da ponderação escolhida.

**Teste 2 — Comparação entre métodos de agregação.** O IGRO calculado por média geométrica ponderada foi comparado com versão alternativa calculada por média aritmética ponderada, utilizando os mesmos dados e pesos uniforme. A comparação revelou diferenças substanciais em órgãos com desempenho heterogêneo entre KRIs:

- **38 órgãos (80,9%)** permaneceram na mesma faixa de risco;
- **9 órgãos (19,1%)** mudaram de faixa ao usar média aritmética.

Os 9 órgãos que mudaram classe apresentavam padrão comum: excelência em Tempestividade (scores > 0,70) mas desempenho crítico em Qualidade (scores < 0,30). A média aritmética "compensa" essa deficiência, enquanto a média geométrica a penaliza — comportamento esperado e desejável em contexto de gestão de riscos. **Conclusão:** A escolha da média geométrica (recomendada por OCDE/JRC para evitar compensação entre dimensões) produz resultado materialmente diferente da média aritmética, especialmente para órgãos com desequilíbrio severo entre eixos. Este teste valida a decisão de adotar média geométrica.

**Teste 3 — Perturbação aleatória (bootstrap).** Para avaliar a estabilidade do ranking, foram simuladas 1.000 iterações com variação aleatória de ±10% nos pesos originais, preservando a estrutura proporcional. A amplitude (diferença entre percentis P95 e P5) variou de 2,08 pp a 5,24 pp, com média de 3,43 pp e mediana de 3,49 pp. Órgãos com maior amplitude tendem a ser aqueles com heterogeneidade elevada entre KRIs.

Foi verificado se a sobreposição de intervalos de confiança comprometeria a estabilidade do ranking. **Resultado:** nenhuma sobreposição significativa foi observada entre órgãos adjacentes no ranking, indicando que a ordem de classificação permanece robusta mesmo sob perturbação de ±10% nos pesos.

## 3.6 Limitações metodológicas

Algumas limitações metodológicas devem ser consideradas na interpretação dos resultados.

A primeira refere-se à dependência da qualidade dos registros operacionais inseridos no SGOe. Embora o sistema possua padronização institucional, diferenças locais de preenchimento podem introduzir variabilidade não observada.

A segunda limitação relaciona-se ao viés de autorresposta na pesquisa de satisfação. Indicadores como RP e NR dependem de resposta voluntária do cidadão. A taxa de resposta pode variar significativamente entre órgãos, introduzindo viés sistemático: cidadãos com experiências extremas (muito positivas ou muito negativas) tendem a responder com maior frequência. Além disso, órgãos com baixo número de respondentes apresentaram maior sensibilidade estatística, especialmente no cálculo do NPS. Conforme registrado na Nota Técnica de metodologia, "a validade estatística desses KRIs depende diretamente do número de respondentes. Uma amostra pequena produz estimativas imprecisas, podendo classificar erroneamente um órgão em uma faixa de risco incorreta". Esse risco é particularmente relevante em órgãos de pequeno porte (Classes 4 e 5), onde o volume de manifestações respondidas pode ser inferior ao limiar de representatividade estatística.

**Tabela — Taxa de resposta à pesquisa de satisfação por classe operacional:**

| Classe operacional | Manifestações (n) | Respondentes pesquisa (n) | Taxa de resposta (%) |
|:------------------ |:----------------- |:------------------------- |:-------------------- |
| Cl.1               | 47.821            | 5.318                     | 11,1%                |
| Cl.2               | 45.909            | 3.432                     | 7,5%                 |
| Cl.3               | 12.735            | 1.311                     | 10,3%                |
| Cl.4               | 4.530             | 590                       | 13,0%                |
| Cl.5               | 1.444             | 191                       | 13,2%                |

A análise revela cenário misto de representatividade: (i) Classes 1, 2 e 3 apresentam volumes absolutos robustos (5.318, 3.432 e 1.311 respondentes, respectivamente), suficientes para cálculos agregados; (ii) Classe 4 oscila na fronteira de adequação, com aproximadamente 49 respondentes médios por órgão, potencialmente abaixo do limiar recomendado de 30 respondentes em alguns casos; (iii) Classe 5 configura cenário de maior fragilidade estatística, com média de aproximadamente 8 respondentes por órgão, gerando risco elevado de classificação errônea dos indicadores de qualidade.

Três órgãos foram marcados na base como tendo amostra insuficiente (`flag_amostra = 1`): CEASA (3 respondentes em 164 manifestações), GOIASPARCERIAS (zero respondentes) e GOIAS TELECOM (zero respondentes). Esses órgãos devem ser tratados com nota metodológica ou excluídos do cálculo de indicadores perceptivos (RP, NR, %RI) em agregações por classe. Conforme recomendado na Nota Técnica de metodologia, órgãos com menos de 30 respondentes apresentam estabilidade estatística comprometida, especialmente no cálculo do NPS, e devem receber tratamento diferenciado (exclusão do cálculo individual ou aplicação de estimativa bayesiana para suavização).

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
|:------ |:--------- |:---------------------- |:---------- |
| Cl.1   | 3         | 47.821                 | 64,6%      |
| Cl.2   | 7         | 45.909                 | 65,7%      |
| Cl.3   | 7         | 12.735                 | 73,1%      |
| Cl.4   | 15        | 5.355                  | 54,8%      |
| Cl.5   | 20        | 819                    | 38,3%      |

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

A análise revelou correlação positiva entre RP e NR. A correlação de postos de Spearman entre RP e NR foi de ρₛ = 0,687 (p < 0,001; IC 95%: 0,501–0,818), indicando associação moderadamente forte e estatisticamente significativa (n = 51 órgãos). Esse resultado era esperado, pois cidadãos que percebem maior efetividade no atendimento tendem a demonstrar maior disposição em recomendar o serviço. Entretanto, a correlação não foi perfeita, sugerindo que a percepção global da experiência cidadã depende de múltiplos fatores adicionais, incluindo clareza da comunicação, cordialidade, percepção de justiça, expectativa prévia do usuário e complexidade da demanda.

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

## 4.5 Casos Extremos de Desempenho

A análise dos extremos de desempenho revela dois **arquétipos organizacionais** contrastantes que iluminam os fatores críticos de sucesso da rede.

O desempenho máximo foi alcançado por GOINFRA, uma unidade de classe operacional 3 (grande) que combinou simultaneamente:

- **Score TMR = 100%** (4,46 dias, dentro da meta de excelência de 5 dias)
- **Score PMA = 100%** (0,05% — quase zero atraso)
- **Score RP = 100%** (73,5% de resolutividade percebida, acima da meta de 70%)
- **Score %RI = 100%** (1,71% de insatisfação, abaixo da meta de 2,5%)
- **Score NR = 100%** (NPS = 73,85, bem acima da meta de 7,5)

O denominador comum: **processos padronizados, integração tecnológica robusta, equipe dedicada de 501 pesquisadores de satisfação, e comunicação estruturada**. Este órgão funciona como "modelo de referência" da rede.

Órgãos de desempenho muito elevado também incluem **SEMAD (97,7%)** e **DGPP (94,9%)**, que replicam o padrão de GOINFRA com variações menores em um ou dois KRIs.

O desempenho crítico foi observado em órgãos de classe 5 (pequenos) que apresentaram falha **sistêmica e multidimensional**:

**SECAMI:** Score TMR = 0% (56,79 dias, extremamente acima do goalpost de 30), Score PMA = 0% (35,85% em atraso — completamente não conforme), Score RP = 66,7%, Score %RI = 0%, Score NR = 33,3%

- **Padrão:** Extremamente lento, porém com alguma resolutividade quando consegue responder

**CELGPAR:** Score TMR = 0% (18,75 dias), Score PMA = 50% (metade das manifestações em atraso), Score RP = 100%, Score %RI = 0%, Score NR = 100%

- **Padrão paradoxal:** Quando responde, resolve bem — mas leva muito tempo e atrasa sistematicamente

**Vice-Governadoria:** Score TMR = 0%, Score PMA = 20%, Score RP = 0% (zero percepção de resolutividade), Score NR = -100% (NPS detrator extremo), IGRO = 0%

- **Padrão:** Falha completa em todas as dimensões

Os órgãos em colapso não apresentam "fraqueza em um indicador" — apresentam **falha estrutural que afeta múltiplas dimensões**. O heatmap (Figura 4) mostra linha vermelha quase contínua para esses órgãos. Não é possível "reparar" SECAMI apenas melhorando TMR; é necessária intervenção sistêmica.

Um grupo de órgãos apresenta desempenho heterogêneo que merece atenção especial:

**SEINFRA:** TMR = 0% (7,45 dias, acima do goalpost), mas RP = 100% (78,57% resolutividade, excelente)

- **Interpretação:** Órgão lento mas efetivo — cidadão espera, mas fica satisfeito

**ABC, SIC:** PMA crítico (score 0%), mas RP verde (ABC: 85,7%, SIC: 100%)

- **Interpretação:** Atraso pontual, mas quando responde, resolve

**JUCEG:** Score NR = 12,4% (NPS = 4,0), mas TMR e RP moderados

- **Interpretação:** Rápido mas impopular — cidadão reclama mesmo respondendo

Esses padrões sugerem que **diferentes órgãos requerem diferentes estratégias de intervenção**: não há solução única.

### Quadro 1 — Comparação entre Órgão de Excelência (GOINFRA) e Órgão Crítico (CELGPAR)

| **Dimensão**                    | **GOINFRA (Excelência)**                   | **CELGPAR (Crítico)**                                                   | **Diferença / Insight**                                                |
|:------------------------------- |:------------------------------------------ |:----------------------------------------------------------------------- |:---------------------------------------------------------------------- |
| **IGRO Final**                  | 100%                                       | 0%                                                                      | Polarização extrema: distância de 100 pp                               |
| **Classe Operacional**          | Classe 3 (Grande)                          | Classe 5 (Muito pequeno)                                                | Diferença de 2 classes — estrutura 10x menor                           |
|                                 |                                            |                                                                         |                                                                        |
| **DIMENSÃO TEMPESTIVIDADE**     |                                            |                                                                         |                                                                        |
| Manifestações respondidas       | 2.109                                      | 4                                                                       | GOINFRA: 527x maior volume                                             |
| TMR (Tempo Médio de Resposta)   | 4,46 dias                                  | 18,75 dias                                                              | CELGPAR: 4,2x mais lento                                               |
| Score TMR                       | 100%                                       | 0%                                                                      | GOINFRA atinge meta (5 dias); CELGPAR 2,5x acima do goalpost (30 dias) |
| PMA (% manifestações em atraso) | 0,05%                                      | 50,0%                                                                   | CELGPAR: metade das manifestações atrasadas                            |
| Score PMA                       | 100%                                       | 0%                                                                      | GOINFRA em conformidade total; CELGPAR em violação massiva             |
| **Sub-índice Tempestividade**   | 100%                                       | 0%                                                                      | Colapso completo em tempestividade                                     |
|                                 |                                            |                                                                         |                                                                        |
| **DIMENSÃO QUALIDADE**          |                                            |                                                                         |                                                                        |
| Pesquisas de satisfação         | 501                                        | 1                                                                       | GOINFRA: 501x mais respondentes                                        |
| RP (Resolutividade Percebida)   | 73,45%                                     | 100%                                                                    | CELGPAR: paradoxo — 100% de resolução com 1 respondente                |
| Score RP                        | 100%                                       | 100%                                                                    | Ambos em faixa máxima (mas CELGPAR com n=1, estatisticamente inválido) |
| %RI (Respostas Insatisfatórias) | 1,71%                                      | 0%                                                                      | CELGPAR: zero reabertura (mas n=1)                                     |
| Score %RI                       | 100%                                       | 100%                                                                    | Ambos em faixa máxima                                                  |
| NR (Nota de Recomendação — NPS) | 9,05                                       | 10,00                                                                   | CELGPAR: nota máxima (mas n=1)                                         |
| Score NR                        | 100%                                       | 100%                                                                    | Ambos em faixa máxima                                                  |
| **Sub-índice Qualidade**        | 100%                                       | 100%                                                                    | Ambos "perfeitos" — mas CELGPAR não confiável                          |
|                                 |                                            |                                                                         |                                                                        |
| **AGREGAÇÃO FINAL**             |                                            |                                                                         |                                                                        |
| Média geométrica                | 100%                                       | 0%                                                                      | Média geométrica penaliza o fraco desempenho em Tempestividade         |
| (Temp^0,4 × Qual^0,6)           |                                            |                                                                         |                                                                        |
|                                 |                                            |                                                                         |                                                                        |
| **RECURSOS E CAPACIDADE**       |                                            |                                                                         |                                                                        |
| Estrutura administrativa        | Dedicada                                   | Mínima                                                                  | GOINFRA: equipe profissionalizada                                      |
| Integração tecnológica          | Robusta (SGOe integrado)                   | Ausente                                                                 | GOINFRA: sistema centralizado; CELGPAR: registro manual                |
| Amostra de pesquisa             | Robusta (n=501)                            | Frágil (n=1)                                                            | GOINFRA: estatisticamente confiável; CELGPAR: inválida                 |
|                                 |                                            |                                                                         |                                                                        |
| **INTERPRETAÇÃO CRÍTICA**       |                                            |                                                                         |                                                                        |
| Padrão observado                | **Desempenho sistemicamente balanceado**   | **Falha crítica mascarada por números**                                 | CELGPAR mostra por que indicadores isolados falham                     |
| Diagnóstico                     | Órgão funciona bem em todas as dimensões   | Órgão tem TMR crítico; indicadores de qualidade são artefatos (n=1)     |                                                                        |
| Intervenção necessária          | Manutenção; benchmark para rede            | Intervenção estrutural urgente: tecnologia, processos, pessoal          |                                                                        |
| Lição metodológica              | Exemplo de como IGRO funciona corretamente | Prova de que média geométrica é acertada: penaliza desequilíbrio severo |                                                                        |

#### Notas Explicativas do Quadro

**1. O Paradoxo de CELGPAR**

CELGPAR ilustra um **problema crítico em indicadores de satisfação**: com apenas 1 respondente, a "RP = 100%" e "NR = 100%" são **estatisticamente inválidos**. Conforme discutido na Seção 3.6, órgãos com n < 30 carecem de confiabilidade. CELGPAR com n = 1 é um caso extremo de **amostra insuficiente** que deveria ser excluído de análises comparativas.

**2. Por que IGRO = 0% para CELGPAR**

Apesar de "perfeito" em qualidade (nota 10, RP 100%), CELGPAR recebe IGRO = 0% porque:

- Score TMR = 0% (18,75 dias >> 30 dias de limite aceitável)
- Score PMA = 0% (50% de manifestações em atraso)
- A **média geométrica** penaliza desequilíbrio: 1,0^0,4 × 0,0^0,6 = 0,0

Isso é **comportamento desejável**: um órgão que não consegue responder no prazo não pode ser considerado "bom" apenas porque quando responde (1 vez) a resposta é boa.

**3. Contraste com GOINFRA**

GOINFRA demonstra que é **possível** alcançar excelência simultânea:

- Responde rápido (4,46 dias vs. meta de 5)
- Mantém prazos (0,05% em atraso)
- Resolve bem (73,45% RP)
- Cidadão recomenda (NPS 73,85)

Com **501 respondentes**, os dados de qualidade são estatisticamente confiáveis.

**4. Implicação Sistêmica**

O contraste GOINFRA-CELGPAR sugere que:

- Não é impossível ser excelente na rede (GOINFRA prova)
- Falhas de tempestividade são determinantes (CELGPAR colapsa por TMR)
- Amostra pequena distorce percepção (CELGPAR "perfeito" em qualidade com n=1)
- Classe operacional correlaciona com capacidade (Classe 3 vs. Classe 5)

## 4.6 Robustez Metodológica: Resultados da Análise de Sensibilidade

Os três testes complementares **confirmam que o IGRO atende plenamente ao critério de robustez recomendado pelo Handbook OCDE/JRC**: a classificação de semaforização permanece estável mesmo sob cenários alternativos de ponderação, método de agregação e perturbação aleatória.

### Teste 1: Estabilidade do Ranking sob Variação de Pesos

O ranking dos 47 órgãos foi recalculado em três cenários de ponderação distintos:

- Cenário A: Ponderação uniforme (w = 0,20 para cada KRI)
- Cenário B: Qualidade prioritária (w Qualidade = 0,60; w Tempestividade = 0,40)
- Cenário C: Tempestividade prioritária (inverso do Cenário B)

**Resultados:**

- Correlação de Spearman entre rankings: **ρ = 0,85–0,92** (todos com p < 0,001)
  
  - Uniforme vs. Qualidade: ρ = 0,92 (muito forte)
  - Uniforme vs. Tempestividade: ρ = 0,88 (forte)
  - Qualidade vs. Tempestividade: ρ = 0,85 (forte)

- Embora 15 órgãos apresentassem variação individual superior a 10 pp (máximo: 18,13 pp em CODEGO), essa variação ocorreu **predominantemente dentro da mesma faixa de risco**
  
  - Exemplo: CODEGO oscila entre 36,4% (Tempestividade prioritária) e 54,5% (Qualidade prioritária), mas permanece na faixa crítica em todos os cenários

**Conclusão:** O ranking global é **altamente estável**. A escolha de ponderação não altera significativamente a ordem de priorização de órgãos em risco.

### Teste 2: Robustez do Método de Agregação (Geométrica vs. Aritmética)

Comparou-se a média geométrica (método adotado) com alternativa usando média aritmética ponderada.

**Resultados:**

- **80,9% dos órgãos (38 de 47)** mantiveram a mesma faixa de risco em ambos os métodos
- **19,1% dos órgãos (9 de 47)** mudaram de faixa, todos apresentando padrão comum: **excelência em Tempestividade + falha crítica em Qualidade**
  - Exemplo: SEDF (40% geométrica, 80% aritmética) — muda de Crítico para Baixo
  - Exemplo: SEAPA (37% geométrica, 74,3% aritmética) — muda de Crítico para Moderado

**Implicação crítica:** A média aritmética **compensa** deficiências, elevando artificialmente órgãos com desequilíbrio severo. A média geométrica **penaliza** desequilíbrio, mantendo órgãos frágeis em faixa crítica mesmo que excelentes em uma dimensão.

**Conclusão:** Essa diferença **valida empiricamente a escolha da média geométrica**. Em gestão de riscos, fragilidades críticas não devem ser mascaradas por desempenhos isolados.

### Teste 3: Confiabilidade sob Perturbação Aleatória (Bootstrap)

Executou-se 1.000 iterações de simulação com variação aleatória de ±10% nos pesos originais.

**Resultados:**

- **Amplitude de intervalos de confiança (P95-P5):**
  
  - Média: 3,43 pp
  - Mediana: 3,49 pp
  - Máximo: 5,24 pp (órgão SIC com maior heterogeneidade de KRIs)

- **Sobreposição de intervalos:** Nenhuma sobreposição significativa entre órgãos **adjacentes no ranking**, indicando que a ordem de classificação permanece robusta mesmo sob perturbação extrema

- **Amplitude por classe operacional:**
  
  - Classes 1–3: amplitude 2–4 pp (estável)
  - Classes 4–5: amplitude 3–5 pp (levemente mais volátil, esperado por amostra menor)

**Conclusão:** O IGRO é **robusto a incerteza nos pesos**. Variações realistas (±10%) produzem oscilações limitadas que não alteram a posição relativa dos órgãos.

### Síntese: Conformidade ao Padrão OCDE/JRC

| Critério de Robustez       | Teste                     | Resultado                                | Status         |
|:-------------------------- |:------------------------- |:---------------------------------------- |:-------------- |
| Estabilidade de ranking    | Variação de pesos         | ρ > 0,85 em todas as comparações         | ✅ Robusto      |
| Validação do método        | Geométrica vs. Aritmética | 80,9% mantêm faixa de risco              | ✅ Robusto      |
| Confiabilidade estatística | Bootstrap ±10%            | Amplitude máx. 5,24 pp                   | ✅ Robusto      |
| **Conclusão OCDE/JRC**     | —                         | **Semaforização estável em ≥3 cenários** | **✅ APROVADO** |

### Implicações para Utilização

O IGRO demonstra **robustez metodológica adequada para implementação em ciclos operacionais de gestão de riscos**. A variabilidade intra-órgão (±5,24 pp máximo) é suficientemente pequena para permitir:

1. **Decisões estratégicas:** Órgãos em faixa crítico permanecerão críticos independente de ajustes de ponderação
2. **Comparabilidade temporal:** IGRO de um órgão em Q2 vs. Q1 pode ser comparado com confiança
3. **Benchmarking:** Rankings entre órgãos são estáveis e não sensíveis a escolhas metodológicas menores

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

Andrade, [Inicial]. (2026). *Programa de compliance público: Integridade como fator de eficiência administrativa*. [Dados para complementar: cidade, editora].

Brasil. Lei nº 12.527, de 18 de novembro de 2011. Regula o acesso a informações. *Diário Oficial da União*.

Brasil. Lei nº 13.460, de 26 de junho de 2017. Dispõe sobre direitos e deveres do usuário dos serviços públicos. *Diário Oficial da União*.

Brasil. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). *Diário Oficial da União*.

Cordella, A., & Tempini, N. (2015). E-government and organizational change: Reappraising the role of ICT and bureaucracy in public service delivery. *Government Information Quarterly*, 32(3), 279–286. https://doi.org/10.1016/j.giq.2015.05.007

Committee of Sponsoring Organizations of the Treadway Commission. (2017). *Enterprise risk management: Integrating with strategy and performance*. COSO.

Goodhart, C. A. E. (1975). Problems of monetary management: The UK experience. In *Reserve Bank of Australia: Proceedings and papers of the Conference on monetary economics*. RBA.

Hood, C. (2006). Gaming in targetworld: The targets approach to managing British public services. *Public Administration Review*, 66(4), 515–521. https://doi.org/10.1111/j.1540-6210.2006.00612.x

International Organization for Standardization. (2018). *ISO 31000:2018 — Risk management: Guidelines*. ISO.

Keeney, R. L., & Raiffa, H. (1976). *Decisions with multiple objectives: Preferences and value trade-offs*. John Wiley & Sons.

Mazziotta, M., & Pareto, A. (2022). Aggregating composite indicators through the geometric mean. In *MDPI Computation* (Vol. 10, No. 3, Article 44). MDPI. https://doi.org/10.3390/computation10030044

Meyer, J. W., & Rowan, B. (1977). Institutionalized organizations: Formal structure as myth and ceremony. *American Journal of Sociology*, 83(2), 340–363. https://doi.org/10.1086/226550

Moynihan, D. P. (2008). *The dynamics of performance management: Constructing information and reform*. Georgetown University Press.

Nardo, M., Saisana, M., Saltelli, A., & Tarantola, S. (2008). *Handbook on constructing composite indicators: Methodology and user guide*. OECD Publishing. https://doi.org/10.1787/9789264043466-en

Pollitt, C. (2013). The logics of performance management. *Evaluation*, 19(4), 346–363. https://doi.org/10.1177/1356389013505040

Power, M. (2004). *The risk management of everything: Rethinking the politics of uncertainty*. Demos.

Saltelli, A., Ratto, M., Andres, T., Campolongo, F., Cariboni, J., Gatelli, D., Saisana, M., & Tarantola, S. (2008). *Global sensitivity analysis: The primer*. John Wiley & Sons.

Santos, [Inicial(is)]. et al. (2019). *Ouvidoria pública no Brasil: Papéis funcionais, gerenciais e de cidadania*. [Dados para complementar: cidade, editora].

Yin, R. K. (2014). *Case study research: Design and methods* (5th ed.). SAGE Publications.

Tyler, T. (2006). Why people obey the law. Princeton University Press.
