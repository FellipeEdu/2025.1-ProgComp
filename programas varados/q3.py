import sys, random, statistics

try:
    elementos = int(input('Digite o valor de N elementos: '))
    if elementos < 1:
        sys.exit('\nERRO: informe um valor positivo e maior que 0.')

except ValueError:
    sys.exit('\nERRO: informe um valor inteiro válido.')

except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')

else:
    media = 0
    mediana = 0 
    somaMedias = 0
    variancia = 0
    lstNumeros = [random.randint(0, 99) for _ in range(elementos)]
    lstNumeros.sort()

    print(lstNumeros)

    for numero in lstNumeros: media += numero
    media = media / len(lstNumeros)
    
    # mediana 
    if len(lstNumeros) % 2 == 0: mediana = (lstNumeros[(len(lstNumeros) // 2) - 1] + lstNumeros[(len(lstNumeros) // 2)]) / 2
    else: mediana = lstNumeros[(len(lstNumeros) // 2)]

    # variancia e desvio
    lstVariancia = [(num - media) ** 2 for num in lstNumeros]
    for numero in lstVariancia: somaMedias += numero
    variancia = somaMedias / len(lstVariancia)
    desvioPadrao = variancia ** (1/2)

    print(f'Média = {media:.1f}; Mediana = {mediana}; Variância Populacional = {variancia}; Desvio Padrão = {desvioPadrao}')
    print(f'variancia = {statistics.pvariance(lstNumeros)}')