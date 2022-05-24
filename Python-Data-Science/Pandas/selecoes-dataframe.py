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
dataset[['Quilometragem', 'Valor']].max()
# %%
dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}
# %%
def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({ 'km_media': media })
        result.update({ item[0]: item[1] })

    return result
# %%
km_media(dados, 2019)
# %%

carros = pd.DataFrame(km_media(dados, 2019)).T
# %%
carros
# %%
data = pd.DataFrame(dados).T

# %%
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)
# %%
dataset['Valor']
# %%
dataset.head()
# %%

#series
type(dataset['Valor'])
# %%
dataset[['Valor']]
# %%
#dataframe
type(dataset[['Valor']])
# %%
dataset[0:3]
# %%
dataset.loc[['Passat', 'DS5']]
# %%
dataset.loc[['Passat', 'DS5'], ['Motor', 'Valor']]

# %%
dataset
# %%
dataset.loc[:, ['Motor', 'Valor']]
# %%
dataset.iloc[[1]]
# %%
dataset.iloc[1:4]

# %%
dataset.iloc[1:4, [0, 5, 2]]

# %%
dataset.iloc[[1, 42, 22], [0, 5, 2]]

# %%
import pandas as pd

dados = {
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor 2.0', 'Motor 1.6'],
    'Ano': [2019, 2003, 1991, 2019, 1990],
    'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Zero_km': [True, False, False, True, False],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
}

dataset = pd.DataFrame(dados, index = ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'])
# %%
dataset.iloc[[1, 3], [0, -1]]
# %%
dataset.loc[['Passat', 'DS5'], ['Motor', 'Valor']]
# %%

