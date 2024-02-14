mascotas = ["Wolfgang","Pelusa", "Pulga", "Copito"]
print(mascotas[0])
mascotas[0] = "Bicho" # aca cambiamos el valor del indice cero por "Bicho", es decir "Wolfgang" ahora es "Bicho"
# print(mascotas)
# print(mascotas[2:]) #aca mostramos a partir del indice 2 que seria "Pulga"
# print(mascotas[-1 ]) # aca se muestra desde el ultimo valor ya que no hay valores negativos contrarios
# print(mascotas[1:2:2]) # el primer numero marca desde el indice de inicio y el del medio son cuantos elementos queremos seleccionar y el numero final es el valor el cual se mostrorara

numero = list(range(1, 21)) # yaca podemos hacer lo mismo que abajo pero se pueden escribir de las dos maneras 
print(numero[::2]) # aca imprimimos los numeros paresaa
print(numero[1::2]) # aca se comienza desde el siguiente elementos mostrandonos los numeros impares