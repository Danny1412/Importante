# un modulo son los archivos que creamos en python es decir los proyectos en los que trabajamos
# los cuales podemos usar para trabajar en nuevos proyectos es decir, usamos un proyecto de mostrar oraciones la usuario
# dentro de otro proeycto donde le pedimos que ingrese las oraciones

# maneras de importar modulos
# import modulo_saludar as m_saludar # el operador "as" es para renombrar el modulo que importamos y asi no tenemr problemas
# # a la hora de trabajar con dicho modulo no presente erroes con archivos que puedan tener mismos valores o nombres

# saludo = m_saludar.saludar("Lucas")

# print(saludo)

# aca importamos desde un modulo dos funciones 
from modulo_saludar import saludar as saludar_bien, saludar_calle as saludar_perro

# variables pasando las funciones con sus parametros
saludo = saludar_bien("Lucas")
saludo_raro = saludar_perro("Pedro")

# mostramos el valor de las varaibles en pantalla
print(saludo)
print(saludo_raro)

# como ver propiedades y metodos del name_space
# print(m_saludar,__name__)

# accedemos al nombre del modulo
print(__name__)

# accedemos al nombre del modulo llamado
# print(m_saludar,__name__)