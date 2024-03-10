print("Vamos calcular seu IMC\n\n")

peso = float(input("Qual o seu peso atual? "))
altura = float(input("\nQual a sua altura? "))

IMC = peso / altura**2

if IMC > 25:
    print("Você está em estado de Sobrepeso")
else:
    print("você está bem com seu peso atual")
