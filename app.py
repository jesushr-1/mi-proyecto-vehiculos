import pandas as pd
import plotly.express as px
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Título de la aplicación
st.title("Bienvenido a la aplicación para visualizar datos de vehículos en EU.")

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us_cleaned.csv')

# Mostrar el DataFrame completo
st.header("Data Viewer")
st.dataframe(car_data)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir histograma del odómetro')

if build_histogram:
    st.write("Generando histograma para la columna *odometer*...")

    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(
        title_text='Distribución del Odómetro',
        xaxis_title="Kilometraje (odometer)",
        yaxis_title="Frecuencia"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla para construir el gráfico de dispersión
build_scatter = st.checkbox(
    'Construir diagrama de dispersión: Precio vs Odómetro')

if build_scatter:
    st.write("Generando gráfico de dispersión entre *price* y *odometer*...")

    fig_scatter = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'
    )])

    fig_scatter.update_layout(
        title_text="Relación entre Precio y Kilometraje",
        xaxis_title="Kilometraje (odometer)",
        yaxis_title="Precio (price)"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
