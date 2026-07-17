#Cuantos números son positivos, negativos y ceros dependiendo de la cantidad ingresada...

cantidad_numeros = int(input("Ingresa la cantidad de números que quieres mandar: "))
print("--------------------------------------------------")

positivos = 0
negativos = 0
ceros = 0

for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print("--------------------------------------------------")
print(f"Cantidad de números positivos ingresados: {positivos}")
print(f"Cantidad de números negativos ingresados: {negativos}")
print(f"Cantidad de números ceros ingresados: {ceros}")
