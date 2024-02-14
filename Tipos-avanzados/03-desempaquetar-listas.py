numeros = [1, 2, 3]

#feo
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# de la manera que vemos arriba es una manera no estetica de desempaquetar la lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9 ] #aca tenemos nuestra lista y la forma de desempaquetar se vera acontinuacion
primero, segundo, *otros, penu ,ultimo = numeros # aca al establecer relacion de las varaibles primero segundo etc.
# cuando damos el simbolo de "=" y agregamos nuesra variable de "numeros" establecemos los valores de enteros que estan en la lista
print(segundo, otros, penu)#aca llamamos a cada valor que este relacionado con "numeros"
# y podemos ver como enseñara el valor en la poscicion llamada ylos demas valores de la lista cuando llamamos a "otros"