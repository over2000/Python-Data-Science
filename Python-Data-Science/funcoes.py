#%%
def media():
    valor = (1 + 2 + 3) / 3
    print(valor)

media()

#função salva em memória

# %%
def media(number_1, number_2, number_3):
  valor = (number_1 + number_2 +number_3) / 3
  print(valor)

#utilizando função passando parametros

# %%
media(1,2,3)
# %%
media(23, 45, 67)

#passando uma lista como parametro

# %%
def media(lista):
  valor = sum(lista) / len(lista)
  print(valor)
# %%
media ([1, 2, 3, 4, 5, 6, 7, 8, 9])
# %%
dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}
# %%
def km_media(dataset, ano_atual):
    for item in dataset.items():
        result = item[1]['km'] / (ano_atual - item[1]['ano'])
        print(result)
# %%
km_media(dados, 2019)
# %%
def media(lista):
  valor = sum(lista) / len(lista)
  return valor
# %%
media([1, 2, 3, 4, 5, 6, 7, 8])

#retornando valor e numero de elementos da lista

# %%
def media(lista):
  valor = sum(lista) / len(lista)
  return (valor, len(lista))
# %%
media([1, 2, 3, 4, 5, 6, 7, 8])

#função que faz a média de quilometros rodados por veiculo a cada ano


# %%
dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}
# %%
dados
# %%
def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        result.update({ item[0]: media })
    return result
# %%
km_media(dados, 2019)
# %%
def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({ 'km_media': media })
        result.update({ item[0]: item[1] })
    return result
# %%
km_media(dados, 2019)
