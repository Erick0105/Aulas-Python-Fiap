listaNum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

transformaQuadrado = lambda num : num**2

#map funciona igual no js
listaTransformada = list(map( transformaQuadrado, listaNum))

print(f'Lista normal: {listaNum}')
print(f'Lista transformada: {listaTransformada}')