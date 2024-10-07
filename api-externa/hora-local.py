import requests
import json

cidade = input("Qual cidade você deseja saber a hora atual?")

parametros = {
    'key': 'a62f6ad9c5e74a809c9120338240710',
    'q': f'{cidade}'
}
res = requests.get(f'https://api.weatherapi.com/v1/timezone.json', params=parametros)

dic_cidade = json.loads(res.content)

print(f' O dia e horario atual da {cidade} é exatamente:  {dic_cidade['location']['localtime']}')

# res = requests.get("https://api.weatherapi.com/v1/timezone.json?key=a62f6ad9c5e74a809c9120338240710&q=São Paulo&aqi=no")
# print(res.content)