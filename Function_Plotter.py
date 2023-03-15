import numpy as np
from matplotlib import pyplot as plt

def main():
    num = get_function() #To return The function selected by the user
    print("------------------------------------")

    x,y = function_select(num) #Return the values of X and Y arrays

    funct = ["1º Degree Function",
             "2º Degree Function",
             "Sinusoidal Function",
             "Polynomial Function",
             "Cosinusoidal Function",
             "Exponential Function",
             "Constant Function",
             "Logarithmic Function",
             "Modular Function"]

    plt.plot(x,y,"-") #Create The Plot
    plt.title(funct[num-1]) #Create The Plot
    plt.grid()
    plt.show() #Show the plot

def get_function(): #User chose the function wanted
    while True:
        print("Choose the function that you want to study:")
        print("1 - 1º Degree Functions")
        print("2 - 2º Degree Functions")
        print("3 - Sinusoidal Function")
        print("4 - Polynomial Function")
        print("5 - Cosinusoidal Function")
        print("6 - Exponential Function")
        print("7 - Constant Function")
        print("8 - Logarithmic Function")
        print("9 - Modular Function")
        x = input("Enter the number referring to the function and confirm: ")

        try:
            x = int(x)
            if 0 < x <= 9:
                return x
            else:
                pass
        except:
            pass

        print("---------------------------------------")
        print("Error in the function indication. TRY AGAIN")
        print("---------------------------------------")

def function_select(n): #Select the function to calculate de values
    x = np.arange(-100,100,0.1)
    y = x
    if n == 1:
        x, y = first_degree(x)

    elif n == 2:
        x, y = second_degree(x)

    elif n  == 3:
        x, y = sinusoidal(x)

    elif n == 4:
        x, y = polynomial(x)

    elif n  == 5:
        x, y = cosinusoidal(x)

    elif n == 6:
        x,y = exponential(x)

    elif n  == 7:
        x, y = constant(x)

    elif n  == 8:
        x, y = logarithmic()

    elif n  == 9:
        x, y = modular()

    return x,y

def first_degree(x,a = 0,b = 0): #First Degree function data generation
    print("1º Degree Functions: ")
    print("Format: ax + b")
    if a == 0:
        a = float(input("Choose the 'a' value: "))
    if b == 0:
        b = float(input("Choose the 'b' value: "))
    y = a*x + b
    return x, y

def second_degree(x,a = 0,b = 0, c = 0): #Second Degree frunction data generation
    print("2º Degree Functions: ")
    print("Format: ax² + bx + c")
    if a == 0:
        a = float(input("Choose the 'a' value: "))
    if b == 0:
        b = float(input("Choose the 'b' value: "))
    if c == 0:
        c = float(input("Choose the 'c' value: "))
    y = a*(x**2) + b * x + c

    return x, y

def sinusoidal(x, A = 0): #Sinusoidal frunction data generation
    print("Sinusoidal Function:")
    print("Format: A.sen(x)")
    if A == 0:
        A = float(input("Choose the 'A' value: "))
    y = A*np.sin(x)
    return x, y

def polynomial(x): #Polynomial frunction data generation
    while True:
        try:
            n = int(input("Choose the polynomial's degree: "))
            break
        except:
            pass
    print("Polynomial Function:")
    print("Format: A0 + A1.x + A2.x² + A3.x³ + ... + An.x^n, sendo:")
    print("A0 = Coefficient of order 0\nA1 = Coefficient of order 1\n.\n.\n.\nAn = Nth order coefficient")

    A = []
    print("---------------------------------------")
    for i in range(0, n + 1):
        while True:
            try:
                print("Choose the coefficient of order", i, end = ": ")
                A.append(int(input()))
                break
            except:
                pass
    y = 0
    for i in range(0, len(A)):
        y += A[i]*(x**i+1)
    return x, y

def cosinusoidal(x, A = 0):#Cosinoidal frunction data generation
    print("Cosinusoidal Function:")
    print("Format: A.cos(x)")
    if A == 0:
        A = float(input("Choose the 'A' value: "))
    y = A*np.cos(x)
    return x, y

def exponential(x, A = 0): #Exponential frunction data generation
    print("Exponential Function:")
    print("Format: A^x")
    if A == 0:
        A = float(input("Choose the 'A' value: "))
    y = A**x
    return x, y

def constant(x, a = 0): #Constant frunction data generation
    print("Constant Function:")
    print("Format: y = a")
    if a == 0:
        a = float(input("Choose the 'a' value: "))
    y = 0*x + a
    return x, y

def logarithmic(): #Logarithmic frunction data generation
    while True:
        print("Logarithmic Function!\n The logarithmic function has a base. Choose the desired base:")
        a = input("Enter the desired base (Must be a number different that 0 and 1): ")
        try:
            a = float(a)
            if a == 0 or a == 1 :
                pass
            else:
                break
        except:
            pass

        print("---------------------------------------")
        print("Error specifying base. TRY AGAIN.")
        print("---------------------------------------")

    x = np.arange(0.1,200,0.1)
    y = np.log(x)/np.log(a)
    return x , y

def modular(): #Modular frunction data generation
    while True:
        print("Modular Function!\n The modular function works with other functions, choose one of then to continue:")
        print("1 - 1º Degree Functions")
        print("2 - 2º Degree Functions")
        print("3 - Sinusoidal Function")
        print("4 - Polynomial Function")
        print("5 - Cosinusoidal Function")
        print("6 - Exponential Function")
        print("7 - Constant Function")
        print("8 - Logarithmic Function")
        n = input("Enter the number referring to the function and confirm: ")
        try:
            n = int(n)
            if 0 < n <= 8:
                break
            else:
                pass

        except:
            print("---------------------------------------")
            print("Error in the function indication. TRY AGAIN")
            print("---------------------------------------")

    x, y = function_select(n)
    y = np.abs(y)
    return x , y

if __name__ == "__main__":
    main()
