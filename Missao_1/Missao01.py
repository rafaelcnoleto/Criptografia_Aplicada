# ==============================================================================
# BIBLIOTECA MATEMÁTICA PARA CRIPTOGRAFIA - SECUREDOCS (MISSAO 1)
# ==============================================================================

# --- 1. ARITMÉTICA MODULAR ---

def Soma_Modular(a, b, n):
    return (a + b) % n

def Subtracao_Modular(a, b, n):
    return (a - b) % n

def Multiplicacao_Modular(a, b, n):
    return (a * b) % n

def Divisao_Modular(a, b, n):
    try:
        # Utiliza a sua própria implementação do algoritmo estendido abaixo
        inverso = inverso_multiplicativo(b, n)
        return Multiplicacao_Modular(a, inverso, n)
    except ValueError:
        return "A divisão não existe (b e n não são coprimos)"


# --- 2. MDC E ALGORITMO DE EUCLIDES ---

def MDC(a, b):
    if b == 0:
        return a
    else:
        return MDC(b, a % b)

def Algoritmo_de_Euclides(a, b):
    return MDC(a, b)


# --- 3. ALGORITMO ESTENDIDO DE EUCLIDES E INVERSO MULTIPLICATIVO ---

def algoritmo_estendido_euclides(a: int, b: int) -> tuple[int, int, int]:
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    
    while b != 0:
        quociente = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - quociente * x1
        y0, y1 = y1, y0 - quociente * y1
        
    return a, x0, y0

def inverso_multiplicativo(a: int, m: int) -> int:
    mdc, x, _ = algoritmo_estendido_euclides(a, m)
    
    if mdc != 1:
        raise ValueError(f"O inverso modular de {a} mod {m} não existe, pois mdc({a}, {m}) = {mdc} != 1.")
    
    # Garante que o resultado esteja no intervalo [0, m - 1]
    return x % m


# --- 4. NÚMEROS PRIMOS ---

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

def Sao_Coprimos(a, b):
    return MDC(a, b) == 1

def Lista_De_Primos(limite):
    return [n for n in range(2, limite + 1) if Eh_Primo(n)]


# --- 5. FUNÇÃO PHI DE EULER ---

def Phi_de_Euler(n):
    if n < 1:
        raise ValueError("phi(n) exige n >= 1.")
    if n == 1:
        return 1
    resultado = 1
    for primo, expoente in Fatorar(n).items():
        resultado *= primo ** expoente - primo ** (expoente - 1)
    return resultado

def Phi_por_Definicao(n):
    if n < 1:
        raise ValueError("phi(n) exige n >= 1.")
    if n == 1:
        return 1
    return sum(1 for k in range(1, n) if Sao_Coprimos(k, n))

def Conjunto_Z_Estrela(m):
    if m < 2:
        raise ValueError("Z*m exige m >= 2.")
    return [k for k in range(1, m) if Sao_Coprimos(k, m)]

def Phi_de_Produto_De_Primos(p, q):
    if not Eh_Primo(p) or not Eh_Primo(q):
        raise ValueError("p e q precisam ser primos.")
    if p == q:
        raise ValueError("p e q precisam ser distintos.")
    return (p - 1) * (q - 1)


# --- 6. EXPONENCIAÇÃO MODULAR ---

def exponenciacao_modular(base, expoente, modulo):
    expoente_binario = bin(expoente)[2:]
    d = 1
    for bit in expoente_binario:
        d = (d * d) % modulo
        if bit == '1':
            d = (d * base) % modulo
    return d


# --- 7. TEOREMA CHINÊS DO RESTO ---

def inverso_modular(a, m):
    m_original = m
    y = 0
    x = 1
    while a > 1:
        quociente = a // m
        resto = a % m
        a = m
        m = resto
        t = y
        y = x - quociente * y
        x = t
    if x < 0:
        x = x + m_original
    return x

def teorema_chines_resto(restos, modulos):
    M_total = 1
    for m in modulos:
        M_total = M_total * m
        
    resultado_final = 0
    for i in range(len(modulos)):      
        Mi = M_total // modulos[i] 
        M_linha = inverso_modular(Mi, modulos[i])
        resultado_final += restos[i] * Mi * M_linha
        
    return resultado_final % M_total


# ==============================================================================
# BLOCO DE TESTES DE VALIDAÇÃO (IMPRESSÃO DA TELA)
# ==============================================================================
if __name__ == "__main__":
    print("====== INICIANDO TESTES DA BIBLIOTECA MATEMÁTICA ======\n")

    # 1. Testes de Aritmética Modular
    print("--- 1. Aritmética Modular ---")
    print(f"Soma Modular (14 + 9 mod 12): {Soma_Modular(14, 9, 12)} | Esperado: 11")
    print(f"Subtração Modular (5 - 8 mod 12): {Subtracao_Modular(5, 8, 12)} | Esperado: 9")
    print(f"Multiplicação Modular (5 * 5 mod 12): {Multiplicacao_Modular(5, 5, 12)} | Esperado: 1")
    print(f"Divisão Modular (4 / 7 mod 11): {Divisao_Modular(4, 7, 11)} | Esperado: 10")
    print(f"Divisão Modular impossível (4 / 2 mod 6): {Divisao_Modular(4, 2, 6)} | Esperado: Mensagem de erro\n")

    # 2. Testes de MDC e Euclides
    print("--- 2. MDC e Algoritmo de Euclides ---")
    print(f"MDC normal (50, 20): {MDC(50, 20)} | Esperado: 10")
    print(f"MDC via Euclides (105, 45): {Algoritmo_de_Euclides(105, 45)} | Esperado: 15\n")

    # 3. Testes do Algoritmo Estendido e Inverso Multiplicativo
    print("--- 3. Algoritmo Estendido e Inverso ---")
    mdc_e, x, y = algoritmo_estendido_euclides(3, 11)
    print(f"Estendido (3, 11) -> MDC: {mdc_e}, Coeficiente x: {x}, Coeficiente y: {y} | Esperado MDC=1")
    print(f"Inverso Multiplicativo (3 mod 11): {inverso_multiplicativo(3, 11)} | Esperado: 4 (pois 3*4 = 12 = 1 mod 11)\n")

    # 4. Testes de Números Primos
    print("--- 4. Números Primos e Fatoração ---")
    print(f"Divisores de 28: {Divisores(28)}")
    print(f"O número 17 é primo? {Eh_Primo(17)} | Esperado: True")
    print(f"O número 20 é primo? {Eh_Primo(20)} | Esperado: False")
    print(f"Fatoração de 24200: {Fatorar(24200)} | Esperado: {{2: 3, 5: 2, 11: 2}}")
    print(f"9 e 14 são coprimos? {Sao_Coprimos(9, 14)} | Esperado: True")
    print(f"Primos até 30: {Lista_De_Primos(30)}\n")

    # 5. Testes da Função Phi de Euler
    print("--- 5. Função Phi de Euler ---")
    print(f"Phi de Euler por Fatoração (phi(10)): {Phi_de_Euler(10)} | Esperado: 4")
    print(f"Phi de Euler por Definição (phi(10)): {Phi_por_Definicao(10)} | Esperado: 4")
    print(f"Conjunto Z* de 10: {Conjunto_Z_Estrela(10)}")
    print(f"Phi de Produto de Primos (p=3, q=5): {Phi_de_Produto_De_Primos(3, 5)} | Esperado: 8\n")

    # 6. Teste de Exponenciação Modular
    print("--- 6. Exponenciação Modular ---")
    print(f"Exponenciação (13^28 mod 29): {exponenciacao_modular(13, 28, 29)} | Esperado: 1\n")

    # 7. Teste do Teorema Chinês do Resto
    print("--- 7. Teorema Chinês do Resto ---")
    restos_teste = [3, 2, 2]
    modulos_teste = [5, 7, 11]
    print(f"Solução do sistema para restos {restos_teste} e módulos {modulos_teste}: {teorema_chines_resto(restos_teste, modulos_teste)} | Esperado: 23")

    print("\n====== FIM DOS TESTES - BIBLIOTECA APROVADA ======")
