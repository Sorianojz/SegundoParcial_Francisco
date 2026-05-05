"""1) Calcular el promedio de un alumnoque tiene 7 calificaciones en la materia:
Diseño Estructurado de Algoritmos"""
#Jesús Francisco Soriano Zamarripa
#Programación II
#23/04/2026

suma = 0

for i in range(1, 8):
    numero = float(input("Ingrese la calificacion: "))
    suma = suma + numero

print("El promedio es", suma / 7)