# Mandar no Teams
listaNum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

def dividindo (numero):
    if numero % 3 == 0 or numero % 4 == 0:
        return True
    else:
        return False
    
novaLista = list(filter(dividindo,listaNum))

print(novaLista)