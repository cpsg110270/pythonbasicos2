pin=1111
intento = 1

while intento < 4:
     print("\n")
     pin1 = int(input("Ingrese su numero PIN: "))

     if pin != pin1:
          intentos_restantes =  3 - intento
          print("Vuelva a digitar el PIN")
          print(f"Intentos restantes: {intentos_restantes}")
          intento = intento + 1
          valido = False
     else:
          valido = True
          break


if valido:
     print ("Acceso Autorizado !!!!!")
else:
     print ("Usuario bloquedo!!!")


