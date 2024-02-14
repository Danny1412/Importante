
# creando la funcion
def sumar_dos():
    # creamos un bucle
    while True:
        # pedimos los datos
        a = input("Numero 1: ")
        b = input("Numero 2: ")
       # se convierten a enteros y se suman
        try:
            resultado = int(a) + int(b)           
        # si se genera un excepcion, que reingrese los datos nuevamente
        except ValueError as e:
            print("te pedi un numero")
            print(f"ERROR: {e}")
        # si el bucle se ejecuta bien, terminamos el bucle
        else:
            break
        # finally se ejecuta siempre
        finally:
            print("Manejo de excepcion finalizado")
    # mostrando el resultado
    return resultado

print(sumar_dos())