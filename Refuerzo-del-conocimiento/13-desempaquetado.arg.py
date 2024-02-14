# manera no optina de sumar valores con funciones
# def suma(lista):
#     numero_sumado=0
#     for numero in lista:
#         numero_sumado = numero_sumado + numero
#     return numero_sumado

# resultado = suma([5,3,9,10,20,3])

# manera optina de sumar valores 
def suma_total(numeros):
    print(*numeros)
    return sum([*numeros])

resultado2 = suma_total([5,3,9,10,20,3])

# lo mismo que arriba, con el operador * como parametro (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma ("lucas",5,3,9,10,20,3)
# print(resultado)

