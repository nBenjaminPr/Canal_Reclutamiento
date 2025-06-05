# Importamos la función del archivo main.py
from db import cargar_datos

# Cargar el DataFrame
df = cargar_datos()

# Consultas estadísticas de ejemplo
print("Resumen estadístico:")
print(df.describe())
