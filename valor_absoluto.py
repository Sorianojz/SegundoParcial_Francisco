"""2) Leer un numero y escribir el valor absoluto del mismo"""
#Jesús Francisco Soriano Zamarripa
#Programación II
#16/04/2026

v = int(input("Ingrese un valor: "))
if v < 0:
    print("El valor absoluto es", v * -1)
if v == 0:
    print("El valor absoluto es 0")
if v > 0:
    print("El valor absoluto es", v)
