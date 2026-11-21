# Si la compra es mayor 1500 el descuento= 15%
# Si la compra es mayor a 800 el descuento = 10%
# Si la compra es mayor a 300 el descuento 
# si la compra es menor a 300 el descuento = 0

compra = float(input("Ingrese el monto de su compra: "))
porcentaje = 0
descuento = 0


if compra >=1500:
    descuento=0.15
    mensaje = "Descuento del 15%"
elif compra >=800:
    descuento=0.10
    mensaje = "Descuento del 10%"
elif compra>=300:
    descuento=0.05
    mensaje = "Descuento del 5%"
else:
    mensaje = "No hay descuento"


total_descuento = compra * descuento
total_pagar = compra - total_descuento

print(" \n=====SUPERMERCADO ======" )
print(mensaje)
print(f"Compra    : C$ {compra:.2f}")
print(f"Descuento : C$ {total_descuento:.2f}")
print(f"Total a pagar : C$ {total_pagar:.2f}")