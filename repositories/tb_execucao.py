from database.db_connection import DBConnection
from utils.simulator import MonteCarloSimulator

SCHEMA = "public"
TABLE = "tb_execucao"

def registrar_execucao(db: DBConnection, co_consulta: int, nu_execucoes: int, nu_dias:int, 
                       vl_cotacao_alvo: float, vl_probabilidade: float,
                       vl_intervalo_confianca_inferior: float,
                       vl_intervalo_confianca_superior: float) -> int:
    """
    Armazena a chave estrangeira da consulta, os parâmetros da simulação, e os valores dos intervalos de confiança
    """

    query = f"""
    INSERT INTO {SCHEMA}.{TABLE} (co_consulta, nu_execucoes, nu_dias,
    vl_cotacao_alvo, vl_probabilidade, vl_intervalo_confianca_inferior, 
    vl_intervalo_confianca_superior)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """ % (co_consulta, nu_execucoes, nu_dias, vl_cotacao_alvo, 
           vl_probabilidade, vl_intervalo_confianca_inferior, 
           vl_intervalo_confianca_superior)
    
    db.query(sql_query=query)