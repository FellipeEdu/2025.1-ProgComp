import sys

dist = int(input('distancia entre cidades (km): ')) # ex 140
if dist <= 0:
    sys.exit('informe distancia positiva')

Vo = int(input('vel inicial (km/h): ')) # ex 50
if Vo <= 0:
    sys.exit('informe vel inicial positiva')

'''acel = int(input('aceleração (m/s²): ')) # 5
if acel <= 0:
    sys.exit('informe aceleração positiva')'''

dist *= 1000 # 140000
Vo /= 3.6 # 14

'''delta = int(Vo ** 2 - 4 * acel * dist) # 
if delta < 0:
    sys.exit('não é possivel calcular o tempo')'''

# t = (-Vo + delta ** 0.5)/(2 * acel) # ** 0.5 = raiz quadrada
t = dist / Vo # 2,7778

hora = t // 3600    # estudar isso a partir daq. Essa linha transforma a hora decimal em hora inteira (2,7778h -> 2h)
t = t % 3600        # Aqui vai pegar 
minuto = t // 60    # 
segundo = t % 60

print(f'tempo restante: {hora:.0f}h:{minuto:.0f}m:{segundo:.0f}s')