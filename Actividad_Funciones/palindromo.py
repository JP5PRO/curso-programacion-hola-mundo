#Ingresa una cadena de texto y conocer si es palíndromo y su longitud

def palindromo(texto):
    limpia = ""
    
    for caracter in texto:
        if caracter != " ":
            limpia += caracter
    return limpia == limpia[::-1], limpia

print("-----------Palíndromo-----------")
cadena = input("Ingresa una frase o cadena de texto: ").lower()
resultado, cadena_limpia = palindromo(cadena)

if resultado:
    print(f"La cadena: {cadena} sí es palíndromo: {cadena_limpia[::-1]}")
else:
    print(f"La cadena: {cadena} no es palíndromo: {cadena_limpia[::-1]}")
print(f"Longitud de la cadena limpia: {len(cadena_limpia)}")