#ENUNCIADO
#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro
# del archivo.  Para ello, tendréis que acceder dos veces al archivo creado.

f = open('nuevodocumento.txt', 'w')
f.write("Se creo nuevo documento\n")
f.close()

f = open('nuevodocumento.txt','r+')
f.readline()
f.write('se modifica nuevamente el documento.\n')
f.close()

