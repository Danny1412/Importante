# Cracion de una Calculadora funcional, donde podemos podeir datos del usuario para procesar y utilizar la informacion 

n1 = input("Ingrese el numero 1")
n2 = input("Ingrese el numero 2")

# transformamos las variables en enteros 
n1 = int(n1) 
n2 = int(n2)

#realizamos los procesos matematicos basicos de una calculadora 
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

# La letra F es para asignar los valores que pedimos de las variables encerradas en llaves 
mensaje = f"""
Para los numeros {n1} y {n2}
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multi es {multi}
el resultado de la div es {div}
"""

print(mensaje)