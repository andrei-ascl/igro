# Ajuste Manual dos `subs` no HTML Infográfico IGRO

Este guia resume como ajustar manualmente o posicionamento dos blocos `Sub-Tempo` e `Sub-Qualidade` na medida `HTML Infografico IGRO`.

## Onde ajustar

Os `subs` são posicionados principalmente por este bloco CSS dentro da medida:

```css
.subs{
  position:absolute;
  left:404px;
  top:98px;
  width:282px;
  display:flex;
  flex-direction:column;
  gap:98px;
}

.subcard{
  position:relative;
  height:92px;
  border-radius:24px;
  padding:16px 92px 16px 88px;
}
```

## O que cada propriedade faz

- `left`: move os dois cards de subíndice para a esquerda ou direita.
- `top`: sobe ou desce o bloco inteiro dos `subs`.
- `width`: aumenta ou reduz a largura da coluna dos `subs`.
- `gap`: aumenta ou reduz a distância vertical entre `Sub-Tempo` e `Sub-Qualidade`.
- `height`: altera a altura de cada card.
- `padding`: ajusta o espaço interno do card, especialmente texto e selo lateral.

## Ordem prática de ajuste

1. Ajustar `.subs left` para acertar a coluna horizontal.
2. Ajustar `.subs top` para casar o bloco com os conectores.
3. Ajustar `.subs gap` para equilibrar a distância entre os dois cards.
4. Só depois, se necessário, ajustar `width` e `padding` de `.subcard`.

## Exemplo de ajuste fino

```css
.subs{
  left:390px;
  top:110px;
  width:290px;
  gap:86px;
}
```

Leitura do exemplo:

- `left:390px`: move os `subs` um pouco mais para a esquerda.
- `top:110px`: desce levemente o conjunto.
- `width:290px`: alarga a coluna.
- `gap:86px`: aproxima os dois cards.

## Ajuste dos conectores

Os conectores ficam no SVG da classe `map`, em linhas como estas:

```html
<line x1='216' y1='180' x2='300' y2='180' ... />
<line x1='216' y1='328' x2='300' y2='328' ... />
<line x1='300' y1='180' x2='404' y2='180' ... />
<line x1='300' y1='328' x2='404' y2='328' ... />
```

Como interpretar:

- `y='180'` representa o eixo do `Sub-Tempo`.
- `y='328'` representa o eixo do `Sub-Qualidade`.
- `x2='404'` conversa diretamente com o `left:404px` da coluna `.subs`.

## Regra prática de sincronização

- Se mudar `left` dos `subs`, ajuste os `x2` das linhas e os `cx` dos círculos próximos.
- Se mudar `top` ou `gap`, ajuste os `y` das linhas e dos círculos correspondentes.

## Checklist rápido

- Os dois `subs` parecem uma coluna única.
- O centro vertical de cada `sub` bate com seu conector.
- O conector não invade o card.
- `Sub-Tempo` e `Sub-Qualidade` têm respiro visual parecido.
- O bloco dos `subs` não compete com o círculo do IGRO nem com os KRIs.

## Observação operacional

Durante esta sessão, os ajustes foram feitos prioritariamente no modelo conectado para economizar iterações no `.tmdl`.

No fim da sessão, lembrar de gerar um novo `.tmdl`.
