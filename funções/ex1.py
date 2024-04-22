def pedir_num(text = "Digite um número" ):
    Texto = text
    """
    Função utilizada para pedir números
    e verifica se o valor digitado é um número mesmo
    """

    valido = False

    while valido == False:
        digitado = input(Texto)

        try:
            num = float(digitado)
            valido = True

        except:
            print("Digite um valor que seja um número")

    return num
        
def menu ():
    mensagem = ("----------------------------------\n" +
               "                 Menu\n\n" 
               + "Iremos calcular o valor da soma\nde duas váriaveis" 
               + "\n----------------------------------")
    print(mensagem)
    num1 = pedir_num("Me mande um número por favor\n==> ")
    num2 = pedir_num("Me passa outro número agora\n==> ")
    
    return num1, num2

#Funcionalidade
n1, n2 = menu()
soma = n1 + n2

print(f'A soma destes dois números é igual a {soma}')
