# objetivo: Registrar los gastos del día
# Se debe solicitar el monto del gasto
# Condiciones
#   monto = 0   ->  Dar por finalizada el procedimiento (break)
#   monto < 0   ->   Omitir registro (continue), enviar mensaje de error
# Acumular los gastos del dia (total_g)
# Totalizar el numero de transacciones (total_t)

# ======================================================================

#monto = 0
total_g = 0
total_t = 0
total_e = 0
continua = True

while continua   :
    monto = float(input("Ingrese un gasto (0 para finalizar): "))

    if monto < 0:
        print ("No se acetan montos negativos... Verifique!!!")
        total_e += 1
        continue
    elif monto == 0:
        continua = False
        break
    else:
        total_g += monto
        total_t += 1


print ("\n========= Registo de gastos =========")
print (f"Total de gastos: C$ {total_g:.2f}")
print (f"Total de transacciones validas: {total_t}")
print (f"Total de transacciones con error: {total_e}")