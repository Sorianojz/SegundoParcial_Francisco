"""2) El Departamento de Seguridad Publica y Transito del D.F. desea saber de los n autos que entran a la
CDMX, cuantos entran con calcomania de cada color. Conociendo el ultimo digito de cada placa: 
Dig. Color: 1 o 2 = Amarrillo, 3 o 4 = Rosa, 5 o 6 = Rojo, 7 o 8 = Verde, 9 o 0 = Azul """
#Jesús Francisco Soriano Zamarripa
#Programación II
#23/04/2026

n = int(input("Ingrese el numero de la placa: "))

while n == 1 or n == 2:
    print("Calcomania Amarrila")
    break
while n == 3 or n == 4:
    print("Calcomania Rosa")
    break
while n == 5 or n == 6:
    print("Calcomania Roja")
    break
while n == 7 or n == 8:
    print("Calcomania Verde")
    break
while n == 9 or n == 0:
    print("Calcomania Azul")
    break