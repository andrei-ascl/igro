## 3.6 Limitações metodológicas

Algumas limitações metodológicas devem ser consideradas na interpretação dos resultados.

A primeira refere-se à dependência da qualidade dos registros operacionais inseridos no SGOe. Embora o sistema possua padronização institucional, diferenças locais de preenchimento podem introduzir variabilidade não observada.

A segunda limitação relaciona-se ao viés de autorresposta na pesquisa de satisfação. Indicadores como RP e NR dependem de resposta voluntária do cidadão. A taxa de resposta pode variar significativamente entre órgãos, introduzindo viés sistemático: cidadãos com experiências extremas (muito positivas ou muito negativas) tendem a responder com maior frequência. Além disso, órgãos com baixo número de respondentes apresentaram maior sensibilidade estatística, especialmente no cálculo do NPS. Conforme registrado na Nota Técnica de metodologia, "a validade estatística desses KRIs depende diretamente do número de respondentes. Uma amostra pequena produz estimativas imprecisas, podendo classificar erroneamente um órgão em uma faixa de risco incorreta". Esse risco é particularmente relevante em órgãos de pequeno porte (Classes 4 e 5), onde o volume de manifestações respondidas pode ser inferior ao limiar de representatividade estatística.

**Tabela — Taxa de resposta à pesquisa de satisfação por classe operacional:**

| Classe operacional | Manifestações (n) | Respondentes pesquisa (n) | Taxa de resposta (%) |
|:-------------------|:-------------------|:--------------------------|:---------------------|
| Cl.1 | 47.821 | 5.318 | 11,1% |
| Cl.2 | 45.909 | 3.432 | 7,5% |
| Cl.3 | 12.735 | 1.311 | 10,3% |
| Cl.4 | 4.530 | 590 | 13,0% |
| Cl.5 | 1.444 | 191 | 13,2% |

A análise revela cenário misto de representatividade: (i) Classes 1, 2 e 3 apresentam volumes absolutos robustos (5.318, 3.432 e 1.311 respondentes, respectivamente), suficientes para cálculos agregados; (ii) Classe 4 oscila na fronteira de adequação, com aproximadamente 49 respondentes médios por órgão, potencialmente abaixo do limiar recomendado de 30 respondentes em alguns casos; (iii) Classe 5 configura cenário de maior fragilidade estatística, com média de aproximadamente 8 respondentes por órgão, gerando risco elevado de classificação errônea dos indicadores de qualidade.

Três órgãos foram marcados na base como tendo amostra insuficiente (`flag_amostra = 1`): CEASA (3 respondentes em 164 manifestações), GOIASPARCERIAS (zero respondentes) e GOIAS TELECOM (zero respondentes). Esses órgãos devem ser tratados com nota metodológica ou excluídos do cálculo de indicadores perceptivos (RP, NR, %RI) em agregações por classe. Conforme recomendado na Nota Técnica de metodologia, órgãos com menos de 30 respondentes apresentam estabilidade estatística comprometida, especialmente no cálculo do NPS, e devem receber tratamento diferenciado (exclusão do cálculo individual ou aplicação de estimativa bayesiana para suavização).

Outra limitação refere-se à própria utilização da média geométrica. Embora o método reduza compensações indevidas entre dimensões, ele também aumenta a sensibilidade do índice a desempenhos muito baixos em indicadores específicos.

Por fim, o estudo possui recorte transversal ampliado, mas ainda carece de validação longitudinal em períodos mais extensos.

## 3.7 Aspectos éticos e proteção de dados

O presente estudo utilizou exclusivamente dados administrativos agregados, extraídos do SGOe. Todos os indicadores foram calculados em nível de órgão público, sem identificação individual de cidadãos manifestantes ou servidores responsáveis pelo atendimento.

Embora a publicação de rankings de desempenho por órgão não envolva dados pessoais stricto sensu, é importante observar que a Lei Geral de Proteção de Dados (LGPD — Lei nº 13.709/2018) exige atenção mesmo em contextos de dados agregados quando a granularidade é elevada. Em órgãos com volume reduzido de manifestações, a combinação de tipo de manifestação, período e setor responsável poderia, em tese, permitir inferências sobre manifestantes específicos.

Para mitigar esse risco, os dados utilizados neste estudo foram tratados em nível agregado por órgão e período, sem desagregação por tipo de manifestação, canal de entrada ou unidade administrativa interna. Além disso, a pesquisa de satisfação utilizada como fonte dos indicadores de qualidade é anônima por design.
