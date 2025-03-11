nombre1 = input("Como se llama jugador 1?: ")
nombre2 = input("Como se llama jugador 2?: ")

adivinado = False


while not adivinado:
    jugador1 = input(f"Hola {nombre1}, qué eliges? Piedra, papel o tijera?: ")
    jugador2 = input(f"Hola {nombre2}, qué eliges? Piedra, papel o tijera?: ")

    if jugador1 == jugador2:
        print("ha sido un empate!")

    elif (
        (jugador1 == "piedra" and jugador2 == "tijeras")
        or (jugador1 == "papel" and jugador2 == "piedra")
        or (jugador1 == "tijera" and jugador2 == "papel")
    ):
        print(f"ha ganado {nombre1}")
    else:
        print(f"ha ganado el {nombre2}")

        jugar_de_nuevo = input("¿Quieren jugar otra vez? (sí/no): ").lower()
        if jugar_de_nuevo != "sí":
            adivinado = True  # Finaliza el bucle

print("fin de juego")
