#Cadastrar
contatos = []
contato1 = {}

contato1["nome"] = input("Digite aqui o seu nome\n=>")
contato1["email"] = input("Agora digite seu e-mail\n=>")
contato1["tele"] = input("E qual séria o seu telefone?\n=>")
contato1["peso"] = float(input("QUal é o seu peso?\n=>"))
contato1["idade"] = int(input("E por ultimo qual a sua idade?\n=>"))
contatos.append(contato1)


#Menu
menu = ("""---------------------------------------- +
        \nBEM VINDO + 
        \n\n Essas são as funções que temos dísponivel no momento
        \n[1] - Cadastrar 
        \n[2] - Listar 
        \n[3] - Procurar
        \n[4] - Backup em um arquivo
        \n[5] - Restaurar de um arquivo
        \n[6] - Sair 
        \n----------------------------------------""")
print(menu)
decisao = int(input("\Digite o valor equivalente a função desejada por favor"))

print("Programa encerrado")

