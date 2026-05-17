# Kit de Comandos MCP para Power BI — Rebel Analytics

Este documento consolida um conjunto abrangente de comandos otimizados para uso com o Model Context Protocol (MCP) no Power BI. Developed by Rebel Analytics, o kit foi desenvolvido para projetos de análise de dados em ouvidorias públicas, com foco em governança semântica, performance DAX e usabilidade. Os comandos seguem o padrão de nomenclatura da metodologia de desenvolvimento orientada por dados, incorporando boas práticas de modelagem e as convenções visuais da identidade Rebel Analytics — minimalista, futurista e orientada ao dato.

---

## 1. Introdução e Contexto de Uso

O Model Context Protocol (MCP) representa uma evolução significativa na forma como interagimos com modelos de dados no Power BI. Em vez de executar múltiplas operações manualmente através da interface gráfica, é possível enviar prompts estruturados que o MCP processa de forma automática, retornando análises, sugestões e até mesmo código DAX otimizado. Este kit foi projetado especificamente para projetos de ouvidorias públicas, onde a governança de dados, a privacidade das informações e a clareza analítica são fundamentais.

O contexto do projeto — focado em Ciência de Dados na Gestão de Ouvidorias — exige que cada comando considere não apenas a técnica, mas também a aplicabilidade no setor público brasileiro. Isso significa incluir考虑了feriados nacionais, semesters fiscais, e a lógica de prazos legais que regem o atendimento das manifestações. Além disso, o alinhamento com a identidade visual Rebel Analytics garante que os dashboards resultantes sejam não apenas funcionais, mas também esteticamente consistentes com a proposta de minimalismo e futurismo que caracteriza a marca.

O kit está organizado em três blocos principais: comandos fundamentais (bloco 1), que cobrem as operações essenciais de análise e organização; comandos avançados (bloco 2), que abordam performance, escalabilidade e governança; e um prompt consolidado (bloco 3), que permite executar toda a revisão em uma única operação. A ordem recomendada de execução também é apresentada, otimizando o fluxo de trabalho e evitando retrabalhos.

---

## 2. Bloco 1: Comandos Fundamentais

### 2.1. Análise do Dashboard e Proposta de Novas Medidas

O primeiro comando fundamental foca na compreensão profunda do objetivo do dashboard e na avaliação crítica das medidas DAX existentes. Em projetos de ouvidorias, o dashboard tipicamente visa apresentar indicadores como resolutividade, satisfação do cidadão, volume de manifestações por tipo, tempo médio de resposta e percentual de manifestações dentro do prazo legal. Compreender esses objetivos é o ponto de partida para qualquer otimização.

O comando proposto solicita que o MCP analise a consistência lógica das medidas existentes, verificando se os contextos de filtro estão corretamente configurados e se não há redundâncias que comprometam a performance. Além disso, o comando pede a identificação de possíveis erros de cálculo — um aspecto crítico em indicadores governamentais, onde erros podem levar a decisões de política pública baseadas em dados incorretos.

A proposta de novas medidas inclui indicadores de tendência, que mostram a direção do comportamento dos dados ao longo do tempo; variação percentual, que quantifica mudanças entre períodos; comparativos temporais como Year-over-Year (YoY) e Month-over-MoM; indicadores de eficiência, que relacionam resultados com recursos utilizados; e indicadores de qualidade, que medem a percepção do cidadão e a conformidade com padrões de atendimento. Para cada nova medida proposta, o comando exige uma explicação clara do objetivo e da polaridade — ou seja, se o indicador é melhor quando maior ou quando menor.

**Comando MCP:**

```text
Analise o objetivo principal do dashboard, considerando o contexto da Ouvidoria e os indicadores já existentes, como resolutividade, satisfação, insatisfatórias, volume de manifestações e prazo de resposta.

Avalie todas as medidas DAX atuais e verifique:
- consistência lógica
- coerência com as regras de negócio
- possíveis redundâncias
- possíveis erros de contexto de filtro
- oportunidades de simplificação e melhoria de performance

Proponha novas medidas que agreguem valor analítico, incluindo:
- tendência
- comparação com período anterior
- variação percentual
- comparativos YoY e MoM
- indicadores de eficiência
- indicadores de qualidade

Explique o objetivo de cada nova medida sugerida e informe quando a polaridade for:
- quanto maior, melhor
- quanto menor, melhor
```

### 2.2. Organização e Governança das Medidas DAX

A organização das medidas em pastas de exibição (Display Folders) é uma prática essencial para a manutenção a longo prazo de modelos semânticos complexos. Em ambientes corporativos, onde múltiplos analistas podem trabalhar simultaneamente no mesmo modelo, uma estrutura clara de pastas reduz significativamente o tempo necessário para localizar e modificar medidas específicas. Além disso, a governança de nomenclatura garante que todos os desenvolvedores utilizem o mesmo padrão, evitando ambiguidades e facilitando a documentação.

O comando proposto organiza as medidas em pastas temáticas que refletem a lógica de negócio da ouvidoria. A pasta `indicadores_gerais` contém medidas agregadas de alto nível, como totais e contagens. A pasta `volume_manifestacoes` concentra indicadores relacionados à quantidade de manifestações recebidas, separadas por tipo, status ou origem. A pasta `satisfacao` abriga todas as medidas relacionadas à pesquisa de satisfação, incluindo notas médias, percentuais de recomendação e índices de satisfação. A pasta `insatisfatorias` é dedicada aos indicadores de manifestações classificadas como insatisfatórias, um dos principais KPIs de qualidade do serviço público. As pastas `prazo_tempo_resposta` e `resolutividade` organizam os indicadores de eficiência operacional. A pasta `comparativos_temporais` guarda medidas de comparação entre períodos, enquanto `tendencia` concentra indicadores de análise de série temporal. Por fim, a pasta `apoio` contém medidas auxiliares utilizadas como intermediárias em cálculos mais complexos.

O comando também padroniza a nomenclatura das medidas em `snake_case`, um padrão amplamente utilizado em desenvolvimento de software que melhora a legibilidade e facilita a busca. Quando forem identificadas medidas com nomes ambíguos, excessivamente técnicos ou inconsistentes, o comando sugere renomeações apropriadas.

**Comando MCP:**

```text
Organize todas as medidas DAX do modelo, incluindo as já existentes, em pastas de exibição (Display Folders) com lógica analítica consistente.

Crie ou ajuste agrupamentos como:
- indicadores_gerais
- volume_manifestacoes
- satisfacao
- insatisfatorias
- prazo_tempo_resposta
- resolutividade
- comparativos_temporais
- tendencia
- apoio

Padronize a nomenclatura das medidas em snake_case.

Sugira renomeações quando houver:
- nomes ambíguos
- nomes excessivamente técnicos
- inconsistência de padrão
- duplicidade de propósito

Ao final, apresente a estrutura final de pastas e a lista das medidas organizadas em cada grupo.
```

### 2.3. Evolução da Tabela Calendário

A tabela calendário é o alicerce de qualquer análise temporal em modelos de dados. Uma tabela calendário bem estruturada permite segmentações sofisticadas, comparações entre períodos e análises de sazonalidade que seriam impossíveis com uma simples lista de datas. No contexto de ouvidorias públicas, a tabela calendário assume importância adicional por causa dos prazos legais de resposta — o artigo 16 da Lei nº 13.460/2017 estabelece o prazo de 30 dias para resposta, prorrogável por mais 30 mediante justificativa.

O comando proposto inicia com a análise do estado atual da tabela calendário, verificando quais colunas já existem e quais precisam ser adicionadas. As colunas temporais básicas incluem o ano, o semestre, o trimestre, o número e o nome do mês (completo e abreviado), o código `ano_mes` para ordenação correta, o número da semana do ano, o dia do mês, o número e nome do dia da semana, e indicadores booleanos para fim de semana e dia útil.

As colunas de feriado representam um diferencial importante para análises governamentais. O comando solicita a criação de uma coluna que identifique o nome do feriado nacional brasileiro (como Natal, Ano Novo, Carnaval, Páscoa, Tiradentes, Dia do Trabalho, Independência, Nossa Senhora Aparecida, Finados e Proclamação da República) e uma coluna booleana que sinalize simplesmente se o dia é feriado. Essa informação é crucial para calcular corretamente o tempo útil de resposta, excluindo dias não úteis do prazo legal.

A coluna de estação do ano (verão, outono, inverno, primavera) permite análises de sazonalidade que podem revelar padrões interessantes no volume de manifestações. Por exemplo, algumas ouvidorias registram picos de reclamações relacionadas a serviços de utility em determinadas épocas do ano, e essa informação pode ser valiosa para planejamento de capacidade.

O comando também sugere colunas adicionais úteis para análises de ouvidoria, como `inicio_do_mes` e `fim_do_mes` para cálculos de indicadores mensais, `inicio_do_trimestre` e `fim_do_trimestre` para análises trimestrais, `ano_trimestre` como chave de concatenação, `competencia_texto` para exibição amigável em relatórios, e `competencia_ordenacao` para garantir ordenação correta em visões tabulares.

**Comando MCP:**

```text
Analise o estado atual da tabela calendário e proponha uma versão mais robusta para análise temporal.

Inclua as seguintes colunas:
- data
- ano
- semestre
- trimestre
- mes_numero
- mes_nome
- mes_abreviado
- ano_mes
- ano_mes_ordenacao
- semana_ano
- dia
- dia_semana_numero
- dia_semana_nome
- fim_de_semana
- dia_util

Adicione também:
- coluna de feriado_nacional_brasil com o nome do feriado
- coluna eh_feriado
- coluna estacao_ano

Sugira outras colunas úteis para análise de dados de ouvidoria, como:
- inicio_do_mes
- fim_do_mes
- inicio_do_trimestre
- fim_do_trimestre
- ano_trimestre
- competencia_texto
- competencia_ordenacao

Explique a utilidade analítica de cada coluna nova.
```

### 2.4. Dicionário de Dados do Modelo

O dicionário de dados é um documento fundamental para a governança do modelo semântico. Ele serve como fonte de verdade para todos os objetos do modelo, permitindo que analistas, desenvolvedores e usuários finais compreendam o significado de cada tabela e coluna sem necessidade de consultar o código ou o autor original. Em ambientes onde múltiplas pessoas trabalham no mesmo modelo, o dicionário de dados reduz significativamente a curva de aprendizado para novos membros da equipe e evita mal-entendidos sobre o significado dos dados.

O comando proposto solicita que o MCP liste todas as tabelas do modelo e classifique cada uma como fato, dimensão, calendário ou tabela de apoio. As tabelas fato contêm os eventos ou transações do negócio — no caso de ouvidorias, tipicamente a tabela de manifestações. As tabelas dimensão contêm os atributos descritivos que contextualizam os dados das fatos — como dimensão de tempo, dimensão de tipo de manifestação, dimensão de órgão responsável, etc. A tabela calendário, como discutido anteriormente, é uma dimensão temporal específica. Tabelas de apoio são auxiliares, frequentemente utilizadas para mapeamentos ou conversões.

Para cada coluna, o comando solicita a descrição do conteúdo, o tipo de dado esperado (texto, número inteiro, número decimal, data, booleano, etc.), e a classificação como chave (primary key ou foreign key), atributo (informação descritiva), data (campo de data) ou métrica base (valor numérico que será utilizado em cálculos). A classificação correta é essencial para que o Power BI apply as agregações apropriadas e para que os usuários compreendam como utilizar cada campo em seus relatórios.

**Comando MCP:**

```text
Liste todas as tabelas do modelo e suas respectivas colunas.

Para cada tabela:
- informe o nome
- classifique como fato, dimensão, apoio ou calendário
- descreva o objetivo da tabela no modelo

Para cada coluna:
- informe o nome
- descreva o que representa
- indique o tipo de dado esperado
- destaque se é chave, atributo, data ou métrica base

Organize a saída em formato tabular, com linguagem clara e orientada ao negócio.
```

### 2.5. Documentação no Modelo Semântico

A documentação diretamente no modelo semântico do Power BI — através do campo Description — é uma das práticas mais valiosas para a governança de dados. Diferentemente de documentos externos que podem se desatualizar, as descrições inseridas no modelo acompanham o arquivo .pbix e estão sempre disponíveis para qualquer usuário que explore o modelo através do Power BI Service ou Power BI Desktop.

O comando proposto solicita que o MCP adicione descrições para todas as tabelas, colunas e principais medidas do modelo. As descrições devem ser claras e objetivas, padronizadas em estilo e linguagem, e orientadas ao negócio — ou seja, focadas no significado dos dados para o usuário final, não em detalhes técnicos de implementação. Por exemplo, em vez de descrever uma coluna como "número inteiro que armazena a contagem", a descrição deveria ser "quantidade total de manifestações recebidas no período".

A padronização do estilo textual é importante para manter a consistência ao longo de todo o modelo. Recomenda-se utilizar o mesmo tempo verbal (geralmente presente do indicativo), o mesmo nível de detalhamento e a mesma estrutura de frase em todas as descrições. Isso facilita a leitura e cria uma experiência consistente para o usuário.

**Comando MCP:**

```text
Adicione descrições no modelo semântico do Power BI para:
- todas as tabelas
- todas as colunas
- principais medidas

As descrições devem ser:
- claras
- objetivas
- padronizadas
- orientadas ao negócio
- úteis para usuários finais e analistas

Mantenha o mesmo estilo textual em todo o modelo.
```

---

## 3. Bloco 2: Comandos Avançados

### 3.1. Revisão Técnica e Otimização DAX

A otimização de medidas DAX é um tópico avançado que pode gerar ganhos significativos de performance, especialmente em modelos com grandes volumes de dados. O comando de revisão técnica solicita que o MCP analise todas as medidas existentes e aplique boas práticas de modelagem, identificando oportunidades de melhoria que não comprometam a regra de negócio.

O uso adequado de variáveis (VAR) é um dos primeiros aspectos avaliados. Variáveis permitem que expressões complexas sejam divididas em partes menores e reutilizadas, reduzindo a redundância de código e melhorando a legibilidade. Além disso, o uso de variáveis pode melhorar a performance ao calcular expressões intermediárias uma única vez em vez de múltiplas vezes.

A remoção de FILTER desnecessário é outro ponto crucial. Em muitos casos, medidas DAX são escritas com filtros que abrangem a tabela inteira quando um filtro mais direcionado seria suficiente. Por exemplo, um FILTER que remove valores em branco de toda a tabela pode frequentemente ser substituído por uma função CALCULATE com a tabela já filtrada, ou por uma expressão mais simples usando ISBLANK ou NOT.

O comando também verifica o tratamento de divisões por zero — um erro comum que pode quebrar relatórios inteiros. Boas práticas incluem o uso de DIVIDE (que aceita um resultado alternativo) ou expressões condicionais que verificam o denominador antes de realizar a divisão. A consistência de contexto de filtro é verificada para garantir que as medidas respondam corretamente aos filtros aplicados nos visuais.

**Comando MCP:**

```text
Revise todas as medidas DAX existentes e aplique boas práticas de modelagem e performance.

Verifique:
- uso adequado de VAR
- remoção de FILTER desnecessário em tabelas inteiras
- melhoria de legibilidade
- simplificação de lógica
- tratamento de divisões por zero
- consistência de contexto de filtro

Sugira versões otimizadas das medidas, preservando a regra de negócio.
```

### 3.2. KPIs Estratégicos para Ouvidoria

Este comando solicita a criação de um conjunto padronizado de KPIs estratégicos para dashboards de ouvidoria. Cada KPI deve incluir a fórmula DAX sugerida, uma interpretação gerencial que explique como o indicador deve ser lido, e a polaridade correta que defina se o indicador é melhor quando maior ou quando menor.

Os KPIs sugeridos cobrem as principais dimensões de desempenho de uma ouvidoria. O `total_manifestacoes` representa o volume total de manifestações recebidas no período. O `manifestacoes_finalizadas` conta apenas as manifestações que já receberam resposta. O `tempo_medio_resposta` calcula a média de dias entre o recebimento e a resposta final. Os indicadores `percentual_no_prazo` e `percentual_fora_prazo` mostram a conformidade com os prazos legais.

O `indice_resolutividade` mede o percentual de manifestações que foram resolvidas na primeira resposta, um indicador importante de eficiência. O `indice_insatisfacao` calcula o percentual de manifestações classificadas como insatisfatórias pelo cidadão. A `nota_media_satisfacao` apresenta a média das notas da pesquisa de satisfação. O `percentual_recomendacao` mostra o índice de pessoas que recomendariam o serviço.

Os indicadores de tendência incluem `crescimento_volume` (variação percentual do volume em relação ao período anterior) e `variacao_tempo_resposta` (variação do tempo médio de resposta). Cada KPI deve ser apresentado com sua fórmula DAX completa e uma explicação detalhada de cada componente.

**Comando MCP:**

```text
Crie um conjunto de KPIs estratégicos para o dashboard da Ouvidoria, com fórmula DAX, interpretação e polaridade.

Inclua, quando fizer sentido:
- total_manifestacoes
- manifestacoes_finalizadas
- tempo_medio_resposta
- percentual_no_prazo
- percentual_fora_prazo
- indice_resolutividade
- indice_insatisfacao
- nota_media_satisfacao
- percentual_recomendacao
- crescimento_volume
- variacao_tempo_resposta

Para cada KPI, informe:
- objetivo do indicador
- fórmula sugerida
- interpretação gerencial
- polaridade correta
```

### 3.3. Padronização Visual dos Indicadores

A padronização visual é essencial para criar dashboards intuitivos e de fácil interpretação. Este comando solicita a criação de medidas auxiliares que padronizem a exibição de ícones e cores para indicação de status, considerando que cada indicador pode ter polaridade diferente — alguns são melhores quando maiores (como resolutividade), outros são melhores quando menores (como tempo médio de resposta).

As medidas auxiliares sugeridas incluem `icone_status`, que retorna um ícone específico com base na avaliação do indicador (seta para cima, seta para baixo, sinal de igual); `cor_status`, que retorna uma cor específica (verde para melhoria, vermelho para piora, amarelo para estabilidade); `texto_variacao`, que apresenta a variação percentual em formato textual com sinal; e `classificacao_desempenho`, que atribui uma categoria geral (excelente, bom, regular, crítico) com base em thresholds pré-definidos.

A implementação dessas medidas requer a criação de variáveis que comparem o valor atual com um valor de referência (período anterior, meta, ou média histórica) e retornem o resultado apropriado. O comando também deve considerar a polaridade de cada indicador para que a lógica de melhoria/piora seja aplicada corretamente.

**Comando MCP:**

```text
Crie medidas auxiliares para exibição visual dos KPIs com semântica consistente de melhoria e piora.

Padronize ícones e status para:
- melhoria
- piora
- estabilidade

Considere que a polaridade depende do indicador.
Exemplo:
- prazo médio: menor é melhor
- resolutividade: maior é melhor

Sugira medidas para:
- icone_status
- cor_status
- texto_variacao
- classificacao_desempenho
```

### 3.4. Revisão do Modelo de Dados

A aderência ao modelo estrela (star schema) é uma das práticas mais importantes para garantir performance e manutenibilidade em modelos tabulares. Este comando solicita uma análise crítica da estrutura do modelo, verificando se ele segue os princípios do modelo estrela ou se apresenta problemas que possam comprometer a performance ou a clareza analítica.

O modelo estrela caracteriza-se por uma tabela fato central cercada por tabelas dimensão que se conectam diretamente a ela, sem tabelas intermediárias. Essa estrutura permite que o motor de análise (VertiPaq no caso do Power BI) realize as agregações de forma eficiente, minimizando o número de joins necessários para responder às consultas.

O comando verifica a existência de relacionamentos desnecessários que podem criar ambiguidades no modelo — por exemplo, quando uma tabela fato está conectada a múltiplas dimensões através de caminhos diferentes, criando o risco de resultados incorretos. Também verifica a presença de dimensões compartilhadas (dimensões utilizadas por múltiplas tabelas fato), que é uma prática recomendada, e a granularidade das tabelas fato, garantindo que cada fato esteja no nível apropriado de detalhe.

**Comando MCP:**

```text
Analise o modelo de dados e avalie:
- aderência ao modelo estrela
- existência de relacionamentos desnecessários
- risco de ambiguidade
- presença de dimensões compartilhadas
- granularidade das tabelas fato

Sugira melhorias estruturais para deixar o modelo mais claro, performático e escalável.
```

### 3.5. Qualidade dos Dados

A qualidade dos dados é um pré-requisito para qualquer análise confiável. Este comando solicita uma avaliação abrangente dos dados no modelo, identificando problemas que possam comprometer a precisão das análises ou causar erros nos relatórios.

Os problemas avaliados incluem valores nulos relevantes — campos que deveriam ter valores preenchidos mas estão em branco, indicando possíveis falhas no processo de captura de dados; inconsistência de tipos — colunas que armazenam diferentes tipos de dados (como texto em colunas numéricas), indicando problemas na extração ou transformação; duplicidades — registros duplicados que podem distorcer contagens e agregações; colunas com baixa utilidade analítica — campos que existem no modelo mas nunca são utilizados nos visuais ou medidas; e atributos com padronização ruim — valores textuais com variações ortográficas ou formatos diferentes que impedem agrupamentos corretos.

Para cada problema identificado, o comando sugere melhorias no tratamento e preparação dos dados, seja através de transformações no Power Query, seja através de correções na fonte de dados.

**Comando MCP:**

```text
Analise o modelo e identifique possíveis problemas de qualidade de dados:
- nulos relevantes
- inconsistência de tipos
- duplicidades
- colunas com baixa utilidade analítica
- atributos com padronização ruim

Sugira melhorias no tratamento e preparação dos dados.
```

### 3.6. Segurança e LGPD

Em projetos de ouvidorias públicas, a segurança e a conformidade com a Lei Geral de Proteção de Dados (LGPD — Lei nº 13.709/2018) são aspectos críticos. Este comando solicita uma análise do modelo para identificar colunas que possam conter dados pessoais ou sensíveis, e propõe estratégias de proteção.

As colunas avaliadas incluem dados pessoais diretos (nome, CPF, e-mail, telefone) e dados pessoais indiretos que possam identificar indiretamente o cidadão. A estratégia de mascaramento sugere como esses dados podem ser apresentados de forma parcialmente oculta em relatórios públicos (como os exigidos pela Lei de Acesso à Informação), preservando a utilidade analítica enquanto protege a privacidade.

O comando também propõe uma estrutura de Row-Level Security (RLS) baseada na dimensão de setor, órgão ou secretaria. Com essa estrutura, cada gestor visualiza apenas as manifestações destinadas à sua área de responsabilidade, garantindo que informações sigilosas não sejam expostas indevidamente. A implementação de RLS é feita através de funções DAX que filtram os dados com base no usuário que está acessando o relatório.

**Comando MCP:**

```text
Analise o modelo e identifique colunas com potencial conteúdo sensível ou pessoal.

Sugira:
- estratégia de mascaramento
- anonimização para relatórios públicos
- separação entre visão gerencial e visão pública

Proponha uma estrutura de RLS com base na dimensão de setor, órgão ou secretaria, permitindo que cada gestor visualize apenas os dados da sua área.
```

### 3.7. Escalabilidade e Arquitetura

À medida que o volume de dados cresce, o modelo semântico precisa estar preparado para lidar com essa escala sem degradação significativa de performance. Este comando avalia o modelo atual e propõe melhorias arquiteturais que garantam escalabilidade.

O incremental refresh é uma técnica que permite processar apenas os dados novos ou alterados desde a última atualização, em vez de reprocessar todo o conjunto de dados. Isso reduz drasticamente o tempo de atualização e permite que o modelo cresça sem se tornar impraticável. O comando avalia se o modelo é candidato ao incremental refresh e quais seriam os critérios de partição.

O particionamento lógico sugere a separação de dados em grupos lógicos (por exemplo, por ano ou por trimestre) que podem ser processados independentemente. Isso não apenas melhora a performance de atualização, mas também permite que usuários acessem apenas as partitions relevantes para suas análises.

A separação entre camadas (raw, treated, curated) é uma prática de arquitetura de dados que facilita a manutenção e a governança. A camada raw contém os dados exatamente como vieram da fonte, sem transformações. A camada treated contém os dados já limpos e transformados, mas ainda próximos do formato original. A camada curated contém os dados prontos para consumo, com as estruturas otimizadas para os relatórios.

**Comando MCP:**

```text
Avalie o modelo atual e proponha melhorias para escalabilidade.

Considere:
- incremental refresh
- particionamento lógico
- separação entre camadas raw, treated e curated
- redução de colunas desnecessárias
- uso adequado de agregações

Explique os ganhos esperados em desempenho, manutenção e governança.
```

---

## 4. Bloco 3: Prompt Único Consolidado

Para situações onde seja necessário executar toda a revisão de uma vez, ou quando o MCP suportar prompts extensos, o comando consolidado abaixo engloba todos os aspectos dos blocos anteriores em uma única solicitação.

Este prompt foi desenhado para fornecer ao MCP uma visão holística do modelo, permitindo que ele realize uma análise integrada e identifique interdependências entre os diferentes aspectos do modelo semântico. A execução completa gera um relatório abrangente que pode servir como base para um plano de ação de melhorias.

**Comando MCP consolidado:**

```text
Analise o arquivo de Power BI atualmente aberto e execute uma revisão completa do modelo semântico, com foco em governança, clareza analítica, performance e usabilidade.

1. Analise o objetivo principal do dashboard considerando o contexto da Ouvidoria.
2. Revise todas as medidas DAX existentes, verificando consistência lógica, redundâncias, erros de contexto e oportunidades de otimização.
3. Proponha novas medidas analíticas relevantes, incluindo tendência, variação percentual, comparativos temporais, eficiência e qualidade.
4. Organize todas as medidas em Display Folders coerentes e padronize seus nomes em snake_case.
5. Analise a tabela calendário atual e proponha uma versão mais completa, incluindo colunas temporais avançadas, feriados nacionais do Brasil, estação do ano e outros atributos úteis.
6. Liste todas as tabelas e colunas do modelo em formato de dicionário de dados, com descrição funcional e classificação de cada objeto.
7. Adicione descrições no modelo semântico para tabelas, colunas e principais medidas, com linguagem clara e orientada ao negócio.
8. Avalie a estrutura do modelo de dados, identificando problemas de modelagem, risco de ambiguidade e oportunidades de melhoria para aderência ao modelo estrela.
9. Identifique possíveis problemas de qualidade de dados.
10. Sugira melhorias de segurança e governança, incluindo RLS e tratamento de colunas sensíveis.
11. Apresente os resultados de forma estruturada, prática e orientada à tomada de decisão.
```

---

## 5. Ordem Recomendada de Execução

A ordem de execução dos comandos influencia diretamente a eficiência do processo de revisão. Executar os comandos na sequência correta evita retrabalhos e garante que cada etapa se beneficie dos resultados das anteriores. A ordem recomendada é:

A primeira etapa deve ser a análise do dashboard, que estabelece o contexto e o objetivo do modelo semântico. Compreender o propósito do dashboard permite avaliar se as medidas existentes estão alinhadas com as necessidades dos usuários e se as novas medidas propostas realmente agregarão valor. Além disso, a análise inicial pode revelar questões que precisam ser consideradas nas etapas seguintes.

A segunda etapa é a revisão e otimização das medidas DAX. Com o contexto estabelecido, é possível avaliar se as medidas existentes estão tecnicamente corretas e otimizadas. Medidas mal otimizadas podem comprometer a performance de todas as etapas subsequentes, por isso é importante identificar e corrigir esses problemas logo no início.

A terceira etapa é a organização em pastas de medidas. Com as medidas já revisadas e otimizadas, é o momento ideal para organizá-las em Display Folders coerentes. Essa organização facilita a localização de medidas durante as etapas seguintes e garante que a estrutura de pastas reflita a versão final do modelo.

A quarta etapa é a evolução da tabela calendário. Uma tabela calendário robusta é fundamental para análises temporais, e suas colunas podem ser utilizadas em filtros e segmentações durante as etapas seguintes. Por isso, é importante que ela esteja completa antes de prosseguir.

A quinta etapa é a criação do dicionário de dados. Com o modelo já praticamente definido, é possível documentar de forma precisa todas as tabelas e colunas, seus tipos e finalidades. O dicionário serve como base para as descrições que serão adicionadas na etapa seguinte.

A sexta etapa é a adição de descrições no modelo semântico. Com o dicionário completo, a adição de descrições torna-se uma tarefa simples de transferência de informações, garantindo consistência e completude.

A sétima etapa é a revisão estrutural do modelo de dados. Com todos os objetos já documentados, é possível avaliar se a estrutura está aderente ao modelo estrela e se não há problemas de relacionamentos ou ambiguidades.

A oitava etapa é a análise de segurança e escalabilidade. Esta é a etapa final, que avalia aspectos não funcionais do modelo e propõe melhorias para prepará-lo para o futuro.

---

## 6. Extensões e Uso Avançado

Além dos comandos fundamentais e avançados apresentados, existem várias extensões que podem agregar valor significativo ao modelo de dados. Estas extensões estão alinhadas com o contexto de TCC em Ciência de Dados na Gestão de Ouvidorias e com a identidade visual Rebel Analytics.

### 6.1. Análise de Pareto

A análise de Pareto (também conhecida como regra 80/20) é uma técnica poderosa para identificar os fatores que mais contribuem para um problema. No contexto de ouvidorias, pode ser utilizada para identificar, por exemplo, quais 20% dos assuntos são responsáveis por 80% das reclamações, permitindo que os gestores priorizem ações de melhoria nos pontos de maior impacto.

**Comando MCP sugerido:**

```text
Crie uma medida DAX de Análise de Pareto para identificar quais são os 20% dos assuntos que geram 80% do volume de reclamações na Ouvidoria.

Apresente:
- lógica de cálculo cumulativo
- visualização sugerida
- interpretação dos resultados
```

### 6.2. Clusterização K-Means

A clusterização é uma técnica de machine learning que agrupa dados em categorias baseadas em similaridade. No contexto de ouvidorias, pode ser utilizada para segmentar manifestações com base em características como tempo de resposta e nota de satisfação, identificando grupos como "Alta Eficiência" vs "Baixa Satisfação".

**Comando MCP sugerido:**

```text
Escreva um script em Python para ser executado no Power Query que realize a clusterização (K-Means) das manifestações, utilizando como variáveis o 'Tempo de Resposta' e a 'Nota de Satisfação', para identificar os grupos de 'Alta Eficiência' vs 'Baixa Satisfação'.

Apresente:
- código Python completo
- lógica de normalização das variáveis
- interpretação dos clusters
- sugestão de integração com o modelo
```

### 6.3. Análise de Sentimento

A análise de sentimento utiliza técnicas de NLP para classificar textos com base no tom emocional — crítico, neutro ou positivo. No contexto de ouvidorias, pode ser aplicada aos textos das manifestações para identificar automaticamente o teor das reclamações, elogios ou sugestões.

**Comando MCP sugerido:**

```text
Sugira uma integração via API (ou script Python) para realizar a Análise de Sentimento dos comentários das manifestações, criando uma nova coluna que classifique o texto em 'Crítico', 'Neutro' ou 'Positivo'.

Apresente:
- opções de implementação (API externa ou biblioteca Python local)
- código sugerido
- consideração de custos e privacidade
```

### 6.4. Tema Visual Rebel Analytics

Para manter a consistência visual com a identidade Rebel Analytics, pode-se criar um arquivo JSON de tema que padronize cores, fontes e estilos em todos os visuais do relatório. O tema deve seguir o conceito minimalista e futurista, com foco em modo escuro (dark mode).

**Comando MCP sugerido:**

```text
Gere um arquivo JSON de Tema (Theme File) para o Power BI utilizando a paleta de cores da Rebel Analytics, com foco em modo escuro (dark mode), fontes sem serifa e estilos de cartões com bordas arredondadas e sutis.

Apresente:
- estrutura JSON completa
- cores primárias, secundárias e de destaque
- definições de fonte
- estilos devisualização (cartões, gráficos, tabelas)
```

### 6.5. Formatação Condicional Avançada

A formatação condicional padrão do Power BI (verde/vermelho) pode ser substituída por lógicas mais sofisticadas que considerem a proximidade do prazo de resposta, indicando urgência de forma mais nuanceda.

**Comando MCP sugerido:**

```text
Crie uma lógica de Formatação Condicional para os KPIs de SLA, onde as cores não sejam apenas o padrão verde/vermelho, mas sigam um gradiente que indique a urgência baseada na proximidade do vencimento do prazo legal.

Considere:
- verde: prazo suficiente (> 10 dias restantes)
- amarelo: atenção (5-10 dias restantes)
- laranja: urgência (1-5 dias restantes)
- vermelho: vencido ou vencendo hoje
```

---

## 7. Considerações Finais

Este kit de comandos representa uma abordagem sistemática para a revisão e otimização de modelos semânticos no Power BI. Cada comando foi desenhado para produzir resultados específicos e acionáveis, e a execução em sequência garante uma cobertura completa de todos os aspectos relevantes do modelo.

A aplicação deste kit em projetos de ouvidorias públicas traz benefícios tangíveis para a gestão. Com um modelo bem estruturado e documentado, os gestores podem tomar decisões baseadas em dados confiáveis, monitorar indicadores de desempenho em tempo real e identificar problemas antes que se tornem crises. A governança de dados garante que essas informações sejam utilizadas de forma ética e em conformidade com a LGPD.

O alinhamento com a identidade visual Rebel Analytics — minimalista, futurista e orientada ao dado — garante que os dashboards resultantes não apenas informem, mas também inspirem os usuários a explorar os dados e descobrir insights que possam melhorar o serviço público.

Recomenda-se que este kit seja utilizado como referência viva, sendo atualizado conforme novas necessidades surgem e novas técnicas se tornam disponíveis. O campo de análise de dados evolui rapidamente, e a atualização contínua deste kit garante que as práticas permaneçam relevantes e eficazes.

---

*Documento desenvolvido por Rebel Analytics — Ciência de Dados na Gestão de Ouvidorias*
