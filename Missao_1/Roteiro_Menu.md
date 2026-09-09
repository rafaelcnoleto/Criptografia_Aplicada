# Roteiro de testes — Menu Interativo

Valores para usar durante a apresentação. Todos foram executados e
conferidos contra o código.

📘 = exemplo tirado do material da disciplina — bons para usar na frente
do professor, porque ele reconhece o valor esperado.

**Para rodar:** `Missao01.py` e `Menu_Interativo.py` na mesma pasta, e

```bash
python Menu_Interativo.py
```

---

## 1. Aritmética modular

| Op | O que digitar | Resultado |
|---|---|---|
| 1 | `14` `9` `12` | 11 |
| 2 | `5` `8` `12` | 9 |
| 3 | 📘 `11` `15` `26` | 9 |
| 4 | `4` `7` `11` | 10 |
| 4 | `4` `2` `6` | *"A divisão não existe"* — erro tratado |

## 2. MDC e Algoritmo de Euclides

| Op | O que digitar | Resultado |
|---|---|---|
| 5 | 📘 `26` `7` | 1 |
| 5 | 📘 `300` `18` | 6 |
| 6 | `105` `45` | 15 |

## 3. Estendido de Euclides e inverso multiplicativo

| Op | O que digitar | Resultado |
|---|---|---|
| 7 | 📘 `26` `7` | MDC = 1, x = 3, y = −11 |
| 8 | 📘 `7` `26` | 15 — e mostra a verificação `7 × 15 mod 26 = 1` |
| 8 | `3` `11` | 4 |

## 4. Números primos — *Rafael*

| Op | O que digitar | Resultado |
|---|---|---|
| 9 | `28` | `[1, 2, 4, 7, 14, 28]` |
| 9 | `36` | 9 divisores — quadrado perfeito, mostra o `set` evitando a duplicata |
| 10 | `17` | True |
| 10 | 📘 `91` | False (= 7 × 13) |
| 11 | 📘 `24200` | `2³ × 5² × 11²` |
| 11 | 📘 `11011` | `7 × 11² × 13` |
| 12 | 📘 `8` `15` | True |
| 12 | 📘 `6` `9` | False |
| 13 | `30` | 10 primos |

## 5. Função phi de Euler — *Rafael*

| Op | O que digitar | Resultado |
|---|---|---|
| 14 | 📘 `21` | 12 |
| 14 | 📘 `26` | 12 |
| 15 | 📘 `21` | 12 — mesmo valor, contando os coprimos |
| **16** | 📘 `21` | **CONFEREM** — as duas versões lado a lado |
| 17 | `10` | `[1, 3, 7, 9]` + "Quantidade = 4, e phi(10) = 4" |
| 17 | 📘 `21` | os 12 inteiros exatos do slide |
| 18 | 📘 `3` `7` | 12 |
| 18 | 📘 `7` `17` | 96 — exemplo do RSA |

## 6. Exponenciação modular

| Op | O que digitar | Resultado |
|---|---|---|
| 19 | 📘 `84` `250` `263` | 52 |
| 19 | 📘 `11` `7` `13` | 2 |

## 7. Teorema Chinês do Resto

A opção 20 pede **duas listas**, uma de cada vez. Separe por espaço ou
por vírgula.

```
Escolha uma opcao: 20

  Sistema x = a1 (mod m1), x = a2 (mod m2), ...
  restos (a1 a2 ...): 2 3 2
  modulos (m1 m2 ...): 3 5 7
```

| Op | Restos | Módulos | Sistema | Resultado |
|---|---|---|---|---|
| 20 | 📘 `2 3 2` | `3 5 7` | x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7) | **23** |
| 20 | `4 8` | `7 13` | x ≡ 4 (mod 7), x ≡ 8 (mod 13) | 60 |

A quantidade de restos e de módulos precisa ser igual, senão o programa
avisa e volta ao menu.

---

## Mostrando o tratamento de erros

| Digite | O que acontece |
|---|---|
| `abc` em qualquer campo numérico | "Digite um numero inteiro." e pergunta de novo |
| Opção `99` | "Opcao invalida." |
| Op 18 com `4` `6` | "p e q precisam ser primos." |
| Op 8 com `4` `6` | "O inverso modular de 4 mod 6 não existe..." |
| Op 15 ou 17 com `999999999` | avisa que vai demorar e pergunta se continua |

Nada derruba o programa — sempre volta ao menu.

---

## Sequência sugerida para a parte do Rafael (~1 min)

1. **Op 11** → `24200` — a fatoração
2. **Op 16** → `21` — as duas versões de phi e o **CONFEREM**
3. **Op 17** → `21` — os 12 inteiros, iguais aos do slide

Se o professor der um número dele, funciona igual — é a razão de ser
do menu.
