from modelo import Funcionario
from repositorio import Repositorio

class Apresentacao:
    def __init__(self):
        
        self.acesso_db = Repositorio()
        lista = []    
        
    def cadastrar(self):
        print("-"*20 + "CADASTRO" + "-"*20)
        repetir = True:
        while repetir == True:
            try:
                nome = input("Qual o nome do funcionario?")
                matricula = int(input("Qual o número da matricula do funcionario?"))
                salario = float(input("Qual o salario do funcionario?"))
                if nome == "":
                    repetir = True
                if matricula == 0:
                    repetir = True
                
                # Deixei possivel o salario ser vazio porque o funcionario pode não estar trabalhando no momento ou algo do tipo
                    
                repetir = False
                
            except:
                print("Preencha os dados de maneira correta")
                repetir = True
        
        contratado = Funcionario(matricula, nome, salario)

        resultado = self.acesso_db.gravar(contratado)
        if resultado = True:
            print("Funcionario cadastrado com sucesso")
        else:
            print("Aconteceu um problema ao cadastrar o funcionario")
        
        return True
    
    def pesquisar(self):
        print("-"*20 + "PESQUISAR" + "-"*20)
        alvo = input("Qual o nome do funcionario que você deseja pesquisar?")

        self.lista.clear()
        self.lista = self.acesso_db.pesquisar(alvo)

        for pessoa in self.lista:
            print("-"*5 + "\nMatricula: {pessoa.matricula}\nNome: {pessoa.nome}\nSalario: {pessoa.salario}")
            
        return True

    
    
    def menu_principal(self):
        menu = 
        "-"* 20 + "MENU-PRINCIPAL" + "-" * 20 + 
        "\n[1] - Cadastrar" +
        "\n[2] - Pesquisar" +
        "\n[3] - Sair" +
        "-"* 20 + "MENU-PRINCIPAL" + "-" * 20 
        
        msg_op = "Digite o número correspondente a opção desejada"
        
        repetir = True
        while repetir == True:
            try:    
                opcao = int(input(msg_op))
                if opcao in [1,2,3]:
                    repetir = False
                else:
                    repetir = True
            except:
                msg_op = "Erro, Digite um número entre 1 a 3 dentre as opções"
                repetir = True
        
        if opcao == 1:
            self.cadastrar()
            
        if opcao == 2:
            self.pesquisar()
            
        else:
            print("Programa Finalizado")
            return True
        
crud = Apresentação()
print(crud)