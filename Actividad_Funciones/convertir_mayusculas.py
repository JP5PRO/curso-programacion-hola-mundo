#Contador de palabras y conversiones

def main():
    contador = 0
    while True:
        try:
            entrada = input("Ingresa una palabra o número (Con espacio terminas): ")
            if entrada == " ":
                break
            else:
                if entrada.isdigit():
                    entrada = str(entrada)
                print(entrada.upper())
                contador += 1
        except Exception as e:
            print("ERROR: ", e)
    print("PROGRAMA TERMINADO")
    print(f"Total de palabras procesadas: {contador}")
main()