#%%
import pandas as pd
# %%
dados = pd.read_csv('aluguel.csv', sep = ';')
# %%
dados.head(10)
# %%
dados['Tipo']
# %%
dados.Tipo
# %%
tipo_de_imovel = dados['Tipo']
# %%
type(tipo_de_imovel)
# %%
tipo_de_imovel.drop_duplicates(inplace = True)
# %%
tipo_de_imovel
# %%
tipo_de_imovel = pd.DataFrame(tipo_de_imovel)
# %%
tipo_de_imovel
# %%
tipo_de_imovel.index
# %%
tipo_de_imovel.shape[0]
# %%
range(tipo_de_imovel.shape[0])
# %%
for i in range(tipo_de_imovel.shape[0]):
    print(i)
# %%
tipo_de_imovel.index = range(tipo_de_imovel.shape[0])
# %%
tipo_de_imovel.index
# %%
tipo_de_imovel
# %%
tipo_de_imovel.columns.name = 'ID'
# %%
