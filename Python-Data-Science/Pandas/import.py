
#%%
import pandas as pd

#%%
json = open('aluguel.json')

# %%
print(json.read())
# %%
df_json = pd.read_json('aluguel.json')
# %%
df_json
# %%
txt = open('aluguel.txt')
print(txt.read())
# %%
df_txt = pd.read_table('aluguel.txt')
# %%
df_txt

# %%
