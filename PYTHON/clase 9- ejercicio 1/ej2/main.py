#En este segundo ejercicio, tenéis que crear una aplicación
# que obtendrá los elementos impares de una lista pasada por parámetro con filter
# y realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce

valor = [11, 20, 30, 10, 5, 2, 4, 8, 9, 22, 31, 13]
resultado = list(filter(lambda x: x % 2!=0, valor))
print(resultado)

def suma(a,b):
    return a + b

res = reduce(suma, resultado)
print(res)




