# al establecer en el parametro el signo "*" y la varaible numeros damos a entender que son iterables

def suma(*numeros):
    resultado = 0
    for numero in numeros: # a partir de aca ya se establecio la funcion del parametro en el ciclo, el resto ya es la funcion del codigo
        resultado += numero
    print(resultado)

# Luego aca en los argumentos tenemos varios valores enlazados a la funcion
# Como en el parametro estableciomos que son varios argumentos todos se convierten iterables los cuales se evaluan en un ciclo for
suma(2, 5, 7) 
suma(2, 5)
suma(2, 8, 7, 45, 32)

# Toda la funcion realizada anteriormente es para demostrar de que manera se puede darle al parametro varios valores con los argumentos
