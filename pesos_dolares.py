"""1) Dada una cantidad en pesos, obtener la equivalencia en dolares, asumiendo que la unidad cambiaria es un dato desconocido"""
#Jesús Francisco Soriano Zamarripa
#Programación II
#16/04/2026

pm = float(input("Ingrese la cantidad en pesos: "))
pd = float(input("Ingrese el valor del dolar: "))
ed = pm / pd
print("La equivalencia a dolares es de", ed)