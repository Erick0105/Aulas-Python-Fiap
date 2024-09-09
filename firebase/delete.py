import requests

url = "https://aula-python-fiap-default-rtdb.firebaseio.com/contatos/-O6Lk7QhfJF8kOak2Twl.json"

resposta = requests.delete(url)
print(resposta)
