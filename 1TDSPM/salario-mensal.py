print("Vamos ajudar a calcular o seu salário mensal!")

horas_trab = int(input("Qual a sua quantidade de horas trabalhadas no mês?"))
valor_hora = float(input("Qual seria o valor da sua hora trabalhada?"))
percen_desc = int(input("Quanto foi o seu percentual de desconto no mês?"))

salario_bruto = horas_trab * valor_hora
total_desc = (percen_desc * salario_bruto)/100
salario_liquido = salario_bruto - total_desc
