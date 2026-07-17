# Secuencia Aritmetica...

inicio = int(input("Ingresa el valor inicial: "))
diferencia = int(input("Ingresa la diferencia: "))
limite = int(input("Ingresa el límite: "))

num = inicio
while True:
    print(num)
    num += diferencia
    if num > limite:
        break

print("--------------------------------------------------")
print(f"Secuencia Aritmetica desde {inicio} hasta {limite} con diferencia de {diferencia}.")