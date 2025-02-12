# -*- coding: utf-8 -*-
"""Proyecto Analisis de datos-Python.ipynb

Generado en Google Colab.

Ver completo directamente en Google Colab! Haz clic en el enlace para explorar el proyecto: 

    https://drive.google.com/file/d/1KsAadmqgOZv7GVCcotPonl68PuzaLZM9/view?usp=sharing

# Analisis de Datos
# Modulo 1

### Juan Pablo Bayter Portacio
"""



"""## Diccionario de datos

|  Atributo  |        Descripción         |
|------------|----------------------------|
|ID_MT|Identificador vía Ministerio de Transporte|
|ENTIDAD | Entidad a cargo de la Vía|
|GiZScore | Calificación según análisis espacial|
|Fallecidos|Cantidad de fallecidos en el sector|
|GiPValue | Probabilidad de ocurrencia en el sector|
|Tramo | Identificación de la vía en una longitud determinada|
|Nombre |Nombre de vía concesionada|
|Latitud| Coordenada geográfica respecto al norte|
|Longitud |Coordenada geográfica respecto al este|
|PR |Punto de referencia en la vía|
|Municipio | Municipio ente territorial|
|Departamento|Departamento ente territorial|
|divipola| Código división política|

"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url= 'https://raw.githubusercontent.com/jmontiel02/Talento-TECH/refs/heads/main/'

data= pd.read_csv(url+'Mortalidad%20En%20Colombia.csv',header=0) #importamos la base de datos

data.head() #Muestra los 5 primeros datos del datafrane

data.tail(10) #Muestra los 10 ultimos datos del dataframe

data.shape #Muestra cuantas filas y columnas tiene el dataframe

data.info() #Muestra informacion sobre las variables y sus tipos de datos

data.describe()

data.isnull().any()

data.isnull().sum()

data.drop(columns=['GiZScore','divipola']) #Eliminar columnas que no se vean utiles
del data['GiZScore']
del data['divipola']

#Rellenar un dato en especifico
data.loc[data['Tramo'] == 'Granada - Villavicencio','Nombre'] = 'N/A'

# Rellenar valores nulos en columnas de texto con un valor fijo
data['Nombre'].fillna('N/A', inplace=True)
data['Tramo'].fillna('N/A', inplace=True)

data.head(20)

data.isnull().sum()

data.groupby(['Municipio','Fallecidos'])['Fallecidos'].count()

plt.figure(figsize=(10, 6))
plt.bar(data['ENTIDAD'],data['Fallecidos'], color='skyblue')

# Añadir título y etiquetas
plt.title('Cantidad de Fallecidos x Entidades', fontsize=16)
plt.xlabel('Entidades', fontsize=14)
plt.ylabel('Fallecidos', fontsize=14)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

data.groupby(['Municipio','GiPValue','Fallecidos'])['Fallecidos'].count()

data['Longitud'].max()

# [4.60971, -74.08175] son las coordenadas de Bogotá, Colombia,
import folium
mapa = folium.Map(location=[4.60971, -74.08175], zoom_start=6)  # Ubicación de Colombia
for index, row in data.iterrows():
    folium.Marker([row['Latitud'], row['Longitud']], popup=row['Fallecidos']).add_to(mapa)

#mapa.save('accidentes_viales_mapa.html')
mapa

data.to_csv('bd_nueva.csv', header = True, index = False) # Guardar dataset con el preproceso finalizado
# para su uso en los siguientes pasos.

#----------------------ESTO ES UNA PRUEBA-----------------------------------

data['Municipio'] = data['Municipio'].astype('category')

data['Municipio'].cat.categories

data['Municipio'].cat.codes

municipio = data['Municipio'].cat.codes.replace(-1, np.nan)

municipio= municipio.interpolate()

municipio = municipio.astype(int).astype('category')
municipio = municipio.cat.rename_categories(data['Municipio'].cat.categories)
data['Municipio']= municipio
data['Municipio']

data['Municipio'].isnull().sum()
