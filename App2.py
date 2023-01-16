from asyncore import write
import pandas as pd
import streamlit as st
import altair as alt
import time as time

dataset = pd.read_csv('dataset_review_books_csv.csv')

dadosRedesNeurais = pd.DataFrame({
    'epoch': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'loss_lstm': [0.5867, 0.4016, 0.1182, 0.0558, 0.0224, 0.0205, 0.0101, 0.0065, 0.0041, 0.0031],
    'accuracy_lstm': [0.7031, 0.8881, 0.9600, 0.9844, 0.9937, 0.9950, 0.9975, 0.9981, 0.9987, 0.9994],
    'val_loss_lstm': [0.4456, 0.3521, 0.4153, 0.4294, 0.5003, 0.4516, 0.5345, 0.6436, 0.6742, 0.7549],
    'val_accuracy_lstm': [0.8375, 0.8600, 0.8350, 0.8475, 0.8550, 0.8550, 0.8475, 0.8400, 0.8350, 0.8325],
    'loss_rnn': [0.7206, 0.6753, 0.6249, 0.5299, 0.3974, 0.2219, 0.1258, 0.0822, 0.0605, 0.0427],
    'accuracy_rnn': [0.4925, 0.6169, 0.6862, 0.8006, 0.8494, 0.9287, 0.9681, 0.9812, 0.9850, 0.9906],
    'val_loss_rnn': [0.6884, 0.6770, 0.6369, 0.6485, 0.6489, 0.5158, 0.5702, 0.5922, 0.6337, 0.6190],
    'val_accuracy_rnn': [0.5750, 0.5975, 0.6650, 0.6175, 0.6875, 0.7950, 0.8025, 0.7925, 0.8000, 0.8125]
})

with st.sidebar:
    st.subheader("DASHBOARD - MENU")

    avaliacao = st.selectbox(
        "Selecione o tipo de avaliação:",
        options=['Positivo', 'Negativo'])
    if avaliacao == 'Negativo':
        st.write('Você selecionou a opção: ', avaliacao)
        avaliacao = 'neg'
    else:
        st.write('Você selecionou a opção: ', avaliacao)
        avaliacao = 'pos'

#    avaliacao = st.selectbox(
#        "Selecione o tipo de avaliação:",
#        options=dataset['sentimento'].unique()
#    )
#    if avaliacao == 'neg':
#        st.write('Você selecionou a exibição dos dados NEGATIVOS!')
#    else:
#        st.write('Você selecionou a exibição dos dados POSITIVOS!')

    # Resultados das Redes Neurais

    opcao = st.selectbox(
        'Tipo da Rede Neural',
        options=['LSTM', 'RNN'])
    st.write('Você selecionou o tipo da Rede Neural: ', opcao)

    with st.spinner("Carregando dados..."):
        time.sleep(1)
    st.success("Carregado!")


tabela_Dataset = dataset.loc[(
    dataset['sentimento'] == avaliacao)
]

st.title("Gráficos dos Resultados da Análise")
st.subheader('Escolha o tipo de rede para ser exibido no gráfico')

# Gráficos da Rede LSTM

graf1_LSTM_loss = alt.Chart(dadosRedesNeurais).mark_line(
    point=alt.OverlayMarkDef(color="blue", size=75,
                             fill='white', filled=False),
    color='blue'
).encode(
    x=alt.X('epoch'),
    y=alt.Y('loss_lstm'),
    tooltip=['epoch', 'loss_lstm', 'accuracy_lstm']
).properties(
    width=800, height=400,
    title='Resultados para Rede Neural ' +
    opcao + ' ( loss x accuracy )'
)

rotulo_graf1 = graf1_LSTM_loss.mark_text(
    dy=-15,
    size=10
).encode(
    text='loss_lstm'
)

graf2_LSTM_accuracy = alt.Chart(dadosRedesNeurais).mark_line(
    point=alt.OverlayMarkDef(color="red", size=75,
                             fill='white', filled=False),
    color='red'
).encode(
    x=alt.X('epoch'),
    y=alt.Y('accuracy_lstm'),
    tooltip=['epoch', 'loss_lstm', 'accuracy_lstm']
)

rotulo_graf2 = graf2_LSTM_accuracy.mark_text(
    dy=-15,
    size=10
).encode(
    text='accuracy_lstm'
)

graf3_LSTM_val_loss = alt.Chart(dadosRedesNeurais).mark_line(
    point=alt.OverlayMarkDef(color="blue", size=75,
                             fill='white', filled=False),
    color='blue'
).encode(
    x=alt.X('epoch'),
    y=alt.Y('val_loss_lstm'),
    tooltip=['epoch', 'val_loss_lstm', 'val_accuracy_lstm']
).properties(
    width=800, height=400,
    title='Resultados para Rede Neural ' +
    opcao + ' ( val_loss x val_accuracy )'
)

rotulo_graf3 = graf3_LSTM_val_loss.mark_text(
    dy=20,
    size=10
).encode(
    text='val_loss_lstm'
)

graf4_LSTM_val_accuracy = alt.Chart(dadosRedesNeurais).mark_line(
    point=alt.OverlayMarkDef(color="red", size=75,
                             fill='white', filled=False),
    color='red'
).encode(
    x=alt.X('epoch'),
    y=alt.Y('val_accuracy_lstm'),
    tooltip=['epoch', 'val_loss_lstm', 'val_accuracy_lstm']
)

rotulo_graf4 = graf4_LSTM_val_accuracy.mark_text(
    dy=10,
    size=10
).encode(
    text='val_accuracy_lstm',
)

# Gráficos da Rede RNN

graf5_RNN_loss = alt.Chart(dadosRedesNeurais).mark_line(
    point=alt.OverlayMarkDef(color="black", size=75,
                             fill='white', filled=False),
    color='black'
).encode(
    x=alt.X('epoch'),
    y=alt.Y('loss_rnn'),
    tooltip=['epoch', 'loss_rnn', 'accuracy_rnn']
).properties(
    width=800, height=400,
    title='Resultados para Rede Neural ' +
    opcao + ' ( loss x accuracy )'
)

rotulo_graf5 = graf5_RNN_loss.mark_text(
    dy=-15,
    size=10
).encode(
    text='loss_rnn'
)

graf6_RNN_accuracy = alt.Chart(dadosRedesNeurais).mark_line(
    point=alt.OverlayMarkDef(color="green", size=75,
                             fill='white', filled=False),
    color='green'
).encode(
    x=alt.X('epoch'),
    y=alt.Y('accuracy_rnn'),
    tooltip=['epoch', 'loss_rnn', 'accuracy_rnn']
)

rotulo_graf6 = graf6_RNN_accuracy.mark_text(
    dy=-15,
    size=10
).encode(
    text='accuracy_rnn'
)

graf7_RNN_val_loss = alt.Chart(dadosRedesNeurais).mark_line(
    point=alt.OverlayMarkDef(color="black", size=75,
                             fill='white', filled=False),
    color='black'
).encode(
    x=alt.X('epoch'),
    y=alt.Y('val_loss_rnn'),
    tooltip=['epoch', 'val_loss_rnn', 'val_accuracy_rnn']
).properties(
    width=800, height=400,
    title='Resultados para Rede Neural ' +
    opcao + ' ( val_loss x val_accuracy )'
)

rotulo_graf7 = graf7_RNN_val_loss.mark_text(
    dy=20,
    size=10
).encode(
    text='val_loss_rnn'
)

graf8_RNN_val_accuracy = alt.Chart(dadosRedesNeurais).mark_line(
    point=alt.OverlayMarkDef(color="green", size=75,
                             fill='white', filled=False),
    color='green'
).encode(
    x=alt.X('epoch'),
    y=alt.Y('val_accuracy_rnn'),
    tooltip=['epoch', 'val_loss_rnn', 'val_accuracy_rnn']
)

rotulo_graf8 = graf8_RNN_val_accuracy.mark_text(
    dy=10,
    size=10
).encode(
    text='val_accuracy_rnn',
)

# Impressão dos Gráficos

if opcao == 'LSTM':
    st.altair_chart(graf1_LSTM_loss +
                    rotulo_graf1 +
                    graf2_LSTM_accuracy +
                    rotulo_graf2)

    st.altair_chart(graf3_LSTM_val_loss +
                    rotulo_graf3 +
                    graf4_LSTM_val_accuracy +
                    rotulo_graf4)
else:
    st.altair_chart(graf5_RNN_loss +
                    rotulo_graf5 +
                    graf6_RNN_accuracy +
                    rotulo_graf6)

    st.altair_chart(graf7_RNN_val_loss +
                    rotulo_graf7 +
                    graf8_RNN_val_accuracy +
                    rotulo_graf8)

tabela_Dataset = dataset.loc[(
    dataset['sentimento'] == avaliacao)]

# Tabela do Dataset
st.title("Dataset do Projeto")
st.write("Veja abaixo os dados do dataset com a avaliação:", avaliacao)
tabela_Dataset
