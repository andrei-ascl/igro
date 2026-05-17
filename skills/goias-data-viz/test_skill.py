import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Adiciona o diretório de scripts da skill ao path
sys.path.append(os.path.abspath('scripts'))

from goias_seaborn_style import apply_goias_theme, CORES, PALETAS, adicionar_cabecalho, adicionar_barra_institucional, adicionar_rodape, formatar_eixo_brl

# Configurações iniciais
apply_goias_theme(context="paper", dpi=150)

# Dados de exemplo
dados = pd.DataFrame({
    'Município': ['Goiânia', 'Aparecida', 'Anápolis', 'Rio Verde', 'Luziânia'],
    'Investimento': [1450, 980, 760, 620, 510] # R$ milhões
}).sort_values('Investimento')

# Criação do gráfico
fig, ax = plt.subplots(figsize=(10, 5.5))
bars = ax.barh(dados['Município'], dados['Investimento'], color=CORES.TEAL, height=0.6, zorder=3)

# Destaque para o primeiro colocado (que é o último no dataframe sorteado)
bars[-1].set_color(CORES.VERDE)

# Formatação e Identidade
formatar_eixo_brl(ax, "x")
adicionar_cabecalho(ax, 
    titulo="Investimentos por Município", 
    subtitulo="Ranking dos 5 maiores investimentos — Exercício 2024",
    fonte="Fonte: Secretaria de Planejamento (GO), 2024")

adicionar_barra_institucional(fig)
adicionar_rodape(fig)

# Salvando
output_path = 'test_ranking_goias.png'
plt.savefig(output_path, bbox_inches='tight', dpi=150)
print(f"Gráfico gerado em: {output_path}")
