lista =[1, 2, 3, 4]
# print(1, 2, 3, 4)
# print(*lista)

lista2 = [5, 6]

combinada =  ["hola", *lista, "mundo", *lista2,]
print(combinada)
# como podemos ver en el codigo de arriba usamos un operador de desempaquetamiento para desempaquetar las lsitas ya existentes
# ademas de que se pueden agregar elemento dentro de la lsita ya desempaquetada

# Ahora veremos como funciona el operador de desempaquetamiento entre los diccionarios
# establecemos nuestros diccionarios "punto1", "punto2"
punto1 = {"x": 19, "y": "hola"} # como vemos aca al imprimir esta llave "y" no se muestra ya que el valor se asigna de derecha a izquierda al reconocer que el valor de "x" ya esta llamado en la operacion de desempaquetado ya se asigno este valor por lo tanto "y" no se mostrara
punto2 = {"y": 15}

# ahora desempaquetamos los diccionarios el operador para estos es "**"
nuevoPunto = {**punto1, "lala": "Hola mundo", **punto2, "z": "Mundo"} # lo que si podemos hacer es agregar llaves en nuestro nuevo diccionario desempaquetado
print(nuevoPunto)
# y como vemos se agregan los diccionarios de "punto1" y "punto2", luego se agerga la llave "lala" y por ultimo la llave de z
# Gracias por todo