#%%
import pandas as pd
# pd.set_option('display.max_rows', 10000)
# pd.set_option('display.max_columns', 1000)
#%%
dataset = pd.read_csv('db.csv', sep = ';')
# %%
dataset
# %%
dataset.dtypes

#função describe(). calcular estátistica descritiva
# %%
dataset[['Quilometragem', 'Valor']].describe()
# %%
dataset.info()
# %%
