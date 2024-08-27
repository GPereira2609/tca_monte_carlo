import pandas as pd
import numpy as np
from scipy.stats import norm

class MonteCarloSimulator:
    def __init__(self, df):
        """
        Inicializa a classe com o DataFrame de dados.

        Args:
            df (pd.DataFrame): DataFrame com os dados históricos.
        """
        self.df = df

    def simular(self, cotacao_alvo, periodo, num_simulacoes):
        """
        Simula o preço do dólar utilizando Monte Carlo.

        Args:
            cotacao_alvo (float): Cotação-alvo a ser atingida.
            periodo (int): Período de tempo em dias.
            num_simulacoes (int): Número de simulações.

        Returns:
            float: Probabilidade de atingir a cotação-alvo no período.
        """

        # Calculando o retorno logístico diário
        self.df['retorno'] = np.log(self.df['vl_cotacao'] / self.df['vl_cotacao'].shift(1))
        retorno_medio = self.df['retorno'].mean()
        desvio_padrao = self.df['retorno'].std()

        # Gerando os preços futuros para cada simulação
        precos_futuros = np.zeros((num_simulacoes, periodo))
        precos_futuros[:, 0] = self.df['vl_cotacao'].iloc[-1]  # Último preço histórico como ponto de partida
        for t in range(1, periodo):
            precos_futuros[:, t] = precos_futuros[:, t - 1] * np.exp(
                retorno_medio + desvio_padrao * np.random.randn(num_simulacoes)
            )

        # Verificando se a cotação-alvo foi atingida em cada simulação
        atingiu_alvo = np.any(precos_futuros >= cotacao_alvo, axis=1)

        # Calculando a probabilidade
        probabilidade = atingiu_alvo.mean()

        return probabilidade

    def simular_com_intervalo(self, cotacao_alvo, periodo, num_simulacoes, alpha=0.05):
        """
        Simula o preço do dólar utilizando Monte Carlo e calcula o intervalo de confiança.

        Args:
            cotacao_alvo (float): Cotação-alvo a ser atingida.
            periodo (int): Período de tempo em dias.
            num_simulacoes (int): Número de simulações.
            alpha (float): Nível de significância (1 - nível de confiança).

        Returns:
            tuple: Probabilidade, limite inferior do intervalo, limite superior do intervalo.
        """

        probabilidade = self.simular(cotacao_alvo, periodo, num_simulacoes)

        # Calculando o intervalo de confiança
        z = norm.ppf(1 - alpha/2)  # Valor crítico da distribuição normal
        erro_padrao = np.sqrt(probabilidade * (1 - probabilidade) / num_simulacoes)
        limite_inferior = probabilidade - z * erro_padrao
        limite_superior = probabilidade + z * erro_padrao

        return probabilidade, limite_inferior, limite_superior