import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Visualizaciones Interactivas de Datos de autos en US')

hist_button = st.button('Construir histograma')  # crear un botón
build_scatter = st.checkbox('Construir un diagrama de dispersión')  # crear una casilla de verificación

if hist_button:  # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de autos en US')
    fig = px.histogram(car_data, x="odometer(miles)")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:  # si la casilla de verificación está seleccionada
    st.write('Creación de un diagrama de dispersión del odómetro vs precio')
    fig = px.scatter(car_data, x="odometer(miles)", y="price(USD)")
    st.plotly_chart(fig, use_container_width=True)