"""8) Todos los Lunes, Miercoles y Viernes, una persona corre la misma ruta y cronometra los tiempos obtenidos.
Determina el tiempo promedio que la persona tarda en recorrer la ruta en una semana cualquiera"""
#Jesús Francisco Soriano Zamarripa
#Programación II
#20/04/2026

#Lunes
t1 = float(input("Ingrese el primer tiempo: "))

#Miercoles
t2 = float(input("Ingrese el segundo tiempo: "))

#Viernes
t3 = float(input("Ingrese el tercer tiempo: "))

tp = (t1 + t2 + t3) / 3
print("El tiempo promedio entre semana es:", tp)