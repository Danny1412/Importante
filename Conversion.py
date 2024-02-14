# Fahrenheit a grados centígrados: restar 32 y luego multiplicar por 5/9 o 0,555.
# grados centígrados a Fahrenheit: multiplicar por 9/5 o por 1,8 y luego sumar 32.
temp = input("Ingrese la temperetura a convertir: ")
temp = int(temp)

temp2 = input("Es Fahrenheit(F) o Celsius(C)?: ")

if temp2.upper() in "(F)":
    resultado = (temp - 32) * 5/9 
    mensaje = f"La temperatura en grados Celsius es {resultado}"
    print(mensaje)
elif temp2.upper() in "(C)":
    resultado = (temp * 9/5) + 32 
    mensaje = f"La temperatura en grados Fahrentheit es {resultado}"
    print(mensaje)
else:
    print("Nomenclatura no valida!")