punto = {"x": 25, "y": 50} # aca creamos un pequeño diccionario, el cual se arma de la siguiente manera, al abrir el parentesis de llaves
# tenemos que agrergar las dos llaves que en este caso se armande de la llave va  a la izquierda y siempre es un formato de string aagregamos ":" y a la derecha el valor que se le asigna que puede ser cualquiera
print(punto)
# los diccionarios al llaamr al valor que posea la llave no cuenta como una lista asi que este valor no se puede modificar solo imprimir en pantalla
print(punto["x"]) # y para imprimir los valores se debe llamar al string que lo contenga en este caso "x"
print(punto["y"]) # en este caso igual como arriba llamamos a "y"

# en la representacion de abajo agregamos un valor mas a la llave 
punto["z"] = 45

# print(punto, punto["lala"])
if "lala" in punto:
    print("econtre lala", punto["lala"])
# como vemos en el if de aca arriba si la llave que se busca no esta agregada o directamente llamada en el diccionario no aparecera

# aca anajo vemos la funcion un metodo llamado "get" que lo traen los diccionarios de manera predeterminada
print(punto.get("x")) # pasamos un string como argumento, asi que le pasamos la llave de "x" lo cual nos devolvera el valor de la misma llave "25"
print(punto.get("lala", 97)) # con get tambien podemos agregar valores a elementos no existentes como "lala", la cual le acabamos de asociar el valor de 97
del punto["x"] # asi podemos eliminar las llaves junto con su valor
del(punto["y"]) # asi tambien se puede eliminar una llave asociada al diccionario lo que se hace con "del (punto["llave a eliminar"])"

print(punto)
punto["x"] = 25 # agregmos de nuevo el valor

# podemos iterar las llaves con sus valores, usando for, pero si usamos anda mas print(valor) solo nos dara las llaves asociadas al diccionario
for valor in punto:
    print(valor, punto[valor]) # para imprimir el valor de las llaves, debemos llamar al diccionario "punto" y pasarle el valor con "[]"
# y ya con eso nos enseña el valor de "x" y "z", la sintaxis de arriba no es necesario en todos los casos

# aca utilizamos otra sintaxis para realizar lo mismo de arriba
for valor in punto.items(): # con el metodo items, lo que sucede con este metodo si se defina mal, nos devuelve todo como tuplas
    print(valor)
# lo cual por lo que sabemos las tuplas no se modifican, pero si se pueden desempaquetar

# aca establecemos los desempaquetados con las varaibles de "llaves, valor"
for llave, valor in punto.items(): # establecemos nuestras varaibles para la funcion de items desempaquete las tuplas
    print(llave, valor) # solo imprimimos en pantalla nuestras variables y ya
# deberia salir nuestras llaves con sus valores

# en el sig, diccionario observaremos el uso de un diccionario de forma correcta, similado a como fuciona una base de datos
# establecemos nuestra variable y dentro ella creamos una lista, lista la cual le pasaremos nuestro diccionario el cual contendra lo sig
usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]
# como podemos ver el diccionario esta separa en sus propias llaves"{}", las cuales contienen las llaves y sus valores que son "id": 1, "nombre": "Chanchito"
# lo cual sabemos que son elementos iterables, asi que ahora sacaremos sus nombres

for usuario in usuarios:
    print(usuario["nombre"])
# con la funcion for creamos nuestra variable de "usuario in usuario"
# llamaremos a los nombres de nuestras llaves de nuestro diccionario