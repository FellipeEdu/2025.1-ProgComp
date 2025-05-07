import sys

dist = int(input('distancia entre cidades (km): '))
if dist <= 0:
    sys.exit('informe distancia positiva')

Vo = int(input('vel inicial (km/h): '))
if Vo <= 0:
    sys.exit('informe vel inicial positiva')

acel = int(input('aceleração (m/s²): '))
if acel <= 0:
    sys.exit('informe aceleração positiva')

dist *= 1000
Vo /= 3.6

delta = int(Vo ** 2 - 4 * acel * dist)
if delta < 0:
    sys.exit('não é possivel calcular o tempo')

t = (-Vo + delta ** 0.5)/(2 * acel) # ** 0.5 = raiz quadrada

hora = t // 3600
t = t % 3600
minuto = t // 60
segundo = t % 60

print(f'tempo restante: {hora}:{minuto}:{segundo}')