dicc = {
    "nombre": "lucas",
    "apellido": "dalto",
    "sub": 100000
}

# recorriendo diccionario para obetener  claves
for key in dicc:
    key
    print(f"la clave es: {key}")

# recorriendo diccionario para obtener items con clave y valor
for datos in dicc.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")