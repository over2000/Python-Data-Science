#%%
import pandas as pd

# %%
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# %%
list('321')
# %%
df = pd.DataFrame(data, list('321'), list('ZYX') )
# %%
df
# %%
df.sort_index(inplace= True)
# %%
df
# %%
df.sort_index(inplace= True, axis = 1)

# %%
df
# %%
df.sort_values(by = 'X', inplace = True)

# %%
df
# %%
df.sort_values(by = '3', axis = 1, inplace = True)
df
# %%
