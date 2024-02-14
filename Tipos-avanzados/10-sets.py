# set significa grupo o conjunto
# como sabemos que son los sets, ahora podemos ver como trabajarlos 
primer = {1, 1, 2, 2, 3, 4} # aca tenemos nuestro primer set el cual se establece encerrando el contenido en "{}"
segundo = [3, 4, 5] # aca creamos una lista
# Y lo interesante es que "set" es un iterable, y como cualquier iterable podemos agergarle nuestra lista que son iterables
segundo= set(segundo) 

# los sets eliminaran elementos repetidos como vemos en el primero de "1" y "2"
# y ademas nuestros sets trabajan con los siguientes operadores
print(primer | segundo) # con este operador lo que hace es tomar los datos de nuestro primer set y agregarle los del segundo, claramente quitandole los elementos repetidos entre ambos sets
print(primer & segundo) # con este operador nos da los elementos en medio del set los  cuales son "3" y "4"
print(primer - segundo) # este operador es de diferencia los cuales calculan que diferencia hay entre dos sets quitandole la diferencia que encuentre al primer set
# es decir en la primera parte tenemos 1 y 2 y en la segunda 2 y 3, como tenemos 2  y 3 eliminara el primer 2 y luego el 3 dandonos el 1 de la izquierda y el dos de la derecha quitando los datos a los elementos del primer set
print(primer ^ segundo) # con este operador establecemos una direfencia simetrica el cual lo que hace es eliminar los numeros duplicados y agregara el numero no duplica si es que este existe
# entonces como en nuestros dos sets sacamos 3 y 4 porque ambos existen en los dos sets

# algo a tener en cuenta es que no podemos acceder a ningun elemento del set, pero si trabajarlos
# en el if de abajo podemos  ver como si usamos el int de 5 para saber si esta en segundo, ejeuctaremos nuestro codigo, esta es una manera de trabajar con los sets
if 5 in segundo:
    print("hola mundo")