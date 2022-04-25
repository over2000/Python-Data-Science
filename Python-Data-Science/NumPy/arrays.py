#%%
import numpy as np

#listas com numpy

#%%
np.arange(10)
# %%
km = np.array([1000, 2300, 4987, 1500])
km
# %%
dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
dados
# %%
Acessorios = np.array(dados)

# %%
Acessorios

#Operações com arrays
#%%
km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
# %%
idade = 2019 - anos
idade
# %%
km_media = km / idade
# %%
km_media
# %%
dados = np.array([km, anos])
dados
# %%
dados.shape
# %%
km_media = dados[0] / (2019 - dados[1])
km_media
# %%
km_media
# %%
peso = np.array([106.0, 68.5, 75.0])
altura = np.array([1.9, 1.53, 1.75])
IMC = peso / (altura * altura)
IMC
# %%

peso = np.array([106.0, 68.5, 75.0])
altura = np.array([1.9, 1.53, 1.75])
IMC = peso / altura ** 2
IMC
# %%
dados
# %%
contador = np.arange(10)
contador
# %%
item = 6
index = item - 1
contador[index]
# %%
contador[-1]
# %%
dados[1][2]
# %%
dados[1,2]
# %%
contador[1:4]

#o ultimo elemento é o passo, ele pula
# %%
contador[1:8:2]
# %%
contador[1::2]
# %%
dados[:, 1:4]

#Aqui estamos fatiamento o conjunto dados de modo a selecionarmos somente os veículos com os índices 1 e 2 (dados[:, 1:3]). Em seguida, pegamos somente a primeira linha - ou seja, o índice 0 desse conjunto. De posse desses valores, passamos a dividi-los por 2019 subtraído de dados[:, 1:3][1], a segunda linha do conjunto também fatiada somente com os veículos de índices 1 e 2. Com isso, estamos dividindo a quilometragem total dos veículos pelo tempo desde a sua fabricação, o que nos resulta na quilometragem média:



# %%
dados[:, 1:3][0] / (2019 - dados[:, 1:3][1])
# %%
contador = np.arange(10)
contador
# %%
contador > 5
# %%
contador[contador >5]
# %%
dados[1] > 2000
# %%
dados[:, dados[1] > 2000]
# %%
dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'],
        ['Sheila', 'solteiro', 'feminino'],
        ['Bruno', 'solteiro', 'masculino'],
        ['Rita', 'casado', 'feminino']
    ]
)

#nome e estado civil, somente das pessoas do sexo masculino.

# %%
dados[0::2, :2]

#Atributos e métodos do NumPy

# %%
dados = np.array([[44410.,  5712., 37123.,     0., 25757.], [ 2003.,  1991.,  1990.,  2019.,  2006.]])
dados

#shape. Esse atributo retorna uma tupla com as dimensões do array. Nesse caso, temos a quantidade de linhas na primeira posição e a de colunas na segunda.

# %%
dados.shape

#ndim. retorna o número de dimensões do array. No nosso caso, como temos linhas e colunas, temos duas dimensões.

# %%
dados.ndim

#size nos mostra o número de elementos de um array.

# %%
dados.size

 #dtype retorna o tipo de dado dos elementos armazenados no array,

# %%
dados.dtype

#T ou transpose() nos retorna o array transposto, ou seja, ele transpõe uma matriz, convertendo linhas em colunas e vice-versa.

# %%
dados.T
# %%
dados.transpose()

#Métodos

#tolist(). transforma um array Numpy em uma lista do Python. Isso pode ser útil quando precisamos executar algum método ou procedimento que não é possível com os arrays Numpy.

# %%
dados.tolist()
# %%
contador = np.arange(10)
contador

#reshape(). retorna um array contendo os mesmos dados, mas com uma nova forma. 

# %%
contador.reshape((5,2))
# %%
contador.reshape((5, 2), order='C')
# %%
km = [44410, 5712, 37123, 0, 25757]
anos = [2003, 1991, 1990, 2019, 2006]
# %%
info_carros = km + anos
info_carros

#Imagine que já encontramos esses dados "bagunçados", de maneira que fica difícil trabalharmos com eles. O reshape() nos ajuda a solucionar esse tipo de problema. Como os dados são do mesmo tipo, podemos transformá-los em um array Numpy

# %%
np.array(info_carros)
# %%
np.array(info_carros).reshape((2, 5))

#order='F' para instruirmos a indexação da linguagem F

# %%
np.array(info_carros).reshape((5, 2), order='F')
# %%
dados_new = dados.copy()
dados_new
# %%
dados_new.resize((3, 5), refcheck=False)
dados_new

#conseguiremos criar a linha extra no array, e poderemos preenchê-las com as novas informações. Para isso, atribuiremos à linha dados_new[2] o cálculo de quilometragem média com o qual já estamos acostumados.

# %%
dados_new[2] = dados_new[0] / (2019 - dados_new[1])
dados_new

#Estatísticas com NumPy

# %%
anos = np.loadtxt(fname = "carros-anos.txt", dtype = int)
km = np.loadtxt(fname = "carros-km.txt")
valor = np.loadtxt(fname = "carros-valor.txt")
# %%
dataset = np.column_stack((anos, km, valor))
dataset
# %%
dataset.shape

#calcular média, Precisaremos informar ao Numpy com que eixo queremos trabalhar, as linhas ou as colunas, algo que é possível por meio do parâmetro axis. Com axis=0, por exemplo, conseguiremos a média das colunas.

#media de km's
# %%
np.mean(dataset[:,1])

#media de valores

# %%
np.mean(dataset[:,1])

#desvio padrão dos valores usando o método np.std().

# %%
np.std(dataset[:,2])

#somatórios

# %%
dataset.sum(axis = 0)
# %%
dataset[:, 1].sum()
# %%
np.sum(dataset, axis = 0)
# %%
idades = np.array([10, 23, 45, 34, 25])
# %%
np.sum(idades) / idades.size
# %%
np.mean(idades)
# %%
idades.mean()
# %%
