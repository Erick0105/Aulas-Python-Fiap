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

    
print(filtrar(listaNum,"impar"))


