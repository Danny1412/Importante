# el for sirve para muchas funciones, pero su principal es iterar listas de elementos
# El uso normal de for es cumplir la funcion de codigo dado, en un rango de numeros

buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontre el numero buscado")

for char in "Ultiamte python":
    print(char)