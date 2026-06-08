# Análise dos resultados por indicador até Q1/2026

## Escopo

Esta nota analisa os três indicadores exibidos no dashboard quadrimestral do IGRO:

- `IGRO`
- `Subíndice de Tempestividade`
- `Subíndice de Qualidade`

Por solicitação do usuário, o ponto `Q2/2026` foi desconsiderado. A leitura, portanto, vai de `Q1/2024` até `Q1/2026`, com base nos valores visíveis no material do dashboard compartilhado.

## Série considerada

| Período | IGRO | Subíndice de Tempestividade | Subíndice de Qualidade |
|---|---:|---:|---:|
| Q1/2024 | 69,1 | 73,8 | 64,6 |
| Q2/2024 | 79,6 | 91,0 | 69,7 |
| Q3/2024 | 72,7 | 73,7 | 71,7 |
| Q1/2025 | 68,0 | 75,3 | 61,5 |
| Q2/2025 | 75,4 | 84,6 | 67,2 |
| Q3/2025 | 71,1 | 83,7 | 60,4 |
| Q1/2026 | 62,6 | 88,8 | 44,2 |

## Leitura por indicador

### 1. IGRO

O `IGRO` apresentou comportamento oscilante ao longo da série, mas com perda de desempenho no trecho final. Após sair de `69,1` em `Q1/2024`, atingiu seu melhor valor em `Q2/2024` (`79,6`), voltou a recuar em `Q3/2024` e `Q1/2025`, recuperou parte do resultado em `Q2/2025` (`75,4`) e encerrou a série considerada em `62,6` no `Q1/2026`.

Os dados sugerem três movimentos relevantes:

- entre `Q1/2024` e `Q3/2025`, o índice permaneceu em uma faixa intermediária, com oscilações, mas sem ruptura estrutural;
- em `Q1/2026`, há uma piora mais forte, com queda de `8,5 p.p.` em relação a `Q3/2025`;
- no acumulado da série analisada, o índice termina `6,5 p.p.` abaixo do ponto inicial.

Em termos interpretativos, o `IGRO` já não sinaliza apenas volatilidade normal entre quadrimestres. Em `Q1/2026`, ele passa a refletir deterioração mais consistente do risco operacional agregado da ouvidoria.

### 2. Subíndice de Tempestividade

O `Subíndice de Tempestividade` foi o componente mais estável e, no recorte até `Q1/2026`, também o mais favorável. A série saiu de `73,8` em `Q1/2024`, alcançou `91,0` em `Q2/2024`, recuou no quadrimestre seguinte, mas retomou trajetória ascendente ao longo de 2025 até chegar a `88,8` em `Q1/2026`.

Os principais sinais da série são:

- ganho de `15,0 p.p.` entre `Q1/2024` e `Q1/2026`;
- crescimento de `5,1 p.p.` na comparação com `Q3/2025`;
- manutenção em patamar próximo da meta visual de `90%` no fim da série analisada.

Isso indica que o risco ligado ao prazo de resposta estava relativamente mais controlado do que os demais componentes do índice. A dimensão temporal não parece ser a principal explicação para a deterioração do resultado global até `Q1/2026`.

### 3. Subíndice de Qualidade

O `Subíndice de Qualidade` é o ponto crítico da série. Embora tenha começado em `64,6` e atingido `71,7` em `Q3/2024`, a trajetória posterior foi de enfraquecimento. Depois de cair para `61,5` em `Q1/2025`, houve recuperação parcial em `Q2/2025` (`67,2`), seguida de nova piora em `Q3/2025` (`60,4`) e queda acentuada para `44,2` em `Q1/2026`.

Os sinais mais importantes são:

- perda de `20,4 p.p.` entre `Q1/2024` e `Q1/2026`;
- queda de `16,2 p.p.` apenas no último intervalo observado;
- encerramento da série muito abaixo da faixa de atenção de `70%`.

Esse comportamento indica deterioração relevante da qualidade percebida ou entregue pelo atendimento. No plano gerencial, a série sugere que o problema deixou de ser episódico e passou a comprometer estruturalmente o desempenho do índice composto.

## Síntese interpretativa

A leitura conjunta dos três indicadores mostra um quadro claro: até `Q1/2026`, o principal vetor de piora do `IGRO` não foi a tempestividade, mas sim a qualidade.

Essa conclusão é consistente com a arquitetura metodológica do projeto, descrita em [10_Desenho_IGRO.md](C:\Users\andre\OneDrive\Claude-Work\Projects\igro\00_admin\planejamento\03_especificacao_e_produto\10_Desenho_IGRO.md), na qual:

- `Tempestividade` tem peso de `40%`;
- `Qualidade` tem peso de `60%`;
- a agregação final do `IGRO` é não compensatória entre subíndices.

Na prática, isso significa que a melhora do componente temporal não é suficiente para neutralizar uma queda forte na qualidade. Foi exatamente o que ocorreu no fechamento em `Q1/2026`: mesmo com `Subíndice de Tempestividade` em `88,8`, a queda do `Subíndice de Qualidade` para `44,2` puxou o `IGRO` para `62,6`.

## Conclusão executiva

Desconsiderando `Q2/2026`, o quadro até `Q1/2026` pode ser resumido assim:

- o `IGRO` entra em trajetória de piora no trecho final da série;
- a `Tempestividade` permanece relativamente robusta e próxima da meta visual;
- a `Qualidade` é o gargalo central e o principal fator de risco do período;
- a prioridade analítica e gerencial deve recair sobre os KRIs que compõem o subíndice de qualidade, especialmente `Resolutividade`, `Respostas Insatisfatórias` e `Nota de Recomendação`.

## Observação metodológica

Esta nota foi construída a partir dos valores mostrados no dashboard enviado na conversa, sem incorporar o ponto `Q2/2026`. Se for necessário, uma próxima etapa pode detalhar a mesma análise no nível dos cinco KRIs do modelo.
