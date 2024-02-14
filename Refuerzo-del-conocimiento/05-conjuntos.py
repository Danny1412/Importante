# creando un set()
cojunto = set(["Dato 1"])

# insertando un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)

#teoria de conjuntos

conjunto1 = {1, 3, 5, 7}
conjunto2 = {2, 4, 6, 7}

# estos siempre arrojaran valores Boleanos

# confirmado el sunconjunto
resultado =  conjunto2.issubset(conjunto1) # con este metodo issubset() damos a entender si un conjunto es un subconjunto de otro, el programa se encargara de validarlo
resultado = conjunto2 <= conjunto1 # esta es otra forma de verificar

# confirmado el sunconjunto
resultado =  conjunto1.issuperset(conjunto2) # con este metodo issubset() damos a entender si un conjunto es un subconjunto de otro, el programa se encargara de validarlo
resultado = conjunto1 > conjunto2 # esta es otra forma de verificar

# verificar un numero igual
resultado = conjunto2.isdisjoint(conjunto1) # cuando hay un numero igual arrojara false ya que hay un numero igual entre los dos conjuntos
# si no hay numero igual sera true ya que son conjuntos totalmente distintos
 
print(resultado)
