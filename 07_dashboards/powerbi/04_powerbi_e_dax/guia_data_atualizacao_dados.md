# Guia: Data de Atualização dos Dados em Todas as Páginas

**Objetivo:** Adicionar um cartão discreto ou nota de rodapé mostrando a data de atualização dos dados em todas as 6 páginas do modelo IGRO.

**Status do dado:** Última atualização em **2026-08-18** (arquivos Parquet em `06_dados/01_brutos/`)

---

## Passo 1: Criar a Medida DAX

A medida abaixo retorna a data máxima das manifestações registradas nos dados, refletindo a última atualização:

### Medida: `dt_ultima_atualizacao_dados`

1. Abra o Power BI Desktop com o modelo `indice_igro_v2.pbip`
2. Clique em **Nova medida** (no menu Modelagem ou clique direito na tabela `_medidas`)
3. Cole o código abaixo:

```dax
dt_ultima_atualizacao_dados = 
VAR max_data_manifestacao = MAX ( f_relatorio[data_manifestacao] )
VAR resultado = 
    IF (
        ISBLANK ( max_data_manifestacao ),
        TODAY (),
        max_data_manifestacao
    )
RETURN
    resultado
```

**Propriedades da medida:**
- **Nome:** `dt_ultima_atualizacao_dados`
- **Descrição:** "Data da última manifestação nos dados; reflete a atualização mais recente do modelo"
- **DisplayFolder:** `11 · Rótulo · Cartão` (para manter organizado junto com outros rótulos)
- **Formato:** `Data Curta` (formato regional)

---

## Passo 2: Adicionar um Cartão Visual em Cada Página

### Opção A: Cartão Discreto (Recomendado)

Cria um visual de cartão pequeno e discreto no rodapé de cada página.

#### Instruções Gerais (repetir para cada página):

1. **Abra a página** (ex: IGRO, CLASSE, GERAL, NPS, EVOLUÇÃO IGRO, EXECUTIVA)
2. **Insira um visual de Cartão:**
   - Clique em **Inserir > Card** (ou busque "Card" na galeria de visuais)
3. **Configure o visual:**
   - Arraste `dt_ultima_atualizacao_dados` para a zona **Campos**
   - Redimensione o cartão para ficar pequeno e discreto (ex: canto inferior direito)
   
4. **Customize (opcional):**
   - Clique no cartão > **Formatar visual**
   - Na seção **Rótulo de categoria:**
     - Marque **Ativado**
     - Defina **Texto** como: `"Dados atualizados em:"`
   - Na seção **Cor de fundo:**
     - Defina uma cor neutra (ex: cinza claro `#F2F2F2`)
   - Na seção **Borda:**
     - Ative a borda e defina cor clara

5. **Posicione no rodapé:**
   - Mova o cartão para o canto inferior direito (ou esquerdo, conforme preferência)
   - Certifique-se de que não conflite com outros elementos

#### Páginas a Processar:
- [ ] IGRO
- [ ] CLASSE
- [ ] GERAL
- [ ] NPS
- [ ] EVOLUÇÃO IGRO
- [ ] EXECUTIVA

---

### Opção B: Caixa de Texto com Fórmula (Alternativa)

Se preferir uma nota de rodapé textual em vez de um cartão:

1. **Insira uma caixa de texto:**
   - Clique em **Inserir > Caixa de Texto**
   
2. **Digite um rótulo dinâmico** (nota: Power BI não interpreta fórmulas DAX em caixas de texto diretamente)
   - Você pode adicionar o rótulo manualmente: `"Dados atualizados em: 2026-08-18"`
   - OU deixar genérico: `"Dados atualizados em: [consulte o refresh do modelo]"`

3. **Posicione e formate:**
   - Tamanho de fonte pequeno (ex: 9pt)
   - Cor neutra (ex: cinza)
   - Rodapé da página

**Desvantagem:** a data precisa ser atualizada manualmente. A Opção A (Cartão) é dinâmica.

---

## Passo 3: Sincronizar e Salvar

1. Após adicionar o cartão/nota em todas as 6 páginas:
   - Clique em **Arquivo > Salvar** (ou `Ctrl+S`)
   
2. Se usar Power BI Desktop com PBIP:
   - O modelo será salvo automaticamente
   - Sincronize o arquivo `.tmdl` com o modelo (se necessário)

3. Valide o resultado:
   - Abra cada página e confirme que a data aparece corretamente
   - Teste um refresh para confirmar que a medida atualiza

---

## Alternativa: Usar uma Caixa de Texto Dinâmica com M (Power Query)

Se quiser que a data seja exibida automaticamente em todas as páginas sem inserir um cartão em cada uma, considere:

1. Criar uma tabela de parâmetros em Power Query:
   ```
   Tabela: _Parametros
   Coluna: DataAtualizacao = "Dados atualizados em: [DATA_DINAMICA]"
   ```

2. Usar essa tabela como fonte de um visual único que possa ser copiado para todas as páginas

**Nota:** Esta abordagem é mais complexa; use a Opção A (Cartão com medida) se for primeira vez.

---

## Referência Técnica

| Campo | Valor |
|-------|-------|
| **Fonte de dados** | `f_relatorio[data_manifestacao]` |
| **Lógica** | MAX da data de manifestação (última manifestação registrada) |
| **Formato esperado** | `20/08/2026` (ou formato regional) |
| **Atualização** | Automática após refresh dos dados do Parquet |
| **Tabela de armazenamento** | `_medidas` |

---

## Verificação Pós-Implementação

Após implementar, verifique:

- ✅ A medida `dt_ultima_atualizacao_dados` foi criada em `_medidas`
- ✅ Um visual foi adicionado em cada uma das 6 páginas
- ✅ O cartão/nota aparece no rodapé discretamente
- ✅ Após um refresh, a data atualiza dinamicamente
- ✅ Nenhum filtro externo afeta a data exibida (ela deve ser sempre a máxima global)

---

## Notas Finais

1. **Frequência de refresh:** Se os dados são atualizados automaticamente (ex: diariamente em 06_dados/01_brutos/), a data no cartão acompanhará
2. **Timezone:** A data reflete a data de manifestação conforme armazenada no Parquet (verificar se é UTC ou local)
3. **Discretion:** Cartões pequenos no rodapé não competem com elementos visuais principais
4. **Acessibilidade:** A data em texto é legível para leitores de tela; o cartão é mais acessível que cores ou ícones isolados

---

**Última revisão:** 2026-08-21  
**Próximo passo:** Executar os passos acima e validar em todas as 6 páginas
