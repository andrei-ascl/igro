# Notebooks de exploração

Notebooks Jupyter usados para gerar as figuras, tabelas e exportações analíticas do IGRO.

## Notebooks

| Notebook | Uso | Saída |
|---|---|---|
| `artigo_igro_graficos_tabelas.ipynb` | Notebook principal — gráficos e tabelas do artigo, incluindo a tabela suplementar com o ranking completo dos 51 órgãos | `09_resultados/artigo_igro_figuras_tabelas/figuras/` e `tabelas/` |
| `igro_analise_sensibilidade_pesos.ipynb` | Análise de sensibilidade dos pesos do IGRO (cenários, bootstrap, mudança de classe) | `09_resultados/exportacoes/analise_sensibilidade_pesos_igro/` |
| `igro_graficos_quadrimestres.ipynb` | Gráficos por quadrimestre (ex.: KRI4 — % respostas insatisfatórias) | `09_resultados/exportacoes/graficos_quadrimestres_igro/` |

## Convenções

- Rodar os notebooks a partir da raiz do repositório, para que os caminhos relativos de leitura (`02_dados/processed/`) e escrita (`09_resultados/`) resolvam corretamente.
- Ao adicionar uma nova célula que gera artefato novo, registrar aqui a saída correspondente.
- Notebooks não substituem os scripts em `05_scripts/python/` quando a geração precisa rodar fora de um kernel Jupyter (ex.: `gerar_tabela_suplementar_excel.py`).

---

**Última atualização:** 2026-07-25
