# Funcion del numero 0 hasta el numero que le pasemos(argumento)
# deben numeros primos hasta llegar al numero que necesitamos

def es_primo(num):# establecemos la funcion y le pasamos un parametro
    for i in range(2,num-1):# establecemos un parametro en for para que ese numero no sea divisible entre 2 y ese mismo numero
        if num%i==0: return False # retornamos falso en caso que se pueda dividir
    return True # luego retormanos true si encontro numeros primos hasta el valor que le pasamos, es decir "es_primo"

# establecemos una funcion para mostrar todos los numeros primos que hay hasta el argumento que le pasemos
def primos_hasta(num):
    primos = [] # creamos nuestra lista
    for i in range(3,num+1): # aca arrancamos desde 3, ya que como sabemos 1 y 2 son primos entonces para demostrar la valides del programa
# le sumamos uno para enseñar el total de numeros
        resultado= es_primo(i)
        if resultado == True: primos.append(i) # si el valor de arriba es primo se agrega a la lisata
# devolvemos el valor de la lista
    return primos

# creamos "resultado" le pasamos la funcion que queremos mostrar
resultado = primos_hasta(100)
print(resultado) # luego imprimimos nuestra variable y enseñamos los valores
