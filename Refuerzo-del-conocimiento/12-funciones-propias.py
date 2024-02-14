# # creando funciones simples
# def saludar():
#     print("hola lucas mi maestro")

# saludar()

# # funcion con  parametros y argumentos
# def saludar(nombre, sexo):
#     sexo = sexo.lower()
#     if (sexo == "mujer"):
#         adjetivo = "reina"
#     elif (sexo == "hombre"):
#         adjetivo = "maquina"
#     else:
#         adjetivo = "parce"
#     print (F"Hola {nombre}, mi {adjetivo}, como te va")

# saludar("Lucas", "mujer")

# funcion para retornar multiples valores
def calculo_clave(num):
    chars = "abcdefghij" # primero creamos un string el cual se debe recorrer
    num_entero = str(num) # creamos una varaible temportal la cual le vamos a pasar el valor de string a nuestro parametro "(num)"
    num = int(num_entero[0]) # luego transformaremos "(num)" en entero y el mismo num recorrera la variables de "num_entero" recorriendo el valor del indice cero "[0]"
# creamos los caracteres del Hash el cual lo haremos operaciones aritmeticas para darle un sentido de "aleaoriedad"    
    c1 = num - 2 # aca pasamos variable "c1" la resta de la varaible "num - 2" y eso restara los string para darnos el caracter que se encuentre en el indice cero 
    c2 = num  # aca no le pasamos nada nos dara el primer valor del indice
    c3 = num - 5 # aca lo restara por cinco
    # luego creamos una varaible "contraseña" la cual le pasaremos un formato de string donde imprimiremos nuestra "clave"
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}" 
    # haremos que la variable "chars" recorra los "c1, c2, c3" e imprima el valor que estos tengas despues de procesar el codigo anterior a el
    # y por ulimo multiplicaremos nuestro parametro "num*2"
    return contraseña, num # imprimimos en pantalla

calculo_clave(9) # llamamos a la funcion
# en el codigo anterior intentamos realizar un "Hash", en una funcion lo cual es bastante practico

# desempaquetado de la funcion
password,primer_num = calculo_clave(978)
# mostrando la funcion
print(f"tu clave nueva es: {password}")
print(f"el numero fue: {primer_num}")