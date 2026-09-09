# Missão 1 — "Precisamos de matemática"

PBL **SecureDocs** — TechSecure. Biblioteca de teoria dos números que serve de
base para os mecanismos criptográficos das próximas missões.

Tudo em um arquivo só: **`Missao01.py`**.

## Numeração das seções

As seções seguem a ordem da lista de tópicos do enunciado. Os números
ausentes são os tópicos que os colegas ainda vão incluir.

| # | Tópico | Integrante | Situação |
|---|---|---|---|
| 1 | Aritmética modular | Gabriel Vicentte | ✅ no arquivo |
| 2 | MDC | Gabriel Vicentte | ✅ no arquivo |
| 3 | Algoritmo de Euclides | Gabriel Vicentte | ✅ no arquivo |
| 4 | Algoritmo estendido de Euclides | Pedro Cardoso | a incluir |
| 5 | Inverso multiplicativo | Pedro Cardoso | a incluir |
| **6** | **Números primos** | **Rafael de Castro** | ✅ no arquivo |
| **7** | **Função phi de Euler** | **Rafael de Castro** | ✅ no arquivo |
| 8 | Exponenciação modular | Daniel Carvalho | a incluir |
| 9 | Teorema Chinês do Resto | Daniel Carvalho | a incluir |

## Funções das seções 6 e 7 (Rafael)

### Seção 6 — Números primos

| Função | O que faz | Usa |
|---|---|---|
| `Divisores(n)` | Lista os divisores positivos de n | — |
| `Eh_Primo(n)` | Primalidade pela definição, até √n | — |
| `Fatorar(n)` | Fatoração em primos, `{primo: expoente}` | — |
| `Sao_Coprimos(a, b)` | Verifica MDC(a,b) = 1 | `MDC` (seção 2) |
| `Lista_De_Primos(limite)` | Primos até o limite | — |

### Seção 7 — Função phi de Euler

| Função | O que faz | Usa |
|---|---|---|
| `Phi_de_Euler(n)` | Fórmula ∏(pᵉ − pᵉ⁻¹) via fatoração | `Fatorar` |
| `Phi_por_Definicao(n)` | Contagem de coprimos (valida a anterior) | `Sao_Coprimos` |
| `Conjunto_Z_Estrela(m)` | Lista os elementos de Z*ₘ | `Sao_Coprimos` |
| `Phi_de_Produto_De_Primos(p,q)` | (p−1)(q−1) | `Eh_Primo` |

A única dependência externa é o `MDC` da seção 2, que já está no arquivo.
As seções 6 e 7 não dependem das partes ainda pendentes.

## Testes

```bash
cd Missao_1
python testes_primos_e_phi.py
```

Sem instalar nada. Os valores esperados vêm do material da disciplina:

- `φ(26) = 12`, `φ(21) = 12`, `φ(8) = 4` — slide "Função phi de Euler"
- Os 12 inteiros de Z*₂₁: `{1,2,4,5,8,10,11,13,16,17,19,20}` — mesmo slide
- `Z*₂₆ = {1,3,5,7,9,11,15,17,19,21,23,25}` — `fundamentos_matematicos.pdf` §3.1.9
- `24200 = 2³ · 5² · 11²` e `11011 = 7 · 11² · 13` — slide "Números Primos"
- `8` e `15` relativamente primos — slide "Números Relativamente Primos"
- `mdc(300, 18) = 6` — slide "Divisor Comum e Máximo Divisor Comum"

Além dos valores do material, os testes verificam propriedades gerais: o
produto dos fatores reconstrói `n` para todo n até 499, as duas
implementações de φ concordam até 299, e `|Z*ₘ| = φ(m)` até 199.

## Pendência de integração

`Divisao_Modular` (seção 1) calcula o inverso multiplicativo com
`pow(b, -1, n)`, da biblioteca padrão. Precisa passar a chamar a função da
seção 5 quando ela chegar — o produto da missão é implementar os algoritmos,
não chamar a biblioteca padrão. Está marcado no código com o comentário
`# TROCAR`.

### Observações para o grupo

- `MDC(60, -24)` devolve `-12`. O material afirma `gcd(60,-24) = 12` e
  `gcd(a,0) = |a|` — falta um `abs()` no caso base.
- `Algoritmo_de_Euclides` hoje é só `return MDC(a, b)`, e o `MDC` já *é* o
  algoritmo de Euclides. Dois itens da tabela resolvidos pela mesma função.
  Sugestão: `MDC` pela definição e `Algoritmo_de_Euclides` pelas divisões
  sucessivas, comparando os dois.

## Ligação com as próximas missões

`Phi_de_Produto_De_Primos` é o passo da geração de chaves do RSA:
φ(n) = (p−1)(q−1). Para primos de centenas de bits, o `Eh_Primo`
determinístico deixa de ser viável e entra o teste de Miller-Rabin, que
aparece no `1_RSA.pdf` e ainda não foi dado em sala.
