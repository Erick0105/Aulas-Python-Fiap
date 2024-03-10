print("Vamos descobrir os valores de ambos os X desta equação para você")

a_valor = int(input("Qual o valor de 'a'?(O valor que acompanha o X²) "))
b_valor = int(input("\nQual o valor de 'b'?(O valor que acompanha o X) "))
c_valor = int(input("\nE qual o valor de 'c'?(O valor sozinho.) "))

delta = b_valor ** 2 - 4*a_valor*c_valor
x1 = (-b_valor + delta**0.5)/2*a_valor
x2 = (-b_valor - delta**0.5)/2*a_valor
