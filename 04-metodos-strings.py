animal = "  chanCHito feliz  "
print(animal.upper()) # Sirve para poner todos en mayusculas
print(animal.lower()) # Sirve para poner todos en minusculas
print(animal.strip().capitalize()) # Pone la primera letra en mayusculas
print(animal.title()) # Pone las dos letras del string en mayusculas
print(animal.strip()) # Quita los espacios al los lados del string
print(animal.lstrip()) # Quita los espacios a la izquierda
print(animal.rstrip()) # Quita los espacios a la derecha 
print(animal.find("cH")) # Busca el indice de los strings si estan sino estan devuelve -1
print(animal.replace("nCH", "j")) # remplaza los valores puestos por el segundo valor en el string
print("nCH" in animal) # Nos da valor de verdadero o falso si los strings estan en la variable
print("nCH" not in animal) # Nos da valor de verdadero o falso si los strings no estan en la variable