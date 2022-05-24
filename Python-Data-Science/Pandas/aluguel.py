#%%
import pandas as pd
# %%
dados = pd.read_csv('aluguel.csv', sep = ';')
# %%
dados.head()
# %%
pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])
# %%
tipos_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])
# %%
tipos_de_dados.columns.name = 'Variáveis'
tipos_de_dados
# %%
dados.shape
# %%
print('A base de dados apresenta {} registros (imóveis) e {} variáveis'.format(dados.shape[0], dados.shape[1]))
# %%
