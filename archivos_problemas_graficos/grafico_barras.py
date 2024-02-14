import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\cofla_ingresos.csv")

# creando el grafico 
sns.barplot(x="fuentes",y="ingreso",data=df)

# obteniendo el total de ingresos
total_ingresos = df["ingreso"].sum()

# mostrando el total de ingresos
print(F"El total de ingresos es de: ${total_ingresos}")

# mostrando el grafico 
plt.show()