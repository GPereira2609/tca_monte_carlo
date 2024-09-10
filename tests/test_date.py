import pytest

from datetime import date
from utils.date import retornar_n_dias, verificar_ordem_das_datas

def test_retornar_n_dias_deve_retornar_2():
    dt_inicial = date(2023, 2, 1)
    dt_final = date(2023, 2, 3)

    assert retornar_n_dias(dt_inicial, dt_final) == 2

def test_retornar_n_dias_onde_datas_sao_iguais():
    dt_inicial = date(2023, 2, 1)
    dt_final = date(2023, 2, 1)

    assert retornar_n_dias(dt_inicial, dt_final) == 0

def test_retornar_n_dias_onde_dias_maior_que_365():
    dt_inicial = date(2023, 1, 1)
    dt_final = date(2024, 1, 10)

    assert retornar_n_dias(dt_inicial, dt_final) > 365

def test_verificar_ordem_das_datas_nao_deve_inverter():
    dt_inicial = date(2023, 2, 1)
    dt_final = date(2023, 2, 3)

    assert verificar_ordem_das_datas(dt_inicial, dt_final) == (dt_inicial, dt_final)

def test_verificar_ordem_das_datas_deve_inverter():
    dt_inicial = date(2023, 1, 3)
    dt_final = date(2023, 1, 1)

    assert verificar_ordem_das_datas(dt_inicial, dt_final) == (dt_final, dt_inicial)