class Vehiculo:
    color = "azul"
    ruedas = 4
    puertas = 2

class Coche(Vehiculo):
    velocidad = 130
    cilindrada = 150

auto = Coche()
print("El color del auto es :", auto.color)
print("Cantidad de ruedas es : ", auto.ruedas)
print("Cantidad de puertas :  ", auto.puertas)
print("Velocidad Max :  ", auto.velocidad)
print("Cilindrada :  ", auto.cilindrada)

