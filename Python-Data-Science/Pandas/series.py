#%%
from hashlib import shake_128
from numpy import column_stack
import pandas as pd
#%%
data = [1, 2, 3, 4, 5]

s = pd.Series(data)
# %%
s
# %%
index = ['Linha' + str(i) for i in range(5)]
# %%
index
# %%
s = pd.Series(data = data, index = index)
# %%
s
# %%
data = {'Linha' + str(i) : i +1 for i in range(5) }
# %%
data
# %%
s = pd.Series(data)
# %%
s
# %%
s1 = s+2
# %%
s1
# %%
s2 = s + s1
# %%
s2
# %%
data = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]
# %%
df1 = pd.DataFrame(data = data)
# %%
df1
# %%
index = ['Linha' + str(i) for i in range(3)]
# %%
df1 = pd.DataFrame(data = data, index = index)

# %%
df1
# %%
columns = ['Coluna' + str(i) for i in range(3)]

# %%
columns
# %%
df1 = pd.DataFrame(data = data, index = index, columns = columns)

# %%
df1
# %%
data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
        'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
        'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}
# %%
df2 = pd.DataFrame(data)
# %%
df2
# %%
data = [(1, 2, 3), 
        (4, 5, 6), 
        (7, 8, 9)]
# %%
data
# %%
df3 = pd.DataFrame(data = data, index = index, columns = columns)

# %%
df3
# %%
df1[df1 > 0] = 'A'
# %%
df1
# %%
df2[df2 > 0] = 'B'
# %%
df2
# %%
df3[df3 > 0] = 'C'

# %%
df4 = pd.concat([df1, df2, df3])
# %%
df4
# %%
df4 = pd.concat([df1, df2, df3], axis= 1)

# %%
df4
# %%
df1 = pd.DataFrame({'A': {'X': 1}, 'B': {'X': 2}})
df2 = pd.DataFrame({'C': {'X': 3}, 'D': {'X': 4}})
pd.concat([df1, df2])
# %%
dados = [('A', 'B'), ('C', 'D')]
df = pd.DataFrame(dados, columns = ['L1', 'L2'],  index = ['C1', 'C2'])
df
# %%
dados = [[1, 2, 3], [4, 5, 6]]
index = 'X,Y'.split(',')
columns = list('CBA')[::-1]
df = pd.DataFrame(dados, index, columns)
df
# %%
dados = {'A': {'X': 1, 'Y': 3}, 'B': {'X': 2, 'Y': 4}}
df = pd.DataFrame(dados)
df
# %%
