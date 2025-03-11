print(
    "---------------------------numero par o impar -------------------------------------"
)
number = input("choose a number from 0 to 1000: ")
number = int(number)
if number % 2 == 0:
    print("seu numero es par")
else:
    print("seu numero é impar")

print(
    "---------------------------contador de 1 ao 10 -------------------------------------"
)

contador = 0
while contador <= 10:
    contador += 1
    print("el contador es:", contador)
