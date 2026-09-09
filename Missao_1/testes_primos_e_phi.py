# =====================================================================
# Testes e demonstracao - Secoes 6 e 7 do Missao01.py
# Numeros Primos e Funcao Phi de Euler
# Integrante: Rafael de Castro
#
# Todos os valores esperados foram retirados do material da disciplina.
# Execute com:  python testes_primos_e_phi.py
# =====================================================================

from Missao01 import (
    Conjunto_Z_Estrela,
    Divisores,
    Eh_Primo,
    Fatorar,
    Lista_De_Primos,
    MDC,
    Phi_de_Euler,
    Phi_de_Produto_De_Primos,
    Phi_por_Definicao,
    Sao_Coprimos,
)


def secao(titulo):
    print()
    print("=" * 68)
    print(titulo)
    print("=" * 68)


# ---------------------------------------------------------------------
secao("1. PRIMALIDADE PELA DEFINICAO  (slide Numeros Primos)")

for n in (2, 3, 5, 7, 11):
    assert Eh_Primo(n), n
for n in (0, 1, 4, 91, 11011, 24200):
    assert not Eh_Primo(n), n

print("Primos do material (2, 3, 5, 7, 11) reconhecidos.")
print("91 = 7 x 13           -> primo?", Eh_Primo(91))
print("11011 = 7 x 11^2 x 13 -> primo?", Eh_Primo(11011))


# ---------------------------------------------------------------------
secao("2. DIVISORES E LISTAGEM DE PRIMOS  (slide Divisores)")

# "Qualquer inteiro p > 1 e primo se e somente se seus unicos
#  divisores sao 1 e p."
assert Divisores(13) == [1, 13]
assert Divisores(26) == [1, 2, 13, 26]
assert Divisores(91) == [1, 7, 13, 91]
assert Lista_De_Primos(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert len(Lista_De_Primos(100)) == 25

print("Divisores de 13:", Divisores(13), "-> so 1 e ele mesmo, logo primo")
print("Divisores de 26:", Divisores(26))
print("Divisores de 91:", Divisores(91), "-> tem 7 e 13, logo composto")
print("Primos ate 30:", Lista_De_Primos(30))
print("Quantidade de primos ate 100:", len(Lista_De_Primos(100)))


# ---------------------------------------------------------------------
secao("3. FATORACAO EM PRIMOS  (slide Numeros Primos)")

# 24200 = 2^3 x 5^2 x 11^2   e   11011 = 7 x 11^2 x 13
assert Fatorar(24200) == {2: 3, 5: 2, 11: 2}
assert Fatorar(11011) == {7: 1, 11: 2, 13: 1}
assert Fatorar(91) == {7: 1, 13: 1}
assert Fatorar(26) == {2: 1, 13: 1}
assert Fatorar(1) == {}

print("24200 =", Fatorar(24200), " (esperado 2^3 x 5^2 x 11^2)")
print("11011 =", Fatorar(11011), " (esperado 7 x 11^2 x 13)")
print("   91 =", Fatorar(91))

# A fatoracao tem que reconstruir o numero original
for n in range(2, 500):
    produto = 1
    for primo, expoente in Fatorar(n).items():
        produto *= primo ** expoente
    assert produto == n, n
print("O produto dos fatores reconstroi n, para n de 2 a 499.")


# ---------------------------------------------------------------------
secao("4. NUMEROS RELATIVAMENTE PRIMOS  (slide homonimo)")

# "Os numeros 4 e 15 sao primos entre si; 6 e 9 nao sao"
assert Sao_Coprimos(4, 15)
assert not Sao_Coprimos(6, 9)
assert Sao_Coprimos(8, 15)

print("4 e 15 sao coprimos? ", Sao_Coprimos(4, 15))
print("6 e  9 sao coprimos? ", Sao_Coprimos(6, 9))
print("8 e 15 sao coprimos? ", Sao_Coprimos(8, 15), " (exemplo do slide)")


# ---------------------------------------------------------------------
secao("5. FUNCAO PHI DE EULER  (slide Funcao phi de Euler)")

assert Phi_de_Euler(1) == 1
assert Phi_de_Euler(26) == 12       # 26 = 2 x 13 -> (2-1)(13-1) = 12
assert Phi_de_Euler(21) == 12       # (3-1)(7-1) = 2 x 6
assert Phi_de_Euler(8) == 4         # Z*8 = {1, 3, 5, 7}
assert Phi_de_Euler(10) == 4
assert Phi_de_Euler(11) == 10
assert Phi_de_Euler(96) == 32

print("phi(26) =", Phi_de_Euler(26), " (material: 12)")
print("phi(21) =", Phi_de_Euler(21), " (material: 12, com 12 inteiros listados)")
print("phi(8)  =", Phi_de_Euler(8), "  (material: 4)")
print("phi(11) =", Phi_de_Euler(11), " (p primo -> phi(p) = p-1)")

# phi(p*q) = (p-1)(q-1), para p e q primos distintos
assert Phi_de_Produto_De_Primos(3, 7) == 12
assert Phi_de_Produto_De_Primos(7, 17) == 96
print("phi(3 x 7)  =", Phi_de_Produto_De_Primos(3, 7), " (material: 12)")
print("phi(7 x 17) =", Phi_de_Produto_De_Primos(7, 17))

# As duas implementacoes precisam concordar
for n in range(1, 300):
    assert Phi_de_Euler(n) == Phi_por_Definicao(n), n
print("Formula da fatoracao == contagem de coprimos, para n de 1 a 299.")


# ---------------------------------------------------------------------
secao("6. CONJUNTO Z*m  (fundamentos_matematicos.pdf 3.1.9)")

Z26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
assert Conjunto_Z_Estrela(26) == Z26
assert Conjunto_Z_Estrela(8) == [1, 3, 5, 7]

print("Z*26 =", Conjunto_Z_Estrela(26))
print("Z*8  =", Conjunto_Z_Estrela(8))

# Os 12 inteiros de Z*21 estao listados no slide de phi de Euler
assert Conjunto_Z_Estrela(21) == [1, 2, 4, 5, 8, 10, 11, 13, 16, 17, 19, 20]
print("Z*21 =", Conjunto_Z_Estrela(21))
print("       (os 12 inteiros listados no slide)")

# |Z*m| = phi(m) por definicao
for m in range(2, 200):
    assert len(Conjunto_Z_Estrela(m)) == Phi_de_Euler(m), m
print("|Z*m| == phi(m) confirmado para m de 2 a 199.")


# ---------------------------------------------------------------------
secao("7. INTEGRACAO COM A SECAO 2 (MDC - Gabriel Vicentte)")

# Sao_Coprimos, e portanto Phi_por_Definicao e Conjunto_Z_Estrela,
# dependem do MDC da secao 2.
assert MDC(26, 7) == 1
assert MDC(300, 18) == 6
print("MDC(26, 7)   =", MDC(26, 7))
print("MDC(300, 18) =", MDC(300, 18), " (material: 300 = 2^2 x 3 x 5^2 e")
print("                           18 = 2 x 3^2, logo o MDC e 6)")


# ---------------------------------------------------------------------
print()
print("=" * 68)
print("TODOS OS TESTES PASSARAM.")
print("=" * 68)
