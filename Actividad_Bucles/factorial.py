#Factorial

num = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1
if num < 0:
    print("ERROR: NÚMERO INCORRECTO. Debe ser positivo.")
else:
    for i in range(1, num + 1):
        factorial *= i

print(f"El factorial de {num} es {factorial}")