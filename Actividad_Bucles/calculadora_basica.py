#Calculadora basica...

while True:
    print("--------------------------------------------------")
    print("Calculadora básica")
    print("--------------------------------------------------")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = input("Ingrese el número de la operación que desea realizar: ")
    
    if opcion == "5":
        print("Saliendo de la calculadora...")
        break
    
    primer_numero = float(input("Ingrese el primer número: "))
    segundo_numero = float(input("Ingrese el segundo número: "))
    
    match opcion:
        case "1":
            resultado = primer_numero + segundo_numero
            print(f"El resultado de la suma es: {resultado}")
        case "2":
            resultado = primer_numero - segundo_numero
            print(f"El resultado de la resta es: {resultado}")
        case "3":
            resultado = primer_numero * segundo_numero
            print(f"El resultado de la multiplicación es: {resultado}")
        case "4":
            if segundo_numero == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                resultado = primer_numero / segundo_numero
                print(f"El resultado de la división es: {resultado}")
        case _:
            print("Opción inválida. Por favor, seleccione una opción válida.")