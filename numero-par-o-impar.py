# Pide un número al usuario y determina si es par o impar.

number = input("elija un numero de 0 a 10: ")
number = int(number)

if number % 2 == 0:
    print(f"felicitaciones, eligiste bien! el numero {number} es par")
else:
    print(f"naa, necesitamos otro numero. el numero {number} no es par")
