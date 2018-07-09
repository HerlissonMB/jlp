import pandas as pd
import numpy as np

#Conjunto de dados das eleicoes primarias dos EUA de 2016
dados = pd.read_csv("C:/Users/Herlisson/Documents/Curso de Machine Learning/3. Pandas/primary-results.csv")

print( dados.head(5) )

candidates = dados['candidate'].drop_duplicates() #Nomes dos candidatos que foram citados nas primarias

states = dados['state'].drop_duplicates() 

#i=0
#for estados in states:
#    i=i+1
#    print(i,'. ',estados,'\n')

print('\n', candidates ) 

print('\n', dados.shape) #Retorna a dimensao do df

#Groupby indica que o resumo sera feito para os valores da coluna candidate
#Aggregate esta recebendo um dicionario da coluna votes e fips que tera as medidas resumo indicadas como elemento do dicionario para cada grupo do Groupby

resumo = dados.groupby('candidate').aggregate( {'votes': [min,np.mean,max,np.std], 'fips': [min,np.mean,max,np.std] } ).round(2)

print('\n', resumo)

resumo2= dados.groupby('candidate').aggregate( {'fraction_votes': [min,np.mean,max,np.std] } ).round(2)

print('\n', resumo2)

def votes_filter(x):
    return x['votes'].sum() > 10000

resumo3 = dados.groupby('state').filter(votes_filter)

print( resumo3.head(10) )

