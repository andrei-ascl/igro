# PRD Interno — IGRO: Índice de Gestão de Riscos da Ouvidoria

> Documento interno de planejamento da implementação.
> Versão 1.0 — Abril/2026
> Proprietário: Andrei Lima (CGE-GO / OGE)
>
> **O que este documento NÃO é:** não é especificação metodológica — essa já está em `10_Desenho_IGRO.md`. Este PRD responde: *o que construir, para quem, como, e o que precisa estar resolvido antes.*

---

## 1. Problema

A Matriz de Gestão de Riscos da Ouvidoria (CGE-GO) monitora os Riscos **0044** (atendimento fora do prazo) e **0046** (baixa qualidade no atendimento) com avaliação de efetividade dos controles marcada como **"Controle Fraco"**. O ciclo quadrimestral de revisão ocorre, mas o registro atual dos KRIs é manual e não está consolidado em um único número que sinalize o nível de materialização de ambos os riscos.

**Três evidências do problema:**

1. **Risco 0044/0046 — controle fraco:** A Matriz registra a avaliação de efetividade como fraca — sinal de que os mecanismos de monitoramento não são suficientes para detectar deterioração antes que ela se materialize.

2. **Dúvida não respondida na Oficina de Prototipação** (SEAD/Pequi Lab, jun/2023, 29 participantes): *"O relatório gerencial deve conter informações monitoradas nos riscos?"* — a oficina não chegou a consenso. O IGRO é a resposta direta a essa lacuna: permite integrar o monitoramento de riscos ao relatório gerencial quadrimestral.

3. **Ausência de sinalização sintética:** Os 5 KRIs são calculados individualmente (quando calculados). Não há um único indicador que responda *"qual é o nível de risco operacional da ouvidoria neste quadrimestre?"* — o que dificulta a comunicação com a alta gestão e com o Comitê Setorial.

---

## 2. Usuários e casos de uso

| Usuário | Papel | Caso de uso principal |
|---------|-------|-----------------------|
| **Proprietário do risco** (Andrei Lima) | Coleta os KRIs, calcula o IGRO, produz o relatório quadrimestral | Calcular o IGRO a partir dos dados do SGOe, identificar qual KRI está deteriorando e propor ação |
| **Escritório de Compliance / GT Riscos** | Analisa a Matriz e avalia efetividade dos controles | Receber o IGRO com a semaforização e os sub-índices desagregados; usar como insumo para a reunião quadrimestral de revisão da Matriz |
| **Alta gestão / Comitê Setorial** | Aprova a Matriz; recebe alertas de risco | Ver o semáforo do IGRO no cabeçalho do relatório gerencial; acionar ação imediata quando Laranja ou Vermelho |

**O que cada usuário NÃO precisa:**
- Proprietário: não precisa de dashboard em tempo real — o ciclo é quadrimestral
- Compliance: não precisa de acesso ao sistema de cálculo — só precisa do output (IGRO + sub-índices + semaforização)
- Alta gestão: não precisa ver os 5 KRIs individuais na primeira tela — só o semáforo e o destaque do KRI mais problemático

---

## 3. MVP: o que construir primeiro

### Decisão: Excel-first, caminho para Power BI

**O MVP é uma planilha Excel estruturada**, não um dashboard Power BI.

| Critério | Excel (MVP) | Power BI |
|----------|------------|----------|
| Dependência de infraestrutura | Nenhuma | Pipeline de dados SGOe → Power BI |
| Auditabilidade | Fórmulas visíveis, rastreáveis | Depende de documentação externa das medidas DAX |
| Aprovação pelo Comitê | Mais fácil — todos têm acesso ao Excel | Requer acesso ao workspace ou exportação |
| Esforço inicial | Baixo (1–2 dias) | Alto (semanas, incluindo pipeline) |
| Escalabilidade | Baixa — manual por quadrimestre | Alta — automatizável com refresh |
| Compartilhamento com GT Riscos | Simples | Requer publicação ou compartilhamento de link |

**Conclusão:** Excel no MVP garante que o IGRO seja calculado e validado no primeiro ciclo quadrimestral sem depender da infraestrutura de dados. A migração para Power BI acontece após validação pelo Comitê Setorial.

### Escopo do MVP (Excel)

- **Aba `KRIs`:** entrada manual dos 5 KRIs com fonte e data de extração
- **Aba `Cálculo`:** normalização (fórmulas de Distância à Meta com goalposts), sub-índices, IGRO — todas as fórmulas expostas e documentadas
- **Aba `Dashboard`:** semáforo do IGRO + sub-índices + destaque do KRI mais baixo + série histórica (começa vazia, acumula por quadrimestre)
- **Aba `Decisões`:** tabela com goalposts, metas, pesos e justificativas — congelada após aprovação do Comitê

> **Fora do escopo do MVP:** integração automática com SGOe, análise de robustez (Monte Carlo), comparação entre órgãos, push para Power BI. Essas funcionalidades entram na Fase 2.

---

## 4. Pipeline de dados: SGOe → KRIs

Para cada KRI, a fonte de dados no SGOe e a lógica de extração:

### KRI 1 — % Manifestações com mais de 30 dias sem resposta conclusiva

**Endpoint:** `/api/relatorios/relatorio-manifestacoes`

```
# Manifestações abertas (status=1) no final do quadrimestre, por data de cadastro
/relatorio-manifestacoes?
  idsOrgaos={codigo_orgao}
  &classificada=1
  &status=1
  &data_inicial={inicio_quadrimestre}
  &data_final={data_extracao}
  &gerar_excel=bi
```

**Cálculo:** filtrar linhas onde `(data_extracao - data_cadastro) > 30 dias` → dividir pelo total de abertas no período.

> **Atenção:** este KRI depende de uma extração na data exata do encerramento do quadrimestre. Extrações tardias subestimam o indicador (algumas manifestações terão sido respondidas).

---

### KRI 2 — Prazo Médio de Resposta (PMR)

**Endpoint:** `/api/relatorios/relatorio-manifestacoes`

```
# Manifestações finalizadas (status=3) no quadrimestre
/relatorio-manifestacoes?
  idsOrgaos={codigo_orgao}
  &classificada=2
  &status=3
  &data_inicial={inicio_quadrimestre}
  &data_final={fim_quadrimestre}
  &gerar_excel=bi
```

**Cálculo:** `MÉDIA(data_finalização - data_cadastro)` em dias corridos para todas as linhas retornadas.

> **Decisão pendente:** incluir ou excluir manifestações com complementação (trâmite 3/4) do cálculo do PMR? A complementação suspende o prazo oficial, mas pode distorcer o PMR percebido. Verificar com o GT Riscos.

---

### KRI 3 — Resolutividade

**Endpoint:** `/api/relatorios/relatorio-manifestacoes`

```
# Manifestações finalizadas no quadrimestre com coluna de resolutividade
/relatorio-manifestacoes?
  idsOrgaos={codigo_orgao}
  &classificada=2
  &status=3
  &data_inicial={inicio_quadrimestre}
  &data_final={fim_quadrimestre}
  &gerar_excel=bi
```

**Cálculo (fórmula do Prêmio das Ouvidorias):**
```
Resolutividade = (0,5 × Parcial + Sim) / Total × 100
```

Onde `Sim`, `Parcial` e `Não` são os valores da coluna de avaliação de resolutividade no retorno do SGOe.

> **Bloqueio identificado:** verificar se o campo de resolutividade no retorno da API corresponde à **avaliação do cidadão** (via pesquisa de satisfação) ou ao **julgamento do ouvidor**. Definições diferentes produzem valores incomparáveis ao longo do tempo. Ver limitação nº 1 em `10_Desenho_IGRO.md`.

---

### KRI 4 — % Respostas Insatisfatórias

**Endpoint:** `/api/relatorios/relatorio-manifestacoes`

```
# Manifestações que passaram pelo trâmite 12 (Resposta Insatisfatória) em qualquer ponto
/relatorio-manifestacoes?
  idsOrgaos={codigo_orgao}
  &condicao_tramite_contem=IN
  &id_tipo_tramite_contem=12
  &classificada=2
  &data_inicial={inicio_quadrimestre}
  &data_final={fim_quadrimestre}
  &gerar_excel=bi
```

**Cálculo:** `COUNT(linhas retornadas) / COUNT(total manifestações finalizadas no período) × 100`

> **Nota:** o parâmetro `id_tipo_tramite_contem=12` captura manifestações cujo cidadão reabrirá a manifestação (trâmite 12 = Resposta Insatisfatória). É diferente de perguntar "o cidadão ficou insatisfeito na pesquisa" — é um ato explícito de rejeição da resposta.

---

### KRI 5 — Nota de Recomendação

**Endpoint:** `/api/relatorios/relatorio-pesquisa`

```
# Pesquisas respondidas no quadrimestre
/relatorio-pesquisa?
  idsOrgaos={codigo_orgao}
  &data_inicial_resp={inicio_quadrimestre}
  &data_final_resp={fim_quadrimestre}
  &gerar_excel=bi
```

**Cálculo:** média da coluna correspondente à pergunta "Você recomendaria esta Ouvidoria?" (escala 1–10) em todas as linhas retornadas.

> **Nota:** excluir manifestações anônimas do denominador (não recebem pesquisa de satisfação) — consistente com a fórmula PR do Prêmio das Ouvidorias.

---

### Resumo do pipeline

| KRI | Endpoint | Parâmetro-chave | Campo de cálculo |
|-----|----------|-----------------|------------------|
| KRI 1 — % > 30 dias | manifestacoes | `status=1`, data de extração | dias desde cadastro > 30 |
| KRI 2 — PMR | manifestacoes | `status=3`, `classificada=2` | média de (data_final - data_cadastro) |
| KRI 3 — Resolutividade | manifestacoes | `status=3`, `classificada=2` | coluna resolutividade (Sim/Parcial/Não) |
| KRI 4 — % Insatisfatórias | manifestacoes | `id_tipo_tramite_contem=12` | contagem / total finalizadas |
| KRI 5 — Nota Recomendação | pesquisa | `data_inicial_resp` / `data_final_resp` | média da nota de recomendação |

---

## 5. Dependências bloqueantes

Estas questões precisam ser resolvidas **antes** de calcular o IGRO pela primeira vez. Cada uma pode mudar os valores — resolver depois é mais caro.

| # | Dependência | Impacto | Responsável | Status |
|---|------------|---------|------------|--------|
| D1 | **Definição de resolutividade:** avaliação do cidadão ou do ouvidor? | Muda o valor do KRI 3 — pode variar em 20–30 pp | GT Riscos / Gerência CGE | ⬜ Pendente |
| D2 | **Validação das metas pela Matriz:** as metas do arquivo 10 são as metas oficiais? | Muda todos os scores normalizados | Proprietário do risco + GT Riscos | ⬜ Pendente |
| D3 | **Código do órgão no SGOe (`idsOrgaos`):** qual o código correto para extração dos dados da OGE? | Bloqueia qualquer extração via API | Gerência de Ouvidoria da CGE | ⬜ Pendente |
| D4 | **Período de referência:** o quadrimestre é jan–abr / mai–ago / set–dez? Ou outro calendário? | Define `data_inicial` / `data_final` de todos os endpoints | Escritório de Compliance | ⬜ Pendente |
| D5 | **Aprovação do Comitê Setorial** para incluir o IGRO formalmente na Matriz | Sem aprovação, o IGRO é instrumento interno sem peso oficial | Proprietário do risco | ⬜ Pendente — pós-validação |

> D1, D2, D3 e D4 bloqueiam o cálculo do MVP. D5 não bloqueia o cálculo, mas bloqueia a integração oficial à Matriz.

---

## 6. Critérios de aceitação — primeiro ciclo quadrimestral

O MVP é considerado aceito quando:

- [ ] Os 5 KRIs foram extraídos do SGOe para o período do quadrimestre corrente, com fonte e data registradas na aba `KRIs`
- [ ] O IGRO e os sub-índices foram calculados com as fórmulas de `10_Desenho_IGRO.md`, sem adaptações não documentadas
- [ ] A semaforização (Verde/Amarelo/Laranja/Vermelho) está visível e corresponde às faixas do documento técnico
- [ ] O KRI com menor score está destacado no Dashboard com a leitura em linguagem natural (ex: "KRI 3 — Resolutividade em 0,65 [Amarelo]: 56% vs. meta de 70%")
- [ ] A planilha foi apresentada ao GT Riscos ou Escritório de Compliance e nenhuma dependência bloqueante (D1–D4) ficou por resolver
- [ ] A análise de robustez (4 cenários de pesos) foi executada e o resultado está registrado na aba `Decisões`

---

## 7. Fases após o MVP

| Fase | O que entrega | Gatilho |
|------|--------------|---------|
| **MVP** (atual) | Planilha Excel com cálculo manual, semaforização e série histórica vazia | Resolver D1–D4 |
| **Fase 2** | Script Python para extração automática dos 5 KRIs via API SGOe | IGRO validado pelo GT Riscos após 1º ciclo |
| **Fase 3** | Página Power BI com o IGRO integrado ao relatório gerencial quadrimestral | Script Python funcionando; aprovação Comitê (D5) |
| **Fase 4** | Análise de robustez Monte Carlo (N ≥ 500) e revisão dos goalposts com série histórica real | 4–6 quadrimestres calculados |

---

## 8. Referências

- `10_Desenho_IGRO.md` — especificação técnica completa: fórmulas, goalposts, pesos, agregação, exemplo numérico, análise de robustez
- `../02_benchmarking_e_referencias_brasileiras/09_Benchmarking_KRIs_Ouvidorias_Estaduais.md` — origem das metas de referência e dos goalposts
- `02_wiki/conceitos/sgoe-sistema.md` — documentação da API SGOe (endpoints, parâmetros, exemplos)
- `02_wiki/conceitos/relatorio-gestao-ouvidoria.md` — Oficina Pequi Lab/SEAD (validação qualitativa dos KRIs; dúvida sobre riscos no relatório)
- `02_wiki/conceitos/gestao-riscos-ouvidoria.md` — Matriz de Gestão de Riscos, Riscos 0044/0046, ações A01xx
