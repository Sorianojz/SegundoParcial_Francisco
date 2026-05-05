"""2) Leer 10 numero e imprimir solo los positivos"""
#Jesús Francisco Soriano Zamarripa
#Programación II
#23/04/2026

numero = 1

for i in range(0, 10):
    numero = float(input("Ingrese el numero: "))
    if numero > 0:
        print(numero, "es positivo")