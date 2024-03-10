print("\nVamos descobrir os valores de ambos os X desta equação para você")

a_valor = int(input("\nQual o valor de 'a'?(O valor que acompanha o X²) "))
b_valor = int(input("\nQual o valor de 'b'?(O valor que acompanha o X) "))
c_valor = int(input("\nE qual o valor de 'c'?(O valor sozinho.) "))

delta = b_valor ** 2 - 4*a_valor*c_valor
x1 = (-b_valor + delta**0.5)/2*a_valor
x2 = (-b_valor - delta**0.5)/2*a_valor

if delta == 0:
    print(
        f'\nEssa questão possui o delta igual a 0 então só possui uma raiz que é igual {x1}')
elif delta < 0:
    print(f'\nO resultado do delta é menor que zero então essa equação não tem resposta dentro dos conjuntos dos Reais.')
else:
    print(f'\nOs valores do x¹ e X² é correspondentemente {x1} e {x2}')
