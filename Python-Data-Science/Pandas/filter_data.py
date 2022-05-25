#%%
import pandas as pd

# %%
dados = pd.read_csv('aluguel.csv', sep = ';')
# %%

list(dados['Tipo'].drop_duplicates())
# %%
residencial = ['Quitinete', 
'Casa',
'Apartamento',
'Casa de Condomínio',
'Casa de Vila']
# %%
residencial
# %%
dados.head(10)
# %%
dados['Tipo'].isin(residencial).head(10)
# %%
selecao = dados['Tipo'].isin(residencial)
# %%
dados_residencial = dados[selecao]
# %%
dados_residencial
# %%
list(dados_residencial['Tipo'].drop_duplicates())
# %%
dados_residencial.shape[0]
# %%
dados_residencial.index = range(dados_residencial.shape[0])

# %%
dados_residencial

#%%










# %%
import pandas as pd

numeros = [i for i in range(11)]
letras = [chr(i + 65) for i in range(11)]
nome_coluna = ['N']

df = pd.DataFrame(data = numeros, index = letras, columns = nome_coluna)
# %%
selecao = df['N'].isin([i for i in range(11) if i % 2 == 0])
df = df[selecao]
df
# %%
