#aca estamos creando una tupla, una tupla es un tipo de dato no cambiante es decir no puede cambiarse con nada ni agregar ni eliminar su contenido
numeros = (1, 2, 3) + (4, 5, 6)
print (numeros)

# las tuplas como vemos abajo recibe todo tipo de dato que sea iterable
punto = tuple([1, 2])
print(punto)

# podemos modificar las listas que contenga la tupla es decir, podemos hacer que nos muestre todo el contenido o no
menosnumeros = numeros[:2]
print(menosnumeros)

# Podemos mostrar los valores que deseemos o enseñar los primeros valores y luego el resto pero aun asi no modificamos la "Tupla" en sí
primero, segundo, *otros = numeros
print(primero, segundo, otros)

# y como sabemos las tuplas trabaja con todo tipo de dato que sea iterable
for n in numeros:
    print(n)

# como sabemos las tuplas no se pueden modificar, en dado caso podemos modificar su contenido, pero esta mdificacion recae en un nuevo contenido es decir
# podemos modificar la lista dentro de la tupla en base a la tupla que usamos, pero como dije se cambia la lista no la tupla
# solo se modifico la lista en base a la tupla y no la tupla directamente, como vemos en el ejemplo mas abajo
listanumeros = list(numeros)
listanumeros[0] = "Chanchito feliz"
print(listanumeros)

# Las tuplas son la mejor a la hora de leer datos, es decir manejar datos de un unico valor y que lo unico que necesitan es recorrer el dato sin la necesidad de modificarlo