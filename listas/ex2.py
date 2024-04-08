lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tamanho = len(lista)
lista_final = []

for i in range(tamanho):
    if lista[i] % 3 != 0:
        lista_final.append(lista[i])
    else:
        print(f'O valor {lista[i]}  é divisivel por 3')

print(lista_final)
