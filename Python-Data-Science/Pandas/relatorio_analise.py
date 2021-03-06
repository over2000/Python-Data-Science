#%%
import pandas as pd
# %%
dados = pd.read_csv('aluguel.csv', sep = ';')
# %%
dados.head(10)
# %%
# Selecione somente os imóveis classificados com tipo 'Apartamento'.

selecao = dados['Tipo'] == 'Apartamento'
 
#%%
selecao

#%%
n1 = dados[selecao].shape[0]
n1

# Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.

#%%
selecao = (dados['Tipo'] == 'Casa') | (dados['Tipo'] ==  'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
n2 = dados[selecao].shape[0]
n2

# Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.

#%%
selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao].shape[0]
n3

# Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
# %%

selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
n4 = dados[selecao].shape[0]
n4
# %%
print("Nº de imóveis classificados com tipo 'Apartamento' -> {}".format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'-> {}".format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}".format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {}".format(n4))
# %%
