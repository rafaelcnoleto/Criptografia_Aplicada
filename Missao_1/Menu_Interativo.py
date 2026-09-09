# ==============================================================================
# MENU INTERATIVO - SECUREDOCS (MISSAO 1)
# ==============================================================================
# Camada de apresentacao da biblioteca. Nao altera o Missao01.py: apenas
# importa as funcoes de la e as chama com os valores digitados pelo usuario.
#
# Executar com:  python Menu_Interativo.py
# ==============================================================================

from Missao01 import (
    Soma_Modular,
    Subtracao_Modular,
    Multiplicacao_Modular,
    Divisao_Modular,
    MDC,
    Algoritmo_de_Euclides,
    algoritmo_estendido_euclides,
    inverso_multiplicativo,
    Divisores,
    Eh_Primo,
    Fatorar,
    Sao_Coprimos,
    Lista_De_Primos,
    Phi_de_Euler,
    Phi_por_Definicao,
    Conjunto_Z_Estrela,
    Phi_de_Produto_De_Primos,
    exponenciacao_modular,
    teorema_chines_resto,
)

LIMITE_LENTO = 100000   # acima disso, pede confirmacao nas funcoes que varrem


# ------------------------------------------------------------------ entradas

def ler_inteiro(rotulo):
    while True:
        texto = input(f"  {rotulo}: ").strip()
        try:
            return int(texto)
        except ValueError:
            print("  >> Digite um numero inteiro.")


def ler_lista(rotulo):
    while True:
        texto = input(f"  {rotulo} (separados por espaco ou virgula): ").strip()
        texto = texto.replace(",", " ")
        try:
            valores = [int(p) for p in texto.split()]
        except ValueError:
            print("  >> Digite apenas numeros inteiros.")
            continue
        if not valores:
            print("  >> Informe pelo menos um valor.")
            continue
        return valores


def confirma_se_grande(n):
    """As funcoes que varrem de 1 ate n ficam lentas para n grande."""
    if n > LIMITE_LENTO:
        print(f"  >> Aviso: esta funcao percorre {n} numeros e pode demorar.")
        return input("  >> Continuar mesmo assim? (s/n): ").strip().lower() == "s"
    return True


def mostrar(rotulo, valor):
    print(f"\n  >>> {rotulo} = {valor}\n")


# ------------------------------------------------------------------ operacoes

def op_soma():
    a = ler_inteiro("a"); b = ler_inteiro("b"); n = ler_inteiro("n (modulo)")
    mostrar(f"({a} + {b}) mod {n}", Soma_Modular(a, b, n))

def op_subtracao():
    a = ler_inteiro("a"); b = ler_inteiro("b"); n = ler_inteiro("n (modulo)")
    mostrar(f"({a} - {b}) mod {n}", Subtracao_Modular(a, b, n))

def op_multiplicacao():
    a = ler_inteiro("a"); b = ler_inteiro("b"); n = ler_inteiro("n (modulo)")
    mostrar(f"({a} x {b}) mod {n}", Multiplicacao_Modular(a, b, n))

def op_divisao():
    a = ler_inteiro("a"); b = ler_inteiro("b"); n = ler_inteiro("n (modulo)")
    mostrar(f"({a} / {b}) mod {n}", Divisao_Modular(a, b, n))

def op_mdc():
    a = ler_inteiro("a"); b = ler_inteiro("b")
    mostrar(f"MDC({a}, {b})", MDC(a, b))

def op_euclides():
    a = ler_inteiro("a"); b = ler_inteiro("b")
    mostrar(f"Algoritmo de Euclides({a}, {b})", Algoritmo_de_Euclides(a, b))

def op_estendido():
    a = ler_inteiro("a"); b = ler_inteiro("b")
    d, x, y = algoritmo_estendido_euclides(a, b)
    print(f"\n  >>> MDC = {d}   x = {x}   y = {y}")
    print(f"  >>> Verificacao: {x} x {a} + {y} x {b} = {x*a + y*b}\n")

def op_inverso():
    a = ler_inteiro("a"); m = ler_inteiro("m (modulo)")
    resultado = inverso_multiplicativo(a, m)
    print(f"\n  >>> {a}^-1 mod {m} = {resultado}")
    print(f"  >>> Verificacao: {a} x {resultado} mod {m} = "
          f"{Multiplicacao_Modular(a, resultado, m)}\n")

def op_divisores():
    n = ler_inteiro("n")
    mostrar(f"Divisores de {n}", Divisores(n))

def op_eh_primo():
    n = ler_inteiro("n")
    mostrar(f"{n} e primo?", Eh_Primo(n))

def op_fatorar():
    n = ler_inteiro("n")
    fatores = Fatorar(n)
    partes = " x ".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in fatores.items())
    print(f"\n  >>> Fatoracao de {n} = {fatores}")
    if partes:
        print(f"  >>> Ou seja: {n} = {partes}\n")
    else:
        print()

def op_coprimos():
    a = ler_inteiro("a"); b = ler_inteiro("b")
    print(f"\n  >>> MDC({a}, {b}) = {MDC(a, b)}")
    mostrar(f"{a} e {b} sao coprimos?", Sao_Coprimos(a, b))

def op_lista_primos():
    limite = ler_inteiro("limite")
    if not confirma_se_grande(limite):
        return
    primos = Lista_De_Primos(limite)
    print(f"\n  >>> {len(primos)} primos ate {limite}:")
    print(f"  >>> {primos}\n")

def op_phi():
    n = ler_inteiro("n")
    print(f"\n  >>> Fatoracao de {n} = {Fatorar(n)}")
    mostrar(f"phi({n})", Phi_de_Euler(n))

def op_phi_definicao():
    n = ler_inteiro("n")
    if not confirma_se_grande(n):
        return
    mostrar(f"phi({n}) contando coprimos", Phi_por_Definicao(n))

def op_comparar_phi():
    n = ler_inteiro("n")
    if not confirma_se_grande(n):
        return
    pela_formula = Phi_de_Euler(n)
    pela_definicao = Phi_por_Definicao(n)
    print(f"\n  >>> phi({n}) pela formula   = {pela_formula}")
    print(f"  >>> phi({n}) pela definicao = {pela_definicao}")
    print(f"  >>> {'CONFEREM' if pela_formula == pela_definicao else 'DIVERGEM!'}\n")

def op_z_estrela():
    m = ler_inteiro("m")
    if not confirma_se_grande(m):
        return
    conjunto = Conjunto_Z_Estrela(m)
    print(f"\n  >>> Z*{m} = {conjunto}")
    print(f"  >>> Quantidade = {len(conjunto)}, e phi({m}) = {Phi_de_Euler(m)}\n")

def op_phi_produto():
    p = ler_inteiro("p (primo)"); q = ler_inteiro("q (primo)")
    resultado = Phi_de_Produto_De_Primos(p, q)
    print(f"\n  >>> n = {p} x {q} = {p*q}")
    print(f"  >>> phi(n) = ({p}-1)({q}-1) = {resultado}\n")

def op_exponenciacao():
    base = ler_inteiro("base"); expoente = ler_inteiro("expoente")
    modulo = ler_inteiro("modulo")
    mostrar(f"{base}^{expoente} mod {modulo}",
            exponenciacao_modular(base, expoente, modulo))

def op_tcr():
    print("  Sistema x = a1 (mod m1), x = a2 (mod m2), ...")
    restos = ler_lista("restos (a1 a2 ...)")
    modulos = ler_lista("modulos (m1 m2 ...)")
    if len(restos) != len(modulos):
        print("\n  >> A quantidade de restos e de modulos precisa ser igual.\n")
        return
    resultado = teorema_chines_resto(restos, modulos)
    print()
    for a, m in zip(restos, modulos):
        print(f"      x = {a} (mod {m})")
    produto = 1
    for m in modulos:
        produto *= m
    print(f"\n  >>> x = {resultado}  (mod {produto})\n")


# ------------------------------------------------------------------ menu

OPCOES = {
    "1":  ("Soma modular",                        op_soma),
    "2":  ("Subtracao modular",                   op_subtracao),
    "3":  ("Multiplicacao modular",               op_multiplicacao),
    "4":  ("Divisao modular",                     op_divisao),
    "5":  ("MDC",                                 op_mdc),
    "6":  ("Algoritmo de Euclides",               op_euclides),
    "7":  ("Algoritmo estendido de Euclides",     op_estendido),
    "8":  ("Inverso multiplicativo",              op_inverso),
    "9":  ("Divisores de um numero",              op_divisores),
    "10": ("Testar se e primo",                   op_eh_primo),
    "11": ("Fatorar em primos",                   op_fatorar),
    "12": ("Verificar se sao coprimos",           op_coprimos),
    "13": ("Listar primos ate um limite",         op_lista_primos),
    "14": ("Phi de Euler (pela fatoracao)",       op_phi),
    "15": ("Phi de Euler (pela definicao)",       op_phi_definicao),
    "16": ("Comparar as duas versoes de phi",     op_comparar_phi),
    "17": ("Conjunto Z*m",                        op_z_estrela),
    "18": ("Phi de produto de primos",            op_phi_produto),
    "19": ("Exponenciacao modular",               op_exponenciacao),
    "20": ("Teorema Chines do Resto",             op_tcr),
}

GRUPOS = [
    ("1. ARITMETICA MODULAR",                      ["1", "2", "3", "4"]),
    ("2. MDC E ALGORITMO DE EUCLIDES",             ["5", "6"]),
    ("3. ESTENDIDO E INVERSO MULTIPLICATIVO",      ["7", "8"]),
    ("4. NUMEROS PRIMOS",                          ["9", "10", "11", "12", "13"]),
    ("5. FUNCAO PHI DE EULER",                     ["14", "15", "16", "17", "18"]),
    ("6. EXPONENCIACAO MODULAR",                   ["19"]),
    ("7. TEOREMA CHINES DO RESTO",                 ["20"]),
]


def mostrar_menu():
    print("=" * 62)
    print("   BIBLIOTECA MATEMATICA - SECUREDOCS (MISSAO 1)")
    print("=" * 62)
    for titulo, chaves in GRUPOS:
        print(f"\n  --- {titulo} ---")
        for chave in chaves:
            print(f"   {chave:>2}) {OPCOES[chave][0]}")
    print("\n    0) Sair")
    print("=" * 62)


def main():
    while True:
        mostrar_menu()
        escolha = input("\nEscolha uma opcao: ").strip()

        if escolha == "0":
            print("\nEncerrando.\n")
            break

        if escolha not in OPCOES:
            print("\n>> Opcao invalida.\n")
            continue

        rotulo, funcao = OPCOES[escolha]
        print(f"\n--- {rotulo} ---")
        try:
            funcao()
        except ValueError as erro:
            print(f"\n  >> {erro}\n")
        except ZeroDivisionError:
            print("\n  >> Divisao por zero. O modulo nao pode ser 0.\n")
        except RecursionError:
            print("\n  >> Numeros grandes demais para a versao recursiva.\n")
        except Exception as erro:
            print(f"\n  >> Nao foi possivel calcular: {erro}\n")

        input("Pressione ENTER para voltar ao menu...")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nEncerrando.\n")
