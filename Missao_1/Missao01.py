# PBL SecureDocs - Missao 1
# 1, 2, 3 - Gabriel Vicentte
# 6, 7    - Rafael de Castro
# 4, 5    - Pedro Cardoso (a incluir)
# 8, 9    - Daniel Carvalho (a incluir)

# 1. Aritmetica Modular

def Soma_Modular(a, b, n):
    return (a + b) % n

def Subtracao_Modular(a, b, n):
    return (a - b) % n

def Multiplicacao_Modular(a, b, n):
    return (a * b) % n

def Divisao_Modular(a, b, n):
    # TROCAR pow(b, -1, n) pelo inverso multiplicativo da secao 5
    try:
        inverso = pow(b, -1, n)
        return Multiplicacao_Modular(a, inverso, n)
    except ValueError:
        return "A divisão não existe (b e n não são coprimos)"

# 2. MDC

def MDC(a, b):
    if b == 0:
        return a
    else:
        return MDC(b, a % b)

# 3. Algoritmo de Euclides (para calcular o MDC)

def Algoritmo_de_Euclides(a, b):
    return MDC(a, b)

# 6. Numeros Primos

# Lista os divisores positivos de n
def Divisores(n):
    if n < 1:
        raise ValueError("Exige n >= 1.")
    encontrados = set()
    d = 1
    while d * d <= n:
        if n % d == 0:
            encontrados.add(d)
            encontrados.add(n // d)
        d += 1
    return sorted(encontrados)

# p > 1 e primo se seus unicos divisores sao 1 e p
# Basta procurar divisores ate a raiz de n
def Eh_Primo(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True

# Fatoracao unica: n = p1^e1 x p2^e2 x ... x pt^et
# Retorna {primo: expoente}. Ex: 24200 = 2^3 x 5^2 x 11^2
def Fatorar(n):
    if n < 1:
        raise ValueError("A fatoracao exige n >= 1.")
    fatores = {}
    restante = n
    expoente = 0
    while restante % 2 == 0:
        restante //= 2
        expoente += 1
    if expoente:
        fatores[2] = expoente
    divisor = 3
    while divisor * divisor <= restante:
        expoente = 0
        while restante % divisor == 0:
            restante //= divisor
            expoente += 1
        if expoente:
            fatores[divisor] = expoente
        divisor += 2
    if restante > 1:
        fatores[restante] = fatores.get(restante, 0) + 1
    return fatores

# a e b sao relativamente primos se MDC(a, b) = 1
def Sao_Coprimos(a, b):
    return MDC(a, b) == 1

# Lista os primos ate o limite
def Lista_De_Primos(limite):
    return [n for n in range(2, limite + 1) if Eh_Primo(n)]

# 7. Funcao Phi de Euler

# phi(n) = quantidade de inteiros positivos menores que n
# e relativamente primos a n
# Formula: phi(m) = produto de (pi^ei - pi^(ei-1))
def Phi_de_Euler(n):
    if n < 1:
        raise ValueError("phi(n) exige n >= 1.")
    if n == 1:
        return 1
    resultado = 1
    for primo, expoente in Fatorar(n).items():
        resultado *= primo ** expoente - primo ** (expoente - 1)
    return resultado

# Mesmo phi, mas contando os coprimos um a um (serve para validar)
def Phi_por_Definicao(n):
    if n < 1:
        raise ValueError("phi(n) exige n >= 1.")
    if n == 1:
        return 1
    return sum(1 for k in range(1, n) if Sao_Coprimos(k, n))

# Z*m = elementos de Zm coprimos com m. A quantidade e phi(m)
def Conjunto_Z_Estrela(m):
    if m < 2:
        raise ValueError("Z*m exige m >= 2.")
    return [k for k in range(1, m) if Sao_Coprimos(k, m)]

# Se p e q sao primos: phi(p*q) = (p-1)(q-1)
def Phi_de_Produto_De_Primos(p, q):
    if not Eh_Primo(p) or not Eh_Primo(q):
        raise ValueError("p e q precisam ser primos.")
    if p == q:
        raise ValueError("p e q precisam ser distintos.")
    return (p - 1) * (q - 1)
