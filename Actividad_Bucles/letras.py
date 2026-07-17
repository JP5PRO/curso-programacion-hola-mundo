#Genera si es Vocal o Consonante...

while True:
    print("--------------------------------------------------")
    letra = input("Ingrese una LETRA: ").lower()
    
    if letra == " ":
        print("Saliendo...")
        break
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print(f"La letra '{letra}' es una vocal.")
    else:
        print(f"La letra '{letra}' es una consonante.")