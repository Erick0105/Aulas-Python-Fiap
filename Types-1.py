resposta = input("Vocês lembra todos os 7 tipos de váriaveis?\n(S/N)")
resposta = str(resposta)


if resposta != "S" and resposta != "N" and resposta != "s" and resposta != "n":
    print ("!!ERROR!!\nDígite uma resposta válida")
if resposta == "S" or resposta == "s":
    print("Muito bem, qualquer dúvida sobre qualquer váriavel volte aqui.\n")

while resposta == "N" or resposta == "n":

    resposta = input("\nSe lembra como é uma string(str)?\n(S/N)")
    if resposta != "S" and resposta != "N" and resposta != "s" and resposta != "n":
        print("!!!!ERROR!!!! \n Digite uma resposta valida da proxima vez")
    if resposta == "N" or resposta == "n":
        text = "Palavras ou letras"
        print(f'"{text}", é um exemplo de uma váriavel string')
        print(type(text))
    else:
        print("Otimo, volte caso necessario.")
    
    resposta = input("\nSe lembra como é um inteiro(int)?\n(S/N)")
    if resposta != "S" and resposta != "N" and resposta != "s" and resposta != "n":
        print ("!!ERROR!!\nDígite uma resposta válida na proxima vez")
    elif resposta == "N" or resposta == "n": 
        numero_int = 27
        print(f"{numero_int}, é um exemplo de váriavel inteira")
        print(type(numero_int))
    else:
        print("Otimo, volte caso necessario.")
    
    resposta = input("\nSe lembra como é um decimal(float)?\n(S/N)")
    if resposta != "S" and resposta != "N" and resposta != "s" and resposta != "n":
       print ("!!ERROR!!\nDígite uma resposta válida na proxima vez")
    elif resposta == "N" or resposta == "n": 
        numero_dec = 0.5
        print(f"{numero_dec}, é um exemplo de váriavel decimal")
        print(type(numero_dec))
    else:
        print("Otimo, volte caso necessario.")
    
    resposta = input("\nSe lembra como é uma Boolean(bool)?\n(S/N)")
    if resposta != "S" and resposta != "N" and resposta != "s" and resposta != "n":
        print ("!!ERROR!!\nDígite uma resposta válida na proxima vez")
    elif resposta == "N" or resposta == "n": 
        v_f = True
        f_v = False
        print(f"{v_f} ou {f_v}, são váriaveis booleanas")
        print(type(v_f))
    else:
        print("Otimo, volte caso necessario.")
    
    resposta = input("\nSe lembra como são Listas(list)?\n(S/N)")
    if resposta != "S" and resposta != "N" and resposta != "s" and resposta != "n":
        print ("!!ERROR!!\nDígite uma resposta válida na proxima vez")
    elif resposta == "N" or resposta == "n": 
        lista = ['Erick', 17, True, "Carne", 198.05, "Se perdeu quantas vezes lendo esse codigo?", 190928]
        print(f"{lista}, é um exemplo de uma váriavel do tipo lista")
        print(type(lista))
    else:
        print("Otimo, volte caso necessario.")

    resposta = input("\nSe lembra como são Dicionários(dict)?\n(S/N)")
    if resposta != "S" and resposta != "N" and resposta != "s" and resposta != "n":
        print ("!!ERROR!!\nDígite uma resposta válida na proxima vez")
    elif resposta == "N" or resposta == "n": 
        idade = {'Erick' : 17, 'Rafael': 17, 'Luana': 17}
        print(f"{idade}, é um exemplo de uma váriavel do tipo dicionário")
        print(type(idade))
    else:
        print("Otimo, volte caso necessario.")  

    resposta = input("Deseja refazer esse progama? \n(S/N)") 
    if resposta == "S" or resposta == "s":
        resposta = "N"
    else:
        resposta = "S"
        print("Muito Bem, qualquer dúvida contate o dono deste código ;)")
