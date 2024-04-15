# Faça um programa para cadastrar produtos da feira, o programa deverá perguntar ao usuário sobre detalhes do produto como: (nome,cor,preço, unidade de medida,) e em seguida devera guardar as informações em um dicionario.

lista = []

quantidade = int(input("Quanto produtos deseja cadastras?"))

for i in range(quantidade):
    produto = {}
    produto["nome"] = input("Digite o nome do produto")
    produto["cor"] = input("Digite a cor do produto")
    produto["preco"] = float(input("Digite o preço do produto"))
    produto["unidade_medida"] = input("informe a unidade de medida: ")

    lista.append(produto)


for p in lista:
    print("Produto: ", p["nome"])
    print(f"cor: {p['cor']} preço: {p['preco']} Unidade de medida: {p['unidade_medida']}")


print("Digite o nome do produto a ser pesquisado ==> ")
n1 = input()
for p in lista:
    if n1 == p["nome"]:
         print("Produto: ", p["nome"])
         print(f"cor: {p['cor']} preço: {p['preco']} Unidade de medida: {p['unidade_medida']}")

# resposta = int(input("Quantos produtos de feira deseja cadastras?\n"))

# for i in range(resposta):
#     nome = str(input("Qual o nome do produto?\n"))
#     cor = str(input("Qual a cor do produto?\n"))
#     preco = float(input("Qual o preço do produto?\n"))
#     unidade_medida = str(input("Qual a unidade de medidas deste produto?\n"))
    

# d1 = {"produto1",}

