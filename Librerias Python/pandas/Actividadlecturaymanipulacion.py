import pandas as pd

#Descarga la base de datos "number-of-deaths-by risk-factor" (disponible en canvas).
#Lee la base de datos en Python, llamale a la base de datos tabla.
tabla = pd.read_excel('risk_factors.xlsx')
#Visualiza las primeras 5 filas de la base de datos. Visualiza las primeras 10 filas de la tabla.
print(tabla.head())
#Imprime la base de datos completa.
print(tabla)
#Imprime la columna 10.
print(tabla.iloc[10,:])
# Imprime la fila 20.
print(tabla.iloc[:,20])
#Imprime los elementos de la fila 0 y las columnas 7 y 8.
print(tabla.iloc[0,7:9])
#Imprime los elementos de la columna "Year" de dos formas diferentes.
print(tabla["Year"])
print(tabla.Year)
#Mediante los códigos de Python identifica cuantas filas y cuantas columnas tiene la base de datos.
print(tabla.shape)
#Identifica el nombre de cada una de las columnas
print(tabla.columns.values)
#De la columna "Year" menciona cuantas categorias tiene esta columna.
print(pd.unique(tabla.Year))
#Identifica el tipo de variable por columna
print(tabla.dtypes)
#Menciona y justifica si existen datos faltantes en la base de datos por dos métodos diferentes.
print(pd.isnull(tabla).sum())
print(pd.isna(tabla).sum())
#Crea una nueva base de datos que solo contenga la información de México, llama a esta base de datos MEX y guardala en un archivo excel.
tabla_mex = tabla[tabla.Code.eq("México")]
tabla_mex.to_excel("MEX.xlsx")