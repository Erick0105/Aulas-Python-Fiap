opcao = int(input("Insira uma opção de 1 a 5"))
i = 0

match opcao:
    case 1 : i += 1
    case 2 : i += 2
    case 3 : i += 3
    case 4 : i += 4
    case 5 : i += 5

print(i)