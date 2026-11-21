def valida_retiro (saldo,monto):
    if saldo < 0:
        mensaje ="Existe error en la informacion, vefirique"
        return mensaje
    
    if monto <=0 :
        
        return "Rechazar operación, monto no puede ser cero(0)"

    if monto > saldo:
        return "Rechazar transacción, monto no debe superar saldo."

    saldo_actual =  saldo-monto

    return f"Autorizar transacción. El saldo restante es: C$ {saldo_actual}", saldo_actual


saldo = float(input("Ingrese el saldo: C$ "))
monto = float(input("Ingrese el monto: C$ "))
print(valida_retiro(saldo,monto)) 
