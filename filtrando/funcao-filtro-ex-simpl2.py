# Mandar no Teams
listaNum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]


filtro = lambda numero : numero % 3 == 0 or numero % 4 == 0
    
print("Teste do filtro com número 16: ", filtro(10))


novaLista = list(filter(filtro,listaNum))
print(novaLista)