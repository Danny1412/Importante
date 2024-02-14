def get_product(**datos): #al usar un parametro con doble "**" lo convertimos en un iterable el cual cumplira la funcion de varios argumentos
    print(datos["id"], datos["name"])
# En el print de arriba se observa como se llama al parametro principal y en corchetes llamamos a los sub-parametros, para tomar su valor"argumento" y mostrarlo en pantalla

get_product(id="23", 
            name="Iphone",
            desc="Esto es un Iphone",
            ) # Aca como podemos ver los que podemos considerar sub-parametros como "id", "name", "desc"
# Poseen argumentos como "23", "Iphone", lo que sucede es que a estos parametros les asignamos estos argumentos en sentido de valor
# lo cual nos ayuda a poder usar todos los parametros que deseemos con todos los argumentos que queramos 