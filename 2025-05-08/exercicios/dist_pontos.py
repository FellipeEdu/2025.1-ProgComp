import math

pontoXa = float(input('digite a coordenada X do ponto A: '))
pontoYa = float(input('digite a coordenada Y do ponto A: '))

pontoXb = float(input('digite a coordenada X do ponto B: '))
pontoYb = float(input('digite a coordenada Y do ponto B: '))

dist = math.sqrt(math.pow(pontoXa - pontoXb, 2) + math.pow(pontoYa - pontoYb, 2))

print(f'Distancia entre o pontos A({pontoXa},{pontoYa}) e B({pontoXb},{pontoYb}) é {dist:.2f}')