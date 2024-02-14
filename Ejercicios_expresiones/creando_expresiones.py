import re

#creando un numero CABA y ocultandolo
texto = "Hola Fox, mi numero es: +54 11 4321-4321 +54 11 4421-4523"

pattern = r'\+\d{2}\s{2}\s{4}-\s{4}'

reemplazo = re.sub(pattern,"(Numero oculto)", texto)

print(reemplazo)