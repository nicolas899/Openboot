import calculadora
## CARGAMOS LOS VALORES
valor1= calculadora.operaciones()
valor1.valores(5,2)

valor2 = calculadora.operaciones()
valor2.valores(10,5)

## LLAMAMOS A LOS OPERACIONES CORRESPONDIENTES

valor1.sumar()
valor1.restar()
valor1.multiplicar()
valor1.dividir()

print("")
valor2.sumar()
valor2.restar()
valor2.multiplicar()
valor2.dividir()
