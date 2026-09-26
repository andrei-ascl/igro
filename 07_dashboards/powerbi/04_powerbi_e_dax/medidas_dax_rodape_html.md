# Medidas DAX — Rodapés em HTML para Cada Página

Este documento contém as medidas DAX que geram rodapés HTML personalizados para cada página do modelo IGRO, respeitando os esquemas de cores de cada uma.

**Como usar:** Copie cada medida, crie-a em `_medidas`, e insira um visual **HTML Content** em cada página com a medida correspondente.

---

## Rodapé Padrão — Página IGRO (Azul/Dourado)

**Nome da medida:** `html_rodape_igro`  
**DisplayFolder:** `12 · JSON · Dashboard`

```dax
html_rodape_igro =
VAR data_atualizacao = FORMAT([dt_ultima_atualizacao_dados], "dd/mm/yyyy")
VAR html =
    "<div style='width:100%;padding:12px 16px;background:linear-gradient(90deg,#f5f1ea 0%,#fbf8f3 100%);border-top:2px solid #79bcc0;font-family:Segoe UI,Arial,sans-serif;font-size:11px;color:#4e5c64;display:flex;justify-content:space-between;align-items:center;'>"
    & "<span style='letter-spacing:0.5px;'>Dados atualizados em: <strong style='color:#0f1720;font-weight:600;'>" & data_atualizacao & "</strong></span>"
    & "<span style='font-size:9px;color:#9aa5ad;'>IGRO • Modelo Semântico v2.0</span>"
    & "</div>"
RETURN
    html
```

---

## Rodapé Página CLASSE (Azul/Verde)

**Nome da medida:** `html_rodape_classe`  
**DisplayFolder:** `12 · JSON · Dashboard`

```dax
html_rodape_classe =
VAR data_atualizacao = FORMAT([dt_ultima_atualizacao_dados], "dd/mm/yyyy")
VAR html =
    "<div style='width:100%;padding:12px 16px;background:linear-gradient(90deg,#f0f8f7 0%,#f8fcfb 100%);border-top:2px solid #5fa5ab;font-family:Segoe UI,Arial,sans-serif;font-size:11px;color:#4e5c64;display:flex;justify-content:space-between;align-items:center;'>"
    & "<span style='letter-spacing:0.5px;'>Dados atualizados em: <strong style='color:#0f1720;font-weight:600;'>" & data_atualizacao & "</strong></span>"
    & "<span style='font-size:9px;color:#9aa5ad;'>CLASSE • Análise por Categoria</span>"
    & "</div>"
RETURN
    html
```

---

## Rodapé Página GERAL (Cinza/Neutro)

**Nome da medida:** `html_rodape_geral`  
**DisplayFolder:** `12 · JSON · Dashboard`

```dax
html_rodape_geral =
VAR data_atualizacao = FORMAT([dt_ultima_atualizacao_dados], "dd/mm/yyyy")
VAR html =
    "<div style='width:100%;padding:12px 16px;background:linear-gradient(90deg,#f8f8f8 0%,#fafafa 100%);border-top:2px solid #b0b8c0;font-family:Segoe UI,Arial,sans-serif;font-size:11px;color:#4e5c64;display:flex;justify-content:space-between;align-items:center;'>"
    & "<span style='letter-spacing:0.5px;'>Dados atualizados em: <strong style='color:#0f1720;font-weight:600;'>" & data_atualizacao & "</strong></span>"
    & "<span style='font-size:9px;color:#9aa5ad;'>GERAL • Visão Consolidada</span>"
    & "</div>"
RETURN
    html
```

---

## Rodapé Página NPS (Verde/Teal)

**Nome da medida:** `html_rodape_nps`  
**DisplayFolder:** `12 · JSON · Dashboard`

```dax
html_rodape_nps =
VAR data_atualizacao = FORMAT([dt_ultima_atualizacao_dados], "dd/mm/yyyy")
VAR html =
    "<div style='width:100%;padding:12px 16px;background:linear-gradient(90deg,#f0faf9 0%,#f8fcfb 100%);border-top:2px solid #138ca4;font-family:Segoe UI,Arial,sans-serif;font-size:11px;color:#4e5c64;display:flex;justify-content:space-between;align-items:center;'>"
    & "<span style='letter-spacing:0.5px;'>Dados atualizados em: <strong style='color:#0f1720;font-weight:600;'>" & data_atualizacao & "</strong></span>"
    & "<span style='font-size:9px;color:#9aa5ad;'>NPS • Satisfação e Recomendação</span>"
    & "</div>"
RETURN
    html
```

---

## Rodapé Página EVOLUÇÃO IGRO (Laranja/Âmbar)

**Nome da medida:** `html_rodape_evolucao`  
**DisplayFolder:** `12 · JSON · Dashboard`

```dax
html_rodape_evolucao =
VAR data_atualizacao = FORMAT([dt_ultima_atualizacao_dados], "dd/mm/yyyy")
VAR html =
    "<div style='width:100%;padding:12px 16px;background:linear-gradient(90deg,#fef8f3 0%,#fffbf7 100%);border-top:2px solid #f5b11f;font-family:Segoe UI,Arial,sans-serif;font-size:11px;color:#4e5c64;display:flex;justify-content:space-between;align-items:center;'>"
    & "<span style='letter-spacing:0.5px;'>Dados atualizados em: <strong style='color:#0f1720;font-weight:600;'>" & data_atualizacao & "</strong></span>"
    & "<span style='font-size:9px;color:#9aa5ad;'>EVOLUÇÃO • Série Temporal IGRO</span>"
    & "</div>"
RETURN
    html
```

---

## Rodapé Página EXECUTIVA (Azul Escuro/Premium)

**Nome da medida:** `html_rodape_executiva`  
**DisplayFolder:** `12 · JSON · Dashboard`

```dax
html_rodape_executiva =
VAR data_atualizacao = FORMAT([dt_ultima_atualizacao_dados], "dd/mm/yyyy")
VAR html =
    "<div style='width:100%;padding:12px 16px;background:linear-gradient(90deg,#102028 0%,#1a2f3d 100%);border-top:3px solid #79bcc0;font-family:Segoe UI,Arial,sans-serif;font-size:11px;color:#b0b8c0;display:flex;justify-content:space-between;align-items:center;'>"
    & "<span style='letter-spacing:0.5px;'>Dados atualizados em: <strong style='color:#e0f4f6;font-weight:600;'>" & data_atualizacao & "</strong></span>"
    & "<span style='font-size:9px;color:#6b7b84;'>EXECUTIVA • Briefing para Liderança</span>"
    & "</div>"
RETURN
    html
```

---

## Como Implementar

### Passo 1: Criar as Medidas DAX

1. Abra o Power BI Desktop com `indice_igro_v2.pbip`
2. Para cada medida acima:
   - Clique em **Nova Medida** (ou clique direito em `_medidas`)
   - Cole o código DAX
   - Defina **DisplayFolder** como `12 · JSON · Dashboard`
3. Salve o modelo (`Ctrl+S`)

### Passo 2: Adicionar Visuals de HTML Content

Para cada página:

1. **Abra a página** (ex: IGRO)
2. Clique em **Inserir > HTML Content** (busque na galeria de visuais)
3. Configure o visual:
   - **URL ou código:** Selecione a medida correspondente (ex: `html_rodape_igro`)
4. **Redimensione:**
   - Estique até a borda inferior da página
   - Altura: ~40-50px
   - Posicione no rodapé

5. **Repita para cada página:**
   - IGRO → `html_rodape_igro`
   - CLASSE → `html_rodape_classe`
   - GERAL → `html_rodape_geral`
   - NPS → `html_rodape_nps`
   - EVOLUÇÃO IGRO → `html_rodape_evolucao`
   - EXECUTIVA → `html_rodape_executiva`

### Passo 3: Validar

1. Clique em cada página e confirme que o rodapé aparece
2. Verifique se a data está correta (deve ser 18/08/2026)
3. Confirme que o cor do rodapé se harmoniza com cada página

---

## Características

| Aspecto | Detalhe |
|---------|---------|
| **Data dinâmica** | Usa a medida `dt_ultima_atualizacao_dados` |
| **Discreto** | Rodapé fino (40-50px) |
| **Cores personalizadas** | Cada página tem sua paleta |
| **Legenda de página** | Identifica qual é a página (ex: "IGRO • Modelo Semântico v2.0") |
| **Reutilizável** | Apenas copie e cole |

---

## Customização

Se quiser alterar cores, fontes ou layout:

### Cores principais
- `background`: cor de fundo do rodapé (gradiente)
- `border-top`: cor da linha superior (2-3px)
- `color`: cor do texto principal
- Strong (`color: #0f1720`): cor do texto da data

### Fonts
- `font-size: 11px` → texto principal
- `font-size: 9px` → texto secundário (legenda)

### Espaçamento
- `padding: 12px 16px` → espaçamento interno
- Ajuste conforme necessário

---

## Exemplo Visual

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│              [CONTEÚDO PRINCIPAL DA PÁGINA]                │
│                                                             │
│─────────────────────────────────────────────────────────────│
│ Dados atualizados em: 18/08/2026    IGRO • Modelo v2.0    │
│─────────────────────────────────────────────────────────────│
```

---

## Validação

- ✅ Medida criada com nome correto
- ✅ DisplayFolder correto (`12 · JSON · Dashboard`)
- ✅ Visual de HTML Content adicionado em cada página
- ✅ Rodapé posicionado no canto inferior
- ✅ Data atualiza dinamicamente após refresh
- ✅ Cores se harmonizam com a página
- ✅ Modelo salvo

---

**Última revisão:** 2026-08-21  
**Relacionado:** `dt_ultima_atualizacao_dados`, `guia_data_atualizacao_dados.md`
