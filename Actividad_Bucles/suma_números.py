#Ingresa numeros y los suma y hace media hasta que el usuario ingrese uno negativo...

suma = 0
contador_numeros = 0

while True:
    numero = float(input("Ingresa un número (si es negativo se detiene): "))
    if numero < 0:
        break
    suma += numero
    contador_numeros += 1

print("--------------------------------------------------")
if contador_numeros > 0:
    media = suma / contador_numeros
    print(f"La suma de los números ingresados es: {suma}")
    print(f"La media de los números ingresados es: {media}")
else:
    print("ERROR:No se ingresaron números positivos.")