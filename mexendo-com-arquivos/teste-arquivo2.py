
nome1 = input("Digite um nome\n==> ")
nome2 = input("Digite outro nome\n==> ")
nome3 = input("fale mais um nome\n==> ")

arq1 = open("./conjunto.txt", "w", encoding="utf-8")
arq1.write(f'{nome1}\n{nome2}\n{nome3}')