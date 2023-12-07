import requests
import pandas as pd
import json

#response = requests.get('https://dummyjson.com/comments?limit=10&skip=10&select=body,postId')
url = 'https://dummyjson.com/comments?limit=10&skip=10&select=body,postId'
response =  requests.get(url)
if response.status_code == 200:
    dados = json.loads(response.text)
    df = pd.json_normalize(dados, 'comments')
    df = df.add_prefix('comments_')
    #df = pd.DataFrame(dados)
    print(df)
else:
    print(f"Erro ao obter dados da API. Código de status: {response.status_code}")
"""dados = response.json()
#df = json.loads(dados)
df1 = pd.DataFrame(dados)
df2 = df1.explode('comments')
df3 = pd.DataFrame(df2, columns=['id', 'body'])

print(df1)
print(df2)
print(df3)"""
