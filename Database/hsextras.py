# Importamos la función del archivo main.py
from db import cargar_datos

# Cargar el DataFrame
df = cargar_datos()

def clasificar_satisfaccion(x):
    if x >= 4:
        return "Alta"
    elif x == 3:
        return "Media"
    else:
        return "Baja"

df["NivelSatisfaccion"] = df["EncuestaSatisfaccion"].apply(clasificar_satisfaccion)


