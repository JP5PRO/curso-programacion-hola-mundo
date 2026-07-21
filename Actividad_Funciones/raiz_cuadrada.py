#Calcula raíz cuadrada con el metodo de Newton Raphson...

import math

def raiz_newton(n, tolerancia = 1e-10):
    if n < 0:
        raise ValueError("No se puede calcular raíz de negativo")
    estimacion = n / 2.0
    while True:
        nueva = 0.5 * (estimacion + n /estimacion)
        if abs(nueva - estimacion) < tolerancia:
            return nueva
        estimacion = nueva
        
try:
    numero = float(input("Ingresa un número: "))
    rai1 = math.sqrt(numero)
    rai2 = raiz_newton(numero)
    print(f"math.sqrt: {rai1}, Newton: {rai2:.10f}")
    if abs(rai1 - rai2) < 1e-9:
        print("CORRECTO los resultados coinciden")
    else:
        print("ERROR: hay una diferencia significativa...")
except ValueError as e:
    print(f"ERROR: {e}")