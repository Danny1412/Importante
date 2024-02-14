dicc = {"Nombre": "Lucas", "apellido": "Dalto", "sub": 10000}

# Con keys devuelve un objeto dic.item, un elemento iterable
llaves = dicc.keys()

# con get, si el valor existe o no independientemente el programa continua y dara por si que el elemento no existe dejandolo con "none"
valordeasdad = dicc.get("asdad")
print("Vamo adelante")

# con el metodo "clear, elimina todo lo del diccionario
# dicc.clear()

# con "pop", eliminamos el elemento que seleccionemos del diccionario 
dicc.pop("sub")
print(dicc)

# con el valor de items, obtenemos un elemento iterable
dicc_ite = dicc.items()

print(dicc)