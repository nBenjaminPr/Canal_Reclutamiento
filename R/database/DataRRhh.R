#Instalando packages
install.packages("readxl")
install.packages("dplyr")
install.packages("ggplot2")
install.packages("tidyverse")

library(readxl)
library(dplyr)
library(tidyselect)
library(ggplot2)
#"Cargando Base de datos"
Dataset_RRHH <- read_excel("C:/Users/ale_v/OneDrive/Desktop/Proyecto Final/Proyectti 2/Dataset_RRHH.xlsx")
View(Dataset_RRHH)

#Valores faltantes
colSums(is.na(Dataset_RRHH))

#Verificando Duplicados
Dataset_RRHH %>%
  duplicated() %>%
  sum()

#Ver primeras filas
head(Dataset_RRHH)

#Ver nombre de columnas
colnames(Dataset_RRHH)

# Cuenta cuántas veces aparece cada canal
Dataset_RRHH %>% count(CanalReclutamiento) 

#Columna rango de salario
Dataset_RRHH <- Dataset_RRHH %>%
  mutate(Rango_Salario = case_when(
    Salario < 50000 ~ "Bajo",
    Salario >= 50000 & Salario < 70000 ~ "Medio",
    Salario >= 70000 ~ "Alto"
  ))

#Gráfico de barras
Dataset_RRHH %>%
  ggplot(aes(x = Rango_Salario, fill = Rango_Salario)) +
  geom_bar() +
  labs(title = "Cantidad de empleados por rango salarial",
       x = "Rango Salarial",
       y = "Cantidad de Empleados") +
  theme_minimal()

# Elimina columnas que están completamente vacías (solo NA)
Dataset_RRHH <- Dataset_RRHH %>%
  select(where(~ !all(is.na(.))))

#Consultando columnas
colnames(Dataset_RRHH)

#Eliminando columnas con datos irrelevantes
Dataset_RRHH <- Dataset_RRHH %>%
  select(-c(...23,...24))

#Consultando columnas
colnames(Dataset_RRHH)

