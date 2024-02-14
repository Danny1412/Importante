# El codigo while evalua la condicion se le establece para ejecutar el codigo que se le otorgue
# Mientras la condicion se siga cumpliendo while se sigue ejecutando hasta que cumpla su condicion

# numero = 1
#while numero < 100:
 #   print(numero)
 #   numero *= 2

# como podemos observar aca tenemos un ciclo el cual posee una salida 
comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

# Aca tenemos el loop infinito, pero con el if tiene la condicion de salida
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break