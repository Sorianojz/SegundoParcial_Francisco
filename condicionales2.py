"""2) En un juego de preguntas y repuestas de SI o NO gana quien responda correctamente las 3 preguntas.
Si se reponde mal cualquiera de ellas, ya no se puede responder la siguiente y termina el juego"""
#Jesús Francisco Soriano Zamarripa
#Programación II
#23/04/2026

p1 = print("¿Colon descubrio America?")
r = str(input("Ingrese su respuesta: "))
if r == "SI" or r == "Si" or r == "si":
   print("¿La independencia de México fue en el año 1810?")
   r = str(input("Ingrese su respuesta: "))
   if r == "NO" or r == "No" or r == "no":
        print("¿The Doors fue un grupo de rock Americano?")
        r = str(input("Ingrese su respuesta: "))
        if r == "SI" or r == "Si" or r == "si":
            print("!Felicidades completaste todas las preguntas¡")
        elif r == "NO" or "No" or "no": print("Fin del juego")
   elif r == "SI" or "Si" or "si":
       print("Fin del juego")
elif r == "NO" or "No" or "no": print("Fin del juego")