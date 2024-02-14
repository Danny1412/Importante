# crando dicc con dict()
dicc = dict(nombre = "lucas", apellido = "dalto")

# las listas son editables, por lo tanto no se pueden crear en diccionarios con ellas a modo de llaves
dicc2 = {frozenset["dalto", "rancio"]: "jajas"}

# crear diccionario con fromkeys() valor por defecto: none
dicc3 = dict.fromkeys(["nombre","apellido"])

# crear diccionario con fromkeys() valor de defecto "i dont know"
dicc3 = dict.fromkeys(["nombre","apellido"], "i dont know")


print(dicc3["nombre"])
