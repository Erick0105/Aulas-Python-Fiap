import json

novoArquivo = open("acesso-arquivo-json\dados.json", "r", encoding="utf-8")
conteudo = novoArquivo.read()
lista = json.loads(conteudo)
contador = 0
for i in lista:
    contador += 1
    print(f'\n{contador}º nome {i["nome"]}')