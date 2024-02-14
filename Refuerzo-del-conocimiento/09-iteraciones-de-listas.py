frutas = ["banana","manzana","cireula","pera","naranja", "granada","durazno"]
cadena = "hola dalto"
numeros = [2,5,8,10]

# con el metodo continue, se salta un elemento de nuestra lista, evitando que se muestre en pantalla
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"me voy a comer una: {fruta}")

# utilizamos el metodo break, hacemos que el cilo se detenga hasta que llegue al elemeno que le indicamos(el "else" no se ejecuta)
for fruta in frutas:
    print(f"me voy a comer una: {fruta}")
    if fruta == "pera":
        break
else:
    print("terminado")

# recorremos una cadena de texto

for letra in cadena:
    print(letra)


# for en una linea de codigo(es decir iteramos la variable en una linea de texto)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
