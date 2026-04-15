#Nombre del alumno: jesus Francisco Soriano Zamarripa
#Nombre del ejercicio: Mostrar 2 numeros y un operador
#Fecha de elaboración: 25/03/2026

n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
operador = (input("Ingresa el operador: "))
if operador == "+":
    resultado = n1 + n2
    print("El resultado es", resultado)
elif operador == "-":
    resultado = n1 - n2
    print("El resultado es", resultado)
elif operador == "/":
    resultado = n1 / n2
    print("El resultado es", resultado)
elif operador == "*":
    resultado = n1 * n2
    print("El resultado es", resultado)