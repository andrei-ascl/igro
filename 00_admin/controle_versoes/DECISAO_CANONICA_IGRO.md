---
title: "Registro de decisão canônica do IGRO"
date: 2026-08-10
project: igro
status: decidido-no-projeto
decision_scope: "baseline metodológico de trabalho; validação institucional pendente"
owner: "Proprietário do projeto / GT de Gestão de Riscos"
---

# Registro de decisão canônica do IGRO

## Decisão adotada

Em 2026-08-10, o projeto adotou o perfil do Desenho Técnico como baseline
canônico do IGRO. A decisão vale para o cálculo operacional, para o Power BI e
para a especificação principal de uma nova publicação.

Esta é uma decisão de trabalho registrada no projeto. A validação formal das
metas pelo GT de Gestão de Riscos e a aprovação da integração à Matriz ainda
precisam ser obtidas; elas não devem ser confundidas com a escolha técnica
registrada aqui.

## Justificativa da escolha

- O PRD define que o MVP deve usar as fórmulas de 10_Desenho_IGRO.md e
  exclui comparação entre órgãos do escopo inicial.
- O Desenho Técnico é o documento central com justificativas substantivas para
  os pesos, goalposts, agregação e ciclo quadrimestral.
- A análise de sensibilidade mostrou que a média geométrica é importante para
  evitar compensação excessiva; a alteração para média aritmética mudou a
  classificação de 29 dos 47 órgãos analisados.
- As variações de pesos produziram rankings altamente correlacionados, então a
  escolha dos pesos do Desenho Técnico é defensável sem descartar a análise de
  sensibilidade.

## Parâmetros canônicos

### KRIs, metas, goalposts e pesos globais

| KRI | Indicador | Direção | Meta | Goalpost | Peso global | Fonte operacional |
|---|---|---|---:|---:|---:|---|
| 1 | % de manifestações acima de 30 dias | Menor é melhor | 2,0% | 15,0% | 15% | f_relatorio |
| 2 | Prazo médio de resposta | Menor é melhor | 10,0 dias | 30,0 dias | 25% | f_relatorio |
| 3 | Resolutividade declarada na pesquisa | Maior é melhor | 70,0% | 30,0% | 25% | f_pesquisa |
| 4 | % de respostas insatisfatórias | Menor é melhor | 2,5% | 20,0% | 15% | f_insatisfatorias |
| 5 | Nota de recomendação | Maior é melhor | 7,5 | 4,0 | 20% | f_pesquisa |

Os scores são normalizados por distância à meta com goalpost e limitados ao
intervalo [0, 1]. Superar a meta não gera score acima de 1,0.

### Agregação

~~~text
Sub_T = (0,15 × score_1 + 0,25 × score_2) / 0,40
Sub_Q = (0,25 × score_3 + 0,15 × score_4 + 0,20 × score_5) / 0,60
IGRO  = Sub_T^0,40 × Sub_Q^0,60
~~~

A agregação é aritmética ponderada dentro de cada risco e geométrica ponderada
entre Tempestividade e Qualidade. O IGRO não deve ser substituído por média
aritmética sem identificá-la como cenário alternativo.

### Semaforização

| Faixa | Classe |
|---:|---|
| 0,80–1,00 | Risco Baixo |
| 0,60–0,79 | Risco Moderado |
| 0,40–0,59 | Risco Alto |
| 0,00–0,39 | Risco Crítico |

### Regra amostral

KRI 3 e KRI 5 usam respostas da pesquisa enviada ao cidadão. A classificação
de confiabilidade da pesquisa é:

~~~text
amostra adequada     se n_pesquisa >= 30 OU cobertura >= 5%
amostra insuficiente se n_pesquisa < 30 E cobertura < 5%
~~~

cobertura é calculada como respostas de pesquisa divididas pelas manifestações
finalizadas identificadas, excluindo manifestações anônimas. Quando a amostra
for insuficiente, os valores brutos continuam visíveis, mas os scores de
pesquisa, o Sub-Q e o IGRO canônico devem ficar sem cálculo (BLANK/"não
calculado"), acompanhados da sinalização de amostra insuficiente. Ausência de
evidência não deve ser convertida em score zero.

### Período e escopo de interpretação

- O ciclo oficial é quadrimestral: jan–abr, mai–ago e set–dez.
- O uso canônico é longitudinal, comparando cada órgão consigo mesmo ao longo
  dos quadrimestres.
- Rankings entre órgãos não são saída canônica. Qualquer comparação entre
  órgãos deve ser identificada como análise descritiva/sensibilidade e só pode
  ser promovida após validação específica de comparabilidade.

## Tratamento das variantes existentes

| Variante | Tratamento após esta decisão |
|---|---|
| Desenho Técnico | Perfil canônico de trabalho |
| PBIP/TMDL atual | Perfil legado; deve ser alinhado ao contrato antes de novo uso |
| Artigo/análise de sensibilidade com pesos uniformes | Cenário de sensibilidade/publicação, não fonte operacional |

Os resultados antigos não serão sobrescritos. Eles devem ser recalculados com o
perfil canônico antes de serem usados em briefing executivo ou nova submissão.

## Critérios de fechamento da implementação

- [x] Perfil canônico escolhido e registrado.
- [x] Metas, goalposts, pesos e agregação especificados.
- [x] Regra amostral e escopo longitudinal especificados.
- [ ] PBIP/TMDL alinhado aos parâmetros canônicos.
- [ ] Resultados históricos recalculados e comparados com os derivados antigos.
- [ ] Metas e goalposts validados formalmente pelo GT de Gestão de Riscos.
- [ ] Inclusão do IGRO na Matriz aprovada pelo Comitê Setorial.

## Próxima execução

Alinhar as medidas idx_score_igro_kri1 a idx_igro do PBIP ao perfil acima,
aplicar o gate amostral sem converter ausência em zero e recalcular as saídas
com a versão do contrato registrada no projeto.

## Dependências institucionais remanescentes

- confirmação formal das metas e goalposts pela Matriz de Gestão de Riscos;
- confirmação operacional da fonte de resolutividade para cada ciclo de dados;
- aprovação do Comitê Setorial para uso do IGRO como instrumento da Matriz.

