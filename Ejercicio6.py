###Ejercicio 2

###Escribir una función que reciba una muestra de números en una lista y devuelva su medida.

def medida(*tupla):
    print(len(tupla))

medida (2, 3, 4, 10, 20)

def medida(*tupla):
    print(len(tupla))
    for i in tupla:
        print (i)
    return(len(tupla))

print(medida (2, 3, 4, 10, 20))