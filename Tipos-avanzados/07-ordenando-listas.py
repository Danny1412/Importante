numeros = [4, 5, 90, 13]

# numeros.sort(reverse=True) # la funcion de sort nos ordena la lista de menor a mayor
# con el parametro de "reverse=True", nos ordena la lista solo que de mayor a menor
numeros2 = sorted(numeros) # la funcion de sorted ordena los elementos de una lista solo que en vez de ser la lista que tenenmos crea una lista totalmente nueva
print(numeros)
print(numeros2)

# aca creamos otra lista con la varaible de usuarios la cual se puede ordenar de distintas maneras
# Como vemos en la lista hay valores que indican que numeracion tienen
usuarios = [
    ["Chanchito", 4], 
    ["Felipe", 1], 
    ["Pulga", 5]
    ]
# Si usamos Sort con la numeracion enfrente de los strings este la ordenada directamente pero si pasamos esto despues de los strings ahremos lo siguiente
def ordena(elemento):
    return elemento[1]
# # Debemos crear una funcion para poder indicarle a sort como queremos que ordene los elementos 
# # para ello debemos retornar el primer elemento es decir el ennumerado "1" en la funcion
# # ahora que la funcion retora los valores debemos pasarsela al metodo sort, y con la funcion de key en el metodo sort
# usuarios.sort(key=ordena, reverse=True)
# # la funcion de key se usa para llamar los argumentos dentro de la funcion, ya que si se llama por sola a la funcion el sort no lo validara ya que no tomar argumentos no posicionados
# # aca tambien podemos usar la funcion de reverse para darle vuelta si queremos
print(usuarios)


usuarios.sort(key=lambda el:el[1])
print(usuarios)
# aca arriba podemos observar una expresion anonima para ordenar nuestro listado ahorrandonos el proceso de mas arriba, el cual sera habilitar una funcion y luego pasarsela a "key"
# La Expresion anonima no es una mala practica si solo  se usaa para un funcion que solo se ejecuara una vez, es mala practica si la usamos en todo nuestro codigo 