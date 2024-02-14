# Manera optima de abrir un archivo con "with open"    
with open("Archivos\\Notaslol.txt", encoding="utf-8") as archivo:
    
    # leemos el archivo
    contenido = archivo.read()

    # mostramos el contenido
    print(contenido)

# no es necesario cerrarlo usando "with open"