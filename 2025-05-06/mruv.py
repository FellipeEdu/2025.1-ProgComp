import sys

Vo = int(input('vel inicial: '))
if Vo <= 0 :
    sys.exit('informe uma velocidade positiva')

tempo = int(input('tempo: '))
if tempo <= 0 :
    sys.exit('informe um intervalo de tempo positivo')

acel = int(input('aceleração: '))
if acel <= 0 :
    sys.exit('informe uma aceleração positiva')
    
dist = Vo * tempo + ((acel * (tempo ** 2)) / 2)

print(f'distancia percorrida: {dist}')