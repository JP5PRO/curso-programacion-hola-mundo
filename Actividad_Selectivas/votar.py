#Define si una persona puede votar segun su edad...

edad = int(input("Ingresa tu edad: "))

if edad >= 18 and edad <= 100:
    voto = "Eres elegible para votar!"
elif edad >= 0 and edad < 18:
    voto = "No eres elegible para votar, debes tener al menos 18 años."
else:
    voto = "ERROR: Ingresa una edad entre 0 y 100 años."

print(f"Resultado: {voto}")