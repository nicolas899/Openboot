class Alumno:
    nombre : ""
    nota : 0

    def calcular(self, nuevaNota):
        self.nota = nuevaNota
        if nuevaNota >= 4:
            resultado = "Aprobado"
        else:
            resultado = "Aplazado"
        return resultado

    def cambiarNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        return nuevoNombre


a1 = Alumno()
nombre1 = a1.cambiarNombre("Nicolas")
nota1 = a1.calcular(3)
print("Nombre del alumno:" , nombre1)
print("Nota del alumno:", a1.nota)
print("La condicion del alumno es : ",nota1)