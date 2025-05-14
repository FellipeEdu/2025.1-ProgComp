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
except ValueError:  # exceção expecifica, nesse caso, de valor
    print('ERRO: informe um valor que possa ser convertido em inteiro')
except ZeroDivisionError:
    print('ERRO: não existe divisão por zero')
except: # as tipoExcecao:  # passando a informação da exceção pra uma variavel
    print(f'ERRO: {sys.exc_info()}')    
else:
    print(floatResultado)

#teste dnv