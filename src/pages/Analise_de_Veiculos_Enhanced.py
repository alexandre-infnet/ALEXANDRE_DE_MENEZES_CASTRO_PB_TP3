import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Análise de Veículos Enhanced",
    page_icon="🚀",
)

st.title("Análise de Veículos Enhanced")


@st.cache_data
def load_car_data():
    cars_df = pd.read_csv("src/data/cars_data.csv")

    if "uploaded_df" in st.session_state:
        uploaded_df = st.session_state.uploaded_df

        enchanted_df = pd.merge(
            uploaded_df,
            cars_df,
            on=["Marca do Carro", "Ano do Carro", "Modelo do Carro"],
            how="inner",
        )
        return enchanted_df
    else:
        st.error("Por favor, faça o upload de um arquivo CSV.")
        return None


car_enchanter = st.file_uploader(
    "Selecione um CSV com os dados complementares", type="csv"
)
if not car_enchanter:
    st.warning("Use o arquivo user_data.csv")


if car_enchanter:
    st.session_state.uploaded_df = pd.read_csv(car_enchanter)

    enchanted_df = load_car_data()

    if enchanted_df is not None:
        st.write(enchanted_df)
