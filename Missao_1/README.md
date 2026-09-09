# Missão 1 — "Precisamos de matemática"

PBL **SecureDocs** — TechSecure. Biblioteca de teoria dos números que serve de
base para os mecanismos criptográficos das próximas missões.

## Divisão do grupo

| Integrante | Tópicos | Arquivo |
|---|---|---|
| Gabriel Vicentte | Aritmética modular, MDC, Algoritmo de Euclides | `Missoes.py` |
| **Rafael de Castro** | **Função Phi de Euler, Números Primos** | **`Numeros_Primos_e_Phi.py`** |
| Pedro Cardoso | Inverso multiplicativo, Algoritmo estendido de Euclides | *pendente* |
| Daniel Carvalho | Exponenciação modular, Teorema Chinês do Resto | *pendente* |

## Dependências entre as partes

```
Gabriel (MDC) ──────────────► Rafael (Phi_por_Definicao, Sao_Coprimos)
Daniel (Exponenciacao_Modular) ─► Rafael (Miller_Rabin, Gerar_Primo)
Pedro (Inverso_Multiplicativo) ─► Gabriel (Divisao_Modular)
Daniel (Exponenciacao_Modular) ─► Pedro / Daniel (TCR)
```

O arquivo `Numeros_Primos_e_Phi.py` importa as funções dos colegas de
`Missoes.py` quando elas existem, e usa substitutos temporários quando não.
Ao integrar tudo em um único `Missoes.py`, os blocos `try/except ImportError`
resolvem sozinhos — basta remover os substitutos.

**Pendência de integração:** `Exponenciacao_Modular` está usando o `pow()`
nativo do Python como substituto. Precisa ser trocado pela implementação do
Daniel (quadrado e multiplicação binária) antes da entrega, porque o produto
da missão é implementar o algoritmo, não chamar a biblioteca padrão.

Assinatura combinada: `Exponenciacao_Modular(base, expoente, modulo) -> int`

## Funções entregues (Rafael)

### Números primos
| Função | O que faz | Depende de |
|---|---|---|
| `Eh_Primo(n)` | Primalidade pela definição, até √n | — |
| `Crivo_de_Eratostenes(limite)` | Todos os primos ≤ limite | — |
| `Fatorar(n)` | Fatoração em primos, retorna `{primo: expoente}` | — |
| `Sao_Coprimos(a, b)` | Verifica MDC(a,b) = 1 | MDC |
| `Decompor_Em_Potencia_De_Dois(x)` | Escreve x = 2^k · m com m ímpar | — |
| `Miller_Rabin(n, base)` | Uma rodada do teste probabilístico | **exp. modular** |
| `Eh_Provavelmente_Primo(n, rodadas)` | Miller-Rabin com bases aleatórias | **exp. modular** |
| `Rodadas_Recomendadas(bits)` | Tabela do slide 27 (erro < 2⁻⁸⁰) | — |
| `Probabilidade_De_Ser_Primo(bits)` | 2/ln(p) — slide 26 | — |
| `Gerar_Primo(bits)` | Sorteia primo provável do tamanho pedido | **exp. modular** |

### Função phi de Euler
| Função | O que faz | Depende de |
|---|---|---|
| `Phi_de_Euler(n)` | Fórmula ∏(pᵉ − pᵉ⁻¹) via fatoração | — |
| `Phi_por_Definicao(n)` | Contagem de coprimos (valida a anterior) | MDC |
| `Conjunto_Z_Estrela(m)` | Lista os elementos de Z*ₘ | MDC |
| `Phi_de_Produto_De_Primos(p, q)` | (p−1)(q−1) — atalho do RSA | **exp. modular** |

## Testes

```bash
cd Missao_1
python testes_primos_e_phi.py
```

Os valores esperados vêm do material da disciplina:

- `φ(26) = 12`, `φ(21) = 12`, `φ(8) = 4` — `fundamentos_matematicos.pdf` §3.1.10
- `Z*₂₆ = {1,3,5,7,9,11,15,17,19,21,23,25}` — §3.1.9
- `24200 = 2³ · 5² · 11²` e `11011 = 7 · 11² · 13` — §3.1.5
- `φ(7 × 17) = 96` — exemplo do RSA, `1_RSA.pdf` slide 19
- Miller-Rabin sobre 91 com bases 12, 17, 38, 39 — exercício do slide 28
- `P(primo, 512 bits) ≈ 1/177` — slide 26

### Resultado do exercício do slide 28

Testando 91 (= 7 × 13, composto):

| Base | Resultado | Conclusão |
|---|---|---|
| 12 | provavelmente primo | mentirosa forte |
| 17 | provavelmente primo | mentirosa forte |
| 38 | provavelmente primo | mentirosa forte |
| 39 | **composto** | testemunha — detectou |

Três das quatro bases *erram*. É a demonstração de que Miller-Rabin é
probabilístico: uma rodada não prova nada, e por isso o teste é repetido com
várias bases aleatórias antes de aceitar um número como primo.

## Ligação com a Missão 2

`Gerar_Primo` e `Phi_de_Produto_De_Primos` são exatamente o primeiro passo da
geração de chaves do RSA: sortear p e q, calcular n = p·q e φ(n) = (p−1)(q−1).
