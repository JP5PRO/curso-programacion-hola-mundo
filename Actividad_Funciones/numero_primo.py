#Ingresa un número y calcular si es primo...

def es_primo(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    limite = int(n ** 0.5)
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False
    return True

print("-----------¿Tu número es primo o no?-----------")
num = int(input("Ingresa un número: "))
if es_primo(num):
    print(f"{num} sí es primo")
else:
    print(f"{num} no es primo")
