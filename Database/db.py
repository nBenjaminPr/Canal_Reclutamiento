import pandas as pd

def cargar_datos():
    ruta = 'C:/Users/Usuario/Desktop/Proyecto/RRHHproyect.xlsx'
    df = pd.read_excel(ruta)
    return df


