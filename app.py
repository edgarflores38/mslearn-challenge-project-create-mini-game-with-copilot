# write 'hello world' to the console
# print('hello world')

import random

def jugar():
    opciones = ['rock', 'paper', 'scissors']
    puntuacion_jugador = 0
    puntuacion_computadora = 0

    while True:
        eleccion_jugador = input("Elige rock, paper o scissors (o 'salir' para terminar el juego): ").lower()
        if eleccion_jugador == 'salir':
            print(f"Puntuación final - Jugador: {puntuacion_jugador}, Computadora: {puntuacion_computadora}")
            break
        if eleccion_jugador not in opciones:
            print("Opción no válida. Por favor elige rock, paper o scissors.")
            continue

        eleccion_computadora = random.choice(opciones)
        print(f"La computadora eligió: {eleccion_computadora}")

        if eleccion_jugador == eleccion_computadora:
            print("Es un empate.")
        elif (eleccion_jugador == "rock" and eleccion_computadora == "scissors") or \
             (eleccion_jugador == "scissors" and eleccion_computadora == "paper") or \
             (eleccion_jugador == "paper" and eleccion_computadora == "rock"):
            print("¡Ganaste!")
            puntuacion_jugador += 1
        else:
            print("Perdiste.")
            puntuacion_computadora += 1

# Iniciar el juego
jugar()