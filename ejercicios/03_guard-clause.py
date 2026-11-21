def valida_compra(monto):
    if monto <= 0:
        return "Monto invalido"
    if monto > 5000:
        return "Requiere autorizacion"

    return"Compra permitida"


print(valida_compra(250))
print(valida_compra(0))
print(valida_compra(6000))