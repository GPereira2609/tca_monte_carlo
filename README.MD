# Criando Simulações de Monte Carlo: Estratégias de Desenvolvimento e Estudos de Caso


## Resumo

O mercado financeiro é marcado por sua volatilidade, e prever variações nas taxas de câmbio é um desafio devido à influência de fatores econômicos, políticos e sociais. Para ajudar investidores e analistas, este projeto propõe desenvolver uma aplicação que utiliza simulações de Monte Carlo para modelar cenários futuros da cotação real-dólar. A ferramenta permitirá a inserção de uma cotação-alvo, período de tempo e número de simulações, fornecendo uma análise probabilística sobre a possibilidade de atingir a cotação desejada. O objetivo é oferecer suporte à gestão de risco e ao planejamento estratégico.


## Objetivo do Projeto

O objetivo deste projeto é desenvolver uma aplicação capaz de realizar simulações de Monte Carlo sobre a cotação histórica do real-dólar, com o intuito de estimar a probabilidade de que uma cotação específica seja atingida em um intervalo de tempo definido. A aplicação permitirá que os usuários insiram uma cotação-alvo, um período de tempo, e o número de simulações a serem realizadas, fornecendo uma análise probabilística detalhada sobre a viabilidade da cotação-alvo.


## Requisitos funcionais 

# Leitura e Processamento de Dados Históricos
A aplicação deve ser capaz de importar e processar dados históricos da cotação real-dólar de uma fonte confiável, como bancos centrais ou serviços de dados financeiros. Esses dados devem ser limpos e estruturados para uso em simulações.

# Entrada de Parâmetros
A interface da aplicação deve permitir que o usuário insira os parâmetros de cotação-alvo, período de tempo e número de simulações

# Simulação de Monte Carlo
A aplicação deve realizar simulações de Monte Carlo utilizando os dados históricos processados, modelando variações futuras na cotação real-dólar com base nos parâmetros inseridos pelo usuário.

# Cálculo de Probabilidades
Após a execução das simulações, a aplicação deve calcular a probabilidade de a cotação-alvo ser atingida no período de tempo especificado. Os resultados devem ser apresentados de forma clara e detalhada, permitindo fácil interpretação pelo usuário.

# Registro de resultados em banco
A aplicação deve ser capaz de gerar um registro em banco de cada execução, armazenando os principais resultados como probabilidade de alcançar a cotação-alvo, erro-média, intervalo de confiança.


## Requisitos não-funcionais 

# Performance
A aplicação deve ser otimizada para processar grandes volumes de dados e executar simulações em tempo hábil, proporcionando uma experiência fluida para o usuário.
# Usabilidade
A interface do usuário deve ser intuitiva e acessível, com instruções claras e feedback em tempo real, garantindo que usuários com diferentes níveis de expertise técnica possam utilizar a aplicação eficientemente.
# Confiabilidade
A aplicação deve garantir a precisão e consistência dos resultados através de validações de dados e métodos estatísticos robustos.


## Diagramas de banco de dados

![Diagrama das tabelas de banco de dados](diagrams/diagrama%20de%20banco.png)


## Diagramas de classe

![Diagrama da classe DBConnection](diagrams/diagrama%20conexao.png)

![Diagrama da classe MonteCarloSimulator](diagrams/diagrama%20simulador.png)


## Diagramas de sequência

![Diagrama do fluxo da aplicação](diagrams/diagrama%20de%20sequencia.png)