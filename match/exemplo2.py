lista_nomes = ["Ola","João", "Maria", "Jose", "Sara"]


match lista_nomes:
    case [cumprimento, *pessoa]:
        for nome in pessoa:
            print(cumprimento, nome)