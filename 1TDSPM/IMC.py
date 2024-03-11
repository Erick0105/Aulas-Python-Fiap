print("Vamos calcular seu IMC\n\n")

peso = int(input("Qual o seu peso atual? "))
altura = int(input("\nQual a sua altura em centimetros? "))

IMC = peso / altura**2

if IMC > 25:
    print("Você está em estado de Sobrepeso")
else:
    print("você está bem com seu peso atual")
