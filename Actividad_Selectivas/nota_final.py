#Nota final de un estudiante...

parciales = float(input("Ingresa la nota de los parciales de 0 a 100: "))
proyecto = float(input("Ingresa la nota del proyecto de 0 a 100: "))
examen_final = float(input("Ingresa la nota del examen final de 0 a 100: "))

nota_final = (parciales * 0.4) + (proyecto * 0.3) + (examen_final * 0.3)

if (parciales < 0 or parciales > 100) or (proyecto < 0 or proyecto > 100) or (examen_final < 0 or examen_final > 100):
    print("ERROR: Has ingresado una nota incorrecta, por favor ingresa notas entre 0 y 100.")
else:
    print("La nota final del estudiante es: ", nota_final)
    