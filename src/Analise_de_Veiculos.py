import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Configuração da página
st.set_page_config(
    page_title="Análise de Veículos",
    page_icon="🚘",
)

st.title("Análise de Veículos")

df = pd.read_csv("src/data/cars_data.csv")

if "marca" not in st.session_state:
    st.session_state.marca = df["Marca do Carro"].unique()[0]

marca = st.sidebar.selectbox(
    "Selecione a marca do Veículo",
    df["Marca do Carro"].unique(),
    index=list(df["Marca do Carro"].unique()).index(st.session_state.marca),
)

if marca != st.session_state.marca:
    st.session_state.marca = marca

df_filtrado = df[df["Marca do Carro"] == marca]

st.subheader("Dados filtrados por marca")
st.write(df_filtrado)

with st.sidebar:
    st.subheader("Estatísticas básicas")
    st.write(df_filtrado.describe())

st.subheader("Nuvem de palavras - Modelos de veículos")
text = " ".join(df_filtrado["Modelo do Carro"])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
st.pyplot(plt)
