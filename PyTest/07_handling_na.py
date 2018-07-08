import pandas as pd
import numpy as np

dados = {
    'nomes' : ["Joao",'Maria','Jose',np.nan,'Pedro','Judas','Her'],
    'sexo' : ['M','F','M', np.nan, 'M','M', np.nan],
    'idade' : [14,13,np.nan,np.nan, 15,13,14],
    'nota' : [4,10,7,np.nan,8,9,7]
    } #Dados a serem trabalhados em estrutura de dicionario

df = pd.DataFrame(dados) #Importando o dicionario como um dataframe do pandas

print( df.head(3) ) #Verificando o tres primeiros registros do dataframe

df2 = df.dropna() #Cria um novo dataframe retirando os NA

print('\n', df2 )

print('\n', df.dropna(how='all') ) #Retorna apenas a linha que tiver todos os valores Missing

df['serie']=np.nan #Crio a coluna serie no dataframe com valores NA

print('\n', df)

print('\n', df.dropna(how='all', axis=1) )#Axis =1 e how=all indicam que apenas colunas completamente preenchidas com NA serao dropadas

print('\n', df.dropna(thresh=3) ) #Thresh=3 indica que linha com mais de tres coluna com NA serao dropadas

print('\n', df['serie'].fillna(8) ) #Preenche os NA com valor 8

#print('\n', df['serie'].fillna(8,inplace=True) ) #Substitui os NA com valor 8 dentro de df

print('\n', df['idade'].fillna( df['idade'].mean() ) )

print('\n', df[ df['nomes'].notnull() & df['sexo'].notnull() ])

