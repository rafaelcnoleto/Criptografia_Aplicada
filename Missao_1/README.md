# Missão 1 — "Precisamos de matemática"

PBL **SecureDocs** — TechSecure. Biblioteca de teoria dos números que serve de
base para os mecanismos criptográficos das próximas missões.

## Divisão do grupo

Tudo vive em um único arquivo: **`Missao01.py`**.

| Integrante | Tópicos | Seção | Situação |
|---|---|---|---|
| Gabriel Vicentte | Aritmética modular, MDC, Algoritmo de Euclides | 1, 2, 3 | ✅ integrado |
| Pedro Cardoso | Inverso multiplicativo, Euclides estendido | 4 | ⏳ pendente |
| Daniel Carvalho | Exponenciação modular, Teorema Chinês do Resto | 5 | ⏳ pendente |
| **Rafael de Castro** | **Função Phi de Euler, Números Primos** | **6, 7, 8, 9** | ✅ integrado |

## Dependências entre as partes

```
seção 2  MDC (Gabriel) ────────────► seção 6  Sao_Coprimos (Rafael)
seção 5  Exp. modular (Daniel) ───► seções 8 e 9  Fermat e Miller-Rabin (Rafael)
seção 4  Inverso mult. (Pedro) ───► seção 1  Divisao_Modular (Gabriel)
```

## Pendências antes da entrega

Dois pontos ainda usam a biblioteca padrão do Python e estão marcados no
código com `SUBSTITUTO TEMPORARIO`. Nenhum pode ficar assim: o produto da
missão é **implementar** os algoritmos.

| Onde | Hoje | Precisa virar | Responsável |
|---|---|---|---|
| Seção 5 — `Exponenciacao_Modular` | `pow(b, e, n)` | quadrado e multiplicação binária | Daniel |
| Seção 1 — `Divisao_Modular` | `pow(b, -1, n)` | `Inverso_Multiplicativo(b, n)` | Pedro |

Assinaturas combinadas:

```python
Exponenciacao_Modular(base, expoente, modulo) -> int
Inverso_Multiplicativo(a, m) -> int
Algoritmo_Estendido_de_Euclides(a, b) -> (d, alfa, beta)   # alfa*a + beta*b = d
```

Basta colar as implementações nas seções 4 e 5 e apagar os substitutos —
o resto do arquivo já chama pelos nomes certos. A seção 12 dos testes avisa
se algum substituto ainda estiver ativo.

### Observações para o grupo

- `MDC(60, -24)` devolve `-12`. O material afirma `gcd(60,-24) = 12` e
  `gcd(a,0) = |a|` — falta um `abs()` no caso base.
- `Algoritmo_de_Euclides` hoje é só `return MDC(a, b)`, e o `MDC` já *é* o
  algoritmo de Euclides. Dois itens da tabela resolvidos pela mesma função.
  Sugestão: `MDC` pela definição e `Algoritmo_de_Euclides` pelas divisões
  sucessivas, comparando os dois.

## Aulas já dadas

O módulo é organizado conforme o conteúdo visto até agora:

| Conteúdo | Onde | Dado em sala? |
|---|---|---|
| Primos, fatoração única, coprimos | `Introducao_Crip_Teoria_Num.pdf` | ✅ |
| φ de Euler e a fórmula do produto | `Introducao`, `Fermat_Grupo_Corpos` | ✅ |
| Teoremas de Euler e de Fermat (com demonstração) | ambos | ✅ |
| Exponenciação modular | `Introducao`, `Fermat_Grupo_Corpos` | ✅ |
| Miller-Rabin / testes de primalidade | só `1_RSA.pdf` | ❌ ainda não |

`fundamentos_matematicos.pdf` é material de consulta, não dado em sala.

## Funções entregues (Rafael)

### Seções 6 e 7 — Núcleo (conteúdo de sala, determinístico)

| Função | O que faz | Depende de |
|---|---|---|
| `Divisores(n)` | Lista os divisores positivos de n | — |
| `Eh_Primo(n)` | Primalidade pela definição, até √n | — |
| `Fatorar(n)` | Fatoração em primos, `{primo: expoente}` | — |
| `Sao_Coprimos(a, b)` | Verifica MDC(a,b) = 1 | MDC |
| `Lista_De_Primos(limite)` | Primos até o limite | — |
| `Phi_de_Euler(n)` | Fórmula ∏(pᵉ − pᵉ⁻¹) via fatoração | — |
| `Phi_por_Definicao(n)` | Contagem de coprimos (valida a anterior) | MDC |
| `Conjunto_Z_Estrela(m)` | Lista os elementos de Z*ₘ | MDC |
| `Phi_de_Produto_De_Primos(p,q)` | (p−1)(q−1) | — |

**Nenhuma função destas seções depende do Daniel.** Os dois tópicos do
Rafael ficam completos mesmo que a exponenciação modular atrase.

### Seção 8 — Aplicações dos teoremas de Fermat e Euler

Os dois teoremas foram dados em sala, com demonstração. Usam a
exponenciação modular da seção 5, que também já foi vista em aula.

| Função | O que faz | Depende de |
|---|---|---|
| `Verifica_Teorema_de_Euler(a, n)` | Confere a^φ(n) ≡ 1 (mod n) | **exp. modular** |
| `Verifica_Teorema_de_Fermat(a, p)` | Confere aᵖ ≡ a (mod p) | **exp. modular** |
| `Teste_de_Fermat(n, base)` | Primalidade pela contrapositiva do teorema | **exp. modular** |
| `Eh_Provavelmente_Primo_Fermat(n, r)` | Fermat com bases aleatórias | **exp. modular** |

### Seção 9 — Apêndice: Miller-Rabin (`1_RSA.pdf`, ainda não dado em sala)

| Função | O que faz |
|---|---|
| `Decompor_Em_Potencia_De_Dois(x)` | Escreve x = 2ᵏ · m com m ímpar |
| `Miller_Rabin(n, base)` | Uma rodada do teste |
| `Eh_Provavelmente_Primo(n, rodadas)` | Miller-Rabin com bases aleatórias |
| `Rodadas_Recomendadas(bits)` | Tabela do slide 27 (erro < 2⁻⁸⁰) |
| `Probabilidade_De_Ser_Primo(bits)` | 2/ln(p) — slide 26 |
| `Gerar_Primo(bits)` | Sorteia primo provável do tamanho pedido |

## Testes

```bash
cd Missao_1
python testes_primos_e_phi.py
```

Os valores esperados vêm do material da disciplina:

- `φ(26) = 12`, `φ(21) = 12`, `φ(8) = 4` — slide "Função phi de Euler"
- `Z*₂₆ = {1,3,5,7,9,11,15,17,19,21,23,25}` — `fundamentos_matematicos.pdf` §3.1.9
- `3⁵ ≡ 3 (mod 5)`, `10⁵ ≡ 0 (mod 5)`, `7¹⁸ ≡ 1 (mod 19)` — slide "Teorema de Fermat"
- `24200 = 2³ · 5² · 11²` e `11011 = 7 · 11² · 13` — slide "Números Primos"
- `φ(7 × 17) = 96` — exemplo do RSA, `1_RSA.pdf` slide 19
- Miller-Rabin sobre 91 com bases 12, 17, 38, 39 — exercício do slide 28
- `P(primo, 512 bits) ≈ 1/177` — slide 26

### Limite do teste de Fermat — o número de Carmichael 561

561 = 3 × 11 × 17 é composto, mas passa no teste de Fermat para
**todas** as bases coprimas a ele:

| | Bases coprimas que se enganam |
|---|---|
| Teste de Fermat | 319 de 319 (**100%**) |
| Miller-Rabin | 9 de 319 |

Repetir rodadas não resolve: nenhuma base coprima denuncia o 561. O teste
de Fermat só o rejeita por acidente, quando sorteia uma base que
compartilha fator com ele — ou seja, quando tropeça na fatoração. É
exatamente por isso que o Miller-Rabin existe.

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
