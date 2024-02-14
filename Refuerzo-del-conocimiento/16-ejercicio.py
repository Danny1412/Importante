# desarrollamos la funcion para desarrollar el problema
def obtener_compañero(cantidad_compañeros):
    
    # Establecemos la lista que necesitamos 
    compañeros = []

    # usamos un bucle for para iterar la lista en total de los datos que le pediremos al usuario
    for i in range(cantidad_compañeros):

        # dentro de nuestro bucle le pedimos los datos al usuario
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad de los estudiantes: ")) # establecemos int dentro de este input ya que el valor que le pedimos aca es un entero
        
        # establecemos la variable que almacenara los datos que le pedimos al usuario "compañero = nombre,edad"
        compañero = (nombre, edad) # recordemos que esta variable se convirtio en una tupla
        compañeros.append(compañero) # a la lista "compañeros" le iremos añadiendo cada dato que ingrese el usuario en "compañero"
    
    # ahora fuera del ciclo arreglaremos nuestros valores de menor a mayor con "sort"
    compañeros.sort(key=lambda x:x[1]) # establecemos [x] el metodo sort para que en la funcion lambda ingrese a nuestros indices [0][0] pero del segundo valor de compañero es decir [1]
    
    # ahora accedemos al primer indice y luego al primer indice dentro de nuestro lista para obtener el valor de asistente
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0] # luego para acceder al ultimo valor de la lista accedemos al indice "-1" que en python es el ultimo indice, y luego accedemos al primer valor dentro de ese indice es decir [-1][0]
    
    # retornamos nuestros valores en la funcion listo para ser ejecutado
    return asistente,profesor

# desempaquetamos nuestra tupla "compañero"
asistente,profesor = obtener_compañero(5) # pasamos los argumentos de la funcion

# mostramos al usuario su programa
print(f"el asistente es: {asistente}, y su profesor es: {profesor}") 