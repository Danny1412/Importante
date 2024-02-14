import re

text = "Este es un ejemplo de una pagona web: https://proyectonano.com y tambien podemos visitarla"

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, text)

print(result)