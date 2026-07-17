#Estaciones del año

numero_mes = int(input("Ingresa el número del mes del 1 al 12: "))

match numero_mes:
    case 1:
        estacion = "Invierno"
    case 2:
        estacion = "Invierno"
    case 3:
        estacion = "Primavera"
    case 4:
        estacion = "Primavera"
    case 5:
        estacion = "Primavera"
    case 6:
        estacion = "Verano"
    case 7:
        estacion = "Verano"
    case 8:
        estacion = "Verano"
    case 9:
        estacion = "Otoño"
    case 10:
        estacion = "Otoño"
    case 11:
        estacion = "Otoño"
    case 12:
        estacion = "Invierno"
    case _:
        estacion = "ERROR: Ingresa un número de mes válido entre 1 y 12."

print(f"Estamos en el mes {numero_mes} y la estación del año es: {estacion}")
