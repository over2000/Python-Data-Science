#Operações

# %%

acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

# %%

'Rodas de liga' in acessorios

# %%

A = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro']
B = ['Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

# %%

A+B
# %%

len(acessorios)
# %%
carro = [
    'Jetta Variant', 
    'Motor 4.0 Turbo', 
    2003, 
    44410.0, 
    False, 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático'], 
    88078.64
]


# %%
'2003' in carro
# %%
'Rodas de liga' in carro
# %%
'False' not in carro

# %%
Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False, ['Rodas de liga', 'Travas elétricas', 'Piloto automático'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, ['Central multimídia', 'Teto panorâmico', 'Freios ABS'], 106161.94]
Carros = [Carro_1, Carro_2]
Carros
# %%

#Seleções 

Carros
# %%
Carros[0]
# %%
Carros[0][-2]
# %%
Carros[0][-2][1]
# %%
acessorios[2:6]
# %%
acessorios[2:]
# %%
acessorios[:6]
# %%
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# %%
letras[:2]
# %%
letras[2:5]
# %%
letras[-3:]
# %%
carros = [
    [
        'Jetta Variant',
        'Motor 4.0 Turbo',
        2003,
        False,
        ['Rodas de liga', 'Travas elétricas', 'Piloto automático']
    ],
    [
        'Passat',
        'Motor Diesel',
        1991,
        True,
        ['Central multimídia', 'Teto panorâmico', 'Freios ABS']
    ]
]
# %%
carros[1][3]
# %%
carros[1][-1][-2]
# %%
carros[0][-1]


#Métodos
# %%
Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
Acessorios
# %%
Acessorios.sort()
Acessorios
# %%
Acessorios.append('4 x 4')
Acessorios
# %%
Acessorios.pop()
# %%
Acessorios.pop(3)
# %%
Acessorios.pop()
# %%
Acessorios_2 = Acessorios.copy()
Acessorios_2
# %%
Acessorios_2.append('4 x 4')
Acessorios_2
# %%
Acessorios
# %%
Acessorios = [
    'Rodas de liga', 
    'Travas elétricas', 
    'Piloto automático',
    'Bancos de couro',
    'Ar condicionado'
]
Acessorios
# %%
Acessorios.append('Airbag')
Acessorios.sort()
Acessorios.pop()
Acessorios.append('Vidros elétricos')
Acessorios
# %%
dados = [1, 2, 3, 4]
dados_copia = dados
dados_copia.append(5)
# %%
dados
# %%
dados_copia
# %%
