import requests

url = "https://aula-python-fiap-default-rtdb.firebaseio.com/contatos.json"

contato_novo = {
    "nome":"Alberto Santos",
    "email":"alberto@teste.com",
    "telefone":"(13)4444-4444"
}

resposta = requests.post(url,json=contato_novo)

print(resposta)