mascotas = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito Feliz"
    ]
mascotas.insert(1, "Melvin") # con el metodo de insert agregamos elementos a la lista
mascotas.append("Chanchito triste")# aca agregamos un elemento al final de la lista

mascotas.remove("Pulga") # aca eliminamos un elemento el que imtroduzcamos de la lista
mascotas.pop(1) # con esto borramos el ultimo elemento de una lista, y cualquier otro si le pasamos el indice
del mascotas[0] # con este funcion podemos eliminar un elemento pasando el indice
mascotas.clear() # con este metodo eliminamos todos los elementos de una lista
print(mascotas)