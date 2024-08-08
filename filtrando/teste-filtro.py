listaNum = [1,2,3,4,5,6,7,8,9,10]


def filtrar (listaNumeros, opcaoParImpar = "par"):
    listaPar = []  
    listaImpar = []
    for numero in listaNumeros:
        if numero % 2 == 0:
            listaPar.append(numero)
        else:
            listaImpar.append(numero)
    if opcaoParImpar[0].lower() == "p":
        return listaPar
    else:
        return listaImpar

def exponenciacaoLista (lista, exponente = 2):
    listaRetorno = []
    for numero in lista:
        listaRetorno.append(numero ** 2)
    return listaRetorno

listaImpares = filtrar(listaNum, "impar")
print(exponenciacaoLista(listaImpares))


