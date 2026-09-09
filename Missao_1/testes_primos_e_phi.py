# =====================================================================
# Testes e demonstracao - Numeros Primos e Phi de Euler
# Integrante: Rafael de Castro
#
# Todos os valores esperados foram retirados do material da disciplina.
# Execute com:  python testes_primos_e_phi.py
# =====================================================================

from Numeros_Primos_e_Phi import (
    Conjunto_Z_Estrela,
    Crivo_de_Eratostenes,
    Eh_Primo,
    Eh_Provavelmente_Primo,
    Exponenciacao_Modular,
    Fatorar,
    Gerar_Primo,
    Miller_Rabin,
    Phi_de_Euler,
    Phi_de_Produto_De_Primos,
    Phi_por_Definicao,
    Probabilidade_De_Ser_Primo,
    Rodadas_Recomendadas,
    Sao_Coprimos,
)


def secao(titulo):
    print()
    print("=" * 68)
    print(titulo)
    print("=" * 68)


# ---------------------------------------------------------------------
secao("1. TESTE DE PRIMALIDADE PELA DEFINICAO  (secao 3.1.5)")

for n in (2, 3, 5, 7, 11):
    assert Eh_Primo(n), n
for n in (0, 1, 4, 91, 11011, 24200):
    assert not Eh_Primo(n), n

print("Primos do material (2, 3, 5, 7, 11) reconhecidos.")
print("91 = 7 x 13          -> primo?", Eh_Primo(91))
print("11011 = 7 x 11^2 x 13 -> primo?", Eh_Primo(11011))


# ---------------------------------------------------------------------
secao("2. CRIVO DE ERATOSTENES")

assert Crivo_de_Eratostenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert Crivo_de_Eratostenes(1) == []
assert len(Crivo_de_Eratostenes(100)) == 25

print("Primos ate 30:", Crivo_de_Eratostenes(30))
print("Quantidade de primos ate 100:", len(Crivo_de_Eratostenes(100)))


# ---------------------------------------------------------------------
secao("3. FATORACAO EM PRIMOS  (secao 3.1.5)")

# 24200 = 2^3 x 5^2 x 11^2   e   11011 = 7 x 11^2 x 13
assert Fatorar(24200) == {2: 3, 5: 2, 11: 2}
assert Fatorar(11011) == {7: 1, 11: 2, 13: 1}
assert Fatorar(91) == {7: 1, 13: 1}
assert Fatorar(26) == {2: 1, 13: 1}
assert Fatorar(1) == {}

print("24200 =", Fatorar(24200), " (esperado 2^3 x 5^2 x 11^2)")
print("11011 =", Fatorar(11011), " (esperado 7 x 11^2 x 13)")
print("   91 =", Fatorar(91))


# ---------------------------------------------------------------------
secao("4. NUMEROS RELATIVAMENTE PRIMOS  (secao 3.1.6)")

# "Os numeros 4 e 15 sao primos entre si; 6 e 9 nao sao"
assert Sao_Coprimos(4, 15)
assert not Sao_Coprimos(6, 9)
assert Sao_Coprimos(8, 15)

print("4 e 15 sao coprimos? ", Sao_Coprimos(4, 15))
print("6 e  9 sao coprimos? ", Sao_Coprimos(6, 9))


# ---------------------------------------------------------------------
secao("5. FUNCAO PHI DE EULER  (secao 3.1.10)")

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

# phi(p*q) = (p-1)(q-1), usado na geracao de chaves do RSA
assert Phi_de_Produto_De_Primos(7, 17) == 96      # exemplo do 1_RSA.pdf
assert Phi_de_Produto_De_Primos(3, 7) == 12
print("phi(7 x 17) =", Phi_de_Produto_De_Primos(7, 17), " (exemplo do RSA: 96)")

# As duas implementacoes precisam concordar
for n in range(1, 300):
    assert Phi_de_Euler(n) == Phi_por_Definicao(n), n
print("Formula da fatoracao == contagem de coprimos, para n de 1 a 299.")


# ---------------------------------------------------------------------
secao("6. CONJUNTO Z*m  (secao 3.1.9)")

Z26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
assert Conjunto_Z_Estrela(26) == Z26
assert Conjunto_Z_Estrela(8) == [1, 3, 5, 7]

print("Z*26 =", Conjunto_Z_Estrela(26))
print("Z*8  =", Conjunto_Z_Estrela(8))

# |Z*m| = phi(m) por definicao
for m in range(2, 200):
    assert len(Conjunto_Z_Estrela(m)) == Phi_de_Euler(m), m
print("|Z*m| == phi(m) confirmado para m de 2 a 199.")


# ---------------------------------------------------------------------
secao("7. TEOREMA DE EULER  (secao 3.6)")

# a^phi(n) = 1 (mod n), com a e n coprimos
for n in (8, 10, 11, 21, 26):
    for a in Conjunto_Z_Estrela(n):
        assert Exponenciacao_Modular(a, Phi_de_Euler(n), n) == 1

print("a^phi(n) = 1 (mod n) verificado para todo a em Z*n, com n em {8,10,11,21,26}.")
print("  3^phi(10) mod 10 =", Exponenciacao_Modular(3, Phi_de_Euler(10), 10), "(material: 3^4 = 81 = 1 mod 10)")
print("  2^phi(11) mod 11 =", Exponenciacao_Modular(2, Phi_de_Euler(11), 11), "(material: 2^10 = 1024 = 1 mod 11)")


# ---------------------------------------------------------------------
secao("8. MILLER-RABIN - exercicio do slide 28 do 1_RSA.pdf")

print("Testar se 91 e primo, com as bases 12, 17, 38 e 39.")
print("Valor real: 91 = 7 x 13, portanto COMPOSTO.")
print()
print("  base | resultado do teste     | conclusao")
print("  -----+------------------------+------------------------------")

resultados = {}
for base in (12, 17, 38, 39):
    passou = Miller_Rabin(91, base)
    resultados[base] = passou
    veredito = "provavelmente primo" if passou else "COMPOSTO"
    nota = "base mentirosa forte" if passou else "base testemunha - detectou"
    print(f"   {base:3d} | {veredito:22s} | {nota}")

# 12, 17 e 38 sao mentirosas fortes para 91; 39 e testemunha.
assert resultados[12] and resultados[17] and resultados[38]
assert not resultados[39]

print()
print("Licao: uma unica rodada nao prova nada. Por isso o teste e repetido")
print("com varias bases aleatorias antes de aceitar um numero como primo.")

assert not Eh_Provavelmente_Primo(91, rodadas=20)
print("Eh_Provavelmente_Primo(91) com 20 rodadas ->", Eh_Provavelmente_Primo(91, rodadas=20))


# ---------------------------------------------------------------------
secao("9. COERENCIA ENTRE OS DOIS TESTES DE PRIMALIDADE")

# O teste probabilistico precisa concordar com o deterministico
divergencias = [n for n in range(2, 2000)
                if Eh_Primo(n) != Eh_Provavelmente_Primo(n, rodadas=12)]
assert divergencias == [], divergencias
print("Eh_Primo e Eh_Provavelmente_Primo concordam para todo n de 2 a 1999.")


# ---------------------------------------------------------------------
secao("10. GERACAO DE PRIMOS  (slides 26 e 27 do 1_RSA.pdf)")

assert Rodadas_Recomendadas(250) == 11
assert Rodadas_Recomendadas(500) == 5
assert round(1 / Probabilidade_De_Ser_Primo(512)) == 177

print("Rodadas recomendadas para 250 bits:", Rodadas_Recomendadas(250), "(tabela: 11)")
print("Rodadas recomendadas para 500 bits:", Rodadas_Recomendadas(500), "(tabela: 5)")
print("P(impar de 512 bits ser primo) = 1 em",
      round(1 / Probabilidade_De_Ser_Primo(512)), "(slide 26: 1/177)")
print()

for bits in (16, 64, 128):
    p = Gerar_Primo(bits)
    assert p.bit_length() == bits
    assert Eh_Provavelmente_Primo(p, rodadas=20)
    print(f"Primo de {bits:3d} bits gerado: {p}")

# Um par (p, q) pronto para o RSA da proxima missao
p = Gerar_Primo(64)
q = Gerar_Primo(64)
print()
print("Par para o RSA:")
print("  p        =", p)
print("  q        =", q)
print("  n = p*q  =", p * q)
print("  phi(n)   =", Phi_de_Produto_De_Primos(p, q))


# ---------------------------------------------------------------------
print()
print("=" * 68)
print("TODOS OS TESTES PASSARAM.")
print("=" * 68)
