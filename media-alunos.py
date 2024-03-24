print("Programa para calcular a média")

escolha = True
while escolha == True:
    nome_aluno = str(input("Qual é o nome do estudante? "))
    n1 = int(input("Qual a 1º nota do estudante? "))
    n2 = int(input("Qual a 2º nota do estudante? "))
    n3 = int(input("Qual a 3º nota do estudante? "))

    media = n1 + n2 + n3

    print("Nome            Nota 1         Nota 2         Nota 3         Média")
    print(f'{nome_aluno:<12}{n1:<9.1f}{n2:<9.1f}{n3:<9.1f}{media:>5.1f}')

    escolha = str(input("Deseja calcular a média de outro estudante? (S/N)"))
    resposta = escolha.lower()
    if resposta == "N":
        escolha == False
    else:
        escolha == True
