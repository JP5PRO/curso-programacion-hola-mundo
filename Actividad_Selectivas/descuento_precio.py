#Genera el precio final dependiendo del descuento...

precio_original = float(input("Ingresa el precio original del producto: "))

if precio_original <= 100:
    descuento = 1
elif precio_original <= 200:
    descuento = 0.9
elif precio_original <= 500:
    descuento = 0.8
else:
    descuento = 0.75

precio_final = precio_original * descuento
print(f"El precio final del producto es: {precio_final}")
