#Ingresa 8 numeros y encuentra el valor mínimo y máximo...

def maximo_bucle(lista_numeros):
    if len(lista_numeros) == 0:
        return None
    maximo = lista_numeros[0]
    
    for i in lista_numeros[1:]:
        if i > maximo:
            maximo = i
    return maximo

def minimo_bucle(lista_numeros):
    if len(lista_numeros) == 0:
        return None
    minimo = lista_numeros[0]
    
    for i in lista_numeros:
        if i < minimo:
            minimo = i
    return minimo

numeros = []
for i in range(8):
    num = int(input(f"{i+1}.- Ingresa un numero: "))
    numeros.append(num)
    
numero_maximo = maximo_bucle(numeros)
numero_minimo = minimo_bucle(numeros)

print("-------------------------------------------------------------------------------")
print(f"El número maximo en tu lista de numeros de forma manual es: {numero_maximo} ")
print(f"El número minimo en tu lista de numeros de forma manual es: {numero_minimo} ")