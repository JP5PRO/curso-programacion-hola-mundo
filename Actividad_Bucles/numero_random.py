#Numeros Random hasta adivinar...
import random

numero_random = random.randint(1, 100)

while True:
    print("--------------------------------------------------")
    numero_usuario = int(input("Adivina el número entre 1 y 100: "))
    
    if numero_usuario < numero_random:
        print("El número es mayor.")
    elif numero_usuario > numero_random:
        print("El número es menor.")
    else:
        print(f"¡Felicidades! Has acertado el número {numero_random}.")
        break
