import re

#cadena en la que se busca los patrones
text = "La fecha es 23/06/2021 y el telefono es +1-555-555-5555"

# el patron a buscar
pattern = r"\d{2}/\d{2}/\d{4}"

# el texto con el que se reemplarazara el patron
replacement = "Fecha oculta"

# reemplazar todas las aparaciones del patron en la cadena de texto
new_text = re.sub(pattern, replacement, text)

# imprimimos en pantalla
print("Texto modificado", new_text)