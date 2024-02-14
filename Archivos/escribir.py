with open('Archivos\\textolol.txt',"w",encoding="UTF-8") as archivo:
    # sobreescribiendo el archivo
    # archivo.write("JAJAJAJAJ te la meti")
    
    # agregando 2 lineas con writelines()
    archivo.writelines([" - Hola guapo\n", " - misericordia\n"])

    # agregando otras dos lineas
    archivo.writelines([" - quiero follarte\n", " - yo tambien"])