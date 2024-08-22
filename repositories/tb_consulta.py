from database.db_connection import DBConnection

SCHEMA = "public"
TABLE = "tb_consulta"

def registrar_consulta(db: DBConnection, data_inicio: str, data_fim: str) -> int:
    """
    Armazena as datas de corte de uma consulta e retorna o id para utilização na tb_execucao
    """

    query = f"""
    INSERT INTO {SCHEMA}.{TABLE} (dt_inicio_consulta, dt_fim_consulta) VALUES ('%s', '%s') RETURNING co_consulta;
    """ % (data_inicio, data_fim)

    id_consulta = db.query(sql_query=query)
    
    return id_consulta