# Scripts e Automações — IGRO

Utilitários Python e Power Query para processamento de dados, geração de artefatos e automações do estudo.

## Estrutura

### `python/`
Scripts executáveis em Python:
- `main.py` — Ponto de entrada principal
- `gerar_tabela_suplementar_excel.py` — Gera `tabela_suplementar_igro_51_orgaos.xlsx` (ranking completo dos 51 órgãos), saída em `09_resultados/artigo_igro_figuras_tabelas/tabelas/`
- `apresentacoes/` — Scripts para geração e manutenção de apresentações
  - `criar_apresentacao_igro.py` — Gerador de apresentação v1
  - `criar_apresentacao_igro_v2.py` — Gerador de apresentação v2

## Objetivo

Automatizar tarefas repetitivas: processamento de dados brutos, geração de artefatos (slides, gráficos), cálculo de KRIs normalizados, e validação de consistência entre bases.

## Execução

```bash
python main.py
```

Para gerar apresentações:
```bash
python apresentacoes/criar_apresentacao_igro_v2.py
```

## Dependências

Especificadas em arquivo de requisitos (se existente na raiz do projeto ou em `requirements.txt`).

---

**Mantido em:** Estudos do IGRO  
**Última atualização:** 2026-07-25
