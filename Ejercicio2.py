###Ejercicio 2

###Escribir una función que reciba un número entero positivo y devuelva su factorial.

### Primer metodo
'''def factorial():
    num = int(input("Ingresa tu numero entero y positivo: "))
    if num > 0:
        factorial = 1
        for i in range(1 , num + 1):
            factorial = factorial * i
        print(factorial)
    else:
        print("El numero es negativo y no podemos proceder")

factorial()'''

###Segundo Metodo, mas rapido
def factorial():
    from math import factorial
    num = int(input("Ingresa tu numero entero y positivo: "))
    if num > 0:
        print(factorial(num))      
    else:
        print("El numero es negativo y no podemos proceder")

factorial()