import csv

# manera de leer datos CSV
with open("archivos\\datos.csv")as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row) 
# este tipo de datos se pueden iterar por lo que son str