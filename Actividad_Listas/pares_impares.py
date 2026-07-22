#Guarda 10 numeros cuántos pares y impares...

def pares_impares(numeros):
    contador_pares = 0
    contador_impares = 0
    for i in numeros:
        if i % 2 == 0:
            contador_pares += 1
        else:
            contador_impares +=1
    return contador_pares, contador_impares

numeros = []
for i in range(1, 11):
    num = int(input(f"{i}.- Ingresa un numero: "))
    numeros.append(num)

print("---------------------------------------")
pares, impares = pares_impares(numeros)
print(f"La cantidad de numeros pares ingresados es de: {pares}")
print(f"La cantidad de numeros impares ingresados es de: {impares}")