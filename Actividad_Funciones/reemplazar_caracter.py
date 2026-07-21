#Implemetar una cadena y elegir un caracter a reemplazar...abs

def reemplazo_manual(texto, viejo, nuevo):
    if len(viejo) != 1 or len(nuevo) != 1:
        return texto, 0
    resultado = ""
    contador = 0
    for letra in texto:
        if letra == viejo:
            resultado += nuevo
            contador += 1
        else:
            resultado += letra
    return resultado, contador

print("----------Reemplazo de carácteres----------")
cadena = input("Ingresa una cadena de texto: ")
caracter_anterior = input("Carácter a reemplazar: ")
caracter_nuevo = input("Carácter nuevo: ")

if len(caracter_anterior) != 1 or len(caracter_nuevo) != 1:
    print("ERROR: Debes ingresar un solo carácter")
else:
    texto_modificado, numero = reemplazo_manual(cadena, caracter_anterior, caracter_nuevo)
    texto_modificado2 = cadena.replace(caracter_anterior, caracter_nuevo)
    print(f"De la forma manual: {texto_modificado} | Cantidad de Reemplazos: {numero}")
    print(f"De la forma repleace: {texto_modificado2}")
    if texto_modificado == texto_modificado2:
        print("CORRECTO los dos resultados coinciden")
    else:
        print("ERROR no coinciden los resultados")