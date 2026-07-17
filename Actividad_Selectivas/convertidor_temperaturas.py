#Convierte temperaturas...

temp_celsius = float(input("Ingresa la temperatura en grados Celsius: "))

print("-----------------------------------------------------")
print("Elige la opción de conversión: ")
print("1. Convertir a Fahrenheit")
print("2. Convertir a Kelvin")
opcion = int(input("Ingresa tu opción: "))

match opcion:
    case 1:
        temp_convertida = (temp_celsius * 9/5) + 32
        opcion_elegida = "Fahrenheit"
    case 2:
        temp_convertida = temp_celsius + 273.15
        opcion_elegida = "Kelvin"
    case _:
        temp_convertida = None
        opcion_elegida = None
        temp_celsius = None
        print("ERROR: Opción inválida. Por favor, elige 1 o 2.")

print("-----------------------------------------------------")
print(f"Temperatura en Celsius: {temp_celsius}°C y la temperatura convertida a {opcion_elegida} es: {temp_convertida}°")
