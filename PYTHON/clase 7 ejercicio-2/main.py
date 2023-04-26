import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

print("Hora actual =",hora,":",minutos)

print()
if int(hora) >= 7:
    print("Es hora de irse a casa")
else:
    print("Restan {} horas y {} minutos para terminar la jornada laboral".format(6- int(hora), 59 - int(minutos)))

