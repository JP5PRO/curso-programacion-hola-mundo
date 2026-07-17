#Numeros impares desde 1 hasta el n...

numero = int(input("Ingresa un número POSITIVO: "))
if numero < 0:
    print("ERROR: NÚMERO INCORRECTO. Debe ser positivo.")
else:
    print(f"Los números impares desde 1 hasta {numero} son:")
    i = 1
    while True:
        if i > numero:
            break
        if i % 2 != 0:
            print(i, end=" , ")
        i += 1