# si el modulo estuviera dentro de una carpeta en la misma ruta se impora asi:
#import Enrutamiento.saludar as m_saludar

# para importar modulos fuera de la ruta de acceso es decir no esten integrados en una carpeta
# se realiza el siguiente llamado

import sys

sys.path.append("c:\\Users\\Ñañel\\Desktop\\PY\\Enrutamiento")
print(sys.path)

import saludar as modulo_saludo

print(modulo_saludo.saludar("Dalto"))