Vo = int(input('vel inicial (): '))
tempo = int(input('tempo (): '))
acel = int(input('aceleração (m/s2): '))
dist = int(input('distancia entre cidades (km): '))

tempo_viagem = ((acel * (tempo ** 2)) / 2) + Vo * tempo - dist

print