import re

texto = '''Hola maestro, esa es la cadena 1. como estas mi capitan
Por aca podemos seguir escribiendo el sexo 24312431  aababab
Por esta abaabab 4
por aca cerramos 5 capo'''

# realizando una busqueda simple
# resultado = re.findall("aca", texto)

# \d -> busca digitos numericos del 0 - 9, en el texto
# resultado = re.findall(r"\d",texto)

# \D -> busca Todo menos digitos numericos del 0 - 9, en el texto
# resultado = re.findall(r"\D",texto)

# \w -> busca caracteres alfa numerricos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\w",texto)

# \W -> busca Todos los caracteres menos alfa numerricos [a-z A-Z 0-9 _]
# resultado = re.findall(r"\W",texto)

# \s -> busca espacios en blanco -> espacios, tabs, saltos de linea
# resultado = re.findall(r"\s",texto)

# \S -> busca Todo menos espacios en blanco -> espacios, tabs, saltos de linea
# resultado = re.findall(r"\S",texto)

# . -> busca Todo menos saltos en linea
# resultado = re.findall(r'.',texto)

# \n -> busca saltos en linea
# resultado = re.findall(r"\n", texto)

# \ -> cancelamos caracteres especiales, "cancelamos la funcion del punto y buscamos puntos"
# resultado = re.findall(r'\.',texto)

# armando una cadena buscando numeros seguidos de un texto y seguido de un punto y un espacio
# resultado = re.findall(f"\d\.\s", texto)

# ^ -> busac el comienzo de una linea (Buscamos hola al principio), solo lo que esta en el principio (maestro no esta)
# flags = re.M deja la multi linea activa
# resultado = re.findall(f"^Por",texto,flags=re.M)

# $ -> busca el final de una linea
# resultado = re.findall(r"capo$",texto,flags=re.M)

# {n} -> busca n cantidad de veces el valor de la izquierda (3 numeros juntos esta vez)
# resultado = re.findall(r'\d{3}\s',texto)

# {n,m} -> al menos n, como maximo m
# resultado = re.findall(r'[ab]{2}',texto)

# | -> busca una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola',texto)

print(resultado)