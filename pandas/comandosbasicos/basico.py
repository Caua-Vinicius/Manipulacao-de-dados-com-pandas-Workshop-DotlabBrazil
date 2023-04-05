import pandas as pd
# criando um DataFrame a partir de um dicionário
data = {'nome': ['Alice', 'Bob', 'Charlie', 'Dave', 'Emily', 'Sebastiao', 'Elisson', 'Kayo', 'Maicon', 'Patricia'],
        'idade': [25, 30, 35, 40, 45, 30, 28, 35, 30, 28],
        'cidade': ['Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Salvador', 'Recife', 'Lajedo', 'Bonito', 'Tuparetama', 'Gravatá', 'Garanhuns']}
df = pd.DataFrame(data)




###    Vale salientar que cada um dos comandos realizados foram feitos individuais ###




# exibe as primeiras linhas do DataFrame
df.head()

# exibe as oito primeiras linhas do DataFrame
df.head(8)

#imprime as 5 últimas linhas
df.tail()

df.describe()

df.columns

df.count()

df.info

# mostra a quantidade de linhas e colunas
df.shape

# Apresenta uma amostra aleatoria do data set
df.sample()

filtro = df['idade']>30
df_filtrado = df[filtro]
df_filtrado

df_ordenado = df.sort_values('idade', ascending = False)
df_ordenado

df_agrupado = df.groupby('cidade').mean()
df_agrupado