# Posicionamento dos Cartões de Data de Atualização

## Posições Recomendadas por Página

Este guia visual mostra onde posicionar os cartões discretos com a data de atualização em cada página.

---

### Página: IGRO

**Posição recomendada:** Canto inferior direito

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│          [CONTEÚDO PRINCIPAL DA PÁGINA IGRO]           │
│                                                         │
│                                                         │
│                                                         │
│                                         ┌──────────────┤
│                                         │ 20/08/2026   │
│                                         │ Atualizado   │
│                                         └──────────────┤
└─────────────────────────────────────────────────────────┘
```

**Tipo:** Cartão visual com medida `dt_ultima_atualizacao_dados`  
**Tamanho:** ~150px largura × 40px altura  
**Cor de fundo:** Cinza muito claro (#F2F2F2) com borda sutil

---

### Página: CLASSE

**Posição recomendada:** Canto inferior direito

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│       [ANÁLISE POR CLASSE - TABELA/GRÁFICOS]           │
│                                                         │
│                                                         │
│                                         ┌──────────────┤
│                                         │ 20/08/2026   │
│                                         └──────────────┤
└─────────────────────────────────────────────────────────┘
```

**Alinhamento:** Consistente com IGRO

---

### Página: GERAL

**Posição recomendada:** Canto inferior direito

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│        [OVERVIEW GERAL DO MODELO IGRO]                 │
│                                                         │
│                                                         │
│                                         ┌──────────────┤
│                                         │ 20/08/2026   │
│                                         └──────────────┤
└─────────────────────────────────────────────────────────┘
```

---

### Página: NPS

**Posição recomendada:** Canto inferior direito

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│      [ANÁLISE NPS - SATISFAÇÃO E RECOMENDAÇÃO]        │
│                                                         │
│                                                         │
│                                         ┌──────────────┤
│                                         │ 20/08/2026   │
│                                         └──────────────┤
└─────────────────────────────────────────────────────────┘
```

---

### Página: EVOLUÇÃO IGRO

**Posição recomendada:** Canto inferior direito

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   [SÉRIE TEMPORAL - EVOLUÇÃO DO ÍNDICE E SUBINDICES]  │
│                                                         │
│                                                         │
│                                         ┌──────────────┤
│                                         │ 20/08/2026   │
│                                         └──────────────┤
└─────────────────────────────────────────────────────────┘
```

---

### Página: EXECUTIVA

**Posição recomendada:** Canto inferior direito (ou rodapé completo)

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│         [BRIEFING EXECUTIVO - RESUMO IGRO]             │
│                                                         │
│                                                         │
│                                                         │
│  Atualizado em: 20/08/2026 └─────────────────────────┤
└─────────────────────────────────────────────────────────┘
```

**Nota:** Na página EXECUTIVA, pode-se usar uma caixa de texto em vez de cartão para criar um rodapé mais formal.

---

## Diretrizes de Estilo

| Aspecto | Recomendação |
|---------|--------------|
| **Tipo de visual** | Cartão (Card) em 5 páginas; Caixa de texto na EXECUTIVA |
| **Medida** | `dt_ultima_atualizacao_dados` (dinâmica) |
| **Rótulo** | "Atualizado em:" ou "Dados atualizados em:" |
| **Formato de data** | Data curta regional (ex: 20/08/2026) |
| **Tamanho de fonte** | 10-11pt para cartões; 10pt para caixa de texto |
| **Cor de fundo** | Cinza muito claro (#F2F2F2) |
| **Borda** | Sim, cor cinza (#CCCCCC), espessura 1px |
| **Transparência** | Nenhuma (fundo opaco) |
| **Posição** | Canto inferior direito em todas as páginas |
| **Distância de borda** | ~10-15px do canto da página |

---

## Verificação Visual

Após implementar os cartões, a página deve se parecer com:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│                    CONTEÚDO PRINCIPAL                        │
│                                                              │
│                                                              │
│                                                              │
│                                                              │
│                            ┌──────────────────────────────┐  │
│                            │                              │  │
│                            │  Atualizado em: 20/08/2026   │  │
│                            │                              │  │
│                            └──────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

**Objetivo:** O cartão é **discreto, legível mas não intrusivo**.

---

## Implementação Detalhada

### Copiar e Colar (Atalho Rápido)

Após criar o primeiro cartão na página IGRO:

1. Clique no cartão
2. Pressione `Ctrl+C` (copiar)
3. Vá para a próxima página (ex: CLASSE)
4. Pressione `Ctrl+V` (colar)
5. Reposicione se necessário (as mesmas coordenadas podem não funcionar em layouts diferentes)

**Tempo total:** ~2 minutos por página

### Criação Manual (Mais Controle)

Se preferir criar cada cartão manualmente:

1. Clique em **Inserir > Card**
2. Arraste `dt_ultima_atualizacao_dados` para o visual
3. Clique direito > **Formatar visual**
4. Customize cor, fonte, rótulo
5. Reposicione e redimensione

**Tempo total:** ~5 minutos por página

---

## Alternativa: Nota de Rodapé de Página

Se o modelo IGRO usar um rodapé compartilhado ou header/footer de página (Power BI não oferece isso nativamente, mas você pode criar um visual de rodapé compartilhado):

1. Crie uma página chamada `_Rodape` (começa com `_` para ficar no final)
2. Adicione o cartão nessa página
3. Copie a imagem ou o visual para o rodapé de cada página

**Essa abordagem é útil se você quiser:** manter um único ponto de atualização para o rodapé em todas as páginas.

---

## Próximos Passos

1. ✅ Abra o modelo `indice_igro_v2.pbip` no Power BI Desktop
2. ✅ Crie a medida `dt_ultima_atualizacao_dados` (ver: `guia_data_atualizacao_dados.md`)
3. ✅ Adicione o cartão na página IGRO (canto inferior direito)
4. ✅ Copie o cartão para as outras 5 páginas
5. ✅ Salve o modelo (`Ctrl+S`)
6. ✅ Teste um refresh para confirmar que a data atualiza
7. ✅ Valide visualmente em todas as páginas

---

**Última revisão:** 2026-08-21  
**Relacionado:** `guia_data_atualizacao_dados.md`
