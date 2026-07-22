#Lee 5 numeros y calcula su suma con SUM y bucle...

def suma_numeros(lista_numeros):
    suma_num = 0
    for i in lista_numeros:
        suma_num += i
    return suma_num

numeros = []
for i in range(5):
    num = int(input(f"{i+1}.- Ingresa un numero: "))
    numeros.append(num)
    
suma = suma_numeros(numeros)
suma_con_sum = sum(numeros)

print("--------------------------------------")
print(f"La suma de tus numeros con bucle: {suma}")
print(f"La suma de tus numeros con SUM: {suma_con_sum}")

if suma == suma_con_sum:
    print("CORRECTO los dos resultados coinciden")
else:
    print("ERROR los dos resultados no coinciden")