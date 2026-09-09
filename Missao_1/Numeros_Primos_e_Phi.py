# =====================================================================
# PBL SecureDocs - MISSAO 1: "Precisamos de matematica"
# Integrante: Rafael de Castro
# Topicos: Funcao Phi de Euler | Numeros Primos
#
# O modulo esta dividido em tres partes, conforme o conteudo ja visto:
#
#   PARTE 1 - NUCLEO DA ENTREGA
#             So usa conteudo dado em sala (Introducao_Crip_Teoria_Num.pdf
#             e Fermat_Grupo_Corpos.pdf). Nao depende de nenhum colega.
#
#   PARTE 2 - APLICACOES DOS TEOREMAS DE FERMAT E EULER
#             Os dois teoremas foram dados em sala, com demonstracao.
#             Usam a exponenciacao modular (Daniel Carvalho), que
#             tambem ja foi vista em sala.
#
#   PARTE 3 - APENDICE: MILLER-RABIN
#             Conteudo de 1_RSA.pdf, AINDA NAO DADO EM SALA. Incluido
#             como preparacao para a geracao de chaves do RSA.
#
# Consulta complementar: fundamentos_matematicos.pdf
# =====================================================================


import math
import random


# ---------------------------------------------------------------------
# DEPENDENCIAS DOS OUTROS INTEGRANTES
# ---------------------------------------------------------------------
# Se o Missoes.py do grupo estiver na mesma pasta, as funcoes dos colegas
# sao usadas automaticamente. Caso contrario, entram os substitutos
# temporarios abaixo, para que este modulo rode sozinho.
#
#   MDC                    -> Gabriel Vicentte  (ja entregue)
#   Exponenciacao_Modular  -> Daniel Carvalho   (usado apenas nas
#                                                PARTES 2 e 3)
# ---------------------------------------------------------------------

try:
    from Missoes import MDC
except ImportError:
    def MDC(a, b):
        """SUBSTITUTO TEMPORARIO - trocar pelo MDC do Gabriel Vicentte."""
        return abs(a) if b == 0 else MDC(b, a % b)

try:
    from Missoes import Exponenciacao_Modular
except ImportError:
    def Exponenciacao_Modular(base, expoente, modulo):
        """SUBSTITUTO TEMPORARIO - trocar pela funcao do Daniel Carvalho.

        Assinatura combinada com o grupo:
            Exponenciacao_Modular(base, expoente, modulo) -> int

        O algoritmo de quadrado e multiplicacao binaria esta no slide
        "Aspectos Computacionais - Exponenciacao" do material de sala.
        """
        return pow(base, expoente, modulo)


# #####################################################################
#
#   PARTE 1 - NUCLEO DA ENTREGA
#   Conteudo dado em sala. Deterministico e sem dependencias.
#
# #####################################################################

# ---------------------------------------------------------------------
# NUMEROS PRIMOS
# ---------------------------------------------------------------------

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
    Custo O(raiz(n)) - instantaneo ate cerca de 10^12, inviavel para
    os primos de centenas de bits usados no RSA.
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
    primos.
    """
    return MDC(a, b) == 1


def Lista_De_Primos(limite):
    """Lista os primos ate 'limite', testando um a um com Eh_Primo.

    Funcao auxiliar, usada para montar exemplos e tabelas.
    """
    return [n for n in range(2, limite + 1) if Eh_Primo(n)]


# ---------------------------------------------------------------------
# FUNCAO PHI DE EULER
# ---------------------------------------------------------------------

def Phi_de_Euler(n):
    """Funcao phi de Euler pela formula da fatoracao.

    Slide "Funcao phi de Euler": phi(n) e o numero de inteiros
    positivos menores que n e relativamente primos a n.

        phi(m) = produto de (pi^ei - pi^(ei - 1))

    Nao depende de nenhum colega: usa apenas Fatorar.
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
    de 1 ate n. Usa o MDC do Gabriel Vicentte.
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


def Phi_de_Produto_De_Primos(p, q, verificar=True):
    """phi(p*q) = (p-1)(q-1), para p e q primos distintos.

    Slide "Funcao phi de Euler": se p e q sao primos, entao
    phi(pq) = phi(p)phi(q) = (p-1)(q-1). Exemplo do material:
    phi(21) = phi(3)phi(7) = 2 * 6 = 12.

    E o atalho usado na geracao de chaves do RSA. Para primos grandes,
    chame com verificar=False: a verificacao usa Eh_Primo, que e
    deterministico mas custa O(raiz(n)).
    """
    if verificar and (not Eh_Primo(p) or not Eh_Primo(q)):
        raise ValueError("p e q precisam ser primos.")
    if p == q:
        raise ValueError("p e q precisam ser distintos.")
    return (p - 1) * (q - 1)


# #####################################################################
#
#   PARTE 2 - APLICACOES DOS TEOREMAS DE FERMAT E EULER
#   Teoremas dados em sala, com demonstracao. Usam a exponenciacao
#   modular do Daniel Carvalho.
#
# #####################################################################

def Verifica_Teorema_de_Euler(a, n):
    """Confere que a^phi(n) = 1 (mod n), para a e n relativamente primos.

    Exemplos do material:
        a = 3, n = 10, phi(10) = 4  -> 3^4  = 81   = 1 mod 10
        a = 2, n = 11, phi(11) = 10 -> 2^10 = 1024 = 1 mod 11
    """
    if not Sao_Coprimos(a, n):
        raise ValueError("O teorema de Euler exige MDC(a, n) = 1.")
    return Exponenciacao_Modular(a, Phi_de_Euler(n), n) == 1


def Verifica_Teorema_de_Fermat(a, p):
    """Confere que a^p = a (mod p), para p primo.

    Slide "Teorema de Fermat", item (i): para todo a inteiro,
    a^p = a (mod p). Exemplos do material:
        p = 5, a = 3  -> 3^5  = 243    = 3 mod 5
        p = 5, a = 10 -> 10^5 = 100000 = 0 mod 5
    """
    if not Eh_Primo(p):
        raise ValueError("O teorema de Fermat exige p primo.")
    return Exponenciacao_Modular(a, p, p) == a % p


def Teste_de_Fermat(n, base):
    """Teste de primalidade derivado do Teorema de Fermat.

    O item (ii) do teorema diz: se p nao divide a, entao
    a^(p-1) = 1 (mod p). A CONTRAPOSITIVA vira um teste:

        se a^(n-1) != 1 (mod n), entao n NAO e primo.

    Retorna False -> n e COMPOSTO (certeza absoluta).
    Retorna True  -> n passou no teste para esta base.

    Atencao: a reciproca do teorema e falsa. Um composto pode passar
    no teste, e nesse caso a base e chamada de mentirosa. Pior ainda,
    existem compostos que passam para TODA base coprima a eles - os
    numeros de Carmichael, sendo 561 = 3 * 11 * 17 o menor deles.
    Por isso este teste sozinho nao serve para o RSA, e o Miller-Rabin
    da PARTE 3 existe.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    if base % n == 0:
        # Base fora do intervalo util; nada a concluir.
        return True

    return Exponenciacao_Modular(base, n - 1, n) == 1


def Eh_Provavelmente_Primo_Fermat(n, rodadas=10):
    """Teste de Fermat repetido com bases aleatorias."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for _ in range(rodadas):
        base = random.randrange(2, n - 1)
        if not Teste_de_Fermat(n, base):
            return False
    return True


# #####################################################################
#
#   PARTE 3 - APENDICE: MILLER-RABIN
#   Conteudo de 1_RSA.pdf (slides 25 a 28), AINDA NAO DADO EM SALA.
#   Incluido como preparacao para a geracao de chaves do RSA, onde os
#   primos tem centenas de bits e Eh_Primo se torna inviavel.
#
# #####################################################################

def Decompor_Em_Potencia_De_Dois(numero):
    """Escreve 'numero' na forma 2^k * m, com m impar. Retorna (k, m)."""
    k = 0
    m = numero
    while m % 2 == 0:
        m //= 2
        k += 1
    return k, m


def Miller_Rabin(n, base):
    """Uma rodada do teste de Miller-Rabin para a base informada.

    Retorna False -> n e COMPOSTO (certeza absoluta).
    Retorna True  -> n e PROVAVELMENTE PRIMO para esta base.

    Diferenca para o teste de Fermat: alem de conferir a^(n-1) = 1,
    o algoritmo acompanha as raizes quadradas de 1 ao longo do
    caminho. Isso derruba os numeros de Carmichael, que enganam o
    teste de Fermat.

    Se n for composto e o teste retornar True, a base e chamada de
    mentirosa forte. O exercicio do slide 28 explora esse caso com
    n = 91 = 7 x 13.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    if base % n == 0:
        return True

    k, m = Decompor_Em_Potencia_De_Dois(n - 1)

    b = Exponenciacao_Modular(base, m, n)
    if b == 1 or b == n - 1:
        return True

    for _ in range(k - 1):
        b = Exponenciacao_Modular(b, 2, n)
        if b == n - 1:
            return True

    return False


def Eh_Provavelmente_Primo(n, rodadas=10):
    """Miller-Rabin repetido com bases aleatorias.

    A probabilidade de um composto passar em todas as rodadas e menor
    que 4^(-rodadas).
    """
    if n < 2:
        return False

    for primo_pequeno in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n == primo_pequeno:
            return True
        if n % primo_pequeno == 0:
            return False

    for _ in range(rodadas):
        base = random.randrange(2, n - 1)
        if not Miller_Rabin(n, base):
            return False
    return True


def Rodadas_Recomendadas(bits):
    """Numero de rodadas do Miller-Rabin para erro abaixo de 2^-80.

    Tabela do slide 27 do 1_RSA.pdf.
    """
    tabela = [(250, 11), (300, 9), (400, 6), (500, 5), (600, 3)]
    for tamanho, rodadas in tabela:
        if bits <= tamanho:
            return rodadas
    return 3


def Probabilidade_De_Ser_Primo(bits):
    """Probabilidade de um impar aleatorio de 'bits' bits ser primo.

    P(p primo) = 2 / ln(p), com p ~ 2^bits  (slide 26 do 1_RSA.pdf).
    Para 512 bits o resultado e aproximadamente 1/177.
    """
    return 2 / (bits * math.log(2))


def Gerar_Primo(bits, rodadas=None):
    """Sorteia um primo provavel com exatamente 'bits' bits.

    O candidato tem o bit mais significativo e o bit menos significativo
    forcados em 1: o primeiro garante o tamanho exato, o segundo garante
    que o numero seja impar.
    """
    if bits < 2:
        raise ValueError("E preciso pelo menos 2 bits.")
    if rodadas is None:
        rodadas = Rodadas_Recomendadas(bits)

    while True:
        candidato = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if Eh_Provavelmente_Primo(candidato, rodadas):
            return candidato
