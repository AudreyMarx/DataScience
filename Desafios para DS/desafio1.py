#DESAFIO 01 = Leia o TXT 'lista_desafio' que contém várias listas dentro dele e faça um algoritmo que retorne o tamanho da maior lista.

with open("lista_desafio.txt", "r") as arquivo:
    tamanhos = [len(linha.split()) for linha in arquivo]
tamanho_maior_lista = max(tamanhos)
print("Tamanho da maior lista:", tamanho_maior_lista)