import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\pedos.csv")

# creando el grafico 
sns.lineplot(x="Fecha",y="Pedos",data=df)

# creando un punto en el momento con mas pedos
plt.plot("16-05",9,"o")

# mostrando el grafico 
plt.show()