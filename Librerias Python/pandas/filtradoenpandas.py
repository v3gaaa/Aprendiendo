import pandas as pd

dates=['April-10', 'April-11', 'April-12', 'April-13','April-14','April-16']
sales=[200,300,400,200,300,300]
prices=[3, 1, 2, 4,3,2]

df = pd.DataFrame({'Date':dates ,
                   'Sales':sales ,
                   'Price': prices})


#Uso de metodo booleano
df_mask=df['Sales']==300
filtered_df = df[df_mask]
print(filtered_df)

#Usa numpy para verificar posiciones dentro de la columna
import numpy as np
df_mask=df['Sales']==300
positions = np.flatnonzero(df_mask)
filtered_df=df.iloc[positions]
print(filtered_df)

#Metodo de cadenas
filtered_df = df[df.Sales.eq(300)]
print(filtered_df)

#Metodo query
filtered_df = df.query('Sales == 300')
print(filtered_df)

#Seleccion de varios valores dentro de la columna
values=[200,400]
filtered_df = df[df.Sales.isin(values)]
print(filtered_df)
