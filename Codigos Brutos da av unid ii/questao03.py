import sys

try:
    numero = int(input('Digite um número: '))

    if numero <= 0:
        sys.exit('ERRO: o valor do número deve ser positivo.')

except ValueError:
    print('ERRO: digite um valor válido.')

except Exception as excecao:
    print(f'ERRO: {excecao}')

else:
    numeroTeste = 1
    numeroTriangular = 0
    triangular = False

    while numeroTriangular < numero:

        numeroTriangular = int((numeroTeste * (numeroTeste + 1)) / 2)

        if numeroTriangular == numero:
            print(f'{numero} é um número triangular.')
            triangular = True

        numeroTeste += 1
    
    if triangular == False:
        print(f'{numero} não é um número triangular.')