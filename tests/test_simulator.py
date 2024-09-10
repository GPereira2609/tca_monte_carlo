import pytest
import pandas as pd

from datetime import date
from utils.simulator import MonteCarloSimulator

def test_simular_deve_retornar_valor_entre_0_e_1():
    dados = pd.DataFrame({
        'dt_cotacao': [
            date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3),
        ],
        'vl_cotacao': [
            4.5, 4.6, 4.7, 
        ]
    })

    simulador = MonteCarloSimulator(dados)

    cotacao_alvo = 5
    periodo = 3
    num_simulacoes = 5000

    assert 0 <= simulador.simular(
        cotacao_alvo,
        periodo,
        num_simulacoes,
    ) <= 1

def test_simular_com_intervalo_deve_ter_probabilidade_entre_limites():
    dados = pd.DataFrame({
        'dt_cotacao': [
            date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3),
        ],
        'vl_cotacao': [
            4.5, 4.6, 4.7, 
        ]
    })

    simulador = MonteCarloSimulator(dados)

    cotacao_alvo = 5
    periodo = 3
    num_simulacoes = 5000

    p, li, ls = simulador.simular_com_intervalo(
        cotacao_alvo,
        periodo,
        num_simulacoes,
    )

    assert li <= p <= ls


