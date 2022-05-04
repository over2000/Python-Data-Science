#%%
import pandas as pd

# %%
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)

# %%
dataset.Motor
# %%
select = dataset.Motor == 'Motor Diesel'
# %%
type(select)
# %%
dataset[select]
# %%
dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)]
# %%
dataset.query('Motor == "Motor Diesel" and Zero_km == True')
# %%
import pandas as pd

dados = {
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor Diesel', 'Motor 1.6'],
    'Ano': [2019, 2003, 1991, 2019, 1990],
    'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Zero_km': [True, False, False, True, False],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
}

dataset = pd.DataFrame(dados, index = ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'])
# %%
dataset.query('Motor == "Motor Diesel" or Zero_km == True')
# %%
dataset[(dataset.Motor == 'Motor Diesel') | (dataset.Zero_km == True)]
# %%
dataset.query('Motor == "Motor Diesel" | Zero_km == True')
# %%
dataset[(dataset.Motor == 'Motor Diesel') | (dataset.Zero_km == True)]
# %%
