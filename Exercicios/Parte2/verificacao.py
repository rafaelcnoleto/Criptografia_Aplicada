#!/usr/bin/env python3
"""
Verificacao dos Exercicios de Aprendizagem - Parte 2
Teorema Chines do Resto e Partilha de Senha.

Reproduz o metodo da secao 3.4 de fundamentos_matematicos.pdf:
    x = SUM(a_i * M_i * M'_i) mod M,  com M_i = M/m_i  e  M'_i = M_i^-1 mod m_i

Uso: python3 verificacao.py
"""

from itertools import combinations
from math import gcd, prod


def tcr(congruencias):
    """Resolve x = a_i (mod m_i). Retorna (x, M, passos) com os passos detalhados."""
    modulos = [m for _, m in congruencias]
    for a, b in combinations(modulos, 2):
        assert gcd(a, b) == 1, f"modulos {a} e {b} nao sao coprimos"

    M = prod(modulos)
    passos, x = [], 0
    for a, m in congruencias:
        Mi = M // m
        Mli = pow(Mi, -1, m)          # inverso modular (Euclides estendido)
        termo = a * Mi * Mli
        passos.append((a, m, Mi, Mi % m, Mli, termo))
        x += termo
    return x % M, M, passos


def exibir(titulo, congruencias):
    x, M, passos = tcr(congruencias)
    print(f"\n{titulo}")
    print(f"  M = {' x '.join(str(m) for _, m in congruencias)} = {M}")
    for a, m, Mi, Mi_red, Mli, termo in passos:
        print(f"    a={a:>3}  m={m:>3}  Mi={Mi:>6}  Mi mod m={Mi_red:>3}"
              f"  M'i={Mli:>3}  ->  {a}*{Mi}*{Mli} = {termo}")
    print(f"  soma = {sum(p[5] for p in passos)}  =>  x = {x} (mod {M})")
    return x, M


def limiar(L, k):
    """N = produto dos k menores; M = produto dos k-1 maiores. Valido se M < s < N."""
    ordenado = sorted(L)
    return prod(ordenado[:k]), prod(ordenado[-(k - 1):])


def gerar_S(L, s):
    """Conjunto gerador de senhas: pares (p, s mod p)."""
    return {p: s % p for p in L}


# ----------------------------------------------------------------------
print("=" * 70)
print("Q1 - Tres satelites sobre o Rio")
x1, _ = exibir("  x = 2 (mod 13), 5 (mod 15), 8 (mod 19)", [(2, 13), (5, 15), (8, 19)])
assert (x1 % 13, x1 % 15, x1 % 19) == (2, 5, 8)
print(f"  RESPOSTA: {x1} horas apos a meia-noite = {x1 // 24} dias e {x1 % 24} horas")

print("=" * 70)
print("Q2 - Menor inteiro positivo com restos 2, 4 e 5")
x2, _ = exibir("  x = 2 (mod 5), 4 (mod 7), 5 (mod 11)", [(2, 5), (4, 7), (5, 11)])
assert (x2 % 5, x2 % 7, x2 % 11) == (2, 4, 5)
print(f"  RESPOSTA: x = {x2}")

print("=" * 70)
print("Q3 - O general chines (2000 soldados, mais de 1500 na formatura)")
x3, M3 = exibir("  x = 5 (mod 7), 4 (mod 9), 1 (mod 10)", [(5, 7), (4, 9), (1, 10)])
sobreviventes = [x3 + k * M3 for k in range(10) if 1500 < x3 + k * M3 <= 2000]
assert len(sobreviventes) == 1, sobreviventes
vivos = sobreviventes[0]
assert (vivos % 7, vivos % 9, vivos % 10) == (5, 4, 1)
print(f"  solucao geral: x = {x3} + {M3}k  ->  unica em (1500, 2000]: {vivos}")
print(f"  RESPOSTA: {vivos} sobreviventes, logo 2000 - {vivos} = {2000 - vivos} mortos")

print("=" * 70)
print("Q4 - Sistema de quatro congruencias")
print("  reducao: 5 = 2 (mod 3)  e  11 = 4 (mod 7)")
x4, _ = exibir("  x = 3 (mod 5), 2 (mod 3), 4 (mod 7), 3 (mod 4)",
               [(3, 5), (2, 3), (4, 7), (3, 4)])
assert (x4 % 5, x4 % 3, x4 % 7, x4 % 4) == (3, 5 % 3, 11 % 7, 3)
print(f"  RESPOSTA: x = {x4}")

print("=" * 70)
print("Q5 - Cofre da empresa X (k = 2)")
S5 = {7: 6, 11: 3, 13: 4, 17: 1, 19: 12}
L5, k5 = list(S5), 2
N5, M5 = limiar(L5, k5)
print(f"  L = {L5},  N = {N5},  M = {M5}  ->  intervalo do limiar: {M5} < s < {N5}")
senha5 = [s for s in range(M5 + 1, N5) if all(s % p == r for p, r in S5.items())]
assert len(senha5) == 1
exibir("  usando os pares (7,6) e (11,3):", [(6, 7), (3, 11)])
for par in combinations(S5.items(), 2):
    x, _, _ = tcr([(r, p) for p, r in par])
    assert x == senha5[0], par
print(f"  todos os C(5,2) = {len(list(combinations(L5, 2)))} pares recuperam a mesma senha")
print(f"  RESPOSTA: s = {senha5[0]}")

print("=" * 70)
print("Q6 - Banco TAMBURETE (k = 3, s = 640)")
L6, k6, s6 = [7, 11, 13, 17, 19], 3, 640
N6, M6 = limiar(L6, k6)
print(f"  N = {N6} (3 menores),  M = {M6} (2 maiores)  ->  {M6} < {s6} < {N6}: {M6 < s6 < N6}")
S6 = gerar_S(L6, s6)
print(f"  S = {{{', '.join(f'({p},{r})' for p, r in S6.items())}}}")
exibir("  tres funcionarios com (7,3), (11,2) e (13,3):",
       [(S6[7], 7), (S6[11], 11), (S6[13], 13)])
for trio in combinations(L6, k6):
    x, _, _ = tcr([(S6[p], p) for p in trio])
    assert x == s6, trio
print(f"  todos os C(5,3) = {len(list(combinations(L6, k6)))} trios recuperam s = {s6}")
print(f"  com apenas 2 chaves o maior modulo e {M6} < {s6}: senha NAO determinavel")

print("=" * 70)
print("Q7 - Macro empresa, 6 gerentes (k = 3, s = 1500)")
L7, k7, s7 = [11, 13, 15, 17, 19, 23], 3, 1500
assert all(gcd(a, b) == 1 for a, b in combinations(L7, 2)), "L nao e coprimo dois a dois"
N7, M7 = limiar(L7, k7)
print(f"  L coprimo dois a dois (15 = 3*5 nao e primo, mas e admissivel): OK")
print(f"  N = {N7} (3 menores),  M = {M7} (2 maiores)  ->  {M7} < {s7} < {N7}: {M7 < s7 < N7}")
S7 = gerar_S(L7, s7)
print(f"  (a) S = {{{', '.join(f'({p},{r})' for p, r in S7.items())}}}")
exibir("  (b) chaves (13,5), (17,4) e (23,5):", [(S7[13], 13), (S7[17], 17), (S7[23], 23)])
exibir("  (b) chaves (11,4), (15,0) e (19,18):", [(S7[11], 11), (S7[15], 15), (S7[19], 19)])
for trio in combinations(L7, k7):
    x, _, _ = tcr([(S7[p], p) for p in trio])
    assert x == s7, trio
print(f"  todos os C(6,3) = {len(list(combinations(L7, k7)))} trios recuperam s = {s7}")
print(f"  com apenas 2 chaves o maior modulo e {M7} < {s7}: senha NAO determinavel")

print("=" * 70)
print("Todas as verificacoes passaram.")
