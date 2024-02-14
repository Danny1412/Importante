# # creando funciones de tres parametros
# def frase(nombre,apellido,adjetivo):
#     return f"Hola {nombre} {apellido} sos muy {adjetivo}"

# #utilizadno keyargs 
# frase_result = frase (nombre = "lucas",apellido = "dalto",adjetivo = "es un capo")

# creando la misma funcoin, con parametros opcional y valor por defecto
def frase (nombre,apellido,adjetivo="tonto"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_result = frase ("Lucas","Dalto",adjetivo="inteligente")
print(frase_result)

