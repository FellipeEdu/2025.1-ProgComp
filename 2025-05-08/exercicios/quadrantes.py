import sys

pontoX = int(input('digite a coordenada X:'))
pontoY = int(input('digite a coordenada Y:'))

if pontoX > 0 and pontoY > 0:
    print(f'O ponto ({pontoX},{pontoY}) pertence ao 1° quadrante.')
elif pontoX < 0 and pontoY > 0:
    print(f'O ponto ({pontoX},{pontoY}) pertence ao 2° quadrante.')
elif pontoX < 0 and pontoY < 0:
    print(f'O ponto ({pontoX},{pontoY}) pertence ao 3° quadrante.')
elif pontoX > 0 and pontoY < 0:
    print(f'O ponto ({pontoX},{pontoY}) pertence ao 4° quadrante.')
else:
    print(f'O ponto ({pontoX},{pontoY}) é origem do plano ou está nos eixos coordenados')