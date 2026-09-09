# =====================================================================
# PBL SecureDocs - MISSAO 1: "Precisamos de matematica"
# Integrante: Rafael de Castro
# Topicos: Funcao Phi de Euler | Numeros Primos
#
# Referencias do material da disciplina:
#   fundamentos_matematicos.pdf  - secoes 3.1.5, 3.1.6, 3.1.9, 3.1.10
#   1_RSA.pdf                    - slides 25 a 28 (Miller-Rabin)
# =====================================================================


import math
import random


# ---------------------------------------------------------------------
# DEPENDENCIAS DOS OUTROS INTEGRANTES
# ---------------------------------------------------------------------
# Se o arquivo Missoes.py do grupo ja estiver na mesma pasta, as funcoes
# dos colegas sao usadas automaticamente. Caso contrario, entram os
# substitutos temporarios abaixo, para que este modulo rode sozinho.
#
#   MDC                    -> Gabriel Vicentte  (usado so em Phi_por_Definicao)
#   Exponenciacao_Modular  -> Daniel Carvalho   (usado no Miller-Rabin)
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
        """
        return pow(base, expoente, modulo)


# =====================================================================
# NUMEROS PRIMOS
# =====================================================================

def Eh_Primo(n):
    """Teste de primalidade pela definicao (secao 3.1.5).

    Um inteiro p >= 2 e primo se seus unicos divisores positivos sao 1 e p.
    Basta testar divisores ate a raiz quadrada de n: se n = a * b com
    a <= b, entao a <= raiz(n).

    Deterministico, mas so viavel para numeros pequenos.
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


def Crivo_de_Eratostenes(limite):
    """Retorna a lista de todos os primos menores ou iguais a 'limite'."""
    if limite < 2:
        return []

    eh_candidato = [True] * (limite + 1)
    eh_candidato[0] = eh_candidato[1] = False

    numero = 2
    while numero * numero <= limite:
        if eh_candidato[numero]:
            # Marca os multiplos de 'numero' comecando em numero^2:
            # os menores ja foram marcados por primos anteriores.
            for multiplo in range(numero * numero, limite + 1, numero):
                eh_candidato[multiplo] = False
        numero += 1

    return [n for n, primo in enumerate(eh_candidato) if primo]


def Fatorar(n):
    """Fatoracao em primos por divisao por tentativa.

    Retorna um dicionario {primo: expoente}, correspondente ao produto
    p1^e1 * p2^e2 * ... * pt^et do Teorema Fundamental da Aritmetica.

    Exemplo: Fatorar(24200) -> {2: 3, 5: 2, 7: 1, 11: 2}
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
    """Verifica se a e b sao relativamente primos, isto e, MDC(a, b) = 1."""
    return MDC(a, b) == 1


def Decompor_Em_Potencia_De_Dois(numero):
    """Escreve 'numero' na forma 2^k * m, com m impar. Retorna (k, m).

    Usado pelo Miller-Rabin, que decompoe n - 1 dessa maneira.
    """
    k = 0
    m = numero
    while m % 2 == 0:
        m //= 2
        k += 1
    return k, m


def Miller_Rabin(n, base):
    """Uma rodada do teste de Miller-Rabin para a base informada.

    Retorna False  -> n e COMPOSTO (certeza absoluta).
    Retorna True   -> n e PROVAVELMENTE PRIMO para esta base.

    Atencao: True nao prova primalidade. Se n for composto e o teste
    retornar True, a base e chamada de "mentirosa forte" para n.
    O exercicio do slide 28 do 1_RSA.pdf explora exatamente esse caso
    com n = 91 = 7 x 13.

    Esta e a unica funcao do topico que depende da exponenciacao
    modular do Daniel Carvalho.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    if base % n == 0:
        # Base fora do intervalo util 1 <= a <= n-1; nada a concluir.
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

    Depende do Miller-Rabin e, portanto, da exponenciacao modular.
    """
    if bits < 2:
        raise ValueError("E preciso pelo menos 2 bits.")
    if rodadas is None:
        rodadas = Rodadas_Recomendadas(bits)

    while True:
        candidato = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if Eh_Provavelmente_Primo(candidato, rodadas):
            return candidato


# =====================================================================
# FUNCAO PHI DE EULER
# =====================================================================

def Phi_de_Euler(n):
    """Funcao phi de Euler pela formula da fatoracao (secao 3.1.10).

        phi(m) = produto de (pi^ei - pi^(ei - 1))

    phi(n) conta quantos inteiros positivos menores que n sao
    relativamente primos a n, ou seja, e a quantidade de elementos
    de Z*n.

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

    A quantidade de elementos e exatamente phi(m) (secao 3.1.9).
    Exemplo: Conjunto_Z_Estrela(26) -> [1, 3, 5, 7, 9, 11, 15, 17,
                                        19, 21, 23, 25]
    """
    if m < 2:
        raise ValueError("Z*m exige m >= 2.")
    return [k for k in range(1, m) if Sao_Coprimos(k, m)]


def Phi_de_Produto_De_Primos(p, q):
    """phi(p*q) = (p-1)(q-1), para p e q primos distintos.

    Atalho usado na geracao de chaves do RSA. Levanta erro se as
    hipoteses nao valerem, para nao mascarar uso indevido.

    A verificacao usa Eh_Provavelmente_Primo, e nao Eh_Primo: os primos
    do RSA tem centenas de bits, e a divisao por tentativa levaria mais
    de 2^256 operacoes. E exatamente o motivo de o Miller-Rabin existir.
    """
    if not Eh_Provavelmente_Primo(p) or not Eh_Provavelmente_Primo(q):
        raise ValueError("p e q precisam ser primos.")
    if p == q:
        raise ValueError("p e q precisam ser distintos.")
    return (p - 1) * (q - 1)
