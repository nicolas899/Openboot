#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

class vehiculo:

    def __init__(self, ruedas, puertas, asientos):
        self.ruedas = ruedas
        self.puertas = puertas
        self.asientos= asientos

    def getInfo(self):
        return self.ruedas, self.puertas, self.asientos


auto = vehiculo(4,2,5)
print(auto)
print(auto.getInfo())

f= open('datos.bin', 'wb')
pickle.dump(auto, f)
f.close()


f = open('datos.bin', 'rb')
miAuto = pickle.load(f)
f.close()

print(miAuto.getInfo())


