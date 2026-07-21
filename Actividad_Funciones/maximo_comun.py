#Dados dos números enteros calcular su máximo común divisor...
import math

def max_comun_divisor(n1, n2):
    max_divisor=0
    n1 = abs(n1)
    n2 = abs(n2)
    
    if n1 == 0 and n2 == 0:
        return 0
    
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

print("----------Calcula el MCD----------")
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

resultado = max_comun_divisor(num1, num2)
resultado_math = math.gcd(num1, num2)

print(f"El máximo común divisor de {num1} y {num2} es: {resultado}")
print(f"El máximo común divisor con math.gcd es: {resultado_math}")

if resultado == resultado_math:
    print("Correcto!! Los resultados sí coinciden")
else:
    print("ERROR: Los resultados no coinciden")
    
if num1 == 0 and num2 == 0:
    print("Caso especial los dos números son 0")
else:
    print("Programa Terminado")