
def pedir_num(text):
    Texto = text

    valido = False

    while valido == False:
        digitado = input(Texto)

        try:
            digitado = float(digitado)
            valido = True
        except:
            print("Digite um valor que seja um número")
    return digitado
        

n1 = pedir_num("Me mande um número por favor\n==>")
n2 = pedir_num("Me passa outro número agora\n==>")
soma = n1 + n2

print(f'A soma destes dois números é igual a {soma}')
