import numpy as np
from matplotlib import pyplot as plt

def main():
    num = get_function()
    print("------------------------------------")
    
    x,y = function_select(num)

    plt.plot(x,y,"-")
    plt.grid()
    plt.show()

def get_function():
    while True:
        print("Escolha a função que deseja estudar:")
        print("1 - 1º Grau")
        print("2 - 2º Grau")
        print("3 - Senoide")
        print("4 - Polinômial")
        print("5 - Cossenoide")
        print("6 - Exponencial")
        print("7 - Constante")
        print("8 - Função logarítmica")
        print("9 - Função Modular")
        x = input("Digite o Número referente a função e confirme: ")
        try:
            x = int(x)
            if 0 < x <= 9:
                return x
            else:
                pass
        except:
            pass

        print("---------------------------------------")
        print("ERRO AO INDICAR FUNÇÃO. TENTE NOVAMENTE")
        print("---------------------------------------")

def function_select(n):
    x = np.arange(-100,100,0.1)
    y = x
    if n == 1:
        x, y = primeiro_grau(x)

    elif n == 2:
        x, y = segundo_grau(x)

    elif n  == 3:
        x, y = senoide(x)

    elif n == 4:
        x, y = polinomial(x)
    
    elif n  == 5:
        x, y = cossenoide(x)

    elif n == 6:
        x,y = exponencial(x)

    elif n  == 7:
        x, y = constante(x)

    elif n  == 8:
        x, y = logaritmica()

    elif n  == 9:
        x, y = modular()

    return x,y

def primeiro_grau(x):
    print("Função de Primeiro Grau:")
    print("Formato: ax + b")
    a = float(input("Escolha o valor de a: "))
    b = float(input("Escolha o valor de b: "))
    y = a*x + b
    return x, y

def segundo_grau(x):
    print("Função de Segundo Grau:")
    print("Formato: ax² + bx + c")
    a = float(input("Escolha o valor de a: "))
    b = float(input("Escolha o valor de b: "))
    c = float(input("Escolha o valor de c: "))
    y = a*(x**2) + b * x + c
    
    return x, y

def senoide(x):
    print("Função Seno:")
    print("Formato: A.sen(x)")
    A = float(input("Escolha o valor de A: "))
    y = A*np.sin(x)
    return x, y

def polinomial(x):
    while True:
        try:
            n = int(input("Determine o Grau do polinômio: "))
            break
        except:
            pass
    print("Função Polinomial:")
    print("Formato: A0 + A1.x + A2.x² + A3.x³ + ... + An.x^n, sendo:")
    print("A0 = Coeficiente de ordem 0\nA1 = Coeficiente de ordem 1\n.\n.\n.\nAn = Coeficiente de ordem enéssima ordem")
    A = []
    print("---------------------------------------")
    for i in range(0, n + 1):
        while True:
            try: 
                print("Indique o coeficiente de ordem", i, end = ": ")
                A.append(int(input()))
                break
            except:
                pass
    y = 0
    for i in range(0, len(A)):
        y += A[i]*(x**i+1)
    return x, y

def cossenoide(x):
    print("Função Seno:")
    print("Formato: A.cos(x)")
    A = float(input("Escolha o valor de A: "))
    y = A*np.cos(x)
    return x, y

def exponencial(x):
    print("Função Exponencial:")
    print("Formato: A^x")
    A = float(input("Escolha o valor de A: "))
    y = A**x
    return x, y

def constante(x):
    print("Função Constante:")
    print("Formato: y = a")
    a = float(input("Escolha o valor de a: "))
    y = 0*x + a
    return x, y

def logaritmica():
    while True:
        print("Função Logarítmica!\n A função Logarítmica possui um Logarítmando e uma base, escolha a base:")
        a = input("Digite a base desejada (Precisa ser diferente de 0 e 1): ")
        try:
            a = float(a)
            if a == 0 or a == 1 :
                pass
            else:
                break
        except:
            pass

        print("---------------------------------------")
        print("ERRO AO INDICAR A BASE. TENTE NOVAMENTE.")
        print("---------------------------------------")
    
    x = np.arange(0.1,200,0.1)
    y = np.log(x)/np.log(a)
    return x , y

def modular():
    while True:
        print("Função Modular!\n A função modular funciona com outras funções, escolha uma para continuar:")
        print("1 - 1º Grau")
        print("2 - 2º Grau")
        print("3 - Senoide")
        print("4 - Polinomial")
        print("5 - Cossenhoide")
        print("6 - Exponencial")
        print("7 - Constante")
        print("8 - Função logarítmica")
        n = input("Digite o Número referente a função e confirme: ")
        try:
            n = int(n)
            if 0 < n <= 8:
                break
            else:
                pass
        except:
            print("---------------------------------------")
            print("ERRO AO INDICAR FUNÇÃO. TENTE NOVAMENTE")
            print("---------------------------------------")

    x, y = function_select(n)
    y = np.abs(y)
    return x , y


main()