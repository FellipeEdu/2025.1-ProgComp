import sys

dist = int(input('distancia entre cidades (km): '))
if dist <= 0:
    sys.exit('informe distancia positiva')

dist *= 1000
#tempo_decorrido = int(input('tempo (): '))
Vo = int(input('vel inicial (km/h): '))
if Vo <= 0:
    sys.exit('informe vel inicial positiva')

acel = int(input('aceleração (m/s²): '))
if acel <= 0:
    sys.exit('informe aceleração positiva')

#tempo_viagem = ((acel * (tempo_decorrido ** 2)) / 2) + Vo * tempo_decorrido - dist

delta = int(Vo ** 2 - 4 * acel * dist)

print