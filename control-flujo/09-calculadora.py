# Para recordar, Simepre que usemos un loop infiino se declara la variable total por fuera y antes del loop

print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""

while True:
# Como podemos observar con la variable generada, se establece le fin de loop
# Para asi poder acumplir todas las operaciones
    if not resultado:
        resultado = input("ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
# Aca se establecen las operaciones y el numero por el cual el "resultado" se va a procesar ya sea sum rest multi y div
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    
# aca se cumplen todas las operaciones con un if y elif para que cuando el usuario agregue la operacion se cumpla
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("operacion no valida")
        break
    print(f"El resultado es {resultado}")