mascotas = ["Pelusa","Pulga","Felipe","Chanchito Feliz"]
# aca arriba tenemos nuestra lista y nuestros elementos 

# en el  ciclo for de aca abajo tenemos dos cosas el agregado de las varaibles "indice" y "mascota" mas la funcion de "enumerate"
# Esto nos enseña los valores de la lista que estamos iterando mas sus indices, ya que gracias a la funcion de enumerate podemos realizarlo
# Y esta funcion de enumerate se el conoce como Tupla
for indice, mascota in enumerate(mascotas): # Tupla
    print(indice, mascota) 