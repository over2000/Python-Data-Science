#%%
import pandas as pd

# %%
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)
# %%
dataset.info()
# %%
dataset.Quilometragem.isna()
# %%
dataset[dataset.Quilometragem.isna()]

# %%
dataset.fillna(0, inplace=True)
# %%
dataset
# %%
dataset.query("Zero_km == True")
# %%
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)

# %%
dataset
# %%
dataset.dropna(subset = ['Quilometragem'], inplace=True)
# %%
dataset
# %%
#isna() - Detecta valores faltantes. Retorna um DataFrame ou uma Series booleana, identificando se o registro é um NA

#fillna() - Preenche os registros identificados com NA, utilizando um método específico

#dropna() - Remove registros com valores identificados como NA