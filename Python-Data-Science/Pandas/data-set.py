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

#tuplas

# %%
nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
nomes_carros
# %%
nomes_carros[0]
# %%
nomes_carros[1]
# %%
nomes_carros[-1]
# %%
nomes_carros[1:3]
# %%
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))
nomes_carros
# %%
nomes_carros[-1]
# %%
nomes_carros[-1][1]
# %%
carros = (
    (
        'Jetta Variant',
        'Motor 4.0 Turbo',
        2003,
        False,
        ('Rodas de liga', 'Travas elétricas', 'Piloto automático')
    ),
    (
        'Passat',
        'Motor Diesel',
        1991,
        True,
        ('Central multimídia', 'Teto panorâmico', 'Freios ABS')
    )
)
# %%
carros[0][3]
# %%
carros[-1][-1][-1]
# %%
carros[0][-1][:2]
# %%
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
nomes_carros
# %%
for item in nomes_carros:
  print(item)

#desempacotamento de tupla

# %%
carro_1, carro_2, carro_3, carro_4 = nomes_carros
# %%
carro_1
# %%
_, A, _, B = nomes_carros
# %%
A
# %%
B
# %%
_, C, *_ = nomes_carros
# %%
C
# %%
carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
carros
# %%
valores = [88078.64, 106161.94, 72832.16, 124549.07]
valores

#zip(). cria um iterador com tuplas (de maneira semelhante à função range())

# %%
for item in zip(carros, valores):
    print(item)
# %%
for carro, valor in zip(carros, valores):
  print(carro, valor)
# %%
for carro, valor in zip(carros, valores):
  if(valor > 100000):
    print(carro)
# %%
carros = (
    (
        'Jetta Variant',
        'Motor 4.0 Turbo',
        2003,
        False,
        ('Rodas de liga', 'Travas elétricas', 'Piloto automático')
    ),
    (
        'Passat',
        'Motor Diesel',
        1991,
        True,
        ('Central multimídia', 'Teto panorâmico', 'Freios ABS')
    )
)
# %%
for tupla in carros:
    for item in tupla[-1]:
        print(item)
# %%
nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']
kms = [15000, 12000, 32000, 8000, 50000]
# %%

for nome, km in zip(nomes, kms):
    if(km < 20000):
        print(nome)
# %%
