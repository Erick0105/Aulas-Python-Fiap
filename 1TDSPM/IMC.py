print("Programa para calcular seu IMC\n\n")

peso = int(input("Qual o seu peso atual? "))
altura = float(input("\nQual a sua altura em centimetros? "))

IMC = peso / altura**2

if IMC > 25:
    print("\nVocê está em estado de Sobrepeso")
elif IMC <= 18.4:
    print("\nVocê está em estado de magreza tome cuidado com sua saúde")
else:
    print("\nvocê está bem com seu peso atual")
