# =====================================================================
# PBL SecureDocs - TechSecure
# MISSAO 1: "Precisamos de matematica"
#
# Biblioteca de teoria dos numeros do grupo.
#
# ---------------------------------------------------------------------
# NUMERACAO DAS SECOES
# ---------------------------------------------------------------------
# As secoes seguem a ordem da lista de topicos do enunciado:
#
#   1. aritmetica modular         Gabriel Vicentte   [neste arquivo]
#   2. MDC                        Gabriel Vicentte   [neste arquivo]
#   3. algoritmo de Euclides      Gabriel Vicentte   [neste arquivo]
#   4. algoritmo estendido        Pedro Cardoso      [a incluir]
#   5. inverso multiplicativo     Pedro Cardoso      [a incluir]
#   6. numeros primos             Rafael de Castro   [neste arquivo]
#   7. funcao phi de Euler        Rafael de Castro   [neste arquivo]
#   8. exponenciacao modular      Daniel Carvalho    [a incluir]
#   9. Teorema Chines do Resto    Daniel Carvalho    [a incluir]
#
# Os numeros ausentes correspondem aos topicos que ainda serao
# incluidos pelos colegas.
#
# ---------------------------------------------------------------------
# PENDENCIA DE INTEGRACAO
# ---------------------------------------------------------------------
# Divisao_Modular (secao 1) calcula o inverso multiplicativo com
# pow(b, -1, n), da biblioteca padrao. Precisa passar a chamar a funcao
# da secao 5, quando ela chegar - o produto da missao e implementar os
# algoritmos, nao chamar a biblioteca padrao.
#
# ---------------------------------------------------------------------
# REFERENCIAS DO MATERIAL DA DISCIPLINA
# ---------------------------------------------------------------------
#   Introducao_Crip_Teoria_Num.pdf   (aula)
#   Fermat_Grupo_Corpos.pdf          (aula)
#   fundamentos_matematicos.pdf      (consulta)
# =====================================================================


# #####################################################################
#
#   SECAO 1 - ARITMETICA MODULAR
#   Gabriel Vicentte
#
# #####################################################################

def Soma_Modular(a, b, n):
    return (a + b) % n


def Subtracao_Modular(a, b, n):
    return (a - b) % n


def Multiplicacao_Modular(a, b, n):
    return (a * b) % n


def Divisao_Modular(a, b, n):
    # SUBSTITUTO TEMPORARIO: pow(b, -1, n) calcula o inverso
    # multiplicativo pela biblioteca padrao. Trocar pela funcao da
    # secao 5 (Pedro Cardoso).
    try:
        inverso = pow(b, -1, n)
        return Multiplicacao_Modular(a, inverso, n)
    except ValueError:
        return "A divisão não existe (b e n não são coprimos)"


# #####################################################################
#
#   SECAO 2 - MAXIMO DIVISOR COMUM
#   Gabriel Vicentte
#
# #####################################################################

def MDC(a, b):
    if b == 0:
        return a
    else:
        return MDC(b, a % b)


# #####################################################################
#
#   SECAO 3 - ALGORITMO DE EUCLIDES
#   Gabriel Vicentte
#
# #####################################################################

def Algoritmo_de_Euclides(a, b):
    return MDC(a, b)


# #####################################################################
#
#   SECAO 6 - NUMEROS PRIMOS
#   Rafael de Castro
#
# #####################################################################

def Divisores(n):
    """Lista todos os divisores positivos de n.

    Slide "Divisores": diz-se que b != 0 divide a se a = m*b, com
    a, b e m inteiros.
    """
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


def Eh_Primo(n):
    """Teste de primalidade pela definicao dada em sala.

    "Qualquer inteiro p > 1 e um numero primo se e somente se seus
    unicos divisores sao 1 e p."

    Na pratica basta procurar divisores ate a raiz quadrada de n: se
    n = a * b com a <= b, entao a <= raiz(n).

    Deterministico: quando responde, responde com certeza.
    """
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


def Fatorar(n):
    """Fatoracao em primos por divisao por tentativa.

    Slide "Numeros Primos": qualquer inteiro a > 1 pode ser fatorado,
    de forma unica, como a = p1^e1 * p2^e2 * ... * pt^et.

    Retorna um dicionario {primo: expoente}.
    Exemplo do material: 24200 = 2^3 * 5^2 * 11^2
    """
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


def Sao_Coprimos(a, b):
    """Verifica se a e b sao relativamente primos, isto e, MDC(a, b) = 1.

    Slide "Numeros Relativamente Primos": 8 e 15 sao relativamente
    primos. Usa o MDC da secao 2 (Gabriel Vicentte).
    """
    return MDC(a, b) == 1


def Lista_De_Primos(limite):
    """Lista os primos ate 'limite', testando um a um com Eh_Primo.

    Funcao auxiliar, usada para montar exemplos e tabelas.
    """
    return [n for n in range(2, limite + 1) if Eh_Primo(n)]


# #####################################################################
#
#   SECAO 7 - FUNCAO PHI DE EULER
#   Rafael de Castro
#
# #####################################################################

def Phi_de_Euler(n):
    """Funcao phi de Euler pela formula da fatoracao.

    Slide "Funcao phi de Euler": phi(n) e o numero de inteiros
    positivos menores que n e relativamente primos a n.

        phi(m) = produto de (pi^ei - pi^(ei - 1))
    """
    if n < 1:
        raise ValueError("phi(n) exige n >= 1.")
    if n == 1:
        return 1

    resultado = 1
    for primo, expoente in Fatorar(n).items():
        resultado *= primo ** expoente - primo ** (expoente - 1)
    return resultado


def Phi_por_Definicao(n):
    """Funcao phi calculada pela definicao, contando os coprimos.

    Serve para validar Phi_de_Euler. Lenta: percorre todos os inteiros
    de 1 ate n.
    """
    if n < 1:
        raise ValueError("phi(n) exige n >= 1.")
    if n == 1:
        return 1
    return sum(1 for k in range(1, n) if Sao_Coprimos(k, n))


def Conjunto_Z_Estrela(m):
    """Lista os elementos de Z*m: os inteiros de Zm coprimos com m.

    A quantidade de elementos e exatamente phi(m).
    Exemplo: Conjunto_Z_Estrela(26) -> [1, 3, 5, 7, 9, 11, 15, 17,
                                        19, 21, 23, 25]
    """
    if m < 2:
        raise ValueError("Z*m exige m >= 2.")
    return [k for k in range(1, m) if Sao_Coprimos(k, m)]


def Phi_de_Produto_De_Primos(p, q):
    """phi(p*q) = (p-1)(q-1), para p e q primos distintos.

    Slide "Funcao phi de Euler": se p e q sao primos, entao
    phi(pq) = phi(p)phi(q) = (p-1)(q-1). Exemplo do material:
    phi(21) = phi(3)phi(7) = 2 * 6 = 12.
    """
    if not Eh_Primo(p) or not Eh_Primo(q):
        raise ValueError("p e q precisam ser primos.")
    if p == q:
        raise ValueError("p e q precisam ser distintos.")
    return (p - 1) * (q - 1)
