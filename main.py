from utils.simulator import MonteCarloSimulator as MCSimulator
from database.db_connection import DBConnection
from repositories.tb_cotacao import retornar_cotacao, retornar_datas_limite
from repositories.tb_consulta import registrar_consulta
from repositories.tb_execucao import registrar_execucao
from config.settings import DB_NAME, USER, PASSWORD, HOST, PORT
from figures.plot_scatter import plot

import streamlit as st

def run(db: DBConnection):
    # Inicializando a página
    st.title("Simulador de Monte Carlo para cotação do Dólar (USD)")

    # Inicializando variáveis de estado
    if 'df_cotacao' not in st.session_state:
        st.session_state.df_cotacao = None
    if 'visibility' not in st.session_state:
        st.session_state.visibility = True
    if 'co_consulta' not in st.session_state:
        st.session_state.co_consulta = None

    # Datas limite (por exemplo)
    datas_limite = retornar_datas_limite(db)
    maior_data = datas_limite['max'][0]
    menor_data = datas_limite['min'][0]

    # Entradas de data
    data_inicio = st.date_input(
        label="Selecione a data inicial do recorte",
        min_value=menor_data,
        max_value=maior_data
    )

    data_fim = st.date_input(
        label="Selecione a data final do recorte",
        min_value=menor_data,
        max_value=maior_data
    )

    # Botão para consulta de dados
    consultar = st.button(label="Consultar dados")

    if consultar:
        st.session_state.df_cotacao = retornar_cotacao(db, data_inicio, data_fim)
        st.session_state.visibility = False
        st.session_state.co_consulta = registrar_consulta(db, data_inicio, data_fim)[0][0]

    # Exibe o gráfico se houver dados armazenados
    if st.session_state.df_cotacao is not None:
        st.plotly_chart(plot(st.session_state.df_cotacao))

    # Input para cotação-alvo e número de dias
    cotacao_alvo = st.number_input(
        label="Insira a cotação-alvo desejada",
        min_value=.1,
        max_value=10.0,
        disabled=st.session_state.visibility
    )

    n_dias = st.number_input(
        label="Insira o número de dias para a simulação",
        min_value=365,
        max_value=10000,
        disabled=st.session_state.visibility
    )

    n_simulacoes = st.number_input(
        label="Insira a quantidade de simulações que devem ser realizadas",
        min_value=1000,
        max_value=100000,
        disabled=st.session_state.visibility
    )

    simular = st.button(label="Simular")

    if simular:
        mc_simulator = MCSimulator(st.session_state.df_cotacao)

        p, li, ls = mc_simulator.simular_com_intervalo(cotacao_alvo, n_dias, n_simulacoes)
        registrar_execucao(db, st.session_state.co_consulta, n_simulacoes,
                           n_dias, cotacao_alvo, p, li, ls)

        with st.container(border=True):
            st.metric(label="""Probabilidade de atingir 
                        cotação-alvo""", value=f"{p:.2%}")
        with st.container(border=True):
            st.metric(label="""Limite inferior do intervalo de confiança de 95%""", value=f"{li:.2%}")
        with st.container(border=True):
            st.metric(label="""Limite superior do intervalo de confiança de 95%""", value=f"{ls:.2%}")

if __name__ == '__main__':
    db = DBConnection(
        DB_NAME, HOST, USER, PASSWORD, PORT
    )

    run(db)