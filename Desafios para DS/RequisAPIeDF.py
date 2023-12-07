import requests
import pandas as pd
import json

url = 'https://dummyjson.com/comments?limit=10&skip=10&select=body,postId'
response =  requests.get(url)
if response.status_code == 200:
    dados = json.loads(response.text)
    df = pd.json_normalize(dados, 'comments')
    print(df)
else:
    print(f"Erro ao obter dados da API. Código de status: {response.status_code}")
