#Convertir de pesos mexicanos a cualquier otra moneda

dinero_mxn = float(input("Ingresa tu cantidad en pesos mexicanos (MXN): "))

print("Elige la moneda a la que deseas convertir: ")
print("1.-Dólar (USD) 2.-Euro (EUR) 3.-Bath (THB) 4.-Yen (JPY) 5.-Won (KRW) 6.-Dólar Australiano (AUD) 7.-Sol (PEN)")
print("8.-Dólar Canadiense (CAD) 9.-Bolívar (VES) 10.-Peso Argentino (ARS)")
opcion = int(input("Ingresa tu opción: "))

match opcion:
    case 1:
        dinero_convertido = dinero_mxn / 16.5
        moneda = "Dólar (USD)"
    case 2:
        dinero_convertido = dinero_mxn / 18.0
        moneda = "Euro (EUR)"
    case 3:
        dinero_convertido = dinero_mxn / 0.45
        moneda = "Bath (THB)"
    case 4:
        dinero_convertido = dinero_mxn / 0.12
        moneda = "Yen (JPY)"
    case 5:
        dinero_convertido = dinero_mxn / 0.013
        moneda = "Won (KRW)"
    case 6:
        dinero_convertido = dinero_mxn / 11.5
        moneda = "Dólar Australiano (AUD)"
    case 7:
        dinero_convertido = dinero_mxn / 2.8
        moneda = "Sol (PEN)"
    case 8:
        dinero_convertido = dinero_mxn / 8.2
        moneda = "Dólar Canadiense (CAD)"
    case 9:
        dinero_convertido = dinero_mxn / 0.0023
        moneda = "Bolívar (VES)"
    case 10:
        dinero_convertido = dinero_mxn / 0.046
        moneda = "Peso Argentino (ARS)"
    case _:
        print("ERROR: Opción inválida. Por favor, elige un número del 1 al 10.")
        dinero_mxn = None
        dinero_convertido = None
        moneda = None
    
print(f"Tu cantidad de {dinero_mxn} pesos mexicanos (MXN) convertida a {moneda} es: {dinero_convertido}")
