# Benchmarking de KRIs em Ouvidorias Estaduais Brasileiras

## Contexto: O Sistema Nacional de Ouvidorias

O sistema de ouvidorias públicas brasileiras opera sob um arcabouço normativo que cria condições para benchmarking, embora sua efetivação seja desigual entre as esferas. Os principais marcos são:

- **Lei 13.460/2017** — estabelece prazos, tipos de manifestação e exige avaliação de satisfação; é a principal referência para metas de KRIs em todo o Brasil
- **Decreto 9.492/2018** — regulamenta a Lei 13.460 no Executivo Federal, define o prazo-padrão de 20 dias úteis e cria o Painel de Monitoramento de Ouvidorias
- **Instrução Normativa CGU nº 8/2017** — orienta a estruturação de sistemas de ouvidoria no Executivo Federal
- **Resolução OGU nº 2/2022** — define as tipologias de manifestações (reclamação, denúncia, solicitação, elogio, sugestão) com padronização que facilita comparações

A CGU/OGU consolida dados do Poder Executivo Federal via **e-Ouv** (Sistema de Ouvidorias do Poder Executivo Federal) e publica periodicamente o **Painel de Monitoramento de Ouvidorias**, que funciona como o principal instrumento de benchmarking nacional disponível publicamente.

---

## KRIs Padronizados no Sistema Federal

O sistema federal acompanha um conjunto de métricas que funcionam na prática como KRIs — não apenas KPIs de desempenho, mas sinais de risco de falha no atendimento:

| KRI | Definição operacional | Sentido | Limiar de referência (Lei 13.460) |
|-----|-----------------------|---------|-----------------------------------|
| Taxa de atendimento no prazo | % manifestações respondidas em até 20 dias úteis | Maior = melhor | Meta: 100%; alerta abaixo de 90% |
| Taxa de resolutividade | % manifestações com solução efetiva registrada | Maior = melhor | Não há padrão legal; varia por órgão |
| Taxa de prorrogação | % manifestações com prazo prorrogado | Menor = melhor | Sinaliza pressão sistêmica sobre prazo |
| Taxa de satisfação (NPS simplificado) | % usuários satisfeitos na pesquisa de satisfação | Maior = melhor | Não há padrão nacional definido |
| Taxa de reincidência | % manifestantes que retornam com o mesmo tema | Menor = melhor | Indica falha estrutural não resolvida |

> **Atenção:** A definição de "resolutividade" varia entre sistemas — alguns contam a manifestação como resolvida ao dar uma resposta, outros apenas quando a solicitação foi efetivamente atendida. Verificar a definição local antes de comparar.

---

## GCOuv — O Índice Composto Existente

O **Grau de Confiança na Ouvidoria (GCOuv)** é o único índice composto padronizado para ouvidorias públicas brasileiras, desenvolvido pela CGU/OGU. Sua relevância para este projeto é dupla: serve como referência metodológica e como fonte de benchmarking.

### Estrutura do GCOuv

O GCOuv agrega dimensões relacionadas à confiança do cidadão na ouvidoria como canal de participação. Embora sua composição detalhada não seja totalmente pública, as dimensões documentadas incluem:

- Percepção de resolutividade pelo manifestante
- Percepção de prazo de atendimento
- Satisfação geral com o canal
- Intenção de uso futuro

### Limitações do GCOuv como KRI

O GCOuv mede **percepção do usuário** — é um indicador de resultado (outcome), não um indicador de risco operacional. Não captura, por exemplo, se manifestações estão acumulando fora do prazo internamente antes de chegar ao usuário. Para gestão de riscos, o GCOuv é complementar, não substituto dos KRIs operacionais da Matriz.

---

## Panorama dos Estados: Heterogeneidade e Desafios de Comparação

### Situação dos sistemas estaduais

Os estados brasileiros apresentam três perfis distintos no que se refere à mensuração e publicação de KRIs:

**Perfil A — Sistemas integrados ao federal:**
Alguns estados aderiram ao e-Ouv ou desenvolveram sistemas interoperáveis com a CGU. Nesses casos, os KRIs federais são aplicáveis diretamente e a comparação com ouvidorias federais é metodologicamente válida.

**Perfil B — Sistemas próprios com indicadores parcialmente comparáveis:**
Estados como São Paulo (SP156/Fale Conosco) e Minas Gerais possuem sistemas próprios com relatórios públicos, mas as métricas são definidas internamente e nem sempre comparáveis com o padrão federal. Por exemplo, o prazo de referência pode ser diferente dos 20 dias úteis federais.

**Perfil C — Sistemas sem publicação sistemática de KRIs:**
A maioria dos estados não publica dados desagregados em formato que permita benchmarking direto. Os relatórios, quando existem, são anuais e apresentam dados consolidados sem possibilidade de análise por tipo de risco.

### Principais barreiras ao benchmarking estadual

1. **Ausência de taxonomia comum:** "Reclamação resolvida" pode significar coisas diferentes entre estados
2. **Diferentes sistemas de TI:** A fragmentação tecnológica impede extração automatizada de indicadores comparáveis
3. **Variação nos prazos-referência:** A Lei 13.460 se aplica ao Executivo Federal diretamente; estados e municípios dependem de legislação própria para adotar os mesmos padrões
4. **Baixa publicidade de dados operacionais:** Estados tendem a publicar números de manifestações, não indicadores de risco por tipo de falha
5. **Divergência na definição de "manifestação":** Alguns sistemas incluem consultas e pedidos de informação LAI no mesmo banco; outros separam

---

## Fontes de Dados para Benchmarking Disponíveis

### Nacionais (fontes verificadas)

| Fonte | O que publica | Periodicidade | Acesso |
|-------|--------------|---------------|--------|
| Painel de Monitoramento de Ouvidorias (CGU) | KRIs das ouvidorias do Executivo Federal | Contínuo | [ouvidorias.gov.br](https://www.ouvidorias.gov.br/ouvidorias/monitoramento) |
| Relatório Anual das Ouvidorias (OGU/CGU) | Dados consolidados do sistema federal | Anual | Repositório CGU |
| e-Ouv (Sistema Federal) | Dados brutos para órgãos aderentes | Contínuo | Acesso restrito por órgão |
| LAI — Portal da Transparência | Pedidos LAI permitem obter dados de estados | Sob demanda | Gov.br |

### Estaduais selecionados (exemplos com publicação regular)

| Estado | Instrumento | Indicadores disponíveis |
|--------|-------------|------------------------|
| SP | Relatório SP156 / Secretaria de Gestão | Volume, prazo, satisfação |
| MG | Relatório Ouvidoria-Geral do Estado | Volume por tipo, prazo médio |
| RS | Portal da Ouvidoria-Geral | Volume, resolutividade |
| BA | Relatório OGE-BA | Volume, prazos |

> **Nota metodológica:** Os dados estaduais listados acima devem ser verificados diretamente nos portais dos estados, pois publicações podem ser descontinuadas ou alteradas. Recomenda-se consulta via LAI para obter séries históricas detalhadas.

---

## OGDF/SIGO-DF: O Benchmarking Mais Próximo

O sistema do Distrito Federal é o referencial de benchmarking mais direto para ouvidorias vinculadas ao GDF, pois compartilham o mesmo sistema (SIGO-DF), a mesma taxonomia de manifestações e o mesmo arcabouço normativo distrital (Lei nº 4.896/2012, Decreto nº 36.462/2015, Lei Distrital nº 6.519/2020).

### O que a OGDF publica

| Instrumento | Conteúdo | Limitação |
|-------------|----------|-----------|
| **Painel de Ouvidoria do DF** (`painel.ouv.df.gov.br`) | Volume por tipo, assuntos mais demandados, prazos, indicadores de desempenho, **ranking entre os 93 órgãos** | Metodologia do ranking **não documentada publicamente** |
| **Índice de Resolutividade SIGO-DF** | Avaliação pós-atendimento pelo cidadão; apresentado como "principal inovação do SIGO-DF" | Mede percepção (outcome), não risco operacional; definição de "resolvido" não padronizada entre órgãos |
| **Relatórios trimestrais** | Volume de manifestações, variações entre períodos, assuntos mais demandados | Não desagregam por indicadores de risco; sem faixas de alerta |
| **Guia Prático para Ouvidorias do GDF – 2025** | Fluxos de atendimento, governança, proteção de dados | Não aborda KRIs, índices compostos nem metodologia de avaliação de risco |

### Lacunas identificadas na pesquisa (março 2026)

A pesquisa nas fontes públicas da OGDF e CGDF não identificou:

- **KRIs formais** por tipo de risco de atendimento (prazo, qualidade)
- **Índice composto de risco** para ouvidorias do SIGO-DF
- **Metodologia documentada** do ranking do Painel (fórmula, pesos, critérios)
- **Integração formal** entre o Portal de Gestão de Riscos da CGDF e o SIGO-DF
- **Metas numéricas públicas** por indicador além do prazo legal

O **Projeto Ouvidoria Destaque** (lançado em 2025), que visa reconhecer órgãos por excelência, pode vir a preencher parcialmente essa lacuna — mas seus critérios não foram publicados até a data desta pesquisa.

### Iniciativas relevantes da rede SIGO-DF (Concurso de Melhores Práticas, 6ª edição)

As práticas inscritas pelos órgãos do GDF revelam o nível real de maturidade em gestão por indicadores:

- **CAESB — "Ouvidoria Ativa"**: comunicação proativa baseada em análise de dados para antecipar problemas — a prática mais próxima de uso preditivo de indicadores encontrada na rede
- **SEJUS — "Gestão da Qualidade da Resposta"**: verificação da qualidade da resposta antes do envio ao cidadão
- **DF Legal — "Painel da Ouvidoria do DF Legal"**: sistema interativo com comparação de dados entre períodos
- **IPREV/DF — "Relatório Dinâmico"**: interface de divulgação de manifestações com linguagem acessível

Nenhuma iniciativa inscrita propõe framework de KRI ou índice composto formal.

### Implicação para o IGRO

O IGRO (Índice de Gestão de Riscos da Ouvidoria), tal como estruturado neste projeto, **não tem equivalente publicado no SIGO-DF**. A ausência de um framework de KRIs integrado à Matriz de Gestão de Riscos é uma lacuna real no sistema distrital — o que posiciona o IGRO como contribuição potencialmente pioneira nesse contexto.

**Ação recomendada:** Solicitar via LAI à CGDF a metodologia do ranking do Painel de Ouvidoria (`painel.ouv.df.gov.br`). Pode conter critérios e pesos úteis para calibração, ainda que não publicados na documentação aberta.

---

## Estratégia de Benchmarking para a Matriz de Gestão de Riscos

Dado o cenário de heterogeneidade, propõe-se uma estratégia em três camadas:

### Camada 1 — Benchmarking interno (mais confiável)

Comparar os KRIs da ouvidoria **com ela mesma** ao longo do tempo (quadrimestres, anos). Este é o benchmarking mais robusto metodologicamente porque elimina problemas de definição e sistema. Permite identificar tendências e sazonalidade.

```
Exemplo: O KRI "% manifestações > 30 dias" passou de 0,40% (Q1) para 0,65% (Q2)?
→ Sinal de deterioração independente de comparação externa
```

### Camada 2 — Benchmarking com órgãos federais (sistema e-Ouv)

Se a ouvidoria utiliza o e-Ouv ou sistema compatível, comparar com a mediana das ouvidorias federais de porte similar (por volume de manifestações). O Painel de Monitoramento CGU permite essa comparação para os KRIs padronizados.

**Agrupamento sugerido por porte:**
- Pequeno: < 5.000 manifestações/ano
- Médio: 5.000 a 30.000 manifestações/ano
- Grande: > 30.000 manifestações/ano

### Camada 3 — Benchmarking estadual (referência complementar)

Usar os relatórios públicos de estados com sistemas mais desenvolvidos (SP, MG, RS) como referência de metas aspiracionais. Não comparar diretamente scores — comparar **faixas de desempenho** e tendências.

---

## Metas de Referência Derivadas do Panorama Nacional

Com base nos dados publicados pelo sistema federal e na Lei 13.460/2017, propõem-se as seguintes faixas de referência para os KRIs da Matriz:

| KRI | Referência legal | Referência boas práticas | Sinal de alerta |
|-----|-----------------|--------------------------|-----------------|
| % manifestações > 30 dias (prazo total) | — | < 2% | > 5% |
| Prazo Médio de Resposta | ≤ 20 dias úteis (~30 dias corridos) | ≤ 10 dias úteis | > 15 dias úteis |
| Resolutividade | Não definida em lei | > 70% | < 50% |
| % Respostas Insatisfatórias | — | < 5% | > 10% |
| Nota de Recomendação (0-10) | — | ≥ 7,5 | < 6,0 |

> Esses valores são referências para calibração das metas — não substitutos das metas institucionais já definidas na Matriz. O alinhamento com a realidade do órgão e com seus objetivos estratégicos tem precedência.

---

## Recomendações para Uso do Benchmarking no IGRO

1. **Não usar benchmarking externo para definir pesos** — os pesos do IGRO devem refletir as prioridades institucionais da ouvidoria, não médias externas
2. **Usar benchmarking para calibrar metas** — as metas de normalização por distância à meta (arquivo 02) devem ser validadas contra o panorama nacional
3. **Documentar a fonte de cada referência** — fundamental para auditabilidade do índice
4. **Revisão anual das referências** — o panorama de ouvidorias estaduais evolui; as metas de referência devem ser revisadas anualmente
5. **Análise de sensibilidade com diferentes metas** — testar (arquivo 05) como o IGRO se comportaria com metas mais conservadoras (padrão legal) e mais ambiciosas (melhores práticas)

---

## Fontes

### Sistema Nacional
- [Painel de Monitoramento de Ouvidorias — CGU/OGU](https://www.ouvidorias.gov.br/ouvidorias/monitoramento)
- [Relatórios Anuais das Ouvidorias — OGU](https://www.gov.br/ouvidorias/pt-br/ouvidorias/publicacoes)
- [Lei 13.460/2017 — Participação, Proteção e Defesa dos Direitos do Usuário](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13460.htm)
- [Decreto 9.492/2018 — Regulamento da Lei 13.460](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/D9492.htm)
- [Instrução Normativa CGU nº 8/2017](https://www.in.gov.br/web/dou/-/instrucao-normativa-n-8-de-19-de-setembro-de-2017)
- [OGU — Sistema e-Ouv: Manual do Gestor](https://www.gov.br/ouvidorias/pt-br/ouvidorias/e-ouv)
- [ANEOP — Associação Nacional dos Especialistas em Ouvidoria Pública](https://aneop.org.br)

### OGDF / SIGO-DF (pesquisa realizada em março 2026)
- [Painel de Ouvidoria do DF — CGDF](https://www.cg.df.gov.br/painel-de-ouvidoria-do-df)
- [Painel de Ouvidoria — OGDF](https://ouvidoria.df.gov.br/painel-de-ouvidoria/)
- [Legislações e Manuais — OGDF](https://ouvidoria.df.gov.br/manuais/)
- [Gestão de Riscos — CGDF](https://www.cg.df.gov.br/gestao-de-riscos/)
- [Novas diretrizes 2025 — OGDF](https://www.ouvidoria.df.gov.br/ouvidorias-do-df-se-reunem-para-alinhar-novas-diretrizes-de-atendimento-ao-cidadao/)
- [Concurso de Melhores Práticas (6ª edição) — OGDF](https://ouvidoria.df.gov.br/conhecam-na-integra-as-iniciativas-inscritas-no-concurso/)
- [Relatório 2º Trimestre 2024 — OGDF](https://ouvidoria.df.gov.br/ouvidoria-geral-do-df-divulga-relatorio-do-2o-trimestre-de-2024/)
