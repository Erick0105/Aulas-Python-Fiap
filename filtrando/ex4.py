 #* Selecione as vendas que são superiores a um valor mínimo de 100 e depois aplique um desconto de 10%
listaVendas = [120,80,150,90,200]

#? Parte que seleciona as vendas que tem um valor mínimo de 100
selecaoVendas = lambda venda: venda >= 100
vendasSelecionadas = list(filter(selecaoVendas,listaVendas))

#? Parte que aplica um desconto de 10% nas vendas selecionadas
aplicarDesconto = lambda venda: venda-(venda * 0.1)
vendasFinais = list(map(aplicarDesconto, vendasSelecionadas))

i=0
for valoresFinais in vendasFinais:
    i+=1
    print(f'Preço da {i}º venda de R${valoresFinais}')