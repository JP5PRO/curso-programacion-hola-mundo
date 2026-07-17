#Programa para calcular el índice de masa corporal de cualquier persona...

peso = float(input("Ingrese su masa en kilos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es de: {imc}")