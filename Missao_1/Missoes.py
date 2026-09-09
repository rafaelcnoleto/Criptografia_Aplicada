# Aritmetica Modular

def Soma_Modular(a, b, n):
    return (a + b) % n

def Subtracao_Modular(a, b, n):
    return (a - b) % n

def Multiplicacao_Modular(a, b, n):
    return (a * b) % n

def Divisao_Modular(a, b, n):
    try:
        inverso = pow(b, -1, n)
        return Multiplicacao_Modular(a, inverso, n)
    except ValueError:
        return "A divisão não existe (b e n não são coprimos)"

# MDC

def MDC(a, b):
    if b == 0:
        return a
    else:
        return MDC(b, a % b)

# Algoritmo de Euclides (para calcular o MDC)

def Algoritmo_de_Euclides(a, b):
    return MDC(a, b)