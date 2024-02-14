# Validar nombres de usuarios

def validar_usuarios():
    
    user = input("Ingrese su usuario: ")
    chars = [user]
    for chars in (chars):
        if chars < "":
            print(chars)
    # if user in user < 6:
    #     print(f"El {user} debe contener 6 o mas caracteres")
    return chars


resultado = validar_usuarios()
print(resultado)