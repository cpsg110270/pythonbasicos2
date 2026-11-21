# objetivo: Control de gasto de un paseo familiar
# Se debe mostrar un menu de opciones: Visualizar Categoria del gasto, visualizar gastos
# se pueden dreistrar hasta 3 gastos por categorias, no se aceptan gastos negativos
# El gasto a registrar no debe superara el saldo del presupuesto
# Mostrar el total acumulado y la cantidad de gastos.
# clasificar el consumo del presupuesto:
#   90 % o más: presupuesto casi agotado.
#   60 % o más: presupuesto moderadamente utilizado.
#   Menos del 60 %: presupuesto bajo control.

# ============================================================================================

gasto = 0
presupuesto = 0
consumo_porciento = 0
total_gastado = 0
cantidad_gasto = 0
disponibilidad = 0

#Acumuladores por categoria
g_transporte = 0
g_comida = 0
g_entradas = 0

opcion = 0

categorias = [
    "Transporte",
    "Comida",
    "Entradas"
]


def tipo_gasto():
    no_seleccion = True
    tipo = 0

    print ("Elija el tipo de gasto:")
    print ("1. Transpote")
    print ("2. Comida")
    print ("3. Entradas")
    
    while no_seleccion:
        tipo = int(input("Digite la opción: "))   
    
        if tipo <1  or tipo > 3:
            print ("seleccion invalida")
            continue
        else:
            no_seleccion = False
            return tipo


print("=================== Control de Gastos ===================")
presupuesto = float(input("Ingrese el monto del presuluesto: C$ "))
opcion=tipo_gasto()
 