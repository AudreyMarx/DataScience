import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://http.cat/status/200'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
imagem = soup.find('img')

if imagem:
    link_imagem = urljoin(url, imagem['src'])
    print("Link da imagem: ", link_imagem)
    print("HTML para exibir a imagem: ", f'<img src="{link_imagem}" alt="Imagem">')
else:
    print("Nenhuma tag <img> encontrada no HTML.")
