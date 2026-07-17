#Cuenta todos los digitos de un numero entero 12345, 0, -7...

numero = int(input("Ingresa un número entero: "))
contador_digitos = 0

if numero == 0:
    contador_digitos = 1
else:
    if numero < 0:
        numero = abs(numero)
    while numero != 0:
        numero //= 10
        contador_digitos += 1

print(f"El número {numero} tiene {contador_digitos} dígitos.")