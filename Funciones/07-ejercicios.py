def no_space(texto): # aca definimos la funcion de no espacios la cual elimina los espacios de cualquier string que nosotros pasemos 
    nuevo_texto = "" #establecemos la variable la cual usaremos en nuestra condicion
    for char in texto: # iteramos en sentido a caracteres
        if char != " ": # aca establecemos que un espacio es diferente a un string vacio 
            nuevo_texto += char # luego haacemos que la funcion elimine todos los espacios existentes en el string
    return nuevo_texto


def reverse(texto): # en esta funcion damos vuelta al texto veamos como funciona 
    texto_al_reves= "" # como siemrpe un string vacio para dar a entender que la varaible se debe llenar con los valores que le pasemos de las palabras
    for char in texto:
        texto_al_reves = char + texto_al_reves 
    return texto_al_reves
# aca cumplimos la funcion de dar vuelta a la palbra ya que usando "char + texto al reves", toma la oracion o la palabra y le dan vuelta es decir, tomando los caracteres de derecha a izquierda en ves de izquierda a derecha

def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()
# Aca tendriamos la funcion en su totalidad uniendo las funciones de "no_space" y la de "reverse" dando asi el resultado al problema que nos muestre que palabras son palindromos o no

print (es_palindromo("Amo la paloma"))
print (es_palindromo("hola mundo"))
print (es_palindromo("reconocer"))