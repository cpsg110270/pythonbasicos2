nombre = input("Ingrese su nombre: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Digite la cantidad: "))

#precio_unitario = 125.5
#cantidad = 3
descuento_porcentaje = 10

subtotal = precio_unitario * cantidad
descuento = subtotal * (descuento_porcentaje/100)
total = subtotal - descuento

print ("RESUMEN DE COMPRA")

print (f"Sub Total: C$ {subtotal:.2f}")
print (f"Descuento: C$ {descuento}")
print (f"Total    : C$ {total}")

print(total > 300)