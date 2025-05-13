import math

pontoXa = int(input('digite a coordenada X do ponto A: '))
pontoYa = int(input('digite a coordenada Y do ponto A: '))
pontoXb = int(input('digite a coordenada X do ponto B: '))
pontoYb = int(input('digite a coordenada Y do ponto B: '))

dist = math.sqrt(math.pow(pontoXa - pontoXb, 2) + math.pow(pontoYa - pontoYb, 2))

print(f'Distancia entre o pontos A({pontoXa},{pontoYa}) e B({pontoXb},{pontoYb}) é {dist}')