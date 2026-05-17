"""
=============================================================================
GUIA DE ESTILOS SEABORN — IDENTIDADE VISUAL GOVERNO DE GOIÁS
=============================================================================
Baseado no Manual de Marca Impresso 2022 do Governo do Estado de Goiás.

COMO USAR
---------
    from goias_seaborn_style import apply_goias_theme, CORES, PALETAS
    apply_goias_theme()                      # aplica o tema globalmente
    # ... crie seus gráficos normalmente com matplotlib/seaborn

CONTEÚDO
--------
    1. Tokens de cor (CORES, PALETAS)
    2. Tema Matplotlib/Seaborn  (apply_goias_theme)
    3. Funções auxiliares       (set_titulo, adicionar_rotulo, etc.)
    4. Gráficos de exemplo      (executar como __main__ gera preview.png)
=============================================================================
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import rcParams
from matplotlib.colors import LinearSegmentedColormap

# =============================================================================
# 1. TOKENS DE COR
# =============================================================================

class CORES:
    """
    Paleta oficial do Governo de Goiás — Manual de Marca 2022.

    Cores primárias (logo)
    ----------------------
    VERDE      #1fa22e   Verde bandeira (cor institucional principal)
    AZUL       #00519e   Azul bandeira
    AMARELO    #ffdd00   Amarelo bandeira

    Cores auxiliares — tons frios (recomendadas para gráficos de gestão)
    ---------------------------------------------------------------------
    TEAL_ESCURO   #004f4b
    TEAL          #00766f
    VERDE_ESCURO  #054222
    AZUL_ESCURO   #153274

    Cores auxiliares — tons quentes (destaques / alertas)
    -----------------------------------------------------
    LARANJA       #f7931e
    LARANJA_ESCO  #d56f24
    AMARELO_QUENTE #fbb03b

    Neutros
    -------
    BRANCO        #ffffff
    CINZA_TEXTO   #4a4a4a   (usado em corpo de texto no manual)
    CINZA_GRADE   #e5e5e5   (linhas de grade sutis)
    FUNDO         #f9f9f9   (fundo de área do gráfico)
    """

    # — Primárias (logo) —
    VERDE        = "#1fa22e"
    AZUL         = "#00519e"
    AMARELO      = "#ffdd00"

    # — Auxiliares frios —
    TEAL_ESCURO  = "#004f4b"
    TEAL         = "#00766f"
    VERDE_ESCURO = "#054222"
    AZUL_ESCURO  = "#153274"

    # — Auxiliares quentes —
    LARANJA_ESCURO  = "#d56f24"
    LARANJA         = "#f7931e"
    AMARELO_QUENTE  = "#fbb03b"

    # — Neutros —
    BRANCO      = "#ffffff"
    CINZA_TEXTO = "#4a4a4a"
    CINZA_GRADE = "#e5e5e5"
    FUNDO       = "#f9f9f9"

    # — Destaque / ênfase —
    ACENTO      = TEAL         # cor de acento recomendada para títulos e bordas


class PALETAS:
    """
    Conjuntos de cores prontos para uso em gráficos categóricos e sequenciais.

    Uso:
        ax.bar(x, y, color=PALETAS.FRIA)
        sns.barplot(..., palette=PALETAS.CATEGORICA)
    """

    # 6 cores para séries categóricas (até 6 categorias)
    CATEGORICA = [
        CORES.TEAL,
        CORES.AMARELO_QUENTE,
        CORES.AZUL,
        CORES.LARANJA,
        CORES.VERDE,
        CORES.AZUL_ESCURO,
    ]

    # 4 cores preferidas para relatórios de gestão (tom institucional)
    GESTAO = [
        CORES.TEAL,
        CORES.AZUL,
        CORES.AMARELO_QUENTE,
        CORES.VERDE,
    ]

    # Sequencial verde (magnitude única, ex.: execução orçamentária)
    SEQUENCIAL_VERDE = LinearSegmentedColormap.from_list(
        "goias_verde",
        [CORES.FUNDO, "#a8ddb0", CORES.VERDE, CORES.VERDE_ESCURO]
    )

    # Sequencial teal (alternativa fria para mapas de calor)
    SEQUENCIAL_TEAL = LinearSegmentedColormap.from_list(
        "goias_teal",
        [CORES.FUNDO, "#b2dfdb", CORES.TEAL, CORES.TEAL_ESCURO]
    )

    # Divergente (ex.: variação acima/abaixo da meta)
    DIVERGENTE = LinearSegmentedColormap.from_list(
        "goias_div",
        [CORES.LARANJA_ESCURO, CORES.AMARELO_QUENTE, CORES.FUNDO,
         CORES.TEAL, CORES.TEAL_ESCURO]
    )

    # Lista simples com as cores primárias da logo
    LOGO = [CORES.VERDE, CORES.AZUL, CORES.AMARELO]

    # Fria (tons frios em sequência)
    FRIA = [CORES.AZUL_ESCURO, CORES.AZUL, CORES.TEAL, CORES.TEAL_ESCURO]

    # Quente (tons quentes em sequência)
    QUENTE = [CORES.LARANJA_ESCURO, CORES.LARANJA, CORES.AMARELO_QUENTE, CORES.AMARELO]


# =============================================================================
# 2. TEMA MATPLOTLIB / SEABORN
# =============================================================================

def apply_goias_theme(
    font_scale: float = 1.0,
    context: str = "paper",       # "paper" | "notebook" | "talk" | "poster"
    dpi: int = 150,
    figsize: tuple = (10, 5.5),
):
    """
    Aplica o tema do Governo de Goiás globalmente ao matplotlib e seaborn.

    Parâmetros
    ----------
    font_scale : float
        Escala da fonte (1.0 = tamanho padrão; use 1.2 para slides).
    context : str
        Contexto seaborn: 'paper' para PDF/relatório, 'talk' para slides.
    dpi : int
        Resolução padrão das figuras.
    figsize : tuple
        Tamanho padrão (largura, altura) em polegadas.

    Exemplo
    -------
        apply_goias_theme(context="paper", figsize=(12, 6))
    """
    sns.set_theme(
        context=context,
        style="white",
        palette=PALETAS.CATEGORICA,
        font="DejaVu Sans",    # substituto open-source para BW Mitga
        font_scale=font_scale,
        rc={
            # — Figura —
            "figure.figsize"        : list(figsize),
            "figure.dpi"            : dpi,
            "figure.facecolor"      : CORES.BRANCO,
            "figure.edgecolor"      : CORES.BRANCO,

            # — Eixos —
            "axes.facecolor"        : CORES.FUNDO,
            "axes.edgecolor"        : CORES.CINZA_GRADE,
            "axes.linewidth"        : 0.8,
            "axes.labelcolor"       : CORES.CINZA_TEXTO,
            "axes.labelsize"        : 10 * font_scale,
            "axes.titlesize"        : 13 * font_scale,
            "axes.titleweight"      : "bold",
            "axes.titlecolor"       : CORES.TEAL_ESCURO,
            "axes.titlepad"         : 14,
            "axes.spines.top"       : False,
            "axes.spines.right"     : False,
            "axes.prop_cycle"       : plt.cycler(color=PALETAS.CATEGORICA),

            # — Grade —
            "axes.grid"             : True,
            "axes.grid.axis"        : "y",           # grade apenas horizontal
            "grid.color"            : CORES.CINZA_GRADE,
            "grid.linewidth"        : 0.7,
            "grid.linestyle"        : "--",
            "grid.alpha"            : 0.8,

            # — Texto —
            "text.color"            : CORES.CINZA_TEXTO,
            "font.family"           : ["DejaVu Sans", "sans-serif"],

            # — Ticks —
            "xtick.color"           : CORES.CINZA_TEXTO,
            "ytick.color"           : CORES.CINZA_TEXTO,
            "xtick.labelsize"       : 9 * font_scale,
            "ytick.labelsize"       : 9 * font_scale,
            "xtick.major.size"      : 0,
            "ytick.major.size"      : 0,

            # — Legenda —
            "legend.frameon"        : False,
            "legend.fontsize"       : 9 * font_scale,
            "legend.title_fontsize" : 10 * font_scale,
            "legend.labelcolor"     : CORES.CINZA_TEXTO,

            # — Linhas —
            "lines.linewidth"       : 2.0,
            "lines.markersize"      : 6,

            # — Patches (barras, áreas) —
            "patch.linewidth"       : 0,

            # — Exportação —
            "savefig.dpi"           : dpi,
            "savefig.bbox"          : "tight",
            "savefig.facecolor"     : CORES.BRANCO,
        }
    )


# =============================================================================
# 3. FUNÇÕES AUXILIARES
# =============================================================================

def adicionar_cabecalho(
    ax: plt.Axes,
    titulo: str,
    subtitulo: str = "",
    fonte: str = "",
) -> None:
    """
    Adiciona título, subtítulo e nota de fonte ao gráfico no estilo Goiás.

    Parâmetros
    ----------
    ax       : eixo matplotlib
    titulo   : texto principal (será em bold e cor teal escuro)
    subtitulo: texto secundário (menor, cinza)
    fonte    : nota de rodapé com a origem dos dados (ex: "Fonte: SEFAZ-GO, 2024")

    Exemplo
    -------
        adicionar_cabecalho(ax, "Receita Arrecadada", "Jan–Dez 2024",
                            "Fonte: SEFAZ-GO")
    """
    fig = ax.get_figure()

    ax.set_title(titulo, fontsize=13, fontweight="bold",
                 color=CORES.TEAL_ESCURO, pad=14, loc="left")

    if subtitulo:
        ax.annotate(
            subtitulo,
            xy=(0, 1.0), xycoords="axes fraction",
            fontsize=9, color=CORES.CINZA_TEXTO, va="bottom",
        )

    if fonte:
        fig.text(
            0.01, -0.06, fonte,
            fontsize=7.5, color="#888888", style="italic",
            ha="left", va="top",
            transform=ax.transAxes,
        )


def adicionar_barra_institucional(
    fig: plt.Figure,
    texto: str = "Governo do Estado de Goiás",
    cor_barra: str = CORES.TEAL_ESCURO,
    cor_acento: str = CORES.AMARELO,
    altura: float = 0.028,
) -> None:
    """
    Insere uma barra colorida no topo da figura, imitando o cabeçalho do manual.

    Parâmetros
    ----------
    fig        : figura matplotlib
    texto      : texto institucional exibido na barra
    cor_barra  : cor principal da barra (padrão: teal escuro)
    cor_acento : cor do bloco lateral (padrão: amarelo)
    altura     : fração da altura total da figura ocupada pela barra

    Exemplo
    -------
        fig, ax = plt.subplots()
        adicionar_barra_institucional(fig)
    """
    # Barra principal
    barra = fig.add_axes([0, 1 - altura, 0.88, altura])
    barra.set_facecolor(cor_barra)
    barra.set_xticks([]); barra.set_yticks([])
    for spine in barra.spines.values():
        spine.set_visible(False)
    barra.text(
        0.015, 0.5, texto,
        transform=barra.transAxes,
        color=CORES.BRANCO, fontsize=8.5, fontweight="bold",
        va="center", ha="left",
    )

    # Bloco de acento lateral direito
    acento = fig.add_axes([0.88, 1 - altura, 0.12, altura])
    acento.set_facecolor(cor_acento)
    acento.set_xticks([]); acento.set_yticks([])
    for spine in acento.spines.values():
        spine.set_visible(False)


def adicionar_rodape(
    fig: plt.Figure,
    cor_principal: str = CORES.TEAL_ESCURO,
    cor_acento: str = CORES.AMARELO,
    altura: float = 0.018,
) -> None:
    """
    Insere uma linha decorativa no rodapé da figura (como no manual impresso).
    """
    rodape = fig.add_axes([0, 0, 0.88, altura])
    rodape.set_facecolor(cor_principal)
    rodape.set_xticks([]); rodape.set_yticks([])
    for spine in rodape.spines.values():
        spine.set_visible(False)

    acento = fig.add_axes([0.88, 0, 0.12, altura])
    acento.set_facecolor(cor_acento)
    acento.set_xticks([]); acento.set_yticks([])
    for spine in acento.spines.values():
        spine.set_visible(False)


def formatar_eixo_brl(ax: plt.Axes, eixo: str = "y") -> None:
    """
    Formata um eixo para exibir valores em R$ de forma legível
    (ex.: R$ 1,2 bi / R$ 850 mi / R$ 12 mil).

    Parâmetros
    ----------
    ax   : eixo matplotlib
    eixo : 'x' ou 'y'
    """
    def _fmt(x, _):
        if abs(x) >= 1e9:
            return f"R$ {x/1e9:.1f} bi"
        elif abs(x) >= 1e6:
            return f"R$ {x/1e6:.1f} mi"
        elif abs(x) >= 1e3:
            return f"R$ {x/1e3:.0f} mil"
        else:
            return f"R$ {x:.0f}"

    formatter = mticker.FuncFormatter(_fmt)
    if eixo == "y":
        ax.yaxis.set_major_formatter(formatter)
    else:
        ax.xaxis.set_major_formatter(formatter)


def formatar_eixo_pct(ax: plt.Axes, eixo: str = "y", casas: int = 0) -> None:
    """
    Formata um eixo para exibir porcentagens (ex.: 45,2%).
    Assume que os valores já estão em escala 0–100.
    """
    fmt = mticker.FuncFormatter(lambda x, _: f"{x:.{casas}f}%")
    if eixo == "y":
        ax.yaxis.set_major_formatter(fmt)
    else:
        ax.xaxis.set_major_formatter(fmt)


def rotular_barras(
    ax: plt.Axes,
    fmt: str = "{:.0f}",
    color: str = CORES.CINZA_TEXTO,
    fontsize: float = 8.5,
    padding: float = 3,
) -> None:
    """
    Adiciona rótulos de valor no topo (ou interior) de cada barra.

    Parâmetros
    ----------
    ax      : eixo matplotlib com barras já desenhadas
    fmt     : formato do valor (ex.: "{:.1f}%" ou "R$ {:.0f}")
    color   : cor do texto
    fontsize: tamanho da fonte
    padding : distância em pontos entre o topo da barra e o texto

    Exemplo
    -------
        ax = sns.barplot(...)
        rotular_barras(ax, fmt="{:.1f}%")
    """
    for patch in ax.patches:
        h = patch.get_height()
        if np.isnan(h):
            continue
        ax.annotate(
            fmt.format(h),
            xy=(patch.get_x() + patch.get_width() / 2, h),
            xytext=(0, padding),
            textcoords="offset points",
            ha="center", va="bottom",
            fontsize=fontsize, color=color,
        )


# =============================================================================
# 4. GRÁFICOS DE EXEMPLO (executar diretamente para gerar preview)
# =============================================================================

def _exemplo_barras_simples():
    """Barras verticais — execução orçamentária por secretaria."""
    secretarias = ["SEGPLAN", "SEDUC", "SAÚDE", "AGEFIS", "SEINFRA", "SEFAZ"]
    valores = [82.4, 91.2, 78.6, 65.3, 88.1, 94.7]

    fig, ax = plt.subplots()
    bars = ax.bar(
        secretarias, valores,
        color=PALETAS.CATEGORICA[:len(secretarias)],
        width=0.6, zorder=3,
    )
    ax.set_ylim(0, 110)
    formatar_eixo_pct(ax, "y")
    rotular_barras(ax, fmt="{:.1f}%", fontsize=8)
    adicionar_cabecalho(
        ax,
        "Execução Orçamentária por Secretaria",
        subtitulo="% do orçamento empenhado — Exercício 2024",
        fonte="Fonte: SIAFEM-GO, 2024.",
    )
    adicionar_barra_institucional(fig)
    adicionar_rodape(fig)
    return fig


def _exemplo_linhas_temporais():
    """Linhas — arrecadação mensal comparada."""
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
             "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    np.random.seed(42)
    arrecadado  = 2.1 + np.cumsum(np.random.randn(12) * 0.08)
    meta        = np.linspace(2.05, 2.55, 12)

    fig, ax = plt.subplots()
    ax.plot(meses, arrecadado, color=CORES.TEAL,    marker="o", label="Arrecadado")
    ax.plot(meses, meta,       color=CORES.LARANJA, marker="s", linestyle="--",
            label="Meta", alpha=0.85)
    ax.fill_between(meses, arrecadado, meta,
                    where=(arrecadado >= meta),
                    color=CORES.TEAL, alpha=0.12, label="_nolegend_")
    ax.fill_between(meses, arrecadado, meta,
                    where=(arrecadado < meta),
                    color=CORES.LARANJA, alpha=0.12, label="_nolegend_")

    ax.legend(loc="upper left")
    ax.set_ylabel("R$ bilhões")
    adicionar_cabecalho(
        ax,
        "Arrecadação Mensal de ICMS",
        subtitulo="Realizado vs. Meta — 2024",
        fonte="Fonte: SEFAZ-GO, 2024.",
    )
    adicionar_barra_institucional(fig)
    adicionar_rodape(fig)
    return fig


def _exemplo_barras_horizontais():
    """Barras horizontais — ranking de municípios."""
    municipios = ["Goiânia", "Aparecida", "Anápolis",
                  "Rio Verde", "Luziânia", "Senador Canedo"]
    investimento = [1_450, 980, 760, 620, 510, 430]  # R$ mi

    df = pd.DataFrame({"Município": municipios, "Investimento": investimento})
    df = df.sort_values("Investimento")

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(
        df["Município"], df["Investimento"],
        color=CORES.TEAL, height=0.55, zorder=3,
    )
    # Destaque para o maior valor
    bars[-1].set_color(CORES.VERDE)

    ax.set_xlabel("Investimento (R$ milhões)")
    ax.grid(axis="x"); ax.grid(axis="y", visible=False)
    formatar_eixo_brl(ax, "x")

    # Rótulos inline
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 15, bar.get_y() + bar.get_height() / 2,
                f"R$ {w:,.0f} mi", va="center", fontsize=8.5,
                color=CORES.CINZA_TEXTO)

    adicionar_cabecalho(
        ax,
        "Investimentos por Município",
        subtitulo="Ranking dos 6 maiores — 2024",
        fonte="Fonte: SEGPLAN-GO, 2024.",
    )
    adicionar_barra_institucional(fig)
    adicionar_rodape(fig)
    return fig


def _exemplo_mapa_calor():
    """Heatmap — indicadores por bimestre."""
    indicadores = ["Escolaridade", "Saúde", "Saneamento", "Emprego", "Renda"]
    bimestres   = ["1º Bim", "2º Bim", "3º Bim", "4º Bim", "5º Bim", "6º Bim"]
    np.random.seed(7)
    dados = 60 + np.random.randn(5, 6) * 15
    dados = np.clip(dados, 0, 100)

    fig, ax = plt.subplots(figsize=(10, 4.5))
    sns.heatmap(
        dados, ax=ax,
        xticklabels=bimestres, yticklabels=indicadores,
        cmap=PALETAS.SEQUENCIAL_TEAL,
        annot=True, fmt=".1f", annot_kws={"size": 9},
        linewidths=0.5, linecolor=CORES.BRANCO,
        cbar_kws={"shrink": 0.8, "label": "Índice (0–100)"},
    )
    ax.tick_params(left=False, bottom=False)
    adicionar_cabecalho(
        ax,
        "Painel de Indicadores Sociais",
        subtitulo="Desempenho bimestral por área — 2024",
        fonte="Fonte: IMB-GO, 2024.",
    )
    adicionar_barra_institucional(fig)
    adicionar_rodape(fig)
    return fig


def _exemplo_pizza():
    """Gráfico de rosca — distribuição de receitas."""
    categorias  = ["ICMS", "IPVA", "Taxas", "Transferências", "Outros"]
    participacao = [52.3, 14.1, 8.7, 20.6, 4.3]

    fig, ax = plt.subplots(figsize=(8, 5.5))
    wedges, texts, autotexts = ax.pie(
        participacao,
        labels=None,
        autopct="%1.1f%%",
        startangle=90,
        pctdistance=0.78,
        wedgeprops={"width": 0.55, "edgecolor": CORES.BRANCO, "linewidth": 2},
        colors=PALETAS.GESTAO + [CORES.AZUL_ESCURO],
    )
    for at in autotexts:
        at.set_fontsize(9)
        at.set_color(CORES.BRANCO)
        at.set_fontweight("bold")

    ax.legend(
        wedges, [f"{c} ({v:.1f}%)" for c, v in zip(categorias, participacao)],
        loc="center left", bbox_to_anchor=(1.0, 0.5),
        frameon=False, fontsize=9,
    )
    ax.set_title(
        "Composição da Receita Estadual",
        fontsize=13, fontweight="bold",
        color=CORES.TEAL_ESCURO, pad=14,
    )
    adicionar_barra_institucional(fig)
    adicionar_rodape(fig)
    fig.tight_layout()
    return fig


def gerar_preview(caminho: str = "goias_preview.png") -> None:
    """
    Gera todos os gráficos de exemplo em um único arquivo PNG.

    Parâmetros
    ----------
    caminho : caminho de saída do arquivo PNG
    """
    apply_goias_theme(context="paper", font_scale=1.0, dpi=150)

    exemplos = [
        _exemplo_barras_simples,
        _exemplo_linhas_temporais,
        _exemplo_barras_horizontais,
        _exemplo_mapa_calor,
        _exemplo_pizza,
    ]

    fig_master, axes = plt.subplots(
        3, 2, figsize=(20, 26),
        facecolor=CORES.BRANCO,
    )
    fig_master.subplots_adjust(hspace=0.45, wspace=0.35)

    titulos_exemplos = [
        "Barras Verticais",
        "Linhas Temporais",
        "Barras Horizontais",
        "Mapa de Calor",
        "Rosca (Donut)",
    ]

    for i, (fn, titulo) in enumerate(zip(exemplos, titulos_exemplos)):
        fig_ind = fn()
        # Renderiza figura individual como imagem e incorpora no painel
        import io
        buf = io.BytesIO()
        fig_ind.savefig(buf, format="png", bbox_inches="tight",
                        facecolor=CORES.BRANCO)
        buf.seek(0)
        import matplotlib.image as mpimg
        img = mpimg.imread(buf)
        row, col = divmod(i, 2)
        axes[row][col].imshow(img)
        axes[row][col].axis("off")
        axes[row][col].set_title(titulo, fontsize=11,
                                  color=CORES.TEAL_ESCURO, fontweight="bold")
        plt.close(fig_ind)

    # Célula vazia para referência de paleta
    ax_pal = axes[2][1]
    ax_pal.set_facecolor(CORES.FUNDO)
    ax_pal.axis("off")
    ax_pal.set_title("Referência de Paleta", fontsize=11,
                      color=CORES.TEAL_ESCURO, fontweight="bold")

    todas_cores = {
        "Verde (primário)": CORES.VERDE,
        "Azul (primário)": CORES.AZUL,
        "Amarelo (primário)": CORES.AMARELO,
        "Teal Escuro": CORES.TEAL_ESCURO,
        "Teal": CORES.TEAL,
        "Verde Escuro": CORES.VERDE_ESCURO,
        "Azul Escuro": CORES.AZUL_ESCURO,
        "Laranja": CORES.LARANJA,
        "Laranja Escuro": CORES.LARANJA_ESCURO,
        "Amarelo Quente": CORES.AMARELO_QUENTE,
    }

    for j, (nome, hex_) in enumerate(todas_cores.items()):
        y_pos = 0.93 - j * 0.093
        rect = mpatches.FancyBboxPatch(
            (0.02, y_pos - 0.03), 0.09, 0.065,
            boxstyle="round,pad=0.01",
            facecolor=hex_, edgecolor="white", linewidth=1.5,
            transform=ax_pal.transAxes,
        )
        ax_pal.add_patch(rect)
        ax_pal.text(0.14, y_pos, f"{nome}  {hex_}",
                     transform=ax_pal.transAxes,
                     fontsize=8.5, va="center", color=CORES.CINZA_TEXTO)

    fig_master.suptitle(
        "Guia de Estilos Seaborn — Governo do Estado de Goiás",
        fontsize=16, fontweight="bold",
        color=CORES.TEAL_ESCURO, y=1.01,
    )

    fig_master.savefig(caminho, bbox_inches="tight",
                       facecolor=CORES.BRANCO, dpi=150)
    plt.close(fig_master)
    print(f"✓ Preview salvo em: {caminho}")


# =============================================================================
# EXECUÇÃO DIRETA — gera arquivo de preview
# =============================================================================

if __name__ == "__main__":
    gerar_preview("/sessions/wonderful-blissful-pasteur/mnt/Documents/goias_preview.png")
    print("\nGuia de uso rápido:")
    print("  from goias_seaborn_style import apply_goias_theme, CORES, PALETAS")
    print("  apply_goias_theme()")
    print("  # ... seus gráficos seaborn/matplotlib normalmente")
