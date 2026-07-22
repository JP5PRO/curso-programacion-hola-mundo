#Ingresa 6 numeros en una lista y inviertela...

def invertir_lista(lista_numeros):
    invertida = []
    for i in range(len(lista_numeros) -1, -1, -1):
        invertida.append(lista_numeros[i])
    return invertida

numeros = []
for i in range(6):
    num = int(input(f"{i+1}.- Ingresa un numero: "))
    numeros.append(num)

print("-------------------------------")
print(f"Lista Original: {numeros}")

lista_invetida = invertir_lista(numeros)
print(f"Lista Invertiva: {lista_invetida}")