#edad = 25
#print(edad < 18)

monto = 250
limite = 1000
porcentaje = 10

descuento = 0


if monto>=limite:
    descuento = monto * porcentaje / 100


total = monto - descuento
print (total)