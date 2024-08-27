from utils.simulator import MonteCarloSimulator as MCSimulator
from database.db_connection import DBConnection
from repositories.tb_cotacao import retornar_cotacao, retornar_datas_limite
from repositories.tb_consulta import registrar_consulta
from config.settings import DB_NAME, USER, PASSWORD, HOST, PORT
from figures.plot_scatter import plot

import streamlit as st
from plotly import graph_objects as go
def run(db: DBConnection):
    st.title("Simulador de Monte Carlo para cotação do Dólar(USD)")

    datas_limite = retornar_datas_limite(db)
    maior_data = datas_limite['max'][0]
    menor_data = datas_limite['min'][0]
    
    data_inicio = st.date_input(label="Selecione a data inicial do recorte",
                                min_value=menor_data,
                                max_value=maior_data)
    
    data_fim = st.date_input(label="Selecione a data final do recorte",
                                min_value=menor_data,
                                max_value=maior_data)
    
    consultar = st.button(label="Consultar dados")

    if consultar:
        co_consulta: int = registrar_consulta(db, data_inicio, data_fim)
        df = retornar_cotacao(db, data_inicio, data_fim)

        st.plotly_chart(plot(df))

    # data_inicio = '2009-01-01'
    # data_fim = '2011-01-01'
    # cotacao_alvo = 2.3
    # n_dias = 365
    # n_simulacoes = 10000

    # df = retornar_cotacao(db, data_inicio, data_fim)

    # mc_simulator = MCSimulator(df)

    # p, li, ls = mc_simulator.simular_com_intervalo(cotacao_alvo, n_dias, n_simulacoes)
    # print(f"""
    #     A probabilidade do dólar atingir {cotacao_alvo} em {n_dias} dias é de: {p:.2%},
    #     com intervalo de confiança de 95%: [{li:.2%}, {ls:.2%}]
    # """)

if __name__ == '__main__':
    db = DBConnection(
        DB_NAME, HOST, USER, PASSWORD, PORT
    )

    run(db)