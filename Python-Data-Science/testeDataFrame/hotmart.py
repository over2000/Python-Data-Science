#%%
import requests
import pandas
from pandas import json_normalize
from datetime import datetime, timezone
import numpy as np
from threading import Event

def getToken():
    url = "https://api-sec-vlc.hotmart.com/security/oauth/token?grant_type=client_credentials&client_id=1d1b0957-3583-43fe-8281-35e06c62fd0a&client_secret=a70f45cf-bcbf-4480-a192-25dc56158444"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic MWQxYjA5NTctMzU4My00M2ZlLTgyODEtMzVlMDZjNjJmZDBhOmE3MGY0NWNmLWJjYmYtNDQ4MC1hMTkyLTI1ZGM1NjE1ODQ0NA==',
        'Cookie': 'AWSALB=4Bg+SztA2I7BygDTyAPTwTxzxiBG2ESkRSvb6woSVNuvZHwN6LEFEWxuqwobmJCwkFh2a7IydXA6Sk7pO/ggArFm5ePXARkJhLnV+LnCWZpR7E9m+kSMYEjcKVam; AWSALBCORS=4Bg+SztA2I7BygDTyAPTwTxzxiBG2ESkRSvb6woSVNuvZHwN6LEFEWxuqwobmJCwkFh2a7IydXA6Sk7pO/ggArFm5ePXARkJhLnV+LnCWZpR7E9m+kSMYEjcKVam'
    }

    response = requests.request("POST", url, headers=headers)

    Token = response.json()

    return ('{}'.format(Token['access_token']))


def getVendasJson(token, nextPageToken, data_inicial, data_final):
    data_inicial = str(convertDateToTimestampMilliseconds(data_inicial))
    data_final = str(convertDateToTimestampMilliseconds(data_final))

    url = "https://developers.hotmart.com/payments/api/v1/sales/history?transaction_status=STARTED&transaction_status=PRINTED_BILLET&transaction_status=WAITING_PAYMENT&transaction_status=APPROVED&transaction_status=UNDER_ANALISYS&transaction_status=CANCELLED&transaction_status=PROTESTED&transaction_status=REFUNDED&transaction_status=COMPLETE&transaction_status=CHARGEBACK&transaction_status=BLOCKED&transaction_status=OVERDUE&transaction_status=EXPIRED&transaction_status=PARTIALLY_REFUNDED&max_results=100&start_date=" + data_inicial + "&end_date=" + data_final

    if (nextPageToken is not None):
        url += "&page_token=" + nextPageToken

    response = requests.request("GET", url, headers={'Authorization': 'Bearer {}'.format(token),
                                                     "Content-Type": "application/json"})

    return response.json()


def incrementMonth(data, month):
    return data + pandas.DateOffset(months=month)

def generateDateFromString(date):
    date = datetime.strptime(date, '%d/%m/%Y')
    return date.replace(tzinfo=timezone.utc)

def convertDateToTimestampMilliseconds(data):
    return int(data.timestamp() * 1000)

print('start')

token = getToken()

data_inicial = generateDateFromString('1/1/2022')
vendas = []

for x in range(6):

    data_final = incrementMonth(data_inicial, 1)
    vendasJson = getVendasJson(token, None, data_inicial, data_final)

    if "next_page_token" in vendasJson['page_info']:
        nextPageToken = vendasJson['page_info']['next_page_token']
    else:
        nextPageToken = None

    vendas.extend(vendasJson['items'])

    total_results = int(vendasJson['page_info']["total_results"])
    total_current = int(vendasJson['page_info']["results_per_page"])

    print("Processando: [" + str(data_inicial) + "] até [" + str(data_final) + "] - ["
            + str(convertDateToTimestampMilliseconds(data_inicial)) + "] até ["
            + str(convertDateToTimestampMilliseconds(data_final)) + "]")

    while nextPageToken is not None:
        percentualConcluido = (total_current / total_results) * 100
        print("ja processados [" + str(total_current) + "] de " + str(total_results) + " - " + str(
            percentualConcluido) + " %")

        gerarNovoTokenDeAcesso = total_current % 5000 == 0

        if (gerarNovoTokenDeAcesso):
            token = getToken()
            print("gerando novo token de acesso [" + token + "]")

        vendasJson = getVendasJson(token, nextPageToken, data_inicial, data_final)
        vendas.extend(vendasJson['items'])

        total_current += int(vendasJson['page_info']["results_per_page"])

        if "next_page_token" in vendasJson['page_info']:
            nextPageToken = vendasJson['page_info']['next_page_token']
        else:
            nextPageToken = None

    data_inicial = data_final

vendasHotmart = json_normalize(vendas)

# %%
vendasHotmart
# %%
vendasHotmart['product.name'].unique()
# %%
vendasHotmart.dtypes
# %%
list(vendasHotmart['product.name'].drop_duplicates())
# %%
produto = ['Ebook Comida do Futuro']
# %%
selecao = vendasHotmart['product.name'].isin(produto)
# %%
dados_comida_futuro = vendasHotmart[selecao]
# %%
dados_comida_futuro['purchase.price.value'].sum()
# %%
dados_comida_futuro
# %%
