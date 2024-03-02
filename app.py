import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')

# Criando botões
hist_button = st.button('Criar histograma')
scatter_button = st.button('Criar gráfico de dispersão')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Se o botão de gráfico de dispersão for clicado
if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig_scatter = px.scatter(car_data, x="model_year", y="price", color="fuel")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Criando caixas de seleção
build_hist = st.checkbox('Criar histograma')
build_scatter = st.checkbox('Criar gráfico de dispersão')

# Se a caixa de seleção de histograma estiver marcada
if build_hist:
    st.write('Criando um histograma para a coluna odometer')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Se a caixa de seleção de gráfico de dispersão estiver marcada
if build_scatter:
    st.write('Criando um gráfico de dispersão para a coluna ano em relação ao preço')
    fig_scatter = px.scatter(car_data, x="model_year", y="price", color="fuel")
    st.plotly_chart(fig_scatter, use_container_width=True)


