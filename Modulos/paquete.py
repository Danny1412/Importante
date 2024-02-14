# un paquete se convierte en paquete cuando tiene un archivo llamado __init__.py
# los paquetes son capaces de poseer de 1 a muchos modulos los cuales podemos acceder a ellos si estan en el paquete
import Paquete.saludar

# aca accedemos al paquete y dentro de ese paquete tenemos el modulo saludar dentro de ese modulo tenemos la funcion saludar
# la cual se ejecuto en nuestro modulo paquete
print(Paquete.saludar.saludar("Dalto"))