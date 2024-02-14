# Como podemos ver esta funcion definida como hola, nos representa el codigo dentro de ella
# el cual se refleja al ausuario por la consola
# al final vemos como repetimos "hola()" para hacer el llamado a la funcion y que esta se pueda ejecutar
# def hola():
#     print("hola mundo!")
#     print("ultiamte python")

# hola()

# En el caso de "apellido="feliz" estamos pasando un valor al parametro de la funcion el cual se agregara si el argumento no lo posee
def hola(nombre, apellido="feliz"): # Parametros # Cuando usamos la varaible de la funcion dentro de la misma funcion se cosidera parametro
    print("hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")

hola("Nicolas", "Schurman")
hola("chanchito") # Argumentos # Aca estamos argumentando la variable mas no la usamos, asi que esto es un argumento


# Aca le estamos pasando a los argumentos, el valor que poseeran los parametros
hola(apellido="Schurman", nombre="Bolo")
