#Contar cuantas A tiene una palabra "Algoritmo", "casa", "AAaa"...

palabra = input("Ingresa una palabra: ").lower()
contador = 0

for letra in palabra:
    if letra == "a":
        contador += 1

print(f"La palabra '{palabra}' tiene {contador} letras 'A'.")