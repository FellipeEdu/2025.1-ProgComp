import sys

try:
    strNumero_1 = input('Digite o 1° número binario: ')
    strNumero_2 = input('Digite o 2° número binario: ')

    if strNumero_1.count('-') > 0 or strNumero_2.count('-') > 0:
        sys.exit('ERRO: o número deve ser binário e positivo.')

    if len(strNumero_1) != len(strNumero_2):
        sys.exit('ERRO: os dois numeros devem ter tamanhos iguais.')

    numerosInvalidos = '23456789'

    for num in strNumero_1:
        if num in numerosInvalidos:
            sys.exit('ERRO: os números devem ser binários.')

    for num in strNumero_2:
        if num in numerosInvalidos:
            sys.exit('ERRO: os números devem ser binários.')

except ValueError:
    print('ERRO: digite um valor válido.')

except Exception as excecao:
    print(f'ERRO: {excecao}')

else:
    #AND
    print(f'AND ({strNumero_1} | {strNumero_2}): ', end='')

    indiceAnd = 0
    for numAnd in strNumero_1:

        if numAnd == '1' and strNumero_2[indiceAnd] == '1':
            print(1, end=' ')
        else:
            print(0, end=' ')

        indiceAnd += 1
    print()

    #OR
    print(f'OR ({strNumero_1} | {strNumero_2}): ', end='')

    indiceOR = 0
    for numAnd in strNumero_1:

        if numAnd == '0' and strNumero_2[indiceOR] == '0':
            print(0, end=' ')
        else:
            print(1, end=' ')

        indiceOR += 1
    print()

    #XOR
    print(f'XOR ({strNumero_1} | {strNumero_2}): ', end='')

    indiceXor = 0
    for numAnd in strNumero_1:

        if (numAnd == '0' and strNumero_2[indiceXor] == '0') or (numAnd == '1' and strNumero_2[indiceXor] == '1'):
            print(0, end=' ')
        else:
            print(1, end=' ')

        indiceXor += 1