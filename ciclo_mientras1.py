"""1) En una empresa se requiere calcular el salario semanal de cada uno de los n obrerosque laboran en
ella. El salario se obtiene de la siguiente forma: obrero trabaja <= 40 = $20 por hora,
si el obrero trabaja > 40, $20 por las primeras 40h y $25 por cada hora extra"""
#Jesús Francisco Soriano Zamarripa
#Programación II
#23/04/2026

nh = int(input("Ingrese el numero de horas: "))

while nh <= 40:
    salario = nh * 20
    print("El salario es:", salario)
    break
while nh > 40:
    salario = 800 + (nh - 40) * 25
    print("El salario más horas extra es:", salario)
    break
