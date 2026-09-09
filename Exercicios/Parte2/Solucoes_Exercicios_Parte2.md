# Exercícios de Aprendizagem — Parte 2
## Teorema Chinês do Resto e Partilha de Senha

**Disciplina:** Criptografia Aplicada
**Base teórica:** `Introducao_Crip_Teoria_Num.pdf`, `Fermat_Grupo_Corpos.pdf`, `fundamentos_matematicos.pdf` (seção 3.4)

---

## Método utilizado (Teorema Chinês do Resto)

Sejam `m₁, m₂, ..., m_k` inteiros positivos **dois a dois primos entre si**. O sistema

```
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
        ⋮
x ≡ a_k (mod m_k)
```

tem **solução única módulo** `M = m₁ × m₂ × ... × m_k`, dada por:

```
x ≡ Σ aᵢ × Mᵢ × M'ᵢ   (mod M),   onde   Mᵢ = M / mᵢ   e   M'ᵢ ≡ Mᵢ⁻¹ (mod mᵢ)
```

Este é exatamente o procedimento da seção 3.4 de `fundamentos_matematicos.pdf`, usado em todas as questões abaixo.

---

## Questão 1 — Os três satélites

### Modelagem

Seja `x` o número de horas decorridas a partir da meia-noite até a passagem simultânea.

| Satélite | 1ª passagem | Período | Congruência |
|---|---|---|---|
| 1º | 2 h | 13 h | `x ≡ 2 (mod 13)` |
| 2º | 5 h | 15 h | `x ≡ 5 (mod 15)` |
| 3º | 8 h | 19 h | `x ≡ 8 (mod 19)` |

Cada satélite passa sobre o Rio nos instantes `2 + 13t`, `5 + 15t` e `8 + 19t`. O instante comum é a solução do sistema.

**Verificação da hipótese:** `mdc(13,15) = mdc(13,19) = mdc(15,19) = 1` → os módulos são dois a dois coprimos, o TCR se aplica.

### Resolução

`M = 13 × 15 × 19 = 3705`

| i | aᵢ | mᵢ | Mᵢ = M/mᵢ | Mᵢ mod mᵢ | Congruência do inverso | M'ᵢ |
|---|---|---|---|---|---|---|
| 1 | 2 | 13 | 285 | 12 | `12·M'₁ ≡ 1 (mod 13)`, e `12 ≡ −1` → `−M'₁ ≡ 1` | **12** |
| 2 | 5 | 15 | 247 | 7 | `7·M'₂ ≡ 1 (mod 15)`, pois `7·13 = 91 = 6·15 + 1` | **13** |
| 3 | 8 | 19 | 195 | 5 | `5·M'₃ ≡ 1 (mod 19)`, pois `5·4 = 20 = 19 + 1` | **4** |

```
x = 2·285·12 + 5·247·13 + 8·195·4
x = 6840 + 16055 + 6240 = 29135
29135 = 7·3705 + 3200  →  x ≡ 3200 (mod 3705)
```

### Conferência

`3200 = 246·13 + 2` ✓  `3200 = 213·15 + 5` ✓  `3200 = 168·19 + 8` ✓

### Resposta

> **x = 3200 horas** após a meia-noite (solução geral: `x = 3200 + 3705k`).
> Isso equivale a **133 dias e 8 horas**.

---

## Questão 2 — Menor inteiro positivo com restos 2, 4 e 5

### Modelagem

```
x ≡ 2 (mod 5)
x ≡ 4 (mod 7)
x ≡ 5 (mod 11)
```

Módulos 5, 7 e 11 são primos distintos → dois a dois coprimos. `M = 5 × 7 × 11 = 385`

### Resolução

| i | aᵢ | mᵢ | Mᵢ | Mᵢ mod mᵢ | Cálculo do inverso | M'ᵢ |
|---|---|---|---|---|---|---|
| 1 | 2 | 5 | 77 | 2 | `2·3 = 6 ≡ 1 (mod 5)` | **3** |
| 2 | 4 | 7 | 55 | 6 | `6·6 = 36 ≡ 1 (mod 7)` | **6** |
| 3 | 5 | 11 | 35 | 2 | `2·6 = 12 ≡ 1 (mod 11)` | **6** |

```
x = 2·77·3 + 4·55·6 + 5·35·6
x = 462 + 1320 + 1050 = 2832
2832 = 7·385 + 137  →  x ≡ 137 (mod 385)
```

### Conferência

`137 = 27·5 + 2` ✓  `137 = 19·7 + 4` ✓  `137 = 12·11 + 5` ✓

### Resposta

> **x = 137** é o menor inteiro positivo. (Solução geral: `x = 137 + 385k`.)

---

## Questão 3 — O general chinês

### Modelagem

Seja `x` o número de soldados **sobreviventes** presentes na formatura:

```
x ≡ 5 (mod 7)     (filas de 7, sobram 5)
x ≡ 4 (mod 9)     (filas de 9, sobram 4)
x ≡ 1 (mod 10)    (filas de 10, sobra 1)
```

`mdc(7,9) = mdc(7,10) = mdc(9,10) = 1` → coprimos dois a dois. `M = 7 × 9 × 10 = 630`

### Resolução

| i | aᵢ | mᵢ | Mᵢ | Mᵢ mod mᵢ | Cálculo do inverso | M'ᵢ |
|---|---|---|---|---|---|---|
| 1 | 5 | 7 | 90 | 6 | `6·6 = 36 ≡ 1 (mod 7)` | **6** |
| 2 | 4 | 9 | 70 | 7 | `7·4 = 28 ≡ 1 (mod 9)` | **4** |
| 3 | 1 | 10 | 63 | 3 | `3·7 = 21 ≡ 1 (mod 10)` | **7** |

```
x = 5·90·6 + 4·70·4 + 1·63·7
x = 2700 + 1120 + 441 = 4261
4261 = 6·630 + 481  →  x ≡ 481 (mod 630)
```

### Seleção da solução no intervalo do problema

Solução geral: `x = 481 + 630k`

| k | x | Válido? (1500 < x ≤ 2000) |
|---|---|---|
| 0 | 481 | não |
| 1 | 1111 | não |
| 2 | **1741** | **sim** |
| 3 | 2371 | não (excede os 2000 soldados iniciais) |

### Conferência

`1741 = 248·7 + 5` ✓  `1741 = 193·9 + 4` ✓  `1741 = 174·10 + 1` ✓

### Resposta

> Sobreviveram **1741 soldados**, logo morreram na batalha
> **2000 − 1741 = 259 soldados**.

---

## Questão 4 — Sistema de quatro congruências

### Redução prévia

O sistema dado é:

```
x ≡  3 (mod 5)
x ≡  5 (mod 3)
x ≡ 11 (mod 7)
x ≡  3 (mod 4)
```

Duas congruências têm resto maior que o módulo e precisam ser reduzidas à forma canônica (`0 ≤ aᵢ < mᵢ`):

- `5 ≡ 2 (mod 3)` → `x ≡ 2 (mod 3)`
- `11 ≡ 4 (mod 7)` → `x ≡ 4 (mod 7)`

Sistema equivalente:

```
x ≡ 3 (mod 5)
x ≡ 2 (mod 3)
x ≡ 4 (mod 7)
x ≡ 3 (mod 4)
```

**Coprimalidade:** 5, 3, 7 são primos distintos e `4 = 2²` não compartilha fatores com nenhum deles → dois a dois coprimos. `M = 5 × 3 × 7 × 4 = 420`

### Resolução

| i | aᵢ | mᵢ | Mᵢ | Mᵢ mod mᵢ | Cálculo do inverso | M'ᵢ |
|---|---|---|---|---|---|---|
| 1 | 3 | 5 | 84 | 4 | `4·4 = 16 ≡ 1 (mod 5)` | **4** |
| 2 | 2 | 3 | 140 | 2 | `2·2 = 4 ≡ 1 (mod 3)` | **2** |
| 3 | 4 | 7 | 60 | 4 | `4·2 = 8 ≡ 1 (mod 7)` | **2** |
| 4 | 3 | 4 | 105 | 1 | `1·1 = 1 ≡ 1 (mod 4)` | **1** |

```
x = 3·84·4 + 2·140·2 + 4·60·2 + 3·105·1
x = 1008 + 560 + 480 + 315 = 2363
2363 = 5·420 + 263  →  x ≡ 263 (mod 420)
```

### Conferência

`263 = 52·5 + 3` ✓  `263 = 87·3 + 2` ✓  `263 = 37·7 + 4` ✓  `263 = 65·4 + 3` ✓

### Resposta

> **x = 263** é o menor inteiro positivo que satisfaz o sistema.

---

## Questão 5 — Cofre da empresa X (k = 2)

### Fundamentação (Partilha de Senha)

Segundo as definições de `Fermat_Grupo_Corpos.pdf`:

- **Limiar de um conjunto:** `L` é um conjunto de `n` inteiros positivos dois a dois coprimos, `N` = produto dos `k` **menores** elementos de `L` e `M` = produto dos `k − 1` **maiores**. `L` tem limiar `k` se `M < s < N`.
- **Conjunto gerador de senhas:** `S` é formado pelos pares `(p, s_p)` com `p ∈ L` e `s_p ≡ s (mod p)`.

### Dados

```
S = {(7,6), (11,3), (13,4), (17,1), (19,12)}   →   L = {7, 11, 13, 17, 19},  n = 5,  k = 2
```

- `N` = produto dos `k = 2` menores = `7 × 11 = 77`
- `M` = produto do `k − 1 = 1` maior = `19`
- Portanto **`19 < s < 77`**

### Resolução — dois funcionários quaisquer

Tomando os funcionários de senhas `(7,6)` e `(11,3)`:

```
x ≡ 6 (mod 7)
x ≡ 3 (mod 11)
```

`M = 7 × 11 = 77`

| i | aᵢ | mᵢ | Mᵢ | Mᵢ mod mᵢ | Cálculo do inverso | M'ᵢ |
|---|---|---|---|---|---|---|
| 1 | 6 | 7 | 11 | 4 | `4·2 = 8 ≡ 1 (mod 7)` | **2** |
| 2 | 3 | 11 | 7 | 7 | `7·8 = 56 ≡ 1 (mod 11)` | **8** |

```
x = 6·11·2 + 3·7·8 = 132 + 168 = 300
300 = 3·77 + 69  →  x ≡ 69 (mod 77)
```

Como `19 < 69 < 77`, a senha está no intervalo do limiar: **s = 69**.

### Verificação com os demais pares

Qualquer par de funcionários chega ao mesmo valor (o produto de dois módulos quaisquer é sempre `≥ 77 > 69`, garantindo unicidade):

| Par usado | Módulo do sistema | Resultado |
|---|---|---|
| (7,6) e (11,3) | 77 | 69 |
| (7,6) e (13,4) | 91 | 69 |
| (11,3) e (17,1) | 187 | 69 |
| (13,4) e (19,12) | 247 | 69 |
| (17,1) e (19,12) | 323 | 69 |

**Consistência total:** `69 mod 7 = 6` ✓ · `69 mod 11 = 3` ✓ · `69 mod 13 = 4` ✓ · `69 mod 17 = 1` ✓ · `69 mod 19 = 12` ✓

### Segurança do esquema

Um funcionário **sozinho** conhece no máximo `x ≡ 12 (mod 19)`, cujo módulo `19 < 69`. No intervalo `(19, 77)` isso deixa os candidatos **31, 50 e 69**, indistinguíveis entre si — logo a senha **não** é recuperável com uma única chave. É exatamente essa a função do limiar `k = 2`.

### Resposta

> **s = 69**

---

## Questão 6 — Banco "TAMBURETE" (k = 3)

### Dados e verificação do limiar

```
L = {7, 11, 13, 17, 19},  n = 5,  k = 3,  s = 640
```

- `N` = produto dos `k = 3` **menores** = `7 × 11 × 13 = 1001`
- `M` = produto dos `k − 1 = 2` **maiores** = `17 × 19 = 323`
- Condição do limiar: `323 < s < 1001` → **`323 < 640 < 1001` ✓** (a senha `s = 640` é válida)

### Determinação do conjunto gerador S

Cada par é `(p, s_p)` com `s_p = 640 mod p`:

| p | Divisão | s_p = 640 mod p | Par |
|---|---|---|---|
| 7 | `640 = 91·7 + 3` | 3 | **(7, 3)** |
| 11 | `640 = 58·11 + 2` | 2 | **(11, 2)** |
| 13 | `640 = 49·13 + 3` | 3 | **(13, 3)** |
| 17 | `640 = 37·17 + 11` | 11 | **(17, 11)** |
| 19 | `640 = 33·19 + 13` | 13 | **(19, 13)** |

```
S = {(7,3), (11,2), (13,3), (17,11), (19,13)}
```

### Como três funcionários abrem o cofre

Suponha os portadores de `(7,3)`, `(11,2)` e `(13,3)` (o pior caso, de menor módulo):

```
x ≡ 3 (mod 7)
x ≡ 2 (mod 11)
x ≡ 3 (mod 13)
```

`M = 7 × 11 × 13 = 1001`

| i | aᵢ | mᵢ | Mᵢ | Mᵢ mod mᵢ | Cálculo do inverso | M'ᵢ |
|---|---|---|---|---|---|---|
| 1 | 3 | 7 | 143 | 3 | `3·5 = 15 ≡ 1 (mod 7)` | **5** |
| 2 | 2 | 11 | 91 | 3 | `3·4 = 12 ≡ 1 (mod 11)` | **4** |
| 3 | 3 | 13 | 77 | 12 | `12·12 = 144 ≡ 1 (mod 13)` | **12** |

```
x = 3·143·5 + 2·91·4 + 3·77·12
x = 2145 + 728 + 2772 = 5645
5645 = 5·1001 + 640  →  x ≡ 640 (mod 1001)
```

**A senha recuperada é s = 640** ✓

### Por que funciona para qualquer trio

Existem `C(5,3) = 10` trios possíveis. O menor produto de módulos é `7·11·13 = 1001 > 640`, portanto **qualquer** trio recupera `s = 640` de forma única (todos os 10 trios foram verificados).

Já **dois** funcionários não conseguem: o maior produto de dois módulos é `17 × 19 = 323 < 640`. A dupla obteria apenas `640 mod 323 = 317`, isto é `x = 317 + 323k`. Dentro do intervalo do limiar `(323, 1001)` restam os candidatos **640 e 963** — impossível decidir qual é a senha. Isso confirma o limiar `k = 3`.

### Resposta

> **S = {(7,3), (11,2), (13,3), (17,11), (19,13)}**, e três funcionários quaisquer resolvem o sistema de congruências correspondente pelo TCR, obtendo **s = 640**.

---

## Questão 7 — Macro empresa com 6 gerentes (k = 3)

### (a) Construção das chaves

**Dados:** `L = {11, 13, 15, 17, 19, 23}`, `n = 6`, `k = 3`, `s = 1500`

**Coprimalidade dois a dois:** 11, 13, 17, 19 e 23 são primos distintos; `15 = 3 × 5` não compartilha fator com nenhum deles. Logo, todos os pares têm `mdc = 1` ✓ *(observe que o TCR exige apenas coprimalidade dois a dois, não que os elementos sejam primos — por isso o 15 é admissível)*.

**Verificação do limiar `k = 3`:**
- `N` = produto dos 3 **menores** = `11 × 13 × 15 = 2145`
- `M` = produto dos 2 **maiores** = `19 × 23 = 437`
- `437 < 1500 < 2145` ✓ → a senha `s = 1500` é válida para o limiar 3

**Chaves `(p, s_p)` com `s_p = 1500 mod p`:**

| Gerente | p | Divisão | s_p | Chave |
|---|---|---|---|---|
| G1 | 11 | `1500 = 136·11 + 4` | 4 | **(11, 4)** |
| G2 | 13 | `1500 = 115·13 + 5` | 5 | **(13, 5)** |
| G3 | 15 | `1500 = 100·15 + 0` | 0 | **(15, 0)** |
| G4 | 17 | `1500 = 88·17 + 4` | 4 | **(17, 4)** |
| G5 | 19 | `1500 = 78·19 + 18` | 18 | **(19, 18)** |
| G6 | 23 | `1500 = 65·23 + 5` | 5 | **(23, 5)** |

```
S = {(11,4), (13,5), (15,0), (17,4), (19,18), (23,5)}
```

### (b) Recuperação da senha com 3 chaves aleatórias

**Escolha 1 — gerentes G2, G4 e G6: chaves (13,5), (17,4) e (23,5)**

```
x ≡ 5 (mod 13)
x ≡ 4 (mod 17)
x ≡ 5 (mod 23)
```

`M = 13 × 17 × 23 = 5083`

| i | aᵢ | mᵢ | Mᵢ | Mᵢ mod mᵢ | Cálculo do inverso | M'ᵢ |
|---|---|---|---|---|---|---|
| 1 | 5 | 13 | 391 | 1 | `1·1 ≡ 1 (mod 13)` | **1** |
| 2 | 4 | 17 | 299 | 10 | `10·12 = 120 = 7·17 + 1 ≡ 1 (mod 17)` | **12** |
| 3 | 5 | 23 | 221 | 14 | `14·5 = 70 = 3·23 + 1 ≡ 1 (mod 23)` | **5** |

```
x = 5·391·1 + 4·299·12 + 5·221·5
x = 1955 + 14352 + 5525 = 21832
21832 = 4·5083 + 1500  →  x ≡ 1500 (mod 5083)
```

**s = 1500** ✓

**Escolha 2 — gerentes G1, G3 e G5: chaves (11,4), (15,0) e (19,18)** *(trio com o menor produto após o mínimo, incluindo o módulo não primo)*

```
x ≡  4 (mod 11)
x ≡  0 (mod 15)
x ≡ 18 (mod 19)
```

`M = 11 × 15 × 19 = 3135`

| i | aᵢ | mᵢ | Mᵢ | Mᵢ mod mᵢ | Cálculo do inverso | M'ᵢ |
|---|---|---|---|---|---|---|
| 1 | 4 | 11 | 285 | 10 | `10·10 = 100 = 9·11 + 1 ≡ 1 (mod 11)` | **10** |
| 2 | 0 | 15 | 209 | 14 | `14·14 = 196 = 13·15 + 1 ≡ 1 (mod 15)` | **14** |
| 3 | 18 | 19 | 165 | 13 | `13·3 = 39 = 2·19 + 1 ≡ 1 (mod 19)` | **3** |

```
x = 4·285·10 + 0·209·14 + 18·165·3
x = 11400 + 0 + 8910 = 20310
20310 = 6·3135 + 1500  →  x ≡ 1500 (mod 3135)
```

**s = 1500** ✓ — confirmado, como pedido no enunciado.

### Conferência da consistência

`1500 mod 11 = 4` ✓ · `1500 mod 13 = 5` ✓ · `1500 mod 15 = 0` ✓ · `1500 mod 17 = 4` ✓ · `1500 mod 19 = 18` ✓ · `1500 mod 23 = 5` ✓

Existem `C(6,3) = 20` trios possíveis e **todos** recuperam `s = 1500` (verificado computacionalmente), pois o menor produto de três módulos é `11 × 13 × 15 = 2145 > 1500`.

### Segurança: por que 2 chaves não bastam

O maior produto de duas chaves é `19 × 23 = 437 < 1500`. Dois gerentes obteriam apenas `x ≡ 189 (mod 437)`, isto é `x = 189 + 437k`. Dentro do intervalo do limiar `(437, 2145)` restam **quatro** candidatos — `626, 1063, 1500 e 1937` — sem meio de identificar a senha correta. O limiar `k = 3` está, portanto, corretamente estabelecido.

### Resposta

> **(a)** `S = {(11,4), (13,5), (15,0), (17,4), (19,18), (23,5)}` — uma chave por gerente.
> **(b)** Quaisquer 3 chaves, resolvidas pelo TCR, devolvem **s = 1500**. Exemplos verificados: `{(13,5),(17,4),(23,5)}` → 1500 (mod 5083) e `{(11,4),(15,0),(19,18)}` → 1500 (mod 3135).

---

## Quadro-resumo das respostas

| Questão | Sistema / Dados | Módulo M | Resposta |
|---|---|---|---|
| 1 | `x ≡ 2(13), 5(15), 8(19)` | 3705 | **3200 horas** (133 dias e 8 h) |
| 2 | `x ≡ 2(5), 4(7), 5(11)` | 385 | **137** |
| 3 | `x ≡ 5(7), 4(9), 1(10)` | 630 | 1741 sobreviventes → **259 mortos** |
| 4 | `x ≡ 3(5), 2(3), 4(7), 3(4)` | 420 | **263** |
| 5 | `L={7,11,13,17,19}`, k=2 | — | **s = 69** (limiar: 19 < 69 < 77) |
| 6 | `L={7,11,13,17,19}`, k=3, s=640 | 1001 | **S = {(7,3),(11,2),(13,3),(17,11),(19,13)}** |
| 7 | `L={11,13,15,17,19,23}`, k=3, s=1500 | 2145 (mín.) | **S = {(11,4),(13,5),(15,0),(17,4),(19,18),(23,5)}** |

---

*Todos os resultados foram conferidos por substituição direta nas congruências originais e validados pelo script `verificacao.py`, que testa também todos os subconjuntos de chaves das questões 5, 6 e 7.*
