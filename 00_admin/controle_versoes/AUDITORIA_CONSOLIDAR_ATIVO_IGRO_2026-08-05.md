---
title: "Auditoria de consolidação do ativo IGRO"
date: 2026-08-05
project: igro
mode: auditar
status: staging
source: "Skill consolidar-ativo — auditoria documental e técnica do projeto IGRO"
---

# Auditoria de consolidação do ativo IGRO

## Escopo

Auditoria realizada em 2026-08-05 sobre o repositório `igro`, sem alterações
prévias nos arquivos. O objetivo foi identificar o ativo principal, avaliar sua
permanência e propor derivados para `vault`, `skill`, `template` ou `projeto`.

## Ativo principal

**IGRO — método composto para monitoramento de riscos em redes de ouvidorias
públicas.**

O ativo combina seleção de cinco KRIs, normalização por metas/goalposts,
agregação, semaforização, análise de sensibilidade e ciclo de governança
quadrimestral. Seu valor está em transformar dados operacionais do SGOe em um
sinal sintético, auditável e acionável para gestão de riscos.

### Classificação

- Tipo: método/framework e especificação operacional.
- Destino primário: projeto, como fonte canônica.
- Destino secundário: vault, atualizando notas existentes.
- Permanência: **staging**.

O ativo não deve ser promovido como método único enquanto houver divergência
entre a implementação PBIP, o Desenho Técnico e a variante usada no artigo.

## Evidências positivas

- Desenho metodológico explícito em `00_admin/planejamento/03_especificacao_e_produto/10_Desenho_IGRO.md`.
- PRD, artigo, análise de sensibilidade e pacote executivo disponíveis.
- Projeto PBIP com TMDL, documentação semântica, medidas DAX e review técnico.
- Dados brutos Parquet preservados em `02_dados/raw/`.
- Nota de IGRO já existente no `second_brain`, com backlinks orgânicos.

## Achados que impedem a promoção imediata

1. Há três perfis metodológicos: PBIP ativo; Desenho Técnico/documentação; e
   artigo/sensibilidade com pesos uniformes.
2. O Desenho Técnico restringe a interpretação à comparação longitudinal,
   enquanto artigo e resumo executivo defendem ranking e benchmarking entre
   órgãos.
3. O universo geral é de 51 órgãos, mas a análise de sensibilidade usa 47 com
   dados completos.
4. `flag_amostra` é exportada, mas não bloqueia diretamente o cálculo de
   `idx_igro`; resultados com poucos respondentes podem ser extremos.
5. O dicionário de dados está praticamente vazio, o README de dados descreve
   uma estrutura diferente da existente e arquivos `.csv` processados contêm
   HTML/JavaScript de dashboard.
6. Existem resultados consolidados diferentes entre versões, decorrentes de
   períodos e parametrizações não reconciliados.

## Artefatos derivados propostos

| Artefato | Destino | Classificação | Situação |
|---|---|---|---|
| Registro da decisão canônica | Projeto | Staging | Criado após esta auditoria |
| Contrato de métricas e proveniência | Projeto | Staging | Criado após esta auditoria |
| Método de índice composto orientado a risco | Vault | Staging | Atualizar nota existente; não criar duplicata |
| Guardrail de confiabilidade amostral | Vault | Permanente candidato | Integrar à metodologia já existente |
| Nota técnica de sensibilidade | Template | Permanente candidato | Estrutura reutilizável para outros índices |
| Briefing executivo de índice de risco | Template | Permanente candidato | Derivado do resumo executivo do IGRO |
| Checklist de auditoria de índice composto | Skill | Staging/deferido | Só após segunda aplicação; evitar duplicação de skills existentes |
| Contrato de handoff Power BI/DAX | Projeto | Específico | Deve permanecer específico ao IGRO |

## Dedupe e integração

O vault já possui `igro-indice-desempenho-ouvidorias.md`, além de notas sobre
índices compostos, gestão de riscos, amostragem e Goodhart. A recomendação é
atualizar e deduplicar essas notas, preservando backlinks, em vez de criar uma
nova página de IGRO.

As skills locais `pbi-modelo-review`, `pbi-doc` e `pbi-dax-create` já cobrem os
fluxos Power BI próximos. Não há justificativa para criar uma skill IGRO nova
nesta etapa.

## Quality gate

- [x] Problema de uso explícito.
- [x] Usuários e saída esperada identificados.
- [x] Fontes do projeto e evidências principais localizadas.
- [ ] Variante metodológica canônica definida.
- [ ] Regra amostral incorporada ao cálculo ou formalmente tratada como alerta.
- [ ] Período, universo e comparabilidade reconciliados.
- [ ] Contrato de dados preenchido e reproduzível.
- [ ] Vault atualizado sem duplicação.

## Próxima ação registrada

Criar e manter no projeto um registro de decisão canônica e um contrato de
métricas/proveniência antes de atualizar o vault ou promover qualquer skill.
