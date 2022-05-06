#%%
import pandas as pd

# %%
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)

#adicionando coluna quilometragem média de um veiuclo, e tratando divsões por zero

# %%
for index, row in dataset.iterrows():
    if(2019 - row['Ano'] != 0):
        dataset.loc[index, 'km_media'] = row['Quilometragem'] / (2019 - row['Ano'])
    else:   
        dataset.loc[index, 'km_media'] = 0
 # %%
dataset
# %%
