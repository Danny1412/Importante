#creamos lista
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20]

# crear una funcion lambda para multiplicar dos nuemros
# multi = lambda x: x*2 # la funcion realiza el proceso que le agreguemos de manera unica y rapida 
# print(multi(5)) # le pasamos el valor de "x" para que realice la operacion agregada en la funcion

# # creando una funcion que diga numeros pares e impares
# def es_par(num):
#     if (num%2==0):
#         return True
# # con el metodo de filter relizamos el proceso de la funcion
# numeros_par= filter(es_par,numeros)

# ahora toda la funciona anterior la crearemos con lambda

numeros_par = filter(lambda numero: numero%2==1, numeros)

print(list(numeros_par))