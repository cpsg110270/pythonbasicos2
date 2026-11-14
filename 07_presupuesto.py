print("DATOS DE LA ORDEN")
print("-------------------")
des_producto = input("Descripción del producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Digite la cantidad: "))
presupuesto = float(input("Presupuesto Disponible: "))



total = precio_unitario * cantidad
diferencia = presupuesto - total
 



print ("RESUMEN DE COMPRA")
print("-------------------")
print (f"Producto         :    {des_producto}")
print (f"Cantidad Ordenada:    {cantidad}")
print (f"Precio unitario  : C$ {precio_unitario:.2f}")
print (f"Total            : C$ {total:.2f}")
print (f"Presupuesto      : C$ {presupuesto:.2f}")
print ()
print ()

print ("RESULTADO")
print("-----------")
print ("Disponibilidad presupuestaria")  
if diferencia < 0:
    print("Presupuesto insuficiente, elija otro producto o lleve menos unidades"
)
else:
    print("Proceda con la compra, tiene fondos disponibles")

print ("----- Ultima linea -----")


 