animales = ["gato","perro","loro","cocodrilo"]
numeros = [10,62,12,70]

# como recorrer o iterar la lista animales con for
for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")

# recorriendo lista numeros con for
for numero in numeros:
    resultado = numero * 10
    print(resultado)

# con la funcion zip podemos recorrer dos lista al mismo tiempo, del mismo tamaño
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorrienda lista 2: {animal}")

# forma no optima de recorrer una lista(no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de recorrer una lista con su idice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")

nume1 = (5,7,9,11,13)

for num,i in enumerate(nume1):
    print(num,i)

#usando el for/else
for numero in numeros:
    print(f"ejecutnado el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")

# todo funciona con tuplas de la misma manera que para las listas al igual que los conjuntos