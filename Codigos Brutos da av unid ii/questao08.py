import sys

letrasValidas = 'UDRLONEW'
coordInicialX = int(input('Digite a coordenada X: '))
coordInicialY = int(input('Digite a coordenada Y: '))
coordFinalX = 0
coordFinalY = 0
movValidos = 0
strMovValidos = ''
quadranteIni = ''
quadranteFin = ''

print('Direções válidas: U (cima); D (baixo);')
print('................. L (esquerda); R (direita)')
print('................. O (noroeste); N (nordeste)')
print('................. E (sudeste); W (sudoeste)\n')

try:
    movimentos = input('Digite as direções: ').upper()

except ValueError:
    sys.exit('ERRO: digite um valor válido.')

except Exception as excecao:
    sys.exit(f'ERRO: {excecao}')

else:
    # mapeamento
    for direcao in movimentos:
        if direcao == 'U':
            coordFinalY += 1

        elif direcao == 'D':
            coordFinalY -= 1

        elif direcao == 'L':
            coordFinalX -= 1

        elif direcao == 'R':
            coordFinalX -= 1
            
        elif direcao == 'O':
            coordFinalY += 1
            coordFinalX -= 1

        elif direcao == 'N':
            coordFinalY += 1
            coordFinalX += 1

        elif direcao == 'E':
            coordFinalY -= 1
            coordFinalX += 1

        elif direcao == 'W':
            coordFinalY -= 1
            coordFinalX -= 1
        else:
            movValidos -= 1 # subtrai 1 movimento valido pra somar 1 ao final do FOR, deixando a quantidade de movimentos validos inalterada

        strMovValidos += f'({coordFinalX}, {coordFinalY}) '
        movValidos += 1

    if coordInicialX > 0 and coordInicialY > 0:
        quadranteIni = 1
    elif coordInicialX < 0 and coordInicialY > 0:
        quadranteIni = 2
    elif coordInicialX < 0 and coordInicialY < 0:
        quadranteIni = 3
    elif coordInicialX > 0 and coordInicialY < 0:
        quadranteIni = 4
    else:
        quadranteIni = 'Origem'

    if coordFinalX > 0 and coordFinalY > 0:
        quadranteFin = 1
    elif coordFinalX < 0 and coordFinalY > 0:
        quadranteFin = 2
    elif coordFinalX < 0 and coordFinalY < 0:
        quadranteFin = 3
    elif coordFinalX > 0 and coordFinalY < 0:
        quadranteFin = 4
    else:
        quadranteFin = 'Origem' 

    print(f'\nPOSIÇÃO INICIAL: ({coordInicialX}, {coordInicialY})')
    print(f'POSIÇÃO FINAL: ({coordFinalX}, {coordFinalY})')
    print(f'MOVIMENTOS VÁLIDOS: {movValidos}')
    print(f'MOVIMENTOS: {strMovValidos}')
    print(f'QUADRANTE INICIAL: {quadranteIni}')
    print(f'QUADRANTE FINAL: {quadranteFin}')