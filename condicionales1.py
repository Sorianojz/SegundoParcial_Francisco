"""1) En una fabrica de computadoras se planea ofrecer a los clientes un descuento que dependera del numero de
computadoras que compre. < de 5 = 10%, >= de 5 pero < de 10 = 20%, >= 10 = 40%. 
El precio de cada computadora es de $11,000 """
#Jesús Francisco Soriano Zamarripa
#Programación II
#22/04/2026

nc = int(input("Ingrese el numero de computadoras compradas: "))

if nc < 5:
    cp = nc * 11000
    d = cp * 0.10
    pt = cp - d
    print("El precio original es", cp)
    print("El precio con descuento es", pt)

if nc >= 5 and nc < 10:
    cp = nc * 11000
    d = cp * 0.20
    pt = cp - d
    print("El precio original es", cp)
    print("El precio con descuento es", pt)

if nc >= 10:
    cp = nc * 11000
    d = cp * 0.40
    pt = cp - d
    print("El precio original es", cp)
    print("El precio con descuento es", pt)