#Multiplos de 3 y 5...

print("--------------------------------------------------")
print("Los números divisibles entre 3 y 5 del 1 al 100 son:")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)