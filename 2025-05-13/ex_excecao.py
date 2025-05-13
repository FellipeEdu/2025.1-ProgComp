'''try:
    intNum = int(input('Digite algo:'))
except:
    print('valor invalido')
else:
    print(intNum)
'''
import sys

try:
    intDividendo = int(input('Digite o dividendo:'))
    intDivisor = int(input('Digite o dividendo:'))
    floatResultado = intDividendo / intDivisor
except ValueError:
    print('ERRO: informe um valor que possa ser convertido em inteiro')
except Exception as tipoExcecao:
    print(f'valor invalido')
    print(f'ERRO: {tipoExcecao}')
    print(f'ERRO: {sys.exc_info()}')
else:
    print(floatResultado)