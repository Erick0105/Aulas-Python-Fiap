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


#Cadastrar
def cadastro( cadastros_realizados ):
    contato = {}
    i = cadastros_realizados
    i = i + 1


    contato["nome"] = input("Digite aqui o seu nome\n=>")
    contato["email"] = input("Agora digite seu e-mail\n=>")
    contato["tele"] = input("E qual é o seu telefone?\n=>")
    contato["peso"] = float(input("Qual é o seu peso?\n=>"))
    contato["idade"] = int(input("E por ultimo qual a sua idade?\n=>"))
    contato["id"] = f'{i}'

    return contato




#Procurar
def procurar( lista_contatos ):
    id_desejado = input("Qual o id da conta que deseja procurar?\n=>")
    print(id_desejado)
    print(lista_contatos)

    valor_boolean = id_desejado in lista_contatos
    if valor_boolean == True:
        print(f'Os dados desta conta são {lista_contatos[id_desejado]}')
    else:
        print("E-mail não encontrado")

#Menu-Procurar
def menu_procurar():
    sub_menu = ("""
                -----------------------------------
                [1] - Alterar as informações
                [2] - Excluir as informações
                [3] - Retornar ao menu principal
                -----------------------------------""")
    print(sub_menu)
    resposta = input("O que o senhor deseja fazer dentre estas opções?\n=>")



#funcionalidade
qnt_cadastros = 0
repetir = True
contatos = contatos_gerais_por_id = {}

while repetir == True:
    decisao = menu_principal()

    if decisao == 1:
        informacoes = cadastro(qnt_cadastros)
        qnt_cadastros = qnt_cadastros + 1
        contatos[f'{qnt_cadastros}'] = informacoes
        print(contatos)
        
    #elif decisao == 2:

    elif decisao == 3:
        procurar(contatos)
        menu_procurar()

    #elif decisao == 4:

    #elif decisao == 5:

    elif decisao == 6:
        repetir = False


print("Programa encerrado")