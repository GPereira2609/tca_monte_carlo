from plotly import graph_objects as go

def plot(df):
    fig = go.Figure(data=[go.Scatter(x=df['dt_cotacao'], y=df['vl_cotacao'])])

    fig.update_layout(
        title='Cotação do Dólar(USD) em comparação com o Real(BRL) ao longo do tempo',
        xaxis_title='Data',
        yaxis_title='Cotação',
    )
    
    return fig
