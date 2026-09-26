---
title: "Contrato de métricas e proveniência do IGRO"
date: 2026-08-10
project: igro
status: metodo-canonico-dados-em-reconciliacao
version: "0.2"
---

# Contrato de métricas e proveniência do IGRO

> A variante canônica do método foi definida em 2026-08-10. Este contrato
> registra os parâmetros adotados e separa as validações institucionais e de
> dados que ainda precisam ser concluídas.

## Objetivo

Garantir que cada execução do IGRO informe fonte, período, universo,
denominadores, regra amostral, parâmetros de normalização, pesos, fórmula de
agregação e escopo de interpretação. Nenhum resultado deve ser interpretado
sem esses metadados.

## Perfil metodológico canônico

O perfil canônico é o Desenho Técnico do IGRO:

- normalização por distância à meta com goalposts, score limitado a [0, 1];
- pesos globais de 15%, 25%, 25%, 15% e 20% para os cinco KRIs;
- média aritmética ponderada dentro de cada subíndice;
- agregação final IGRO = Sub_T^0,40 × Sub_Q^0,60;
- interpretação longitudinal por órgão e quadrimestre;
- pesos uniformes e o perfil PBIP anterior permanecem como cenários/legado.

## Fontes observadas

| Camada | Local | Papel |
|---|---|---|
| Dados brutos de referência | 02_dados/raw/ | Extrações originais preservadas |
| Extrações posteriores | 06_dados/01_brutos/ | Staging legado; requer reconciliação com 02_dados/raw/ |
| Modelo | 07_dashboards/powerbi/04_powerbi_e_dax/indice_igro_v2.SemanticModel/ | Medidas, relacionamentos e saídas |
| Método | 00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md | Perfil canônico |
| Decisão | 00_admin/controle_versoes/DECISAO_CANONICA_IGRO.md | Governança metodológica |
| Evidência | 04_notas_tecnicas/final/nota_tecnica_analise_sensibilidade_igro.md | Robustez e cenários |

## Grão mínimo da saída

Cada execução deve produzir, por período e órgão:

- identificador do órgão;
- período e data de corte;
- volume de manifestações e finalizadas;
- número de pesquisas respondidas;
- taxa de cobertura da pesquisa;
- cinco valores brutos dos KRIs;
- cinco scores normalizados;
- dois subíndices;
- IGRO final;
- classe/semaforização;
- flag e categoria de confiabilidade amostral;
- perfil metodológico, versão do contrato e fonte da extração.

Quando a amostra for insuficiente, os valores brutos permanecem disponíveis, mas
Sub-Q e IGRO ficam sem cálculo; não usar zero como substituto de ausência.

## Catálogo canônico de métricas

| KRI | Nome operacional | Direção | Meta | Goalpost | Peso global | Fonte |
|---|---|---|---:|---:|---:|---|
| KRI 1 | Percentual de manifestações acima de 30 dias | Menor é melhor | 2,0% | 15,0% | 15% | f_relatorio |
| KRI 2 | Tempo médio de resposta | Menor é melhor | 10,0 dias | 30,0 dias | 25% | f_relatorio |
| KRI 3 | Resolutividade declarada na pesquisa | Maior é melhor | 70,0% | 30,0% | 25% | f_pesquisa |
| KRI 4 | Percentual de respostas insatisfatórias | Menor é melhor | 2,5% | 20,0% | 15% | f_insatisfatorias |
| KRI 5 | Nota de recomendação | Maior é melhor | 7,5 | 4,0 | 20% | f_pesquisa |

## Fórmulas canônicas

Para indicadores em que menor é melhor:

~~~text
score = max(0, min(1, (goalpost - valor) / (goalpost - meta)))
~~~

Para indicadores em que maior é melhor:

~~~text
score = max(0, min(1, (valor - goalpost) / (meta - goalpost)))
~~~

~~~text
Sub_T = (0,15 × score_1 + 0,25 × score_2) / 0,40
Sub_Q = (0,25 × score_3 + 0,15 × score_4 + 0,20 × score_5) / 0,60
IGRO  = Sub_T^0,40 × Sub_Q^0,60
~~~

## Pré-condições obrigatórias

1. O período deve estar fechado e declarado como jan–abr, mai–ago ou set–dez.
2. O universo de órgãos deve distinguir total disponível e casos completos para
   os cinco KRIs.
3. Numeradores, denominadores, nulos, duplicidades e filtros devem estar
   registrados.
4. O perfil metodológico e a versão deste contrato devem ser informados antes
   do cálculo.
5. Para KRI 3 e KRI 5, a amostra é adequada quando n_pesquisa >= 30 ou a
   cobertura >= 5%; caso contrário, a saída fica marcada como insuficiente e o
   IGRO não é calculado.
6. A saída deve ser recalculável a partir das fontes preservadas ou indicar por
   que a reprodução não é possível.

## Quality gates de uma execução

- [ ] Fonte e data de extração registradas.
- [ ] Período e coorte fechados registrados.
- [ ] Schema e tipos conferidos.
- [ ] Duplicidades e nulos avaliados.
- [ ] Numeradores e denominadores preservados.
- [ ] Regra amostral aplicada e exibida.
- [x] Perfil metodológico identificado.
- [x] Fórmula e parâmetros versionados.
- [ ] Resultado validado contra pelo menos um cálculo independente.
- [ ] Limitações e escopo longitudinal exibidos no produto final.

## Pendências de implementação e governança

- alinhar o PBIP/TMDL ao perfil canônico;
- recalcular os resultados históricos e comparar com os derivados anteriores;
- reconciliar as extrações posteriores de 06_dados/01_brutos com a fonte
  documentada em 02_dados/raw/;
- confirmar formalmente metas e goalposts com o GT de Gestão de Riscos;
- confirmar a fonte operacional de resolutividade em cada ciclo;
- obter aprovação do Comitê Setorial para integração à Matriz.

## Regra de revisão

Revisar este contrato sempre que houver mudança em fonte, período, definição de
KRI, meta, goalpost, peso, agregação, regra amostral ou escopo de comparação.

