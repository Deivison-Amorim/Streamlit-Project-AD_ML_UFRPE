from asyncore import write
import pandas as pd
import streamlit as st
import altair as alt
import time as time

dataset = pd.read_csv('F:\Streamlit\Arquivos_Alunos\dataset_review_books_csv')

# dataset = pd.read_excel(
#    io='F:\Streamlit\Arquivos_Alunos\Datasets\dataset_review_books.xlsx',
#    engine='openpyxl',
#    sheet_name='Plan1',
#    usecols='A:B',
#    nrows=2001
# )

with st.sidebar:
    st.subheader("DASHBOARD - MENU")
    avaliacao = st.selectbox(
        "Selecione o tipo de avaliação:",
        options=dataset['sentimento'].unique()
    )
    with st.spinner("Carregando dados..."):
        time.sleep(2)
    st.success("Dados carregados!")

    # Tabela do Dataset
    tabela_Dataset = dataset.loc[(
        dataset['sentimento'] == avaliacao)
    ]

st.title("Data Set of Project")
st.write("Veja abaixo os dados do dataset com a avaliação:", avaliacao)
tabela_Dataset


# def convert_df(dataset):
#    return dataset.to_csv().encode('utf-8')

# st.download_button(
#    label="Baixar Dataset em CSV",
#    data=convert_df(dataset),
#    file_name="dataset_review_books_csv",
#    mime='text/csv'
# )
