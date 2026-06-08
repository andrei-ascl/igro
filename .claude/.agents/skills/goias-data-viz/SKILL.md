---
name: goias-data-viz
description: Cria, revisa e orienta visualizacoes de dados com identidade visual do Governo de Goias/CGE-GO. Use sempre que o usuario pedir graficos, dashboards, relatorios gerenciais, layout de Power BI, Streamlit, Python/Matplotlib/Seaborn, escolha de tipos de grafico, paleta institucional, acessibilidade visual ou padronizacao de visualizacoes para projetos de Goias, CGE, ouvidoria, indicadores publicos ou gestao governamental.
---

# Goias Data Viz

Use esta skill para produzir visualizacoes institucionais claras, acessiveis e com cara de gestao publica profissional. A skill combina boas praticas de data visualization com a identidade visual do Governo de Goias e materiais de referencia curados em `referencias_estilo`.

## Quando Ativar

Ative quando a tarefa envolver:

- Criar ou revisar graficos em Python, Seaborn, Matplotlib, Streamlit ou Power BI.
- Escolher tipo de grafico para ranking, serie temporal, meta, composicao, distribuicao ou correlacao.
- Aplicar paleta, tipografia, cabecalho, rodape ou barra institucional de Goias/CGE-GO.
- Melhorar dashboard ou relatorio gerencial para leitura executiva.
- Validar acessibilidade, contraste, excesso de cores, rotulos, unidades e hierarquia visual.
- Transformar dados de ouvidoria, gestao publica, indicadores ou rankings municipais em visualizacao pronta para publicacao.

## Recursos

Leia recursos adicionais somente quando forem relevantes:

- `scripts/goias_seaborn_style.py`: utilitario principal para temas, cores, cabecalho, rodape, formatacao monetaria/percentual e rotulos.
- `references/fontes_estilo.md`: resumo das fontes de estilo usadas nesta revisao e caminhos para os guias completos.
- `evals/evals.json`: prompts de teste para verificar se a skill produz saidas no padrao esperado.

## Fluxo de Trabalho

1. Entenda o objetivo decisorio: o leitor precisa comparar, acompanhar tendencia, detectar excecao, ver composicao ou prestar contas?
2. Escolha o grafico pelo relacionamento dos dados, nao pela estetica.
3. Aplique a identidade Goias com paleta controlada, hierarquia clara e elementos institucionais quando o material for formal.
4. Reduza carga cognitiva: priorize 3 a 5 elementos em sumarios executivos e 7 a 9 em paineis de acompanhamento.
5. Valide acessibilidade: contraste, unidades, rotulos, legibilidade, segunda pista visual alem da cor e ausencia de 3D.
6. Entregue codigo ou recomendacao com proximos passos concretos, incluindo onde salvar/exportar quando fizer sentido.

## Escolha de Grafico

| Objetivo | Grafico recomendado | Observacoes |
|---|---|---|
| Tendencia no tempo | Linha | Use linha de meta em `LARANJA` e serie principal em `TEAL`. |
| Ranking | Barras horizontais | Ordene do menor para o maior e destaque o primeiro colocado. |
| Comparacao simples | Barras verticais | Comece no zero e use rotulos quando houver poucas categorias. |
| Meta vs realizado | Linha com meta ou bullet chart | Evite gauge salvo para KPI unico muito executivo. |
| Composicao | Barras empilhadas | Prefira 100% empilhado quando o foco for proporcao. |
| Distribuicao | Histograma ou boxplot | Use boxplot para comparar grupos. |
| Correlacao | Dispersao | Adicione anotacao apenas para outliers ou grupos importantes. |
| Muitos indicadores | Small multiples | Mantenha mesma escala quando a comparacao for direta. |

Evite 3D. Use pizza ou rosca apenas com poucas categorias e quando a leitura aproximada for suficiente.

## Identidade Visual Goias/CGE

Paleta base:

- `VERDE`: `#1fa22e` para desempenho positivo ou destaque institucional.
- `AZUL`: `#00519e` para serie secundaria, contexto ou comparacao.
- `AMARELO`: `#ffdd00` apenas como acento institucional, nunca como texto em fundo claro.
- `VERDE_ESCURO`: `#054222` para fundo premium e cabecalhos institucionais.
- `TEAL_ESCURO`: `#004f4b` para titulos e texto de alto contraste.
- `TEAL`: `#00766f` para serie principal de dados.
- `LARANJA`: `#f7931e` para metas, alertas e excecoes.
- `AMARELO_QUENTE`: `#fbb03b` para highlights visuais, nao para texto.
- `CINZA_TEXTO`: `#4a4a4a` para labels e corpo.
- `FUNDO`: `#f9f9f9` para areas neutras.

Padrao de uso:

- Use `TEAL` como cor principal de dados.
- Use `LARANJA` para meta, atencao ou desvio.
- Use `VERDE` para resultado positivo, meta atingida ou top performer.
- Use `AZUL` para comparacao historica ou serie secundaria.
- Distribua cores no espirito 60-30-10: neutros dominam, cores frias sustentam, acentos aparecem pouco.

## Python e Seaborn

Sempre que gerar codigo Python, comece aplicando o tema:

```python
import matplotlib.pyplot as plt
import seaborn as sns
from goias_seaborn_style import (
    apply_goias_theme,
    CORES,
    PALETAS,
    adicionar_cabecalho,
    adicionar_barra_institucional,
    adicionar_rodape,
    formatar_eixo_brl,
    formatar_eixo_pct,
    rotular_barras,
)

apply_goias_theme(context="paper", font_scale=1.0)
```

Use os helpers quando couber:

- `adicionar_cabecalho(ax, titulo, subtitulo, fonte)` para contexto e fonte.
- `adicionar_barra_institucional(fig)` para relatorios formais.
- `adicionar_rodape(fig)` para acabamento institucional.
- `formatar_eixo_brl(ax, eixo="y")` para valores monetarios.
- `formatar_eixo_pct(ax, eixo="y", casas=0)` para percentuais.
- `rotular_barras(ax, fmt="{:.1f}%")` para barras com poucos pontos.

## Padroes de Codigo

Ranking horizontal:

```python
dados = dados.sort_values("valor")
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(dados["categoria"], dados["valor"], color=CORES.TEAL, height=0.6)
bars[-1].set_color(CORES.VERDE)

formatar_eixo_brl(ax, "x")
adicionar_cabecalho(
    ax,
    titulo="Ranking de Investimentos",
    subtitulo="Cinco maiores municipios - 2024",
    fonte="Fonte: base analitica do projeto",
)
adicionar_barra_institucional(fig)
adicionar_rodape(fig)
plt.tight_layout()
```

Serie temporal com meta:

```python
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["mes"], df["realizado"], color=CORES.TEAL, marker="o", label="Realizado")
ax.plot(df["mes"], df["meta"], color=CORES.LARANJA, linestyle="--", label="Meta")
ax.fill_between(
    df["mes"],
    df["realizado"],
    df["meta"],
    where=df["realizado"] >= df["meta"],
    color=CORES.TEAL,
    alpha=0.12,
)

formatar_eixo_brl(ax, "y")
adicionar_cabecalho(ax, "Evolucao Mensal", "Realizado vs. meta")
adicionar_barra_institucional(fig)
adicionar_rodape(fig)
```

## Acessibilidade

Antes de finalizar, confira:

- Texto normal com contraste minimo WCAG AA (`4.5:1`).
- `AMARELO` e `AMARELO_QUENTE` nao usados como texto em fundo claro.
- Cor nunca e a unica pista: adicione rotulo, simbolo, linha, marcador ou anotacao.
- Barras sempre partem do zero.
- Eixos mostram unidade (`R$`, `%`, quantidade, dias, pontos).
- Rotulos longos ficam legiveis; prefira barras horizontais para muitas categorias.
- Paleta categorica tem no maximo 5 cores principais.
- Grafico tem titulo, subtitulo ou fonte suficiente para ser entendido fora do notebook.

## Power BI e Dashboards

Para layouts Power BI ou dashboards:

- Use fundo premium `#054222` quando o painel tiver carater executivo ou publico.
- Use cards brancos ou cinza claro sobre fundo escuro, com numeros em `TEAL` ou `TEAL_ESCURO`.
- Agrupe indicadores relacionados por proximidade e alinhamento.
- Coloque o KPI mais importante no topo ou na area de maior atencao.
- Evite excesso de visuais: dashboards executivos devem caber em leitura de poucos segundos.
- Reserve `LARANJA` para excecoes, metas e itens que precisam de acao.
- Inclua fonte, data de atualizacao e responsavel quando o material for publicavel.

## Forma de Resposta

Quando o usuario pedir um grafico:

- Entregue codigo completo e executavel quando houver dados ou estrutura suficiente.
- Explique em 2 a 4 frases por que aquele grafico foi escolhido.
- Cite as escolhas de cor e acessibilidade mais importantes.
- Quando faltar dado essencial, faca uma pergunta curta ou assuma uma estrutura de exemplo claramente marcada.

Quando o usuario pedir revisao:

- Liste primeiro os problemas encontrados, priorizados por impacto.
- Diga qual regra de identidade, UX ou acessibilidade esta sendo violada.
- Sugira a cor, grafico, layout ou helper correto.

## Criterios de Qualidade

Uma boa saida desta skill deve:

- Parecer institucional sem ficar burocratica.
- Deixar claro o que o leitor precisa decidir.
- Usar poucas cores, com significado consistente.
- Ter escala, rotulos, fonte e unidade.
- Ser reproduzivel em Python/Streamlit ou traduzivel para Power BI.
- Respeitar a identidade Goias/CGE sem sacrificar legibilidade.
