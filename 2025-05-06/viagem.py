import sys

dist = int(input('distancia entre cidades (km): '))
if dist <= 0:
    sys.exit('informe distancia positiva')
#tempo_decorrido = int(input('tempo (): '))

Vo = int(input('vel inicial (km/h): '))
if Vo <= 0:
    sys.exit('informe vel inicial positiva')

acel = int(input('aceleração (m/s²): '))
if acel <= 0:
    sys.exit('informe aceleração positiva')

#tempo_viagem = ((acel * (tempo_decorrido ** 2)) / 2) + Vo * tempo_decorrido - dist

dist *= 1000
Vo /= 3.6

delta = int(Vo ** 2 - 4 * acel * dist)
if delta < 0:
    sys.exit('não é possivel calcular')

print(f'')