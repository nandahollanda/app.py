import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Gráfico a partir de um arquivo CSV")

# Upload do arquivo CSV
arquivo = st.file_uploader("Faça o upload do seu arquivo CSV", type=["csv"])

if arquivo is not None:
    # Lê o CSV
    df = pd.read_csv(arquivo)

    # Mostra os dados
    st.subheader("Visualização dos dados:")
    st.write(df)

    # Lista de colunas do arquivo
    colunas = df.columns.tolist()

    # Selecionar colunas para o gráfico
    coluna_x = st.selectbox("Escolha a coluna para o eixo X", colunas)
    coluna_y = st.selectbox("Escolha a coluna para o eixo Y", colunas)

    # Criar o gráfico
    fig, ax = plt.subplots()
    ax.plot(df[coluna_x], df[coluna_y], marker='o')
    ax.set_xlabel(coluna_x)
    ax.set_ylabel(coluna_y)
    ax.set_title("Gráfico gerado a partir do CSV")

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)
else:
    st.info("Por favor, faça upload de um arquivo CSV para continuar.")
