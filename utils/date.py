from datetime import datetime as dt

def retornar_n_dias(dt_inicio: dt.date, dt_fim: dt.date):
    return (dt_fim-dt_inicio).days

def verificar_ordem_das_datas(dt_inicio: dt.date, dt_fim: dt.date):
    return min(dt_inicio, dt_fim), max(dt_inicio, dt_fim)