lista = ["João", "Maria", "Pedro"]
print(f'Lista original {lista}')

lista.append("José")
print(f'Lista com José {lista}')
tamanho = len(lista)
print("Tamanho ", tamanho)

lista.insert(1, "Matheus")
tamanho = len(lista)
print(f'Lista com Matheus {lista}')
print("Tamanho ", tamanho)

nome = lista.pop(2)
print(f'Lista sem a Maria : {lista}')

lista.insert(1, "Pedro")
pedros = lista.count("Pedro")
print(f"Há {pedros} Pedros na lista")
print("Tamanho: ", tamanho)
 
lista.remove("Pedro")
tamanho = len(lista)
print("Lista sem Pedro: ", lista)
print("Tamanho: ", tamanho)
