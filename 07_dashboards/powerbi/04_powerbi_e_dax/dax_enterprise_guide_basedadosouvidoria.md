# Nível Enterprise Completo — Governança de Medidas DAX

> Guia prático para manter o modelo `BaseDadosOuvidoria` em padrão corporativo.

## 1. Arquitetura recomendada de camadas

### 1.1 Camadas semânticas
- `camada_base`: contagens, médias atômicas e bases elegíveis
- `camada_indicadores`: percentuais e métricas derivadas
- `camada_tempo`: inteligência temporal
- `camada_ranking`: ranking e top N
- `camada_indices`: índices compostos, scores, metas e pesos
- `camada_auxiliares`: títulos, labels e helpers de exibição
- `camada_formatacao`: semáforos, hexadecimais e labels de formatação condicional

### 1.2 Regra de dependência
Uma camada só pode depender da própria camada ou de camadas anteriores.

```text
base -> indicadores -> tempo/ranking -> indices -> auxiliares/formatacao
```

## 2. Convenção de nomes

### 2.1 Prefixos
- `base_` = contagens, médias-base e denominadores comuns
- `ind_` = indicadores percentuais e derivados
- `tempo_` = time intelligence
- `rank_` = ranking, top N e exibição por posição
- `idx_` = score e índice composto
- `meta_` = metas fixas
- `goal_` = goalposts
- `peso_` = pesos do índice
- `aux_` = helpers textuais
- `fmt_` = saída para formatação condicional

### 2.2 Regras gerais
- usar apenas `snake_case`
- sem acentos no nome da medida
- sem `%`, `#`, `-`, `/`, espaços
- nomes curtos, mas semanticamente claros
- evitar aliases desnecessários
- uma medida, uma responsabilidade

## 3. Padrões de escrita DAX

### 3.1 Template obrigatório
```dax
nome_da_medida =
VAR valor_1 = ...
VAR valor_2 = ...
VAR resultado = ...
RETURN
    resultado
```

### 3.2 Regras
- usar `VAR/RETURN` sempre que houver 2 ou mais componentes
- usar `DIVIDE` em vez de `/`
- usar `COALESCE` para retornos numéricos quando zero for desejado
- usar `KEEPFILTERS` quando o filtro da medida deve compor com o contexto
- qualificar colunas sempre como `'Tabela'[Coluna]`
- medidas sempre como `[medida]`

## 4. Anti-patterns a evitar

### 4.1 Evitar
```dax
COUNTROWS ( FILTER ( fRelatorio, fRelatorio[Dias_vida] > 30 ) )
```

### 4.2 Preferir
```dax
CALCULATE (
    COUNTROWS ( fRelatorio ),
    KEEPFILTERS ( fRelatorio[Dias_vida] > 30 )
)
```

### 4.3 Evitar
```dax
resultado + 0
```

### 4.4 Preferir
```dax
COALESCE ( resultado, 0 )
```

### 4.5 Evitar
- repetir denominadores complexos em várias medidas
- misturar escalas distintas em índice composto sem normalização
- usar nomes diferentes para a mesma métrica em tabelas diferentes sem necessidade

## 5. Catálogo corporativo de medidas

### 5.1 Medidas base essenciais
- `base_qtd_manifestacoes`
- `base_qtd_manifestacoes_em_aberto`
- `base_qtd_manifestacoes_finalizadas`
- `base_qtd_manifestacao_inativada`
- `base_qtd_lai`
- `base_qtd_comunicacao`
- `base_qtd_pesquisa`
- `base_qtd_sim`
- `base_qtd_parcialmente`
- `base_qtd_resolvidas`
- `base_manifestacoes_elegiveis`

### 5.2 Indicadores essenciais
- `ind_media_tempo_resposta`
- `ind_media_nota_recomendacao`
- `ind_pct_mais_30_dias`
- `ind_pct_resolutividade`
- `ind_pct_pesquisas_respondidas`
- `ind_pct_respostas_insatisfatorias`
- `ind_pct_manifestacao_inativada`

### 5.3 Índices
- `idx_iqo`
- `idx_igro`
- `idx_igro_sub_t`
- `idx_igro_sub_q`

## 6. Padrão de pastas no Tabular Editor

```text
Medidas
├── camada_base
├── camada_indicadores
├── camada_tempo
├── camada_ranking
├── camada_indices
├── camada_auxiliares
└── camada_formatacao
```

## 7. Formatos recomendados

- contagens: `#,0`
- médias: `0.0`
- percentuais: `0.0%;-0.0%;0.0%`
- scores: `0.000`
- índices: `0.000`
- texto: sem formato
- cores hex: sem formato

## 8. Padrão para comentários/descrições

### Exemplo
**Descrição da medida**
```text
Calcula o percentual de respostas insatisfatórias sobre a base elegível de manifestações finalizadas, excluindo LAI.
```

**Display Folder**
```text
camada_indicadores
```

**Format String**
```text
0.0%;-0.0%;0.0%
```

## 9. Checklist de revisão antes de publicar

- [ ] medida usa `snake_case`
- [ ] coluna está qualificada com tabela
- [ ] medida usa `DIVIDE` quando há divisão
- [ ] não há `+ 0`
- [ ] não há `FILTER(tabela inteira)` sem necessidade
- [ ] denominador reutilizável virou medida base
- [ ] nomes não duplicam conceitos
- [ ] formato está correto
- [ ] pasta está correta
- [ ] descrição da medida foi preenchida
- [ ] dependência respeita a ordem das camadas

## 10. Recomendação para o IQO

[Inferência] A fórmula original do IQO mistura variáveis em escalas heterogêneas. Em padrão enterprise, o recomendado é:
1. normalizar cada componente em escala comum
2. aplicar pesos após a normalização
3. documentar meta e goalpost de cada componente
4. validar a sensibilidade do índice por porte de órgão

## 11. Recomendação para ranking

- usar `DESC, DENSE` no `RANKX`
- garantir coerência entre nome e filtro, por exemplo `top_3` com `<= 3`
- separar medida agregada (`rank_top_3_assuntos`) da medida de exibição em matriz (`rank_exibir_top_3_assuntos`)

## 12. Próximo padrão ideal

Para maturidade máxima no modelo:
- descrições em todas as medidas
- BPA no Tabular Editor
- script de validação de nomes
- data dictionary das medidas
- convenção única de prefixos em todo o modelo
- controle de versão das medidas em `.md` ou `.tmdl`
