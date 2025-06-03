import seaborn as sns
import matplotlib.pyplot as plt
# Importamos la función del archivo main.py
from db import cargar_datos

# Cargar el DataFrame
df = cargar_datos()



canales = df.groupby("CanalReclutamiento")[["Salario", "EncuestaSatisfaccion"]].mean().reset_index()

fig, ax = plt.subplots(1, 2, figsize=(14, 5))
sns.barplot(data=canales, x="Salario", y="CanalReclutamiento", ax=ax[0])
sns.barplot(data=canales, x="EncuestaSatisfaccion", y="CanalReclutamiento", ax=ax[1])
plt.tight_layout()
plt.show()
