#Contador de palabras y conversiones

def main():
    contador = 0
    while True:
        try:
            cadena = input("Ingresa una palabra o número (Con espacio terminas): ")
            if cadena == " ":
                break
            else:
                if cadena.isdigit():
                    cadena = str(cadena)
                print(cadena.upper())
                contador += 1
        except Exception as e:
            print("ERROR: ", e)
    print("PROGRAMA TERMINADO")
    print(f"Total de palabras procesadas: {contador}")
main()