# Recibiras un rango dependiendo de la calificacion ingresada...

calificacion = float(input("Ingresa tu calificación del 0 al 100: "))

if calificacion < 0 or calificacion > 100:
    rango = "ERROR: Has ingresado una calificación incorrecta, cumple con el rango de 0 a 100."
elif calificacion >= 90:
    rango = "Tu calificación es A"
elif calificacion >= 80:
    rango = "Tu calificación es B"
elif calificacion >= 70:
    rango = "Tu calificación es C"
elif calificacion >= 60:
    rango = "Tu calificación es D"
else:
    rango = "Tu calificación es F"

print(f"Tu calificación es: {rango}")
