def valores():
    global num1
    global num2 ### con global, se pueden usar las variables para otras funciones. Primero se engloba y luego se asigna el valor
    num1 = 110
    num2 = 40
    resultado = num1 + num2
    return resultado

print(valores())
print(valores())
print(valores())

resta = num1 -  num2
print(resta)