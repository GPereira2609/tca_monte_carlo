from database.db_connection import DBConnection
import pandas as pd 

SCHEMA = "public"
TABLE = "tb_cotacao"

def retornar_cotacao(db: DBConnection, data_inicio: str, data_fim: str) -> pd.DataFrame:
    """
    Retorna um conjunto de dados de cotação que esteja entre os valores de corte estabelecidos
    """

    query = f"""
    SELECT vl_cotacao, dt_cotacao FROM {SCHEMA}.{TABLE}
    WHERE dt_cotacao BETWEEN '%s' AND '%s' ORDER BY 2;
    """ % (data_inicio, data_fim)

    with db.connection() as conn:
        df = pd.read_sql(sql=query, con=conn)

    return df

def retornar_datas_limite(db: DBConnection) -> (str, str):
    """
    Retorna maior e menor datas de cotação
    """

    query = f"""
    SELECT MAX(dt_cotacao), MIN(dt_cotacao) from tb_cotacao
    """

    with db.connection() as conn:
        df = pd.read_sql(sql=query, con=conn)

    return df