import pandas as pd

# usando la funcion read-csv para leer el archivo csv creado
df = pd.read_csv("Archivos\\datos.csv") # con esto podemos agregar el encavezado de cada columna names=["name","lasname","age"]
df2 = pd.read_csv("Archivos\\datos.csv")

# sacando los datos de la columna nombre
nombres = df["nombre"]

# ordenado las edades de la data frame
df_ordenado_ascendente = df.sort_values("edad")

# ordedando de forma descendente
df_ordenado_descendente = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

# accediendo a las primeras 3 filas con head
primeras_fila = df.head(3)

# accediendo a las ultimas 3 filas con head
ulimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape

# obteniendo data estadistica del dataframe
df_info = df.describe()

# accediendo a un elemento especifico del dataframe con loc, la edad de la segunda fila
elemento_espc = df.loc[2,"edad"]

# accediendo a un elemento especifico del dataframe con iloc, la edad de la segunda fila
elemento_espc = df.iloc[2,2]

# accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#accediendo a los datos de la fila 3
fila3 = df.loc[2,:]

#accediendo a los datos de la fila 3
fila3 = df.iloc[2,:]

# accediendoa  filas con edad mayor que 30

mayor_edades = df.loc [df["edad"]<30,:]

print(mayor_edades)