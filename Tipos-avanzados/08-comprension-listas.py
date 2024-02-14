usuarios = [
    ["Chanchito", 4], 
    ["Felipe", 1], 
    ["Pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)
# en el ocdigo de aca arriba vemos una manera facil de agregarle a una variable con lista los nombres de una lista ya existente

# aca abajo vemos una manera mas facil de hacer el codigo e arriba
#Map
# nombres = [usuario[0] for usuario in usuarios]; Aca transformamos la lista para que nos muesrtre solo los nombres, en la variable "nombres" pasadole un ciclo for con una expresion

#filtrar-filter; como dice el nombre filtramos los elementos de una lista usando  el ciclo for y la condicion de If
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

#Filtrar y transformar; y como vemos juntando la transformacion y la filtracion, podemos transformar los elementos y filtrar los mismos elementos es decir
# con la varaible de expresion antes del ciclo for "usuario[0]" tranformamos los varoles del indice 0 y en el if con el "usuario[1]" filtramos los valores del indice 1
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# nombres = list(map(lambda usuario: usuario[0],usuarios ))

menosUsuarios = list(filter(lambda usuario: usuario[1]>2, usuarios))
print(menosUsuarios) 