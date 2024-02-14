mascotas = ["Pelusa","Wolfgang","Felipe","Wolfgang","Chanchito Feliz"]

print(mascotas.count("Wolfgang"))
#Con el print de arriba usamos el metodo count o contar para ver cuantas veces hay un elemento en la misma lista
# en este caso nos muestra que lo hay 2 veces pero solo encuentra el indice 1 por lo tanto alguno de los dos elementos repetidos se debe eliminar
if "Wolfgang" in mascotas:
    print(mascotas.index("Wolfgang"))
# Con el metodo de index buscamos el elemento de la lista por el indice que le corresponda en este caso 3
# Esta busqueda se realiza con una condicional If 