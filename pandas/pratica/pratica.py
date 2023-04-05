import pandas as pd
arquivo = 'pandas\pratica\acidentes2021.csv'
dataset = pd.read_csv(arquivo, sep=';', header = 0)
# heades seria a coluna(basicamente a linha no topo que define o tipo da informação que vai ter embaixo dela)
print('Base carregada com sucesso')

dataset.head()

dataset.info()

dataset2 = dataset[['moto', 'auto']]
dataset2.info()

#  comando isna verifica se o registro está vazio
# o comando sum faz o somatorio, nesse caso vai somar
# toda vez que o isna encontrar um registro vazio

print('Número de linhas vazias para cada coluna(NaN):')
dataset.isna().sum()

# Lista de colunas indesejadas que não serão úteis para a classificação
colunas_indesejadas = ['numero', 'detalhe_endereco_acidente', 'complemento', 
                       'num_semaforo', 'acidente_verificado', 'situacao_semaforo', 'divisao_via1', 'divisao_via2', 'divisao_via3']
print(f'Removendo as colunas indesejadas: {colunas_indesejadas}')
print(f'Dataset antes da remoção das colunas: {dataset.shape[0]} linhas e {dataset.shape[1]} colunas')

# Removendo as colunas indesejadas.
# O parâmetro 'labels' espera receber uma lista com os nomes das colunas que devem ser removidas (dropadas).
# O parâmetro 'axis' espera receber 0 (ou 'index') para remover linhas ou 1 (ou 'columns') para remover colunas.
# No nosso caso, iremos remover as colunas (axis=1 ou axis='columns')
dataset_novo = dataset.drop(labels=colunas_indesejadas, axis=1)

print(f'Dataset após a remoção das colunas: {dataset_novo.shape[0]} linhas e {dataset_novo.shape[1]} colunas\n')
dataset_novo.head()

dataset_novo.isna().sum()

dataset_novo['tipo'].unique()

# nesse caso foi pego o nome de uma coluna e dentro dessa coluna foi analisada as situações unicas
dataset_novo['situacao'].unique()

print('TOTAL SITUAÇÃO FINALIZADA --->', (dataset_novo['situacao']=="FINALIZADA").sum())
print('TOTAL SITUAÇÃO CANCELADA --->',(dataset_novo['situacao']=='CANCELADA').sum())
print('TOTAL SITUAÇÃO DUPLICIDADE --->',(dataset_novo['situacao']=='DUPLICIDADE').sum())
print('TOTAL SITUAÇÃO EVADIU-SE --->',(dataset_novo['situacao']=='EVADIU-SE').sum())


dataset_novo.loc[dataset_novo['situacao'] == 'FINALIZADA', 'situacao'] = 0
dataset_novo.loc[dataset_novo['situacao'] == 'CANCELADA', 'situacao'] = 1
dataset_novo.loc[dataset_novo['situacao'] == 'DUPLICIDADE', 'situacao'] = 2
dataset_novo.loc[dataset_novo['situacao'] == 'EVADIU-SE', 'situacao'] = 3

dataset_novo['situacao'].unique()

print('TOTAL SITUAÇÃO FINALIZADA --->', (dataset_novo['situacao']==0).sum())
print('TOTAL SITUAÇÃO CANCELADA --->',(dataset_novo['situacao']==1).sum())
print('TOTAL SITUAÇÃO DUPLICIDADE --->',(dataset_novo['situacao']==2).sum())
print('TOTAL SITUAÇÃO EVADIU-SE --->',(dataset_novo['situacao']==3).sum())

import pandas_profiling

profile = pandas_profiling.ProfileReport(dataset)
profile