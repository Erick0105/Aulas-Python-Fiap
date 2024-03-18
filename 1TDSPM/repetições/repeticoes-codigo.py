executar_novamente = True
while executar_novamente == True:
    nome = str(input("Por favor digite seu nome: "))
    print(f'Bom dia{nome}')
    resposta = str(input("Você deseja executar o programa novamente? (S/N)"))
    if resposta == "S":
        executar_novamente = True
    else:
        executar_novamente = False
