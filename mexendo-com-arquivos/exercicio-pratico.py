#Cadastrar
def cadastro():
    contato = {}

    contato["nome"] = input("Digite aqui o seu nome\n=>")
    contato["email"] = input("Agora digite seu e-mail\n=>")
    contato["tele"] = input("E qual séria o seu telefone?\n=>")
    contato["peso"] = float(input("QUal é o seu peso?\n=>"))
    contato["idade"] = int(input("E por ultimo qual a sua idade?\n=>"))
    return contato


#Menu
def menu_principal():
    menu = ("""----------------------------------------
                             BEM VINDO 
            Essas são as funções que temos dísponivel no momento
            [1] - Cadastrar 
            [2] - Listar 
            [3] - Procurar
            [4] - Backup em um arquivo
            [5] - Restaurar de um arquivo
            [6] - Sair 
            ----------------------------------------""")
    print(menu)
    return int(input("Digite o valor equivalente a função desejada por favor\n=>"))


#Procurar
def procurar( lista_contatos ):
    email_desejado = input("Qual o e-mail da conta que deseja procurar?\n=>")

    if email_desejado == lista_contatos[0]["email"]:
        print(f'Os dados desta conta são {lista_contatos[0]}')
    else:
        print("E-mail não encontrado")

#Sub-menu-Procurar
def sub_menu_procurar():
    sub_menu = ("""[1] - Alterar
    [2] - Excluir
    [3] - Retornar ao menu principal""")
    print(sub_menu)

#funcionalidade

repetir = True
while repetir == True:
    decisao = menu_principal()

    if decisao == 1:
        contatos_gerais = cadastro()
    #elif decisao == 2:

    elif decisao == 3:
        procurar(contatos_gerais)

    #elif decisao == 4:

    #elif decisao == 5:

    elif decisao == 6:
        repetir = False


print("Programa encerrado")