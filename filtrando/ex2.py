#Mandar no Teams
clientes = [
    {"nome": "João Silva", "idade": 24, "genero":"M"},
    {"nome": "Maria Silva", "idade": 25, "genero":"F"},
    {"nome": "Alberto Roberto", "idade": 30, "genero":"M"},
    {"nome": "Iracema Souza", "idade": 23, "genero":"F"}
]

pegarNomes = lambda pessoa : pessoa["nome"]

listaNomes = list(map(pegarNomes,clientes))

i = 0
for nome in listaNomes:
    i += 1
    print(f"{i}º Nome:  {nome}")