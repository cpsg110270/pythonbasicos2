contador = 1

while contador <= 5:
    print (f"Paso numero {contador}" )
    contador = contador + 1
     

meta = 500
ahorrado = 0

while ahorrado < meta:

    aporte = float(input("Cuanto desea ahorrar ? C$ "))

    if aporte <= 0:
        print("El aporte debe ser mayor de cero")
        continue
    ahorrado += aporte
    print(f"Total ahorrado: C$  {ahorrado:.2f}")

print ("Felicidades!!!! Has alcanzado la meta")