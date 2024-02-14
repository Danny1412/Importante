saludo = "Hola global" # Variable global, nunca pero bajo ninguno circunstancia usarlas asi sea el motivo que sea
# para no caer en un mala practica y que despues nuestro programa y codigo se dañe

# Aca establecemos dos funciones donde tenemos nuestras dos variables y les damos su alcance dentro de la misma funcion
# y simplemnete para manejar estas variables puedes darle su valor sea int o string.
# luego llamar la funcion y que el codigo dentro de la misma se ejecute 
def saludar():
    saludo = "Hola Mundo"
    print(saludo)

def saludachanchito():
    saludo = "Hola chanchito"
    print(saludo)

saludar()
print(saludo)