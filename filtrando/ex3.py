#Crie uma nova lista contendo apenas os produtos que estão em estoque
listaProd = [
    {"nome":"Camisa","preco":50,"emEstoque":True},
    {"nome":"Calça","preco":80,"emEstoque":False},
    {"nome":"Chapéu","preco":30,"emEstoque":True}
]

verificarEstoque = lambda produto : produto["emEstoque"] == True

novaListaProd = list(filter(verificarEstoque, listaProd))

print("Os produtos que estão no estoque são:")
total = 0
for produto in novaListaProd:
    print(f'{produto["nome"]} de R${produto["preco"]}')
    total =  total + produto["preco"]
print(f'O valor total desses produtos é igual a R${total}')