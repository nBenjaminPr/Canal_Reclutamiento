# Importamos la función del archivo main.py
from db import cargar_datos

# Cargar el DataFrame
df = cargar_datos()


LISTA = df.groupby("CanalReclutamiento")[["Salario", "HorasExtraUltimoTrimestre", "EncuestaSatisfaccion"]].mean()


print (LISTA)

