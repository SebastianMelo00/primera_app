import pandas as pd 
import matplotlib.pyplot as plt 
import geopandas as gpd 
import streamlit as st

df = pd.read_csv('f2021.csv')
#gdf = gpd.read_parquet('deptos.parquet')

st.title("Proporción mujeres")

mapa = (gpd
        .read_parquet('info_deptos.parquet')
        .astype({'DPTO':int}))

mes = st.slider('Seleccionar mes', 1, 12)

fil = df[(df['MES'] == mes) & (df['edad'] >= 15)]
t = fil.replace({'F':1,
            'M':0}).groupby(['DPTO'])['sexo'].mean().reset_index()

gdf = gpd.GeoDataFrame(t.merge(mapa, on='DPTO', how='right'))




fig, ax = plt.subplots(1, 1, figsize=(10, 4))

gdf.plot(column='sexo', ax=ax, legend=True, missing_kwds={'color':'gray'})
plt.axis('off')

st.pyplot(fig)
