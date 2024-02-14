# creando mi excepcion personalizada 
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometi un error {err}")

# lanzando mi propia excepcion
# raise MiExcepcion("jajasjaj tonto")

# manejando la excepcion
try:
    raise MiExcepcion("que tonto quien divide por cero")
except:
    print("como vas a hacer eso")

