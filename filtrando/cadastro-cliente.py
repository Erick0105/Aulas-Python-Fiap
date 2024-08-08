clientes = [
    {"nome": "João Silva", "idade": 24, "genero":"M"},
    {"nome": "Maria Silva", "idade": 25, "genero":"F"},
    {"nome": "Alberto Roberto", "idade": 30, "genero":"M"},
    {"nome": "Iracema Souza", "idade": 23, "genero":"F"}
]

filtroHomem = lambda pessoa : pessoa["genero"] == "M"
listaHomens = list(filter(filtroHomem, clientes))

filtroMulher = lambda pessoa : pessoa["genero"] == "F"
listaMulheres = list(filter(filtroMulher, clientes))

print(f'Lista de Homens: {listaHomens}\nLista de Mulheres: {listaMulheres}')