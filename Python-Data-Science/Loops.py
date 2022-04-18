#Intrução For

# %%
Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
Acessorios
# %%
for item in Acessorios:
  print(item)

#Range
# %%
list(range(10))
# %%
for i in range(10):
    print(i ** 2)
# %%
quadrado = []
for i in range(10):
    quadrado.append(i ** 2)

quadrado

#list comprehensions

# %%
[i ** 2 for i in range(10)]


#Loops Aninhados


# %%
dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
dados
# %%
for lista in dados:
    print(lista)
# %%
for lista in dados:
    for item in lista: 
        print(item)
# %%
Acessorios = []
for lista in dados:
  for item in lista:
        Acessorios.append(item)
print(Acessorios)

#A função SET é muito utilizada para realizar operações em conjuntos matemáticos, como interseção e união. Outro uso é justamente a remoção de duplicatas em uma sequência
# %%
list(set(Acessorios))

#list comprehensions

# %%
list(set([item for lista in dados for item in lista]))

# %%
dados = [ 
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]
# %%
result = []
for lista in dados:
    for item in lista:
        result.append(item)
result

#Lembre-se que o operador de soma (+), quando aplicado em duas listas, retorna a concatenação destas listas

# %%
result_2 = []
for lista in dados:
    result_2 += lista
result_2
# %%
[item for lista in dados for item in lista]


# %%
# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]
dados
# %%
for lista in dados:
    print(lista)
# %%
for lista in dados:
  if (lista[2] == True):
    print(lista)
# %%
zero_km_Y = []

for lista in dados:
  if (lista[2] == True):
    zero_km_Y.append(lista)
zero_km_Y
# %%
zero_km_N = []

for lista in dados:
  if (lista[2] == False):
    zero_km_N.append(lista)
zero_km_N

#list comprehensions
# %%
[lista for lista in dados if lista[2] == True]
# %%
zero_km_N, zero_km_Y = [], []

for lista in dados:
  if (lista[2] == True):
    zero_km_Y.append(lista)
  else:
    zero_km_N.append(lista)
# %%
zero_km_N
# %%
zero_km_Y
# %%
dados
# %%
A, B, C = [], [], []

for lista in dados:
  if lista[1] <= 2000:
    A.append(lista)
  elif lista[1] >= 2000 and lista[1] <= 2010:
    B.append(lista)
  else:
    C.append(lista)

# %%
C
# %%
