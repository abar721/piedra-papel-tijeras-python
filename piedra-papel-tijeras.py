# Desafío
# Se puede colocar el nombre en la segunda solicitud OKAY
# Lo ingresado por el usuario sea lowerCase de tal forma de comparar minuscula con minuscula OKAY
# Más de 1 turno con bucle while OKAY

nombre1 = input("¿Cómo se llama el jugador 1?: ")
nombre2 = input("¿Cómo se llama el jugador 2?: ")

# Variables para registrar las victorias de cada jugador
puntaje1 = 0
puntaje2 = 0

# El bucle se ejecuta mientras ninguno de los jugadores tenga 2 victorias
while puntaje1 < 2 and puntaje2 < 2:
    print("\n--- Turno actual ---")
    print(f"Puntaje actual: {nombre1} = {puntaje1}, {nombre2} = {puntaje2}")

# uso de lower() para evitar errores de mayusculas y minusculas
    jugador1 = input(f"Hola {nombre1}, ¿Qué eliges? (piedra, papel o tijeras): ").lower()
    jugador2 = input(f"Hola {nombre2}, ¿Qué eliges? (piedra, papel o tijeras): ").lower()

    condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijeras" and jugador2 == "papel"
    
    if jugador1 == jugador2:
        print("¡Empate! No hay puntos para nadie.")
    elif condicion1 or condicion2 or condicion3:
        print(f"¡{nombre1} gana esta ronda!")
        puntaje1 += 1  # Incrementa el puntaje del jugador 1
    else: 
        print(f"¡{nombre2} gana esta ronda!")
        puntaje2 += 1  # Incrementa el puntaje del jugador 2

# El juego termina cuando uno de los dos puntajes llega a 2
print("\n--- ¡Fin del juego! ---")
if puntaje1 == 2:
    print(f"¡Felicidades, {nombre1} es el gran ganador!")
else:
    print(f"¡Felicidades, {nombre2} es el gran ganador!")