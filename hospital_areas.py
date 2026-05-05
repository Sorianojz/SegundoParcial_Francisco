"""6) En un hospital existen 3 areas: Ginecologia, Pediatria, Traumatologia.
Presupuesto anual: Ginecologia 40%, Traumatologia 30%, Pediatria 30%
Obtener la cantidad de dinero que recibira cada area, para cualquier monto presupuestal"""
#Jesús Francisco Soriano Zamarripa
#Programación II
#20/04/2026

monto = float(input("Ingrese el valor del monto: "))
areaG = monto * 0.40
areaT = monto * 0.30
areaP = monto * 0.30
print("El presupuesto para cada area del hospital es: Ginecologia:", areaG, "Traumatologia:", areaT, "Pediatria:", areaP)