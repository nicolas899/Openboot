def comprobar(ano):
    valor = ano % 4
    return valor


esBiciesto = comprobar(2029)
if esBiciesto == 0:
    print("Es un año Biciesto")
else:
    print("No es un año Biciesto")
