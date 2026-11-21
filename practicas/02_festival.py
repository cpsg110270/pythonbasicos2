# Obtener precio de entrada a fertiva de acuerdo a:
# Edad
# Tarifa segun grupo etario:
#   +12             -> 50   -> Niño
#   entre 12 y 15   -> 80   -> Adolecente 
#   entre 18 y 64   -> 120  -> Adulto
#   Mayor de 64     -> 70   -> Adutlo mayor
# Si tiene bono promosional, aplicar descuento del 10%
# Salida del programa
#   Categoria del visitante
#   Precio original
#   Descuento
#   Total a pagar

#Inicialilzacion de variables
edad = 0
categoria = ""
precio = 0
descuento = 0
total_pagar = 0
bono="N"


edad = int(input("Ingrese su edad: "))
bono = str(input("Tiene bono promocional s/n? "))

# Consturyento categorias y asignando tarifa
if edad > 0 and edad < 12:
    categoria = "Niño"
    tarifa = 50
elif edad <= 17:
    categoria ="Adolecente"
    tarifa = 80
elif edad<= 64:
    categoria = "Adulto"
    tarifa = 120
else:
    categoria = "Adulto mayor"
    tarifa = 70

if bono == "S" or bono =="s":
    descuento = tarifa*0.10

total_pagar = tarifa - descuento

print ("\n========== Entrada Festival ==========\n")
print (f"Edad             : {edad}")
print (f"Categoría        : {categoria}" )  
print (f"Bono promocional : {bono} " )
print (f"Precio orginal   : C$ {tarifa:.2f} " )
print (f"Descuento        : C$ {descuento:.2f}" )
print (f"Total a pagar    :  C$ {total_pagar:.2f} " )
