import requests
import json
url = "https://aula-python-fiap-default-rtdb.firebaseio.com/contatos.json"

resposta = requests.get(url)
resposta_texto = resposta.text


contatos = json.loads(resposta_texto)


print(contatos)
print("Chaves dos contatos:")
for contato in contatos.values():
    print(contato)