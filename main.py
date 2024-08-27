from utils.simulator import MonteCarloSimulator as MCSimulator
from database.db_connection import DBConnection
from repositories.tb_cotacao import retornar_cotacao
from config.settings import DB_NAME, USER, PASSWORD, HOST, PORT

def run():
    db = DBConnection(
        DB_NAME, HOST, USER, PASSWORD, PORT
    )

    data_inicio = '2009-01-01'
    data_fim = '2011-01-01'
    cotacao_alvo = 2.3
    n_dias = 365
    n_simulacoes = 10000

    df = retornar_cotacao(db, data_inicio, data_fim)

    mc_simulator = MCSimulator(df)

    p, li, ls = mc_simulator.simular_com_intervalo(cotacao_alvo, n_dias, n_simulacoes)
    print(f"""
        A probabilidade do dólar atingir {cotacao_alvo} em {n_dias} dias é de: {p:.2%},
        com intervalo de confiança de 95%: [{li:.2%}, {ls:.2%}]
    """)

if __name__ == '__main__':
    run()