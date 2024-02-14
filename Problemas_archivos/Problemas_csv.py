# cambiemos los datos de una columna

import pandas as pd
df = pd.read_csv("Problemas_archivos\\datos.csv")

# convertimos en string los datos de una columna
df ["edad"] = df["edad"].astype(str)

# # muestra el tipo de dato   
# print(type(df["edad"][0]))

# reemplazando el dato dalto por maestro
df ["apellido"].replace("dalto","maestro",inplace=True)

# eliminando filas con datos vacios, con axis = eliminamos la columna que desees desde la 0 en adelante
df = df.dropna()

# eliminando las filas repetidas
df = df.drop_duplicates()

# creando un CSV con el dataframe restante (limpio)
df.to_csv("Problemas_archivos\\datos_limpios.csv")