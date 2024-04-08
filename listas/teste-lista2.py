lista = ["Isabela", "Guilherme", "Juliana", "Pablo", "Mikael", "Enzo", "Vicenzo", "Guilherme"]

pos = lista.index("Pablo") #localiza o item da lista
print(f'O pablo está na posição {pos}')

pos = lista.index("Guilherme")
print(f'O Guilherme está na posição {pos}')

pos = lista.index("Guilherme", 2)
print(f'O segundo Guilherme está na posição {pos}')

try:
    pos = lista.index("João")
    print(f'O joão esta na posição: {pos}')
except:
    print("Não há João na Lista")