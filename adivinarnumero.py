
""" ADIVINA EL NUMERO
import random

def adivinar_numero():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!")

    while not adivinado:
        # Solicitar al usuario que ingrese un número
        try:
            numero_usuario = int(input("Ingresa un número entre 1 y 100: "))
            
            if numero_usuario < 1 or numero_usuario > 100:
                print("Por favor, ingresa un número dentro del rango 1-100.")
                continue

            intentos += 1

            # Comparar el número ingresado con el número secreto
            if numero_usuario < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif numero_usuario > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                adivinado = True
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Llamar a la función del juego
adivinar_numero() """

#ADIVINAR EL NUMERO EN UN MAXIMO DE INTENTOS

import random

def adivinar_numero():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    intentos = 0
    max_intentos = 10
    adivinado = False

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!")
    print(f"Tienes un máximo de {max_intentos} intentos para adivinar el número.")

    while not adivinado and intentos < max_intentos:
        # Solicitar al usuario que ingrese un número
        try:
            numero_usuario = int(input(f"Intento {intentos + 1}/{max_intentos}: Ingresa un número entre 1 y 100: "))
            
            if numero_usuario < 1 or numero_usuario > 100:
                print("Por favor, ingresa un número dentro del rango 1-100.")
                continue

            intentos += 1

            # Comparar el número ingresado con el número secreto
            if numero_usuario < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif numero_usuario > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                adivinado = True
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    if not adivinado:
        print(f"Lo siento, no has adivinado el número en {max_intentos} intentos. El número secreto era {numero_secreto}.")

# Llamar a la función del juego
adivinar_numero()
