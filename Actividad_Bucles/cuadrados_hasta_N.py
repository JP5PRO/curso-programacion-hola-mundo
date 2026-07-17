#Cuadrados hasta N...

numero = int(input("Ingresa un número POSITIVO: "))

if numero < 0:
    print("ERROR: NÚMERO INCORRECTO. Debe ser positivo.")
else:
    i = 1
    print(f"Secuencia de cuadrados hasta {numero}:")
    while True:
        print(i ** 2)
        i += 1
        if i > numero:
            break