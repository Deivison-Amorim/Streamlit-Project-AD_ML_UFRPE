from asyncore import write
import pandas as pd
import streamlit as st
import altair as alt
import time as time

dataset = pd.read_csv(
    'Streamlit_AD_ML_UFRPE/Arquivos_Alunos/dataset_review_books_csv')

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
