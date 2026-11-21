# Tarifa
# Pedir diatancia al usuario
# evaluar valor introducido por el usuario
# Si valor negativo  o  cero,  indicar que no es un valor correcto
# Hasta 3KM  -> C$ 30
# Mas de 3 hata 8 -> C$50
# Mas de 8 -> C$ 75




distancia = float(input("Ingrese la distancia: "))
tarifa = 0
mensaje = "Distancia valida"


if distancia <= 0:
    tarifa = 0 
elif distancia <= 3:
    tarifa = 30
elif distancia >3 and distancia <= 8:
    tarifa = 50
else:
    tarifa = 75

print(" \n=====valor del envio ======" )

if tarifa<=0:
    print("Distancia invalida, verifique!!!!!!")
else:
    print(f"Tarifa por Km    : C$ {tarifa:.2f}")
    
    print(f"Distancia  : {distancia:.2f}")

