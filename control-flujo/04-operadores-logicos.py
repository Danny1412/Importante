# and, or, not
# Los operadores logicos mencionados anteriormente se pueden evaluar de distintas formas
# como se puede observar en el codigo de abajo se prueban dichos operaciones logicos

gas = False
encendido = True
edad = 18

if  not gas and (encendido or edad > 17):
    print("Puedes avanzar")

# Para una operacion de corto circuito And evalua lo que esta a la izquierda e idenpendientemente de si es verdadera o falso se tomara en cuenta la de la derecha
# Si es Or en una operacion de corto circuito solo se necesita una verdadera la izquiera para descartar el valor de la derecha, a menos que sea falso se tiane b cuenta el valor adyacente
