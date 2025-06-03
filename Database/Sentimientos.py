import seaborn as sns
import matplotlib.pyplot as plt

# Importamos la función del archivo main.py
from db import cargar_datos

# Cargar el DataFrame
df = cargar_datos()


sentimientos = df.groupby(["CanalReclutamiento", "CategoriaSentimiento"]).size().unstack()

print(sentimientos)