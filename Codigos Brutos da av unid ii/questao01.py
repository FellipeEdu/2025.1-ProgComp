import sys

try:
    massaIni = float(input('Valor da massa (em g): '))

    if massaIni <= 0:
        sys.exit('ERRO: a massa deve ser maior que 0.')

except ValueError:
    print('ERRO: digite um valor válido.')

except Exception as excecao:
    print(f'ERRO: {excecao}')

else:
    tempoSeg = 0
    massaFinal = massaIni

    while massaFinal >= 0.5:
        massaFinal /= 2
        tempoSeg += 50

    print(f'Massa Inicial: {massaIni} g')
    print(f'Massa Final: {massaFinal:.8f} g')
    print(f'Tempo de decaimento: {(tempoSeg // 3600):02d}:{(tempoSeg // 60):02d}:{(tempoSeg % 60):02d}')