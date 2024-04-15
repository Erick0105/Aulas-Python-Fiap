d1 = {
    "alunos": 40,
    "professor": "Antonio",
    "computadores": 43,
    "cadeiras": 43,
    "monitores": 43,
    "perifericos": {"computadores": 43, "monitores": 43}
}
d1["sala_aula"] = 201
# print(d1)
if "sala_aula" in d1:
    print("Existe a chave 'sala_aula' no dicionario")
else:
    print("Não existe a chave 'sala_aula' no dicionario")

#tamanho = len(d1.keys)
#for i in range(tamanho):
#    chave = d1.keys[i]
#    print(chave)

for chave in d1.keys():
    print(chave, "==> ", d1[chave])