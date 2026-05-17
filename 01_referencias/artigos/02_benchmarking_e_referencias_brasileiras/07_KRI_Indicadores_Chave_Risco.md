# Indicadores-Chave de Risco (KRIs) e Índices de Risco Composto

## O que são KRIs?

Key Risk Indicators (KRIs) são métricas utilizadas por organizações para fornecer sinais antecipados de exposição crescente a riscos em diversas áreas. Diferem de KPIs (Key Performance Indicators): enquanto KPIs medem "quão bem algo está sendo feito", KRIs indicam "a possibilidade de impacto adverso futuro."

No contexto da Matriz de Gestão de Riscos da ouvidoria, os indicadores apresentados funcionam como KRIs — sinalizam se os riscos de atendimento fora do prazo (0044) e baixa qualidade (0046) estão se materializando.

---

## Agregação de KRIs em Índice Composto de Risco

### Abordagem Top-Down vs Bottom-Up

- **Top-down:** Facilita a agregação e o entendimento pela alta administração. Define-se primeiro o que o índice deve medir e depois selecionam-se indicadores.
- **Bottom-up:** Garante que gestores das unidades possam selecionar e monitorar os indicadores mais relevantes para sua situação particular.

Na prática, a agregação deve funcionar em diferentes níveis hierárquicos, resultando em uma métrica compreensível e significativa no nível relevante de gestão.

---

## Composite Risk Index (CRI) — Exemplo da Aviação

A EUROCONTROL utiliza um Composite Risk Index para aviação europeia que serve como referência metodológica:

**Características:**
- Agrega indicadores de diferentes tipos de risco
- Usa ponderação por severidade e probabilidade
- Atualizado periodicamente
- Permite comparação entre países e ao longo do tempo

---

## Taxonomia de Risco Padronizada

Para garantir qualidade e integridade dos dados na agregação de KRIs em um índice composto, é fundamental ter uma **taxonomia de risco padronizada** em toda a organização. Uma taxonomia comum facilita:
- Entendimento consistente dos riscos
- Harmonização dos dados na agregação
- Análise comparativa entre unidades e períodos

---

## Governança e Validação

Para boa governança de um programa de indicadores de risco:
- Uma **validação independente** do processo de seleção de indicadores deve ser realizada
- Isso inclui a forma como os dados são coletados, agregados e entregues à gestão
- A validação deve ocorrer razoavelmente cedo no ciclo de vida do programa

---

## Aplicação à Matriz de Gestão de Riscos

### Estrutura proposta como Índice de Risco Composto:

```
ÍNDICE DE GESTÃO DE RISCOS DA OUVIDORIA (IGRO)
│
├── Sub-índice de TEMPESTIVIDADE (Risco 0044)
│   ├── KRI 1: % Manifestações > 30 dias
│   │   - Sinal: Verde (< meta), Amarelo (próximo meta), Vermelho (> meta)
│   └── KRI 2: Prazo Médio de Resposta (dias)
│       - Sinal: Verde (< meta), Amarelo (próximo meta), Vermelho (> meta)
│
└── Sub-índice de QUALIDADE (Risco 0046)
    ├── KRI 3: Resolutividade (%)
    │   - Sinal: Verde (> meta), Amarelo (próximo meta), Vermelho (< meta)
    ├── KRI 4: % Respostas Insatisfatórias
    │   - Sinal: Verde (< meta), Amarelo (próximo meta), Vermelho (> meta)
    └── KRI 5: Nota de Recomendação
        - Sinal: Verde (> meta), Amarelo (próximo meta), Vermelho (< meta)
```

### Semaforização do Índice

O índice final pode ser traduzido em faixas de risco:

| Faixa do IGRO | Classificação | Ação |
|---------------|---------------|------|
| 0,80 - 1,00 | Risco Baixo (Verde) | Monitoramento rotineiro |
| 0,60 - 0,79 | Risco Moderado (Amarelo) | Atenção e plano de ação |
| 0,40 - 0,59 | Risco Alto (Laranja) | Intervenção necessária |
| 0,00 - 0,39 | Risco Crítico (Vermelho) | Ação imediata |

---

## Fontes

- [Institute of Operational Risk — KRI Guidance](https://www.ior-institute.org/public/IORKRIGuidanceNov2010.pdf)
- [EUROCONTROL — Composite Risk Index Methodology](https://ansperformance.eu/methodology/cri-pi/)
- [MetricStream — Key Risk Indicators in ERM](https://www.metricstream.com/insights/Key-Risk-indicators-ERM.htm)
- [AuditBoard — How to Develop KRIs](https://auditboard.com/blog/how-to-develop-key-risk-indicators-kris-to-fortify-business)
