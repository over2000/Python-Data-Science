#%%
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados
# %%
dados
# %%
type(dados)
# %%
carros = ['Jetta Variant', 'Passat', 'Crossfox']
carros
# %%
valores = [88078.64, 106161.94, 72832.16]
valores
# %%
list(zip(carros, valores))
# %%
dados = dict(zip(carros, valores))
dados
# %%
nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']
kms = [15000, 12000, 32000, 8000, 50000]
# %%
dict(zip(nomes, kms))

#Operações com dicionários

# %%
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados
# %%
dados['Passat']
# %%
'Passat' in dados
# %%
'Fusca' in dados
# %%
'Fusca' not in dados
# %%
len(dados)
# %%
dados['DS5'] = 124549.07
dados
# %%
del dados['Passat']
dados
# %%
dados = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
    }, 
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
    }
}
# %%
'acessorios' in dados['Crossfox']
# %%
'acessorios' in dados['Passat']
# %%
dados['Crossfox']['valor']
# %%
dados['Passat']['acessorios'][-1]
# %%
dados

#update(), copy(), pop() e clear().

# %%
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados
# %%
dados.update({'Passat Turbo': 6161.94})
dados
# %%
dados.update({'Passat': 106161.95, 'Fusca': 150000})
dados
# %%
dadosCopy = dados.copy()
dadosCopy
# %%
del dadosCopy['Fusca']
dadosCopy
# %%
dados

#pop() elimina uma chave do dicionário e retorna o seu valor. 

# %%
dadosCopy.pop('Passat')

#clear(), que simplesmente limpa todo o dicionário.

# %%
dadosCopy.clear()
dadosCopy

#Iterando em dicionários

# %%
dados = {'Jetta': 88000, 'Crossfox': 72000, 'DS5': 124000}
# %%
dados.pop()
# %%
dados.clear()
# %%
dados = {'Crossfox': 72832.16, 'DS5': 124549.07,  'Fusca': 150000,  'Jetta Variant': 88078.64,  'Passat': 106161.95}
dados

#keys(), que simplesmente retorna todas as chaves contidas

# %%
dados.keys()
# %%
for key in dados.keys():
  print(dados[key])
# %%
dados.values()
# %%
dados.items()
# %%
for item in dados.items():
    print(item)
# %%
for key, value in dados.items():
    print(key, value)
# %%
for key, value in dados.items():
  if (value > 100000):
    print(key)
# %%
dados = {
    'Crossfox': {'valor': 72000, 'ano': 2005}, 
    'DS5': {'valor': 125000, 'ano': 2015}, 
    'Fusca': {'valor': 150000, 'ano': 1976}, 
    'Jetta': {'valor': 88000, 'ano': 2010}, 
    'Passat': {'valor': 106000, 'ano': 1998}
}

#somente os nomes dos veículos com ano de fabricação maior ou igual a 2000.

# %%
for item in dados.items():
    if(item[1]['ano'] >= 2000):
        print(item[0])
# %%
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados

#soma total dos valores sem built-in functions

# %%
valores = []

for valor in dados.values():
  valores.append(valor)
valores
# %%
soma = 0
for valor in dados.values():
  soma += valor
soma

#soma total com built-in functions

# %%
list(dados.values())
# %%
sum(dados.values())