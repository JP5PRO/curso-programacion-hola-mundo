#Programa para calcular el salario neto de un empleado...

salario_bruto_mensual = float(input("Ingrese su salario bruto mensual: "))
porcentaje_impuestos = float(input("Ingrese su porcentaje de impuestos: "))
deducciones_adicionales = float(input("Ingrese sus deducciones adicionales: "))

impuestos = (salario_bruto_mensual * (porcentaje_impuestos / 100))
salario_neto = salario_bruto_mensual - impuestos - deducciones_adicionales

print(f"Su salario neto es igual a: {salario_neto}")