Vo = int(input('vel inicial: '))
tempo = int(input('tempo: '))
acel = int(input('aceleração: '))

dist = Vo * tempo + ((acel * (tempo ** 2)) / 2)

print(f'distancia percorrida: {dist:.2f}')