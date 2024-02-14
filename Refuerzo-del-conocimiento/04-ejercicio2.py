# aca le pedimos a nuestro ususario que ingrese alguna frase
frase = input("Dime una frase, para calcular cuanto tardas en decirla: ")

# cracmos una lista para cada palabra que ingrese el usuario y separarla (se seaaran cuando se cree un espacio blanco)
numero_palabras = frase.split(" ")

# con len(longiud de un string) podemos ver la cantidad de elementos de la lista de separacion
cant_palabras = len(numero_palabras)

# con el if tomamos en cuenta si el ususario escribe un total de palabras equivalentes a 1 min de tiempo
if cant_palabras > 120:
    print("Calma tampoco era un enciclpedia")

# se calcula cuanto tardaria en decirlo, cuanto tardaria dalto, y se lo mostramos al usuario
print(f"dijiste {cant_palabras} palabras, y tardarias {cant_palabras/2} en decirlo")
print(f"Dalto lo diria en {cant_palabras*100 //2*1.3/100} segundos")