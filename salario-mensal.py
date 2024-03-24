print("Vamos ajudar a calcular o seu salário mensal!")

horas_trab = int(input("Qual a sua quantidade de horas trabalhadas no mês? "))
valor_hora = float(input("\nQual seria o valor da sua hora trabalhada? "))
percen_desc = int(input("\nQuanto foi o seu percentual de desconto no mês? "))

salario_bruto = horas_trab * valor_hora
total_desc = (percen_desc * salario_bruto)/100
salario_liquido = salario_bruto - total_desc

print(f'\nO senhor possui salário bruto de {salario_bruto}.')
print(f'\nE como o senhor possui um total de desconto igual a {total_desc}')
print(f'\n Então seu Slário final será igual a {salario_liquido}')
